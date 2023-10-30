nums = list(range(1,11))
nums_par = []
nums_cuadrado = []

for num in nums:
    nums_cuadrado.append(num**2) 
    if num%2 == 0:
        nums_par.append(num)

print(min(nums))
print(max(nums))
print(sum(nums))

print(nums_cuadrado)
print(nums_par)