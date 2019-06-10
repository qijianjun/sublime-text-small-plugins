import re
import time
import sublime
import sublime_plugin

class CancelCalculateNumsCommand(sublime_plugin.EventListener):
    def on_selection_modified_async(self, view):
        calnums = view.get_status("calnums")
        if calnums:
            view.erase_status("calnums")

class CalculateNumsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        allnums = []
        sel_cnt = len(selection)
        for region in selection:
            region_text = self.view.substr(region)
            nums = re.findall(r'(\d+(\.\d+)?)', region_text)
            allnums += [float(x[0]) for x in nums]
        nums_cnt = len(allnums)
        allsum = sum(allnums)
        avg = round(allsum/nums_cnt, 2)
        self.view.set_status("calnums", "[%s/%s=%s, max %s, min %s]" % (allsum, nums_cnt, avg, max(allnums), min(allnums)))
