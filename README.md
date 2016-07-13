# FlaskServiceWin32
Python Flask sample for windows service registration.

## Requirement
  * pywin32 - [Python for Windows Extensions](http://sourceforge.net/projects/pywin32/files/)

## how to setup
  1. install pywin32
  2. edit win32_service.py to modify  `svc_name` and  `svc_display_name`
  3. admin cmd open
  4. service install: `#python win32_service.py install`
  5. check service: `#sc query svc_name`
  6. You can stop: `#sc stop svc_name`
  7. If you want to delete this service: `#sc delete svc_name`
