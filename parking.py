rates = {
    "two-wheeler": 20,
    "four-wheeler": 50,
    "heavy vehicle": 100,
}

v_number = input("Vehicle number: ").strip().upper()
v_type = input("Vehicle type (Two-wheeler / Four-wheeler / Heavy vehicle): ").strip().lower()
hours = float(input("Hours parked: "))

fee = rates[v_type] * hours

print("\nVehicle Number:", v_number)
print("Vehicle Type:", v_type.title())
print("Duration (hrs):", hours)
print("Total Fee: Rs.", fee)