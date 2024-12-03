from units import TemperatureUnit, TimeUnit, Unit

def sigfig(value: float, precision: float = 2) -> str:
    if value == 0:
        return "0"

    if value.is_integer():
        return str(int(value))

    
    if "e" in f"{value}":
        exponent = int(f"{value}".split("e-")[1])
        sigfigs = f"{value}"[:4].replace(".", "")
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
                last = precision
        num = float(f"{integer_part}.{truncated_decimal.rstrip('0')}")
        if len(truncated_decimal) > precision:
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
    raise ValueError(f"Unsupported unit: {input}")
