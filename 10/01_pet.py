from stack2 import *
# def show(s)
# def total(.s)
# def inverse(s)
# def noc(x,s)


def is_substack(s1, s2):
    s1_i = inverse(clone(s1))
    s2_i = inverse(clone(s2))

    while not is_empty(s1_i) and not is_empty(s2_i):
        if top(s1_i) != top(s2_i):
            return False
        s1_i = pop(s1_i)
        s2_i = pop(s2_i)
    return is_empty(s1_i)


def overlap(s1, s2):
    s1_i = inverse(clone(s1))
    while not is_empty(s1_i):
        s2 = push(top(s1_i), s2)
        s1_i = pop(s1_i)
    return s2
