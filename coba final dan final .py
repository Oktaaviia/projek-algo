import csv 
import pandas as pd
import os

def cetak_selamat_datang():
    os.system("cls")
    print("=" * 115)
    print("BibitSmart".center(115))
    print("Selamat datang di BibitSmart".center(115))
    print("=" * 115)
    print("Jangan lupa untuk registrasi terlebih dahulu jika belum mempunyai akun ya!".center(115))
    print("=== Silahkan pilih menu di bawah ini ya! ===".center(115))

def registrasi():
    print("=" * 54,"Registrasi","=" *54)
    while True:
        nama = str(input('Masukkan nama anda: ')).strip().lower()
        password = input('Masukkan PIN (5 digit): ')
        if len(password) != 5 or not password.isdigit():
            print('PIN harus terdiri dari 5 digit angka.')
            continue 
        if not nama.isalpha():
            print("Nama harus berupa huruf")
            continue
        Hasil = False
        with open('pengguna.csv','r') as r:
         reader = csv.reader(r)
         for x in reader:
           if x[0] == nama :
             Hasil = False
             break
           else:
               Hasil = True
        if Hasil == True:
           with open('pengguna.csv', 'a', newline="") as f:
                csvtambah1 = csv.writer(f)
                csvtambah1.writerow([nama,password,'user'])
                print("\n===========| Berhasil Membuat Akun Baru |==========")
        elif Hasil == False :
           input('\nMaaf Nama sudah digunakan, Enter untuk coba lagi !')
           registrasi()    

