from typ import Point
import input
import enhance

from debug import p
from pprint import pp


def t_1():
    algo, img = input.parse_input(input.get_info_from_file("ex_input.txt"))
    enhancer = enhance.Enhancer(img, algo)

    enhancer.execute()
    enhancer.execute()
    assert enhancer.count_pixels() == 35

    algo, img = input.parse_input()
    enhancer = enhance.Enhancer(img, algo)
    enhancer.execute()
    enhancer.execute()
    assert enhancer.count_pixels() == 5229


t_1()


def t_2():

    algo, img = input.parse_input()
    enhancer = enhance.Enhancer(img, algo)
    for _ in range(50):
        print(_)
        enhancer.execute()
    print(enhancer.img)
    assert enhancer.count_pixels() == 17009


t_2()
