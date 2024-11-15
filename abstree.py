from msilib import Binary
from print_color import print
import math

###############
# VALUE NODES #
###############

class Number():
    def __init__(self, val):
        self.value = val

    def eval(self, context):
        return int(self.value)

class Single():
    def __init__(self, value):
        self.value = value

class BinaryPair():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class TrinarySet():
    def __init__(self, left, middle, right):
        self.left = left
        self.middle = middle
        self.right = right

####################
# ARITHMETIC NODES #
####################

class Float(BinaryPair):
    def eval(self, context):
        return float(f"{self.left.getstr()}.{self.right.getstr()}")

###############
#  OP  NODES  #
###############

class Sin(Single):
    def eval(self, context):
        return math.sin(self.value.eval(context))

class Cos(Single):
    def eval(self, context):
        return math.cos(self.value.eval(context))


class Negate(Single):
    def eval(self, context):
        return - self.value.eval(context)

class Sum(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)


class Sub(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)


class Mul(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)


class Div(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) / self.right.eval(context)


class Mod(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) % self.right.eval(context)

class Exp(BinaryPair):
    def eval(self, context):
        return self.left.eval(context) ** self.right.eval(context)


##################
#  OUTPUT NODES  #
##################

class Print():
    def __init__(self, val):
        self.value = val

    def eval(self, context):
        print(self.value.eval(context), color='white', tag="TIA", tag_color="green")

##################
# VARIABLE NODES #
##################

class Assignment:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def eval(self, context):
        context[self.var_name] = self.value.eval(context)   # ASSIGN THE VALUE TO THE SYMBOL TABLE


class Variable:
    def __init__(self, var_name):
        self.var_name = var_name

    def eval(self, context):
        if self.var_name in context:   # SEARCH SYMBOL TABLE FOR VARIABLE NAME, RETURN RESULT OR THROW ERROR
            return context[self.var_name]
        else:
            raise NameError(f"Variable '{self.var_name}' is not defined.")


##############
# FUNC NODES #
##############

class QSolve(TrinarySet):
    def eval(self, context):
        a = self.left.eval(context)
        b = self.middle.eval(context)
        c = self.right.eval(context)
        return (-b - ((b**2) - 4 * a * c)**0.5) / (2 * a)
