# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mlxtend.frequent_patterns.apriori as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    module_0.apriori(none_type_0, max_len=none_type_0)


def test_case_1():
    bool_0 = False
    none_type_0 = None
    with pytest.raises(ValueError):
        module_0.apriori(bool_0, bool_0, low_memory=none_type_0)
