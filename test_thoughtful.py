from thoughtful import is_package_bulky, is_package_heavy, sort


def test_is_package_bulky__volume_boundary():
    assert not is_package_bulky(width=100, height=100, length=99)
    assert is_package_bulky(width=100, height=100, length=100)
    assert is_package_bulky(width=100, height=100, length=101)


def test_is_package_bulky__width_dimension_boundary():
    assert not is_package_bulky(width=149, height=1, length=1)
    assert is_package_bulky(width=150, height=1, length=1)
    assert is_package_bulky(width=151, height=1, length=1)


def test_is_package_bulky__height_dimension_boundary():
    assert not is_package_bulky(width=1, height=149, length=1)
    assert is_package_bulky(width=1, height=150, length=1)
    assert is_package_bulky(width=1, height=151, length=1)


def test_is_package_bulky__length_dimension_boundary():
    assert not is_package_bulky(width=1, height=1, length=149)
    assert is_package_bulky(width=1, height=1, length=150)
    assert is_package_bulky(width=1, height=1, length=151)


def test_is_package_heavy__mass_boundary():
    assert not is_package_heavy(mass=19)
    assert is_package_heavy(mass=20)
    assert is_package_heavy(mass=21)


def test_sort__standard_packages():
    assert sort(width=100, height=100, length=99, mass=1) == 'STANDARD'
    assert sort(width=100, height=100, length=99, mass=19) == 'STANDARD'


def test_sort__special_packages():
    assert sort(width=100, height=100, length=100, mass=1) == 'SPECIAL'
    assert sort(width=100, height=100, length=99, mass=20) == 'SPECIAL'


def test_sort__rejected_packages():
    assert sort(width=100, height=100, length=100, mass=20) == 'REJECTED'
    assert sort(width=150, height=1, length=1, mass=20) == 'REJECTED'
    assert sort(width=149, height=149, length=149, mass=20) == 'REJECTED'
