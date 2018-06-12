import sublime
import sublime_plugin


class ReplaceDuplinesToDashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view

        result = []
        allcontent = sublime.Region(0, v.size())
        lines = v.substr(allcontent).split('\n')

        lastline = ""
        for line in lines:
            if line == lastline:
                result.append("-")
            else:
                result.append(line)
            lastline = line

        output = '\n'.join(result)

        self.view.replace(edit, allcontent, output)