user_csv= 'pengguna.csv'
def init_user_file():
    if not os.path.exists(user_csv):
        with open(user_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            # Menambahkan akun admin
            writer.writerow(['petani', '24240'])

def admin_login():
    print("=" * 54, "Login Admin", "=" * 54)
    while True:
        nama = input('Masukkan nama admin: ').strip().lower()  
        password = input('Masukkan PIN: ')

        if nama == 'petani' and password == '24240':
            print("Login admin berhasil!")
            menu_admin()
        else:
            print("Nama atau PIN salah. Silakan coba lagi.")

def user_login():
    global nama_pengguna
    print("=" * 54, "Login User", "=" * 54)
    if not os.path.exists(user_csv):
        print("Anda belum melakukan registrasi. Silakan registrasi terlebih dahulu.")
        return None
    while True:
        nama = input('Masukkan nama anda: ').strip().lower()  
        password = input('Masukkan PIN: ')
        with open(user_csv, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == nama:
                    if row[1] == password:
                        print(f"Login berhasil! Selamat datang, {nama}.")
                        nama_pengguna = nama
                        menu_pengguna() 
                    print("PIN salah. Silakan coba lagi.")
                    return None  
            print(f"Nama '{nama}' tidak ditemukan. Anda belum melakukan registrasi.")
            return None


def main_menu():
    cetak_selamat_datang()
    init_user_file()  # Inisialisasi file pengguna jika belum ada
    while True:
        print("\nMenu:")
        print("[1] Login Admin")
        print("[2] Login Pengguna")
        print("[3] Registrasi Pengguna")
        print("[4] Keluar")
        pilihan = input("Pilih opsi ([1],[2],[3],[4]): ")

        if pilihan == '1':
            admin_login()
        elif pilihan == '2':
            user_login()
        elif pilihan == '3':
            registrasi()
        elif pilihan == '4':
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

jenis_bibit = [
    "Wortel", "Bayam", "Sawi", "Kangkung", "Pare", 
    "Kentang"
]
harga_standar = [20000, 25000, 18000, 22000, 24000, 26000]
harga_premium = [harga + 5000 for harga in harga_standar]
stok_standar = [30, 25, 40, 35, 50, 20]
stok_premium = [20, 15, 35, 30, 40, 25]
garis = "+-----+-------------+--------------+--------------+--------------+--------------+"

bibit_csv = "data_bibit.csv"

def simpan_data_bibit():
    with open(bibit_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["No", "Jenis Bibit", "Harga Standar", "Stok Standar", "Harga Premium", "Stok Premium"])
        for i in range(len(jenis_bibit)):
            writer.writerow([i + 1, jenis_bibit[i], harga_standar[i], stok_standar[i], harga_premium[i], stok_premium[i]])

def tampilkan_tabel():
    print(garis)
    print("| No  | Jenis Bibit | Harga Standar| Stok Standar | Harga Premium| Stok Premium |")
    print(garis)
    for i in range(len(jenis_bibit)):
        print("| {:<3} | {:<11} | {:<12} | {:<12} | {:<12} | {:<12} |".format(
            i + 1, jenis_bibit[i], harga_standar[i], stok_standar[i], harga_premium[i], stok_premium[i]))
    print(garis)

nama_pengguna = None
laporan_pembelian_pengguna=[]
ulasan_list=[]
nama_pembelian_csv = 'riwayat_pembelian.csv'

def menu_pengguna():
    os.system("cls")
    print("=" * 50,"Menu Pengguna","=" *50)
    print("1. Lihat Daftar Harga Bibit")
    print("2. Membeli")
    print("3. Riwayat Pembelian")
    print("4. Deskripsi Perawatan Tanaman")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == '1':
        lihat_daftar_harga()
    elif pilihan == '2':
        membeli()
    elif pilihan == '3':
        lihat_riwayat_pembelian()
    elif pilihan == '4':
        tampilkan_deskripsi_perawatan()
    elif pilihan == '5':
        print("Terima kasih telah menggunakan layanan kami!")
        main_menu()
    else:
        print("Pilihan tidak valid. Silakan coba lagi!")
        menu_pengguna ()

def lihat_riwayat_pembelian():
    os.system("cls")
    print("-" * 50, "Riwayat Pembelian", "-" * 50)
    if not os.path.exists(nama_pembelian_csv):
        print("Anda belum melakukan pembelian.")
        kembali = input("\nKetik 'ya' jika ingin kembali: ").lower().strip()
        if kembali == 'ya':
            menu_pengguna()
            return 
        else:
            print("Input tidak valid. Ketik 'ya' untuk kembali.")
            lihat_riwayat_pembelian()
    with open(nama_pembelian_csv, mode='r') as file:
        reader = csv.reader(file)
        print(f"{'No':<5} {'Nama Pengguna':<15} {'Bibit':<15} {'Kualitas':<15} {'Kuantitas':<10} {'Total Harga':<15}")
        print("-" * 115)
        for index, row in enumerate(reader, start=1):
            if row[0] == nama_pengguna: 
                print(f"{index:<5} {row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<10} {row[4]:<15}")
    print("=" * 115)
    kembali = input("\nKetik 'ya' jika ingin kembali: ").lower()
    if kembali == 'ya':
        menu_pengguna()
    else:
        print("Input tidak valid. Ketik 'ya' untuk kembali.")
        lihat_riwayat_pembelian()
        
def tampilkan_deskripsi_perawatan():
    os.system("cls")
    tampilkan_tabel()  # Menampilkan tabel bibit
    try:
        nomor_bibit = int(input("Masukkan nomor bibit untuk melihat deskripsi perawatan: "))
        if 1 <= nomor_bibit <= len(jenis_bibit):
            nama_bibit = jenis_bibit[nomor_bibit - 1]
            found = False
            if os.path.exists('deskripsi_produk.csv'):
                with open('deskripsi_produk.csv', mode='r') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if row[0].lower() == nama_bibit.lower():
                            print(f"\nDeskripsi perawatan untuk '{row[0]}': {row[1]}")
                            found = True
                            break
            if not found:
                print(f"Deskripsi perawatan untuk '{nama_bibit}' belum tersedia.")
            
            pilihan = input("\nApakah Anda ingin melihat deskripsi perawatan bibit lain? (ya/tidak): ").lower().strip()
            if pilihan == 'ya':
                tampilkan_deskripsi_perawatan()
            else:
                print("Kembali ke menu pengguna.")
                menu_pengguna()
        else:
            print("Nomor bibit tidak valid. Silakan coba lagi.")
            tampilkan_deskripsi_perawatan()
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
        tampilkan_deskripsi_perawatan()
        
def simpan_pembelian(bibit, kualitas, kuantitas, total_harga):
    with open(nama_pembelian_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama_pengguna, bibit, kualitas, kuantitas, total_harga])

def lihat_daftar_harga ():
    os.system("cls")
    while True:
        tampilkan_tabel ()
        kembali = input("\nKetik 'ya' jika ingin kembali: ").lower()
        if kembali == 'ya':
           menu_pengguna ()
        else:
            print("Input tidak valid. Silakan tekan 'ya' untuk kembali.")

def membeli():
    os.system("cls")
    tampilkan_tabel()
    diskon = {200000: 0.03, 400000: 0.05, 600000: 0.07}
    total_pembelian = 0
    transaksi = []  
    if nama_pengguna is None:
        pass
    while True:
        print("="*35)
        print("|       MENU PEMBELIAN BIBIT      |")
        print("="*35)
        print("\tDaftar Jenis Bibit: ")
        nomor = 1
        for bibit in jenis_bibit:
            print(f"\t{nomor}. {bibit}")
            nomor += 1
        try:
            pilihan_bibit = int(input("Pilih nomor jenis bibit yang ingin dibeli: "))
            if pilihan_bibit < 1 or pilihan_bibit > len(jenis_bibit):
                print("Pilihan tidak ada, silahkan coba lagi.")
                continue
        except ValueError:
            print("Masukkan angka yang valid, silahkan coba lagi.")
            continue
        nama_bibit = jenis_bibit[pilihan_bibit - 1]
        harga_bibit_standar = harga_standar[pilihan_bibit - 1]
        harga_bibit_premium = harga_premium[pilihan_bibit - 1]
        kualitas = input("Pilih kualitas bibit (Standar/Premium): ").lower().strip()
        if kualitas not in ["standar", "premium"]:
            print("Kualitas tidak tersedia, silahkan pilih kualitas yang ada.")
            continue
        stok = stok_standar if kualitas == "standar" else stok_premium
        harga_bibit = harga_bibit_standar if kualitas == "standar" else harga_bibit_premium
        if stok[pilihan_bibit - 1] == 0:
            print(f"Mohon maaf stok {nama_bibit} dengan kualitas {kualitas} sudah habis.")
            continue
        try:
            kuantitas = int(input(f"Masukkan jumlah bibit yang ingin dibeli (stok tersedia: {stok[pilihan_bibit - 1]}): "))
            if kuantitas <= 0 or kuantitas > stok[pilihan_bibit - 1]:
                print("Kuantitas tidak valid, silahkan coba lagi.")
                continue
        except ValueError:
            print("Masukkan jumlah yang valid, silahkan coba lagi.")
            continue
        print(f"Bibit yang dibeli berupa {nama_bibit} dengan kualitas {kualitas} {kuantitas}")
        total_harga_bibit = harga_bibit * kuantitas
        total_pembelian += total_harga_bibit
        break
        
    diskon_persen = 0
    for batas, persen in diskon.items():
        if total_pembelian > batas:
            diskon_persen = persen
    jumlah_diskon = total_pembelian * diskon_persen
    total_setelah_diskon = total_pembelian - jumlah_diskon
    try:
        pembayaran = int(input(f"Total belanja Anda: Rp {total_setelah_diskon:,}\nMasukkan jumlah uang: Rp "))
        if pembayaran < total_setelah_diskon:
            print("Uang anda tidak cukup. Transaksi dibatalkan.")
            membeli()
        else : 
            transaksi.append((nama_bibit, kualitas, kuantitas, harga_bibit, total_harga_bibit))
            stok[pilihan_bibit - 1] -= kuantitas 
        kembalian = pembayaran - total_setelah_diskon
    except ValueError:
        print("Masukkan jumlah yang valid. Transaksi dibatalkan.")
        membeli()
    for item in transaksi :
        laporan_pembelian_pengguna.append({
        "Nama Pembeli"                   : nama_pengguna,
        "Jenis Bibit"                    : item[0],
        "Kualitas"                       : item[1],
        "Kuantitas"                      : item[2],
        "Harga Pembelian"                : item[4],
        "Harga Pembelian Setelah Diskon" : total_setelah_diskon
    })
    with open("struk_pembelian.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nama Pengguna", nama_pengguna])
        writer.writerow(["Nama Bibit", "Kualitas", "Kuantitas", "Harga Satuan", "Total Harga"])
        for item in transaksi:
            writer.writerow(item)
        writer.writerow([])
        writer.writerow(["Total Harga", "", "", "", f"Rp {total_pembelian:,}"])
        writer.writerow(["Diskon", "", "", "", f"Rp {jumlah_diskon:,}"])
        writer.writerow(["Total Bayar", "", "", "", f"Rp {total_setelah_diskon:,}"])
        writer.writerow(["Pembayaran", "", "", "", f"Rp {pembayaran:,}"])
        writer.writerow(["Kembalian", "", "", "", f"Rp {kembalian:,}"])

    df_pembelian = pd.DataFrame(laporan_pembelian_pengguna)
    df_pembelian.to_csv("laporan_pembelian_pengguna.csv", index=False)
    simpan_pembelian(nama_bibit, kualitas, kuantitas, total_harga_bibit)

    print("="*47)
    print("|                STRUK PEMBELIAN              |")
    print("="*47)
    for item in transaksi:
        print(f"{item[0]} ({item[1]}) - {item[2]}  x Rp {item[3]:,} = Rp {item[4]:,}") 
    print("-"*47)
    print(f"Nama Pembeli     : {nama_pengguna}")
    print(f"Total Harga      : Rp {total_pembelian:,}")
    print(f"Diskon           : {diskon_persen*100:.0f}% (Rp {jumlah_diskon:,})")
    print("-"*47)
    print(f"Total Bayar      : Rp {total_setelah_diskon:,}")
    print(f"Uang Anda        : Rp {pembayaran:,}")
    print(f"Kembalian        : Rp {kembalian:,}")
    print("="*47)
    ada_ulasan ()

