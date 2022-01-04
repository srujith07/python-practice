nums={22,34,12,78,24,13}
l=list(nums)
min=l[0]
for i in nums:
    if min>i:
        min=i
print(min)