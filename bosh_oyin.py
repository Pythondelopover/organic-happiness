from registratsiya import admin_ad
from top_reyting import reyting
from profil import profil
from registratsiya import user_tekshirish
from jon import jon_hisoblash
from tekshirish import tekshirish
from play import play
from level import level
from registratsiya import registr

cd = 'yoq'
max_reyting = 0
hd = 0
kn = 1

while True:
     if kn ==1:
         comand_go = input('Registratsiya kerakmi? ha/yoq: ')
         kn += 1
         if comand_go == 'ha':
            print('Registratsiya qilish')
            user_user = input('Username: ')
            user_pasword = input('Pasword: ')
            user_name = input('Name: ')
            registr(user_user, user_pasword, user_name)
            print('Sucsesful')
     if cd == 'ha':
        break
     username = input("Username: ")
     pasword = input('Pasword: ')
     name = input('Name: ')
     if user_tekshirish(username, pasword, name) == True:
         print('Sucsecful')
         print(f'Xush, kelibsiz {name}')
        
         while True:
             comand_user = input('profil/reyting/oyin/break:\n')
             if comand_user == 'profil':
                 kn = profil(username, max_reyting)
                 print(kn)
                 continue
             elif comand_user == 'reyting':
                 print(reyting(max_reyting, username))
              #  print(kn)
             elif comand_user == 'oyin':
                 oyin_boshlash = input('Oyinni boshlaysizmi? ha\yoq: ')
                 if oyin_boshlash == 'ha':
                     s = 1
                     a=[]
                     while True:
                         if s == 1:
                             k = level(True)
                             s+=1
                         else:
                             k = level(a[-1])
                         s=play(k)
                 
                         natija = tekshirish(*s)
                         if natija == True:
                             print("Togri")
                             print(" LEVEL UP")
                 #   print(k)
                  #  k = level(True)
                         else:
                  #  k = level(False)
                             print("Xato")
                
                         result = jon_hisoblash(natija)
                         a.append(natija)
                         if result == False:
                             if max_reyting < k:
                                 max_reyting = k
                             print(f'Siz oyinda maglub boldingiz. Siz {k}-levelgacha chiqdingiz')
                             k = 0
                             yana_oyin = 'yoq'
                             if yana_oyin == 'ha':
                                 s = 1
                                 continue
                             else:
                                 cd = 'ha'
                                 if cd == 'ha':
                                     break   
                 else:
                     javob = input('Chiqmoqchimisiz? ha/yoq: ')
                     if javob == 'ha':
                         hd = 1
                         break
                     else:
                         continue
             elif comand_user =='break':
                 print("Sucsecful")
                 break
             else:
                 print('Xato, comanda terdingiz!!!')
                 print('Qayta, urining')
                 continue
     elif tekshirish(username, pasword, name) == None:
         print("Assalomu, alaykum")
         print('Admin dasturga xush kelibsiz')
         while True:
             comand = input('admin_add/registr/braek:\n')
             if comand == 'registr':
            #s = open(registratsiya)
                 print('Foydalanuvchi qoshish')
                 user = input('User_name: ')
                 user_pas = input('Pasword: ')
                 user_name = input('Name: ')
                 s = registr(user, user_pas, user_name)
                 if s == True:
                     print('Sucsesful')
                    
             elif  comand == 'admin_add':
                
                 print('Admin qoshish')
                 user = input('User_name: ')
                 user_pas = input('Pasword: ')
                 user_name = input('Name: ')
                 s = admin_ad(user, user_pas, user_name)
                 if s == True:
                     print('Sucsesful')
                 else:
                     print('Error')
                     comand = 'admin_add'
                     continue
             elif comand == 'break':
                 break
             else:
                 print('Xato comanda terdingiz.')
                 print('Qayta urining!')
                 continue
     else:
           if hd != 1:
               print('<<Username>> yoki <<pasword>> yoki <<name>>ni xato terdingiz')
               print('Qayta urinib koring.')
               continue
           else:
               break
print('Etiboringiz, uchun raxmat')