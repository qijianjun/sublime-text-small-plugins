import sublime
import sublime_plugin
import re

class HtmlTableToTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view

        result = []
        allcontent = sublime.Region(0, v.size())
        content = v.substr(allcontent).strip().replace("|", "^esc^") # 转移文本表格的分隔符
        content = re.sub(r'\s*\n\s*', r' ', content) # 去除换行符
        content = content.replace("<tr", "|<tr")
        content = content.replace("</td>", "</td>|")
        content = content.replace("</th>", "</th>|")
        content = content.replace("</tr>", "|\n</tr>")
        content = re.sub(r'\|\s*\|$', '|', content, 0, re.M) # 去除最后一个td/th和tr的重复分隔符
        content = re.sub(r'<[^>]+>', '', content) # 去除标签
        content = re.sub(r'^\s+', '', content, 0, re.M) # 去除行首的空白
        self.view.replace(edit, allcontent, content)
