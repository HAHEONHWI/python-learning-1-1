# %% [markdown]
# # 리스트 복습

# %%
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i, end=' ')

print()

for j in range(len(nums)):
    print(nums[j], end=' ')

# %%
nums = [3, 5, 7, 9]
n = 0
for i in nums :
    n += i
print('합:',n)

print()
total = 0
for j in range(len(nums)):
    total += nums[j]
print('합:',total)

# %%
nums = [12, 7, 9, 20, 33, 18]
zak = []
for i in nums:
    if i%2 == 0:
        zak.append(i)
for j in zak:
    print(j, end=' ')

print()

zak = []
for j in range(len(nums)):
    if nums[j]%2 == 0:
        zak.append(nums[j])
for k in zak:
    print(k, end=' ')
    

# %%
nums = [45, 12, 78, 34, 23]
maxi = 0
for i in nums:
    if maxi < i:
        maxi = i
print('최댓값:', maxi)


# %%
scores = [70, 85, 60, 90, 75]
hap =0
for i in range(len(scores)):
    hap += scores[i]
print(f"평균: {hap/len(scores)}")
print("평균 이상 :", end='')
for i in range(len(scores)):
    if scores[i] >= hap/len(scores):
        print(scores[i], end=' ')

# %%
scores = [70, 85, 60, 90, 75]
hap =0
for i in scores:
    hap += i
print(f"평균: {hap/len(scores)}")
print("평균 이상 :", end='')
for i in scores:
    if i >= hap/len(scores):
        print(i, end=' ')

# %%
nums = [10, 20, 30, 40, 50, 60]
for i in range(len(nums)):
    if i%2 == 0:
        print(nums[i], end=" ")
    

# %%
#7번
nums = [5, 7, 3, 8, 10]
for i in range(len(nums)):
    if nums[i] > nums[i-1] :
        print(nums[i], end=' ')

# %%
#8번
nums =[10, 15, 13, 20]
for i in range(len(nums)-1):
    print(nums[i+1] - nums[i] , end=' ')

# %%
#9번
nums = [1, 2, 3, 4]
for i in range(len(nums)-1, -1, -1):
    print(nums[i], end=' ')


