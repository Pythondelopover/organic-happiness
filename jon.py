jon = 3
def jon_hisoblash(natija):
    global jon
    if natija == True:
        return True
    else:
        jon = jon - 1
        if jon == 0:
            return False
        else:
            return True