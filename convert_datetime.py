import sublime
import sublime_plugin
import re
from datetime import datetime

class ConvertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            if re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', region_text):
                ts = str(datetime.strptime(region_text, "%Y-%m-%d %H:%M:%S").timestamp())
            elif re.match(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}', region_text):
                ts = str(datetime.strptime(region_text, "%Y/%m/%d %H:%M:%S").timestamp())
            elif re.match(r'\d{4}-\d{2}-\d{2}', region_text):
                ts = str(datetime.strptime(region_text, "%Y-%m-%d").timestamp())
            elif re.match(r'\d{4}/\d{2}/\d{2}', region_text):
                ts = str(datetime.strptime(region_text, "%Y-%m-%d").timestamp())
            self.view.replace(edit, region, ts)
            # self.view.insert(edit, self.view.sel()[0].begin(), table)
        # self.view.sel().clear()
