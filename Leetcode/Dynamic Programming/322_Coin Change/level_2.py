class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        visited = set()
        queue = collections.deque([(0, 0)])

        while queue:
            coin_num, current_amount = queue.popleft()
            for i_coin in coins:
                next_amount = current_amount + i_coin
                if next_amount == amount:
                    return coin_num + 1
                elif next_amount < amount:
                    if next_amount not in visited:
                        visited.add(next_amount)
                        queue.append((coin_num + 1, next_amount))

        return -1
