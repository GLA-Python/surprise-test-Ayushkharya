def expanding_lst(l):

   for i in range(len(l)-2):

       if(l[i]>=l[i+1]):

           return False

   return True
lst = list(map(int,input().split()))   
out = expanding_lst(lst)
print(out)
