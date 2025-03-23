from collections import deque

def min_of_max_brightness(k, n, brightness):
    max_in_subarrays = []
    dq = deque()  

    for i in range(n):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and brightness[dq[-1]] < brightness[i]:
            dq.pop()
        dq.append(i)
        
        if i >= k - 1:
            max_in_subarrays.append(brightness[dq[0]])
    
    return min(max_in_subarrays)

k = int(input("Enter the size of the subarray (k): "))
n = int(input("Enter the size of the brightness array (n): "))
brightness = [int(input(f"Enter brightness level for lantern {i+1}: ")) for i in range(n)]

result = min_of_max_brightness(k, n, brightness)
print(f"The minimum value among all maximum brightness levels is: {result}")
