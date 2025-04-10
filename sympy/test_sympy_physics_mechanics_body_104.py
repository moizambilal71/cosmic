# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import sympy.physics.mechanics.body as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1147
    module_0.Body(int_0, frame=int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1845
    module_0.Body(int_0, int_0, frame=int_0, central_inertia=int_0)


def test_case_2():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4Wdv:v"
    module_0.Body(str_0, mass=str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    module_0.Body(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "46]sJ~FAn@S/"
    module_0.Body(str_0, mass=str_0, central_inertia=str_0)


def test_case_6():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.dcm(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_0) == 9
    var_1 = var_0.__repr__()
    with pytest.raises(TypeError):
        body_0.apply_torque(var_0)


def test_case_7():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.__repr__()
    assert (
        var_1
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_2 = body_0.apply_force(var_0)


def test_case_8():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(TypeError):
        body_0.remove_load(body_0)


def test_case_9():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.dcm(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_0) == 9
    var_1 = var_0.__repr__()
    var_2 = body_0.clear_loads()


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "PM)U7"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.__repr__()
    assert (
        var_0
        == "Body('PM)U7', masscenter=PM)U7_masscenter, frame=PM)U7_frame, mass=PM)U7_mass, inertia=Inertia(dyadic=PM)U7_ixx*(PM)U7_frame.x|PM)U7_frame.x) + PM)U7_ixy*(PM)U7_frame.x|PM)U7_frame.y) + PM)U7_izx*(PM)U7_frame.x|PM)U7_frame.z) + PM)U7_ixy*(PM)U7_frame.y|PM)U7_frame.x) + PM)U7_iyy*(PM)U7_frame.y|PM)U7_frame.y) + PM)U7_iyz*(PM)U7_frame.y|PM)U7_frame.z) + PM)U7_izx*(PM)U7_frame.z|PM)U7_frame.x) + PM)U7_iyz*(PM)U7_frame.z|PM)U7_frame.y) + PM)U7_izz*(PM)U7_frame.z|PM)U7_frame.z), point=PM)U7_masscenter))"
    )
    body_0.ang_vel_in(var_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    body_0.kinetic_energy(str_0)


def test_case_12():
    str_0 = 'bc"Pg'
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.apply_force(var_0)


@pytest.mark.xfail(strict=True)
def test_case_13():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.dcm(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_0) == 9
    var_0.__lshift__(body_0)


@pytest.mark.xfail(strict=True)
def test_case_14():
    str_0 = "p]M)u7"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    bool_0 = True
    body_0.masscenter_vel(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_15():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.dcm(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_0) == 9
    var_1 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_1.args == []
    var_2 = body_0.apply_torque(var_1)
    body_0.dcm(var_2)


@pytest.mark.xfail(strict=True)
def test_case_16():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.__repr__()
    assert (
        var_1
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_2 = body_0.dcm(body_0)
    assert (
        f"{type(var_2).__module__}.{type(var_2).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_2) == 9
    var_3 = body_0.apply_force(var_0)
    var_4 = body_0.apply_torque(var_0)
    body_0.kinetic_energy(body_0)


@pytest.mark.xfail(strict=True)
def test_case_17():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = str_0.__repr__()
    body_0.parallel_axis(body_0, body_0)


def test_case_18():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.remove_load()
    with pytest.raises(TypeError):
        body_0.apply_force(var_0)


def test_case_19():
    str_0 = "P\tM)U7"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    with pytest.raises(TypeError):
        body_0.apply_force(body_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_20():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    body_1 = module_0.Body(str_0)
    var_1 = body_0.dcm(body_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_1) == 9
    var_2 = var_1.as_real_imag()
    var_3 = body_0.__repr__()
    assert (
        var_3
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_4 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_4).__module__}.{type(var_4).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_4.args == []
    var_5 = body_0.apply_force(var_4)
    var_6 = body_0.remove_load()
    body_0.kinetic_energy(var_4)


def test_case_21():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.remove_load()
    var_1 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_1.args == []
    var_2 = body_0.apply_force(var_1)
    var_3 = body_0.apply_torque(var_1)


@pytest.mark.xfail(strict=True)
def test_case_22():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.__repr__()
    assert (
        var_0
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_1 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_1).__module__}.{type(var_1).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_1.args == []
    var_2 = body_0.apply_force(var_1, reaction_point=var_1)
    var_3 = body_0.dcm(body_0)
    assert (
        f"{type(var_3).__module__}.{type(var_3).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_3) == 9
    var_4 = var_3.as_real_imag()
    var_5 = body_0.__repr__()
    assert (
        var_5
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_6 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_6).__module__}.{type(var_6).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_6.args == []
    var_7 = body_0.apply_force(var_6)
    var_8 = body_0.remove_load()
    body_0.kinetic_energy(var_6)


@pytest.mark.xfail(strict=True)
def test_case_23():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.apply_torque(var_0)
    var_2 = body_0.__repr__()
    assert (
        var_2
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_3 = body_0.remove_load()
    var_4 = body_0.dcm(body_0)
    assert (
        f"{type(var_4).__module__}.{type(var_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_4) == 9
    var_5 = var_4.__rmul__(var_2)
    var_6 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_6).__module__}.{type(var_6).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_6.args == []
    var_7 = body_0.apply_force(var_6)
    var_0.__divmod__(var_7)


@pytest.mark.xfail(strict=True)
def test_case_24():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    body_0.apply_force(var_0, reaction_body=var_0)


@pytest.mark.xfail(strict=True)
def test_case_25():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.__repr__()
    assert (
        var_1
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_2 = body_0.apply_torque(var_0, body_0)
    var_0.dir(body_0, body_0)


@pytest.mark.xfail(strict=True)
def test_case_26():
    str_0 = "dUb+!pwZ"
    body_0 = module_0.Body(str_0)
    assert (
        f"{type(body_0).__module__}.{type(body_0).__qualname__}"
        == "sympy.physics.mechanics.body.Body"
    )
    assert body_0.points == []
    assert (
        f"{type(module_0.Body.loads).__module__}.{type(module_0.Body.loads).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.x).__module__}.{type(module_0.Body.x).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.y).__module__}.{type(module_0.Body.y).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.z).__module__}.{type(module_0.Body.z).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.inertia).__module__}.{type(module_0.Body.inertia).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.Body.is_rigidbody).__module__}.{type(module_0.Body.is_rigidbody).__qualname__}"
        == "builtins.property"
    )
    var_0 = body_0.ang_vel_in(body_0)
    assert (
        f"{type(var_0).__module__}.{type(var_0).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_0.args == []
    var_1 = body_0.__repr__()
    assert (
        var_1
        == "Body('dUb+!pwZ', masscenter=dUb+!pwZ_masscenter, frame=dUb+!pwZ_frame, mass=dUb+!pwZ_mass, inertia=Inertia(dyadic=dUb+!pwZ_ixx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.x) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.y) + dUb+!pwZ_izx*(dUb+!pwZ_frame.x|dUb+!pwZ_frame.z) + dUb+!pwZ_ixy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.x) + dUb+!pwZ_iyy*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.y) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.y|dUb+!pwZ_frame.z) + dUb+!pwZ_izx*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.x) + dUb+!pwZ_iyz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.y) + dUb+!pwZ_izz*(dUb+!pwZ_frame.z|dUb+!pwZ_frame.z), point=dUb+!pwZ_masscenter))"
    )
    var_2 = body_0.remove_load()
    var_3 = body_0.apply_torque(var_0)
    var_4 = body_0.dcm(body_0)
    assert (
        f"{type(var_4).__module__}.{type(var_4).__qualname__}"
        == "sympy.matrices.dense.MutableDenseMatrix"
    )
    assert len(var_4) == 9
    var_5 = var_4.__repr__()
    var_6 = body_0.masscenter_vel(body_0)
    assert (
        f"{type(var_6).__module__}.{type(var_6).__qualname__}"
        == "sympy.physics.vector.vector.Vector"
    )
    assert var_6.args == []
    var_7 = body_0.apply_force(var_0)
    var_1.__getstate__()
