import sublime
import sublime_plugin

class PasteMultilinesAsOneCommand(sublime_plugin.TextCommand):
	def run(self, edit, slash_position):
		content = sublime.get_clipboard()
		lines = content.split("\n")
		output = ''
		for line in lines:
			if slash_position == "begin":
				output += ('/' + line)
			elif slash_position == "end":
				output += (line + '/')
			elif slash_position == "no":
				output += line
		self.view.insert(edit, self.view.sel()[0].begin(), output)
