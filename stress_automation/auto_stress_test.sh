#！ bin/bash
export jmx_template="PreClassMenu_auto"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
export os_type=`uname`

# 需要在系统变量中定义jmeter根目录的位置，如下
# export jmeter_path="/your jmeter path/"

# 清空nohup.out
cat /dev/null > nohup.out

# 强制杀掉jmeter进程
killJMeter() # bash函数
{
  # shellcheck disable=SC2034
  # shellcheck disable=SC2006
  # shellcheck disable=SC2009
  pid=`ps - ef|grep jmeter |grep java|grep "${jmx_filename}"|awk '{print $2}'`


}


