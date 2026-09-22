# Mechanical design plan for Fusion 360

The first Fusion cycle must prove sensor installation, service access, water separation, and float stability before cosmetic refinement. All dimensions marked `confirm` remain parameters until measured from received parts.

## Assembly structure

Create one Fusion component for each item below. Do not model the product as one multi-body component.

1. `00_MASTER_LAYOUT` - waterline, origin planes, keep-out volumes, mass points, and shared sketches.
2. `10_FLOAT_UPPER` - upper pontoon shell and dry-tub flange.
3. `11_FLOAT_LOWER` - sealed displacement shell, ballast pockets, and sensor-pod attachment.
4. `20_DRY_ELECTRONICS_TUB` - ESP32, sensor interfaces, drivers, regulators, and BMS.
5. `21_SENSOR_CONNECTOR_BAY` - probe cable glands and dry connectors isolated from the main tub.
6. `30_DISPLAY_BEZEL` - clear window, gasket, sun lip, and display supports.
7. `40_BATTERY_HATCH` - top access, gasket, pull ribbon, and four captive M3 screws.
8. `50_SENSOR_FLOW_BLOCK` - 25-35 mL chamber, inlet, pump takeoff, cartridge pilots, and drain slope.
9. `51_PH_CARTRIDGE` - common 54 mm flange plus captured 3/4-inch NPT female insert.
10. `52_EC_CARTRIDGE` - common 54 mm flange plus captured 1/2-inch NPT female insert.
11. `60_PROBE_GUARD` - removable polymer cage below the flow block.
12. `70_PUMP_CRADLE` - elastomer-supported downstream pump mount and cover.
13. `80_VALVE_CASSETTE` - three independent valve pockets, tube labels, and drain path.
14. `90_REFERENCE_COMPONENTS` - non-manufactured proxy bodies for every purchased part.

## Initial master dimensions

| Parameter | Initial value | Purpose |
|---|---:|---|
| Overall plan envelope | 240 x 190 mm | Compact float with room for service clearances |
| Upper dry-deck height | 62 mm | Display, PCBs, and cable bends |
| Float depth | 55 mm | Displacement and low component placement |
| Sensor pod depth below float | 180 mm | Process-probe and guard envelope |
| Structural wall | 3.0 mm | FDM prototype baseline |
| Wet-block minimum wall | 4.0 mm | Screw bosses and leak-test margin |
| Main gasket section | 2.5 mm | Dry-tub perimeter seal |
| Probe centers | 62 mm | Common interface specification |
| Sensor chamber target | 30 mL | Fast flush without crowding probes |
| Main fastener | M3 | Common enclosure hardware |
| Prototype slip clearance | 0.30 mm per side | Removable trays and cartridges |

The parameter file and setup script under `fusion/` contain the same values. Change the parameters first; avoid editing dependent features directly.

## Wet-path layout

Use this order:

`submerged inlet -> bubble-reducing inlet passage -> pH/EC chamber -> sample pump -> submerged return`

The pump is downstream. During sampling the chamber is slightly below ambient pressure. The wet block has its own drain path to the reservoir and has no open route into the dry electronics tub.

Mount both probes vertically from the top of the wet block. Their purchased female threaded inserts are captured inside removable cartridges. The cartridges seal to the wet block through the common pilot O-ring described in `SENSOR_INTERFACE_SPEC.md`.

The flow block mounts to the float with four screws and a keyed locating feature. Its removal must not require separating the main float halves.

The three concentrate supply tubes make the floating unit a tethered float. Route them as one strain-relieved loom through the valve cassette and provide a separate tether eye near the loom exit. The tube pull must react into the float structure rather than the valve barbs. Use a 1 N lateral loom load in the first heel and strain-relief check.

## Dry-zone layout

Place the two 42 x 32 mm sensor boards closest to the connector bay. Keep their BNC/input ends away from pump and valve wiring. Mount boards on nylon standoffs or a removable polymer rail.

Place the battery holder low and on the longitudinal centerline. Put the BMS and regulators beside the battery but outside the battery-removal sweep. The ESP32 antenna faces the outer wall and remains clear of batteries, metal threaded inserts, cable shields, and the display PCB.

Use a separate top battery hatch. Removing the battery must not open the main perimeter gasket. Provide a pull ribbon and a keyed two-pin pack connector.

## Display and controls

- Model the MSP2807 as a 90 x 54 x 12 mm keep-out body.
- Use a separate 1.5-2.0 mm clear polycarbonate window.
- Provide a replaceable window gasket and hard compression stops.
- Start with no external buttons. Reserve one 18 x 35 mm internal flat area for a later membrane or magnetic control.
- Angle the display plane 5 degrees from horizontal for drainage, with a 2 mm raised splash lip.

