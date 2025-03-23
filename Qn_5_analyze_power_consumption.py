def analyze_power_consumption(data):
    if any(reading < 10 or reading > 200 for reading in data):
        return "INVALID INPUT"
    
    sensors = [data[i::5] for i in range(5)]
    averages = [sum(sensor) / 4 for sensor in sensors]
    max_average = max(averages)
    
    if max_average < 50:
        return "Energy consumption is optimal."
    else:
        sensor_number = averages.index(max_average) + 1
        return f"Sensor Number : {sensor_number}"

data = list(map(int, input("Enter the 20 power readings (space-separated): ").split()))

if len(data) != 20:
    print("INVALID INPUT")  
else:
    result = analyze_power_consumption(data)
    print(result)
