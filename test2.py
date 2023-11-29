class Fraction:
    def __init__(self,s ,m):
        self.s = s
        self.m = m

    def sum(self, f2):
        result_s = (self.s * f2.m) + (f2.s *self.m)
        result_m = self.m * f2.m
        result = Fraction(result_s, result_m)
        return result

    def mul(self, f2):
        #result =((self.s * f2.s) / (self.m * f2.m))
        result_s = self.s * f2.s
        result_m = self.m * f2.m
        result = Fraction(result_s, result_m)
        result = Fraction(result_s, result_m)
        return result
        

    def sub(self, f2):
        result_s = (self.s * f2.m)-(f2.s * self.m)
        result_m = (self.m * f2.m)
        result = Fraction(result_s, result_m)
        return result

    def div(self, f2):
        result_s = (self.s * f2.m)
        result_m = (self.m * f2.s)
        result = Fraction(result_s, result_m)
        return result

    def show(self):
        print(self.s, "/", self.m)
   
    def fraction_to_number(self):
        return self.s / self.m
        

f1 = Fraction(2, 3)
f1.show()

f2 = Fraction(4, 5)
f2.show()

#result_m = Fraction.mul(f1, f2)
result_mul = f1.mul(f2)
result_mul.show()

result_sum = f1.sum(f2)
result_sum.show()

result_sub = f1.sub(f2)
result_sub.show()

result_div = f1.div(f2)
result_div.show()


print(f1.fraction_to_number())
print(f2.fraction_to_number())
