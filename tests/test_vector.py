from classes.math3d.vector import Vector
import math

def test_vector():
    a = Vec3(1, 2, 3)
    b = Vec3(3, 0, -1)

    print("a =", a)
    print("b =", b)

    print("add :", a.add(b))       # (4, 2, 2)
    print("sub :", a.sub(b))       # (-2, 2, 4)
    print("dot :", a.dot(b))       # 1*3 + 2*0 + 3*(-1) = 0

    n = a.normalize()
    print("normalize(a) =", n)
    print("length =", n.length())  # doit être ≈ 1.0


if __name__ == "__main__":
    test_vector()
