
## 題目參照
 - [top interview](https://leetcode.com/problem-list/top-interview-questions/)
 - [top 100](https://leetcode.com/problem-list/top-100-liked-questions/) 
 - [Grind 75 (No hard, by topic)](https://www.techinterviewhandbook.org/grind75?difficulty=Easy&difficulty=Medium&order=topics)

## Python 常見操作複雜度
參考 [Python Complexity](https://wiki.python.org/moin/TimeComplexity)
 - `list.sort()`: Tim sort, $O(n\cdot logn)$
 - `set(list)`: $O(n)$
 - `x in set/dict`: $O(1)$
 - `x in list`: $O(n)$
 - set/dict operation: $O(1)$
 - [set difference](https://stackoverflow.com/questions/48044353/what-is-the-run-time-of-the-set-difference-function-in-python): $O(n)$

## Python 相關重要連結 & 筆記
- [collections.deque (used for stack & queue)](https://docs.python.org/zh-tw/3/library/collections.html#deque-objects)
    ```python=
    from collections import deque
    D = deque()
    D.append(1)
    D.appendleft(2)
    _ = D.pop()
    _ = D.popleft()
    print(D[0])
    print(D[-1])
    ```
- [Performance comparison between list & deque](https://stackoverflow.com/questions/23487307/python-deque-vs-list-performance-comparison)
- [Initialize a 2d matrix](https://www.geeksforgeeks.org/initialize-matrix-in-python/)
    ```python=
    # correct
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    mat = [[0] * cols for _ in range(rows)]
    # Wrong
    mat = [[0] * cols] * rows 
    mat = [[0 for _ in range(cols)]] * rows
    ```
- [heapq (Default: min heap)](https://docs.python.org/zh-tw/3.10/library/heapq.html)
    ```python=
    import heapq
    H = [1,3,5,7,9]
    heapq.heapify(H)
    heapq.heappush(H,2)
    _ = heapq.heappop(H)
    _ = heapq.heappushpop(H,2)    
    ```
- [List](https://docs.python.org/zh-tw/3/tutorial/datastructures.html) and [More about list](https://steam.oxxostudio.tw/category/python/basic/list.html)
    ```python=
    >>> a = [1,2,3,4,5,6,7]
    >>> a[:3]
    [1, 2, 3]
    >>> a[3:]
    [4, 5, 6, 7]
    >>> a[:-3]
    [1, 2, 3, 4]
    >>> a[-3:]
    [5, 6, 7]
    >>> a[-3]
    5
    ```
- [Bit Manipulation](https://weikaiwei.com/python/python-bitwise/)
    ```python=
    >>> bin(13)
    '0b1101'
    >>> bin(200)
    '0b11001000'
    >>> int(bin(200),2)
    200
    >>> int(bin(200)[2:],2)
    200
    ```
- [bisect](https://docs.python.org/zh-tw/3/library/bisect.html)
    ```python=
    >>> import bisect
    >>> a = [1,2,3,4,5,6,7]
    >>> bisect.bisect_left(a, 4) # [1,2,3,*,4...]
    3
    >>> bisect.bisect_right(a, 4) # [1,2,3,4,*...]
    4
    >>> bisect.bisect(a, 4) # [1,2,3,4,*...]
    4    
    ```
    ```python=
    # binary search example
    def BinarySearch(a, x):
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        else:
            return -1
    ```
- [collections.defaultdict](https://ithelp.ithome.com.tw/articles/10193094)
    ```python=
    >>> s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    >>> d = defaultdict(set)
    >>> for k, v in s:
    ...    d[k].add(v)
    ...
    >>> sorted(d.items())
    [('blue', {2, 4}), ('red', {1, 3})]
    ```
- [Nonlocal vs global](https://stackoverflow.com/questions/33211272/what-is-the-difference-between-non-local-variable-and-global-variable)
- [LRU Cache](https://medium.com/@jepersyne/python-functools-lru-cache-d5cb632df710)

## 相關重要演算法
- [Fucking Algorithms Github](https://github.com/labuladong/fucking-algorithm)
- [Dijkstra](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2)
- [DFS Big-O](https://www.quora.com/Why-is-the-complexity-of-DFS-O-V+E) and [BFS Big-O](https://www.quora.com/Why-is-the-time-complexity-of-BFS-O-V+E)
- [Difference between DFS & BFS](https://www.tutorialspoint.com/difference-between-bfs-and-dfs)

## Array
### 1. Two Sum (E)
 - 使用 Dictionary 以空間換取速度 (Hash)
 - 納入 enumerate 的使用，以及省去沒必要的 assignment
 - 邊 Traverse 邊計算，可以 O(n) 就不用 O(n^2)

### 26. Remove Duplicates from Sorted Array (E)
 - 使用 two pointer 的方式邊比較邊紀錄目前位置
 - 要注意原本就是 sorted， result 也要維持 sorted，同時我們不關心 list 後面的長相
 - 一樣要精簡，不需要的東西就不要寫，不需要的變數就不用宣告
 - 與其寫 if A then continue else do something ，不如寫 if not A then do something

### 27. Remove Element (E)
- 2 pointers，兩邊跑的條件剛好相反，boundary condition 有夠難想......要注意......
- 阿幹根本不用 2 pointers，把符合條件的往前蓋掉就好了，再那邊想邊界想半天==

### 67. Plus One (E)
- 就直接幹就好，不過用 for 應該比 while 好，不用加就直接 return

### 169. Majority Element (E)
 - Linear traverse + Hash table
 - But how to achieve O(1) of space complexity? [Reference](https://leetcode.com/problems/majority-element/solutions/51613/o-n-time-o-1-space-fastest-solution/?orderBy=most_votes) and [摩爾投票法](https://www.zhihu.com/question/49973163/answer/235921864)

### 217. Contains Duplicate (E)
 - Linear traverse + Hash table
 - Can be solved in one line (but slower)

### 228. Summary Ranges (E)
- No skills, just for if-else and list of strings

### 744. Find Smallest Letter Greater Than Target (E)
- Linear is okay, or binary search
- Compare alphabet order directly or with ord() (char - > int) / chr() (int -> char)


### 1491. Average Salary Excluding the Minimum and Maximum Salary (E)
 - 可以 sorting 或 linear traverse，丟掉最大最小算平均就好

### 1502. Can Make Arithmetic Progression From Sequence (E)
 - 等差級數，先 sorting 後判斷公差即可

### 1822. Sign of the Product of an Array (E)
 - 就計算幾個負數就好，EZ，若有 0 return 0

### 2148. Count Elements With Strictly Smaller and Greater Elements (E)
- 沒啥水準，O(N) 去掉最大最小 or O(N log N) 排序再去掉都可

### 15. 3Sum (M)
 - 使用一個 target ，再對剩下的做 2 sum
 - 先對原始 list sorting，就可以避免 target 重複的狀況
 - [0,0,0,0] 的狀況 - 將符合的結果從 pair 中刪除
 - [-4,2,2,2,2] 的狀況 - 用一個 paired 來記錄配對過的
 - 為何所有狀況分開討論會比較快?複雜度看起來都是 O(n^2)?是因為處理數量變少很多了嗎?
 - 最快的解法：0,0,0 ; x,-x,0 ; x1,x2,-x1-x2分開討論
    用dict來幫助判斷有沒有這個pair
    
### 56. Merge Intervals (M)
- 以為很簡單，結果被搞，資料沒有排序......
- 偷吃步用 sort 後，再用 57 的方法就可以了
- 看到最多人推的解法也用 sort，雖然感覺不太好就是了

### 57. Insert Interval (M)
 - 蠻好玩的，把問題簡化成兩兩 pair 的判斷，就好做了
 - 用 stack，每次都把下個東西跟最上面的範圍 merge
 - Merge 就用 `[min(aS,bS),max(aE,bE)]` 就好

### 75. Sort Colors (M)
 - 參考 [Dutch flag Problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)，蠻酷的想法做 3-way partition
```python=
procedure three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
            # Note: There is no j += 1 here
            # Since we still need to check A[j] after swap
        else:
            j ← j + 1
```

### 134. Gas Station (M)
- 一開始 TLE，將近 O(n^2) 太慢，還有沒考慮到每個位置都相差 0 的可能性
- 後來亂想亂試突然就過了，嚇歪：先算出每個位置 diff，再用 2 pointers，一個跑一個記可能出發點，當可能出發點到跑中間的總和為負時就把可能出發點變成跑到那點 (前面總和負所以整坨往後丟，在這之中也不可能有可能出發點，找完一輪後還沒有就沒有)，但這樣有點慢就是了
```python=
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        new = []
        for i in range(n):
            diff = gas[i] - cost[i]
            new.append(diff)
        new += new

        start = 0
        nowpos = 0
        sumnow = 0
        while nowpos - start <= n and start < n:
            sumnow += new[nowpos]
            nowpos += 1
            if sumnow < 0:
                sumnow = 0
                start = nowpos
    
        return -1 if start >= n else start
```
- 更快解：如果總和 gas > cost，則必存在一出發點!!!(But why?)
- 結果好像是電腦問題，兩個方法我交出去都差不多快==，[但這的確是個不錯的解法啦](https://leetcode.com/problems/gas-station/solutions/1706142/java-c-python-an-explanation-that-ever-exists-till-now/?orderBy=most_votes)
    
### 347. Top K Frequent Elements (M)
- 原本想說是不是要用甚麼神奇的技巧，結果就 hash 記次數 + sort lambda 然後回傳就好
- 可以用 [Bucket Sort](https://en.wikipedia.org/wiki/Bucket_sort)，一樣 hash 再將結果存到不同 bucket，可以省略 bucket 內 sort 的步驟因為答案保證 unique，這樣複雜度只有 O(N)
```python=
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
```
### 1146. Snapshot Array (M)
- 很容易 TLE 或 MLE，似乎一定要照他的方法
- 紀錄修改的 history + version，再用 binary search 尋找最接近的，要注意結束條件，因為同版本有可能改好幾次，要找到最後的


### 4. Median of Two Sorted Arrays (H)
- 先用 merge 的方式合在一起，同時 (m+n)//2 為中位數點，回傳中位數點就好
- 複雜度是 O(m+n)，不過題目要求 O(log(m+n))
- [蠻複雜的遞迴解法](https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/2511/intuitive-python-o-log-m-n-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms/?orderBy=most_votes)，有空再看

### 41. First Missing Positive (H)
- 兩種解法，但好像沒到他的空間要求（O(N) of time & O(1) of space)
- 用 Set 然後從頭找 OR 創一個一樣大的 array 記 True False
- O (1) 解法：把數字換到屬於他的位置，並持續做直到換過來的不用再考慮，最後確認每個位置的值跟位置一樣，找到第一個不同就好 

### 135. Candy (H)
- 左右各一次，很簡單但應該不好想@@
![](https://hackmd.io/_uploads/r1m9igXk6.png)


### 1187. Make Array Strictly Increasing (H)
- 超難幹，看 [Editorial](https://leetcode.com/problems/make-array-strictly-increasing/editorial/) 才解出來，不過省略 binary search 的部分改用線性往後找，沒差多少時間
- 用 DP + Recursion + Memorization(Hash) 從前往後找，將每種可能狀況下可採取手段（換 or 不換）之所需步數算出並找 min 再更新在 table，若無法換就用 inf

### 2448. Minimum Cost to Make Array Equal (H)
- 用數學角度來想會簡單不少，原本有想到 O(N^2) 的方法，但有人說不會過，看了提示有夠爛，就叫我們一個一個試（搭配 prefix & suffix），後來看到有位老哥用 c1*|a1-x| + c2*|a2-x| + ... 的視角來解，真滴讚，就照他的方式解了，[My Solution](https://leetcode.com/problems/minimum-cost-to-make-array-equal/solutions/3664355/100-time-python3-solution-a-easy-math-perspective/)

### 2551. Put Marbles in Bags (H)
- 原本看似很難，用數學想輕輕鬆鬆解出，最頭最尾不算，其他每個區間的頭尾會計算，所以先做 pair sum，又因為總共的區間數固定，所以 sorting 後取 k 個最大 - k 個最小即可!

## Linked List
### 21. Merge Two Sorted Lists (E)
 - 還是需要熟悉 Linked List 的操作
 - 用捨棄第一個 Node 的方式會好做很多

### 141. Linked List Cycle (E)
 - 我的作法：字典紀錄出現的地址，重複就有 cycle
 - 另解（較快）：快慢指標，看是否有相遇，注意條件為 `while fast and fast.next`

### 206. Reverse Linked List (E)
 - 其實用這個就好了~之前學過又忘記了，我就爛QQ
    ![](https://i.imgur.com/zhfs6Ex.png =70%x)
 - recursion 的版本真酷...但概念跟上面那張圖類似
```python=
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def recursion(prev,curr):
        if not curr:
            return prev
        curr.next, temp = prev, curr.next
        return recursion(curr,temp)
    return recursion(None, head)
```

### 876. Middle of the Linked List (E)
 - 快慢指針輕鬆解決! 但要記得從 -1 位置開始，還有不可以直接 fast.next.next 會錯

### 2. Add two numbers (M)
 - 用一行解決 if else 的宣告
 - 熟悉 Linked List 的操作
 - 精簡 code

### 19. Remove Nth Node From End of List (M)
- 不確定我 2 pointers 有沒有用對，先跑完全部一遍，在跑 length - n 個到要刪掉的那邊
- Linked List 的都在 head 前面加個 prev 會比較好處理
- [2 pointers 正確作法](https://www.codecademy.com/article/the-two-pointer-technique-in-a-linked-list-swift)：
```python=
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head.next:
        return None

    length = 0
    prev = ListNode(-1, head)
    ptr = prev
    tail = head

    while tail:
        if length > n - 1:
            ptr = ptr.next
        tail = tail.next
        length += 1

    ptr.next = ptr.next.next

    return prev.next
```

### 24. Swap Nodes in Pairs (M)
- 用跟類似 reverse 的方式，總之一直改 ptr 就好了，也可以用 recursion
- 不知為啥我很慢，但寫法跟快的一樣

### 445. Add Two Numbers II (M)
- adder + stack 注意邊界條件 & 精簡即可

### 1721. Swapping Nodes in a Linked List (M)
- 用雙重指針，先找到 left，再用 head 跟 left 的相對位置去 traverse，當 left 到底時 head 就是 right！但不知道為何這樣比先找結尾再找 right 還慢，詭異


### 2130. Maximum Twin Sum of a Linked List (M)
- 用 stack + two pointers，透過快慢指針先找到中間
- 接著將前半存入 stack，後半一對一相加，紀錄最大值

### 25. Reverse Nodes in k-Group (H)
- 把 reverse linked list 的函數拿來借用，但要稍微修改成看到 end 停住，並且一開始的 prev 要設成 end（區域 reverse，區域前後要接好）
- 最後再同步移動所有指針 k 步，當移不了時就結束，特別小心 fast = None 也說不定還可以再 reverse 一次，所以 except 直接把 fast = -1


## Matrix
### 1351. Count Negative Numbers in a Sorted Matrix (E)
- O(n + m) algorithm is a really elegant one. Just switch to another row whenever you meet a positive number in a column position, and add the count of negative numbers.

### 36. Valid Sudoku (M)
- 列出所有需檢查 index 並丟入另一個函數檢查
- 有點太慢，感覺是出在 append 的時候？
- 不需要先存全部的 index 下來，邊跑邊檢查，快了一點點
- 看有沒有更好的做法：有人創一堆 set 記錄下出現過的，用 in 檢查，快了不少？

### 54. Spiral Matrix (M)
- 用蠻 naive 的方式，紀錄 boundary 與朝向，並持續更新
- 但竟然 work 然後也跑得不慢，那應該代表還行？

### 934. Shortest Bridge (M)
- 這題好讚，dfs + bfs 兩者結合，概念要清楚
- [我的解法](https://leetcode.com/problems/shortest-bridge/submissions/954241518/)
> 參考的 Discussion
Intuition
Use DFS for traversal of 1st island.(same can be done using BFS)
Use BFS for finding smallest path to the 2nd island.
Approach
Traverse the 1st island found using dfs.
While doing dfs add all the water boundaries(i,j)grid[i][j]=0 of 1st island in the queue.
Using multi-source BFS, find the smallest path to the 2nd island.

### 1091. Shortest Path in Binary Matrix (M)
- 就是 BFS，寫的時候小心點就好，然後提早紀錄踩過的點可以減少複雜度，直接把踩過的點變成 1 可以不用另開 set 紀錄

### 2352. Equal Row and Column Pairs (M)
- 先把 row 記在 hash table，要記次數，然後再從 column 去對應加總就好，transpose 需要 O(N^2)

### 864. Shortest Path to Get All Keys (H)
- 變種 BFS，因為有 key 跟 lock，所以會比較麻煩，把每種拿到 key 的狀態都當作獨立的 state，不同 state 可以走過同一格（傳統 BFS 不行），state 的部分用 bit manipulation 來做（101010 -> has key A,C,E） 
- 就只差沒想到要讓不同 state 可以走到同一格，不過這個也似乎是關鍵？
- 後來照他的順序調整 if else 就過了，真搞不懂到底卡在哪裡@@ 總之就是我看 state 之後自己寫的方法也對，只是需要調整一些順序才能通過，不然會 TLE

### 1970. Last Day Where You Can Still Cross (H)
- BFS / DFS + Binary Search（感覺 Binary Search 有點硬要，但似乎牽扯到 last possible 都會要用這個，也確實比較快啦）
- 可以用水來想，如果存在一條橫的水路貫穿，那就不能直的走到底，但其實直接對陸地做 BFS / DFS 就好，根本也不用那麼麻煩
- 就只差 binary search 就對了，雖然前面水的走法搞了很久

## Stack (DFS)
### 20. Valid Parentheses (E)
- Stack 基本題，把是左邊的存進去，每當有右邊時 pop 檢查
- 可以用字典存，左為 key 右為 value

### 232. Implement Queue using Stacks (E)
- 基本題，用兩個 stack 模擬 queue
- 一個尾朝上一個頭朝上，要插跟要取時分別用兩種，並且兩個 stack 會丟來丟去
- 僅有一個 stack 包含所有資料，朝向會不同

### 844. Backspace String Compare (E)
- 可以直接兩個 stack 解決，記得要處理沒東西 pop 的狀況
- 用一個 stack 比較難搞，但一樣可以，要處理的狀況比較多

### 150. Evaluate Reverse Polish Notation (M)
- [參考這個](https://zh.wikipedia.org/wiki/%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E7%A4%BA%E6%B3%95)，把答案推回去 stack 就好!!!(畢竟他本來就是這樣定義的)

### 155. Min Stack (M)
- 用兩個 stack，如下圖，雖然簡單但要記得此概念：
![](https://hackmd.io/_uploads/BkWwRi243.png)

### 32. Longest Valid Parentheses (H)
- 題目看起來很簡單，但實際上還真的蠻難的
> So in this case I use stack and an array, and then change this problem as finding longest continuous 1 in a 01 array. Let me tell how to do it.
First, stack push position of each '(', then when we meet ')' I pop stack to find its match'('， place both ')' and '(' as 1 in array
For example, (()()，array should look like[0,1,1,1,1]
Then it is super easy, to find out longest substring that all items are 1 !!!

## Queue (BFS)
### 225. Implement Stacks using Queue (E)
- 基本題，用兩個 queue 模擬 stack
- 兩個 queue 丟來丟去，但就沒分誰朝前誰朝後了
- 要插時正常插，要取時全部出來到另一個 queue 並取出最後一個
- 僅有一個 queue 包含所有資料，朝向相同

### 387. First Unique Character in a String (E)
- 用兩個 set 紀錄是否為重複出現的 character，再用 queue 把是的 pop 掉直到遇到不是的即可


## Heap
- [Python heapq 介紹](https://ithelp.ithome.com.tw/articles/10247299)

### 703. Kth Largest Element in a Stream (E)
- 原本用 list.sort 亂搞，也行但超慢，後來用 min heap 來搞就快多了
- python 的 heapq 是 min heap，加入負號可以變 max heap
> We can build a MinHeap that contains only k largest elements.
On add:
1.compare a new element x with min to decide if we should pop min and insert x
2.take into account a case when heap_size is less than k
Construction is simply calling the add function N times.

### 1046. Last Stone Weight (E)
- Heap 基本題，用 max heap 每次取兩個，再把剩下的加回去，最後看剩下多少就好

### 1337. The K Weakest Rows in a Matrix (E)
- Traverse 過每個 row(O(M))，計算有多少士兵(O(N), O(log(N) if binary search))，並用 heap 紀錄找出 k smallest 再 sort 即可，感覺介於 E ~ M 之間

### 215. Kth Largest Element in an Array (M)
- 這題跟 703 難度相反了吧 @@，用一樣的方法解就好，還比較簡單
- 不過 heapq.nlargest() 好像是 O(N log(N))?

### 373. Find K Pairs with Smallest Sums (M)
- 以為很簡單，結果被騙了，直接繞完 O(MN) 的根本不可能過，要用比較有效率的方式繞，因為原始 list 有 sorted，所以 nums1[i] + nums2[j] < nums1[i] + nums2[j+1] for all i,j，因此可以先把 j 設為 0 的結果找出來，min heap 每次 pop 最小並加入該次 pop 的下一個 (i,j - > i,j+1)，就可以確保每次都拿到最小直到 k 個，也不用擔心 i+1, j 會大於 i,j+1 而被先拿出來因為是 min heap
- 或是從 (0,0) 開始，每次加入 (1,0) 跟 (0,1)，這樣比較好想也比較快，有個 hint 有說但沒想出來，不過這樣要小心不要踩到重複的地方


### 2462. Total Cost to Hire K Workers (M)
- 該怎搞基本上都寫出來了，就照他的用 heap 來存，每回找出一個 min 並搭配 two pointers 更新左右 heap，注意邊界條件就好


### 2542. Maximum Subsequence Score (M) & 1383 Maximum Performance of a Team (H)
- 這兩題根本一樣，不知道幹嘛分兩題，還不同難度，[參考這個](https://leetcode.com/problems/maximum-subsequence-score/solutions/3557153/python-java-c-simple-solution-easy-to-understand/)
- 先依 efficient 排序，從最大的降序排，**然後只能找 k 個 speed**所以用 min heap，每次都把新的 speed 加到 heap 中，同時乘以目前的 efficient，再記住最大的結果就好，兩題差異小於 k 個時可不可以計算

## Tree
### 589. N-ary Tree Preorder Traversal (E)
- 就跟 binary tree preorder traversal 一樣，只是換成 for 迴圈繞 children

### 1376. Time Needed to Inform All Employees (M)
- 就是 DFS/BFS，甚至也不用建成樹，但要注意很容易 TLE，不要亂用複雜度大的 function (seta - setb, sum(list)...)
- 用 dp + recursion 的概念也可以解，更快更好寫
```python=
def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    def find(idx):
        if manager[idx] != -1:
            informTime[idx] += find(manager[idx])
            manager[idx] = -1
        return informTime[idx]
    return max([find(i) for i in range(n)])
```

## String
### 14. Longest Common Prefix (E)
- 根本不用建 Trie，直接 linear 字串處理還比較省空間，忘記 break 害我賠了一個 WA
- 還有其他更快方法，但沒差多少就是了

### 125. Valid Palindrome (E)
 - 第一次看到 `x == x[::-1] ` 這個神奇的東西，可以快速倒轉字串（參考 List Slicing）
 - 可以試著用 `string.join()` ，但要注意它的用法

### 205. Isomorphic Strings (E)
 - 用 hashmap 紀錄出現過的對應，並檢查是否重複即可，要小心 key、value 都不能有不同的對應

### 242. Valid Anagram (E)
 - 用 2 pointer 繞一圈
 - dict 出現s裡的+1，出現t裡的-1
 - 最後結果要是0
 - 用get會更快嗎? 快一點點但差不多

### 344. Reverse String (E)
- 2 pointers 簡單收工

### 409. Longest Palindrome (E)
- 用 set 記出現過的，只要成對就 += 2，最後再補上可能的 1 (單獨出現在正中央)
- 想說我寫的已經很有效率，但不知道為啥表現沒很好，結果前面都用 collections.Counter

### 859. Buddy Strings (E)
- Brute Force 會 TLE (O(N^2))，要 O(N) 才會過，跑過一遍將所有狀況考慮好即可（完全相同、差異超過 2 個、差異等於 2 個）

### 3. Longest Substring Without Repeating Characters (M)
 - 用 set 記住出現過的，搭配雙重指標，一個記開頭一個記結尾
 - 當出現重複時，開頭移到重複+1處繼續找，並讓此時指針間的字母留在 set
 - 用 remove() 不要重創一個 set 就不用跑兩次(這樣速度變超快！99%讚！)
 - set 相關操作：`s.add(), s.remove()`
 - 有個類似的作法是用字典，並且持續 update 每個字母的位置，就可以瞬移

### 1647. Minimum Deletions to Make Character Frequencies Unique (M)
- 因為只能刪除，所以我們只要找出所有字母的頻率，並且從大到小檢查每個頻率，再把出現超過一次的往下帶，計算帶幾個（要刪幾次）直到 0 為止

## Trie
### 208. Implement Trie (Prefix Tree) (M)
- 原本有點不太確定，但搭配字典跟遞迴解沒有太難
- 結構是 Trie 中有個字典，裡面是小孩，結構為 {char: Trie}
- 要記得原本就有的要沿用，不要新創一個 Trie
- 其實他就是一個樹，但不需要每個小孩都創一個 Trie，用 dfs + 單純存字母 可以省空間跟時間
- 也不需要 dfs，就用字典包字典就好了，速度跟空間都好了不少
- 居然有人用 list 死記再用 str.startswith() 硬幹，他媽這三小狗子寫法 ==

### 676. Implement Magic Dictionary (M)
- 其實這題不用 trie，直接把所有都記下來一個一個比，或是記下 length 再比即可
- 但我還是嘗試用 trie 實作，有點擊敗浪費了我不少時間==


## Binary Tree
### 94. Binary Tree Inorder Traversal (E)
### 144. Binary Tree Preorder Traversal (E)
### 145. Binary Tree Postorder Traversal (E)
- 三題差不多，參照下面 BST，用遞迴 helper function 解決，不難但重要

### 100. Same Tree (E)
- recursion at its finest, just check this node & left & right

### 104. Maximum Depth of Binary Tree (E)
- dfs, keep every depth is this path
- remember: if not root then 0, if one node then 1(maxdepth = 1)

### 111. Minimum Depth of Binary Tree (E)
- bfs / dfs + updating depth when leaf node

### 226. Invert Binary Tree (E)
- dfs, then swap all the left & right
- remember to check: if not root then return

### 110. Balanced Binary Tree (E)
- [參考這篇的 code](https://ithelp.ithome.com.tw/articles/10213283)，其實蠻簡單的
- 用 recursion 檢查左右子樹高度是否差超過 1，左右子樹用 recursion 得到高度，base case 是 node == null return 0，若中間有任一子樹不平衡則一路 return -1 到頂就好，只要對 root 跑一次就好

### 512. Diameter of Binary Tree (E)
- 這到底算啥 Easy，至少要 medium 吧
- 用 recursion 紀錄每個節點最高高度，同時記錄最大直徑，所以有兩個回傳值
- 記得要 max(hr + hl, diar, dial)，因為要求所有樹中最大

### 102. Binary Tree Level Order Traversal (M)
- bfs, when current depth != now depth, create new list
- remember to update current depth

### 236. Lowest Common Ancestor of a Binary Tree (M)
- 原本想用 235 的解法，要注意一些差異，是可以但超慢 （因為現在是亂的，搜尋沒效率）
- 厲害的遞迴解：（若到底會回傳 None，若 l r 都不是 None 則結果是該位置的祖先）
```python=
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    l = self.lowestCommonAncestor(root.left,p,q)
    r = self.lowestCommonAncestor(root.right,p,q)

    if l and r:
        return root

    return l or r
```
### 863. All Nodes Distance K in Binary Tree (M)
- Nice question, need to go back in a binary tree -> traverse using bfs / dfs and construct a graph, then use graph to move k step!
- Don't be framed by given strcture, you can create another structure to help

### 1161. Maximum Level Sum of a Binary Tree (M)
- Traverse 過並記錄 level，再把對應的 level 加起來就好，要小心不要多存，不然有可能會錯（像是 0 > 所有負數），有幾層 level 就存多少就好

### 2265. Count Nodes Equal to Average of Subtree (M)
- 看起來有點難，但其實完全 ok，就是 DFS using recursion，每次回去的時候 return total sum & total count，並計算該 node 是否符合條件即可
- The magical I'm looking for is `nonlocal` inside the recursion function. ([Global & Nonlocal in Python](https://ktinglee.github.io/LearningPython100days(6)_global_and_nonlocal/))
## [Binary Search](https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1)

A Standard Binary Search:
```python=
def binary_search(list_sorted, target):
    left, right = 0, len(list_sorted)
    while left <= right:
        mid = (left + right) // 2
        if list_sorted[mid] > target:
            right = mid - 1
        elif list_sorted[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1
```


### 35. Search Insert Position (E)
- 因應 O(log N) 要求，此題為標準 binary search，想一下注意 return 哪個位置就好

### 69. Sqrt(x) (E)
- 用 binary search 來減少搜尋空間，要注意若最後一次是在 > 結束，結果要再減一（因為要不超過，且不保證有 exact match）

### 704. Binary Search (E)
- 一直在鬼打牆，要注意整個跟新的搜尋範圍怎麼寫
- 總搜尋範圍是 0~len-1，更新時左邊更新到中間+1，右邊更新到中間-1，反過來就會停不下來

### 278. First Bad Version(E)
- 為何為何這麼難...
- 最後是把數字當作 version 後間的間隔，不知道哪來的想法
- 可能是要從 base case 往上想會比較好想？
- 解決了 1 個、2 個的狀況，只要確認剩下的狀況都會正確的坍塌到這兩種即可

### 33. Search in Rotated Sorted Array (M)
- Binary search 變形版，其實邏輯清楚的話應該想得出來，多加點 if-else 判斷就好

### 209. Minimum Size Subarray Sum (M)
- 用 search 尋找正確答案，搭配 sliding window 計算 subarray sum，要注意是因為本題都是正數，subarray sum 只會隨著長度遞增，才能用這招
- 有個很猛的做法：2 pointers，右邊若還未滿足就一直前進，左邊則是在滿足時一直前進，將所有滿足的狀況記下來，可行的原因是其他沒有被判斷到的 subarray 都會知道是不滿足的，因為有比他更大的 subarray 被判斷到不滿足 or 比他更小的 subarray 被判斷到滿足

### 852. Peak Index in a Mountain Array (M)
- 就完全是 binary search 找最大，知道何時找左找右，還有處理邊界值跟尋找範圍就好，輕鬆


### 1802. Maximum Value at a Given Index in a Bounded Array (M)
- 這題看了 hint 之後大概知道怎麼做了，但卡住的不是 binary search，反而是 check() 的函數
- 遞迴會爆，不要硬幹，有邏輯的慢慢拆，先算出 shift 再用梯形公式加總就好，然後一次算完不要用減的會 overflow

## Binary Search Tree
- [3 ways to iterate BST](https://shubo.io/iterative-binary-tree-traversal/)
- In-order traversal (left -> mid -> right) will give you sorted list!

### 501. Find Mode in Binary Search Tree (E)
 - 直接 traverse 並把次數記在 hash table，不確定 BST 的性質要如何利用，要注意最多的可能不只一個

### 530. Minimum Absolute Difference in BST (E)
### 783. Minimum Distance Between BST Nodes (E)
- 完全一樣，用 in-order traverse 得到 sorted list，再 traverse 找出最小差距即可


### 235. Lowest Common Ancestor of a Binary Search Tree (M)
- dfs 找出 path，再一個一個比直到不同，前一個就是最低共同祖先
- 又有厲害的遞迴解了qq，但這次速度就差不多
- 蠻簡單直白的怎麼沒想到，若兩者不同邊則現在位置就是最低共同祖先，要好好利用 BST 的性質
```python=
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val > root.val and q.val > root.val:
            root = root.right
        elif p.val < root.val and q.val < root.val:
            root = root.left
        else:
            return root
```

### 1569. Number of Ways to Reorder Array to Get Same BST (H)
- Devide and Conquer + 排列組合，想很久，雖然中間漏掉一些狀況，但算是有想出來，左右子樹都有元素的情況下才會有排列的可能性，把這層的排列組合 x 左子樹的 x 右子樹的即可，要考慮清楚每層的總狀況
- 被[這個](https://stackoverflow.com/questions/67438654/is-x1e9-7-and-x109-7-different-in-python-if-yes-why)搞到心態差點崩潰，取 mod 要取 10**9+7 不能取 1e9+7，後者是浮點數會有運算問題，明明寫法就對但取模取錯 ==，[取模原因](https://www.zhihu.com/question/49374703)
- [牛逼的 solution](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/solutions/3643494/python-easy-fast-solution/)
```python=
def numOfWays(self, nums: List[int]) -> int:
    def f(nums):
        if len(nums) <= 2:
            return 1
        left = [v for v in nums if v < nums[0]]
        right = [v for v in nums if v > nums[0]]
        return comb(len(left) + len(right), len(right)) * f(left) * f(right)

    return (f(nums) - 1) % (10**9 + 7)
```
- `comb(len(left) + len(right), len(right))` 原因：
![](https://hackmd.io/_uploads/ByhMX9tD2.png)


## Recursion
### 17. Letter Combinations of a Phone Number (M)
 - 使用 recursion 的時候要注意，call 的位置跟回傳值的位置！
 - 這題跟其他兩題不同的地方是，他是從上往下呼叫，所以回傳值就要特別處理，最後用一層一層傳上來，不知道有沒有更好的？
 - 承上，如果我改做法，就可以從下往上呼叫，就沒有上面的問題了
 - 看到有人用 DFS，每當跑完所有路徑就加到 result，用 list 來記錄走過的順序，並且每結束一層就 pop 一次
 - 速度結果太不穩定，不知道到底快還慢
 - 要記得不要動態增加 iterator 的內容！！！

### 46. Permutations (M)
 - 用 1 當作 base case，在 return 的每個結果中每個位置都插一次
 - 這作法有點爛，感覺應該有更好的做法，但這個就跑得蠻快的了
 - 不要用 `copy.deepcopy()`，用 `list.copy()` 就好
 - [Python yield 的用法](https://ithelp.ithome.com.tw/articles/10258195)
 - [詳細解說參考](https://leetcode.com/problems/permutations/solutions/993970/python-4-approaches-visuals-time-complexity-analysis/)
 - 另解：classic backtracking

### 50. Pow(x, n) (M)
- 如題，但不能直接遞迴，要每次 // 2，這樣才不會爆
- 我用 memorization 解，也看到很多神奇的解法（迴圈也可以?），但核心精神就是要每次 // 2 再處理奇數


### 78. Subsets (M)
- 跟 46 大同小異，在 return 的每個 subset 都插一次並記錄下來回傳
- [不要動態持續修改 iterator](https://stackoverflow.com/questions/18254038/is-it-safe-to-change-the-iterator-dynamically-in-python)
- 這樣空間複雜度有點高？但其實也沒有差到太多
- 看到有人用 bin mask 做，蠻有創意的
- 好像也可以用 DFS 之類的做？

## Dynamic Programming
### 70. Climbing Stairs (E)
 - A very classic DP，就注意一些 DP 細節就好
 - 邊跑邊往之前參照，前 1 or 2 階有幾種方式到，這階就加上幾種方式
 - 看到有人用 [0,1,2] 開局直接往前算，用類似費波納契數列，似乎也可行？

### 118. Pascal's Triangle (E)
 - 一層一層建，下一層用前一層的結果往下
 - 在每層的 list 運算時前後各加一個 0，會比較好算

### 53. Maximum Subarray (M)
 - 建二維的 map 複雜度會到 O(n^2)，太慢沒過
 - 僅設一維 map，每個元素為「到這個元素為止的最大值」
    如此一來，每個元素的算法就會變成
    dp[i] = nums[i] + max(0,dp[i-1])
    蠻簡單易懂的
    ![](https://i.imgur.com/odVvoYT.png)
 - 可以參考[這裡](https://zhuanlan.zhihu.com/p/85188269)，Kadane's Algorithm 再進一步優化空間複雜度
    ```python=
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        max_end = max_subsum = nums[0]
        for i in range(1,N):
            max_end = nums[i] + max(0, max_end)
            max_subsum = max(max_end, max_subsum)
        return max_subsum
    ```

### 55. Jump Game (M)
- 原本的寫法好像沒 DP 到，從頭往前算邊建表，複雜度要 O(N^2)
- 更好的寫法是從終點往回找，並定期更新可以走到的最近的地方
```python=
def canJump(self, nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums)-1,-1,-1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0 
```

### 62. Unique Paths (M)
- 就是常見的方格可能走法，國高中數學竟然出現在 leetcode
- 可以少掉一些沒差的檢查，省點時間，有時候雖然不該計算，但不影響結果也可以讓他算，總結來說可以省去判斷時間

### 63. Unique Paths II (M)
- 跟 62 差不多，就是多了障礙物，一樣方法迴圈 + dp 解就好，用 recursive 從結尾叫回來反而慢超多不知為啥

### 97. Interleaving String (M)
- 用 recursion 結果 TLE，看了解答提示大概知道怎做，但就是做不出來，不知為何他想得跟我想的不一樣
- 基本上是一個 2d dp，先建兩個方向的第一排，然後再建後面的，建後面時參考前面是否有 n-1 個為 true 的情況（兩個方向），然後比較第 n 個是否一致即為 true

### 332. Coin Change (M)
 - 照順序跑跑到目標為止，檢查current - coin 是否有值，有就存最佳的
 - 當 current == coin 時設為 1 (這可以省略，因為上面的就可以處理這個狀況)
 - 複雜度為 O(CT)，C = len(coin)，T = Target

### 377. Combination Sum IV (M)
- 其實就是有多種 step size，問走到 target 有多少種走法
- 可以先 sort 過，遇到 step size > target 的就可以跳掉，會快一點（只有一點）

### 416. Partition Equal Subset Sum (M)
- 二維 dp，當放進去有達到就可以，但要小心特殊 case (除二就無法分、超過一半肯定無法分、還有要往哪些地方找)
- 更快的做法：一維 DP + 用 set 紀錄可以到達的數字，真是高明...

### 688. Knight Probability in Chessboard (M)
- 想用更快的方式解，結果 O(N^2 K) 的複雜度竟然可以==
- 基本上就是先建立一個一輪的 probability map，再用這個來計算下一輪機率，直到 k 輪後就是答案
- 看到有用 recursion + LRU cache （Memorization）的解法，酷又簡潔

### 837. New 21 Game (M)
- 被數學折磨死...我覺得我明明就算對...[解答](https://leetcode.com/problems/new-21-game/solutions/3560251/python-java-c-simple-solution-easy-to-understand/)
- 結果 DP 一維就夠，[解釋影片](https://www.youtube.com/watch?v=sVrX3OrBhGc)，這她媽誰想得出來==

### 1027. Longest Arithmetic Subsequence (M)
- 想出來的 TLE @@ 只好看個 Editorial
- dp 裡為「到這項為止有的公差與長度」，因此做一個 O(n^2) 迴圈時（right 固定），就可以檢查到前面所有出現過的公差，同時順便檢查該項是否有相同公差的已知長度，相加即可
![](https://hackmd.io/_uploads/B1P7ZpGuh.png)

### 1218. Longest Arithmetic Subsequence of Given Difference (M)
- Exactly how I thought! Nice! dp[i] = longest subsequence seen so far, dp[i] = dp[i-k] + 1, dp[i-k] = 0 if i-k not exist

### 956. Tallest Billboard (H)
- 想不到，好難想，但 [Editorial](https://leetcode.com/problems/tallest-billboard/editorial/) 的寫法好直白...哭了，不過也有人說這題很難
- 目的是平衡，所以要 diff = 0，同時要求最高高度，所以可以好好利用這兩個資訊，把所有可能的組合跑過記錄下來，13 行輕鬆解決
- Dynamic Programming 的精隨是使用前面往後面算，所以使用前面 rod 的各種平衡結果，往下一個 rod 的各種可能結果算，加上只要保留最高即可
```python=
def tallestBillboard(self, rods: List[int]) -> int:
    dp = {0:0} # dp[taller - shorter] = taller

    for r in rods:
        new_dp = dp.copy()
        for diff, taller in dp.items():
            shorter = taller - diff
            new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
            new_dp[abs(diff - r)] = max(new_dp.get(abs(diff - r), 0), taller, shorter + r)
        dp = new_dp

    return dp[0]
```

### 1547. Minimum Cost to Cut a Stick (H)
- 原本以為很難，結果還好，[解釋影片](https://www.youtube.com/watch?v=HYKVPfFGpiE)
- 用 Recursion + 2D DP (memorization) 即可，最直觀，也可以用迴圈

### 1575. Count All Possible Routes (H)
- 又一個 hard，還好這題算簡單，看了 hint 後有想出來，用 (idx, fuel) 作為 key，到終點的 path 數量作為 value，再用 recursive helper function 即可，要住到終點也還可以繼續走，只要 fuel 用光前都可以，另外迴圈對 fuel 或對 len(loc) 繞速度似乎都差不多快

### 1751. Maximum Number of Events That Can Be Attended II (H)
- [Solution](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/solutions/3770450/ex-amazon-explains-a-solution-with-a-video-python-javascript-java-and-c/) **TODO**

### 2272. Substring With Largest Variance (H)
- 有夠折磨，自己想就是想不出來，pairwise + [kadane's algorithms 變形版](https://leetcode.com/problems/substring-with-largest-variance/solutions/2579146/weird-kadane-intuition-solution-explained/)
- 總之就是個很詭異的兩兩做 kadane，要考慮 b 有出現並且適時重置位置，這題根本是狗屎吧想出來要想多久
- 也可以把 pair 的一次算完，會比較快，但我完全看不懂也不想看就是了
![](https://hackmd.io/_uploads/B1fT8_Sya.png)

### 2328. Number of Increasing Paths in a Grid (H)
- 原本的寫法 TLE，後來發現應該是因為一個長度一個長度算太慢，看了提示後直接改用 Recusive DP + Memorization，跟上面那題作法應該類似?
- 若還沒計算過的，計算並 recursively call 附近的 node，計算過的直接回傳 memory 結果（2D DP）


## Math
### 9. Palindrome Number (E)
- 用 string + 2 pointers
- math way is to calculate from the other side again, i.e. keep *= 10 and += x%10

### 13. Roman to Integer (E)
 - 好玩簡單，用dict加上升降序的概念即可
 - 怎麼一堆人寫出詭異的code@@
 - 兩種Case若皆須相同操作可以寫一起

### 168. Excel Sheet Column Title (E) & 171 Excel Sheet Column Number (E)
- 先寫 171 會比較好想 168，171 就是不斷乘加乘加，168 要注意它不是一個完整的 26-based 進位系統，她可以有 26 (Z) 的出現，且沒有 0，處理方式就是當遇到 mod 26 = 0 的時候，要手動扣掉一次 26 並加上 Z，並不是 25 或 27 進位，是詭異的 26 進位


### 202. Happy Number (E)
- 就照規則算就好，要記錄出現過的避免 loop

### 258. Add Digits (E)
- 用迴圈很簡單，用數學算的話更快，直接 % 9 再處理 edge cases 就好

### 263. Ugly Number (E)
- Edge cases: 負數必 False，1 True(don't know why)
- 一直除以 2,3,5 直到不能除，再檢查是否為 1 即可

### 412. FizzBuzz (E)
- 拍手遊戲，毫無難度

### 1232. Check If It Is a Straight Line (E)
- 用斜率無難度，但被 inf 搞混了 == 有夠笨
- 如果不想處理除法的例外，不如就用乘法ㄅ！

## Graph
### 733. Flood Fill (E)
- 蠻好玩經典的填色題，就要嘛 DFS 要嘛 BFS，上下左右都找完就好（我用DFS）
- 要注意若初始格顏色已經一樣就不用填色，害我在那邊算半天==
- [用 deque 來實現 Stack (DFS) 與 Queue (BFS)](https://leetcode.com/problems/flood-fill/solutions/2332243/python-dfs-bfs-solution/?q=python+dfs+bfs&orderBy=most_relevant) (原來這麼方便！)：
```python=
# Generalization
from collections import deque
H = len(image)
W = len(image[0])
v = image[sr][sc]
if v == color:
    return image

to_search = deque([(sr,sc)])

while to_search:
    # Stack (LIFO, DFS)
    # (nowsr, nowsc) = to_search.pop()

    # Queue (FIFO, BFS)
    (nowsr, nowsc) = to_search.popleft()

    for (i,j) in [(0,1),(0,-1),(1,0),(-1,0)]:
        newsr = nowsr + i
        newsc = nowsc + j
        if newsr in range(0,H) and newsc in range(0,W):
            if image[newsr][newsc] == v:
                to_search.append((newsr,newsc))
    print(to_search)
    image[nowsr][nowsc] = color
return image
```

### 133. Clone Graph (M)
- 複製 graph of nodes，一樣先做 bfs 但先存 index，最後再把 index 轉成 nodes，用字典暫存 nodes (hash table)
- 其實不用先存 index，可以先初始化 node，然後每走完一個鄰居就 append 進去，bfs 完這個 node 的鄰居也就加完了


### 200. Number of Islands (M)
- 就 DFS / BFS + Matrix，不難，每到一個陸地就搜完所有相連陸地
- [寫得很好的 Union Find](https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/UnionFind%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3.md) & [Union Find / Disjoint Set](https://haogroot.com/2021/01/29/union_find-leetcode/) 

### 542. 01 Matrix (M)
- 注意原始的 0 1 沒有意義，好難...
- 寫了超久錯了超多次，最後也只寫出一個爛爛的作法：
    先把所有非零的格子設為超大數
    跑兩層迴圈過所有格子，若為超大數則做 BFS
    BFS:
    用 Queue 實作，要存目前 distance
    當 BFS 到零格子的時候，總距離就是這格的值
    同時所有走過的格子都可以更新 distance
    不能走重複的路，不然會 TLE
 - 好像有很簡單的寫法，等等來看一下 [Editorial](https://leetcode.com/problems/01-matrix/editorial/)
 - DP 的作法好讚...簡潔又快，但要記得要做兩次(兩個方向各一次)
 - Python range() 若是倒序要記得加 step size
```python=
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    self.r = len(mat)
    self.c = len(mat[0])
    self.maxcost = self.r * self.c
    dis = [[mat[i][j]*self.maxcost for j in range(self.c)] for i in range(self.r)]
    for i in range(self.r):
        for j in range(self.c):
            if mat[i][j]:
                if i > 0:
                    dis[i][j] = min(dis[i][j], dis[i-1][j] + 1)
                if j > 0:
                    dis[i][j] = min(dis[i][j], dis[i][j-1] + 1)

    for i in range(self.r-1,-1,-1):
        for j in range(self.c-1,-1,-1):
            if mat[i][j]:
                if i < self.r-1:
                    dis[i][j] = min(dis[i][j], dis[i+1][j] + 1)
                if j < self.c-1:
                    dis[i][j] = min(dis[i][j], dis[i][j+1] + 1)
    return dis
```
### 547. Number of Provinces (M)
- Count the number of connected component using dfs / bfs

### 782. Is Graph Bipatite (M)
- [解答](https://leetcode.com/problems/is-graph-bipartite/solutions/3540122/image-explanation-both-bfs-dfs-ways-c-java-python/)，我想不出來@@，用填色方法，相鄰的填不同顏色

### 994. Rotting Oranges (M)
- 類似 flood fill
- BFS，反正就找到沒有相鄰 1 的時候，把 round count 回傳就好，不能 DFS 因為要最快完成的回合
- 要注意沒有相鄰 1 但有可能有 不相鄰 1，我在一開始的地方用 onecnt 算有多少 1，確保經過的數量要一樣多

### 1557. Minimum Number of Vertices to Reach All Nodes (M)
- 原本不知道怎麼做，結果超簡單，答案就直接是所有 indegree = 0 的 vertices（怎麼會是 M）

### 2101. Detonate the Maximum Bombs (M)
- 先用 table 記下距離，再根據距離去 dfs/bfs 即可，要注意只要走的到都算，而不是要同一條路
- 把 table 跟後面 dfs/bfs 一起跑，結果不知為何更慢 ==，詭異


## Hash Table / Hash Function
### 383. Ransom Note (E)
- Easy peasy lemon squeezy
- 字典紀錄出現次數，再用扣掉的就好

### 705. Design HashSet (E)
- Many ways to do that (good and bad), a simple approach is use % 10^3 as hash function
- Use python built-in list as linked list

### 1396. Design Underground System (M)
- 沒啥難度，但要小心使用甚麼 key (a ab & aa b)


## Binary
### 67. Add Binary (E)
- 就是加法器，用 % // 計算 carry left 就好
- 但要小心一些很靠腰的錯誤


## Stone Game (DP + Game theory)
### 486. Predict the Winner (M)
### 877. Stone Game (M)
- Return True XDDDD
- [1D Version Explanation](https://leetcode.com/problems/stone-game/solutions/154610/dp-or-just-return-true/comments/393623)，這真的有夠難想，也有 2D Version
- 做 486 的時候重想了一遍，最一開始 dp 是 window = 0 的狀況，意即直接拿走，後面就是慢慢擴大 window size 到整個 array，檢查每次擴大時，到底拿左還是拿右賺，並更新上去，最後第 0 個位置就會是一開始 window size 為 n 時的虧損狀況，但是只會往一個方向更新，真的很難==
```python=
def stoneGame(self, p):
    n = len(p)
    dp = p[:]
    for d in range(1, n):
        for i in range(n - d):
            dp[i] = max(p[i] - dp[i + 1], p[i + d] - dp[i])
    return dp[0] > 0
```

### 1140. Stone Game II (M)
- 算有趣但好難，我覺得我概念想出來了但還是沒 AC，[解答](https://leetcode.com/problems/stone-game-ii/solutions/3563326/python-java-c-simple-solution-easy-to-understand/)
- 用總和減掉的，會比較好算，同時 index 也要搞清楚，架構跟迴圈都跟我寫的差不多

### 1406. Stone Game III (H)
- 這次寫了兩個小時總算靠自己 AC 了 QQ，但時間跟空間可以再優化
- 寫法跟前面差不多，找出 best response 並更新 dp table
- 這解法太神奇了...把 DP 用到極致大概就是這樣...(Biggest comparative outcome)
```python=
def stoneGameIII(self, stoneValue: List[int]) -> str:
    n = len(stoneValue)
    dp = [0] * (n + 1)
    for i in range( n - 1, -1, -1):
        dp[i] = stoneValue[i] - dp[i + 1]
        if i + 2 <= n:
            dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] - dp[i + 2])
        if i + 3 <= n:
            dp[i] = max(dp[i], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]) 

    if dp[0] > 0:
        return "Alice"
    if dp[0] < 0:
        return "Bob"
    return "Tie"
```

## Simulation
### 832. Flipping an Image (E)
- 一個一個反過來 traverse，再直接插入其 inverse 即可

### 1603. Design Parking System (E)
- 沒啥好說的，比 2 sum 還簡單

## Bit Manipulation 
### 137. Single Number II
- 這題的魔法太酷了，總之 a ^ b ^ b (a xor b xor b) 會等於 a，但這題是三次，所以他用兩個變數分別記錄出現一次與兩次的，但彼此之間不可以互搶所以用 ones ^= (num & ~twos) 的方式，一定要是非出現兩次的才可以加到 ones，twos 也是，最後的 ones 就是答案

### 1318. Minimum Flips to Make a OR b Equal to c (M)
- 直接迴圈一個一個判斷的話，還蠻簡單的，但情況要想清楚就好
- 也可以直接用 bit 的 logic 跟 shift 來處理

## Prefix Sum
### 724. Find Pivot Index (E)
### 1991. Find the Middle Index in Array (E)
- 用 prefix sum array，判定是否有 `prefix[i] + prefix[i+1] == prefix[-1]` 即可（中間項 + 兩倍左邊總和 == Array 總和，該中間項 index 就是 pivot），注意範圍即可
- 或這個方法也蠻酷的，簡單易懂，類似 2 pointers 移動：
```python=
def findMiddleIndex(self, nums: List[int]) -> int:
    left_sum=0
    right_sum=sum(nums)
    for i in range(len(nums)):
        if(left_sum == right_sum-nums[i]):
            return i

        left_sum=left_sum+nums[i]
        right_sum=right_sum-nums[i]
    return -1
```

### 1480. Running Sum of 1d Array (E)
- 標準 prefix sum，同 1732

### 1588. Sum of All Odd Length Subarrays (E)
- 蠻酷的一題，先搞出 prefix array，再用 2 pointers 相減，就是 sum of odd subarray 了，2 pointers 的 diff 為 1,3,5,7...
- hint says brute force (range step = 2)，or use math to calculate occurences then multiplies it and sums up: `return sum(((i + 1) * (len(arr) - i) + 1) // 2 * arr[i] for i in range(len(arr)))`

### 1732. Find the Highest Altitude (E)
- Prefix Sum，其實也不用，traverse 過一遍，更新高度並記錄最大值就好，不過這其實就是標準 Prefix Sum


## Sliding Window
### 1493. Longest Subarray of 1's After Deleting One Element (M)
- 先 Traverse 一遍找出 0 1 的出現次數，再用 window 的方式看可否將中間 0 去掉並更新最大值，若不行就只更新左右兩個 1 的最大值，要注意一些邊界條件

### 424. Longest Repeating Character Replacement (M)
### 1004. Max Consecutive Ones III (M)
- 這兩題都算是 2024 的變種，稍微改一下判斷條件就可，似乎有更快的解法未來有碰到再回來看

### 2024. Maximize the Confusion of an Exam (M)
- 其實不難，用 k 大小開始的 sliding window，一直擴大，直到不行（T、F 相差大於 k）就縮左邊，持續記錄最大總長度即可，應該要想出來的 @@

### 2090. K Radius Subarray Averages (M)
- Sliding Window，注意邊界條件還有 window 大小的判斷
- 亦可用 Prefix Sum 來解，不過也要 window 所以差不多意思


## Buy & Sell Stock
### 121. Best Time to Buy and Sell Stock (E)
 - 想得太複雜了，用O(n)就能解決
 - 對於當下的價格，歷史最低價買進並在當下賣肯定是最賺
 - 跑過全部一次，找到最賺就好了

### 122. Best Time to Buy and Sell Stock II (M)
- 想不到@@，結果是找到所有綠線（上升處）再加總即可，因為已知所有股票價錢，最賺就是所有低谷到高峰都買，且 [1,2,3] 跟 [1,3] 一樣都賺 2，簡單 O(n) 解決
- 另解：一樣用迴圈，把該回買跟不買可以獲得的最大 profit 記錄下來，並且買只能以不買的 profit 來算，繞過所有以後就是答案
```python=
def maxProfit(self, prices: List[int]) -> int:
    prevS, prevB = 0,0
    currS, currB = 0,0

    for i in range(len(prices)-1,-1,-1):
        currS = max(prices[i] + prevB, prevS)
        currB = max(-prices[i] + prevS, prevB)
        prevS = currS
        prevB = currB

    return currB
```

### 714. Best Time to Buy and Sell Stock with Transaction Fee (M)
- 用上題的另解，在每次買貨賣的時候加入 fee 即可


## Shortest Path
### 399. Evaluate Division (M)
- Find Path in Weighted Graph，有夠難搞，明明就沒有很難
- 不知為何我的 dfs stack 會 MLE，只好參考別人的用 dfs recursion

### 743. Network Delay Time (M)
- 也是 Dijkstra 小修改，注意是有向圖，從 1514 修改就好

### 1514. Path with Maximum Probability (M)
- 標準的 [Dijkstra's Algorithm](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2) 小修改 / [Why it worked](https://stackoverflow.com/questions/2856670/why-does-dijkstras-algorithm-work)
- 注意實作方法，不好的資料結構或 Traverse 很容易 TLE / MLE，做類似 dfs / bfs 的 search，但用 heap 來儲存，就可以確保每次 visited 的都是當前最佳的路徑，直到所有都找完或先找到終點為止，另外用 adjacency list 的方式存 path ( [{e: w}, {}, {} ...] ) 會比較省空間也比較快，還有去過的就不用再去了，最先去的路徑一定最佳

## [Backtracking](https://medium.com/appworks-school/%E9%80%B2%E5%85%A5%E9%81%9E%E8%BF%B4-recursion-%E7%9A%84%E4%B8%96%E7%95%8C-%E4%B8%89-d2fd70b5b171)

### 77. Combinations (M)
- simple but classic backtracking

### 2305. Fair Distribution of Cookies (M)
- 標準 Backtracking，但需要稍微 optimized 一下
- 看了最佳解快超多（但他多一個迴圈）：先用最少的人先拿最大塊的方法找到一個不差的解，再把它當作上限，超過就不用找，另外直接把每個人的 cookies 數量記著，不要記分配方式，比較麻煩

### 1601. Maximum Number of Achievable Transfer Requests(H)
- 標準 Backtracking 即可通過，甚至更簡單，每個就是選或不選，不過也有人寫很快版本

### 1723. Find Minimum Time to Finish All Jobs (H)
- 同 2305，但 k 更大時間更嚴格，所以相同的 code 不行，用 2305 的最佳解竟然還 TLE...
- **TODO** [99% Solution](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/solutions/3819577/4-optimizations-that-can-be-made-beats-99-53-in-runtime/)


## Topological Sort
### 207. Course Schedule (M)
- [有向圖找 Cycle](https://segmentfault.com/a/1190000005687907)，基本上一模一樣
- 算是寫出來了，但超慢，待檢查
- Topological sort
    - If cycle then not possible
    - Must have a vertex with indegree = 0
- [這個解法](https://leetcode.com/problems/course-schedule/solutions/58586/python-20-lines-dfs-solution-sharing-with-explanation/)快多了，也很易懂@@ (Recursive dfs)

### 802. Find Eventual Safe States (M)
- 跟 207 差不多，主要就是 Topological sort，先找出 terminal 然後看有沒有 cycle，如果走到已經是 terminal 的地方就 ok
- 這個主題還需要再熟一點！