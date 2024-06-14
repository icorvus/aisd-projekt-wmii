class SegmentTree:
    def __init__(self, data: list[int]) -> None:
        self.n: int = len(data)
        self.tree: list[tuple[int, int]] = [(0, -1)] * (2 * self.n)
        self.build(data)

    def build(self, data: list[int]) -> None:
        for i in range(self.n):
            self.tree[i + self.n] = (data[i], i)
        for i in range(self.n - 1, 0, -1):
            left_child = self.tree[i * 2]
            right_child = self.tree[i * 2 + 1]
            self.tree[i] = max(left_child, right_child, key=lambda x: x[0])

    def update(self, index: int, value: int) -> None:
        index += self.n
        self.tree[index] = (value, index - self.n)
        while index > 1:
            index //= 2
            left_child = self.tree[2 * index]
            right_child = self.tree[2 * index + 1]
            self.tree[index] = max(left_child, right_child, key=lambda x: x[0])

    def query(self, left: int, right: int) -> tuple[int, int]:
        left += self.n
        right += self.n
        max_val: tuple[int, int] = (-float("inf"), -1)
        while left < right:
            if left % 2:
                max_val = max(max_val, self.tree[left], key=lambda x: x[0])
                left += 1
            if right % 2:
                right -= 1
                max_val = max(max_val, self.tree[right], key=lambda x: x[0])
            left //= 2
            right //= 2
        return max_val
