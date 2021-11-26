# if we want to achieve the minimum cost, there should be at leat one workder who is paied as expected, we call this worker as key worker
# then for ther worker, we can calculate the wage to pay as keyWorkerWage / keyWorkderQuality * Quality
# since the ratio = keyWorkerWage / keyWorkderQuality is fxied, to find the minimum that is to find the min of sum of qualities, thus to find k smallest qualities.
# the paid ratio should satistfy at least k workers
import heapq


class Solution:
    def minCostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # calculate the pay ratio for each worker and sort the pay ratio, smallest goest to first
        info = [(w / q, q, w) for q, w in zip(quality, wage)]
        info = sorted(info)
        # iterate starting from index k - 1 so that the selected pay ratio can satisfy at least k workers
        h = []  # use a maxHeap to save the k smallest qualities
        totalQuality = 0
        ans = float('inf')
        for i in range(k - 1, len(info)):
            payRatio = info[i][0]
            if i == k - 1:
                for j in range(i + 1):
                    heapq.heappush(h, -info[j][1])
                totalQuality = -sum(h)
            else:
                heapq.heappush(h, -info[i][1])
                totalQuality = totalQuality + info[i][1] + heapq.heappop(h)

            ans = min(ans, totalQuality * payRatio)
        return ans
