#!/usr/bin/python3
"""Facilitating the deployment process, this script efficiently
distributes an archive to your designated
web servers via the do_deploy function."""
from fabric.api import run, put
import os.path
from fabric.api import env
env.hosts = ['100.25.33.31', '100.26.10.209']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
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
