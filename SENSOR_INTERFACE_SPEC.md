# Sensor interface control specification

This document is the binding mechanical contract between the float body and the replaceable pH/EC sensors. Probe-specific geometry ends at the removable cartridge. Changes outside these limits require a design review.

## Common cartridge-to-flow-block interface

Both sensors use the same outer cartridge interface:

| Feature | Baseline |
|---|---:|
| Cartridge flange outside diameter | 54.0 mm |
| Cartridge flange thickness | 14.0 mm |
| Flow-block pilot diameter | 34.0 mm |
| Pilot engagement | 5.0 mm |
| Retention | 3 x M3 screws on 46.0 mm pitch circle |
| Cartridge body clearance in flow block | 0.30 mm radial for FDM prototype |
| Primary cartridge seal | 2.5 mm circular-section O-ring around the 34 mm pilot |
| Target O-ring compression | 20-25% with a hard stop |
| Sensor center-to-center spacing | 62.0 mm |
| Minimum tool clearance above flange | 38.0 mm diameter |

The O-ring gland dimensions must be recalculated against the purchased O-ring supplier table before a release drawing is issued. The values above define the layout envelope only.

The 54 mm flange, 46 mm screw circle, and 34 mm pilot provide about 2.3 mm of nominal material outside an M3 clearance hole and about 1.8 mm between that hole and the estimated outer edge of a 2.5 mm O-ring. Do not reduce the flange without repeating this clearance check.

The flow block receives a smooth printed pilot and O-ring gland. It does not contain a printed NPT or PG13.5 thread.

## pH cartridge

| Item | Controlled value |
|---|---|
| Target probe | BOQU PH8012 |
| Process thread | 3/4-inch NPT male |
| Purchased insert | 3/4-inch NPT female, maximum 36 mm OD/AF x 32 mm |
| Probe envelope | 27.4 mm maximum body x 161 mm long; 25.6 mm tip housing; 3.5 mm cable |
| CAD proxy | 32 mm diameter x 165 mm below cable bend |
| Vertical removal envelope | 200 mm above installed position |
| Tip clearance | 4 mm radial and 8 mm axial minimum from printed surfaces |
| Cable service loop | 80 mm minimum bend-free length before any tie point |

The purchased female insert is trapped axially in the printed cartridge between a lower shoulder and a bolted retainer. It must be replaceable. Seal the probe thread with the method specified by the probe and insert vendors; do not count the cartridge O-ring as the probe-thread seal.

## EC cartridge

| Item | Controlled value |
|---|---|
| Target probe | Winters WTS-SS-1-1-1401 |
| Cell constant | K=1 |
| Process thread | 1/2-inch NPT male |
| Purchased insert | 1/2-inch NPT female, maximum 30 mm OD/AF x 28 mm |
| Published sensing stem | 13 mm diameter; exact length to confirm |
| CAD proxy | 30 mm diameter x 180 mm total |
| Vertical removal envelope | 200 mm above installed position |
| Tip clearance | 6 mm radial and 10 mm axial minimum from printed surfaces |
| Cable service loop | 80 mm minimum before first tie point |

Do not place a metal guard within 12 mm of the active EC electrode region. The initial probe guard is polymer and open on at least 60% of its side area.

## Sensor chamber

- Target wetted volume: 25-35 mL with both proxy probes installed.
- Chamber is non-pressurized and is upstream of the sample pump.
- Sample inlet enters low and tangentially to discourage bubbles at the sensing tips.
- Pump takeoff leaves from the upper opposite side.
- Provide a 1.5 mm-per-10 mm floor slope toward the drain/takeoff with no trapped high point.
- Keep the pH bulb out of the direct inlet jet.
- Keep the EC active area at least 15 mm from the inlet jet centerline.
- Include a transparent or removable inspection cover on the first prototype sensor block.

## Cable boundary

Probe cables enter a small connector/service bay through individual compression glands. The service bay is separated from the main electronics tub by a second wall. BNC and EC interface connectors remain dry and accessible after removing the service-bay cover.

Do not pot the probe cables into the float body. A sensor replacement must require only:

1. opening the connector-bay cover;
2. disconnecting the probe;
3. loosening its cable gland;
4. removing three cartridge screws;
5. lifting the probe and cartridge vertically.

## Permitted substitutions

A replacement probe may be accepted without changing the float body if:

- it fits inside the defined service and installed envelopes;
- its process thread can be carried by a new 54 mm common cartridge;
- its active region reaches the defined sensing plane;
- its cable can pass through the allocated gland and service loop;
- it does not require a larger tool envelope.

Electrical compatibility is a separate gate and is not granted by mechanical fit.
