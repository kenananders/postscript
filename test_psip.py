import psip

# Arithmetic Tests
def test_add_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("add")
    assert psip.op_stack[-1] == 3
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("-6")
    psip.process_input("add")
    assert psip.op_stack[-1] == -1
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("6")
    psip.process_input("add")
    assert psip.op_stack[-1] == 1

def test_div_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("div")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("-10")
    psip.process_input("5")
    psip.process_input("div")
    assert psip.op_stack[-1] == -2
    psip.op_stack.clear()
    psip.process_input("-10")
    psip.process_input("-5")
    psip.process_input("div")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("2")
    psip.process_input("3")
    psip.process_input("div")
    assert psip.op_stack[-1] == (2/3)
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("0")
    psip.process_input("div")
    assert psip.op_stack[-1] == 0 and psip.op_stack[-2] == 10

def test_sub_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("sub")
    assert psip.op_stack[-1] == -1
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("2")
    psip.process_input("sub")
    assert psip.op_stack[-1] == 3
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("2")
    psip.process_input("sub")
    assert psip.op_stack[-1] == -7
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("-2")
    psip.process_input("sub")
    assert psip.op_stack[-1] == -3

def test_idiv_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("4.8")
    psip.process_input("idiv")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("-10")
    psip.process_input("5.2")
    psip.process_input("idiv")
    assert psip.op_stack[-1] == -2
    psip.op_stack.clear()
    psip.process_input("-10")
    psip.process_input("-5")
    psip.process_input("idiv")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("2")
    psip.process_input("3")
    psip.process_input("idiv")
    assert psip.op_stack[-1] == 0
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("0")
    psip.process_input("div")
    assert psip.op_stack[-1] == 0 and psip.op_stack[-2] == 10

def test_mul_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("mul")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("2")
    psip.process_input("mul")
    assert psip.op_stack[-1] == 10
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("2")
    psip.process_input("mul")
    assert psip.op_stack[-1] == -10
    psip.op_stack.clear()
    psip.process_input("-5")
    psip.process_input("-2")
    psip.process_input("mul")
    assert psip.op_stack[-1] == 10
    psip.op_stack.clear()
    psip.process_input("0")
    psip.process_input("2")
    psip.process_input("mul")
    assert psip.op_stack[-1] == 0

def test_mod_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("mod")
    assert psip.op_stack[-1] == 1
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("2")
    psip.process_input("mod")
    assert psip.op_stack[-1] == 0

def test_abs_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("abs")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("-2")
    psip.process_input("abs")
    assert psip.op_stack[-1] == 2

def test_neg_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2")
    psip.process_input("neg")
    assert psip.op_stack[-1] == -2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("-2")
    psip.process_input("neg")
    assert psip.op_stack[-1] == -2

def test_ceiling_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2.6")
    psip.process_input("ceiling")
    assert psip.op_stack[-1] == 3
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("2.2")
    psip.process_input("ceiling")
    assert psip.op_stack[-1] == 3

def test_floor_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2.6")
    psip.process_input("floor")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("2.1")
    psip.process_input("floor")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("-4.8")
    psip.process_input("floor")
    assert psip.op_stack[-1] == -5

def test_round_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("2.5")
    psip.process_input("round")
    assert psip.op_stack[-1] == 2
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("2.6")
    psip.process_input("round")
    assert psip.op_stack[-1] == 3

def test_sqrt_operation():
    psip.op_stack.clear()
    psip.process_input("1")
    psip.process_input("49")
    psip.process_input("sqrt")
    assert psip.op_stack[-1] == 7
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("9")
    psip.process_input("sqrt")
    assert psip.op_stack[-1] == 3


# Stack Manipulation tests

def test_exch_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    assert psip.op_stack[-1] == 5 and psip.op_stack[-2] == 10
    psip.process_input("exch")
    assert psip.op_stack[-1] == 10 and psip.op_stack[-2] == 5

def test_pop_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    assert len(psip.op_stack) == 2
    psip.process_input("pop")
    assert len(psip.op_stack) == 1

def test_copy_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("3")
    psip.process_input("3")
    psip.process_input("copy")
    assert len(psip.op_stack) == 6
    assert psip.op_stack[-1] == 3 and psip.op_stack[-2] == 5 and psip.op_stack[-3] == 10 and psip.op_stack[-4] == 3 and psip.op_stack[-5] == 5 and psip.op_stack[-6] == 10

