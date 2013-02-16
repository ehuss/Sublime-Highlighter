import sublime, sublime_plugin

class HighlighterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        rs = [x for x in self.view.sel()]
        existing = self.view.get_regions('eric_highlighter')
        rs.extend(existing)
        self.view.add_regions('eric_highlighter', rs, 'string')

class UnhighlighterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.erase_regions('eric_highlighter')
