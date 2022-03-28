

- adb logcat | grep -i displayed

- adb shell dumpsys activity top
    ![img_1.png](img_1.png)
  
- adb shell dumpsys window | grep mCurrent
    ![img.png](img.png)

- adb shell am start -W -n com.xueqiu.android/com.xueqiu.android.common.search.USearchActivity -S


- # 获取包和启动activity
    - adb shell dumpsys activity top | grep ACTIVITY 
    - adb shell monkey -p "com.tencent.wework" -vvv 1
