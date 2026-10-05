// Checks the Cloudflare Access gate in app/src/worker.js with self-signed test tokens.
// Run: node tests/test_access.mjs
import worker from '../app/src/worker.js';
const { subtle } = globalThis.crypto;
const kp = await subtle.generateKey({ name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1,0,1]), hash: 'SHA-256' }, true, ['sign','verify']);
const jwk = { ...(await subtle.exportKey('jwk', kp.publicKey)), kid: 'k1' };
const other = await subtle.generateKey({ name: 'RSASSA-PKCS1-v1_5', modulusLength: 2048, publicExponent: new Uint8Array([1,0,1]), hash: 'SHA-256' }, true, ['sign','verify']);
globalThis.fetch = async () => new Response(JSON.stringify({ keys: [jwk] }));
const b64 = o => Buffer.from(typeof o === 'string' ? o : JSON.stringify(o)).toString('base64url');
async function token(payload, key = kp.privateKey, kid = 'k1') {
  const h = b64({ alg: 'RS256', kid }), p = b64(payload);
  const sig = Buffer.from(await subtle.sign('RSASSA-PKCS1-v1_5', key, new TextEncoder().encode(`${h}.${p}`))).toString('base64url');
  return `${h}.${p}.${sig}`;
}
const env = { ACCESS_TEAM_DOMAIN: 'fabio.cloudflareaccess.com', ACCESS_AUD: 'aud123',
  ASSETS: { fetch: async () => new Response('page') }, DB: { prepare(){ return { bind(){return this}, all: async()=>({results:[]}) }; } } };
const now = Math.floor(Date.now()/1000);
const good = { aud: ['aud123'], iss: 'https://fabio.cloudflareaccess.com', exp: now + 600, email: 'me@x' };
const cases = [
  ['no token', null, 403],
  ['valid token header', await token(good), 200],
  ['valid token cookie', 'cookie:' + await token(good), 200],
  ['wrong audience', await token({ ...good, aud: ['other'] }), 403],
  ['wrong issuer', await token({ ...good, iss: 'https://evil.cloudflareaccess.com' }), 403],
  ['expired', await token({ ...good, exp: now - 5 }), 403],
  ['forged signature', await token(good, other.privateKey), 403],
  ['unknown kid', await token(good, kp.privateKey, 'k9'), 403],
  ['garbage', 'a.b.c', 403],
];
let failed = 0;
for (const [name, t, want] of cases) {
  const headers = {};
  if (t && t.startsWith('cookie:')) headers.cookie = 'x=1; CF_Authorization=' + t.slice(7);
  else if (t) headers['cf-access-jwt-assertion'] = t;
  const res = await worker.fetch(new Request('https://brain.fabio.cool/', { headers }), env, { waitUntil(){} });
  if (res.status !== want) failed++;
  console.log(res.status === want ? "PASS" : "FAIL", name, res.status);
}
const unconf = await worker.fetch(new Request('https://brain.fabio.cool/'), { ...env, ACCESS_AUD: '' }, {});
console.log(unconf.status === 403 ? 'PASS' : 'FAIL', 'fails closed when unconfigured', unconf.status);
if (unconf.status !== 403) failed++;
process.exit(failed ? 1 : 0);
