from units import LengthUnit, TemperatureUnit, TimeUnit, Unit, UnitType


def convert_temperature(value: float, input_unit: TemperatureUnit, output_unit: TemperatureUnit) -> float:
    # Convert to celsius as base unit
    if input_unit == TemperatureUnit.CELSIUS:
        celsius = value
    elif input_unit == TemperatureUnit.FAHRENHEIT:
        celsius = ((value - 32) * 5) / 9
    elif input_unit == TemperatureUnit.KELVIN:
        celsius = value - 273.15
    else:
        raise ValueError(f"Unsupported input unit: {input_unit}")
    
    # Convert celsius to output unit
    if output_unit == TemperatureUnit.CELSIUS:
        return celsius
    elif output_unit == TemperatureUnit.FAHRENHEIT:
        return ((celsius * 9) / 5) + 32
    elif output_unit == TemperatureUnit.KELVIN:
        return celsius + 273.15
    else:
        raise ValueError(f"Unsupported output unit: {output_unit}")

def convert_time(value: float, input_unit: TimeUnit, output_unit: TimeUnit) -> float:
    # Convert to milliseconds as base unit
    match input_unit:
        case TimeUnit.MILLISECOND:
            milliseconds = value
        case TimeUnit.SECOND:
            milliseconds = value * 1000
        case TimeUnit.MINUTE:
            milliseconds = value * 1000 * 60
        case TimeUnit.HOUR:
            milliseconds = value * 1000 * 60 * 60
        case TimeUnit.DAY:
            milliseconds = value * 1000 * 60 * 60 * 24
        case TimeUnit.WEEK:
            milliseconds = value * 1000 * 60 * 60 * 24 * 7
        case TimeUnit.MONTH:
            milliseconds = value * 1000 * 60 * 60 * 24 * 30
        case TimeUnit.YEAR:
            milliseconds = value * 1000 * 60 * 60 * 24 * 365
        case TimeUnit.DECADE:
            milliseconds = value * 1000 * 60 * 60 * 24 * 365 * 10
        case TimeUnit.CENTURY:
            milliseconds = value * 1000 * 60 * 60 * 24 * 365 * 100
        case TimeUnit.MILLENNIUM:
            milliseconds = value * 1000 * 60 * 60 * 24 * 365 * 1000
        case _:
            raise ValueError(f"Unsupported input unit: {input_unit}")
        
    # Convert milliseconds to output unit
    match output_unit:
        case TimeUnit.MILLISECOND:
            return milliseconds
        case TimeUnit.SECOND:
            return milliseconds / 1000
        case TimeUnit.MINUTE:
            return milliseconds / 1000 / 60
        case TimeUnit.HOUR:
            return milliseconds / 1000 / 60 / 60
        case TimeUnit.DAY:
            return milliseconds / 1000 / 60 / 60 / 24
        case TimeUnit.WEEK:
            return milliseconds / 1000 / 60 / 60 / 24 / 7
        case TimeUnit.MONTH:
            return milliseconds / 1000 / 60 / 60 / 24 / 30
        case TimeUnit.YEAR:
            return milliseconds / 1000 / 60 / 60 / 24 / 365
        case TimeUnit.DECADE:
            return milliseconds / 1000 / 60 / 60 / 24 / 365 / 10
        case TimeUnit.CENTURY:
            return milliseconds / 1000 / 60 / 60 / 24 / 365 / 100
        case TimeUnit.MILLENNIUM:
            return milliseconds / 1000 / 60 / 60 / 24 / 365 / 1000
        case _:
            raise ValueError(f"Unsupported output unit: {input_unit}")

def convert_length(value: float, input_unit: LengthUnit, output_unit: LengthUnit) -> float:
    # Convert to millimeters as base unit
    match input_unit:
        case LengthUnit.INCH:
            millimeters = value * 25.4
        case LengthUnit.FOOT:
            millimeters = value * 25.4 * 12
        case LengthUnit.YARD:
            millimeters = value * 25.4 * 12 * 3
        case LengthUnit.MILE:
            millimeters = value * 25.4 * 12 * 5280
        case LengthUnit.MILLIMETER:
            millimeters = value
        case LengthUnit.CENTIMETER:
            millimeters = value * 10
        case LengthUnit.METER:
            millimeters = value * 1000
        case LengthUnit.KILOMETER:
            millimeters = value * 1000 * 1000
        case _:
            raise ValueError(f"Unsupported input unit: {input_unit}")

    # Convert millimeters to output unit
    match output_unit:
        case LengthUnit.INCH:
            return millimeters / 25.4
        case LengthUnit.FOOT:
            return millimeters / 25.4 / 12
        case LengthUnit.YARD:
            return millimeters / 25.4 / 12 / 3
        case LengthUnit.MILE:
            return millimeters / 25.4 / 12 / 5280
        case LengthUnit.MILLIMETER:
            return millimeters
        case LengthUnit.CENTIMETER:
            return millimeters / 10
        case LengthUnit.METER:
            return millimeters / 1000
        case LengthUnit.KILOMETER:
            return millimeters / 1000 / 1000
        case _:
            raise ValueError(f"Unsupported output unit: {input_unit}")

def convert(value: float, input_unit: Unit, output_unit: Unit) -> float:
    match input_unit.get_type():
        case UnitType.TEMPERATURE:
            return convert_temperature(value, input_unit, output_unit)
        case UnitType.TIME:
            return convert_time(value, input_unit, output_unit)
        case UnitType.LENGTH:
            return convert_length(value, input_unit, output_unit)
    raise ValueError(f"Unsupported unit: {input_unit}")
