#Add evan numbers

end_num = int(input("To which number do you want to add? "))
added_num = 0

for i in range(0,end_num+1, 2):
  added_num += i
  print(i)

print(added_num)
