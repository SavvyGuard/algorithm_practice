import random

class BinaryTree(object):
    def __init__(self, value = None, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        return self.get_value()

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def set_right(self, leaf):
        self.right = leaf
        return self.get_right()

    def set_left(self, leaf):
        self.left = leaf
        return self.get_left()

    def as_dict(self):
        if self.left is None and self.right is None:
            return self.value
        else:
            tree_dict = {
                'left': None,
                'value': self.value,
                'right': None
            }
            if self.left is not None:
               tree_dict['left'] = self.left.as_dict()
            if self.right is not None:
               tree_dict['right'] = self.right.as_dict()

        return tree_dict

    def __str__(self):
        return self.as_dict()

def get_random_list_int(list_length = 10, min_int = 0, max_int = 10):
    return [random.randint(min_int, max_int) for i in xrange(list_length)]

def get_random_tree(levels = 10):
    root = BinaryTree(random.randint(0,10))
    if levels == 1:
        return root
    elif levels > 1:
        root.set_left(get_random_tree(levels - 1))
        root.set_right(get_random_tree(levels - 1))
    else:
        raise Exception

    return root
