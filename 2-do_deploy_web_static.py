#!/usr/bin/python3
"deploy in servers"
from fabric.api import*
from os import path


env.hosts = ['35.243.150.102', '35.237.124.126']


def do_deploy(archive_path):
    version = archive_path[9:-4]
    remote_path = "/data/web_static/releases/{}".format(version)
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            run("mkdir -p {}".format(remote_path))
            with cd('/tmp'):
                run("tar -xvzf {} --directory {}".format(archive_path[9:],
                                                         remote_path))
                run("rm *.tgz")
            run("ln -nsf /data/web_static/releases/{} /data/web_static/current"
                .format(version))
            run("mv {}/web_static/* {}".format(remote_path, remote_path))
            run("rm -d {}/web_static/".format(remote_path))
            return True
        except:
            return False
    else:
        return False
