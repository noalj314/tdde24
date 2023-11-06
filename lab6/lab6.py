from calc import *


def exec_program(lst):
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            exec_statement(statement)


def exec_statement(lst):
    if is_output(lst):
        print_statement(lst)
    elif is_selection(lst):
        if_statement(lst)
    elif is_binaryexpr(lst):
        return binary_statement(lst)
    elif is_constant(lst):
        return lst


def print_statement(print_list):
    print(output_expression(print_list))


calc1 = ['calc', [4]]
# print_list = ['print', 2 + 4]


# The binary_statement function assumes that the left and right sides of a binary expression are always constants, but they could also be variables or other expressions based on the grammar.
def binary_statement(lst):
    result = None
    if binaryexpr_operator(lst) == "+":
        print(exec_statement(binaryexpr_left(lst)))
        result = exec_statement(binaryexpr_left(lst)) + exec_statement(binaryexpr_right(lst))
    elif binaryexpr_operator(lst) == "-":
        result = binaryexpr_left(lst) - binaryexpr_right(lst)
    elif binaryexpr_operator(lst) == "/":
        result = binaryexpr_left(lst) / binaryexpr_right(lst)
    elif binaryexpr_operator(lst) == "*":
        result = binaryexpr_left(lst) * binaryexpr_right(lst)
    return result


def if_statement(if_list):

    if is_binaryexpr(selection_condition(if_list)):
        if_condition = if_list[1:]
        print(if_list)
        if condition_operator(if_condition) == '>':
            if exec_statement(condition_left(if_condition)) > exec_statement(condition_right(if_condition)):
                return True
            else:
                return False
        if condition_operator(if_condition) == '<':
            if exec_statement(condition_left(if_condition)) < exec_statement(condition_right(if_condition)) :
                return True
            else:
                return False
        if condition_operator(if_condition) == '=':
            if exec_statement(condition_left(if_condition)) == exec_statement(condition_right(if_condition)):
                return True
            else:
                exec_statement(if_list[3])


calc2 = ['calc', ['if', [4, "+", 2], '>', 5], ['print', 2], ['print', 4]]
calc3 = ['calc', ['if', [3, '=', 5], ['print', 2], ['print', 4]]]

exec_program(calc2)