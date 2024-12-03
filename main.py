import sys

from convert import convert
from utils import normalize_unit, sigfig


def main():
    if len(sys.argv) < 4:
        print("Usage: python main.py <value> <input_unit> <output_unit> [decimal_precision=2]")
        print("Example: python main.py 100 celsius fahrenheit [2]")
        print("Result: 100 celsius is 212 fahrenheit")
        sys.exit(1)
    
    try:
        value = float(sys.argv[1])
        input_unit = normalize_unit(sys.argv[2])
        output_unit = normalize_unit(sys.argv[3])

        if len(sys.argv) > 4:
            decimal_precision = int(sys.argv[4])
        else:
            decimal_precision = 2

        if input_unit.get_type() != output_unit.get_type():
            print(f"Error: Cannot convert from {input_unit.get_type().upper()} to {output_unit.get_type().upper()} - incompatible unit types")
            sys.exit(1)
        
        result = convert(value, input_unit, output_unit)

        print(f"{sigfig(value, decimal_precision)} {input_unit.format(value)} is {sigfig(result, decimal_precision)} {output_unit.format(result)}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
