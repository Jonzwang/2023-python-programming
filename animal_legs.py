
has_zero_legs = 0
has_two_legs = 0
has_four_legs = 0

animals = [4,0,2,4,2,0,2,4,4,2,0,2,4,'test']

for animal in animals:
  if animal == 0:
    has_zero_legs += 1

  elif animal == 2:
    has_two_legs += 1
  
  elif animal == 4:
    has_four_legs += 1

print(f'Animals with no legs: {has_zero_legs}')
print(f'Animals with two legs: {has_two_legs}')
print(f'Animals with four legs: {has_four_legs}')
print(f'Total number of animals: {len(animals)}')
print(f'Total number of legs: {has_two_legs * 2 + has_four_legs *4}')