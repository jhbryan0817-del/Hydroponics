# Fusion 360 start package

This folder prepares a blank Fusion design for the first mechanical layout. It does not create finished geometry.

## Files

- `FusionParameters.csv` - authoritative starting parameter table.
- `HydroponicsFusionSetup/HydroponicsFusionSetup.py` - Fusion script that adds or updates the parameters and creates the assembly component structure.
- `HydroponicsFusionSetup/HydroponicsFusionSetup.manifest` - Fusion script metadata.

## Use

1. Create a new Fusion design and save it before running the script.
2. Open **Utilities > Add-Ins > Scripts and Add-Ins**.
3. Add or copy the `HydroponicsFusionSetup` folder into the Fusion API scripts location.
4. Run `HydroponicsFusionSetup` once.
5. Confirm the user parameters and named components were created.
6. Begin sketches only in `00_MASTER_LAYOUT` and derive dependent geometry into the manufacturing components.

Running the script again updates existing parameter expressions and does not duplicate existing named root components.

The CSV is the human-reviewable source of truth. If a value changes in Fusion, update the CSV and the script together in the same commit.
