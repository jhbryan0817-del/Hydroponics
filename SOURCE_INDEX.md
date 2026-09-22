# Source index

Retrieved 2026-09-22 unless stated otherwise.

## Taobao / Tmall indexed procurement pages

These pages state that their product data comes from Taobao or Tmall. They were used because direct interaction with `taobao.com` was rejected by the browser safety layer.

- NodeMCU-32S CP2102 exact-title result: https://tao.hooos.com/tag_cp2102%E9%A9%B1%E5%8A%A8_5.html
- MSP2807 2.8-inch ILI9341 display: https://tao.hooos.com/goods_bX3dgoQ9hgtokjqkP0QiyxQuQt6-DokRR8IPPe6DqkQHM.html
- Your Cee EC kit: https://tao.hooos.com/goods_623341388528.html
- Waterproof DS18B20: https://tao.hooos.com/goods_557335406985.html
- CJWP12 pump indexed result: https://tao.hooos.com/tag_%E8%BF%B7%E4%BD%A0%E6%B0%B4%E6%B3%B512v_1.html
- Miniature 3.7/6/12 V normally-closed valve: https://tao.hooos.com/goods_KQbQZMH3t3gdmKSmpjuJtW-QAnppRSbaOyxQ0MsA.html
- Four-channel MOSFET driver: https://tao.hooos.com/goods_541617370335.html
- Lishen LR1865SK exact-title result: https://tao.hooos.com/search?w=2600mAH
- Covered 2S 18650 holder result: https://tao.hooos.com/tag_18650%E7%94%B5%E6%B1%A0%E4%BB%93%E7%9B%92_1.html
- LiitoKala Lii-202 exact-title result: https://tao.hooos.com/search?w=Liitokala
- 2S 5 A BMS: https://tao.hooos.com/goods_eQOjQBMiDt373mwu8XyCzt0-ZWRNNbuA3OMYgYrcq.html
- MP1584EN result: https://tao.hooos.com/search?w=MP24
- 2 x 4 mm silicone tube: https://tao.hooos.com/goods_MPd0Vw9HKtbMRY5FVVDhQtA-DokRR8IPrwVvWZzTa.html
- 2 x 4 mm PTFE exact-title result: https://tao.hooos.com/tag_%E5%9B%9B%E6%B0%9F%E7%94%B2%E9%86%9A%E8%8F%8A%E9%85%AF_9.html
- FKM soft adapter tube: https://tao.hooos.com/goods_0vMGY6aoi7t8BRRBB8YF00jt2t6-DokRR8Ipq4XQaj3iOK.html
- PP through-panel barbed fittings: https://tao.hooos.com/tag_%E5%AE%9D%E5%A1%94%E6%8E%A5%E5%A4%B4_40.html

## Manufacturer and technical sources

- DFRobot SEN0161-V2 product and limitations: https://www.dfrobot.com.cn/goods-1828.html
- DFRobot SEN0161-V2 wiki: https://wiki.dfrobot.com/sen0161-v2
- Ai-Thinker NodeMCU-32S datasheet: https://docs.ai-thinker.com/_media/esp32/docs/nodemcu-32s_product_specification.pdf
- MSP2807 / ILI9341 display manual: https://offer-product.oss-cn-beijing.aliyuncs.com/product/offer/attachment/2213299636726/file/subPdf_202380_109426_20220314-151844022.pdf
- Conjoin CJWP12-AB family: https://conjoinfluid.com/zh-CN/products/cjwp12-ab
- Conjoin CJWP12-AB datasheet: https://conjoinfluid.com/files/products/cjwp12-ab.pdf
- LiitoKala Lii-202 manufacturer page: https://www.liito-kala.com/page92?product_id=5
- EC-kit matching technical description: https://vctec.co.kr/product/detail.html?product_no=24121
- September 2026 exchange-rate reference: https://ca.investing.com/currencies/usd-cny-historical-data

## Downloaded assets

| File | Part | Exactness | Use |
|---|---|---|---|
| `reference-assets/NodeMCU-32S-datasheet.pdf` | CTRL-01 | Exact family and selected board type | PCB outline, pin spacing, revision comparison. |
| `reference-assets/MSP2807-ILI9341-display-manual.pdf` | DISP-01 | Exact module family | Board and active-area dimensions. |
| `reference-assets/SEN0161-V2-datasheet.pdf` | PH-01 | Exact SKU | Electrical limits and kit data. |
| `reference-assets/SEN0161-V2-dimensions.jpg` | PH-01 board | Exact SKU | Board outline and mounting holes. |
| `reference-assets/SEN0161-V2-layout.svg` | PH-01 board | Exact SKU | Fusion sketch/reference import. |
| `reference-assets/CJWP12-AB-pump-datasheet.pdf` | PUMP-01 | Exact family; AB05A variant selected | Pump envelope and duty/performance data. |
| `reference-assets/LiitoKala-Lii-202-manual.pdf` | CHG-01 | Exact charger model | Off-device charger specification. |

No trustworthy exact STEP model was found for the selected display, EC kit, pump, or valves. Similar-looking community models were excluded because connector and mounting geometry varies. The next Fusion cycle should create simple parameterized components from the downloaded 2D references and replace confirm-marked dimensions with caliper measurements after parts arrive.