def ada_ulasan () : 
    ulasan = input("Apakah Anda ingin memberikan ulasan? (Ya/Tidak): ").lower()
    if ulasan == 'ya':
        isi_ulasan = input("Masukkan ulasan Anda: ")
        if not isi_ulasan.strip():
            print("ulasan tidak boleh kosong bro")
            ada_ulasan()
        ulasan_list.append({"nama": nama_pengguna, "ulasan": isi_ulasan})
        print("Ulasan berhasil ditambahkan!")
        menu_pengguna ()
    elif ulasan == 'tidak' : 
        print ("Terimakasih Sudah Membeli Produk Kami!")
        menu_pengguna ()
    else :
        print ("Pilihan tidak tersedia. Silahkan coba lagi!")
        ada_ulasan()

def menu_admin():
    os.system("cls")
    print("\n=== Menu Admin ===")
    print("1. Update Daftar Bibit")
    print("2. Laporan Pembelian")
    print("3. Lihat Ulasan")
    print("4. Deskripsi Perawatan")
    print("5. Keluar")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == "1": 
        menu_update()
    elif pilihan == "2":    
        laporan_pembelian()   
    elif pilihan == "3":
        lihat_ulasan()
    elif pilihan == "4":
        lihat_deskripsi_bibit()
    elif pilihan == "5":
        os.system("cls")
        main_menu() 
    else: 
        print("Pilihan tidak tersedia. Silahkan coba lagi!")
    menu_admin()

