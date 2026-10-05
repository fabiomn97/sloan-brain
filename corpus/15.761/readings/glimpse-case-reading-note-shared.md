---
title: "Glimpse case reading note - shared"
course: "15.761"
course_name: "Introduction to Operations Management"
term: "Fall Term (AY 2026-2027)"
type: "reading"
date: "2026-05-28"
source: "canvas"
url: "https://canvas.mit.edu/courses/38556/files/6526051"
original: "raw/fall-term-ay-2026-2027/15.761/files/uploaded-media/glimpse-case-reading-note-shared.pdf"
locator_kind: "page"
---

## Page 1

A Glimpse into EV Battery Quality Control

Prepared by Ali Aouad and Eric Moch

Eric Moch is the CEO of Glimpse, a startup building a quality management software for battery cells. Before founding Glimpse in March 2023, Eric was a Program Manager at Tesla Inc., one of the world’s largest producers of Electric Vehicles (EVs). In his role, Eric realized that poor battery quality is a fundamental bottleneck to the electrification of the $5T transportation industry: “Producing battery cells1 at scale is incredibly complex: electrodes must be mixed, coated, and dried at speeds of up to 100 meters per minute while maintaining precision within a few microns (1/1000 of a millimeter). These electrodes are then assembled into battery cells at rates sometimes exceeding 100 parts per minute.” Insufficient quality control has led to major incidents such as ebikes catching on fire in apartments and billion-dollar EV recalls. In 2022, for example, GM recalled over 142,000 Chevy Bolt vehicles due to defective cells from LG Energy Solution. More recently, Samsung SDI, another major cell manufacturer, recalled 180,000 battery packs used in plug-in hybrid vehicles. Such recalls are so costly they can wipe out years of profit and significantly damage the reputations of both the cell producers and their customers, the OEMs (Original Equipment Manufacturers, in this case, EV makers).

Fig 1: Battery cells come in 3 major form factors: cylindrical (left), pouch (middle), and prismatic (right). These cells are assembled in battery packs. In a typical EV, a battery pack is made with a couple hundred to several thousand cells.

Eric saw that improving quality control technologies may be critical to mitigate these issues and enable a safe and profitable transition to electric mobility. Together with Peter Attia, whom he met at Tesla, and Patrick Herring (ex-Toyota), they founded Glimpse to deliver a more holistic quality control solution to the battery cell industry. By leveraging industrial X-ray computed tomography (CT) scanning - the industrial equivalent of CAT scanning used in the medical field! - Glimpse has developed a scalable, AI-powered technology capable of detecting microscopic internal defects in battery cells before they’re assembled into packs. By December 2024, Glimpse had successfully deployed its solution at several customers. But the Glimpse team faces critical questions ahead: How much are their customers willing to pay for their software? Were they pricing themselves out of deals, or undercharging and leaving money on the table? And how might the Glimpse team leverage AI to provide more value to their customers and scale up their solution?

1 Technical terms are deﬁned in the Glossary.

## Page 2

Electric vehicles and lithium-ion batteries: Brief industry landscape

The Electric Vehicle (EV) market has grown substantially since the early 2010s. The Tesla Model S achieved a 200+ mile range as early as 2012. In 2016, GM introduced the Chevy Bolt, an affordable, long-range EV widely available to consumers. Heightened public concern about greenhouse gas emissions, fluctuating fossil fuel prices, and government incentives - combined with more efficient battery manufacturing - have fueled rapid EV adoption. Global EV manufacturers such as BYD and Tesla invested heavily to expand production, and by 2021, most automakers like BMW, Honda, Stellantis, Ford, and Volvo also announced ambitious EV strategies. The total number of EVs on the road rose from roughly 17,000 in 2010 to over 40 million by 2024, with some forecasts projecting hundreds of millions - and potential sales dominance over traditional vehicles - by 2035 (IEA, Global 2024 outlook report).

