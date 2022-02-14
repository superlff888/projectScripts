# **一、配置文件**

- **配置文件示例**

  ```ini
  [mysql]
  default-character-set=utf-8
  
  [mysqld]
  port = 3306
  basedir = ***
  datadir = ***
  max_connections = 200
  character-set-server = utf-8
  default-storage-engine=INNODB
  explicit_defaults_for_timestamp=true
  ```

- **场景举例**

  - 多个地方需要同一个参数,此时最好配置,这样改动一处就可以了
  - 经常发生变化的变量也可以做配置文件.--->要区别于参数化

- **常见的配置文件格式**

  - .ini      .conf    .cfg

- **配置文件对象**(忽略*)

  - **section**    例如:  

    ```ini
    [mysql]
    *** = **
    ```

    

  - **option**     

    ```ini
    [***]
    port = 3306
    basedir = 
    datadir = 
    max_connections = 200
    character-set-server = utf-8
    default-storage-engine=INNODB
    explicit_defaults_for_timestamp=true
    ```

# 二、configparser模块

- **打开配置文件**

  - ```
    conf = configparser.ConfigParser() # 实例化一个对象
    conf.read('my.conf', encoding='utf-8') # 打开my.conf配置文件
    ```

- **常用方法**

  - 配置文件

    ```ini
    [name] # section
    leader = 张三
    student = 李四
    
    [age]
    # 以下为 option
    leader = 28
    student = 18
    ```

  - ​	解析配置文件

    ```python
    # @Author    : ╰☆H.俠ゞ
    # -*-coding=utf-8-*-
    # =============================================================
    
    import configparser
    conf = configparser.ConfigParser()
    # 打开my.conf配置文件
    conf.read('my.conf', encoding='utf-8')
    print(conf.sections())
    print(conf.options('name'))
    print(conf.get('name', 'leader'))  # 打印出读取出的leader的value
    print(conf.items('name'))
    print(dict(conf.items('name')))  # 当可以转化成字典时，用dict函数可以转化为字典格式
    
    ```
  - 运行结果
    ```python
    "D:\Program Files\pythonProject_CTTQ\venv\Scripts\python.exe" "D:/Program Files/pythonProject_CTTQ/lemonBan/lemonBan/配置文件/myConfigparserDemo.py"
    ['name', 'age']
    ['leader', 'student']
    张三
    [('leader', '张三'), ('student', '李四')]
    {'leader': '张三', 'student': '李四'}
    28
    99.5
    True
    
    Process finished with exit code 0
    ```
- 以下均为采用上述解析方法获得的结果
  
  - sections()      获取所有的section,并以列表的形式返回

    ```ini
    ['name', 'age']
    ```

  - options(section)      获取该section中所有的option

    ```ini
    ['leader', 'student']
    ```

  - get(section, option)      获得section中该option的value值

    ```ini
    张三
    ```

  - items(section)      获取该section中option的所有键值对

    ```ini
    [('leader', '张三'), ('student', '李四')]
    ```

    ```ini
    {'leader': '张三', 'student': '李四'}
    ```

  - getint(section, option)      获得section中该option的int型value值

    ```ini
    28
    ```

  - getfloat(section, option)      获得section中该option的float型value值

    ```ini
    99.5
    ```

  - getboolean(section, option)      获得section中该option的布尔型value值

    ```ini
    True
    ```

# 随笔

### 控制语句

- ```pytho
  for i in range(10):
  	print(i)
  else:
  	pass
  # for循环正常执行完,就会执行else语句;for循环非正常运行阻断,则不会执行else语句,如 break
  ```

  