# Procurement and receiving checklist

No purchase has been made. Use this list in Taobao before ordering and again when the parts arrive.

## Seller questions before ordering

### Controller and display

- NodeMCU-32S: confirm **38 pins, CP2102, ESP-WROOM-32, Micro-USB**, and provide a current top/bottom photo with ruler.
- Display: confirm **MSP2807, ILI9341, SPI, 240 x 320, 50 x 86 mm PCB**. Confirm whether the selected price includes the resistive touch layer.

### Sensors

- pH: confirm the sealed box label reads **DFRobot SEN0161-V2** and the kit includes pH 4.0/7.0 buffers.
- EC: confirm **K=1**, **0–20 mS/cm**, **5 V**, **AO 0–3.4 V**, **T1 temperature output**, 42 x 32 mm board, and the exact probe length/diameter.
- DS18B20: confirm genuine DS18B20, 1 m cable, stainless probe diameter and length, and three-wire pin colors.

### Pump and valves

- Pump: confirm **CJWP12-AB05A**, 5 V, 130–170 mL/min, and inlet/outlet barb diameter.
- Valves: confirm **6 V normally closed**, liquid-rated, 3 mm barbs, coil current, maximum pressure, and duty cycle.
- Ask the valve seller to name the wetted body, seal, spring, and armature materials. A statement such as “water valve” is not a chemical compatibility specification.

### Power and switching

- MOSFET board: confirm four channels, 3.3 V logic input, operation with a 6 V load rail, continuous current above 1 A per channel, and whether flyback diodes are fitted.
- Cells: request grade-A **Lishen LR1865SK 2600 mAh** cells from one production batch, matched in voltage and internal resistance.
- Holder: confirm **2S series / 7.4 V**, covered, switched. Reject the parallel 3.7 V version.
- BMS: confirm 2S Li-ion, common charge/discharge port, 5 A or more, and under-voltage protection.
- Charger: confirm LiitoKala **Lii-202**, two independent slots, 4.2 V Li-ion setting, and included USB cable.

## Receiving inspection

1. Photograph every part next to a metric ruler before removing labels.
2. Record overall length, width, height, connector overhang, mounting-hole diameter, and hole-center coordinates to 0.1 mm.
3. Verify the two 18650 cells are within 0.05 V of each other and label them as one pair.
4. Set the regulators with a bench supply before connecting electronics: 5.00 V and 6.00 V.
5. Confirm every valve remains closed with power removed and opens reliably through the planned battery range.
6. Confirm the sample pump self-primes in the intended orientation and measure real flow through the complete tube path.
7. Calibrate pH with fresh pH 4.0 and 7.0 buffers.
8. Calibrate EC with 1413 µS/cm and 12.88 mS/cm standards at a recorded temperature.
9. Verify the EC divider keeps the ESP32 input below 3.2 V at the sensor's maximum output.

## Chemical compatibility gate

For every concentrate that will touch a valve or soft connector:

1. place spare wetted parts or an entire spare valve in the actual concentrate for seven days;
2. compare mass, dimensions, hardness, swelling, cracking, and discoloration against an unused control;
3. cycle the valve at least 1,000 times with the concentrate while checking for external leakage and failure to close;
4. measure flow at the same head pressure before and after the test;
5. reject the valve if the seller cannot identify wetted materials or any visible/measurable degradation occurs.

Concentrated pH-down acid or pH-up base must not enter the prototype until this gate passes. If it fails, use a chemical-rated pinch valve or peristaltic dosing pump so the fluid touches only rated tubing.

## Design-freeze data to add to the repository

- actual dimension sheet for every received part;
- seller screenshots showing the selected variants;
- measured pump curve at the intended tube length;
- valve dose-volume repeatability versus open time and reservoir head;
- assembled component mass and center-of-mass estimate;
- calibration logs for pH, EC, and temperature.

