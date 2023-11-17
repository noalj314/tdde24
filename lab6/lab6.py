from calc import *

def exec_program(lst, dic=None):
    """Runs a calc program if it has the correct syntax"""
    if dic is None:
        dic = {}
    if is_program(lst):
        statements = program_statements(lst)
        for statement in statements:
            dic = exec_statement(statement, dic)
        return dic
    else:
        raise SyntaxError("Not a program")

def exec_statement(lst, dic):
    """Checks what kind of a statement it is and runs the corresponding function"""
    if is_output(lst):
        return print_statement(lst, dic)
    elif is_assignment(lst):
        return assign_statement(lst, dic)
    elif is_selection(lst):
        return if_statement(lst, dic)
    elif is_input(lst):
        return inputer(lst, dic)
    elif is_repetition(lst):
        return whiler(lst, dic)


def eval_expression(lst, dic):
    if is_variable(lst):
        return variable(lst, dic)
    elif is_binaryexpr(lst):
        return binary_statement(lst, dic)
    elif is_constant(lst):
        return lst
    return dic
    

def print_statement(print_list, dic):
    """Prints a given expression"""
    if output_expression(print_list) in dic:
        y = dic.get((output_expression(print_list)))
        print(output_expression(print_list) + " =", + y)
    else:
        print(eval_expression(output_expression(print_list), dic))
    return dic


def inputer(lst, dic):
    """Gives a variable for which a value shall be inputted"""
    dic_local = dic.copy()
    read_variable = input_variable(lst)
    val = input(f"Enter value for {read_variable}: ")
    int_val = int(val)
    dic_local[read_variable] = int_val
    return dic_local


def binary_statement(lst, dic):
    """Does the math for all statmenets"""
    result = None
    left = eval_expression(binaryexpr_left(lst), dic)
    right = eval_expression(binaryexpr_right(lst), dic)
    if binaryexpr_operator(lst) == "+":
        result = left + right
    elif binaryexpr_operator(lst) == "-":
        result = left - right
    elif binaryexpr_operator(lst) == "/":
        if right == 0:
            raise Exception(f"Division is by zero")
        else:
            result = left / right
    elif binaryexpr_operator(lst) == "*":
        result = left * right
    return result



def variable(statement, dic):
    """Returns the value of given variable"""
    variable_value = dic.get(statement)
    return variable_value
   

def eval_constant(statement,dic):
    return statement


def assign_statement(statement, dic):
    """Assigns a variable the value of an expression"""
    dic_local = dic.copy()
    var = assignment_variable(statement)
    value = eval_expression(assignment_expression(statement), dic_local)
    dic_local[var] = value
    return dic_local


def whiler(lst, dic):
    """Runs a while loop for given condition"""
    while if_condition(repetition_condition(lst), dic_local):
        for statement in repetition_statements(lst):
            dic_local = exec_statement(statement, dic_local) 
    return dic


def if_condition(lst, dic):
    """Returns true or false depending on if a condition is true or false"""
    if is_condition(lst):
        left = eval_expression(condition_left(lst), dic)
        right = eval_expression(condition_right(lst), dic)
        if condition_operator(lst) == '>':
            if left > right:
                return True
            else:
                return False
        if condition_operator(lst) == '<':
            if left < right:
                return True
            else:
                return False
        if condition_operator(lst) == '=':
            if left == right:
                return True
            else:
                return False
        return dic
    else: 
        raise SyntaxError


def if_statement(if_list, dic):
    """If a condition statment is true print the first print statement else print the second if it exists"""
    if eval_statement(if_list,dic):
        do_this = if_list[2]
    else: 
        do_this = if_list[3] if selection_has_false_branch(if_list) else None
    return exec_statement(do_this, dic) if do_this else dic
    

def eval_statement(if_list,dic):
    if is_condition(if_list[1]):
        if if_condition(if_list[1], dic):
            return True
        else: 
            return False
    else:
        raise SyntaxError
    


calc10 = ['calc', ['if', [1 , '>', 5], ['print', 4], ['print', 3]]]
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