## Float stability

The master layout uses a 240 x 190 mm rounded planform. At 40 mm average immersion, its bounding-box displacement is about 1.82 L before corner and cavity deductions. The first design target is at least 1.5 L effective displacement at the normal waterline and at least 25 mm freeboard at the expected prototype mass.

Fusion mass properties must be updated with measured part masses. Add four accessible ballast pockets near the lower perimeter. Perform a heel check with a 100 g service load placed at each outer corner; the wet-block vents and dry gasket line must remain above the waterline.

The probe guard extends below the float and may catch on the reservoir. Round its lower edge and make it replaceable. Keep at least 20 mm clearance between probe tips and the bottom of the guard.

## Sealing and fasteners

- Main dry-tub gasket: continuous 2.5 mm silicone cord with 20-25% compression and hard stops.
- Main lid screws: M3 at 35-45 mm pitch, outside the gasket centerline.
- Battery hatch: four captive M3 screws and an independent gasket.
- Sensor cartridges: three M3 screws each on the controlled pitch circle.
- Threaded sensor connection: purchased female insert; never rely on a printed NPT thread as the pressure or alignment surface.
- Cable glands: separate replaceable parts with nuts accessible from the connector bay.
- First prototype target: splash-resistant and leak-testable. Do not claim an IP rating without testing.

Heat-set insert pilot diameters follow the exact insert vendor specification. Maintain at least 2.0 mm material around insert knurls and 3.0 mm from an insert to any wet surface.

## FDM allowances

- General removable fit: 0.30 mm per side.
- Close nonmoving fit: 0.20 mm per side.
- M3 clearance hole: 3.4 mm before printer compensation.
- Minimum printable wall: 2.4 mm; use 3.0 mm structural and 4.0 mm wet-wall baselines.
- Minimum inside radius: 1.5 mm on structural ribs.
- Silicone tube bend radius: at least 12 mm.
- PTFE tube bend radius: at least 20 mm.
- Horizontal O-ring faces: machine or wet-sand flat after printing if required by the leak test.

## Fusion work sequence

### Stage 1 - skeleton and reference envelopes

- Run `fusion/HydroponicsFusionSetup/HydroponicsFusionSetup.py` in a new design.
- Confirm the named components and user parameters were created.
- Build the waterline, float planform, sensor axes, gasket boundary, display plane, and battery axis in `00_MASTER_LAYOUT`.
- Create proxy bodies only; no cosmetic detail.

### Stage 2 - sensor mechanics

- Model the common 54 mm cartridge interface.
- Model the pH and EC insert carriers as separate components.
- Model the chamber, sample passages, pump cradle, and removable guard.
- Verify vertical probe extraction and tool access with the display and lid installed.

### Stage 3 - dry shell and float

- Build the lower displacement shell and upper dry tub from the master sketches.
- Add the main gasket, hard stops, M3 bosses, connector bay, and battery hatch.
- Run section analysis at both probe axes and every gasket corner.

### Stage 4 - internal equipment and service

- Place PCB, battery, display, pump, and valve proxy components.
- Add adjustable rails and cable/tube clips.
- Simulate battery, probe, pump, and valve removal paths.
- Add labels for sample in/out and dosing A/B/pH.

### Stage 5 - checks and exports

- Run interference detection.
- Calculate mass properties and displacement at the design waterline.
- Create an exploded view and component drawing set.
- Export assembly STEP plus per-part STEP and 3MF files.
- Record the Fusion version and parameter revision in the repository.

## Mechanical acceptance criteria

The first CAD iteration is successful when:

- both probe proxies install through purchased-thread cartridge envelopes;
- either cartridge can be removed without splitting the float body;
- probe tips have the clearances specified in the interface document;
- a leak in the sensor block drains to the reservoir rather than the electronics tub;
- the pump, three valves, battery, display, and all PCBs fit with their stated connector/tube bends;
- the battery is removable without opening the main enclosure;
- the calculated normal waterline stays below every dry-zone seal;
- a 1 N lateral pull at the dosing-tube loom does not detach a tube or submerge a dry-zone seal;
- the design contains no inaccessible fastener required for routine service;
- all unverified dimensions remain named parameters rather than buried sketch values.

## Release gates

Final manufacturing geometry waits for:

- caliper sheet and mass for both process probes and both female thread inserts;
- seller drawing and wiring for WTS-SS-1-1-1401;
- confirmed PH8012 connector and cable length;
- measured display glass, PCB, connector overhang, and mounting holes;
- measured pump barb axis and valve dimensions;
- leak test of a printed cartridge/flow-block coupon;
- float displacement and heel test using representative ballast.
