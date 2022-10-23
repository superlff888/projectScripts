# @Time  : 2021/1/12 13:18
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
IO流
open(filename,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
参数说明：
    filename:文件名称的字符串值
    mode:只读r，写入w，追加a，默认文件访问模式为只读r
    buffering：寄存区缓存 ，可以通过它来控制IO的操作；通常系统默认，读取大文件时，可以选择性设置缓存区大小
        0：不寄存
        1：访问问及那时会寄存行
        >1:寄存区的缓存大小
        负值：寄存区缓存大小为系统默认

"""
f = open('data.txt')
print(f.readlines())  # 如果文件特别大，可能会再读取过程中占用过大系统内存，导致系统卡死
print('---')
print(f.readline())  # 上面执行过read()相当于已经流出来了，可以理解成里面没内容了，故再执行readline肯定打印不出来内容
f.close()

### 上面这种方式每次都要关闭文件,释放程序资源，避免死锁
###  -----


"""
python中提供了一个简单的方法：
    with open(files) as 别名:
        with语句块
    --with语句块可以将文件打开后，操作完毕，自动关闭这个文件，避免每次都要关闭文件的麻烦
    --文件操作代码应放在with语句块里
    --正常的文本读取使用'rt',即默认格式即可
    --图片读取需要使用'rb'【即with open('test.txt','rb') as f:】,读取二进制格式
"""

with open('data.txt') as f:
    while True:
        line = f.readline()  #按行读取，节省资源
        if line:    # 如果行有数据
            print(line)
        else:
            break
# print会完成换行的操作，行尾也会有\n换行，故输出结果会空两行


with open('data.txt') as f:
    f.readlines()

