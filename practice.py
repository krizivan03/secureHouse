#!/usr/bin/env python3
def insSort(list, n):
    if n <= 1:
        return
    
    insSort(list, n-1)
    last = list[n-1] 
    j = n-2
    while (j>=0 and list[j]>last): 
        list[j+1] = list[j] 
        j = j-1
  
    list[j+1]=last 

#     InsertSort( int[] list, int n){
# if n <= 1{
# return;}

# InsertSort( list, n-1);

# int last = list[n-1];
# int j = n-2;

# while (j>=0 & list[j]> last){
# list[j+1] = list[j];
# j--;
# }
# list[j+1] =last
# }

    

if __name__ == "__main__":
    list =  [5,4,3,2,1]
    insSort(list,5)
    print(list)
