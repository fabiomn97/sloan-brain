# Inbox

Drop anything here that should go into the brain, then run `python brain/convert.py`.

| Folder | What goes in it |
|---|---|
| `canvas/<course>/` | Course files the harvester couldn't get (see `raw/failed.csv`). Use the course number as the folder name, e.g. `canvas/15.010/`. |
| `transcripts/` | Coffee chats, meetings, interviews: `.txt` `.md` `.vtt` `.srt` `.docx` `.pdf` |
| `newsletters/` | Sloan newsletters: save the email as `.eml`, or as PDF/HTML |
| `notes/` | Your own notes, anything else. Subfolders become the "module" label. |

Start a file name with a date to date it: `2026-10-03 Coffee chat with Ana.txt`.

Files in this folder are not committed (they can be large); the Markdown that
`convert.py` makes from them is. Back this folder up to a personal drive.
