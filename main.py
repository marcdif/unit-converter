from convert import convert
import sys
from utils import normalize_unit, sigfig

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <value> <input_unit> <output_unit>")
        print("Example: python main.py 100 celsius fahrenheit")
        sys.exit(1)
    
    try:
        value = float(sys.argv[1])
        input_unit = normalize_unit(sys.argv[2])
        output_unit = normalize_unit(sys.argv[3])

        if input_unit.get_type() != output_unit.get_type():
            print(f"Error: Cannot convert from {input_unit.get_type().upper()} to {output_unit.get_type().upper()} - incompatible unit types")
            sys.exit(1)
        
        result = convert(value, input_unit, output_unit)

        print(f"{sigfig(value)} {input_unit.format(value)} is {sigfig(result)} {output_unit.format(result)}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
