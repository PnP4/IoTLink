import apt



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



cache=checkPip()
if(cache):#become true if the package is not installed
    installPip(cache)
