sugarservices
=============

Webservice for allowing Sugar activities talk to sugar shell, network manager, etc.

Load this webservice into extensions/webservices

* SetZoomLevel : Set zoom level of Sugar Shell, e.g., shell.ShellModel.ZOOM_HOME
* GetZoomLevel : Get zoom level of Sugar Shell
* IsJournal : Is the current activity the Journal
* GetActivityName : get the bundle_id of the current activity
* OpenJournal : Open the Sugar Journal
* FindChild : Find a child node in the UI Tree
* NMStatus: Get wiressless device status from Network Manager, e.g., 'network-adhoc-6-connected'
