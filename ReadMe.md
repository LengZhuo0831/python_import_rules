## 1. About
This repo shows us how to import vars, modules or packages in python projects for beginners. \
这个文件向新学者展示python项目中如何使用import来引用你想要的变量、模块或者包。

## 2. import 同一个目录下的变量、类、模块、包
Project  
├── main.py  
├── a.py  
├── b.py  
├── pkg1  
├ ├── c1.py
├ ├── util
├ ├  ├── util1.py
├── pkg2
├ ├── d.py
├ ├── pkg11.py
├ ├── pkg22
├ ├  ├── e.py
├ ├── pkg23
├ ├  ├── f.py


### 2.1 from a import xxx
例如在 main.py 中引用 a.py 中的变量、类，使用 from a import xxx 即可，xxx 可以是变量、类名、函数名。  
注意：from a import xxx 会先执行完 a.py 中的每一句代码，因此第一行输出了 “this is file a.py, and a: I'm a”，不需要在 a.py 被引用时被执行的代码可以放在 ``` if __name__=='__main__' ``` 的判断语句后面。

```
# main.py

from a import a, A, AA, a_function

print(a)
print(A)
aa = AA()
print(aa)
a_function()
```
```
# a.py

a = "I'm a"
A = "I'm A"

class AA:
    def __init__(self):
        self.aa = "I'm class AA"
    
    def __str__(self):
        return self.aa

def a_function():
    print("this is a function in a.py")

print("this is file a.py, and a:",a)
if __name__=='__main__':
    print(print("this is file a.py, and A:",A))
    
```
```
# 输出：
this is file a.py, and a: I'm a
I'm a
I'm A
I'm class AA
this is a function in a.py
```

### 2.2 除了 from 的操作，也可以直接去引用模块（对应一个py文件）：import xxx
```
# b.py
name = "I'm b.py"
```
```
#main.py
import b
print(b.name)
```
```
#输出：
I'm b.py
```

### 2.3 同样可以去引用一个包（对应一个文件夹）：import xxx
但是引用包的时候，需要通过一个__init__.py来定义包中有哪些东西，例如在与main.py相同路径下有pkg1文件夹，pkg1中有c1.py  
|--Project  
|   |- main.py  
|   |- pkg1  
|   |   |-c1.py
```
# c1.py
name = "I'm c1.py in pkg1"
```
在不加__init__.py时，可以这样去引用：
```
import pkg1.c1
print(pkg1.c1.name)

# 输出：
I'm c1.py in pkg1
```
```
import pkg1.c1 as c1
print(c1.name)

# 输出
I'm c1.py in pkg1
```
下面这种方式则会直接报错：
```
import pkg1
print(pkg1.c1.name)

# 输出：
AttributeError: module 'pkg1' has no attribute 'c1'
```
在pkg1目录下添加__init__.py 即可，python会把当前文件中各个模块均视为包 pkg1 的模块。

python 还可以识别出__init__.py 中的内容作为包的内容。你可以直接在其中定义一些变量、类等，或者也可以用相对引用的方式，直接引用目录下其他py文件中的内容，使之成为pkg1的内容
```
# __init__.py in pkg1
pkg1_name = "My name is pkg1"
from .c1 import name as c1_name

# main.py
import pkg1
print(pkg1.pkg1_name)
print(pkg1.c1_name)
```

### 2.4 多级引用，用 '.' 连接
```
import pkg1.util.util1 as util1
print(util1.uname)

# 输出：
this is util1.py in pkg1.util, who are u?
```

## 3. 非同级目录下的引用
例如，想在 pkg2 的 d.py 中去引用 pkg1 的内容；通常没办法用相对的方式进行

### 3.1 添加PATH的方式实现，将想要引用的包所在的目录添加到PATH
在pkg2文件夹中想要引用pkg1中的内容，直接使用 ```import pkg1``` 或者 ```from pkg1 import xxx``` 会报错：找不到 pkg1 模块。此处我们将工作目录添加到PATH：
```
# d.py
import sys
import os
sys.path.append(os.path.abspath('.'))

from pkg1 import c1
print(c1.name)

# 输出
I'm c1.py in pkg1
```
但是如果你的 pkg2 文件夹中恰好有一个名为 pkg1.py 的文件，则 ```from pkg1 import c1``` 会优先到 pkg1.py 中去找：
```
# pkg1.py in pkg2
class C:
    def __init__(self):
        self.name="im pkg1.py in pkg2"
c1=C()

# d.py 输出：
im pkg1.py in pkg2
```
所以应当避免上述情况的发生。

### 3.2 当然你也可以手动将你的包所在的路径添加到系统PATH中，Linux在控制台运行：
```export PYTHONPATH=$PYTHONPATH:/your/pkg/root/path```  
注意需要是你的包所在的路径，而不是包的路径。例如/x/xx/xxx/test1，而非/x/xx/xxx/test1/pkg1。一旦该路径生效，你还可以在其他的 python project 中去引用你的包

### 3.3 此外，可以了解一下如何用 setup 打包你的项目
本人也在学习当中，不献丑了。

### 3.4 常见报错
ImportError: attempted relative import with no known parent package  
ValueError: attempted relative import beyond top-level packag  
可以说这个报错真的令人头皮发麻两眼发黑四肢抓狂，例如直接在 d.py 中用这种方式引用：
```
from ..pkg1 import c1

# 报错：ImportError: attempted relative import with no known parent package
```
翻译过来就是：引用错误，不知道父包的情形下尝试相对引用；

为啥不知道父包：例如当你运行 d.py 的时候，python并不会解析整个项目，而只知道 d.py 所在路径下的文件、包等等。如果在 pkg2 下有两个包：pkg22 和 pkg23，他们父包为 pkg2，这个时候运行 pkg2 同级及以上目录中的文件时，可以识别到 pkg22 和 pkg23 中的相对引用。
例如：
```
# e.py
from ..pkg11 import c1
print(c1.name)
print('eeeeee')
```
```
# f.py
from ..pkg22 import e
print('ffffff')
```
```
# main.py (跟pkg2在同一个路径)
import pkg2.pkg23.f

# 输出：
im pkg11.py in pkg2
eeeeee
ffffff
```

另外，pkg1 和 pkg2 均处于项目的根目录下，他们无法相对引用。除非需要运行的py文件是与根目录同级的。如果你一定要在pkg2的文件中引用pkg1的话，请使用绝对引用。

### 3.5 总结，运行py绝对引用，不在同一个目录就去添加path（3.1）；被引用的文件才用相对目录
作者：Leng Zhuo，冷焯
日期：2023.01.16
email：len@stu.pku.edu.cn
