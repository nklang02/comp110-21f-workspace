"""Learning to program with relational operators"""
__author__ = "730418254"
value_1: str = input("Left-hand side: ")
value_2: str = input("Right-hand side: ")
value_1_int_form: int = int(value_1)
value_2_int_form: int = int(value_2)
print((value_1) + " < " + (value_2) + " is " + str((value_1_int_form) < (value_2_int_form)))
print((value_1) + " >= " + (value_2) + " is " + str((value_1_int_form) >= (value_2_int_form)))
print((value_1) + " == " + (value_2) + " is " + str((value_1_int_form) == (value_2_int_form)))
print((value_1) + " != " + (value_2) + " is " + str((value_1_int_form) != (value_2_int_form)))
