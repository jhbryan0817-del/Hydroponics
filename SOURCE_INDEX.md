# Source index

Retrieved or rechecked 2026-09-22 unless stated otherwise.

## Selected process sensors

- BOQU PH8012 manufacturer drawing and datasheet: https://img.yfisher.com/m6121/1726824698tqn.pdf
  - Used for PH8012 model identity, 0-14 pH range, PPS/PC body, two 22 mm 3/4-inch NPT zones, 161 mm overall length, 27.4 mm main body, 25.6 mm tip housing, 3.5 mm cable, and connector options.
- BOQU PH8012 distributor technical page: https://www.instrument.com.cn/netshow/SH102583/H1003014.html
  - Used for temperature options, cable construction, and planning price reference.
- BOQU PH8012 corroborating product listing: https://kr.made-in-china.com/co_shboqu/product_Aquiculture-Boqu-pH8012-on-Line-pH-Electrode-pH-Sensor_eohngoneg.html
  - Used to corroborate the 3/4-inch NPT process connection and industrial mounting form.
- Winters WTS conductivity sensor datasheet: https://www.winters.com.cn/upfile/202401/2024010435321481.pdf
  - Used for exact model WTS-SS-1-1-1401, K=1, 0.1-20,000 uS/cm, 1/2-inch NPT, Pt1000, 13 mm stem, and cable data.

The selected sensor prices in `BOM.csv` are procurement caps. Direct Taobao checkout prices were not verified because automated access to `taobao.com` was blocked by the browser site-safety policy.

## Mechanical alternatives evaluated

- AWE 9015-S8 PG13.5 pH electrode: https://www.awe-ltd.co.uk/products/ph/ph-electrode/pg13-5-thread-9015-s8.html
- MEDOTEC PG13.5 conductivity probes: https://www.medotec.de/fileadmin/PDF/Produkte/Mess-_und_Regeltechnik/Zubehoer/conductivity_sensors_DS-EN_01.pdf
- Pispa SEC135-S8 K=1 PG13.5 conductivity probe: https://pispa.fr/en/sensors-c-8/conductivity-probe-pg135-p-47
- Hach LZY082 K=1 PG13.5 conductivity probe: https://in.hach.com/2-electrode-conductivity-sensor-k-1-pg13-5-120-mm-graphite-electrode/product-details?id=61926485624
- GAIMC GEC threaded conductivity family: https://www.gaimc.com/Products/GWQ-EC200-1

These sources established that threaded process probes are readily available and that the enclosure should use replaceable adapters. The Pispa price of EUR 85.20 for the EC probe alone made an all-PG13.5 verified configuration impractical under the US$150 cap.

## Signal conditioning and control

- DFRobot SEN0161-V2 product page: https://www.dfrobot.com.cn/goods-1828.html
- DFRobot SEN0161-V2 wiki: https://wiki.dfrobot.com/sen0161-v2
- DFRobot industrial pH kit reference: https://www.dfrobot.com/product-2069.html
- Ai-Thinker NodeMCU-32S datasheet: https://docs.ai-thinker.com/_media/esp32/docs/nodemcu-32s_product_specification.pdf
- MSP2807 / ILI9341 display manual: https://offer-product.oss-cn-beijing.aliyuncs.com/product/offer/attachment/2213299636726/file/subPdf_202380_109426_20220314-151844022.pdf
- Conjoin CJWP12-AB family page: https://conjoinfluid.com/zh-CN/products/cjwp12-ab
- Conjoin CJWP12-AB datasheet: https://conjoinfluid.com/files/products/cjwp12-ab.pdf
- LiitoKala Lii-202 manufacturer page: https://www.liito-kala.com/page92?product_id=5
- EC kit technical cross-check: https://vctec.co.kr/product/detail.html?product_no=24121

## Taobao-indexed planning pages

These public indexed pages were retained from the first research pass. They are not a substitute for confirming the exact variant and delivered price in the signed-in Taobao cart.

- NodeMCU-32S CP2102: https://tao.hooos.com/tag_cp2102%E9%A9%B1%E5%8A%A8_5.html
- MSP2807 display: https://tao.hooos.com/goods_bX3dgoQ9hgtokjqkP0QiyxQuQt6-DokRR8IPPe6DqkQHM.html
- Your Cee EC kit: https://tao.hooos.com/goods_623341388528.html
- CJWP12 search result: https://tao.hooos.com/tag_%E8%BF%B7%E4%BD%A0%E6%B0%B4%E6%B3%B512v_1.html
- Miniature valves: https://tao.hooos.com/goods_KQbQZMH3t3gdmKSmpjuJtW-QAnppRSbaOyxQ0MsA.html
- Four-channel MOSFET driver: https://tao.hooos.com/goods_541617370335.html
- Lishen 18650 search: https://tao.hooos.com/search?w=2600mAH
- Covered 2S holder: https://tao.hooos.com/tag_18650%E7%94%B5%E6%B1%A0%E4%BB%93%E7%9B%92_1.html
- 2S BMS: https://tao.hooos.com/goods_eQOjQBMiDt373mwu8XyCzt0-ZWRNNbuA3OMYgYrcq.html
- MP1584 search: https://tao.hooos.com/search?w=MP24
- Silicone tube: https://tao.hooos.com/goods_MPd0Vw9HKtbMRY5FVVDhQtA-DokRR8IPrwVvWZzTa.html
- PTFE tube: https://tao.hooos.com/tag_%E5%9B%9B%E6%B0%9F%E7%94%B2%E9%86%9A%E8%8F%8A%E9%85%AF_9.html
- Through-panel barbs: https://tao.hooos.com/tag_%E5%AE%9D%E5%A1%94%E6%8E%A5%E5%A4%B4_40.html

## Repository assets

| File | Source | Exactness | Intended use |
|---|---|---|---|
| `reference-assets/NodeMCU-32S-datasheet.pdf` | Ai-Thinker | Exact board family | PCB envelope and pin/header layout |
| `reference-assets/MSP2807-ILI9341-display-manual.pdf` | Module documentation | Exact module family | Display proxy and opening |
| `reference-assets/SEN0161-V2-datasheet.pdf` | DFRobot | Exact interface-kit SKU | Electrical limits |
| `reference-assets/SEN0161-V2-dimensions.jpg` | DFRobot | Exact interface board | Board mounting reference |
| `reference-assets/SEN0161-V2-layout.svg` | Derived from DFRobot drawing | Exact interface board | Fusion sketch reference |
| `reference-assets/CJWP12-AB-pump-datasheet.pdf` | Conjoin | Exact pump family | Pump proxy and duty data |
| `reference-assets/LiitoKala-Lii-202-manual.pdf` | LiitoKala | Exact charger | Off-device reference |
| `reference-assets/PH8012-manufacturer-drawing.pdf` | BOQU | Exact selected pH model | Thread, body, cable, and connector dimensions |
| `reference-assets/WTS-SS-conductivity-sensor-datasheet.pdf` | Winters | Exact selected EC family/model table | EC process-probe reference |
| `reference-assets/PH8012-controlled-envelope.svg` | Project-controlled drawing | Conservative, not manufacturing | Fusion proxy profile |
| `reference-assets/WTS-SS-1-1-1401-controlled-envelope.svg` | Project-controlled drawing | Conservative pending exact seller drawing | Fusion proxy profile |

No trustworthy exact STEP model was found for PH8012, WTS-SS-1-1-1401, the display, pump, EC board, or valves. Similar-looking community models are excluded from final fits. Use proxy components until the actual parts are measured.
