def count(msg):
  lc = {}
  for l in msg:
    lc[l] = lc.get(l, 0) + 1
  print(lc)


msg = input("Please enter your message: ")
count(msg)

