# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import misc as module_0


def test_case_0():
    var_0 = module_0.coalesce()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1613.274352
    bool_0 = True
    var_0 = module_0.nthword(bool_0)
    module_0.diffheaders(float_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.diffvalues(none_type_0, none_type_0, none_type_0)


def test_case_3():
    none_type_0 = None
    var_0 = module_0.strjoin(none_type_0)


def test_case_4():
    bytes_0 = b""
    var_0 = module_0.nthword(bytes_0)


def test_case_5():
    bool_0 = False
    str_0 = "K\x0cD<0/\x0b:g;\t"
    var_0 = module_0.typeset(str_0, bool_0)
