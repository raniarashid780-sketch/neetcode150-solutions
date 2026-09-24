class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_items = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        return [pair[0] for pair in sorted_items[:k]]