"""Learning to work with numeric operators, type conversions, and more string concatenations."""
__author__ = "730418254"
variable_1: str = input("Left-hand side: ")
variable_2: str = input("Right-hand side: ")
variable_1_int_form: int = int(variable_1)
variable_2_int_form: int = int(variable_2)
print(((variable_1) + " ** " + (variable_2) + " is ") + str((variable_1_int_form) ** (variable_2_int_form)))
print(((variable_1) + " / " + (variable_2) + " is ") + str((variable_1_int_form) / (variable_2_int_form)))
print(((variable_1) + " // " + (variable_2) + " is ") + str((variable_1_int_form) // (variable_2_int_form)))
print(((variable_1) + " % " + (variable_2) + " is ") + str((variable_1_int_form) % (variable_2_int_form)))