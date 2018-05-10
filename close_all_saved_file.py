import sublime
import sublime_plugin

# https://gist.github.com/unpoetic-circle/f6eb5755b55ed5f4fbe4b43b1805c0ac
class CloseAllSavedFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        activeWindow = sublime.active_window()
        views = sublime.Window.views(activeWindow)
        for view in views:
            if view.is_dirty() == False:
                if view.file_name():
                    print("Closing " + view.file_name())
                view.close()
