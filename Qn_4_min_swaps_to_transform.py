def min_swaps_to_transform(N, A, B):
    if sorted(A) != sorted(B):
        return -1 
    
        A = list(A)  
    swaps = 0
    for i in range(N):
    
        if A[i] != B[i]:
            j = i
            while A[j] != B[i]:
                j += 1
            while j > i:
                A[j], A[j - 1] = A[j - 1], A[j]  
                j -= 1
                swaps += 1  
    return swaps

N = int(input("Enter the length of the words: "))
A = input("Enter the original word (A): ")
B = input("Enter the target word (B): ")

result = min_swaps_to_transform(N, A, B)
print(result)
