# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mlxtend.classifier.adaline as module_0


def test_case_0():
    adaline_0 = module_0.Adaline()
    assert (
        f"{type(adaline_0).__module__}.{type(adaline_0).__qualname__}"
        == "mlxtend.classifier.adaline.Adaline"
    )
    assert adaline_0.eta == pytest.approx(0.01, abs=0.01, rel=0.01)
    assert adaline_0.minibatches is None
    assert adaline_0.epochs == 50
    assert adaline_0.random_seed is None
    assert adaline_0.print_progress == 0
