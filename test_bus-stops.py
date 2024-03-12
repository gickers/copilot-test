import unittest

from bus_stops import total_on_bus

class TestBusStops(unittest.TestCase):
    def test_total_on_bus(self):
        # Test case 1: Empty bus stops
        bus_stops = []
        self.assertEqual(total_on_bus(bus_stops), 0)

        # Test case 2: Single bus stop with no passengers
        bus_stops = [[0, 0]]
        self.assertEqual(total_on_bus(bus_stops), 0)

        # Test case 3: Single bus stop with passengers getting on and off
        bus_stops = [[5, 3]]
        self.assertEqual(total_on_bus(bus_stops), 2)

        # Test case 4: Multiple bus stops with passengers getting on and off
        bus_stops = [[3, 0], [2, 1], [4, 2]]
        self.assertEqual(total_on_bus(bus_stops), 6)

        # Test case 5: Multiple bus stops with no passengers
        bus_stops = [[0, 0], [0, 0], [0, 0]]
        self.assertEqual(total_on_bus(bus_stops), 0)

if __name__ == '__main__':
    unittest.main()