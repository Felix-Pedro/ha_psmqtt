import os
import pyfiglet as pf
import gettext

localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')

translate = gettext.translation('hass_psmqtt', localedir, fallback=True)
_ = translate.gettext

# Startup Process
psmqtt_path = os.path.join(*__file__.split(os.path.sep)[:-2])

title = pf.figlet_format('HASS psmqtt', font='banner3-D')

print(title)
print()
print(_("Welcome to HASS PSMQTT"))
print()
print(_("This application is designed to help implement a simple way to connect a device that runs python to Home Assistant via MQTT, for more information please read the docs for both hass_psmqtt and psmqtt"))


