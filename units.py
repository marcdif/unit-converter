from enum import StrEnum, auto


class UnitType(StrEnum):
    TEMPERATURE = auto()
    LENGTH = auto()
    TIME = auto()
    WEIGHT = auto()
    SPEED = auto()

class Unit(StrEnum):
    def get_type(self) -> UnitType:
        raise NotImplementedError("Subclass must implement this method")
    
    def format(self, value) -> str:
        return self

class TemperatureUnit(Unit):
    CELSIUS = auto()
    FAHRENHEIT = auto()
    KELVIN = auto()

    def get_type(self) -> UnitType:
        return UnitType.TEMPERATURE

class TimeUnit(Unit):
    MILLISECOND = auto()
    SECOND = auto()
    MINUTE = auto()
    HOUR = auto()
    DAY = auto()
    WEEK = auto()
    MONTH = auto()
    YEAR = auto()
    DECADE = auto()
    CENTURY = auto()
    MILLENNIUM = auto()

    def get_type(self) -> UnitType:
        return UnitType.TIME
    
    def format(self, value) -> str:
        if value == 1:
            return self;
        else:
            if self == TimeUnit.CENTURY:
                return "centuries"
            elif self == TimeUnit.MILLENNIUM:
                return "millennia"
            else:
                return f"{self}s"

class LengthUnit(Unit):
    # Imperial
    INCH = auto()
    FOOT = auto()
    YARD = auto()
    MILE = auto()

    # Metric
    MILLIMETER = auto()
    CENTIMETER = auto()
    METER = auto()
    KILOMETER = auto()

    def get_type(self) -> UnitType:
        return UnitType.LENGTH
    
    def format(self, value) -> str:
        if value == 1:
            return self;
        else:
            if self == LengthUnit.INCH:
                return "inches"
            elif self == LengthUnit.FOOT:
                return "feet"
            else:
                return f"{self}s"
