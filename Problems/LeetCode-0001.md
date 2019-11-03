# LeetCode - 0001

[원본 링크](https://leetcode.com/problems/two-sum/)

## 문제

Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the *same* element twice.

Example.

``` c
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## 해결

배열이 주어지고 타깃이 정해진다.

이 타깃 값은 배열의 원소 중 2개를 Sum 했을때 나오는 값이다.

이 때 target 값이 나오려면 어떤 원소로 얻을 수 있는가에 대한 문제이다.

dict로 풀면 아마 더 간편하게 풀수 있을 것이지만 나는 리스트를 하나 더 만들어서 풀었다.

#### 솔루션 1번)

``` python
# solution1
# Runtime: 6576ms, Mem: 14.7MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = nums[:]
        count = 0
        for num1_index in range(len(nums)):
            lst.remove(nums[num1_index])
            count = count + 1
            for num2_index in range(len(lst)):
                if nums[num1_index]+nums[num2_index+count] == target:
                    return [num1_index,num2_index+count]
```

3: lst에 리스트를 복사

4: count 초기화

5: 1차 반복 - 입력 받은 배열 리스트 만큼 반복

6: lst에서 반복될 수는 제외하기 위해 remove()

7: count++

8: 2차 반복 - lst 만큼 반복

9: (1차 반복의 인덱스의 값 + 2차 반복의 인덱스+count의 값)과 target 값이 같은지 비교

10: 같은면 target과 비교한 값의 인덱스가 담긴 리스트 반환

count는 리스트를 비교하면서 인덱스 값이 망가지기 때문에 추가한 것, num1_index로도 처리가 가능하여 적용해봤음

#### 솔루션 2번)

``` python
# solution2
# Runtime: 7704ms, Mem: 14.8MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = nums[:]
        for num1_index in range(len(nums)):
            lst.remove(nums[num1_index])
            for num2_index in range(len(lst)):
                if nums[num1_index]+nums[num2_index+num1_index+1] == target:
                    return [num1_index,num2_index+num1_index+1]
```

pass가 되었으나, 런타임이 1000ms 증가하고 메모리가 0.1MB 증가했음. 이유는 알수가 없다.

#### 솔루션 3번)

반복할때 `range(len(nums))`로 인해 런타임이 더 먹는 것 같아 `enumerate()`로 수정해보았다.

``` python
# solution3
# Runtime: 5124ms, Mem: 14.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = nums[:]
        for num1_index, dat1 in enumerate(nums):
            lst.remove(dat1)
            for num2_index, dat2 in enumerate(lst):
                if dat1+dat2 == target:
                    return [num1_index,num2_index+num1_index+1]
```

런타임은 감소했고 메모리 0.2MB 하락

#### 솔루션 4번)

현재 비교하고 있는 값을 target에서 뺀 값이 해당 리스트에 있는지 검사하면 어떨까 라는 생각이 들었다.

그럼 시간복잡도가 지금 n^2인걸 줄일수있을것 같았다.

for 문을 제거하고 `if(target - dat1) in lst:`를 통해 반복과 값 비교를 통합했다.

``` python
# solution 4
# Runtime: 580ms, Mem: 14.9MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = nums[:]
        for num1_index, dat1 in enumerate(nums):
            lst.remove(dat1)
            if (target - dat1) in lst:
                return [num1_index,lst.index(target-dat1)+num1_index+1]
```

pass, 런타임 580ms, 메모리는 0.3MB 증가한 14.9MB

어찌됬든 런타임이 이중 반복을 없애니깐 10배 가까이 감소했다.

#### 솔루션 5번)

난 더 줄이고 싶었다. 리스트를 없앨수 있겠다는 생각이 들었고 적용했다.

이젠 첫 값을 저장할 num이라는 변수만 하나 있으면 된다.

대체 `range(len())` vs `enumerate()` 중 어느것이 더 빠르고 좋은지 궁금해 관련 [링크](https://stackoverflow.com/questions/11990105/rangelenlist-or-enumeratelist)에서 찾아 봤고 결론은 `range(len())` 승!

``` python
# solution 5
# Runtime: 584ms, Mem: 14.6MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[0]
            nums.remove(num)
            if (target - num) in nums:
                return [i,nums.index(target-num)+i+1]
```

더는 못 줄이겠다. 내 한계인듯하다..



## 결론

작년에 미국 인턴십 뽑을 때 시험 문제를 풀면서 Leetcode를 알게되었는데, 알게된 이후로 20 문제 가량을 풀었지만 지금에서야 1번 문제를 풀었다. 모든걸 내려놓고 조금씩 풀어나가면 도움이 되겠지..



# LeetCode - 0053

나를 굉장히 혼란스럽게하는 문제이다.

일단 n^2 형태는 풀었다.
문제는 시간이 1000ms가 넘어가서 시간초과가 뜬다.

1520ms
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tmp = nums
        res = float('-inf')
        if len(nums) is 1:
            return nums[0]
        
        for i in range(len(nums)):
            for k in range(len(tmp)):
                res=max(res, sum(tmp[:k+1]))
                #print(res)
                
            tmp.pop(0)
            
        return res

1250ms
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        num = len(nums)
        tmp=nums
        lst=[]
        if len(nums) is 1:
            return nums[0]
        count = 0
        k=0
        
        while(count!=num):
            #print(count==num-1)
            k=k+1
            lst.append(sum(tmp[:k]))
            if k == len(tmp):
                k = 0
                tmp.pop(0)
                count=count+1
            #print(lst)
        return max(lst)

이 문제를 통과 시키려면 Time Limite Exceeded를 발생시키게 하면 안된다.

해결하기 위해 5시간을 사용했지만, 나의 머리로는 해결할 수 없었다.

영상을 찾아도 보았지만 이해가 안되다가 
https://www.youtube.com/watch?v=ohHWQf1HDfU
위 영상을 참고했고 디버깅을 해보면 뭔가 해결할 수 있을것 같았다.

예를 들어 [3,-2,5,-1]이 있다 가정하면

index 0
3
3-2
3-2+5
3-2+5-1

index 1
-2
-2+5
-2+5-1

index 2
5
5-1

index 3
-1

여기서 이전 합을 사용해 중복을 줄일수 있는 것이 보인다.
정리를 해보면 sum에 이전 sum을 가지고 있으면 된다.

일단 두번째 루프를 for i in range(len(nums)): 로 바꾸고
최초에 sum=0 루프 안에서 sum=sum+k

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tmp = nums
        res = float('-inf')
        s=0
        if len(nums) is 1:
            return nums[0]
        
        for i in range(len(nums)):
            s=0
            for k in tmp:
                s = s + k
                res=max(res, s)
                #print(res)
                
            tmp.pop(0)
            
        return res

그래도 Time limit exceeded 이다.
sum()이 없어졌다.

8:10

이걸 nlogn으로 줄이기 위해 반 잘라서 해본다.
res_r=res_l=float('-inf')
m = len(nums)/2;
s_left = maxSubArray(tmp)
s_right = maxSubArray(tmp)
for i in range(m):
    s = s+tmp[i]
    s_left = max(s_left,s)
s=0
for i in range(len(nums)-m)
    s = s+tmp[i+m]
    s_right = max(s_right,s)
res = max(s_left,s_right)
return max(res,s_left+s_right)

구상했으나 망했다.
아래는 구상한 코드

class Solution:
    def test():
        print('test')
        
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums
        res_r = float('-inf')
        res_l = float('-inf')
        res=0
        s=0
        if len(nums) is 1:
            return nums[0]
        
        m=len(nums)/2
        s_left = self.maxSubArray(tmp)
        s_right = self.maxSubArray(tmp)
        
        for i in range(m):
            s = s+tmp[i]
            res_l = max(res_l,s)
            
            s=0
            
        for i in range(len(nums)-m):
            s = s+tmp[i+m]
            res_r = max(res_r,s)
            
        res = max(s_left,s_right)
        return max(res,res_l+res_l)

모르겠다. 레알 답이 없다.
이따 영상 보고 이해하는 수밖에 없겠다.

혹시나 해서 while 했던거에 다시 적용했더니
역시나 Time limit exceeded..
잔다.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

            num = len(nums)
            tmp=nums
            if len(nums) is 1:
                return nums[0]
            count = 0
            k=0
            s=0
            res=-99999
            print(tmp)
            while(count!=num):
                s = s + tmp[k]
                res=max(res,s)
                k=k+1
                
                if k == len(tmp):
                    k = 0
                    tmp.pop(0)
                    count=count+1
                    s=0
                
                #print(lst)
            return res