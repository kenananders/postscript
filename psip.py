import logging
import math
logging.basicConfig(level = logging.INFO)

op_stack = []
dict_stack = []
dict_stack.append({})
lexical_scoping = False


class ParseFailed(Exception):
    """ Exception while parsing """
    def __init__(self, message):
        super().__init__(message)

class TypeMismatch(Exception):
    """ Exception with types of operators and operands """
    def __init__(self, message):
        super().__init__(message)

class StaticTable:
    def __init__(self, code, definition):
        self.code = code  # The data 
        self.definition = definition  # The dictionary at the time of creation

def isLexical():
    if lexical_scoping:
        print("Lexical Scoping Enabled")
    else:
        print("Dynamic Scoping Enabled")


def repl():
    global lexical_scoping
    while True:
        user_input = input("REPL> ")
        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "printstack":
            print(op_stack)
        elif user_input.lower() == "dynamic":
            lexical_scoping = False
            isLexical()
        elif user_input.lower() == "lexical":
            lexical_scoping = True
            isLexical()
        else:
            process_input(user_input)
        logging.debug(f"Operand Stack: {op_stack}")

def process_boolean(input):
    logging.debug(f"Input to process boolean: {input}")
    if input == "true":
        return True
    elif input == "false":
        return False
    else:
        raise ParseFailed("can't parse it into boolean")
   
def process_number(input):
    logging.debug(f"Input to process number: {input}")
    try:
        float_value = float(input)
        if float_value.is_integer():
            return int(float_value)
        else:
            return float_value
    except ValueError:
        raise ParseFailed("can't parse this into a number")
   
def process_code_block(input):
    logging.debug(f"Input to process number: {input}")
    if len(input) >= 2 and input.startswith("{") and input.endswith("}"):
        code_list = input[1:-1].strip().split()
        if lexical_scoping:
            definition = list(dict_stack)
            return StaticTable(code_list, definition)
        else:
            return code_list
    else:
        raise ParseFailed("can't parse this into a code block")
    
def process_string(input):
    logging.debug(f"Input to process number: {input}")
    if input.startswith("(") and input.endswith(")"):
        return input[1:-1]
    else:
        raise ParseFailed("can't parse this into a string")

def process_name_constant(input):
    logging.debug(f"Input to process number: {input}")
    if input.startswith("/"):
        return input
    else:
        raise ParseFailed("Can't parse into name constant")
   
PARSERS = [
    process_boolean,
    process_number,
    process_code_block,
    process_string,
    process_name_constant
]

def process_constants(input):
    for parser in PARSERS:
        try:
            res = parser(input)
            op_stack.append(res)
            return
        except ParseFailed as e:
            logging.debug(e)
            continue
    raise ParseFailed(f"None of the parsers worked for the input {input}")

# ============================================ START STACK MANIPULATION OPERATIONS ============================================
def exch_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op1)
        op_stack.append(op2)
    else:
        raise TypeMismatch("Not enough operands for operation exch")
   
dict_stack[-1]["exch"] = exch_operation

def pop_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
    else:
        raise TypeMismatch("Not enough operands for operation pop")
   
dict_stack[-1]["pop"] = pop_operation

def copy_operation():
    if len(op_stack) >= 1:
        count = op_stack.pop()
        if count < 0 or len(op_stack) < count or not isinstance(count, int):
            raise TypeMismatch("Not enough operands for operation copy")
        to_copy = op_stack[-count:]
        op_stack.extend(to_copy)
    else:
        raise TypeMismatch("Not enough operands for operation copy")
   
dict_stack[-1]["copy"] = copy_operation

def dup_operation():
    if len(op_stack) >= 1:
        op1 = op_stack[-1]
        op_stack.append(op1)
    else:
        raise TypeMismatch("Not enough operands for operation dup")
   
dict_stack[-1]["dup"] = dup_operation

def clear_operation():
    op_stack.clear()
   
dict_stack[-1]["clear"] = clear_operation

def count_operation(): # Does this print the count or add it to top of stack?
    res = len(op_stack)
    op_stack.append(res)
   
dict_stack[-1]["count"] = count_operation

# ============================================ END STACK MANIPULATION OPERATIONS ============================================

# ============================================ START ARITHMETIC OPERATIONS ============================================
def add_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op1 + op2
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation add")
   
dict_stack[-1]["add"] = add_operation

