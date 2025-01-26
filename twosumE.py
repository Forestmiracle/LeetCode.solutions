# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List  # Импортируем List из модуля typing


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Создаем словарь для хранения индексов значений

        for i, num in enumerate(nums):
            # Вычисляем разницу между целевым значением и текущим элементом
            complement = target - num

            # Проверяем, если данное дополнение существует в словаре
            if complement in num_to_index:
                # Если существует, возвращаем текущий индекс и индекс дополнения
                return [num_to_index[complement], i]

            # В противном случае, добавляем текущее значение и его индекс в словарь
            num_to_index[num] = i


# Примеры использования функции
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Ожидаемый результат: [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # Ожидаемый результат: [1, 2]
print(solution.twoSum([3, 3], 6))  # Ожидаемый результат: [0, 1]
