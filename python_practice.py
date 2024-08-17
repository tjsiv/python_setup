def hello():
  print("Hello User")

hello()

def pack(a, b, c):
  package_list = [ a, b, c]
  return package_list

print(pack("1", "87", "95"))

def eat_lunch(food_list):
  if len(food_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(food_list)):
      if i == 0:
        print(f"First I eat {food_list[0]}")
      else:
        print(f"Next I eat {food_list[i]}")

eat_lunch(["Sandwich", "Soda", "Salad", "buffalo wings", "Chips"])
