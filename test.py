def hello():
  print("Hello, user!")
  
def pack(blanket,food,computer):
  return [blanket,food,computer]


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")


hello()
print(pack("blanket","food","computer"))
eat_lunch(["Peach","Hot Dog","Cookie"])
eat_lunch([])