def lihat_deskripsi_bibit():
    os.system("cls")
    print("\n=== Menu Admin ===")
    print("1. Tambah Deskripsi")
    print("2. Hapus Deskripsi")
    print("3. Lihat Deskripsi")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")
    if pilihan == "1": 
        tambah_deskripsi()
    elif pilihan == "2":    
        hapus_deskripsi()   
    elif pilihan == "3":
        lihat_deskripsi()
    elif pilihan == "4":
        os.system("cls")
        main_menu() 
    else: 
        print("Pilihan tidak tersedia. Silahkan coba lagi!")
        menu_admin()

def lihat_deskripsi():
    os.system("cls")
    if not os.path.exists('deskripsi_produk.csv'):
        print("Belum ada deskripsi yang tersedia.")
        return
    print("=" * 115)
    print("Deskripsi Bibit".center(115))
    print("=" * 115)
    with open('deskripsi_produk.csv', mode='r') as file:
        reader = csv.reader(file)
        print(f"{'No':<5} {'Nama Produk':<20} {'Deskripsi':<25}")
        print("=" * 50)
        for index, row in enumerate(reader, start=1):
            print(f"{index:<5} {row[0]:<20} {row[1]:<25}")
    print("=" * 50)

def tambah_deskripsi():
    os.system("cls")
    tampilkan_tabel()  
    try:
        nomor_bibit = int(input("Masukkan nomor bibit untuk menambahkan deskripsi: "))
        if nomor_bibit < 1 or nomor_bibit > len(jenis_bibit):
            print("Nomor bibit tidak valid. Silakan coba lagi.")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor yang benar.")
        return

    nama_produk = jenis_bibit[nomor_bibit - 1]  
    deskripsi = input(f"Masukkan deskripsi untuk '{nama_produk}': ")
    rows = []
    found = False
    try:
        with open('deskripsi_produk.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == nama_produk.lower():
                    row[1] = deskripsi  
                    found = True
                rows.append(row)
    except FileNotFoundError:
        pass
    if not found:
        rows.append([nama_produk, deskripsi])  
        print(f"Deskripsi baru untuk '{nama_produk}' berhasil ditambahkan!")
    else:
        print(f"Deskripsi untuk '{nama_produk}' berhasil diperbarui!")
    with open('deskripsi_produk.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    while True:
        lagi = input("\nApakah Anda ingin menambahkan deskripsi untuk bibit lain? (ya/tidak): ").lower()
        if lagi == 'ya':
            tambah_deskripsi()  
            return
        elif lagi == 'tidak':
            break
        else:
            print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")

def hapus_deskripsi():
    os.system("cls")
    while True:
        lihat_deskripsi()  
        nomor_input = input("Masukkan nomor deskripsi yang ingin dihapus: ")
        try:
            nomor = int(nomor_input)
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor yang benar.")
            continue
        rows = []
        found = False
        try:
            with open('deskripsi_produk.csv', mode='r') as file:
                reader = csv.reader(file)
                for index, row in enumerate(reader, start=1):
                    if index == nomor:
                        found = True  
                        print(f"Deskripsi untuk '{row[0]}' telah dihapus.")
                        continue  
                    rows.append(row)
        except FileNotFoundError:
            print("File deskripsi_produk.csv tidak ditemukan.")
            return
        if not found:
            print("Nomor deskripsi tidak valid. Tidak ada yang dihapus.")
        else:
            with open('deskripsi_produk.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("\nTabel deskripsi setelah penghapusan:")
            lihat_deskripsi()  
        lagi = input("\nApakah Anda ingin menghapus deskripsi lain? (ya/tidak): ").lower()
        if lagi == 'tidak':
            break
        elif lagi != 'ya':
            print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")

def lihat_ulasan():
    os.system("cls")
    if not ulasan_list:
        print("Belum ada ulasan.")
    else:
        print("=" * 40)
        print("Daftar Ulasan".center(40))
        print("=" * 40)
        for i, ulasan in enumerate(ulasan_list, start=1):
            print(f"{i}. {ulasan['nama']}: {ulasan['ulasan']}")
        print("=" * 40)

def menu_update():
    os.system("cls")
    while True:
        print("\nMenu Update:")
        print("1. Tambah Bibit")
        print("2. Hapus Bibit")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        if pilihan == "1":
            tambah_bibit()
        elif pilihan == "2":
            hapus_bibit()
        elif pilihan == "3":
            print("Terima kasih telah berkunjung!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

def tambah_bibit():
    os.system("cls")
    while True:
        nama_bibit = str(input("Masukkan nama bibit baru: "))
        if not nama_bibit.isalpha() or not nama_bibit.strip():
            print("Nama bibit harus berupa huruf dan tidak boleh kosong. Silakan coba lagi.")
            continue
        try:
            harga = int(input("Masukkan harga standar bibit: "))
            stok_standar_bibit = int(input("Masukkan stok standar bibit: "))
            stok_premium_bibit = int(input("Masukkan stok premium bibit: "))
        except ValueError:
            print("Harga dan stok harus berupa angka bulat. Silakan coba lagi.")
            continue
        harga_premium_bibit = harga + 5000
        jenis_bibit.append(nama_bibit)
        harga_standar.append(harga)
        harga_premium.append(harga_premium_bibit)
        stok_standar.append(stok_standar_bibit)
        stok_premium.append(stok_premium_bibit)
        tampilkan_tabel()
        print(f"Bibit '{nama_bibit}' berhasil ditambahkan!")
        break

def hapus_bibit():
    os.system("cls")
    tampilkan_tabel()
    try:
        no_bibit = int(input("Masukkan nomor bibit yang ingin dihapus: "))
        if no_bibit < 1 or no_bibit > len(jenis_bibit):
            print("Nomor bibit tidak valid!")
        else:
            jenis_bibit.pop(no_bibit - 1)
            harga_standar.pop(no_bibit - 1)
            harga_premium.pop(no_bibit - 1)
            stok_standar.pop(no_bibit - 1)
            stok_premium.pop(no_bibit - 1)
            print(f"Bibit nomor {no_bibit} berhasil dihapus!")
    except ValueError:
        print("Masukkan nomor bibit yang valid.")

def laporan_pembelian():
    if not laporan_pembelian_pengguna:
        print("Belum ada transaksi yang dilakukan.")
        return        

    print("="*115)
    print("Laporan Pembelian".center(115))
    print("="*115)
    print("+----------------+-------------+----------+------------+-----------------+--------------------------------+")
    print("| Nama Pembeli   | Jenis Bibit | Kualitas | Kuantitas  | Harga Pembelian | Harga Pembelian Setelah Diskon |")
    print("+----------------+-------------+----------+------------+-----------------+--------------------------------+")
    total_pembelian=0
    total_pembelian_setelah_diskon=0
    for pembelian in laporan_pembelian_pengguna:
        print("| {:<14} | {:<11} | {:<8} | {:<10} | {:<15} | {:<30} |".format(
            pembelian["Nama Pembeli"], pembelian["Jenis Bibit"],
            pembelian["Kualitas"], pembelian["Kuantitas"],
            pembelian["Harga Pembelian"],pembelian["Harga Pembelian Setelah Diskon"]))
        
        total_pembelian += pembelian["Harga Pembelian"]
        total_pembelian_setelah_diskon += pembelian["Harga Pembelian Setelah Diskon"]
    
    print("+----------------+-------------+----------+------------+-----------------+--------------------------------+")
    print(f"| Total Keseluruhan Pembelian :           |            |Rp{total_pembelian:,.0f}        | Rp{total_pembelian_setelah_diskon:,.0f}                      |")
    print("="*115)


    df_pembelian = pd.DataFrame(laporan_pembelian_pengguna)
    df_pembelian.to_csv("Laporan Pembelian.csv", index=False)
    df_pembelian = pd.read_csv("Laporan Pembelian.csv")

if __name__ == "__main__":
    main_menu()
