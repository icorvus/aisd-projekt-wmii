from grafik.route_optimizer import RouteOptimizer


class TestRouteOptimizer:
    def test_brightness_strictly_increasing(self):
        optimizer = RouteOptimizer(brightness=[1, 2, 3, 4, 5], max_points=2)
        expected_stops = [1, 3]
        expected_melodies = 2

        melody_listened, stops = optimizer.naive_patrol_route_optimization()

        assert stops == expected_stops
        assert melody_listened == expected_melodies

    def test_brightness_empty(self):
        optimizer = RouteOptimizer(brightness=[], max_points=2)
        expected_stops = []
        expected_melodies = 0

        melody_listened, stops = optimizer.naive_patrol_route_optimization()

        assert stops == expected_stops
        assert melody_listened == expected_melodies

    def test_brightness_strictly_decreasing(self):
        optimizer = RouteOptimizer(brightness=[5, 4, 3, 2, 1], max_points=2)
        expected_stops = [1, 2, 3, 4]
        expected_melodies = 0

        melody_listened, stops = optimizer.naive_patrol_route_optimization()

        assert stops == expected_stops
        assert melody_listened == expected_melodies

    def test_brightness_constant(self):
        optimizer = RouteOptimizer(brightness=[5, 5, 5, 5, 5], max_points=2)
        expected_stops = [1, 3]
        expected_melodies = 2

        melody_listened, stops = optimizer.naive_patrol_route_optimization()

        assert stops == expected_stops
        assert melody_listened == expected_melodies

    def test_brightness_alternating(self):
        optimizer = RouteOptimizer(brightness=[5, 3, 5, 3, 5], max_points=2)
        expected_stops = [1, 3]
        expected_melodies = 0

        melody_listened, stops = optimizer.naive_patrol_route_optimization()

        assert stops == expected_stops
        assert melody_listened == expected_melodies
