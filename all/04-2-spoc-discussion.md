#lec9 虚存置换算法spoc练习

## 个人思考题
1. 置换算法的功能？

2. 全局和局部置换算法的不同？

3. 最优算法、先进先出算法和LRU算法的思路？

4. 时钟置换算法的思路？

5. LFU算法的思路？

6. 什么是Belady现象？

7. 几种局部置换算法的相关性：什么地方是相似的？什么地方是不同的？为什么有这种相似或不同？

8. 什么是工作集？

9. 什么是常驻集？

10. 工作集算法的思路？

11. 缺页率算法的思路？

12. 什么是虚拟内存管理的抖动现象？

13. 操作系统负载控制的最佳状态是什么状态？

## 小组思考题目

----
(1)（spoc）请证明为何LRU算法不会出现belady现象

```
设S为物理页面数量为n的LRU算法的缺失率,算法表示为K，S1是物理页面数量为n+l的LRU算法缺失率，算法表示为K1
证明对于任意访存次数p，S>=S1。
 
数学归纳法：
P=0时候，S=S1=0
当P<=i(i=0,1,2,。。。)时S<S1，在P = i+1时, 第i+1次访问的可能情况有：K与K1都不缺页，K与K1都缺页，K缺页K1不缺页。这三种情况均能保证p=i+1时S>=S1.而K1缺页K不缺页这种情况不存在，因为前n次访问一定包含于钱n+l次访问中
 
综上所述，由数学归纳法得， 对于任意非负整数P均有S>=S1。
即对任意时刻，对S1的缺页数量不会大于S。即物理页数量增加，缺页率不会上升。
 
即证明了，LRU算法，不会出现belady现象。
```

(2)（spoc）根据你的`学号 mod 4`的结果值，确定选择四种替换算法（0：LRU置换算法，1:改进的clock 页置换算法，2：工作集页置换算法，3：缺页率置换算法）中的一种来设计一个应用程序（可基于python, ruby, C, C++，LISP等）模拟实现，并给出测试。请参考如python代码或独自实现。
 - [页置换算法实现的参考实例](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab3/page-replacement-policy.py)

```
余数为0；
代码：
a=['c','a','d','b','e','b','a','b','c','d']
stacksize=4
stack=[]
num=0
order=0
for i in a:
    order+=1
    print ""
    print "step",order,":"
    if  i in stack:
        stack.remove(i)
        print i," alredy in stack, get it to the top"
        
    stack.insert(0,i)
    if len(stack)>stacksize:
        stack.pop()
        print "stack already full, pop the bottom"
        num+=1
    else:
         print "insert",i,"into stack"
    print "now stack is : ",stack
print "\nFinally:"
print "Page fault number = ", num
结果：
step 1 :
insert c into stack
now stack is :  ['c']

step 2 :
insert a into stack
now stack is :  ['a', 'c']

step 3 :
insert d into stack
now stack is :  ['d', 'a', 'c']

step 4 :
insert b into stack
now stack is :  ['b', 'd', 'a', 'c']

step 5 :
stack already full, pop the bottom
now stack is :  ['e', 'b', 'd', 'a']

step 6 :
b  alredy in stack, get it to the top
insert b into stack
now stack is :  ['b', 'e', 'd', 'a']

step 7 :
a  alredy in stack, get it to the top
insert a into stack
now stack is :  ['a', 'b', 'e', 'd']

step 8 :
b  alredy in stack, get it to the top
insert b into stack
now stack is :  ['b', 'a', 'e', 'd']

step 9 :
stack already full, pop the bottom
now stack is :  ['c', 'b', 'a', 'e']

step 10 :
stack already full, pop the bottom
now stack is :  ['d', 'c', 'b', 'a']

Finally:
Page fault number =  3
```
 
## 扩展思考题
（1）了解LIRS页置换算法的设计思路，尝试用高级语言实现其基本思路。此算法是江松博士（导师：张晓东博士）设计完成的，非常不错！

参考信息：

 - [LIRS conf paper](http://www.ece.eng.wayne.edu/~sjiang/pubs/papers/jiang02_LIRS.pdf)
 - [LIRS journal paper](http://www.ece.eng.wayne.edu/~sjiang/pubs/papers/jiang05_LIRS.pdf)
 - [LIRS-replacement ppt1](http://dragonstar.ict.ac.cn/course_09/XD_Zhang/(6)-LIRS-replacement.pdf)
 - [LIRS-replacement ppt2](http://www.ece.eng.wayne.edu/~sjiang/Projects/LIRS/sig02.ppt)

