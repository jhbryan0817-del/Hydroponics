# Component selection

Prices are a 2026-09-22 snapshot. Taobao/Tmall links point to indexed mirrors because direct `taobao.com` interaction was blocked by the browser safety layer. No order was placed.

## Control and display

### CTRL-01 — Ai-Thinker NodeMCU-32S, CP2102, 38-pin

This is a documented ESP32 board with enough GPIO for the display, two analog channels, temperature probe, pump, and three valves. The Ai-Thinker dimensional drawing gives a 48.26 x 25.40 mm PCB. Because Taobao sellers mix CP2102 and CH340 revisions under one listing, the enclosure reserve is 55 x 28 x 14 mm and the exact seller photo must be locked before detailed CAD.

The lower-cost NodeMCU-32S preserves the measurement budget. The official ESP32-DevKitC Taobao result was roughly CNY 79–82, while this selected exact-title result is CNY 23.86.

### DISP-01 — MSP2807 2.8-inch SPI TFT

The 2.8-inch ILI9341 module is large enough to show pH, EC, temperature, dosing state, and battery status without making the float excessively wide. The module uses a 50 x 86 mm PCB and a 43.2 x 57.6 mm active display area. The later enclosure must expose only a clear window; the PCB and card slot remain inside the dry zone.

Select the SPI ILI9341 variant. A resistive-touch layer is acceptable but is not required by iteration 1.

## Measurement chain

### PH-01 — DFRobot SEN0161-V2

The SEN0161-V2 was chosen over generic PH4502C boards because it accepts 3.3–5.5 V, outputs 0–3.0 V, includes two-point calibration buffers, and has published dimensional data. Its board is 42 x 32 mm and its stated accuracy is ±0.1 pH at 25 °C.

DFRobot explicitly limits this kit to laboratory-style measurement and warns that the probe may drift during extended measurement. The prototype will use repeated cycles:

1. run the sample pump to flush the chamber;
2. stop the pump to remove flow and electrical noise;
3. wait for the pH probe to settle;
4. sample pH, EC, and temperature;
5. drain or refresh the chamber;
6. sleep until the next cycle.

If continuous 24/7 measurement becomes a hard requirement, move to an industrial pH kit such as SEN0169-V2 and revise the budget.

### EC-01 — Your Cee K=1 analog EC kit

The selected EC kit covers 0–20 mS/cm and recommends 1–15 mS/cm, a practical range for hydroponic nutrient solutions. The board is reported as 42 x 32 mm, the probe is about 172 mm long, and the analog output is 0–3.4 V.

The 3.4 V maximum is above the ESP32 input rail. Route AO through a 10 kΩ series resistor and 100 kΩ resistor to ground, then add 100 nF to ground at the ADC1 pin. This scales 3.4 V to about 3.09 V. Use an ADC1 pin because ESP32 ADC2 conflicts with Wi-Fi. Calibration requires 1413 µS/cm and 12.88 mS/cm standards.

### TEMP-01 — waterproof DS18B20

Temperature is a supporting input even though the product UI exposes pH and EC. Both measurements vary with temperature, so the control logic must retain the raw temperature and the compensated values. Reserve a 6 mm diameter by 50 mm probe envelope until the seller confirms the supplied probe.

## Fluid handling

### PUMP-01 — Conjoin CJWP12-AB05A

The exact selected pump is the 5 V AB05A variant, not the lower-flow AA variant. Manufacturer data gives 130–170 mL/min, less than 180 mA, and less than 0.9 W. The life test is specified at 10 seconds on / 10 seconds off; this supports cyclic sampling and does not support assuming indefinite continuous operation.

### VALVE-01 — three 6 V normally-closed miniature valves

These valves satisfy the count, size, and price targets. They rely on gravity head from three external concentrate reservoirs. Firmware must open only one valve at a time.

The listing does not publish trustworthy wetted-material data. Until the seller confirms the body, seal, and armature materials, these valves are limited to water and diluted-nutrient trials. Concentrated acid or base can attack common seals and metals. Passing criteria for each actual concentrate are in `PROCUREMENT_CHECKLIST.md`.

If gravity feed is not possible or the valves fail compatibility testing, replace the removable valve cassette with three small peristaltic dosing pumps. The sample pump must never be reused for dosing because shared plumbing would cross-contaminate concentrates and make dose volume unpredictable.

### Tubes and ports

Use 2 x 4 mm silicone tube for the reservoir sample loop. Use 2 x 4 mm PTFE for the three long concentrate runs, with short FKM sleeves only where a soft connection to a 3 mm barb is required. The current architecture needs eight tube interfaces: sample inlet, sample outlet, three concentrate inlets, and three dosing outlets.

## Power and switching

Two matched Lishen LR1865SK cells form a 2S pack: 7.4 V nominal, 8.4 V full, and roughly 19.2 Wh nominal. A covered 2S holder lets the user remove both cells without exposing a charging connector on the wet device. The cells stay as a labeled matched pair and are charged together in the external Lii-202.

A 2S 5 A protection board provides in-device over-current and under-voltage protection. Two MP1584 modules create:

- 5.0 V for the ESP32 VIN, display, sensors, and sample pump;
- 6.0 V for the valve coils.

The four-channel MOSFET board controls the pump and three valves. Add a reverse-biased flyback diode across every inductive load unless the received module visibly includes the diodes.

The nominal energy estimate is 19.2 Wh. With conversion losses and a 20% reserve, about 15 Wh is usable. A continuously lit display plus continuous sampling is expected to run for roughly 5–7 hours. Cyclic sampling, display dimming, and Wi-Fi sleep should extend this to roughly 8–12 hours. These are engineering estimates; final runtime must be measured on the assembled hardware.

## Alternatives rejected for iteration 1

| Alternative | Reason not selected |
|---|---|
| DFRobot industrial pH / EC kits | Better for 24/7 use but exceed the complete US$100 budget. |
| DFRobot SEN0244 TDS kit | 0–1000 ppm is too narrow for many hydroponic solutions and is not a direct wide-range EC measurement. |
| Three peristaltic dosing pumps | Better metering and chemical isolation, but larger and materially more expensive. Retained as the preferred upgrade. |
| Chemical-rated pinch valves | Ideal wetted path, but three units alone consume or exceed the hardware budget. |
| Official ESP32-DevKitC | Mechanically well documented but approximately CNY 55 more than the selected NodeMCU board. |
| Onboard chemical reservoirs | They increase size, weight, spill risk, and the number of service openings on a floating device. |

