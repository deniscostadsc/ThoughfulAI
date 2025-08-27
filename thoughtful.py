from enum import Enum

BULKY_VOLUME_LIMIT_CM3: int = 1000000
BULKY_DIMENSION_LIMIT_CM: int = 150
HEAVY_MASS_LIMIT_KG: int = 20


class PackageType(Enum):
    SPECIAL = 'SPECIAL'
    STANDARD = 'STANDARD'
    REJECTED = 'REJECTED'


def is_package_bulky(*, width: int, height: int, length: int) -> bool:
    for dimension in [width, height, length]:
        if dimension >= BULKY_DIMENSION_LIMIT_CM:
            return True

    volume = width * height * length
    return volume >= BULKY_VOLUME_LIMIT_CM3


def is_package_heavy(*, mass: int) -> bool:
    return mass >= HEAVY_MASS_LIMIT_KG


def sort(*, width: int, height: int, length: int, mass: int) -> str:
    if is_package_bulky(
        width=width, height=height, length=length
    ) and is_package_heavy(mass=mass):
        return PackageType.REJECTED.value
    if is_package_bulky(
        width=width, height=height, length=length
    ) or is_package_heavy(mass=mass):
        return PackageType.SPECIAL.value
    return PackageType.STANDARD.value
