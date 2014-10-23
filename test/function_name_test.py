#encoding: utf-8

from nose.tools import *
import sys
sys.path.append('../lib')


from shopping_list_printer import format_shopping_list




@raises(TypeError)
def test_average_takes_a_list_as_argument():

    format_shopping_list()




def test_average_a_list_with_3_7_5_should_give_5():

    assert_equal(format_shopping_list(["1","3","4"]), "3 items:\n1: 1\n2: 3\n3: 4")


def test_average_a_list_with_3_7_5_6_should_give_5_point_25():

    assert_equal(format_shopping_list(["1"]), "1 item:\n1: 1")


def test_average_a_list_with_3__5_should_give_4():

    assert_equal(format_shopping_list([]), "No items in list")