def div_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if op1 != 0:
            res = op2 / op1 # Backwards?
            op_stack.append(res)
        else:
            op_stack.append(op2)
            op_stack.append(op1)
            raise TypeMismatch("Cannot divide by zero!")
    else:
        raise TypeMismatch("Not enough operands for operation div")
   
dict_stack[-1]["div"] = div_operation

def sub_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op2 - op1 # Backwards?
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation sub")
   
dict_stack[-1]["sub"] = sub_operation

def idiv_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if op1 != 0:
            res = op2 // op1 # Backwards?
            op_stack.append(res)
        else:
            op_stack.append(op2)
            op_stack.append(op1)
            raise TypeMismatch("Cannot divide by zero!")
    else:
        raise TypeMismatch("Not enough operands for operation idiv")
   
dict_stack[-1]["idiv"] = idiv_operation

def mul_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op1 * op2
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation mul")
   
dict_stack[-1]["mul"] = mul_operation

def mod_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        res = op2 % op1
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation mod")
   
dict_stack[-1]["mod"] = mod_operation

def abs_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = abs(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation abs")
   
dict_stack[-1]["abs"] = abs_operation

def neg_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = abs(op1) * -1
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation neg")
   
dict_stack[-1]["neg"] = neg_operation

def ceiling_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = math.ceil(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation ceiling")
   
dict_stack[-1]["ceiling"] = ceiling_operation

def floor_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = math.floor(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation floor")
   
dict_stack[-1]["floor"] = floor_operation

def round_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = round(op1) # Python round - rounded to nearest even integer
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation round")
   
dict_stack[-1]["round"] = round_operation

def sqrt_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        res = math.sqrt(op1)
        op_stack.append(res)
    else:
        raise TypeMismatch("Not enough operands for operation sqrt")
   
dict_stack[-1]["sqrt"] = sqrt_operation

# ============================================ END ARITHMETIC OPERATIONS ============================================

# ============================================ START DICTIONARY OPERATIONS ============================================

def dict_operation():
    if len(op_stack) >= 1:
        size = op_stack.pop()
        if isinstance(size, int):
            empty_dict = {i: None for i in range(size)}
            #empty_dict = {}
            op_stack.append(empty_dict)
    else:
        raise TypeMismatch("Not enough operands for operation dict")
   
dict_stack[-1]["dict"] = dict_operation

def length_operation(): # DO FOR DICT AND STRING
    if len(op_stack) >= 1:
        dict_or_string = op_stack.pop()
        if isinstance(dict_or_string, str):
            op_stack.append(len(dict_or_string))
        elif isinstance(dict_or_string, dict): # Where values aren't 'None' (see 'dict_operation()')
            new_dict = dict_stack[-1]
            count = sum(1 for i in new_dict.values() if i is not None)
            res = count - 45 # 45 elements in the base dictionary
            op_stack.append(res)
        else:
            raise TypeMismatch("Not a dictionary or string")
    else:
        raise TypeMismatch("Not enough operands for operation length")
   
dict_stack[-1]["length"] = length_operation

def maxlength_operation():
    if len(op_stack) >= 1:
        max_dict = op_stack.pop()
        if isinstance(max_dict, dict):
            op_stack.append(len(max_dict))
        else:
            raise TypeMismatch("Not a dictionary")
    else:
        raise TypeMismatch("Not enough operands for operation maxlength")
   
dict_stack[-1]["maxlength"] = maxlength_operation

def begin_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        if isinstance(op1, dict):
            new_scope = op1.copy()
            new_scope.update(dict_stack[-1])
            dict_stack.append(new_scope)
        else:
            raise TypeMismatch("Expected dict for begin")
    else:
        raise TypeMismatch("Not enough operands for operation begin")
    
dict_stack[-1]["begin"] = begin_operation

def end_operation():
    if len(dict_stack) > 1:
        dict_stack.pop()
    else:
        raise TypeMismatch("Not enough operands for operation end")

dict_stack[-1]["end"] = end_operation

# ============================================ END DICTIONARY OPERATIONS ============================================

# ============================================ START STRING OPERATIONS ============================================

def get_operation():
    if len(op_stack) >= 2:
        index = op_stack.pop()
        s = op_stack.pop()
        if isinstance(s, str) and isinstance(index, int):
            op_stack.append(s[index]) # Returns int - unicode? The character? 
        else:
            raise TypeMismatch("Expected string and int for get")
    else:
        raise TypeMismatch("Not enough operands for operation get")
    
dict_stack[-1]["get"] = get_operation

def getinterval_operation():
    if len(op_stack) >= 3:
        count = op_stack.pop()
        index = op_stack.pop()
        s = op_stack.pop()
        if isinstance(s, str) and isinstance(index, int) and isinstance(count, int):
            op_stack.append(s[index:index+count])
        else:
            raise TypeMismatch("Expected string and int and int for getinterval")
    else:
        raise TypeMismatch("Not enough operands for operation getinterval")

dict_stack[-1]["getinterval"] = getinterval_operation

def putinterval_operation():
    if len(op_stack) >= 3:
        s2 = op_stack.pop()
        index = op_stack.pop()
        s1 = op_stack.pop()
        if isinstance(s1, str) and isinstance(index, int) and isinstance(s2, str): # Immutable string? To List:
            s1_list = list(s1)
            s2_list = list(s2)
            s1_list[index:index+len(s2_list)] = s2_list
            op_stack.append("".join(s1_list))
        else:
            raise TypeMismatch("Expected string and int and string for putinterval")
    else:
        raise TypeMismatch("Not enough operands for operation putinterval")

dict_stack[-1]["putinterval"] = putinterval_operation

# ============================================ END STRING OPERATIONS ============================================

# ============================================ START BIT/BOOL OPERATIONS ============================================

def eq_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op1 == op2)
    else:
        raise TypeMismatch("Not enough operands for eq")

dict_stack[-1]["eq"] = eq_operation

def ne_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op1 != op2)
    else:
        raise TypeMismatch("Not enough operands for ne")

dict_stack[-1]["ne"] = ne_operation

def ge_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op2 >= op1)
    else:
        raise TypeMismatch("Not enough operands for ge")

