# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mlxtend.classifier.stacking_classification as module_0
import scipy.interpolate._fitpack_repro as module_1
import scipy.stats.biasedurn as module_2
import numpy.ma.core as module_3


def test_case_0():
    none_type_0 = None
    stacking_classifier_0 = module_0.StackingClassifier(
        none_type_0,
        none_type_0,
        none_type_0,
        none_type_0,
        fit_base_estimators=none_type_0,
    )
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers is None
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is None
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is None
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    stacking_classifier_0 = module_0.StackingClassifier(none_type_0, none_type_0)
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers is None
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is False
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is True
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    stacking_classifier_0.fit(none_type_0, none_type_0)


def test_case_2():
    none_type_0 = None
    stacking_classifier_0 = module_0.StackingClassifier(
        none_type_0,
        none_type_0,
        none_type_0,
        none_type_0,
        fit_base_estimators=none_type_0,
    )
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers is None
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is None
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is None
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(ValueError):
        module_0.StackingClassifier(
            none_type_0,
            none_type_0,
            none_type_0,
            stacking_classifier_0,
            stacking_classifier_0,
            stacking_classifier_0,
            none_type_0,
        )


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    dict_0 = {}
    stacking_classifier_0 = module_0.StackingClassifier(
        none_type_0,
        none_type_0,
        none_type_0,
        none_type_0,
        fit_base_estimators=none_type_0,
    )
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers is None
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is None
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is None
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    stacking_classifier_0.fit(stacking_classifier_0, dict_0, stacking_classifier_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    stacking_classifier_0 = module_0.StackingClassifier(
        none_type_0,
        none_type_0,
        none_type_0,
        none_type_0,
        fit_base_estimators=none_type_0,
    )
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers is None
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is None
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is None
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    stacking_classifier_0.get_params()


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    bunch_0 = module_1.Bunch()
    stacking_classifier_0 = module_0.StackingClassifier(bunch_0, none_type_0)
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert (
        f"{type(stacking_classifier_0.classifiers).__module__}.{type(stacking_classifier_0.classifiers).__qualname__}"
        == "scipy.interpolate._fitpack_repro.Bunch"
    )
    assert stacking_classifier_0.meta_classifier is None
    assert stacking_classifier_0.use_probas is False
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is True
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    stacking_classifier_0.set_params()


@pytest.mark.xfail(strict=True)
def test_case_6():
    var_0 = module_2.__dir__()
    var_1 = module_3.compressed(var_0)
    stacking_classifier_0 = module_0.StackingClassifier(var_0, var_0)
    assert (
        f"{type(stacking_classifier_0).__module__}.{type(stacking_classifier_0).__qualname__}"
        == "mlxtend.classifier.stacking_classification.StackingClassifier"
    )
    assert stacking_classifier_0.classifiers == []
    assert stacking_classifier_0.meta_classifier == []
    assert stacking_classifier_0.use_probas is False
    assert stacking_classifier_0.drop_proba_col is None
    assert stacking_classifier_0.average_probas is False
    assert stacking_classifier_0.verbose == 0
    assert stacking_classifier_0.use_features_in_secondary is False
    assert stacking_classifier_0.store_train_meta_features is False
    assert stacking_classifier_0.use_clones is True
    assert stacking_classifier_0.fit_base_estimators is True
    assert (
        f"{type(module_0.StackingClassifier.named_classifiers).__module__}.{type(module_0.StackingClassifier.named_classifiers).__qualname__}"
        == "builtins.property"
    )
    stacking_classifier_0.fit(var_1, var_1)
