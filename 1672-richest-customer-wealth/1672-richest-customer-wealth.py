class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        rich = 0
        for account in accounts:
            new = sum(account)
            rich = max(rich, new)
           
        
        return rich

        