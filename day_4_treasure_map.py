
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

def treasure_map():
  position = input("Where do you want to put the treasure? ")
  print("\n")


  row = position[0]
  col = position[1]

  row = int(row) -1
  col = int(col) -1

  if col <= 2 and col <= 2:
    map[row][col] = "X"
    print(f"{row1}\n{row2}\n{row3}\n\n")
  else:
    print("Your coordinates were out of range. Please try it again.")
    treasure_map()

  

treasure_map()