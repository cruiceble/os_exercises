#lec 3 SPOC Discussion

## 第三讲 启动、中断、异常和系统调用-思考题

## 3.1 BIOS
 1. 比较UEFI和BIOS的区别。
 1. 描述PXE的大致启动流程。

## 3.2 系统启动流程
 1. 了解NTLDR的启动流程。
 1. 了解GRUB的启动流程。
 1. 比较NTLDR和GRUB的功能有差异。
 1. 了解u-boot的功能。

## 3.3 中断、异常和系统调用比较
 1. 举例说明Linux中有哪些中断，哪些异常？
 1. Linux的系统调用有哪些？大致的功能分类有哪些？  (w2l1)

	总计有三百多个系统调用，常见有206个系统调用，主要分为进程控制、文件系统控制（文件读写操作、文件系统操作）、系统控制、内存管理、网络管理、socket控制、用户管理、进程间通信（信号、消息、管道、信号量、共享内存）。

```
  + 采分点：说明了Linux的大致数量（上百个），说明了Linux系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
 1. 以ucore lab8的answer为例，uCore的系统调用有哪些？大致的功能分类有哪些？(w2l1)
 
	总共有22个系统调用，分为文件操作（sys_pgdir, sys_gettime, sys_open, sys_close, sys_read, sys_write, sys_seek, sys_fstat, sys_dup, sys_getdirentry），进程管理（sys_exit, sys_fork, sys_wait, sys_exec, sys_yield, sys_kill, sys_getpid, sys_sleep），内存管理三类（sys_lab6_set_priority, sys_fsync, sys_getcwd, sys_putc）。

 ```
  + 采分点：说明了ucore的大致数量（二十几个），说明了ucore系统调用的主要分类（文件操作，进程管理，内存管理等）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.4 linux系统调用分析
 1. 通过分析[lab1_ex0](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex0.md)了解Linux应用的系统调用编写和含义。(w2l1)
 
Objdump：对于目标文件进行反汇编，命令格式为：
objdump
[-a] [-b bfdname |
--target=bfdname] [-C] [--debugging]
[-d] [-D]
[--disassemble-zeroes]
[-EB|-EL|--endian={big|little}] [-f][1] 
[-h] [-i|--info]
[-j section | --section=section]
[-l] [-m machine ] [--prefix-addresses]
[-r] [-R]
[-s|--full-contents] [-S|--source]
[--[no-]show-raw-insn] [--stabs] [-t]
[-T] [-x]
[--start-address=address] [--stop-address=address]
[--adjust-vma=offset] [--version] [--help]

Nm: 列出目标文件符号清单，命令格式为nm [-a|--debug-syms] [-g|--extern-only] [-B][-C|--demangle] [-D|--dynamic] [-s|--print-armap][-o|--print-file-name] [-n|--numeric-sort][-p|--no-sort] [-r|--reverse-sort] [--size-sort][-u|--undefined-only] [-l|--line-numbers] [--help][--version] [-t radix|--radix=radix][-P|--portability] [-f format|--format=format][--target=bfdname] [objfile...]

File: 该命令用来识别文件类型，也可用来辨别一些文件的编码格式。它是通过查看文件的头部信息来获取文件类型。

系统调用含义：安全起见，许多I/O操作的指令都被限制在只有内核模式可以执行，为了达到这个目的，内核提供一系列具备预定功能
的多内核函数，通过一组称为系统调用的接口呈现给用户。系统调用把应用程序的请求传给内核，调用相应的的内核函数完成所需的处理，将
处理结果返回给应用程序。

 ```
  + 采分点：说明了objdump，nm，file的大致用途，说明了系统调用的具体含义
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 
 ```
 
 1. 通过调试[lab1_ex1](https://github.com/chyyuu/ucore_lab/blob/master/related_info/lab1/lab1-ex1.md)了解Linux应用的系统调用执行过程。(w2l1)
 
	Strace： strace常用来跟踪进程执行时的系统调用和所接收的信号。 在Linux中进程不能直接访问硬件设备，当进程需要访问硬件设备(比如读取磁盘文件，接收网络数据等等)时，必须由用户态模式切换至内核态模式，通 过系统调用访问硬件设备。strace可以跟踪到一个进程产生的系统调用,包括参数，返回值，执行消耗的时间。

 ```
  + 采分点：说明了strace的大致用途，说明了系统调用的具体执行过程（包括应用，CPU硬件，操作系统的执行过程）
  - 答案没有涉及上述两个要点；（0分）
  - 答案对上述两个要点中的某一个要点进行了正确阐述（1分）
  - 答案对上述两个要点进行了正确阐述（2分）
  - 答案除了对上述两个要点都进行了正确阐述外，还进行了扩展和更丰富的说明（3分）
 ```
 
## 3.5 ucore系统调用分析
 1. ucore的系统调用中参数传递代码分析。
 1. ucore的系统调用中返回结果的传递代码分析。
 1. 以ucore lab8的answer为例，分析ucore 应用的系统调用编写和含义。
 1. 以ucore lab8的answer为例，尝试修改并运行代码，分析ucore应用的系统调用执行过程。
 
## 3.6 请分析函数调用和系统调用的区别
 1. 请从代码编写和执行过程来说明。
   1. 说明`int`、`iret`、`call`和`ret`的指令准确功能
 

