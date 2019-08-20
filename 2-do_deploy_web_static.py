#!/usr/bin/python3
"deploy in servers"
from fabric.api import*
from os import path


env.hosts = ['35.243.150.102', '35.237.124.126']


def do_pack():
    """ doc pack task"""
    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M")
    name = "versions/web_static_{}.tgz web_static".format(current_time)
    local('mkdir -p versions')
    result = local("tar -cvzf {}".format(name))
    if result.return_code == 0:
        return name
    else:
        return None


def do_deploy(archive_path):
    """ deploy task """
    version = archive_path[9:-4]
    remote_path = "/data/web_static/releases/{}".format(version)
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            run("mkdir -p {}".format(remote_path))
            with cd('/tmp'):
                run("tar -xzf {} --directory {}".format(archive_path[9:],
                                                         remote_path))
                run("rm *.tgz")
            run("ln -nsf {} /data/web_static/current".format(remote_path))
            run("mv {}/web_static/* {}".format(remote_path, remote_path))
            run("rm -d {}/web_static/".format(remote_path))
            return True
        except:
            return False
    else:
        return False
