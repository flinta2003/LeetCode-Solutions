class Solution:
    def minimumCost(self, cost):
        cost = sorted(cost, reverse = True)
        purchased = []
        total_cost = 0

        for rownumber, cookie in enumerate(cost):
            if (rownumber + 1) % 3 == 0:
                continue
            elif (rownumber + 1) % 3 == 2 or (rownumber + 1) % 3 == 1:
                purchased.append(cookie)

        for i in range(len(purchased)):
            total_cost += purchased[i]
        return total_cost