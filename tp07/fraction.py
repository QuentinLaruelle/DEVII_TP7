import pydoc


class Fraction:
    """Class representing a fraction and operations on it

    Author : Q.Laruelle
    Date : December 2022
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num is an integer and by default 0. den is an integer and by default 1.
        POST : /
        RAISES : ZeroDivisionError if den ==0
        """
        self.__num = num
        self.__den = den

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : /
        POST : Return num/den with 2 decimals.
        """
        return str(self.__num)+"/"+str(self.__den)

    def as_mixed_number(self):
        """Return a textual representation of the simplified form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : /
        POST : Return num/den + an integer
        """
        try:
            return str(int(self.__num/self.__den))+" + "+str(self.__num-(int(self.__num/self.__den)*self.__den))+"/"\
                   + str(self.__den)
        except ZeroDivisionError:
            return 0
    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : other is an integer
         POST : Return num/den + other
         """
        try:
            return (self.__num/self.__den)+other
        except ZeroDivisionError:
            return 0

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is an integer
        POST : Return num/den - other
        """
        try:
            return (self.__num/self.__den)-other
        except ZeroDivisionError:
            return 0

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is an integer
        POST : Return num/den * other
        """
        try:
            return (self.__num/self.__den)*other
        except ZeroDivisionError:
            return 0

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is an integer
        POST : Return num/den / other
        """
        try:
            return (self.__num/self.__den)/other
        except ZeroDivisionError:
            return 0

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other is an integer
        POST : Return num/den ** other
        """
        try:
            return (self.__num/self.__den)**other
        except ZeroDivisionError:
            return 0

    def __eq__(self, other):
        """
        Overloading of the == operator for fractions

        PRE : other is an integer
        POST : Return True si other=num/den sinon False

        """
        try:
            return (self.__num/self.__den) == other
        except ZeroDivisionError:
            return 0

    def __float__(self):
        """
        Returns the decimal value of the fraction

        PRE : /
        POST : Return the decimal value of the fraction
        """
        try:
            return self.__num/self.__den
        except ZeroDivisionError:
            return 0

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """
        Check if a fraction's value is 0

        PRE : /
        POST : Return True if num/den=0 else False
        """
        if self.__num == 0:
            return True
        else:
            return False

    def is_integer(self):
        """
        Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : /
        POST : Return True if num/den gives un integer else False
        """

        try:
            if self.__num/self.__den % 1 == 0:
                return True
            else:
                return False
        except ZeroDivisionError:
            return 0

    def is_proper(self):
        """
        Check if the absolute value of the fraction is < 1

        PRE : /
        POST : Return True if |num/den| <1 else False
        """
        try:
            if abs(self.__num/self.__den) < 1:
                return True
            else:
                return False
        except ZeroDivisionError:
            return 0

    def is_unit(self):
        """
        Check if a fraction's numerator is 1 in its reduced form

        PRE : /
        POST : Return True if after being simplified, num == 1 else False
        """
        try:
            if int(self.__num/pgcd(self.__num, self.__den)) == 1:
                return True
            else:
                return False
        except ZeroDivisionError:
            return 0

    def is_adjacent_to(self, other):
        """
        Check if two fractions differ by a unit fraction (1/x)

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other is a float
        POST : Return True if |(num/den)-other| = 1/x else False
        """
        print(other, pgcd(int(other*10), 10), self.__den)
        if 1/other > self.__den:
            for i in range(1, int(1/other)):
                if 1/i == other:
                    print("Trouvé "+str(i))
            print(True)



def pgcd(a, b):
    """
    Calculus of the greatest common divisor with the Euclide algorithm
    :param a: First value , must be greater than B
    :param b: Second value
    :return: The GCD
    """
    r = -1
    while r != 0:
        if b != 0:
            r = a % b
        else:
            r = a
        a, b = b, r
    return a

# pydoc.help()