Contrary to popular belief, EVs predated gasoline-powered cars. Electric taxis operated in London and New York City as early as 1897, offering greater comfort, reduced noise, and fewer odors than gasoline vehicles. Yet these advantages waned by the early 20th century, as mass production techniques like Fordism drove down the cost of gas-powered cars in ways EV makers could not match. Limited driving range also slowed EV adoption.

Modern EVs owe their resurgence in the 2000s largely to breakthroughs in battery chemistry. The lithium-ion (Li-ion) battery - pioneered in the 1970s by M. Stanley Whittingham - dominates today’s market. A battery cell comprises a negatively charged anode and a positively charged cathode. During discharge, ions flow from the anode to the cathode, reversing when charging. Because lithium is lightweight and highly reactive, Li-ion batteries can, in theory, store much more energy and charge faster than older lead-acid models. Early Li-ion designs faced safety challenges for decades, but key material innovations - like widespread graphite anodes in the 1990s and Nickel-Manganese-Cobalt (NMC) cathodes in the early 2000s - made modern batteries viable.

## Page 3

Whittingham, John B. Goodenough, and Akira Yoshino received the 2019 Nobel Prize for their foundational work on this technology.

A complex battery supply chain

Although battery costs have plummeted in the past decade, they remain the most expensive component of an EV, often accounting for 20% to 40% of total costs. Beyond cost considerations, batteries are also central to EV performance, determining range, charging speed, and vehicle lifetime.

As EV production has scaled, the battery supply chain has become increasingly complex. From raw material extraction and refining to cell manufacturing and pack assembly to recycling, the industry is shaped by volatile commodity prices, geopolitical tensions, and labor and environmental concerns. China sits at the heart of this landscape as the country refines more than half the world’s lithium, produces roughly 70% of global battery cells, and manufactures over half of all EVs worldwide. This prominent role gives China significant influence in shaping the future of battery production and electric mobility, an area where other countries are seeking to enhance their own capabilities2.

2 See, for example, https://www.spglobal.com/commodity-insights/en/news-research/latestnews/metals/092324-factbox-chinas-lithium-industry-eyes-output-cuts-to-shore-up-market-sentiment

## Page 4

Source: Department of Energy

Compared to established sectors like semiconductor manufacturing, the battery industry is still relatively young. This relative immaturity means there are no universally accepted quality benchmarks, creating a lack of transparency in the market. Each battery pack builder must devote substantial resources to testing, qualifying, and controlling the quality of the cells they buy. As the cell manufacturing complex grows larger and more concentrated, it becomes difficult for cell buyers to enforce rigorous quality controls. Eric notes: “In reality, car makers face significant financial and reputational risks when incorporating these cells into EVs sold to consumers. And when a battery pack fails after having been driven for a few thousand miles, it is very difficult and resource intensive for the EV maker to prove to its supplier that it did so due to a faulty cell.”

## Page 5

The challenge of ensuring battery cell quality at scale

What makes cell quality challenging is that a single defective cell can compromise the entire battery pack, which may contain several thousand cells.3 This challenge is further intensified by the pressure on manufacturers to maximize battery cell performance and production throughput, in order to extend driving range, reduce charging speed, and lower production costs.

Inside each cell, two electrodes - called the cathode (positive) and anode (negative) - are kept apart by a thin separator. An electrolyte solution allows lithium ions to move between these electrodes. During discharge (i.e., when the vehicle is driven), the ions flow from the anode to the cathode to create electrical power. When the car charges, that flow reverses.

A large share of EV field failures can be traced back to microscopic production flaws in battery cells that remain latent initially, much like an undetected medical condition. As Eric remarks, “Ensuring battery pack reliability is incredibly challenging. One minuscule defect in one cell can bring an entire pack down.” With repeated charging and discharging, these tiny defects can grow into functional failures or, in extreme cases, lead to what is known as a “thermal runaway.” These rare, high-impact failures cause the cells to heat up and lead to fires or explosions. Manufacturing defects can take various shapes and sizes. For instance, metal debris and burrs can cause a puncture of the separator and trigger a short circuit - an issue implicated in the Samsung Galaxy Note7 $5B recall. Another example is misalignment or folding of the cathode, anode, or separator layers - suspected as the root cause of the GM Chevy Bolt’s $2B recall. Often times, these production issues that occur on a manufacturing line produce waves of defective cells. If not caught in time, entire batches of defective cells can end up in battery-powered products sold to consumers.

