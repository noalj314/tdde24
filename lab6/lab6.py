from calc import *

def exec_program(lst):
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            if is_output(statement):
                print_statement(statement)
            if is_selection(statement):
                if_statement(statement)
            if is_binaryexpr(statement):
                binary_statement(statement)
            if is_constant(statement):
                return statement

def exec_statement(lst):
        if is_output(lst):
            print_statement(lst)
        if is_selection(lst):
            if_statement(lst)
        if is_binaryexpr(lst):
            return binary_statement(lst)
        if is_constant(lst):
            return lst

def print_statement(print_list):
        print(binary_statement(output_expression(print_list)))

def binary_statement(lst):
    result = None
    if isinstance(lst,int):
        return lst
    elif binaryexpr_operator(lst) == '+':
            result = binary_statement(binaryexpr_left(lst)) + binary_statement(binaryexpr_right(lst))
    elif binaryexpr_operator(lst) == '-':
            result = binary_statement(binaryexpr_left(lst)) - binary_statement(binaryexpr_right(lst))
    elif binaryexpr_operator(lst) == '/':
            result = binary_statement(binaryexpr_left(lst)) / binary_statement(binaryexpr_right(lst))
    elif binaryexpr_operator(lst) == '*':
            result = binary_statement(binaryexpr_left(lst)) * binary_statement(binaryexpr_right(lst))
    return result

def if_statement(if_list):
    if is_condition(if_list[1]):
        new = if_list[1] 
        if condition_operator(new) == '>' and binary_statement(condition_left(new)) > binary_statement(condition_right(new)):
            return exec_statement(if_list[2])
        if condition_operator(new) == '<' and binary_statement(condition_left(new)) < binary_statement(condition_right(new)):
            return exec_statement(if_list[2])
        if condition_operator(new) == '=' and binary_statement(condition_left(new)) == binary_statement(condition_right(new)):
            return exec_statement(if_list[2])
        if len(if_list) == 4:
            return exec_statement(if_list[3])
            


calc2 = ['calc', ['if', [[[[2, '*', 3], '-', 1], '+', 1], '=', 6], ['print', 2], ['print', 4]]]
calc3 = ['calc', ['if', [3, '=', 5], ['print', 2], ['print', 4]]]
['if', [8, '>', 5], ['print', 2]]

# STATEMENTS = STATEMENT, STATEMENTS

# STATEMENT = SELECTION | OUTPUT 

# binaryexpr = [['EXPR', '+', 'EXPR'], '+', 'EXPR']

# EXPR = 5 or binaryexpr

# OUTPUT = '[', "'print'", EXPRESSION, ']' 

calc4 = ['calc', ['print', [[[5, '-', [1, '+', 2]], '+', 2], '+', [2, '*', 3]]], ['if', [[[[2, '*', 3], '-', 1], '+', 1], '=', 6], ['print', 2], ['print', 4]], ['if', [3, '=', 5], ['print', 2]]]

exec_program(calc4)