def test_dup_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    assert psip.op_stack[-1] == 5
    psip.process_input("dup")
    assert psip.op_stack[-1] == 5 and psip.op_stack[-2] == 5

def test_clear_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    assert len(psip.op_stack) == 2
    psip.process_input("clear")
    assert len(psip.op_stack) == 0

def test_count_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("count")
    assert psip.op_stack[-1] == 2


# Bit/Bool operators
def test_eq_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("eq")
    assert psip.op_stack[-1] == False
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("10")
    psip.process_input("eq")
    assert psip.op_stack[-1] == True

def test_ne_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("ne")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("10")
    psip.process_input("ne")
    assert psip.op_stack[-1] == False

def test_ge_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("ge")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("10")
    psip.process_input("ge")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("ge")
    assert psip.op_stack[-1] == False

def test_gt_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("gt")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("gt")
    assert psip.op_stack[-1] == False

def test_le_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("le")
    assert psip.op_stack[-1] == False
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("10")
    psip.process_input("le")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("le")
    assert psip.op_stack[-1] == True

def test_lt_operation():
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("5")
    psip.process_input("lt")
    assert psip.op_stack[-1] == False
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("lt")
    assert psip.op_stack[-1] == True

def test_and_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("true")
    psip.process_input("and")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("and")
    assert psip.op_stack[-1] == 0

def test_or_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("true")
    psip.process_input("or")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("10")
    psip.process_input("20")
    psip.process_input("or")
    assert psip.op_stack[-1] == 30

def test_not_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("false")
    psip.process_input("not")
    assert psip.op_stack[-1] == True
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("true")
    psip.process_input("not")
    assert psip.op_stack[-1] == False
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("70")
    psip.process_input("not")
    assert psip.op_stack[-1] == -71
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("-70")
    psip.process_input("not")
    assert psip.op_stack[-1] == 69

def test_true_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("70")
    psip.process_input("true")
    assert psip.op_stack[-1] == True

def test_false_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("10")
    psip.process_input("false")
    assert psip.op_stack[-1] == False


# I/O Tests

def test_print_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string)")
    psip.process_input("(As am I)")
    psip.process_input("print") # Pops
    assert psip.op_stack[-1] == "I am a string"

def test_eqprint_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string)")
    psip.process_input("50.56")
    psip.process_input("=") # Pops
    assert psip.op_stack[-1] == "I am a string"

def test_psprint_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string)")
    psip.process_input("50.56")
    psip.process_input("==")
    assert psip.op_stack[-1] == "I am a string"
    psip.op_stack.clear()
    psip.process_input("(I am a string)")
    psip.process_input("50.56")
    psip.process_input("(As am I)")
    psip.process_input("==")
    assert psip.op_stack[-1] == 50.56


# Flow Control Tests

def test_if_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("{1 2 add}")
    psip.process_input("if")
    assert psip.op_stack[-1] == 3
    psip.op_stack.clear()
    psip.process_input("30")
    psip.process_input("false")
    psip.process_input("{1 2 add}")
    psip.process_input("if")
    assert psip.op_stack[-1] == 30

def test_ifelse_operation():
    psip.op_stack.clear()
    psip.process_input("true")
    psip.process_input("{1 2 add}")
    psip.process_input("{10 20 add}")
    psip.process_input("ifelse")
    assert psip.op_stack[-1] == 3
    psip.op_stack.clear()
    psip.process_input("false")
    psip.process_input("{1 2 add}")
    psip.process_input("{10 20 add}")
    psip.process_input("ifelse")
    assert psip.op_stack[-1] == 30

def test_for_operation():
    psip.op_stack.clear()
    psip.process_input("30")
    psip.process_input("0")
    psip.process_input("1")
    psip.process_input("5")
    psip.process_input("{1 2 add}")
    psip.process_input("for")
    assert psip.op_stack[-1] == 3
    assert psip.op_stack[-2] == 3
    assert psip.op_stack[-3] == 3
    assert psip.op_stack[-4] == 3
    assert psip.op_stack[-5] == 3
    assert psip.op_stack[-6] == 3
    assert psip.op_stack[-7] == 30
  
def test_repeat_operation():
    psip.op_stack.clear()
    psip.process_input("30")
    psip.process_input("5")
    psip.process_input("{1 2 add}")
    psip.process_input("repeat")
    assert psip.op_stack[-1] == 3
    assert psip.op_stack[-2] == 3
    assert psip.op_stack[-3] == 3
    assert psip.op_stack[-4] == 3
    assert psip.op_stack[-5] == 3
    assert psip.op_stack[-6] == 30



