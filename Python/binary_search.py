#이진탐색

def binary_search(left,right,t):
    if left > right :
        return None
    mid = (left+right)//2
    if a[mid] == t :
        return mid
    if a[mid] > t :
        binary_search(left,mid-1,t)
    else:
        binary_search(mid+1,right,t)
        
