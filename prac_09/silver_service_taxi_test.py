from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

#Test constructor
print("Test constructor")
s1 = SilverServiceTaxi("Limo 1",100,2.5)
assert s1.price_per_km == 2.5*Taxi.price_per_km
print(s1)

#Test get fare
print("Test get fare")
s2 = SilverServiceTaxi("Limo 2",100,2)
print(s2.get_fare())
s2.drive(18)
print(s2.get_fare())
assert s2.get_fare() == 48.80

#Test __str__
print("Test __str__")
print(s2)