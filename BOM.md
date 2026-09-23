# Bill of materials

This is the readable version of `BOM.csv`. Prices are the 2026-09-22 planning snapshot. No purchase has been made. **No line has been verified in a live Taobao product page or checkout.** See [TAOBAO_AVAILABILITY_AUDIT.md](TAOBAO_AVAILABILITY_AUDIT.md) for the component-by-component evidence and limitations.

## Budget summary

| Category | CNY | Approx. USD |
|---|---:|---:|
| Sensors and interface electronics | 705.90 | 105.39 |
| Controller and display | 60.16 | 8.98 |
| Fluid handling | 30.46 | 4.55 |
| Power and switching | 70.54 | 10.53 |
| Tubing and mechanical hardware | 57.51 | 8.59 |
| **Parts subtotal** | **924.57** | **138.04** |
| Delivery and price-variance allowance | 75.00 | 11.20 |
| **Planning total** | **999.57** | **149.24** |

Conversion used: 1 USD = 6.6977 CNY. Enclosure filament is assumed to come from workshop stock.

### Status key

| Status | Meaning |
|---|---|
| Ready | The conservative Fusion envelope is defined. |
| Quote open | The exact model is selected, but the Taobao delivered price must stay below its cap. |
| Part open | The interface is fixed, but the exact seller part must be selected and measured. |
| Electrical gate | Mechanical design can proceed; electrical compatibility still needs bench testing. |
| Off-device | The part does not occupy enclosure space. |

Mechanical status does not mean procurement-confirmed. A part may be usable as a conservative Fusion envelope while its exact seller, variant, and price are still open.

## Sensors and interface electronics

