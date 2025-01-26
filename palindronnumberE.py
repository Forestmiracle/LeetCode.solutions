# Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Отрицательные числа не являются палиндромами
        if x < 0:
            return False

        # Превращаем число в строку
        str_x = str(x)

        # Проверяем, является ли строка палиндромом
        return str_x == str_x[::-1]


# Примеры использования функции
solution = Solution()
print(solution.isPalindrome(121))  # Ожидаемый результат: true
print(solution.isPalindrome(-121))  # Ожидаемый результат: false
print(solution.isPalindrome(10))  # Ожидаемый результат: false
