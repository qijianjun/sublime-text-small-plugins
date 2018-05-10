import sublime
import sublime_plugin

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
			if isth:
				line += '\n\t\t\t<th>%s</th>' % (field.strip())
			else:
				line += '\n\t\t\t<td>%s</td>' % (field.strip())
		line += '\n\t\t</tr>'
		return line
