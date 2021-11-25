class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # for kth largest value build a minheap with largest size of K
        # then push all the values in the heap from (0, 0) to (row, col)
        # return the first value of the heap

        # trick: build the prefix Xor matrix to avoid replicating same calculation
        row = len(matrix)
        col = len(matrix[0])
        prefixXor = [[0 for _ in range(col)] for _ in range(row)]
        h = []
        for i in row:
            for j in col:
                # calculate the value first:
                if i == j == 0:
                    prefixXor[0][0] = matrix[0][0]
                elif i == 0:
                    prefixXor[0][j] = prefixXor[0][j - 1] ^ matrix[0][j]
                elif j == 0:
                    prefixXor[i][0] = prefixXor[i - 1][0] ^ matrix[i][0]
                else:
                    prefixXor[i][j] = prefixXor[i - 1][j - 1] ^ prefixXor[i][j -
                                                                             1] ^ prefixXor[i - 1][j] ^ matrix[i][j]
                # push into the heap
                heapq.heappush(h, prefixXor[i][j])
                # check if size of the heap is greater than k, if yes pop smallest value out
                if len(h) > k:
                    heapq.heappop(h)
        return h[0]
