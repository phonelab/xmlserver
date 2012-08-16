from fabric.api import run, env, local, cd
import os

SSH_KEY_DIR = os.getenv('HOME') + '/.ssh/'

env.user = 'ec2-user'
env.key_filename = [os.path.join(SSH_KEY_DIR, "phonelab.pem")]
env.hosts = ['backend.phone-lab.org'] #107.20.190.88

def move():
  stop()
  run('rm -rf xmlserver')
  run("git clone git://github.com/phonelab/xmlserver.git")

def start():
  run('/etc/init.d/xmlserver start')

def stop():
  run('/etc/init.d/xmlserver stop')

def restart():
  start()
  stop()

def migrate():
  with cd('/home/ec2-user/xmlserver'):
    run('python manage.py syncdb')

def deploy():
  move()
#  migrate()
  restart()
