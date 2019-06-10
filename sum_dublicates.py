import itertools

import sublime
import sublime_plugin


class SumDuplicatesCommand(sublime_plugin.TextCommand):
    def run(self, edit, isint=False):
        v = self.view

        allcontent = sublime.Region(0, v.size())
        lines = sorted(v.substr(allcontent).split('\n'))

        o = ""
        s = 0
        d = {}
        for line in lines:
            k, v = line.split("\t")
            if o != "" and o != k:
                d[o] = s
                s = 0
            o = k
            s += float(v)
        d[o] = s

        # dict输出，无排序
        # output = "\n".join(k + "\t" + str(v) for k,v in d.items())

        # 转tuple，有排序
        d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        if isint:
            output = '\n'.join([str(t[0]) + '\t' + str(int(t[1])) for t in d])
        else:
            output = '\n'.join([str(t[0]) + '\t' + str(t[1]) for t in d])

        self.view.replace(edit, allcontent, output)
