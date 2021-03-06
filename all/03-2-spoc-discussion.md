# lec6 SPOC思考题


NOTICE
- 有"w3l2"标记的题是助教要提交到学堂在线上的。
- 有"w3l2"和"spoc"标记的题是要求拿清华学分的同学要在实体课上完成，并按时提交到学生对应的git repo上。
- 有"hard"标记的题有一定难度，鼓励实现。
- 有"easy"标记的题很容易实现，鼓励实现。
- 有"midd"标记的题是一般水平，鼓励实现。


## 个人思考题
---

（1） (w3l2) 请简要分析64bit CPU体系结构下的分页机制是如何实现的

        
       　　　　
```
  + 采分点：说明64bit CPU架构的分页机制的大致特点和页表执行过程
  - 答案没有涉及如下3点；（0分）
  - 正确描述了64bit CPU支持的物理内存大小限制（1分）
  - 正确描述了64bit CPU下的多级页表的级数和多级页表的结构或反置页表的结构（2分）
  - 除上述两点外，进一步描述了在多级页表或反置页表下的虚拟地址-->物理地址的映射过程（3分）
 ```
- [x]  

>  当前64位CPU地址总线都是40位的，实际只支持2^40的内存寻址空间。
        多级页表分为4级。
        以4kb的页面为例，线性地址各位分配如下：
        0－11位：页内偏移offset　　 
       12－20位：Table 　　
       21－29位：Directory
       30－38位：Directory Ptr
       39－47位：PML4
       48 - 63位：符号扩展位
       其中映射过程如下：
       1. PML4索引PML4表项，指向PDP（Page-Directory Pointer Table）
       2. Directory Ptr索引PDP表项，指向PDE（Page-Directory）
       3. Directory索引PDE表项，指向PTE（Page-Table）
       4. Table在PTE中获取物理页帧号
       5. 物理页帧号加上offset即为物理地址

## 小组思考题
---

（1）(spoc) 某系统使用请求分页存储管理，若页在内存中，满足一个内存请求需要150ns。若缺页率是10%，为使有效访问时间达到0.5ms,求不在内存的页面的平均访问时间。请给出计算步骤。 


- [x]  
>  解： 设不在内存的平均访问时间是xms
       根据缺页率10%，有效访问时间为0.5ms
       列出方程： 0.5 = 0.00015*0.9 + x*0.1
                    x = 4.998 ms

（2）(spoc) 有一台假想的计算机，页大小（page size）为32 Bytes，支持32KB的虚拟地址空间（virtual address space）,有4KB的物理内存空间（physical memory），采用二级页表，一个页目录项（page directory entry ，PDE）大小为1 Byte,一个页表项（page-table entries
PTEs）大小为1 Byte，1个页目录表大小为32 Bytes，1个页表大小为32 Bytes。页目录基址寄存器（page directory base register，PDBR）保存了页目录表的物理地址（按页对齐）。

PTE格式（8 bit） :
```
  VALID | PFN6 ... PFN0
```
PDE格式（8 bit） :
```
  VALID | PT6 ... PT0
```


其VALID==1表示，表示映射存在；VALID==0表示，表示映射不存在。
PFN6..0:页帧号
PT6..0:页表的物理基址>>5

结果如下，代码在结果后面：