dict_stack[-1]["ge"] = ge_operation

def gt_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op2 > op1)
    else:
        raise TypeMismatch("Not enough operands for gt")

dict_stack[-1]["gt"] = gt_operation

def le_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op2 <= op1)
    else:
        raise TypeMismatch("Not enough operands for le")

dict_stack[-1]["le"] = le_operation

def lt_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        op_stack.append(op2 < op1)
    else:
        raise TypeMismatch("Not enough operands for lt")

dict_stack[-1]["lt"] = lt_operation

def and_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if isinstance(op1, bool) and isinstance(op2, bool):
            op_stack.append(op2 and op1)
        elif isinstance(op1, int) and isinstance(op2, int):
            op_stack.append(op2 & op1)
        else:
            raise TypeMismatch("and expects two bools or two ints")
    else:
        raise TypeMismatch("Not enough operands for and")

dict_stack[-1]["and"] = and_operation

def or_operation():
    if len(op_stack) >= 2:
        op1 = op_stack.pop()
        op2 = op_stack.pop()
        if isinstance(op1, bool) and isinstance(op2, bool):
            op_stack.append(op2 or op1)
        elif isinstance(op1, int) and isinstance(op2, int):
            op_stack.append(op2 | op1)
        else:
            raise TypeMismatch("or expects two bools or two ints")
    else:
        raise TypeMismatch("Not enough operands for or")

dict_stack[-1]["or"] = or_operation

def not_operation():
    if len(op_stack) >= 1:
        op1 = op_stack.pop()
        if isinstance(op1, bool):
            op_stack.append(not op1)
        elif isinstance(op1, int):
            op_stack.append(~op1)
        else:
            raise TypeMismatch("not expects bool or int")
    else:
        raise TypeMismatch("Not enough operands for not")

dict_stack[-1]["not"] = not_operation

def true_operation():
    op_stack.append(True)

dict_stack[-1]["true"] = true_operation

def false_operation():
    op_stack.append(False)

dict_stack[-1]["false"] = false_operation


# ============================================ END BIT/BOOL OPERATIONS ============================================

# ============================================ START FLOW CONTROL OPERATIONS ============================================

def if_operation():
    if len(op_stack) >= 2:
        proc = op_stack.pop()
        condition = op_stack.pop()
        if isinstance(condition, bool) and isinstance(proc, list):
            if condition:
                for item in proc:
                    process_input(item)
        else:
            raise TypeMismatch("if expects (bool proc) on the stack")
    else:
        raise TypeMismatch("Not enough operands for if operation")

