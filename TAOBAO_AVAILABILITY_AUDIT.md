# Taobao availability audit

Audit date: 2026-09-23.

## What the status means

No BOM line has been verified in a live, signed-in Taobao product page or checkout. Automated access to `taobao.com` is blocked in the available browser environment. A public indexing site was used for some listing evidence, but it cannot confirm that a listing is still active, that the required option is selectable, or that the displayed price applies to that option.

| Status | Meaning |
|---|---|
| Exact model, external only | The manufacturer or another marketplace confirms the model, but no Taobao listing was confirmed. |
| Taobao-indexed model match | A third-party index contains a Taobao-origin listing that appears to match the model or specification; current availability and variant remain unverified. |
| Taobao-indexed generic match | Only a generic product type or search/category page was found. It does not select an exact purchasable part. |
| Mismatch | The indexed item does not satisfy the BOM description and must be replaced. |
| Allowance | No product was selected; the amount is only a budget placeholder. |

## Component-by-component result

| ID | Why it is needed | Taobao finding | Verdict before purchase |
|---|---|---|---|
| PH-PROBE-01 | Threaded wet pH sensor and primary mechanical interface. | The exact BOQU PH8012 is confirmed by BOQU documentation and a manufacturer Alibaba listing. No current Taobao product page was confirmed. | **Exact model, external only.** Do not assume it is available on Taobao. Obtain a Taobao seller link and confirm the BNC/Q9, 3/4-inch NPT, cable, and complete-electrode variant. |
| PH-FE-01 | Converts the very high-impedance pH electrode signal to an analog voltage the ESP32 can read. | DFRobot confirms SEN0161-V2 and its CNY 249 price on its own Chinese store. No current Taobao listing was confirmed. | **Exact model, external only.** It can be bought from DFRobot if Taobao does not carry the exact SKU. |
| EC-PROBE-01 | Threaded K=1 conductivity cell; defines the second wet cartridge. | Winters documentation confirms WTS-SS-1-1-1401. No current Taobao product page or seller quote was found. | **Exact model, external only.** The CNY 180 line is a cap, not a quote. An equivalent threaded K=1 probe may be easier to source. |
| EC-FE-01 | Excites the EC cell and converts conductivity to an analog signal. | A third-party index contains a Taobao-origin listing for the Your Cee K=1, 0-20 mS/cm kit. The live seller, stock, exact option, and compatibility with the WTS probe were not confirmed. | **Taobao-indexed model match.** Mechanically usable as a reserved board envelope; electrically gated. |
| CTRL-01 | Main processor, Wi-Fi/Bluetooth, display control, sensing, and four load-control signals. | Only a third-party Taobao search/tag result was retained; it does not confirm the exact Ai-Thinker 38-pin CP2102 board revision. | **Taobao-indexed generic match.** Select a listing with front/back photos and 48.26 x 25.40 mm board dimensions. |
| DISP-01 | Local display for pH, EC, battery state, and operating mode. | A recently indexed Taobao-origin listing matches a 2.8-inch ILI9341 SPI 240 x 320 module at CNY 36.30. The exact MSP2807 option and live checkout were not opened. | **Taobao-indexed model/family match.** Confirm MSP2807, touch option, 50 x 86 mm PCB, and mounting holes. |
| PUMP-01 | Pulls reservoir water through the sensor chamber for repeated readings. | The exact CJWP12-AB05A is documented by Conjoin, but no exact Taobao listing or CNY 1.20 price was confirmed. | **Exact model, external only.** The price is unsupported as a Taobao quote and must be re-quoted. |
| VALVE-01 | Opens one concentrate line at a time; three valves provide three independent dosing channels. | The indexed listing is described as a miniature air/vent valve. A similar form factor exists, but liquid service was not established. | **Mismatch.** Replace this row with a seller-confirmed liquid valve or use the listed item only for a dry mechanical mock-up. |
| DRV-01 | Lets 3.3 V ESP32 GPIO switch the pump and three valve loads. | A third-party index contains a Taobao-origin four-channel opto-isolated MOSFET board listing. Exact PCB revision and 3.3 V trigger behavior remain unverified. | **Taobao-indexed model/family match.** Confirm board size, logic polarity, load voltage, flyback protection, and continuous current. |
| CELL-01 | Supplies removable battery energy in a 2S pack. | The retained URL is only a Taobao-indexed search for 2600 mAh cells; it does not confirm genuine Lishen LR1865SK cells or a matched pair. | **Taobao-indexed generic match.** Use a reputable cell seller and verify authenticity and matching. |
| HOLDER-01 | Holds the removable cells beneath the sealed battery hatch. | Only a generic indexed category for covered 18650 holders was found. | **Taobao-indexed generic match.** Choose the exact 2S series version and measure it before the hatch is frozen. |
| CHG-01 | Charges removed cells away from the wet device. | LiitoKala confirms the Lii-202 model on its own site. No current Taobao listing or CNY 34 checkout price was confirmed. | **Exact model, external only.** It is off-device and does not affect enclosure CAD. |
| BMS-01 | Protects the 2S pack against over-current, over-charge, and over-discharge. | A third-party index contains a Taobao-origin generic 2S 5 A board listing. No branded model or current board revision was fixed. | **Taobao-indexed generic match.** Confirm dimensions, common-port wiring, and actual protection thresholds. |
| REG-01 | Generates separate 5 V and 6 V rails from the 2S battery. | The retained search URL does not prove an MP1584EN module or the stated CNY 3 price. | **Taobao-indexed generic match.** Select and measure an exact MP1584EN board before clips are finalized. |
| TUBE-01 | Carries sampled reservoir water to and from the measurement chamber. | A third-party index contains a Taobao-origin silicone-tube listing, but the 2 x 4 mm option and quantity price were not checked live. | **Taobao-indexed specification match.** Confirm ID, OD, length, and selected variant. |
| TUBE-02 | Provides three separate concentrate lines. | Only a generic indexed PTFE category was retained. | **Taobao-indexed generic match.** Select an exact 2 x 4 mm product and measure bend behavior. |
| ADAPT-PH-01 / ADAPT-EC-01 | Provide real female NPT threads inside replaceable printed sensor cartridges. | No exact product or seller was selected. | **Allowance.** These are mechanical-lock parts and must be selected before sensor-cartridge detail design. |
| PORT-01 | Makes eight sealed through-panel tube connections. | Only a generic indexed barb category was found. | **Taobao-indexed generic match.** Select an exact bulkhead fitting with a dimensional drawing. |
| MISC-01 | Covers fasteners, inserts, seals, wire, connectors, diodes, and passives. | No exact products were selected. | **Allowance.** Split into exact lines after the enclosure and wiring layout are frozen. |

## Procurement conclusion

The current BOM is a mechanical planning BOM, not a Taobao-ready shopping list. The exact MSP2807-family display, Your Cee EC kit, MOSFET board, and some commodity parts have evidence of Taobao-origin listings, but none has been verified in a live checkout. The two enclosure-defining probes are exact engineering selections with manufacturer documentation, but their Taobao availability and prices are not confirmed.

Before ordering, every selected Taobao row needs a live product URL, seller, option text, current item price, delivery price, and a screenshot or exported product specification. The valve row must be replaced rather than approved as written.
