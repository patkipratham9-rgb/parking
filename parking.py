rates = {
    "two-wheeler": 20,
    "four-wheeler": 50,
    "heavy vehicle": 100,
}

v_type = input("Vehicle type (Two-wheeler / Four-wheeler / Heavy vehicle): ").strip().lower()
hours = float(input("Hours parked: "))

fee = rates[v_type] * hours

print("\nVehicle Type:", v_type.title())
print("Duration (hrs):", hours)
print("Total Fee: Rs.", fee)