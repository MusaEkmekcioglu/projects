def make_bricks(small, big, goal):
  a=False
  for i in range(big):
    for j in range(small):
      if (i*5)+j==goal:
        a=True
        
      
  return a
print(make_bricks(5,3,13))