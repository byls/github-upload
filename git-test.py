import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt", "a+")

  str = "123"
  f.write(str)
  
  quotes = f.readlines()	
  f.close()
  last = 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[0])

if __name__== "__main__":
  primary()
