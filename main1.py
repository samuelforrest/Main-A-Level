numbers = [0,1,2,3,4,5]

total = 0

for index in range(len(numbers)):
  numbers.append(int(input("Enter a number!")))
  numbers[index] = int(input("Enter a Num!")) 
  total += numbers[index]

print(f"The total={total}")
print(f"The array")
for i in range(len(numbers) - 1, -1, -1): 
  print(f"{numbers[i]}")  