dict_stack[-1]["if"] = if_operation

def ifelse_operation():
    if len(op_stack) >= 3:
        proc2 = op_stack.pop()
        proc1 = op_stack.pop()
        condition = op_stack.pop()
        if isinstance(condition, bool) and isinstance(proc1, list) and isinstance(proc2, list):
            proc = proc1 if condition else proc2
            for item in proc:
                process_input(item)
        else:
            raise TypeMismatch("ifelse expects (bool proc1 proc2) on the stack")
    else:
        raise TypeMismatch("Not enough operands for ifelse operation")

dict_stack[-1]["ifelse"] = ifelse_operation

def for_operation():
    if len(op_stack) >= 4:
        proc = op_stack.pop()
        l = op_stack.pop()
        k = op_stack.pop()
        j = op_stack.pop()
        if all(isinstance(x, (int, float)) for x in [j, k, l]) and isinstance(proc, list):
            i = j
            if k > 0:
                while i <= l:
                    #op_stack.append(i)
                    for item in proc:
                        process_input(item)
                    i += k
            else:
                while i >= l:
                    #op_stack.append(i)
                    for item in proc:
                        process_input(item)
                    i += k
        else:
            raise TypeMismatch("for expects (start step end proc) on the stack")
    else:
        raise TypeMismatch("Not enough operands for for operation")

dict_stack[-1]["for"] = for_operation

def repeat_operation():
    if len(op_stack) >= 2:
        proc = op_stack.pop()
        n = op_stack.pop()
        if isinstance(n, int) and isinstance(proc, list):
            for _ in range(n):
                for item in proc:
                    process_input(item)
        else:
            raise TypeMismatch("repeat expects (n proc) on the stack")
    else:
        raise TypeMismatch("Not enough operands for repeat operation")

dict_stack[-1]["repeat"] = repeat_operation


# ============================================ END FLOW CONTROL OPERATIONS ============================================

# ============================================ START I/O OPERATIONS ============================================

def print_operation():
    if (len(op_stack) >= 1):
        string = op_stack.pop()
        if not isinstance(string, str):
            raise TypeMismatch("print expects string")
        print(string)
    else:
        raise TypeMismatch("Not enough operands for operation print")

dict_stack[-1]["print"] = print_operation

def equal_print_operation():
    if (len(op_stack) >= 1):
        op1 = op_stack.pop()
        print(op1)
    else:
        raise TypeMismatch("Stack is empty! nothing to print")

dict_stack[-1]["="] = equal_print_operation

def postscript_print_operation():
    if (len(op_stack) >= 1):
        op1 = op_stack.pop()
        print(f"({op1})")
    else:
        raise TypeMismatch("Stack is empty! nothing to print")

dict_stack[-1]["=="] = postscript_print_operation

# ============================================ END I/O OPERATIONS ============================================

def lookup_in_dictionary(name, definition=None):
    if lexical_scoping and definition: # definition = the dictionary at the state of declaration (see StaticTable class)
        for d in reversed(definition):
            if name in d:
                return d[name]
    else: # Dynamic
        for d in reversed(dict_stack):
            if name in d:
                return d[name]
    raise NameError(f"Name {name} not found")

def def_operation():
    if len(op_stack) >= 2:
        value = op_stack.pop()
        name = op_stack.pop()
        if isinstance(name, str) and name.startswith("/"):
            key = name[1:]
            dict_stack[-1][key] = value
        else:
            op_stack.append(name)
            op_stack.append(value)
    else:
        raise TypeMismatch("Not enough operands for operation def")

dict_stack[-1]["def"] = def_operation

def lookup_helper(input):
    global dict_stack
    if callable(input):
        input()
    elif isinstance(input, list):
        for item in input:
            process_input(item)
    elif isinstance(input, StaticTable):
        old_dict_stack = list(dict_stack.copy())

        if lexical_scoping:
            dict_stack = list(input.definition)
        else:
            dict_stack = list(dict_stack)
        for token in input.code:
            process_input(token)
        dict_stack = old_dict_stack
    else:
        op_stack.append(input)

def process_input(user_input):
    try:
        process_constants(user_input)
    except ParseFailed as e:
        logging.debug(e)
        try:
            value = lookup_in_dictionary(user_input)
            lookup_helper(value)
        except Exception as e:
            logging.error(e)


if __name__ == "__main__":
    repl()