def main():

  #create an empty list for the menu
  menu = []

  #import the file containing the menu
  with open("input.txt") as file:
    file.readline()

    #read in each line of the menu as a list and append to the menu list 
    for line in file:
      
      line=line.strip("\r")
      menu.append(line.split())

  #for each list item, if the label is not None, add to the sum
  sum=0
  for item in menu:
    item[1]=int(item[1])
    if (item[0]!="None"):
      sum=sum+item[1]

  #print the sum
  print("Total sum of menu items with a label:", sum)
main()