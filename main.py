import sys

def normalize_unit(input: str) -> str:
    if input == "c":
        input = "celsius"
    elif input == "f":
        input = "fahrenheit"
    elif input == "k":
        input = "kelvin"
    return input

def convert_temperature(value: float, input_unit: str, output_unit: str) -> float:
    input_unit = input_unit.lower()
    output_unit = output_unit.lower()
    
    # Convert to celsius as base unit
    if input_unit == "celsius":
        celsius = value
    elif input_unit == "fahrenheit":
        celsius = ((value - 32) * 5) / 9
    elif input_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unsupported input unit: {input_unit}")
    
    # Convert celsius to output unit
    if output_unit == "celsius":
        return celsius
    elif output_unit == "fahrenheit":
        return ((celsius * 9) / 5) + 32
    elif output_unit == "kelvin":
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