Importance of quality management

To address consumer worries about battery longevity, most electric vehicle (EV) manufacturers offer warranties covering a substantial distance or a fixed number of years - often around 100,000 miles or eight years. For example, Tesla provides an eight-year warranty (with mileage limits that vary by model).4 These warranties place significant financial and reputational pressure on the industry, since automakers must replace or repair battery packs free of charge if they fail while under warranty.

When field failures or safety concerns arise, manufacturers may issue large-scale recalls, but those high-profile incidents represent just a fraction of actual failures. More commonly, drivers quietly receive notices to bring their vehicles in for pack replacement, often without media attention. A single battery pack replacement can cost automakers anywhere from $10,000 to $25,000. That figure doesn’t include the significant engineering resources required to diagnose and fix largescale production issues, the legal wrangling with suppliers to cover costs, and the potential damage to a brand’s reputation. Estimates suggest that around 1–2% of all EVs might need a pack

3 Zhao, J., Feng, X., Tran, M.K., Fowler, M., Ouyang, M. and Burke, A.F., 2024. Battery safety: Fault diagnosis from laboratory to real world. J. Power Sources, 598(234111), pp.10-1016. 4 See https://www.tesla.com/support/vehicle-warranty Accessed on 03/31/2025.

## Page 6

replacement over their lifetime.5 In many cases, these failures can be traced back to a single defective battery cell per vehicle.

The Glimpse solution: Defect detection via high-throughput cell CT scanning

To ensure battery cells meet strict quality standards, manufacturers employ a broad set of inspection methods ranging from high-speed cameras to ultrasound and electrical checks. “The problem with latent defects is that they don’t produce any electrochemical signature,” Eric emphasizes. “This means standard electrical testing fails at screening cells that contain these defects, and that’s why we end up with so many escapes [tldr: a quality issue that escapes the inspections and makes its way to the customer].”

Ideally an inspection solution should be:

- Nondestructive; - Capable of testing millions of cells a year; - Able to test the entire cell, since defects can reside in any part of the cell; - Able to achieve high precision (sub-50 micrometers of resolution) to detect electrode-level flaws; - Spatially resolved to identify the type and location of defects.

Computed tomography (CT) scanning, which uses X-ray to produce a high-resolution 3D map of an object, is widely recognized by the battery industry as a powerful characterization technique for battery cells.6 This imaging technique can inspect a full cell in 3D and at a sub-50um resolution, which other technology cannot match. However, CT scanning is considered merely a lab instrument because of its low throughput - typically hours per scan - and high cost - up to thousands of dollars per scan. Furthermore, typical workflows for reviewing CT scans are slow, manual, and require expensive hardware and software.

Glimpse’s key innovation is to scale-up CT scanning and deploy it as a high-throughput production quality control tool. In collaboration with CT scanner producers, Glimpse has re-engineered CT scanning’s hardware and software stack and was able to cut the scan time from hours to minutes. Eric notes: “We’re continuously working on reducing scan time. Our goal is to eventually unlock sub-second scans to fully match cell production throughputs.” Alongside faster scanning, Glimpse has developed data processing, AI-enabled feature extraction, and visualization capabilities to convert massive volumes of raw scan data – up to terabytes per minute - into concise, actionable insights. Glimpse’s customers can visualize these insights and

5 See https://www.energy.gov/eere/vehicles/articles/fotw-1339-april-22-2024-plug-electric-vehicle-batteryreplacements-due 6 See Attia, P.M., Moch, E. and Herring, P.K., 2025. Challenges and opportunities for high-quality battery production at scale. Nature Communications, 16(1), p.611.

## Page 7

control their cell quality through a web application, the Glimpse Portal®. Eric estimates that the Glimpse technology can identify roughly 80% of critical defects in each scanned cell.

