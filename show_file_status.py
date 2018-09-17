import os.path
import sublime
import sublime_plugin

class ShowFileStatus(sublime_plugin.EventListener):

    def update_file_status(self, view):

        if not view.file_name():
            status = "NONE"
        elif not os.path.exists(view.file_name()):
            status = "DEL"
        elif view.is_dirty():
            status = "UNSAVED"
        else:
            status = "SAVED"

        window = sublime.active_window()
        status = str(len(window.views())) + " ~ " + status

        view.set_status(self.KEY_SIZE, "[%s]" % status)

    on_post_save_async = update_file_status
    on_modified_async = update_file_status
    on_activated_async = update_file_status
