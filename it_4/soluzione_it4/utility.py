class Utility:

    def __init__(self,input):
        self.__input= input

    @staticmethod
    def is_integer(num):
        try:
            if (num - int(num))==0:
                return True
            return False
        except ValueError:
                return False
        
