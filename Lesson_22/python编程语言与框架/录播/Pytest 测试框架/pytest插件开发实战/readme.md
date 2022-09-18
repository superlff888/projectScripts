# pytest测试原理

## 1、conftest、fixture
- ### 【conftest.py】 是pytest特有的本地测试配置文件，作用在他的目录及子目录
    - #### 可以配置项目级的fixture函数，
    - #### 可以用来导入外部插件
    - #### 可以指定钩子函数
    
- ###【fixture】 通过装饰器@pytest.fixture来告诉pytest某个特定的函数是一个fixture，然后用例可以直接把fixture装饰的函数当作参数来使用

- ### 


