class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        dict_ = {}
        for w in wall:
            bricks_sum = 0
            for brick in w[:-1]:  # the edge is out of range
                bricks_sum += brick
                dict_[bricks_sum] = dict_.get(bricks_sum, 0) + 1
        return len(wall) - max(dict_.values() or [0])
