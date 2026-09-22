# Mechanical inputs for Fusion 360

This is the dimensional and architectural handoff for the next design cycle. Dimensions marked **confirm** must be measured with calipers from the received part before release-quality screw bosses and cutouts are frozen.

## Proposed assembly split

1. **Top bezel** — clear display window, sun hood, button membrane if later required.
2. **Dry electronics tray** — display, ESP32, pH/EC boards, MOSFET driver, regulators, and BMS.
3. **Removable battery hatch** — top-accessed, gasketed, four captive M3 screws, no external charging port.
4. **Float body** — sealed displacement volume with ballast pockets and a high freeboard rim.
5. **Wet sensor pod** — pH, EC, and temperature probe tips in a pump-fed flow cell below the waterline.
6. **Valve cassette** — three independently removable valves, drip tray, and external tube strain relief.

The wet sensor pod and valve cassette must not share an open cavity with the electronics. Any leak must drain to the reservoir rather than enter the dry compartment.

## CAD envelopes

| ID | Published size | Fusion reserve envelope | Mounting approach |
|---|---:|---:|---|
| CTRL-01 | 48.26 x 25.40 mm PCB | 55 x 28 x 14 mm | Socketed 2.54 mm headers or four edge clips; preserve antenna keepout. |
| DISP-01 | 86 x 50 mm PCB; 57.6 x 43.2 mm display area | 90 x 54 x 12 mm | Four internal standoffs; clear window opening based on measured glass, not active area alone. |
| PH-01 board | 42 x 32 mm | 46 x 36 x 18 mm including BNC clearance | M3 nylon standoffs; keep dry and separated from pump/valve wiring. |
| PH-01 probe | diameter not published for this kit | dia 13 x 145 mm **confirm** | Split clamp around body; guard cage around glass bulb; tool-free service access. |
| EC-01 board | 42 x 32 mm | 46 x 36 x 18 mm | M3 nylon standoffs. |
| EC-01 probe | 172 mm long; diameter not published | dia 16 x 180 mm **confirm** | Split clamp; probe tip centered in flow cell. |
| TEMP-01 | seller-specific | dia 6 x 50 mm plus 25 mm cable bend **confirm** | Compression gland into flow cell. |
| PUMP-01 | approximately 39 x 21 x 12 mm | 45 x 25 x 18 mm | Elastomer cradle; barb axis parallel to base; removable cover. |
| VALVE-01 | approximately 23 x 9 x 11 mm | 28 x 15 x 15 mm each plus 20 mm tube bend | Three isolated snap-in or screw-in pockets in cassette. |
| DRV-01 | unpublished | 70 x 55 x 20 mm **confirm** | Slotted tray to tolerate board variation. |
| CELL-01 pair + holder | holder approximately 76 x 41 x 21 mm | 82 x 47 x 27 mm | Low and centered; removable keyed connector; pull ribbon. |
| BMS-01 | unpublished | 40 x 25 x 8 mm **confirm** | Insulated standoffs near battery connector. |
| REG-01 x2 | approximately 22 x 17 x 4 mm each | 28 x 22 x 10 mm each | Ventilated internal clips; trimmer access during commissioning only. |

## Fluid path

The sample inlet and outlet remain submerged. The inlet passes through the CJWP12 pump, then the pH/EC/temperature flow cell, then returns below the waterline. Returning below the surface limits bubbles and aeration near the probes.

The sensing chamber should hold about 20–35 mL, provide smooth flow around both probe tips, and include a drain path with no trapped high points. The pH glass bulb needs a protective cage with at least 2 mm radial clearance from any printed wall.

Three concentrate lines enter the valve cassette separately and leave through three separate outlets. They never merge inside the device. Each line must have a recognizable color or molded label: A, B, and pH correction.

Current port count is eight 4 mm OD tube interfaces:

- sample inlet and outlet: 2;
- concentrate A, B, and pH-correction inlets: 3;
- A, B, and pH-correction outlets: 3.

Add one dedicated cable passage for the temperature probe and serviceable routing for pH/EC probe cables. Do not rely on a printed thread as the only seal around a cable.

## Dry-zone sealing

- Target an IP67-style architecture, with the understanding that a printed prototype is not certified.
- Use a continuous 2.0–2.5 mm silicone gasket in a rectangular groove around the electronics lid.
- Use M3 heat-set inserts or captive nuts outside the gasket centerline, with screw spacing of roughly 35–45 mm.
- Design 20–30% gasket compression with positive hard stops so screws cannot crush the gasket.
- Put the battery hatch on the top face, above the splash line, with its own gasket and four captive M3 screws.
- Put the display behind 1.5–2.0 mm clear polycarbonate with a replaceable perimeter gasket. Do not expose the display PCB.
- Add a protected hydrophobic vent location so heat and pressure cycles do not pump water through seals.

## FDM prototype tolerances

These are starting values for a 0.4 mm nozzle and must be tuned to the selected printer/material:

- slip-fit removable tray clearance: 0.30 mm per side;
- close nonmoving fit: 0.20 mm per side;
- screw clearance: M3 hole 3.4 mm before printer compensation;
- heat-set insert boss: follow insert vendor pilot diameter; keep at least 2.0 mm wall around insert;
- minimum structural wall: 2.4 mm;
- wet-manifold wall: 3.0 mm minimum with 4–5 perimeters;
- tube bend radius: at least 5 x tube OD for PTFE and 3 x tube OD for silicone/FKM;
- gasket groove corner radius: at least 1.5 x gasket cross-section radius.

## Stability and buoyancy inputs

Keep the battery, pump, and valves below the display/electronics plane and near the geometric center. The tall pH and EC probes should extend downward from the wet pod and act as low ballast, but their fragility requires a perimeter guard.

Do not finalize displacement until the assembled component mass is measured. Initial Fusion work should parameterize payload mass, waterline, and freeboard. Use at least a 2.0 safety factor on displaced mass for a hand-built prototype and reserve ballast pockets so the display face can be leveled after assembly.

## CAD readiness gates

Detailed Fusion features may begin from the reserve envelopes. Final cutouts, probe clamps, and screw patterns wait for:

- seller confirmation of NodeMCU revision and display variant;
- caliper measurement of all received PCBs, connectors, and probe diameters;
- valve wetted-material confirmation and chemical testing;
- final decision on gravity-fed reservoirs versus dosing pumps;
- a bench flow test that establishes tube size, sample chamber volume, and pump orientation.

No trustworthy exact STEP model was found for the selected display, pump, EC kit, or valves. The downloaded manufacturer drawings are the correct basis for simple parameterized envelope components. A third-party 3D model with a similar product name should not be used for final fits.