| ID | Selected part and variant | Qty | Unit CNY | Total CNY | Mechanical basis | Status |
|---|---|---:|---:|---:|---|---|
| PH-PROBE-01 | [BOQU PH8012 industrial pH electrode](https://img.yfisher.com/m6121/1726824698tqn.pdf), BNC/Q9, upper and lower 3/4-inch NPT, request 1 m cable | 1 | 90.00 | 90.00 | 27.4 mm maximum body x 161 mm; two 22 mm thread zones; 200 mm removal clearance | **Quote open** |
| PH-FE-01 | [DFRobot SEN0161-V2](https://www.dfrobot.com.cn/goods-1828.html), used for its BNC signal board and calibration supplies | 1 | 249.00 | 249.00 | 42 x 32 mm PCB; reserve 48 x 38 x 24 mm with cable bend | Ready; electrical bench check required |
| EC-PROBE-01 | [Winters WTS-SS-1-1-1401](https://www.winters.com.cn/upfile/202401/2024010435321481.pdf), K=1, Pt1000, 1/2-inch NPT, request 1 m cable | 1 | 180.00 | 180.00 | 13 mm stem; reserve 30 x 180 mm and 200 mm removal clearance | **Quote open** |
| EC-FE-01 | [Your Cee analog EC kit](https://tao.hooos.com/goods_623341388528.html), K=1, 0-20 mS/cm | 1 | 186.90 | 186.90 | Reported 42 x 32 mm PCB; reserve 48 x 38 x 24 mm | **Electrical gate** |
|  | **Sensors subtotal** |  |  | **705.90** |  |  |

The process probes above control the enclosure geometry. The laboratory-style probes included with the interface kits are bench-test spares.

## Controller and display

| ID | Selected part and variant | Qty | Unit CNY | Total CNY | Mechanical basis | Status |
|---|---|---:|---:|---:|---|---|
| CTRL-01 | [Ai-Thinker NodeMCU-32S](https://tao.hooos.com/tag_cp2102%E9%A9%B1%E5%8A%A8_5.html), ESP-WROOM-32, CP2102, 38-pin | 1 | 23.86 | 23.86 | 48.26 x 25.40 mm PCB; reserve 55 x 28 x 14 mm | Ready |
| DISP-01 | [MSP2807 2.8-inch TFT](https://tao.hooos.com/goods_bX3dgoQ9hgtokjqkP0QiyxQuQt6-DokRR8IPPe6DqkQHM.html), ILI9341, SPI, 240 x 320 | 1 | 36.30 | 36.30 | 86 x 50 mm PCB; reserve 90 x 54 x 12 mm | Ready |
|  | **Controller/display subtotal** |  |  | **60.16** |  |  |

## Fluid handling

| ID | Selected part and variant | Qty | Unit CNY | Total CNY | Mechanical basis | Status |
|---|---|---:|---:|---:|---|---|
| PUMP-01 | [Conjoin CJWP12-AB05A](https://conjoinfluid.com/zh-CN/products/cjwp12-ab), 5 V micro diaphragm pump | 1 | 1.20 | 1.20 | Reserve 45 x 25 x 18 mm plus 20 mm barb bends | Ready |
| VALVE-01 | Miniature normally-closed **liquid** valve, 6 V, 3 mm barbs; exact seller part still required | 3 | 6.98 | 20.94 | Reserve 28 x 15 x 15 mm each plus tube bends | **Replace indexed air-valve listing** |
| PORT-01 | [PP through-panel barbed fitting](https://tao.hooos.com/tag_%E5%AE%9D%E5%A1%94%E6%8E%A5%E5%A4%B4_40.html), sized for 4 mm OD tube | 8 | 1.04 | 8.32 | Cutout and retaining-nut envelope require seller drawing | Part open |
|  | **Fluid-handling subtotal** |  |  | **30.46** |  |  |

## Power and switching

| ID | Selected part and variant | Qty | Unit CNY | Total CNY | Mechanical basis | Status |
|---|---|---:|---:|---:|---|---|
| DRV-01 | [Four-channel opto-isolated MOSFET board](https://tao.hooos.com/goods_541617370335.html), 3.3 V logic compatible | 1 | 10.34 | 10.34 | Reserve 70 x 55 x 20 mm on an adjustable rail | Ready |
| CELL-01 | [Lishen LR1865SK](https://tao.hooos.com/search?w=2600mAH), 3.7 V, 2600 mAh matched cells | 2 | 8.50 | 17.00 | 18.3 mm diameter x 65 mm each | Ready |
| HOLDER-01 | [Covered two-cell 18650 holder](https://tao.hooos.com/tag_18650%E7%94%B5%E6%B1%A0%E4%BB%93%E7%9B%92_1.html), 2S/7.4 V | 1 | 1.40 | 1.40 | Reserve 82 x 47 x 27 mm | Ready |
| CHG-01 | [LiitoKala Lii-202](https://www.liito-kala.com/page92?product_id=5), two-slot external charger | 1 | 34.00 | 34.00 | 116 x 60 x 30 mm | Off-device |
| BMS-01 | [2S Li-ion protection board](https://tao.hooos.com/goods_eQOjQBMiDt373mwu8XyCzt0-ZWRNNbuA3OMYgYrcq.html), 5 A common port | 1 | 1.80 | 1.80 | Reserve 40 x 25 x 8 mm | Ready |
| REG-01 | [MP1584EN mini buck module](https://tao.hooos.com/search?w=MP24), adjustable | 2 | 3.00 | 6.00 | Reserve 28 x 22 x 10 mm each | Ready |
|  | **Power/switching subtotal** |  |  | **70.54** |  |  |

## Tubing and mechanical hardware

| ID | Selected part and variant | Qty | Unit CNY | Total CNY | Mechanical basis | Status |
|---|---|---:|---:|---:|---|---|
| TUBE-01 | [Food-grade silicone tube](https://tao.hooos.com/goods_MPd0Vw9HKtbMRY5FVVDhQtA-DokRR8IPrwVvWZzTa.html), 2 mm ID x 4 mm OD, 2 m | 2 | 1.00 | 2.00 | 12 mm minimum bend radius | Ready |
| TUBE-02 | [PTFE tube](https://tao.hooos.com/tag_%E5%9B%9B%E6%B0%9F%E7%94%B2%E9%86%9A%E8%8F%8A%E9%85%AF_9.html), 2 mm ID x 4 mm OD, 3 m | 3 | 1.17 | 3.51 | 20 mm minimum bend radius | Ready |
| ADAPT-PH-01 | Commercial female 3/4-inch NPT insert/socket | 1 | 15.00 | 15.00 | Maximum 36 mm body x 32 mm; captured in common 54 mm cartridge | Part open |
| ADAPT-EC-01 | Commercial female 1/2-inch NPT insert/socket | 1 | 12.00 | 12.00 | Maximum 30 mm body x 28 mm; captured in common 54 mm cartridge | Part open |
| MISC-01 | M3 inserts/screws, O-rings, gasket cord, wire, connectors, diodes, and passives | 1 allowance | 25.00 | 25.00 | Prototype hardware allowance | Allowance |
|  | **Tubing/mechanical subtotal** |  |  | **57.51** |  |  |

## Purchase controls

- PH8012 delivered-price target: **CNY 90**; current external listings suggest this is probably too low for the exact BOQU model.
- WTS-SS-1-1-1401 delivered-price cap: **CNY 180**.
- Complete planning ceiling: **CNY 999.57 / US$149.24**; this is not a validated purchasable cart.
- Confirm the exact probe, connector, cable length, thread, and drawing before ordering.
- See [PROCUREMENT_PLAN.md](PROCUREMENT_PLAN.md) for Taobao search terms, seller questions, and receiving checks.
- `BOM.csv` remains the machine-readable source for calculations and future automation.
