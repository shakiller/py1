[app]
title = ScreenMirrorApp
package.name = screenmirror
package.domain = org.screenmirror
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy,pillow
fullscreen = 1
orientation = landscape
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.allow_backup = False

[buildozer]
log_level = 2
warn_on_root = 1