```
Virtual Address 6c74:
  -->pde index:0x1b pde contents:(valid 1, pfn 0x20)
    -->pte index:0x3 pde contents:(valid 1, pfn 0x61)
      -->Translates to Physical Address 0xc34 --> Value: 0x6
Virtual Address 6b22:
  -->pde index:0x1a pde contents:(valid 1, pfn 0x52)
    -->pte index:0x19 pde contents:(valid 1, pfn 0x47)
      -->Translates to Physical Address 0x8e2 --> Value: 0x1a
Virtual Address 3df:
  -->pde index:0x0 pde contents:(valid 1, pfn 0x5a)
    -->pte index:0x1e pde contents:(valid 1, pfn 0x5)
      -->Translates to Physical Address 0xbf --> Value: 0xf
Virtual Address 69dc:
  -->pde index:0x1a pde contents:(valid 1, pfn 0x52)
    -->pte index:0xe pde contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
Virtual Address 317a:
  -->pde index:0xc pde contents:(valid 1, pfn 0x18)
    -->pte index:0xb pde contents:(valid 1, pfn 0x35)
      -->Translates to Physical Address 0x6ba --> Value: 0x1e
Virtual Address 4546:
  -->pde index:0x11 pde contents:(valid 1, pfn 0x21)
    -->pte index:0xa pde contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
Virtual Address 2c03:
  -->pde index:0xb pde contents:(valid 1, pfn 0x44)
    -->pte index:0x0 pde contents:(valid 1, pfn 0x57)
      -->Translates to Physical Address 0xae3 --> Value: 0x16
Virtual Address 7fd7:
  -->pde index:0x1f pde contents:(valid 1, pfn 0x12)
    -->pte index:0x1e pde contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)
Virtual Address 390e:
  -->pde index:0xe pde contents:(valid 0, pfn 0x7f)
      --> Fault (page directory entry not valid)
Virtual Address 748b:
  -->pde index:0x1d pde contents:(valid 1, pfn 0x0)
    -->pte index:0x4 pde contents:(valid 0, pfn 0x7f)
      --> Fault (page table entry not valid)

```
代码：
```
#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
int base = 544;
int q[10]={0x6c74, 0x6b22,0x03df, 0x69dc, 0x317a, 0x4546, 0x2c03, 0x7fd7, 0x390e, 0x748b};
int main(){
    ifstream fin;
    fin.open("a.txt");
    int a[4096];
    int i=0;
    while (fin >> hex >> a[i]){
	i++;	
    }
    for (int i=0; i<10; i++){
	cout << "Virtual Address " << hex << q[i] << ":" << endl;
	cout << "  -->pde index:0x" << (q[i]>>10) << " pde contents:(valid " << (a[base+(q[i]>>10)]>>7) << ", pfn 0x" << (0x7f & a[base+(q[i]>>10)]) << ")" << endl;
	if (a[base+(q[i]>>10)]>>7) {
	    cout << "    -->pte index:0x" << (0x1f & (q[i]>>5)) << " pde contents:(valid " << (a[0+((0x7f & a[base+(q[i]>>10)])<<5)+(0x1f & (q[i]>>5))]>>7) << ", pfn 0x" << (0x7f &a[0+((0x7f & a[base+(q[i]>>10)])<<5)+(0x1f & (q[i]>>5))]) << ")" << endl;
	    if  (a[0+((0x7f & a[base+(q[i]>>10)])<<5)+(0x1f & (q[i]>>5))]>>7){
		cout << "      -->Translates to Physical Address 0x" << ((0x7f &a[0+((0x7f & a[base+(q[i]>>10)])<<5)+(0x1f & (q[i]>>5))])<<5) + (0x1f & q[i]) << " --> Value: 0x" << a[(((0x7f &a[0+((0x7f & a[base+(q[i]>>10)])<<5)+(0x1f & (q[i]>>5))])<<5) + (0x1f & q[i]))] << endl;
	    } else
		cout << "      --> Fault (page table entry not valid)" << endl;
	} else 
	    cout << "      --> Fault (page directory entry not valid)"<<endl;
    }
    fin.close();
    return 0;
}

```


（3）请基于你对原理课二级页表的理解，并参考Lab2建页表的过程，设计一个应用程序（可基于python, ruby, C, C++，LISP等）可模拟实现(2)题中描述的抽象OS，可正确完成二级页表转换。


（4）假设你有一台支持[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)的机器，请问你如何设计操作系统支持这种类型计算机？请给出设计方案。


--- 

## 扩展思考题

阅读64bit IBM Powerpc CPU架构是如何实现[反置页表](http://en.wikipedia.org/wiki/Page_table#Inverted_page_table)，给出分析报告。

--- 
