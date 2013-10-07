import sublime, sublime_plugin

#recommended keymap:
#    { "keys": ["alt+c"], "command": "show_char_code", "args": {}},
class show_char_codeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		a = self.view.sel()[0].begin()
		b = a + 1
	    #Get current char under cursor and show its numeric values in the statusbar 
		s = self.view.substr( sublime.Region(a,b) )
		self.view.set_status('show_char_code', 'Char [%s] Dec [%s] Hex [%s]' % (s,ord(s),hex(ord(s))) )  
