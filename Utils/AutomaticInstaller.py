import apt
import os



def checkPrivilageMode():  #Find out the current this program is running as root or not.
    return 'SUDO_UID' in os.environ.keys()

def checkPip():
    cache = apt.cache.Cache()
    cache.update()
    pkg = cache["python-pip"]
    if pkg.is_installed:
        print " Pip is already installed"
        return False
    else:
        pkg.mark_install()
        return cache

def installPip(cache):
    try:
        cache.commit()
    except Exception as e:
        print e


if(checkPrivilageMode()):
    cache=checkPip()
    if(cache):#become true if the package is not installed
        installPip(cache)
else:
    print "You have to run this program as root:- sudo python AutomaticInstaller.py"

