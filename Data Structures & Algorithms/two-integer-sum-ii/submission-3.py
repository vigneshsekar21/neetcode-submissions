class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indxes = []
        back = len(numbers) - 1
        i = 0
        while i < len(numbers):
            if numbers[i] + numbers[back] == target:
                return [i + 1, back + 1]
            elif numbers[i] + numbers[back] < target:
                i += 1
            else:
                back -= 1
        return indxes
