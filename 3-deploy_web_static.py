#!/usr/bin/python3
""" Fabric script to create and distribute an archive to web servers """
from fabric.api import run, put
from fabric.api import env
from datetime import datetime
from os.path import isfile
from fabric.api import local
from fabric.operations import sudo
env.hosts = ['100.25.33.31', '100.26.10.209']
env.user = 'ubuntu'


def do_pack():
    """
    make a .tgz archive of the web_static folder
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_{}.tgz'.format(timestamp)
    try:
        local('mkdir -p versions')
        local('tar -cvzf {} web_static/'.format(archive_path))
        return archive_path
    except:
        return None


def do_deploy(archive_path):
    if not isfile(archive_path):
        return False
    try:
        archive_name = archive_path.split('/')[-1]
        archive_folder = "/data/web_static/releases/" + archive_name.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, archive_folder))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}/'.format(archive_folder, archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
