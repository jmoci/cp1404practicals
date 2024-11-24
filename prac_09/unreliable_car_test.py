from prac_09.unreliable_car import UnreliableCar

#Test constructor
print("Test constructor")
u1 = UnreliableCar("Jeep 1",20,50)
print(u1)

#Test drive method
print("Test drive method")
results = []
for i in range(0,10):
    results.append(u1.drive(1))
print(results)
print(u1)