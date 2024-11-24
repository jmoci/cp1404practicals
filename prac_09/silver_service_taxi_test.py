from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

#Test constructor
print("Test constructor")
s1 = SilverServiceTaxi("Limo 1",100,2.5)
assert s1.price_per_km == 2.5*Taxi.price_per_km
print(s1)