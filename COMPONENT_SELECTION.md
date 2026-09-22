# Component selection

This revision treats the sensor mounting system as the product-defining hardware. Prices are planning values from 2026-09-22. No purchase has been made.

## Sensor architecture

The sensing chain has two deliberately separate layers:

1. a replaceable, threaded process probe that defines the wet mechanical interface; and
2. a dry signal-conditioning board that converts the electrochemical signal for the ESP32.

The enclosure is based on the process probes. The interface boards sit on adjustable rails and may change later without changing the wet shell.

### PH-PROBE-01 - BOQU PH8012

Selected variant:

- model PH8012;
- 0-14 pH;
- upper and lower 3/4-inch NPT process threads;
- BNC (Q9) connector option, which uses the pH signal without the optional temperature conductors;
- direct low-noise coaxial cable;
- request a 1 m cable rather than the standard long industrial cable.

The manufacturer drawing gives a 161 mm overall length, 27.4 mm maximum main-body diameter, 25.6 mm tip housing, 3.5 mm cable, and two 22 mm-long 3/4-inch NPT zones. The upper and lower pipe threads allow the probe to be installed without a separate laboratory clamp. It is mechanically more representative of a glass laboratory probe held by an improvised clip.

The target Taobao price is capped at CNY 90. A low advertised quote is not accepted without a photo of the exact variant, current outline drawing, connector, cable length, and confirmation that the quoted item is the complete electrode.

### PH-FE-01 - DFRobot SEN0161-V2 interface

The 42 x 32 mm DFRobot V2 board is retained because it has a documented 3.3-5.5 V input, 0-3.0 V output, BNC probe input, and two-point calibration workflow. The kit includes a laboratory probe; that probe is retained only as a diagnostic spare.

The PH8012/BNC combination still requires a bench compatibility check. A common BNC connector does not by itself prove correct reference construction, cable wiring, or calibration behavior. The mechanical design remains valid if the interface board changes.

### EC-PROBE-01 - Winters WTS-SS-1-1-1401

Selected variant:

- exact model WTS-SS-1-1-1401;
- two-electrode conductivity sensor;
- K=1 cell constant;
- published range 0.1-20,000 uS/cm;
- 1/2-inch NPT process connection;
- 316 stainless sensing body;
- integrated Pt1000;
- request a 1 m cable instead of the standard 10 m cable.

The family data publishes a 13 mm probe stem and both 60 and 120 mm stem lengths, but it does not map those lengths to a complete threaded-outline drawing. Until the seller supplies the drawing for the exact code, Fusion must use a conservative 30 x 180 mm total envelope and 200 mm service-extraction envelope.

The target Taobao quote is capped at CNY 180. If that cap cannot be met, select another K=1, 0-20 mS/cm process cell with a 1/2-inch or 3/4-inch NPT connection and create only a new cartridge insert. Do not remodel the float body.

### EC-FE-01 - Your Cee K=1 analog EC kit

The low-cost board remains in the budget for bench validation. Its stated range is 0-20 mS/cm and its analog output is 0-3.4 V. Route the output through the documented divider before an ESP32 ADC1 input.

The WTS probe is not assumed plug-compatible. Before measurement work begins, verify:

- two-electrode excitation method and frequency;
- acceptable cell constant;
- electrode connection and shield arrangement;
- whether the Pt1000 can be read by the board or needs a separate converter;
- calibration across at least two standards.

The included EC probe is retained as a diagnostic spare. The electronics tray reserves the same 48 x 38 x 24 mm board envelope whether this board is kept or replaced.

## Why NPT process probes were selected

PG13.5 remains a good process-sensor standard, but verified low-cost PG13.5 EC probes consumed too much of the US$150 budget. A known PG13.5 K=1 probe was listed at EUR 85.20 before its cable and interface electronics. The selected NPT probes keep the process-style threaded mounting while preserving enough budget for the controller, display, pump, valves, battery system, and interface boards.

The cartridge system isolates this choice. A later PG13.5 probe requires a different CNY 10-20 insert/cartridge, not a different float body or electronics tub.

## Control and display

### CTRL-01 - Ai-Thinker NodeMCU-32S

The 38-pin CP2102 NodeMCU-32S has enough GPIO for the display, two analog channels, pump, and three valves. The published PCB is 48.26 x 25.40 mm. Fusion uses 55 x 28 x 14 mm to include headers and connector variation. Keep the ESP32 antenna at least 10 mm from batteries, metal fittings, cable shields, and copper pours.

### DISP-01 - MSP2807 2.8-inch SPI TFT

The ILI9341 SPI module uses an 86 x 50 mm PCB and a 57.6 x 43.2 mm active area. It sits behind a separate clear polycarbonate window. The bezel opening remains parameterized until the received glass and viewing area are measured.

## Fluid system

### PUMP-01 - Conjoin CJWP12-AB05A

The 5 V AB05A pump is retained. Published flow is 130-170 mL/min at less than 180 mA. It is mounted after the sensor chamber:

`reservoir inlet -> low-pressure sensor chamber -> sample pump -> submerged return`

This places the sensor chamber under slight suction during a sample cycle. A sealing defect is less likely to push water toward the dry enclosure. The pump remains in an elastomer cradle and is used intermittently.

### VALVE-01 - three normally-closed miniature valves

The three 6 V valves are kept because the requested first prototype specifies valves. Each occupies an independent pocket in a removable cassette. The three fluid paths never merge inside the enclosure.

The concentrate reservoirs remain external, so their three supply tubes form a tether. The valve cassette includes a structural strain-relief point and a separate tether eye; the valve barbs do not carry float-drift loads. Gravity head is still required because a valve does not pump liquid.

This revision intentionally does not make chemical compatibility a design-freeze condition. Mechanical fit, service clearance, tube routing, and leak containment are the current gates. Compatibility testing remains necessary before concentrates are used.

## Power system

Two matched Lishen LR1865SK cells form a 2S pack. A covered holder beneath the top battery hatch allows removal without an external charging port. A 2S protection board remains inside the unit. Two MP1584 modules provide 5 V and 6 V rails.

The battery holder, pump, and valves are placed low and near the centerline. Their mass offsets the top display and keeps the center of gravity below the design waterline.

## Changes from the first BOM

- Replaced both laboratory-style probe envelopes with threaded industrial process probes.
- Added purchased female threaded inserts and removable sensor cartridges.
- Moved the sample pump downstream of the measurement chamber.
- Removed the separate DS18B20 penetration; the EC probe includes Pt1000 and the shell keeps an internal electronics allowance for its converter.
- Removed material-specific chemical acceptance as a CAD blocker.
- Increased the budget from US$100 to US$150 and assigned explicit quote caps to the two process probes.
- Added a Fusion parameter/setup package and sensor interface control document.

## Deliberate limitations

The mechanical design can proceed before electrical compatibility is proved. Automated dosing cannot. The first physical build must use the process probes and purchased thread inserts for fit work, while the included kit probes are used to bring up the electronics separately.

No trustworthy exact STEP model was found for the PH8012 or WTS-SS-1-1-1401. Fusion should use the controlled proxy envelopes until the received parts are measured.
