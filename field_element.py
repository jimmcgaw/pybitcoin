

class FieldElement:
    def __init__(self, number: int, prime: int):
        if number >= prime or number < 0:
            raise ValueError(
                f"{number} is not in field range 0-{prime-1}"
            )
        self.number = number
        self.prime = prime

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        return self.number == other.number and self.prime == other.prime

    def __ne__(self, other) -> bool:
        if other is None:
            return False
        return self.number != other.number or self.prime != other.prime

    def __add__(self, other):
        if not self.prime == other.prime:
            raise TypeError("Field elements are not in same field, cannot add.")
        num = (self.number + other.number) % self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if not self.prime == other.prime:
            raise TypeError("Field elements are not in same field, cannot multiply.")
        num = (self.number * other.number) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        x = exponent % (self.prime - 1)
        n = pow(self.number, x, self.prime)
        return self.__class__(n, self.prime)