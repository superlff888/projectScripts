# xpath
- ���ñ��ʽ����
    - /a ������� ѡȡ������Ԫ��a(��ָ��һ��Ԫ��)��```ע�⣺/ ����Ӹ��ڵ�ѡȡ```
    - //a ��������Ԫ�أ�����Ԫ�� + ����Ԫ��
        - ��ƥ��ѡ��ĵ�ǰ�ڵ�ѡ���ĵ��еĽڵ㣬�Ӳ�����λ��
        - b//a ѡȡbԪ���µ�����aԪ�أ�����Ԫ�ؼ�����Ԫ��
    - nodename ѡȡ�˽ڵ�������ӽڵ�
    - .  ѡȡ��ǰ�ڵ�
    - .. ѡȡ��ǰ�ڵ�ĸ��ڵ�
    - @ ѡȡ����
    ![img_3.png](img_3.png)
- ##xpath��λ����
  - ʵ��  
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <bookstore>
     
    <book>
      <title lang="eng">Harry Potter</title>
      <price>29.99</price>
    </book>
     
    <book>
      <title lang="eng">Learning XML</title>
      <price>39.95</price>
    </book>
     
    </bookstore> 
    ```
    
  
- ����xml
    - /bookstore/book[1] ```ѡȡbookstore��Ԫ���е�һ��bookԪ��```
      - / ������ǰ���Ԫ�أ���Ԫ��
    - /bookstore/book[last()] ```ѡȡbookstore��Ԫ�������һ��bookԪ��```
    - /bookstore/book[last()-1] ```ѡȡbookstore��Ԫ���е����ڶ���bookԪ��```
    - ���·����λ  //��ǩ��[@����=������ֵ��]
        - //div[@id='in1'] ```ѡȡ����id����ֵΪ'in1'��divԪ��'```
        - //*[@id='in1'] ```ѡȡ����id����ֵΪ'in1'��Ԫ��'```
    - /bookstore/book[price>35] ```ѡȡbookstore����book��Ԫ�أ������е�priceԪ�ص�ֵ�������35```
    ![img.png](img.png)
      
    ![img_5.png](img_5.png)
      
- �����console���Ԫ��Ψһ��
  ![img_1.png](img_1.png)
    - 1��clear() ���console����̨
    - 2��$x("Xpath���ʽ") ```$x ������xpath���ж�λ```
    
        - id �� name һ�㶼��Ψһ�ģ�Լ���׳ɣ�,���Կ��Բ���//*[@id='value']��λ
            - //*[@id="kw"]
            - //*[@name="wd"]
#css selector

- ���ʽ
    - .intro ```ѡ��class='intro'������Ԫ��```
    
    - *#firstname* ```ѡ��id='firstname'������Ԫ��```
    - * ```ѡ������Ԫ��```
    - div,p ```ѡ������<div>��ǩԪ�غ�����<p>��ǩԪ��```
    - div p ```ѡ��<div>Ԫ���ڲ�������<p>Ԫ��```
    - div>p ```ѡ��<div>Ԫ���ڲ���<p>��Ԫ��```
    - div+p ```ѡ�������<div>Ԫ�غ��������<p>�ֵ�Ԫ��``` 
    


![img_13.png](img_13.png)      
![img_8.png](img_8.png)

#ʵ��
- ###�������������������޾��������¼���ǩ�����¼���ǩ����
![img_7.png](img_7.png)
![img_9.png](img_9.png)
![img_11.png](img_11.png)
![img_14.png](img_14.png)
![img_15.png](img_15.png)