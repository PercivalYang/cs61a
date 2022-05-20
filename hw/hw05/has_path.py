from hw05 import Tree
def has_path(t, term):
    if len(term) == 0:
        return True
    elif t.label == term[0]:
        if len(term) == 1:
            return True
        for branch in t.branches:
            flag = has_path(branch, term[1:])
            if flag:
                return True

    return False


greetings = Tree("h", [Tree("i"), Tree("e", [Tree("l", [Tree("l", [Tree("o")])]), Tree("y")])])
has_path(greetings, "hello")
