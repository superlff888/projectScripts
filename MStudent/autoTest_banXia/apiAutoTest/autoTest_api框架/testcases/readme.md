# 一、pytest在命令行运行用例，当前目录就是命令行目录
    pytest.ini文件中配置的”--alluredir ./reports/shop --clean-alluredir“
    代表当前所在目录下新建“/reports/shop”，用例执行的中间结果
# 三、 "run.py“文件中采用IDE执行用例，此时当前目录指的是"run.py“所在的目录