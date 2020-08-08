import random
dice_rolls = int(input('How many dice you want?'))
dice_size = int(input('How many sides?'))
dice_sum = 0
for i in range(0,dice_rolls):
  roll = random.randint(1,dice_size)
  dice_sum = dice_sum + roll 
  if roll == 1:
    print(f'You rolled a {roll}! you failed successfully!')
  elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success!!')
  else:
    print(f'You rolled a {roll}!')
print(f'You have rolled a total of {dice_sum}')
# I don't know if I can delete this.
#def main():
#  roll = random.randint(1,6)
#  
#  print(f'You rolled a {roll}')
# 
#if __name__== "__main__":
#  main()
