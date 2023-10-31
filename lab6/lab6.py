from calc import *

def exec_program(lst):
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            if is_output(statement):
                print_statement(statement)
            if is_selection(statement):
                if_statement(statement)

def print_statement(print_list):
        print(output_expression(print_list))
    
def if_statement(if_list):
    if is_condition(if_list[1]):
        new = if_list[1] 
        print(condition_left(new), condition_operator(new), condition_right(new))

calc1 = ['calc', ['print', 2], ['print', 4]]
calc2 = ['calc', ['if', [3, '>', 5], ['print', 2], ['print', 4]]]
exec_program(calc2)

['if', [3, '>', 5], ['print', 2], ['print', 4]]