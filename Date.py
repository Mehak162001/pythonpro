
class Date:
    __dd = None
    __mm = None
    __yy = None

    def __init__(self,dd,mm,yy):
        self.__dd = dd
        self.__mm = mm
        self.__yy = yy

    def show_date(self):
        print("date ",self.__dd,"month",self.__mm,"year "+self.__yy__yy)
