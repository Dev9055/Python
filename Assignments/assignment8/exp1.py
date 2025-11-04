class Cab:
    def __init__(self, driver_name, kms, rate_per_km):
        self.driver_name = driver_name
        self.kms = kms
        self.rate_per_km = rate_per_km

    def rateperkm(self):
        return self.kms * self.rate_per_km

kms = 25
driver_1 = "Raju"
rate_1 = 11
driver_2 = "Rahul"
rate_2 = 13
driver_3 = "Viswas"
rate_3 = 15

firstcab = Cab(driver_1, kms, rate_1)
secondcab = Cab(driver_2, kms, rate_2)
thirdcab = Cab(driver_3, kms, rate_3)

print("First Cab Driver: {}".format(firstcab.driver_name))
print("First Cab Payment: {}".format(firstcab.rateperkm()))

print("Second Cab Driver: {}".format(secondcab.driver_name))
print("Second Cab Payment: {}".format(secondcab.rateperkm()))

print("Third Cab Driver: {}".format(thirdcab.driver_name))
print("Third Cab Payment: {}".format(thirdcab.rateperkm()))

