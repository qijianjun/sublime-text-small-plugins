import sublime
import sublime_plugin
import re

class HtmlTableToTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        allcontent = sublime.Region(0, v.size())
        content = v.substr(allcontent)
        print(len(content))
        s = re.findall(r'(<table.*?</table>)', content, re.S)
        print(len(s), len(s[0]))
        content = re.sub(r'(<table.*?</table>)', deal_table, content, 0, re.S)
        print(len(content))
        self.view.replace(edit, allcontent, content)

def deal_table(m):
    content = m.group(1)
    content = content.strip().replace("|", "^esc^") # 转移文本表格的分隔符
    content = re.sub(r'\s*\n\s*', r' ', content) # 去除换行符
    if content.find(" rowspan=") != -1 or content.find(" colspan=") != -1:
        content = re.sub(r'<(td|th)>[\s　]*</\1>', r'<\1>__</\1>', content)
    if content.find(" colspan=") != -1:
        content = re.sub(r'( colspan=[\'"]?)(\d+)([^>]+)>([^<]+)(</t[dh]>)', r'\1\2\3>\\\2. \4\5', content)
    if content.find(" rowspan=") != -1:
        content = re.sub(r'( rowspan=[\'"]?)(\d+)([^>]+)>([^<]+)(</t[dh]>)', r'\1\2\3>/\2. \4\5', content)
    content = re.sub(r'>/(\d+)\. \\(\d+)\. ', r'>/\1\\\2. ', content)
    content = content.replace("<tr", "|<tr")
    content = content.replace("</td>", "</td>|")
    content = content.replace("</th>", "</th>|")
    content = content.replace("</tr>", "|\n</tr>")
    content = re.sub(r'\|\s*\|$', '|', content, 0, re.M) # 去除最后一个td/th和tr的重复分隔符
    content = content.replace("<td><p>", "").replace("<p>", u"↓").replace("<br>", u"↓").replace("<br />", u"↓")  # 保持换行信息
    content = re.sub(r'<strong>(.*?)</strong>', r'**\1**', content)
    content = re.sub(r'<b>(.*?)</b>', r'**\1**', content)
    content = re.sub(r'<[^>]+>', '', content) # 去除标签
    content = re.sub(r' *\| *', '|', content, 0) # 去除豎線分隔符周圍的空格
    return "\n[mytable]\n%s\n[/mytable]\n" % (content.strip())
