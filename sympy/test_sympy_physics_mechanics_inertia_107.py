# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sympy.physics.mechanics.inertia as module_0
import sympy.physics.vector.frame as module_1
import sympy.physics.vector.point as module_2


def test_case_0():
    str_0 = "R-en-b)<01\x0c%q"
    with pytest.raises(TypeError):
        module_0.inertia(str_0, str_0, str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.Inertia()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"|\xf2\xc0`\x1am\xc0;\xc0\r\x86\xbf\xfbr\xd3\xc5>\x84\xc6"
    none_type_0 = None
    module_0.inertia_of_point_mass(bytes_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Lh"
    module_0.Inertia(*str_0)


def test_case_4():
    str_0 = "\x0bBx#c2\\/akD{z]s4~"
    list_0 = [str_0, str_0, str_0]
    reference_frame_0 = module_1.ReferenceFrame(str_0, variables=list_0)
    none_type_0 = None
    with pytest.raises(TypeError):
        module_0.inertia(reference_frame_0, str_0, list_0, list_0, izx=none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    point_0 = module_2.Point(none_type_0)
    list_0 = [point_0, none_type_0]
    module_0.Inertia(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    none_type_0 = None
    point_0 = module_2.Point(none_type_0)
    list_0 = [point_0, point_0]
    module_0.Inertia(*list_0)
