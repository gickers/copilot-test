def total_on_bus(bus_stops):
    passengers = 0
    for n in range(len(bus_stops)):
        passengers += bus_stops[n][0]
        passengers -= bus_stops[n][1]
    return passengers
