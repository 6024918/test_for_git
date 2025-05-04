print("Hello Word!")

# define a function for greeting Keitaro
def greet(name):
  print(f"Hello! {name.title()}")
greet("Keitaro")

# define a fuction for kissing
def kiss(name, time):
  if time >1:
    s = "times"
  else:
    s = "time"
  print(f"{name.title()}, I want to kiss you {time} {s}!")
kiss("hunter", 1)
kiss("taiga", 4)
