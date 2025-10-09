#calculator

class Calulator():
    def __init__(self,opt_1,opt_2,oprator,result):
        self.opt_1 = opt_1
        self.opt_2 = opt_2
        self.oprator = oprator
        self.result = None

    def oprate(self):      
        if self.oprator in ('/','%') and self.opt_2 == 0:
            print(" ZerodividError")
        else:
            try:
                expression = "self.opt_1" + self.oprator + "self.opt_2"
                self.result = float(eval(expression))
            except Exception:
                return None
        return self.result

    def input_num(self):
        self.opt_1 = float(input("please input the first number : "))
        self.opt_2 = float(input("please input the second number : "))
        self.oprator= input("please input the oprator : ")

    def print_result(self):
        print(self.result)


if __name__ == "__main__":
    calculator = Calulator(None,None,None,None)
    calculator.input_num()
    calculator.oprate()
    calculator.print_result()

