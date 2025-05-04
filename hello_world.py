print("Hello Word!")

# define a function for greeting Keitaro
def greet(name):
  print(f"Hello! {name.title()}")
greet("Keitaro")

# make Hiro greeting loop
number = 0
ACTIVATE = True
while ACTIVATE:
  if number <= 5:
    greet("Hiro")
    number += 1
  else:
    ACTIVATE = False
print("Finished greeting Hiro!")
    