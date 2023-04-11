import getpass

# Data user yang terdaftar
users = [
    {'username': 'john', 'password': 'password123'},
    {'username': 'jane', 'password': 'password456'}
]

# Fungsi untuk melakukan login
def login():
    # Meminta input dari user
    username = input('Masukkan username: ')
    password = getpass.getpass('Masukkan password: ')
    
    # Mengecek apakah data login valid
    for user in users:
        if user['username'] == username and user['password'] == password:
            print('Login berhasil!')
            return
    print('Username atau password salah!')

# Memulai program
while True:
    print('=== Menu ===')
    print('1. Login')
    print('0. Keluar')
    choice = input('Pilih menu: ')
    
    if choice == '1':
        login()
    elif choice == '0':
        break
    else:
        print('Menu tidak valid, silakan coba lagi.')
