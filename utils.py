from units import LengthUnit, TemperatureUnit, TimeUnit, Unit


def sigfig(value: float, decimal_precision: float = 2) -> str:
    if value == 0:
        return "0"

    if value.is_integer():
        return str(int(value))

    
    if "e" in f"{value}":
        exponent = int(f"{value}".split("e-")[1])
        sigfigs = f"{value}"[:(decimal_precision + 1)].replace(".", "")
        if "e-" in sigfigs:
            sigfigs = f"{sigfigs}".split("e-")[0]
        string = "0."
        for i in range(1, exponent):
            string = f"{string}0"
        string = f"{string}{sigfigs}"
        return string

    formatted = f"{value:.10g}"
    if "." in formatted:
        integer_part, decimal_part = formatted.split(".")
        truncated_decimal = ""
        last = -1
        for digit in decimal_part:
            if last != -1:
                last -= 1
                truncated_decimal += digit
                if last == 0:
                    break
                else:
                    continue

            truncated_decimal += digit
            if digit == "0":
                continue
            if digit != "0":
                last = decimal_precision
        num = float(f"{integer_part}.{truncated_decimal.rstrip('0')}")
        if len(truncated_decimal) > decimal_precision:
            num = round(num, len(truncated_decimal) - 1)
        return num
    return formatted

def normalize_unit(input: str) -> Unit:
    # Temperature units
    if input == "c" or input == "celsius":
        return TemperatureUnit.CELSIUS
    elif input == "f" or input == "fahrenheit":
        return TemperatureUnit.FAHRENHEIT
    elif input == "k" or input == "kelvin":
        return TemperatureUnit.KELVIN
    # Time units
    elif input == "ms" or input == "millisecond" or input == "milliseconds":
        return TimeUnit.MILLISECOND
    elif input == "s" or input == "second" or input == "seconds":
        return TimeUnit.SECOND
    elif input == "min" or input == "minute" or input == "minutes":
        return TimeUnit.MINUTE
    elif input == "h" or input == "hour" or input == "hours":
        return TimeUnit.HOUR
    elif input == "d" or input == "day" or input == "days":
        return TimeUnit.DAY
    elif input == "w" or input == "week" or input == "weeks":
        return TimeUnit.WEEK
    elif input == "m" or input == "month" or input == "months":
        return TimeUnit.MONTH
    elif input == "y" or input == "year" or input == "years":
        return TimeUnit.YEAR
    elif input == "decade" or input == "decades":
        return TimeUnit.DECADE
    elif input == "century" or input == "centuries":
        return TimeUnit.CENTURY
    elif input == "millennium" or input == "millennia":
        return TimeUnit.MILLENNIUM
    # Length units
    elif input == "in" or input == "inch" or input == "inches":
        return LengthUnit.INCH
    elif input == "ft" or input == "foot" or input == "feet":
        return LengthUnit.FOOT
    elif input == "yd" or input == "yard" or input == "yards":
        return LengthUnit.YARD
    elif input == "mi" or input == "mile" or input == "miles":
        return LengthUnit.MILE
    elif input == "mm" or input == "millimeter" or input == "millimeters":
        return LengthUnit.MILLIMETER
    elif input == "cm" or input == "centimeter" or input == "centimeters":
        return LengthUnit.CENTIMETER
    elif input == "meter" or input == "meters":
        return LengthUnit.METER
    elif input == "km" or input == "kilometer" or input == "kilometers":
        return LengthUnit.KILOMETER
    raise ValueError(f"Unsupported unit: {input}")
