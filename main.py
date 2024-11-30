from enum import StrEnum, auto
import sys

class TemperatureUnit(StrEnum):
    CELSIUS = auto()
    FAHRENHEIT = auto()
    KELVIN = auto()

def normalize_unit(input: str) -> TemperatureUnit:
    if input == "c":
        input = "celsius"
    elif input == "f":
        input = "fahrenheit"
    elif input == "k":
        input = "kelvin"
    return TemperatureUnit[input.upper()]

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

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <value> <input_unit> <output_unit>")
        print("Example: python main.py 100 celsius fahrenheit")
        sys.exit(1)
    
    try:
        value = float(sys.argv[1])
        input_unit = normalize_unit(sys.argv[2])
        output_unit = normalize_unit(sys.argv[3])
        
        result = convert_temperature(value, input_unit, output_unit)
        print(f"{value} {input_unit} is {result:.2f} {output_unit}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
