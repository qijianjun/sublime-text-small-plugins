import sublime
import sublime_plugin
import re
import time

class ConvertTimestampToDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            match = re.compile(r'^(\d{10})\.?(\d{2,3})?').match(region_text)  # 匹配10位整数时间戳/匹配13位整数时间戳 / 匹配10位整数附加小数位的时间戳
            if match:
                timeStamp = int(match.group(1))
                timeArray = time.localtime(timeStamp)
                dt = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
            else:
                dt = region_text
            self.view.replace(edit, region, dt)
            # self.view.insert(edit, self.view.sel()[0].begin(), table)
        # self.view.sel().clear()
