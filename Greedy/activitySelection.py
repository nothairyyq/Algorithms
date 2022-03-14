"""The following implementation assumes that the activities
are already sorted according to their finish time"""
 
"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities
 
#no sorted: O(nlogn)
#sorted: O(n)
def printMaxActivities(s , f ):
    n = len(f)
    print ("The following activities are selected")
 
    # The first activity is always selected
    i = 0
    print (i,end=' ')
 
    # Consider rest of the activities
    for j in range(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j,end=' ')
            i = j

# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)

''' Python program for activity selection problem
 when input activities may not be sorted.'''
def MaxActivities(arr, n):
    selected = []
     
    # Sort jobs according to finish time
    Activity.sort(key = lambda x : x[1])
     
    # The first activity always gets selected
    i = 0
    selected.append(arr[i])
 
    for j in range(1, n):
       
      '''If this activity has start time greater than or
         equal to the finish time of previously selected
         activity, then select it'''
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected
 
# Driver code
Activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
n = len(Activity)
selected = MaxActivities(Activity, n)
print("Following activities are selected :")
print(selected)



 