# Test String Operators

def test_stringlength_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string!)")
    psip.process_input("length")
    assert psip.op_stack[-1] == 14

def test_get_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string!)")
    psip.process_input("5")
    psip.process_input("get")
    assert psip.op_stack[-1] == 'a'

def test_getinterval_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string!)")
    psip.process_input("5")
    psip.process_input("8")
    psip.process_input("getinterval")
    assert psip.op_stack[-1] == "a string"

def test_putinterval_operation():
    psip.op_stack.clear()
    psip.process_input("(I am a string!)")
    psip.process_input("7")
    psip.process_input("(coffee)")
    psip.process_input("putinterval")
    assert psip.op_stack[-1] == "I am a coffee!"


# Test Dictionary Operators

def test_dict_operation():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("dict")
    created_dict = psip.op_stack[-1]
    assert len(created_dict) == 5
    for v in created_dict.values():
        assert v is None

def test_length_operation_dict():
    psip.op_stack.clear()
    psip.process_input("5")
    psip.process_input("dict")
    psip.process_input("/a")
    psip.process_input("10")
    psip.process_input("def")
    psip.process_input("/b")
    psip.process_input("20")
    psip.process_input("def")
    psip.process_input("length")
    assert psip.op_stack[-1] == 2

def test_maxlength_operation():
    psip.op_stack.clear()
    psip.op_stack.append({"a": None, "b": None, "c": None})
    psip.process_input("maxlength")
    assert psip.op_stack[-1] == 3

def test_begin_operation():
    psip.op_stack.clear()
    psip.dict_stack = [{}]
    psip.dict_stack[-1]["begin"] = psip.begin_operation
    psip.op_stack.append({"a": 2})
    psip.process_input("begin")
    assert len(psip.dict_stack) == 2

def test_end_operation():
    psip.op_stack.clear()
    psip.dict_stack = [{}]
    psip.dict_stack[-1]["end"] = psip.end_operation
    psip.op_stack.append({"b": 1})
    psip.process_input("begin")
    psip.process_input("end")
    assert len(psip.dict_stack) == 1
    assert "b" not in psip.dict_stack[-1]

def test_lookup_operation():
    psip.op_stack.clear()
    psip.process_input("/x")
    psip.process_input("2")
    psip.process_input("def")
    psip.process_input("x")
    assert psip.op_stack[-1] == 2

def test_lexical_subfunction():
    psip.op_stack.clear()
    psip.dict_stack.clear()
    psip.dict_stack.append({})
    psip.lexical_scoping = True
    psip.dict_stack[-1]['x'] = 10
    custom_definition = [{'x': 20}]
    
    result_lexical = psip.lookup_in_dictionary('x', definition=custom_definition)
    assert result_lexical == 20

    psip.lexical_scoping = False
    result_dynamic = psip.lookup_in_dictionary('x')
    assert result_dynamic == 10



# def test_dynamic_operation():
#     psip.op_stack.clear()
#     psip.process_input("/outer")
#     psip.process_input("5")
#     psip.process_input("def")
#     psip.process_input("/func")
#     psip.process_input("{ outer }")
#     psip.process_input("def")
#     psip.process_input("/wrapper")
#     psip.process_input("{ /outer 10 def func }")
#     psip.process_input("def")
#     psip.process_input("wrapper")
#     assert psip.op_stack[-1] == 10

# def test_lexical_operation():
#     psip.op_stack.clear()
#     psip.lexical_scoping = True
#     #print(psip.dict_stack)
#     print("\n\n")
#     psip.process_input("/outer")
#     psip.process_input("5")
#     psip.process_input("def")
#     #print(psip.dict_stack)
#     print("\n\n")
#     psip.process_input("/func")
#     psip.process_input("{ outer }")
#     psip.process_input("def")
#     #print(psip.dict_stack)
#     print("\n\n")
#     psip.process_input("/wrapper")
#     psip.process_input("{ /outer 10 def func }")
#     psip.process_input("def")
#     psip.process_input("wrapper")
#     print(psip.op_stack)
#     #print(psip.dict_stack)
#     #assert psip.op_stack[-1] == 5





# if __name__ == "__main__":
    # test_dynamic_operation()
    # test_lexical_operation()
    # test_lexical_subfunction()