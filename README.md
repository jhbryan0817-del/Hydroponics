# Hydroponics floating controller - mechanical-first prototype

This repository defines the hardware and Fusion 360 inputs for a small battery-powered controller that floats on a hydroponic reservoir, samples pH and electrical conductivity (EC), displays the readings, and controls three concentrate dosing lines.

## Current design baseline

Revision 2 makes mechanical integration the first priority. The wet sensors are no longer treated as laboratory probes held by improvised clamps.

- **pH:** BOQU PH8012 industrial process electrode, specified with upper and lower 3/4-inch NPT threads and a direct low-noise cable.
- **EC:** Winters WTS-SS-1-1-1401 process conductivity electrode, K=1, 1/2-inch NPT, integrated Pt1000, and a 0.1-20,000 uS/cm published range.
- **Mounting:** each probe screws into a purchased female threaded insert captured by a removable, O-ring-sealed cartridge. The enclosure itself does not depend on a printed precision pipe thread.
- **Sampling:** the sensor chamber is upstream of the sample pump so it normally operates at slight negative pressure. The chamber, pump, and drain are isolated from the dry electronics tub.
- **Service:** the pH cartridge, EC cartridge, pump cradle, valve cassette, battery hatch, display bezel, and dry electronics tray are separate Fusion components.

The initial Fusion model can now start from controlled thread interfaces and conservative component envelopes. Final thread seats, cable exits, screw bosses, and display openings remain tied to receiving measurements.

## Budget

The planning total is **CNY 999.57 / US$149.24**, using **1 USD = 6.6977 CNY** for continuity with the first research pass. This includes a CNY 75 delivery allowance and basic mechanical hardware. No purchase was made.

The PH8012 and WTS probe prices are quote caps rather than verified Taobao checkout prices because direct Taobao automation is blocked by the browser safety layer. The procurement plan requires rejecting or re-quoting those lines if the exact requested variants exceed their caps. The mechanical adapter cartridges allow an equivalent threaded sensor to be substituted without remodeling the float body.

## Repository map

- `BOM.csv` - selected parts, quantities, budget caps, source links, mechanical interfaces, and freeze status.
- `COMPONENT_SELECTION.md` - decisions, exact sensor variants, electronics strategy, and alternatives.
- `SENSOR_INTERFACE_SPEC.md` - binding mechanical interface for the pH and EC cartridges.
- `MECHANICAL_DESIGN_PLAN.md` - Fusion assembly structure, parameters, tolerances, sequence, and acceptance checks.
- `PROCUREMENT_PLAN.md` - staged Taobao search plan, seller questions, quote limits, and receiving inspection.
- `DESIGN_RISKS.md` - open mechanical and integration risks with concrete closure tests.
- `SOURCE_INDEX.md` - research provenance and reference asset inventory.
- `fusion/` - Fusion parameter CSV, setup script, and CAD-start instructions.
- `reference-assets/` - manufacturer manuals, dimensional references, and controlled envelope drawings.

## Design status

The project is **ready for the first Fusion envelope and sensor-pod design cycle**. It is not release-ready for fabrication. Release geometry waits for caliper measurements of the purchased probes, female threaded inserts, display, pump, valves, battery holder, and PCB variants.

The low-cost pH and EC interface kits remain in the BOM for electrical bench validation. Their included laboratory-style probes are not the mechanical design basis. Electrical compatibility between each raw process probe and the selected interface board must be demonstrated before measurement accuracy or automated dosing is claimed.
