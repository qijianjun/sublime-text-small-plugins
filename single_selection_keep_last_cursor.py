import sublime, sublime_plugin

# code from:
# https://superuser.com/questions/1050447/sublime-text-escape-multiple-selections-to-last-selection-region-instead-of-fir
# https://stackoverflow.com/questions/37904510/sublime-text-pressing-esc-from-multiple-selections-put-cursor-at-last-select

class SingleSelectionLastCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        last = self.view.sel()[-1]
        self.view.sel().clear()
        self.view.sel().add(last)
        self.view.show(last)