import math
import sys


#ipython = get_ipython()


#def hide_traceback(exc_tuple=None, filename=None, tb_offset=None,
#                   exception_only=False, running_compiled_code=False):
#    etype, value, tb = sys.exc_info()
#    return ipython._showtraceback(etype, value, ipython.InteractiveTB.get_exception_only(etype, value))


# Uncomment after tests
#ipython.showtraceback = hide_traceback

def count_nodes(l):
    n_nodes = 0
    p = l.base
    while p.next_node is not None:
        p = p.next_node
        n_nodes += 1
    return n_nodes

# No picking
def exercise_7(answers):
    solution = {"question_1": 1, "question_2": 2, "question_3":4,"question_4":2,"question_5":4}
    common_pairs = dict()
    for key in answers:
        if (key in solution and answers[key] == solution[key]):
            common_pairs[key] = answers[key]

    assert len(common_pairs)==5, "You have "+ str(5- len(common_pairs))+" incorrect answer. The answers you were correct are: \n"+str((common_pairs))

    print("Answer is correct. Good Job.")


