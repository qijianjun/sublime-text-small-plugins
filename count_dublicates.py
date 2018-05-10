import itertools

import sublime
import sublime_plugin


class CountDuplicatesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        
        result = []
        allcontent = sublime.Region(0, v.size())
        lines = sorted(v.substr(allcontent).split('\n'))

        for key, rows in itertools.groupby(lines):
            result.append((sum(1 for r in rows), key))

        result.sort(key=lambda tup: tup[0], reverse=True)
        output = '\n'.join([str(r[0]) + ' ' + r[1] for r in result])

        self.view.replace(edit, allcontent, output)
