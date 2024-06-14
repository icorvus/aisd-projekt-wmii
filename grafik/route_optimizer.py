class RouteOptimizer:
    def __init__(self, brightness: list[int], max_points: int) -> None:
        self.brightness = brightness
        self.max_points = max_points

    def naive_patrol_route_optimization(self) -> tuple[int, list[int]]:
        if not self.brightness:
            return 0, []

        n = len(self.brightness)

        stops = []
        melody_listened = 0
        current_sequence_length = 1

        for i in range(1, n):
            current_sequence_length += 1

            if self.brightness[i - 1] > self.brightness[i]:
                stops.append(i)
                current_sequence_length = 0
                continue

            if current_sequence_length == self.max_points:
                melody_listened += 1
                stops.append(i)
                current_sequence_length = 0
                continue

        return melody_listened, stops
