from calc import *
def exec_program(lst, dic=None):
    if dic is None:
        dic = {}
    else:
        dic = dic.copy()
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            exec_statement(statement, dic)
        return dic
def exec_statement(lst, dic):
    if is_output(lst):
        print_statement(lst, dic)
    elif is_assignment(lst):
        ass_statement(lst, dic)
    elif is_selection(lst):
        if_statement(lst, dic)
    elif is_input(lst):
        inputer(lst, dic)
    elif is_repetition(lst):
        whiler(lst,dic)
    elif is_condition(lst):
        return if_condition(lst,dic)
    elif is_variable(lst):
        return variable(lst, dic)
    elif is_binaryexpr(lst):
        return binary_statement(lst, dic)
    elif is_constant(lst):
        return lst

def print_statement(print_list, dic):
    if output_expression(print_list) in dic:
        y = dic.get((output_expression(print_list)))
        print(output_expression(print_list) + " =", + y)
    else:
        print(exec_statement(output_expression(print_list),dic))

def inputer(lst,dic):
    z = input()
    if z == '':
        raise ValueError("hej")
    else:
        z = int(z)
    return dic.update({input_variable(lst): z})

def variable(lst, dic):
    return dic.get(lst)

def ass_statement(statement, dic):
    return dic.update({assignment_variable(statement): exec_statement(assignment_expression(statement), dic)})

def whiler(lst,dic):
    while exec_statement(repetition_condition(lst), dic):
        for statement in repetition_statements(lst):
            exec_statement(statement, dic)
    return dic

def binary_statement(lst, dic ):
    result = None
    if binaryexpr_operator(lst) == "+":
        result = exec_statement(binaryexpr_left(lst), dic) + exec_statement(binaryexpr_right(lst), dic)
    elif binaryexpr_operator(lst) == "-":
        result = exec_statement(binaryexpr_left(lst), dic) - exec_statement(binaryexpr_right(lst), dic)
    elif binaryexpr_operator(lst) == "/":
        result = exec_statement(binaryexpr_left(lst), dic) / exec_statement(binaryexpr_right(lst) , dic)
    elif binaryexpr_operator(lst) == "*":
        result = exec_statement(binaryexpr_left(lst), dic) * exec_statement(binaryexpr_right(lst) , dic)
    return result

#calc2 = [['if', [10, '>', 5], ['print', 2], ['print', 4]]

def if_condition(lst, dic):
    if condition_operator(lst) == '>':
        if exec_statement(condition_left(lst), dic) > exec_statement(condition_right(lst), dic):
            return True
        else:
            return False
    if condition_operator(lst) == '<':
        if exec_statement(condition_left(lst), dic) < exec_statement(condition_right(lst), dic):
            return True
        else:
            return False
    if condition_operator(lst) == '=':
        if exec_statement(condition_left(lst), dic) == exec_statement(condition_right(lst), dic):
            return True
        else:
            return False

def if_statement(if_list, dic):
    if is_condition(if_list[1]):
        true_print = if_list[2]
        false_print = if_list[3] if selection_has_false_branch(if_list) else None
        if if_condition(if_list[1], dic):
            exec_statement(true_print, dic)
        else:
            exec_statement(false_print, dic)

        """
        if condition_operator(if_condition) == '>':
            if exec_statement(condition_left(if_condition), dic) > exec_statement(condition_right(if_condition), dic):
                exec_statement(true_print, dic)
            elif false_print is not None:
                exec_statement(false_print, dic)
        if condition_operator(if_condition) == '<':
            if exec_statement(condition_left(if_condition), dic) < exec_statement(condition_right(if_condition), dic):
                exec_statement(true_print, dic)
            elif false_print is not None:
                exec_statement(false_print, dic)
        if condition_operator(if_condition) == '=':
            if exec_statement(condition_left(if_condition) , dic) == exec_statement(condition_right(if_condition) , dic):
                exec_statement(true_print, dic)
            elif false_print is not None:
                exec_statement(false_print, dic) 
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
#exec_program(calc3)
