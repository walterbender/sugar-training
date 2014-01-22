# Copyright (C) 2014 Walter Bender <walter@sugarlabs.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""D-bus service providing access to the shell's functionality"""

import dbus
from gi.repository import Gtk

from jarabe.model import shell
from jarabe.model import bundleregistry


_DBUS_SERVICE = 'org.sugarlabs.Shell'
_DBUS_SHELL_IFACE = 'org.sugarlabs.Shell'
_DBUS_PATH = '/org/sugarlabs/Shell'


class ShellService(dbus.service.Object):
    """Provides d-bus service to script the shell's operations
    Fork of sugar/src/jarabe/view/service.py
    """

    def __init__(self):
        bus = dbus.SessionBus()
        bus_name = dbus.service.BusName(_DBUS_SERVICE, bus=bus)
        dbus.service.Object.__init__(self, bus_name, _DBUS_PATH)

        self._shell_model = shell.get_model()

    @dbus.service.method(_DBUS_SHELL_IFACE,
                         in_signature='i', out_signature='')
    def SetZoomLevel(self, zoom_level):
        """Set Zoom Level of Sugar Shell
        """
        if zoom_level in [shell.ShellModel.ZOOM_HOME,
                          shell.ShellModel.ZOOM_MESH,
                          shell.ShellModel.ZOOM_ACTIVITY]:
            self._shell_model.set_zoom_level(zoom_level)
        return

    @dbus.service.method(_DBUS_SHELL_IFACE,
                         in_signature='', out_signature='i')
    def GetZoomLevel(self):
        """Set Zoom Level of Sugar Shell
        """
        return self._shell_model.get_zoom_level()
