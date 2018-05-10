import sublime
import sublime_plugin

class RemoveHtmlAttrsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        rs = self.view.find_all(r'\s*(id|class|href|title|target)\s*=\s*"[^"]*"\s*')
        edit = self.view.begin_edit()
        for r in rs:
            self.view.replace(edit, r, '')
        self.view.end_edit(edit)
