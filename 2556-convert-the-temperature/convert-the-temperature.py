class Solution(object):
    def convertTemperature(self, celsius):
        tem=[]
        tem.append(celsius + 273.15)
        tem.append(celsius * 1.80 + 32.00)
        return tem
        