class Time:
    def __init__(self,day, h, m, s):
        self.s = s
        self.m = m
        self.h = h
        self.day =day

    def sum(self, time2):
        result_day = self.day + time2.day
        result_h = self.h + time2.h
        result_m = self.m + time2.m
        result_s = self.s + time2.s

        while result_s >= 60:
            result_s -= 60
            result_m += 1

        while result_m >= 60:
            result_m -= 60
            result_h += 1
        
        while result_h >= 24:
            result_h -= 24
            result_day += 1

        result = Time(result_day, result_h, result_m, result_s)
        return result
    
    def sub(self, time2):
        result_day = abs(self.day - time2.day)
        result_h = abs(self.h - time2.h)
        result_m = abs(self.m - time2.m)
        result_s = abs(self.s - time2.s)


        # if result_s <= 0:
        #     result_s += 60
        #     result_m -= 1
        
        # if result_m <= 0:
        #     result_m += 60
        #     result_h -= 1
        
        # if result_h <= 0:
        #     result_h += 24
        #     result_day -= 1

        while result_s >= 60:
            result_s -= 60
            result_m += 1
            
        while result_m >= 60:
            result_m -= 60
            result_h += 1

        while result_h >= 24:
            result_h -=24
            result_day += 1

        result = Time(result_day, result_h, result_m, result_s)
        return result
    

    def show(self):
        print(f"{self.day} : {self.h} : {self.m} : {self.s} ")



time1 = Time(1, 2, 80, 40)
time1.show()

time2 = Time(7, 15, 45, 20)
time2.show()

result_sum = time1.sum(time2)
result_sum.show()


result_sub = time1.sub(time2)
result_sub.show()
