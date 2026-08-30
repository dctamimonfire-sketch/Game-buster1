[app]

title = Game Booster
package.name = gamebooster
package.domain = com.tamim

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json
version = 1.0

requirements = python3==3.11.9,kivy==2.3.0,pyjnius==1.6.1

orientation = portrait
fullscreen = 1

android.api = 35
android.minapi = 23
android.ndk = 27c

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