The Glimpse Portal®, Glimpse’s scan visualization web-based interface. Control charts are built with measurements extracted from scans of battery cells.

Glimpse’s economics

Glimpse’s solution integrates with off-the-shelf CT scanners installed at customer factories. It serves both cell producers, who can deploy Glimpse for in-process quality control or at the end of the production line, and cell buyers, who want to perform incoming quality control on the cells they receive before pack assembly.

Currently, Glimpse can scan one battery cell in about one minute. The CT scanner itself, when equipped with automated cell loading and unloading and integrated into a factory, costs around $1 million and requires an annual maintenance budget equal to 5% of its purchase price. CT scanners have a lifespan of about 7 to 9 years and typically reach an Overall Equipment Effectiveness (OEE) of about 90%. Glimpse charges an annual subscription fee for its scan processing and defect detection software.

Although the company has significantly accelerated CT scanning, one cell per minute still represents well under 1% of a typical production line’s output—for reference, ‘Gigafactories’ produce hundreds of millions of cells per year. Glimpse’s customers use Glimpse’s solution on a production sample to capture a statistically relevant fingerprint of their build quality. “Our value proposition, and thus the size of our addressable market, scales with the scanning throughput we

## Page 8

can deliver,” explains Eric. “Today, scanning a cell per minute supports offline or at-line use cases. In the future, we want to scan every cell coming out of a production line to ensure full coverage.”

AI for better and faster scanning

As Glimpse moves into its next growth stage, increasing scan throughput is crucial. The team’s goal is to reduce scan times without sacrificing the detection accuracy of its defect detection algorithms. Real-world deployments can generate new data to improve Glimpse’s algorithms, allowing them to maintain the required level of performance even when scans are produced faster and, consequently, at lower image quality.

Illustration of how image quality deteriorates as scan time gets shorter.

Eric and his team acknowledge the complexity of this challenge. “How do we maintain or improve detection rates as we scale up our technology? And how do we control the risk of ‘hallucination’ as we push the envelope of our Computer Vision algorithms?” Achieving the goal of catching rare, high-risk defects with limited data aligns with broader “AI scaling laws,” which generally hold that model performance improves predictably when trained on larger, more diverse datasets. In Glimpse’s case, each additional scan from a customer site can bring new insights that strengthen the algorithm’s ability to spot anomalies and reduce the risk of errors. “We aim to enter into a virtuous cycle for our business: more deployments of our technology in factories yield more data, which leads to better algorithms, unlocking higher scanning throughput, increased value for customers, and, in turn, more deployments,” Eric envisions.

Ultimately, the capacity to successfully feed real-world data back into its technology, thereby increasing the throughput of its technology may well define Glimpse’s future. Better quality control could pave the way for safer, more affordable, and reliable EVs worldwide.

## Page 9

Glossary

   Battery cell: The basic energy-storage unit in a battery, converting chemical energy into electrical energy.

   Electrodes: Conductive materials within a battery cell that facilitate energy transfer through chemical reactions; includes anode and cathode.

   Anode: The battery cell electrode that releases electrons during discharge, typically negative in lithium-ion batteries.

   Cathode: The battery cell electrode that gains electrons during discharge, typically positive in lithium-ion batteries.

   Battery pack: An assembly of multiple battery cells arranged and packaged together to provide higher power and capacity.

   Escape: A quality issue that "escapes" the quality control and inspection processes and makes its way to the end customer.

   Overall Equipment Effectiveness: This roughly measures the percentage of scheduled time that the equipment is actually running and achieves satisfactory performance.

   Lithium-ion (Li-ion): Informal shorthand referring to lithium-ion technology, a type of rechargeable battery commonly used in electronics and electric vehicles (EVs).

   Computer Vision: An AI technology enabling machines to interpret and understand visual data, such as images and videos.

   Hallucination (AI): A phenomenon in which artificial intelligence systems generate plausiblesounding but incorrect or misleading information not grounded in actual data or reality.
