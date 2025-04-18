def countgood(nums,k):
    result = 0
    ans = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if i < j:
                if nums[i] == nums[j]:
                    result += 1
                    if result >= k:
                        ans += 1
                        result = 0    
    return ans
    
print(countgood([3,1,4,3,2,2,4], 2))