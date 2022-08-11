# Read an integer that denotes the length of the list which is returned as the output of the algorithm
length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
count=3
outlist=[]
for i in range(0,length_of_circular_linked_list,2):
  if i<3:
    outlist.append(circular_linked_list(i))
  elif circular_linked_list[0]!=circular_linked_list[i]:
    count+=1
    outlist.append(circular_linked_list(i))
  elif circular_linked_list[0]==circular_linked_list[i]:
    break
print(count)
print(outlist)
  
