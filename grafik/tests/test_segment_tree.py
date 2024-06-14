
from grafik.segment_tree import SegmentTree


class TestSegmentTree:
    def test_initialize_with_non_empty_array(self):
        data = [9, 1, 11, 3, 7, 5]
        seg_tree = SegmentTree(data)
        assert seg_tree.query(2, 6) == (11, 2)
        assert seg_tree.query(0, 1) == (9, 0)
        assert seg_tree.query(3, 4) == (3, 3)

    def test_initialize_with_empty_array(self):
        data = []
        seg_tree = SegmentTree(data)
        assert seg_tree.tree == []

    def test_query_non_empty_range(self):
        data = [5, 9, 1, 11, 7, 3]
        seg_tree = SegmentTree(data)
        assert seg_tree.query(2, 3) == (1, 2)

    def test_no_side_effects_non_overlapping_ranges_fixed(self):
        data = [11, 9, 1, 5, 3, 7]
        seg_tree = SegmentTree(data)
        assert seg_tree.query(1, 4) == (9, 1)
        assert seg_tree.query(3, 6) == (7, 5)
