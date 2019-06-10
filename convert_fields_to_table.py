import sublime
import sublime_plugin
import re

class ConvertFieldsToTableCommand(sublime_plugin.TextCommand):
	def run(self, edit, seperator):
		selection = self.view.sel()
		for region in selection:
			region_text = self.view.substr(region)
			lines = region_text.split("\n")
			table = '<table>'
			for line in lines:
				if not line.strip():
					continue
				fields = line.strip(seperator).split(seperator)
				isth = False
				if fields[0].startswith("*"):
					isth = True
					fields[0] = fields[0].lstrip("*")
				tr = self.gen_tr(fields, isth)
				if isth:
					tr = "\n\t<caption></caption>\n\t<thead>%s\n\t</thead>\n\t<tbody>" % (tr)
				table += tr
			table += '\n\t</tbody>\n</table>\n'
			self.view.replace(edit, region, table)
			# self.view.insert(edit, self.view.sel()[0].begin(), table)
		# self.view.sel().clear()

	def gen_tr(self, fields, isth):
		line = '\n\t\t<tr>'
		for field in fields:
			field = field.strip()
			field = "" if field == "__" else field
			# 发现可能的合并指令
			rs = 0
			cs = 0
			if field[0] == "/":
				rm = re.match(r'/(\d+)(\\(\d+))?\.', field)
				if rm:
					rs = int(rm.group(1))
					field = field.replace("/%s" % (rs), "", 1)
				if rm.group(2):
					cs = int(rm.group(3))
					field = field.replace("\\%s" % (cs), "", 1)
				field = field.replace(".", "", 1)
			elif field[0] == "\\":
				cm = re.match(r'\\(\d+)(/(\d+))?\.', field)
				if cm:
					cs = int(cm.group(1))
					field = field.replace("\\%s" % (cs), "", 1)
				if cm.group(2):
					rs = int(cm.group(3))
					field = field.replace("/%s" % (rs), "", 1)
				field = field.replace(".", "", 1)
			# rowspan colspan
			rowspan = ' rowspan="%s"' % (rs) if rs > 0 else ''
			colspan = ' colspan="%s"' % (cs) if cs > 0 else ''
			# 积累格子
			if isth:
				line += '\n\t\t\t<th%s%s>%s</th>' % (rowspan, colspan, field.strip())  # strip()消除replace可能遺漏的空格
			else:
				line += '\n\t\t\t<td%s%s>%s</td>' % (rowspan, colspan, field.strip())  # strip()消除replace可能遺漏的空格
		line += '\n\t\t</tr>'
		return line

	def gen_tr_old(self, fields, isth):
		line = '\n\t\t<tr>'
		for field in fields:
			field = field.strip()
			field = "" if field == "__" else field
			# 跳过被合并的单元格，针对未textile化之前的表格
			if field == "<->":
				continue
			# 发现可能的合并指令
			rs = 0
			cs = 0
			if field.find("_s>") != -1:
				rm = re.search(r'<(\d+)r_s>', field)
				if rm:
					rs = int(rm.group(1))
				cm = re.search(r'<(\d+)c_s>', field)
				if cm:
					cs = int(cm.group(1))
				field = field.replace("<%sr_s>" % (rs), "").replace("<%sc_s>" % (cs), "")
			# rowspan colspan
			rowspan = ' rowspan="%s"' % (rs) if rs > 0 else ''
			colspan = ' colspan="%s"' % (cs) if cs > 0 else ''
			# 积累格子
			if isth:
				line += '\n\t\t\t<th%s%s>%s</th>' % (rowspan, colspan, field)
			else:
				line += '\n\t\t\t<td%s%s>%s</td>' % (rowspan, colspan, field)
		line += '\n\t\t</tr>'
		return line
