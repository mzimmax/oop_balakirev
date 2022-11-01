from Box3D import Box3D


def test_add():
    box1, box2 = Box3D(1, 2, 3), Box3D(2, 4, 6)
    res1 = box1 + box2
    res2 = box2 + box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width + box2.width
    assert res1.height == res2.height == box1.height + box2.height
    assert res1.depth == res2.depth == box1.depth + box2.depth


def test_add_float():
    box1 = Box3D(1, 2, 3)
    constant = 4.75
    res1 = box1 + constant
    res2 = constant + box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width + constant
    assert res1.height == res2.height == box1.height + constant
    assert res1.depth == res2.depth == box1.depth + constant


def test_multiply():
    box1 = Box3D(1, 2, 3)
    constant = 4.1
    res1 = box1 * constant
    res2 = constant * box1

    assert type(res1) is Box3D
    assert type(res2) is Box3D
    assert res1.width == res2.width == box1.width * constant
    assert res1.height == res2.height == box1.height * constant
    assert res1.depth == res2.depth == box1.depth * constant


def test_subtract():
    box1, box2 = Box3D(1, 2, 3), Box3D(2, 4, 6)
    res1 = box2 - box1

    assert type(res1) is Box3D
    assert res1.width == box2.width - box1.width
    assert res1.height == box2.height - box1.height
    assert res1.depth == box2.depth - box1.depth


def test_floordiv():

    box1 = Box3D(53, 7, 28)
    constant = 12
    res1 = box1 // constant

    assert type(res1) is Box3D
    assert res1.width == box1.width // constant
    assert res1.height == box1.height // constant
    assert res1.depth == box1.depth // constant


def test_mod():
    box1 = Box3D(53, 7, 28)
    constant = 12
    res1 = box1 % constant

    assert type(res1) is Box3D
    assert res1.width == box1.width % constant
    assert res1.height == box1.height % constant
    assert res1.depth == box1.depth % constant

test_add()
test_mod()
test_floordiv()
# test_subtract()
test_multiply()
test_add_float()