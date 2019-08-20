#!/usr/bin/python3
""" versioning managment """
from fabric.api import*
from datetime import datetime


def do_pack():
    """ do pack task """
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M")
    name = "versions/web_static_{}.tgz web_static".format(current_time)
    local('mkdir -p versions')
    result = local("tar -cvzf {}".format(name))
    if result.return_code == 0:
        return name
    else:
        return None
