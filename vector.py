"""
一个向量类
"""

import math


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        """ print输出格式化 """
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        """ 定义==运算的规则 """
        return self.coordinates == v.coordinates

    def plus(self, other):
        """ 向量加法 """
        new_coordinates = [x + y for x, y in zip(self.coordinates,
                                                 other.coordinates)]

        return Vector(new_coordinates)

    def minus(self, other):
        """ 减法 """
        new_coordinates = [x - y for x, y in zip(self.coordinates,
                                                 other.coordinates)]

        return Vector(new_coordinates)

    def times_scalar(self, other):
        """ 乘法 """
        new_coordinates = [x * other for x in self.coordinates]

        return Vector(new_coordinates)

    def magnitude(self):
        """ 计算向量大小 """

        return math.sqrt(sum([i**2 for i in self.coordinates]))

    def normalized(self):
        """ 计算向量方向 """

        try:
            return self.times_scalar(1.0/self.magnitude())
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot normalized the zero "
                                    "vector!")

    def dot(self, v):
        """ 计算点积 """
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degress=False):
        """ 计算弧度 """
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = math.acos(u1.dot(u2))
            if in_degress:
                degress_per_randian = 180.0 / math.pi
                return angle_in_radians * degress_per_randian
            else:
                return angle_in_radians
        except Exception as e:
            raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        """ 计算是否正交 """
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        """ 是否平行 """
        return (
            self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == math.pi
        )

    def is_zero(self, tolerance=1e-10):
        """ 是否是零向量 """
        return self.magnitude() < tolerance

    def component_parallel_to(self, basis):
        """ 计算投影 """
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)

        except Exception as e:
            raise e

    def cross(self, v):
        """ 向量积 """
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [
                y_1*z_2 - y_2*z_1,
                - (x_1*z_2 - x_2*z_1),
                x_1*y_2 - x_2*y_1
            ]

            return Vector(new_coordinates)

        except ValueError as e:
            msg = str(e)
            if msg == 'need nore than 2values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                v_embedded_in_R3 = Vector(v.coordinates + ('0',))

                return self_embedded_in_R3.cross(v_embedded_in_R3)
            else:
                raise e


if __name__ == '__main__':
    vector = Vector([-0.221, 7.437])
    print(vector.magnitude())

    vector2 = Vector([8.813, -1.331, -6.247])
    print(vector2.magnitude())

    vector3 = Vector([5.581, -2.136])
    print(vector3.normalized())

    vector4 = Vector([1.996, 3.108, -4.554])
    print(vector4.normalized())