ifrom calc import *

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
        return exec_output(lst, dic)
    elif is_assignment(lst):
        return exec_assignment(lst, dic)
    elif is_selection(lst):
        return exec_selection(lst, dic)
    elif is_input(lst):
        return exec_input(lst, dic)
    elif is_repetition(lst):
        return exec_repetition(lst, dic)


def eval_expression(lst, dic):
    """Evaluates an expression"""
    if is_variable(lst):
        return eval_variable(lst, dic)
    elif is_binaryexpr(lst):
        return eval_binaryexpr(lst, dic)
    elif is_constant(lst):
        return lst
    return dic
    

def exec_output(print_list, dic):
    """Prints a given expression"""
    if output_expression(print_list) in dic:
        y = dic.get((output_expression(print_list)))
        print(output_expression(print_list) + " =", + y)
    else:
        print(eval_expression(output_expression(print_list), dic))
    return dic


def exec_input(lst, dic):
    """Gives a variable for which a value shall be inputted"""
    dic_local = dic.copy()
    read_variable = input_variable(lst)
    val = input(f"Enter value for {read_variable}: ")
    int_val = int(val)
    dic_local[read_variable] = int_val
    return dic_local


def eval_binaryexpr(lst, dic):
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



def eval_variable(statement, dic):
    """Returns the value of given variable"""
    variable_value = dic.get(statement)
    return variable_value
   

def eval_constant(statement,dic):
    """Evaluates a constant"""
    return statement


def exec_assignment(statement, dic):
    """Assigns a variable the value of an expression"""
    dic_local = dic.copy()
    var = assignment_variable(statement)
    value = eval_expression(assignment_expression(statement), dic_local)
    dic_local[var] = value
    return dic_local


def exec_repetition(lst, dic):
    """Runs a while loop for given condition"""
    while eval_condition(repetition_condition(lst), dic):
        for statement in repetition_statements(lst):
            dic = exec_statement(statement, dic) 
    return dic



def eval_condition(lst, dic):
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


def exec_selection(if_list, dic):
    """If a condition statment is true print the first print statement else print the second if it exists"""
    if eval_condition_final(if_list,dic):
        do_this = selection_true_branch(if_list)
    else: 
        do_this = selection_false_branch(if_list) if selection_has_false_branch(if_list) else None
    return exec_statement(do_this, dic) if do_this else dic
    

def eval_condition_final(if_list,dic):
    """ Evaluates a condition """
    if is_condition(selection_condition(if_list)):
        if eval_condition(selection_condition(if_list), dic):
            return True
        else: 
            return False
    else:
        raise SyntaxError
    


calc10 = ['calc', ['if', [10 , '>', 5], ['print', 4], ['print', 3]]]
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

exec_program(calc10)