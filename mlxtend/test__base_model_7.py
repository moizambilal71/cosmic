# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import _base_model as module_0


def test_case_0():
    base_model_0 = module_0._BaseModel()
    var_0 = base_model_0.get_params(base_model_0)


def test_case_1():
    str_0 = "IO3`Ui3<7TU"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0._BaseModel()
    with pytest.raises(ValueError):
        var_0.set_params(**dict_0)


def test_case_2():
    base_model_0 = module_0._BaseModel()
    var_0 = base_model_0.set_params()


def test_case_3():
    base_model_0 = module_0._BaseModel()
