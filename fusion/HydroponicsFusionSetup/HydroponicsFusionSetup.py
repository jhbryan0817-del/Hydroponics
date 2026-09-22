"""Create the parameter and component skeleton for the hydroponics enclosure."""

import traceback

import adsk.core
import adsk.fusion


PARAMETERS = [
    ("shell_length", "240 mm", "mm", "Overall float plan length"),
    ("shell_width", "190 mm", "mm", "Overall float plan width"),
    ("dry_deck_height", "62 mm", "mm", "Height above float split line"),
    ("float_depth", "55 mm", "mm", "Displacement shell depth"),
    ("sensor_pod_depth", "180 mm", "mm", "Maximum sensor pod depth below float"),
    ("structural_wall", "3.0 mm", "mm", "Default FDM structural wall"),
    ("wet_wall", "4.0 mm", "mm", "Minimum flow-block wall"),
    ("main_gasket_diameter", "2.5 mm", "mm", "Main silicone cord section"),
    ("main_gasket_compression", "0.55 mm", "mm", "Nominal 22 percent compression"),
    ("m3_clearance", "3.4 mm", "mm", "Prototype M3 clearance hole"),
    ("removable_clearance", "0.30 mm", "mm", "Clearance per side for removable FDM parts"),
    ("close_fit_clearance", "0.20 mm", "mm", "Clearance per side for close nonmoving fits"),
    ("probe_center_spacing", "62 mm", "mm", "pH-to-EC axis spacing"),
    ("cartridge_flange_od", "54 mm", "mm", "Common sensor cartridge flange OD"),
    ("cartridge_flange_thickness", "14 mm", "mm", "Common sensor cartridge flange thickness"),
    ("cartridge_pilot_od", "34 mm", "mm", "Common flow-block pilot OD"),
    ("cartridge_pilot_depth", "5 mm", "mm", "Pilot engagement depth"),
    ("cartridge_bolt_pcd", "46 mm", "mm", "Three M3 retention screws"),
    ("ph_probe_proxy_diameter", "32 mm", "mm", "Conservative PH8012 body envelope"),
    ("ph_probe_proxy_length", "165 mm", "mm", "Conservative installed PH8012 envelope"),
    ("ph_service_height", "200 mm", "mm", "Vertical removal clearance"),
    ("ec_probe_proxy_diameter", "30 mm", "mm", "Conservative WTS head/body envelope"),
    ("ec_probe_proxy_length", "180 mm", "mm", "Conservative installed WTS envelope"),
    ("ec_service_height", "200 mm", "mm", "Vertical removal clearance"),
    ("sensor_chamber_target_volume", "30 cm^3", "cm^3", "Target with both probes installed"),
    ("tube_od", "4 mm", "mm", "Sample and dosing tube outside diameter"),
    ("silicone_min_bend_radius", "12 mm", "mm", "Minimum silicone tube bend"),
    ("ptfe_min_bend_radius", "20 mm", "mm", "Minimum PTFE tube bend"),
    ("display_tilt", "5 deg", "deg", "Drainage angle from horizontal"),
    ("normal_immersion", "40 mm", "mm", "Initial waterline depth"),
    ("minimum_freeboard", "25 mm", "mm", "Minimum dry-seal height above waterline"),
]


COMPONENTS = [
    "00_MASTER_LAYOUT",
    "10_FLOAT_UPPER",
    "11_FLOAT_LOWER",
    "20_DRY_ELECTRONICS_TUB",
    "21_SENSOR_CONNECTOR_BAY",
    "30_DISPLAY_BEZEL",
    "40_BATTERY_HATCH",
    "50_SENSOR_FLOW_BLOCK",
    "51_PH_CARTRIDGE",
    "52_EC_CARTRIDGE",
    "60_PROBE_GUARD",
    "70_PUMP_CRADLE",
    "80_VALVE_CASSETTE",
    "90_REFERENCE_COMPONENTS",
]


def _upsert_parameters(design):
    user_parameters = design.userParameters
    for name, expression, unit, comment in PARAMETERS:
        parameter = user_parameters.itemByName(name)
        if parameter:
            parameter.expression = expression
            parameter.comment = comment
        else:
            value = adsk.core.ValueInput.createByString(expression)
            user_parameters.add(name, value, unit, comment)


def _ensure_components(root_component):
    existing = {
        root_component.occurrences.item(index).component.name
        for index in range(root_component.occurrences.count)
    }
    matrix = adsk.core.Matrix3D.create()
    for component_name in COMPONENTS:
        if component_name in existing:
            continue
        occurrence = root_component.occurrences.addNewComponent(matrix)
        occurrence.component.name = component_name


def run(context):
    app = adsk.core.Application.get()
    ui = app.userInterface
    try:
        design = adsk.fusion.Design.cast(app.activeProduct)
        if not design:
            ui.messageBox("Open or create a Fusion design before running this script.")
            return

        _upsert_parameters(design)
        _ensure_components(design.rootComponent)
        ui.messageBox(
            "Hydroponics parameters and root components are ready. "
            "Begin layout work in 00_MASTER_LAYOUT."
        )
    except Exception:
        ui.messageBox("Hydroponics setup failed:\n{}".format(traceback.format_exc()))


def stop(context):
    return
