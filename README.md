# Hydroponics floating controller — hardware iteration 1

This repository captures the component selection and mechanical inputs for a small battery-powered controller that floats on a hydroponic reservoir, samples pH and electrical conductivity (EC), displays the readings, and controls three concentrate dosing lines.

## Iteration 1 result

The selected prototype set is estimated at **CNY 620.77 / US$92.68**, using **1 USD = 6.6977 CNY** on 2026-09-22. That leaves about **US$7.32** under the US$100 cap before delivery charges or enclosure material. No purchase was made.

The device is split into two mechanical zones for the later Fusion design:

- a gasketed dry electronics deck with the display, ESP32, signal boards, power conversion, removable battery, and switching electronics;
- a detachable lower wet manifold with the sample pump, probe flow cell, three dosing valves, and tube routing.

External concentrate reservoirs are assumed. Each reservoir must be above the dosing outlet so gravity provides pressure through its valve. A valve does not pump liquid. If the reservoirs cannot be gravity-fed, iteration 2 must replace the valves with three dosing pumps.

## Files

- `BOM.csv` — selected parts, quantities, observed prices, dimensions, and procurement links.
- `COMPONENT_SELECTION.md` — selection rationale, exact variants, limitations, and rejected alternatives.
- `MECHANICAL_INPUTS.md` — CAD envelopes, ports, sealing strategy, clearances, and Fusion part plan.
- `PROCUREMENT_CHECKLIST.md` — seller questions and receiving inspection steps that must be completed before final CAD.
- `SOURCE_INDEX.md` — source provenance and downloaded reference asset index.
- `reference-assets/` — manufacturer manuals and 2D dimensional references.

## Important prototype limits

The DFRobot SEN0161-V2 pH kit is a laboratory-grade probe. DFRobot states that long-duration measurements can drift. Iteration 1 therefore uses repeated sample cycles: flush, stop, settle, read, drain, and sleep. It is not specified as a maintenance-free 24/7 inline pH instrument.

The selected miniature valves have not been certified for concentrated acid, base, or nutrient stock. They are acceptable for water-path and diluted-nutrient bench tests only until the seller supplies wetted-material data and a soak/leak test passes with the actual concentrate. The enclosure will keep the valve cassette removable so a chemical-rated pinch valve or peristaltic pump can replace it.

The low-cost EC kit is selected because its 0–20 mS/cm range covers typical hydroponic use. Its analog output can reach 3.4 V, so a resistor divider and ADC1 input are required before the ESP32. Temperature compensation uses the separate DS18B20 probe.

## Browser research note

The signed-in Chrome session was available, but the computer-use browser safety layer rejected direct interaction with `taobao.com`. Taobao/Tmall parts were therefore identified through indexed product pages that state their data comes from Taobao/Tmall, then cross-checked against manufacturer documentation when available. Exact variant names and seller questions are recorded so the purchase can be verified later in Taobao without guessing.
