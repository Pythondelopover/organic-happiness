admin_user = ['admin']
user = {
         'admin': 0,
         'new': 1
}
parol = {
        'admin': 0,
        'new': 1
}
ism = {
        'admin': 0,
        'farhod': 1
}
sanab = 2
def registr(username, pas, name):
    global sanab
    global user
    global ism
    global parol
    global admin_user
    user[username] = sanab
    parol[pas] = sanab
    ism[name] = sanab
    sanab += 1
    #l = [user, parol, name]
    return True

def user_tekshirish(username, pasword, name):
    global admin_user
    global user
    global ism
    global parol
    try:
        if username in admin_user:
            return None
        elif user[username] == parol[pasword] and user[username] == ism[name]:
            return True
        else:
            return False
    except:
        return False
#print(tekshirish('admin','admin','admin'))

def admin_ad(username, pas, name):
    global admin_user
    global parol
    global ism
    global user
    k = None
    try:
        if user[username] == parol[pasword] and user[username] == ism[name]:
            k = True
        else:
            k = False
    except:
        k = False
    if k == True:
        admin_user.append(username)
def adminlar():
    global admin_user
    return sorted(admin_user)