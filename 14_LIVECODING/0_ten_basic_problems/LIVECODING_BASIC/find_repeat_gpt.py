def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

# Пример использования
nums = [1, 1, 4, 2, 2]
print(find_duplicate(nums))  # Вывод: 2