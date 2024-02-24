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

nama=''
email=''
password=''

while pilihan != '3':
    
    pilihan = input('''
                
    lOGIN & REGISTER SYSTEM VIA CLI BY KAITODECODE
    
    option:
    1 => Register
    2 => Login
    3 => Exit
    
    choose your option: ''')
    
    if pilihan == '1':
        
        if kesempatan_register == 0:
            kesempatan_register+=1
            print("REGISTER PROGRAM")
            nama = input("Masukan nama anda: ")
            email = input("Masukan email anda: ")
            password = input("Masukan password anda: ")
            print(nama,email,password)
        else:
            print("Anda Sudah Menggunakan Kesempatan Register Anda")
        
    elif pilihan == '2':
        print("LOGIN PROGRAM") 
        email_login = input("Masukan email anda: ")
        password_login = input("Masukan password anda: ")
        if email_login == email and password_login == password:
            print("Login berhasil")
        else:
            print("Email atau password salah")
        
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


