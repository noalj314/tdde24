from calc import *
def exec_program(lst, dick=None):
    if dick is None:
        dick = {}
    else:
        dick = dick.copy()
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            exec_statement(statement, dick)
        return dick
def exec_statement(lst, dick):
    if is_output(lst):
        print_statement(lst, dick)
    elif is_assignment(lst):
        ass_statement(lst, dick)
    elif is_selection(lst):
        if_statement(lst, dick)
    elif is_input(lst):
        inputer(lst, dick)
    elif is_repetition(lst):
        whiler(lst,dick)
    elif is_condition(lst):
        return if_condition(lst,dick)
    elif is_variable(lst):
        return variable(lst, dick)
    elif is_binaryexpr(lst):
        return binary_statement(lst, dick)
    elif is_constant(lst):
        return lst

def print_statement(print_list, dick):
    if output_expression(print_list) in dick:
        y = dick.get((output_expression(print_list)))
        print(output_expression(print_list) + " =", + y)
    else:
        print(exec_statement(output_expression(print_list),dick))

def inputer(lst,dick):
    return dick.update({input_variable(lst): int(input())})

def variable(lst, dick):
    return dick.get(lst)

def ass_statement(statement, dick):
    return dick.update({assignment_variable(statement): exec_statement(assignment_expression(statement), dick)})

def whiler(lst,dick):
    while exec_statement(repetition_condition(lst), dick):
        for statement in repetition_statements(lst):
            exec_statement(statement, dick)
    return dick

def binary_statement(lst, dick ):
    result = None
    if binaryexpr_operator(lst) == "+":
        result = exec_statement(binaryexpr_left(lst), dick) + exec_statement(binaryexpr_right(lst), dick)
    elif binaryexpr_operator(lst) == "-":
        result = exec_statement(binaryexpr_left(lst), dick) - exec_statement(binaryexpr_right(lst), dick)
    elif binaryexpr_operator(lst) == "/":
        result = exec_statement(binaryexpr_left(lst), dick) / exec_statement(binaryexpr_right(lst) , dick)
    elif binaryexpr_operator(lst) == "*":
        result = exec_statement(binaryexpr_left(lst), dick) * exec_statement(binaryexpr_right(lst) , dick)
    return result

#calc2 = [['if', [10, '>', 5], ['print', 2], ['print', 4]]

def if_condition(lst, dick):
    if condition_operator(lst) == '>':
        if exec_statement(condition_left(lst), dick) > exec_statement(condition_right(lst), dick):
            return True
        else:
            return False
    if condition_operator(lst) == '<':
        if exec_statement(condition_left(lst), dick) < exec_statement(condition_right(lst), dick):
            return True
        else:
            return False
    if condition_operator(lst) == '=':
        if exec_statement(condition_left(lst), dick) == exec_statement(condition_right(lst), dick):
            return True
        else:
            return False

def if_statement(if_list, dick):
    if is_condition(if_list[1]):
        true_print = if_list[2]
        false_print = if_list[3] if selection_has_false_branch(if_list) else None
        if if_condition(if_list[1], dick):
            exec_statement(true_print, dick)
        else:
            exec_statement(false_print, dick)

        """
        if condition_operator(if_condition) == '>':
            if exec_statement(condition_left(if_condition), dick) > exec_statement(condition_right(if_condition), dick):
                exec_statement(true_print, dick)
            elif false_print is not None:
                exec_statement(false_print, dick)
        if condition_operator(if_condition) == '<':
            if exec_statement(condition_left(if_condition), dick) < exec_statement(condition_right(if_condition), dick):
                exec_statement(true_print, dick)
            elif false_print is not None:
                exec_statement(false_print, dick)
        if condition_operator(if_condition) == '=':
            if exec_statement(condition_left(if_condition) , dick) == exec_statement(condition_right(if_condition) , dick):
                exec_statement(true_print, dick)
            elif false_print is not None:
                exec_statement(false_print, dick) 
        """

#calc1 = ['calc', ['set', 'a', 5], ['print', 'a']]
#calc_set2 = ['calc', ['set', 'a', [[[5, '-', [1, '+', 2]], '+', 2], '+', [2, '*', 3]]], ['print', 'a']]
#exec_program(calc_set2)
#calc100 = ['calc', ['set', 'a', 5], ['print', 'a']]
#new_table = exec_program(calc1)
#exec_program(calc1)
#my_table = {'a': 7}
#new_table = exec_program(calc1, my_table)
#print(my_table)
calc10 = ['calc', ['if', [10, '>', 5], [['read', 'x'], ['print', 'x']], ['print', 4]]]
talc2 = ['calc', ['set', 'x', 7],
             ['set', 'y', 12],
            ['set', 'z', ['x', '+', 'y']],
            ['print', 'z']]

calc3 = ['calc', ['read', 'p1'],
         ['set', 'p2', 47],
            ['set', 'p3', 179],
            ['set', 'result', [['p1', '+', 'p2'], '+', 'p3']],
             ['print', 'result']]
calc4 = ['calc', ['read', 'n'],
             ['set', 'sum', 0],
             ['while', ['n', '>', 0],
             ['set', 'sum', ['sum', '+', 'n']],
             ['set', 'n', ['n', '-', 1]]],
             ['print', 'sum']]
exec_program(calc3)
