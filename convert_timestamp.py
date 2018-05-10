# -*- coding: utf-8 -*-

from datetime import datetime
import re ,time
import sublime_plugin

#  Sublime Text 2 plug-in to insert TimeStamps into your file.
# Type 'now' 然后按 <tab> 转为当前时间 年-月-日 时:分:秒.
# 'tsnow' + <tab> 显示当前时间戳
# 年-月-日-时-分-秒 转为时间戳

class TimestampCommand(sublime_plugin.EventListener):
    """Expand `now`, `tsnow`
    """

    def on_query_completions(self, view, prefix, locations):
        #patten1 匹配10位整数时间戳
        pattern1 = re.compile(r'^\d{10}')
        match1 = pattern1.match(prefix)
        #patten2 匹配13位整数时间戳
        pattern2 = re.compile(r'^\d{13}')
        match2 = pattern2.match(prefix)
        #patten3 匹配10位整数附加小数位的时间戳
        pattern3 = re.compile(r'^\d{10}\.\d{2,3}')
        match3 = pattern3.match(prefix)
        #pattern4 匹配20141220235959这样的时间字符串
        pattern4 = re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2})-(\d{1,2})-(\d{1,2})-(\d{1,2})')
        match4 = pattern4.match(prefix)

        if prefix in ['now']:  # 2013-06-27T23:34:00
            val = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif prefix in ['tsnow','timestamp']:  # 1412092800
            val = str(time.time()).split('.')[0]
        elif match1:
            timeStamp = int(match1.group(0))
            timeArray = time.localtime(timeStamp)
            val = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
        elif match2:
            timeStamp = int(match2.group(0)) / 1000.0
            timeArray = time.localtime(timeStamp)
            val = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
        elif match3:
            timeStamp = float(match3.group(0))
            timeArray = time.localtime(timeStamp)
            val = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
        elif match4:
            timeStr = match4.group(1) + '-' + match4.group(2) + '-' + match4.group(3) +' ' + match4.group(4)+ ':' + match4.group(5)+ ':' + match4.group(6)
            timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")
            val = str(time.mktime(timeArray)).split('.')[0]
        else:
            val = None

        return [(prefix, prefix, val)] if val else []