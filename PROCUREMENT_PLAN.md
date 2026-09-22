# Procurement plan

No purchase has been made. The goal of procurement is to lock mechanical interfaces before the full electronics set is ordered.

## Budget controls

| Control | Limit |
|---|---:|
| Parts subtotal | CNY 924.57 |
| Delivery and seller variance | CNY 75.00 |
| Total authorization ceiling | CNY 999.57 / US$149.24 |
| PH8012 complete probe cap | CNY 90 |
| WTS-SS-1-1-1401 complete probe cap | CNY 180 |

The conversion uses 1 USD = 6.6977 CNY to stay consistent with the first BOM. Recalculate before ordering if the actual exchange rate or card fee would make the cart exceed US$150.

Do not compensate for an over-cap sensor by deleting its thread insert, gasket, protection board, or mechanical hardware. Re-quote the sensor or choose an equivalent threaded probe carried by a new common cartridge.

## Taobao access note

The signed-in Chrome tab is visible, but automated access to `taobao.com` is blocked by the browser site-safety policy. Publicly indexed listings and manufacturer documents were used for planning. The exact cart variant, seller, delivery cost, and current checkout price therefore require a final human verification in Taobao.

## Purchase sequence

### Lot 1 - mechanical lock parts

Buy or quote these first:

1. PH8012 pH probe;
2. WTS-SS-1-1-1401 EC probe;
3. 3/4-inch NPT female insert/socket;
4. 1/2-inch NPT female insert/socket;
5. representative O-rings, M3 inserts, and cable glands.

Do not freeze the sensor block until these parts are measured. The rest of the Fusion assembly can proceed using proxies.

### Lot 2 - enclosure-driving parts

Order the display, battery holder, pump, valves, and through-panel barbs. These set openings, tube bends, service paths, and center of mass.

### Lot 3 - electronics

Order the ESP32, pH kit, EC kit, MOSFET board, BMS, regulators, cells, and external charger after Lot 1 quotes leave enough budget. The dry tray is adjustable, so minor board revision changes do not block the sensor design.

### Lot 4 - tubing and consumables

Order final tube lengths, connectors, screws, gasket cord, and wiring after a routing mock-up establishes real lengths.

## Exact search strings

Paste these into Taobao without removing the model numbers:

| ID | Search string |
|---|---|
| PH-PROBE-01 | `博取 PH8012 在线PH电极 3/4NPT BNC 无温补 1米线` |
| EC-PROBE-01 | `WTS-SS-1-1-1401 电导率电极 K1 1/2NPT PT1000` |
| ADAPT-PH-01 | `3/4NPT 内螺纹 直通 接头 镶件 传感器` |
| ADAPT-EC-01 | `1/2NPT 内螺纹 直通 接头 镶件 传感器` |
| PH-FE-01 | `DFRobot SEN0161-V2 模拟pH计 V2` |
| EC-FE-01 | `Your Cee K=1 电导率模块 0-20mS 5V 模拟` |
| DISP-01 | `MSP2807 ILI9341 SPI 2.8寸 240x320` |
| PUMP-01 | `CJWP12-AB05A 5V 微型隔膜水泵` |

## Seller questions

### PH8012

Send one message containing all of the following:

- Is the quoted item a complete BOQU PH8012 electrode rather than a replacement cap or deposit?
- Confirm upper and lower threads are both 3/4-inch NPT.
- Confirm the manufacturer outline: 161 mm overall, 27.4 mm main body, 25.6 mm tip housing, two 22 mm NPT zones, and 3.5 mm cable.
- Quote the BNC (Q9) pH-signal version with low-noise coax. Do not substitute the multiwire pin/Y-plate option without its full wiring diagram.
- Can the cable be supplied at 1 m? If not, state the shortest available length.
- Send a current photo of the exact connector, cable exit, thread, and glass tip beside a metric ruler.

Reject the listing if the answers mix PH8010, PH8012, ORP8013, or a different thread.

### WTS-SS-1-1-1401

- Confirm the complete model code `WTS-SS-1-1-1401`.
- Confirm K=1 and published range through 20,000 uS/cm.
- Confirm male 1/2-inch NPT and provide the exact thread length.
- Provide total length, stem length, head diameter, wrench size, and cable exit dimensions.
- Confirm two EC electrode wires plus Pt1000 wires and provide the wire assignment.
- Quote a 1 m cable if available; otherwise state whether shortening is allowed.
- Send the current drawing and a photograph beside a metric ruler.

Reject an otherwise similar K=0.1 or K=10 probe. Its active geometry and electronics range differ.

### Thread inserts

- Confirm the internal thread standard is NPT, not BSP/G thread.
- Provide maximum outside diameter/across-flats, body length, thread engagement, shoulder dimensions, and material.
- Prefer a shape with flats or an anti-rotation feature that can be captured in a printed cartridge.

### Display, pump, and valves

- Display: MSP2807, ILI9341, SPI, 240 x 320, 50 x 86 mm PCB; request front/back photos and hole coordinates.
- Pump: CJWP12-AB05A, 5 V, 130-170 mL/min; request barb diameter and barb-center drawing.
- Valves: 6 V normally closed, liquid type, 3 mm barbs; request coil current and outline drawing.

## Quote decision rules

Accept a sensor quote only when all of these are true:

- model and thread match the BOM;
- the seller supplied enough dimensions to update its Fusion proxy;
- connector or wire assignment is known;
- complete delivered price keeps the cart below the total ceiling;
- the seller photo shows one complete probe, not only a transmitter or accessory.

If PH8012 exceeds CNY 90, search the same model from another seller. If it still exceeds the cap, accept an equivalent 3/4-inch NPT BNC pH electrode inside the 32 x 165 mm proxy.

If WTS exceeds CNY 180, request a generic K=1, 0-20 mS/cm, two-electrode process probe with either 1/2-inch or 3/4-inch NPT. The substitute may receive a new cartridge, but it must stay inside the 30 x 180 mm proxy and 200 mm extraction envelope.

## Receiving inspection

1. Photograph each part with its label and a metric ruler before removing packaging.
2. Record overall length, maximum diameter/AF, thread major diameter, usable thread length, cable diameter, cable exit, connector, and mass.
3. Verify thread standards using known fittings; do not force NPT into BSP.
4. Create a simple caliper sketch with one datum and dimensions to 0.1 mm.
5. Test-fit each sensor into its purchased insert before designing the printed cartridge.
6. Check that the probe can be tightened without twisting or damaging its cable.
7. Measure display, pump, valves, holder, and every PCB including connector overhang.
8. Add the measurements and photographs to `reference-assets/received/` using the BOM ID in every filename.
9. Update the `confirm` parameters and commit the measurement sheet before final CAD.

## Bench checks after mechanical inspection

- Confirm PH8012 produces a stable response through the DFRobot board in pH 4 and pH 7 buffers.
- Identify the WTS electrode and Pt1000 wires before connecting the EC board.
- Confirm the EC board excitation and calibration work with the WTS K=1 cell.
- Set regulators to 5.00 V and 6.00 V before connecting loads.
- Measure pump flow through the real sensor block and tubing.
- Confirm each valve operates throughout the battery range.

These electrical checks do not block the first Fusion layout, but they block automated dosing.
