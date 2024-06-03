#!/usr/bin/python3
"""generate a .tgz archive with this script"""

from fabric.api import local
import time
import os


def do_pack():
    time_string = time.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_string)
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print(e)
        return None
