print("")
print("")
print("")
print("K   K   AAAAA    III   TTTTT     OOO ")
print("K  K    A   A     I      T      O   O ")
print("K K     AAAAA     I      T      O   O ")
print("K  K    A   A     I      T      O   O ")
print("K   K   A   A    III     T       OOO ")
print("")
print("========================================")


pilihan = ''
kesempatan_login=0;
kesempatan_register=0;

while pilihan != '3':
    
    pilihan = input('''
                
    lOGIN & REGISTER SYSTEM VIA CMD BY KAITODECODE
    
    option:
    1 => Register
    2 => Login
    3 => Exit
    
    choose your option: ''')
    
    if pilihan == '1':
        print("Anda memilih register")
        
    elif pilihan == '2':
        print("Anda memilih login")
        
    elif pilihan == '3':
        print("Anda memilih exit")
        
    else:
        print("Pilihan tidak valid, silakan coba lagi")
        pilihan = input('''
                
    lOGIN & REGISTER SYSTEM VIA CMD BY KAITODECODE
    
    option:
    1 => Register
    2 => Login
    3 => Exit
    
    choose your option: ''')


