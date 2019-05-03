class ConvertType():

    @staticmethod
    def convertStringToInt(convertValue, exceptReturnValue=0):
        try:
            return int(convertValue)
        except ValueError:
            return exceptReturnValue
    
    @staticmethod
    def possibleConvertStringToInt(convertValue):
        try:
            int(convertValue)
            return True
        except (ValueError, TypeError):
            return False
