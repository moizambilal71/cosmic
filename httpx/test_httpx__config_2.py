# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import httpx._config as module_0
import httpx as module_1


def test_case_0():
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_connections == 100
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


@pytest.mark.xfail(strict=True)
def test_case_1():
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_connections == 100
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20
    none_type_0 = None
    timeout_0 = module_1.Timeout(read=none_type_0, write=none_type_0)


def test_case_2():
    none_type_0 = None
    timeout_0 = module_1.Timeout(
        none_type_0, connect=none_type_0, read=none_type_0, write=none_type_0
    )
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect is None
    assert timeout_0.read is None
    assert timeout_0.write is None
    assert timeout_0.pool is None
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


@pytest.mark.xfail(strict=True)
def test_case_3():
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_connections == 100
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20
    none_type_0 = None
    timeout_0 = module_1.Timeout(connect=none_type_0)


def test_case_4():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    bool_0 = timeout_0.__eq__(timeout_0)
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


def test_case_5():
    int_0 = -2410
    none_type_0 = None
    timeout_0 = module_1.Timeout(
        connect=int_0, read=int_0, write=int_0, pool=none_type_0
    )
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2410
    assert timeout_0.read == -2410
    assert timeout_0.write == -2410
    assert timeout_0.pool is None
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    bool_0 = timeout_0.__eq__(none_type_0)


def test_case_6():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    dict_0 = timeout_0.as_dict()
    bool_0 = timeout_0.__eq__(timeout_0)
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


@pytest.mark.xfail(strict=True)
def test_case_7():
    int_0 = -2410
    none_type_0 = None
    timeout_0 = module_1.Timeout(
        connect=int_0, read=int_0, write=int_0, pool=none_type_0
    )
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2410
    assert timeout_0.read == -2410
    assert timeout_0.write == -2410
    assert timeout_0.pool is None
    str_0 = timeout_0.__repr__()
    module_0.UnsetType(**none_type_0)


def test_case_8():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    str_0 = timeout_0.__repr__()
    bool_0 = timeout_0.__eq__(timeout_0)
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


def test_case_9():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0)
    dict_0 = timeout_1.as_dict()
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )


@pytest.mark.xfail(strict=True)
def test_case_10():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0, connect=int_0, read=int_0, write=int_0)


def test_case_11():
    int_0 = -2410
    none_type_0 = None
    timeout_0 = module_1.Timeout(int_0, read=none_type_0, write=int_0, pool=none_type_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2410
    assert timeout_0.read is None
    assert timeout_0.write == -2410
    assert timeout_0.pool is None
    bool_0 = timeout_0.__eq__(none_type_0)
    str_0 = timeout_0.__repr__()
    dict_0 = timeout_0.as_dict()
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )


@pytest.mark.xfail(strict=True)
def test_case_12():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    str_0 = "k\r?g"
    timeout_1 = module_1.Timeout(connect=str_0, read=int_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0, read=int_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(int_0, connect=timeout_0, read=int_0, write=int_0)
    bool_0 = timeout_0.__eq__(timeout_0)
    bool_1 = timeout_1.__eq__(timeout_0)
    str_0 = timeout_0.__repr__()
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20
    var_0 = module_1.Limits()
    module_0.UnsetType(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    none_type_0 = None
    timeout_1 = module_1.Timeout(int_0, read=none_type_0)
    bool_0 = timeout_1.__eq__(timeout_0)
    module_1.create_ssl_context()


@pytest.mark.xfail(strict=True)
def test_case_16():
    int_0 = -2428
    timeout_0 = module_1.Timeout(int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0, pool=timeout_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0)
    timeout_2 = module_1.Timeout(timeout_0, write=timeout_0)


def test_case_18():
    int_0 = -2367
    tuple_0 = (int_0, int_0, int_0, int_0)
    timeout_0 = module_1.Timeout(tuple_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2367
    assert timeout_0.read == -2367
    assert timeout_0.write == -2367
    assert timeout_0.pool == -2367
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20


@pytest.mark.xfail(strict=True)
def test_case_19():
    str_0 = "t"
    module_1.Proxy(str_0, ssl_context=str_0, auth=str_0)


def test_case_20():
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_connections == 100
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20
    set_0 = set()
    limits_0 = module_1.Limits()
    assert (
        f"{type(limits_0).__module__}.{type(limits_0).__qualname__}" == "httpx.Limits"
    )
    assert limits_0.max_connections is None
    assert limits_0.max_keepalive_connections is None
    assert limits_0.keepalive_expiry == pytest.approx(5.0, abs=0.01, rel=0.01)
    bool_0 = limits_0.__eq__(set_0)


@pytest.mark.xfail(strict=True)
def test_case_21():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(timeout_0)
    limits_0 = module_1.Limits(
        max_connections=int_0,
        max_keepalive_connections=int_0,
        keepalive_expiry=timeout_0,
    )
    bool_0 = limits_0.__eq__(limits_0)
    str_0 = timeout_0.__repr__()
    module_1.Proxy(limits_0, auth=timeout_1)


@pytest.mark.xfail(strict=True)
def test_case_22():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    timeout_1 = module_1.Timeout(int_0, write=timeout_0, pool=int_0)
    bool_0 = timeout_0.__eq__(timeout_1)
    timeout_1.__repr__()


def test_case_23():
    unset_type_0 = module_0.UnsetType()
    assert (
        f"{type(module_0.DEFAULT_TIMEOUT_CONFIG).__module__}.{type(module_0.DEFAULT_TIMEOUT_CONFIG).__qualname__}"
        == "httpx.Timeout"
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.connect == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.read == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.write == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_TIMEOUT_CONFIG.pool == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert (
        f"{type(module_0.DEFAULT_LIMITS).__module__}.{type(module_0.DEFAULT_LIMITS).__qualname__}"
        == "httpx.Limits"
    )
    assert module_0.DEFAULT_LIMITS.max_connections == 100
    assert module_0.DEFAULT_LIMITS.max_keepalive_connections == 20
    assert module_0.DEFAULT_LIMITS.keepalive_expiry == pytest.approx(
        5.0, abs=0.01, rel=0.01
    )
    assert module_0.DEFAULT_MAX_REDIRECTS == 20
    limits_0 = module_1.Limits()
    assert (
        f"{type(limits_0).__module__}.{type(limits_0).__qualname__}" == "httpx.Limits"
    )
    assert limits_0.max_connections is None
    assert limits_0.max_keepalive_connections is None
    assert limits_0.keepalive_expiry == pytest.approx(5.0, abs=0.01, rel=0.01)
    bool_0 = limits_0.__eq__(limits_0)


@pytest.mark.xfail(strict=True)
def test_case_24():
    int_0 = -2428
    timeout_0 = module_1.Timeout(connect=int_0, read=int_0, write=int_0, pool=int_0)
    assert (
        f"{type(timeout_0).__module__}.{type(timeout_0).__qualname__}"
        == "httpx.Timeout"
    )
    assert timeout_0.connect == -2428
    assert timeout_0.read == -2428
    assert timeout_0.write == -2428
    assert timeout_0.pool == -2428
    limits_0 = module_1.Limits()
    limits_1 = module_1.Limits(max_connections=int_0, max_keepalive_connections=int_0)
    bool_0 = limits_0.__eq__(limits_1)
    str_0 = timeout_0.__repr__()
    str_1 = limits_1.__repr__()
    none_type_0 = None
    module_1.Proxy(str_1, headers=none_type_0)
