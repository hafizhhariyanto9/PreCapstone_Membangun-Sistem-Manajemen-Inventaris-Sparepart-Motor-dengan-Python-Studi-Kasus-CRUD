# Project Pre-Capstone E-Commerce Hafizh Saddam
# Ini adalah komentar yang memberikan judul atau deskripsi proyek.

# --- Data Inventaris (List of Dictionaries) ---

ban = [{"Merek": "Bridgestone", "Stok": 30, "Harga": 800000},
       # List (daftar) untuk kategori Ban. Setiap item adalah Dictionary (kamus)
       {"Merek": "Dunlop", "Stok": 20, "Harga": 950000},  # yang menyimpan Merek, Stok, dan Harga.
       {"Merek": "Maxxis", "Stok": 15, "Harga": 500000},
       ]
oli = [{"Merek": "Motul", "Stok": 50, "Harga": 150000},  # List untuk kategori Oli.
       {"Merek": "Shell", "Stok": 80, "Harga": 100000},
       {"Merek": "Castrol", "Stok": 65, "Harga": 125000}
       ]

lampu = [{"Merek": "Osram", "Stok": 20, "Harga": 90000},  # List untuk kategori Lampu.
         {"Merek": "Philips", "Stok": 30, "Harga": 110000},
         {"Merek": "Bosch", "Stok": 30, "Harga": 75000},
         ]
cart = []  # List kosong untuk menyimpan item yang sedang dibeli (Keranjang Belanja).
list_kategori = ["Ban", "Oli", "Lampu"]  # List berisi nama-nama kategori.

# --- Variabel Pengaturan Tampilan Tabel ---

lebar_indeks = 7  # Variabel untuk mengatur lebar kolom 'Index'.
lebar_kategori = 15  # Variabel untuk mengatur lebar kolom 'Kategori' atau 'Merek'.
lebar_stok = 5  # Variabel untuk mengatur lebar kolom 'Stok'.
lebar_harga = 12  # Variabel untuk mengatur lebar kolom 'Harga' atau 'Subtotal'.


# --- Definisi Fungsi ---

def kategoriSparepart():  # Fungsi untuk mencetak tabel daftar kategori.
    print("\n--- Daftar Kategori Sparepart ---")
    print("============================")
    # Mencetak header tabel, menggunakan f-string untuk format dengan lebar kolom (:<{lebar_indeks} = rata kiri).
    print(f"| {'Index':<{lebar_indeks}}| {'Kategori':<{lebar_kategori}} |")
    print("============================")
    for i in range(len(list_kategori)):  # Iterasi (loop) sebanyak jumlah kategori.
        # Mencetak Index (i) dan nama kategori.
        print(f"| {i:<{lebar_indeks}}| {list_kategori[i]:<{lebar_kategori}} |")
    print("============================")


def daftarSparepart():  # Fungsi untuk mencetak tabel daftar spare part dalam kategori yang dipilih.
    # Menggunakan variabel global 'nama_kategori' dan 'list_data' yang diatur di menu utama.
    print(f"\n--- Daftar Sparepart Kategori {nama_kategori} ---")
    print("===============================================")
    # Mencetak header tabel (Index, Merek, Stok, Harga).
    print(
        f"|{'Index':<{lebar_indeks}}| {'Merek':{lebar_kategori}}| {'Stok':<{lebar_stok}}| {"Harga":<{lebar_harga}} |")
    print("===============================================")
    for j in range(len(list_data)):  # Loop melalui item-item dalam list_data yang dipilih.
        # Mengakses nilai Merek, Stok, dan Harga dari dictionary pada index j.
        print(
            f'''|{j:<{lebar_indeks}}| {list_data[j]["Merek"]:<{lebar_kategori}}| {list_data[j]["Stok"]:<{lebar_stok}}| {list_data[j]["Harga"]:<{lebar_harga}} |''')
    print("===============================================")


def format_rupiah(angka):  # Fungsi untuk memformat angka menjadi string Rupiah.
    # Mengubah angka menjadi string dengan pemisah ribuan (1.000.000).
    rupiah_str = f"{int(angka):,.0f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"Rp {rupiah_str},-"  # Mengembalikan string Rupiah.


# --- Loop Utama Program ---

while True:  # Loop utama program yang akan berjalan terus sampai ada 'break'.
    pilihKategori = input('''\nSelamat datang di Webike Indonesia !!!
\nList Menu :
1. Menampilkan Kategori Sparepart
2. Menambah Sparepart
3. Menghapus Sparepart
4. Mengubah Sparepart
5. Membeli Sparepart
6. Exit Program
Pilih list menu : ''')  # Menampilkan menu dan menerima input pilihan menu.

    if pilihKategori in ['1', '2', '3', '4']:  # Jika memilih opsi manajemen data (1, 2, 3, 4), tampilkan kategori dulu.
        kategoriSparepart()

    if pilihKategori == '1':  # Logika untuk Menu 1: Menampilkan Sparepart.
        pilihIndex = int(input("Silahkan Masukkan Index Kategori Sparepart : "))
        if pilihIndex == 0:
            list_data, nama_kategori = ban, "Ban"  # Menetapkan variabel global list_data ke 'ban' dan nama_kategori.
        elif pilihIndex == 1:
            list_data, nama_kategori = oli, "Oli"  # Menetapkan variabel global list_data ke 'oli'.
        elif pilihIndex == 2:
            list_data, nama_kategori = lampu, "Lampu"  # Menetapkan variabel global list_data ke 'lampu'.
        else:
            print("Indeks kategori tidak valid.")
            continue  # Melanjutkan ke awal loop jika input tidak valid.

        daftarSparepart()  # Menampilkan daftar spare part.


    elif pilihKategori == '2':  # Logika untuk Menu 2: Menambah Sparepart.
        pilihIndex = int(input('Masukkan index kategori sparepart : '))
        # Logika pemilihan list_data.
        if pilihIndex == 0:
            list_data, nama_kategori = ban, "Ban"
        elif pilihIndex == 1:
            list_data, nama_kategori = oli, "Oli"
        elif pilihIndex == 2:
            list_data, nama_kategori = lampu, "Lampu"
        else:
            print("Indeks kategori tidak valid.")
            continue

        merekPart = input(
            'Masukkan merek sparepart : ').strip().title()  # Input Merek, membersihkan spasi dan mengubah huruf pertama menjadi kapital.
        stokPart = int(input('Masukkan stok sparepart : '))
        hargaPart = int(input('Masukkan harga sparepart : '))

        # Menambahkan dictionary baru (spare part baru) ke list_data yang dipilih.
        list_data.append({"Merek": merekPart, "Stok": stokPart, "Harga": hargaPart})

        print(f"{merekPart} berhasil ditambah ke dalam kategori {nama_kategori}.")

        daftarSparepart()


    elif pilihKategori == '3':  # Logika untuk Menu 3: Menghapus Sparepart.
        pilihIndex = int(input('Silahkan Masukkan Index Kategori sparepart : '))
        # Logika pemilihan list_data.
        if pilihIndex == 0:
            list_data, nama_kategori = ban, "Ban"
        elif pilihIndex == 1:
            list_data, nama_kategori = oli, "Oli"
        elif pilihIndex == 2:
            list_data, nama_kategori = lampu, "Lampu"
        else:
            print("Indeks kategori tidak valid.")
            continue

        daftarSparepart()
        indexMerk = int(input('Masukkan Index Merek Sparepart yang ingin dihapus: '))

        if 0 <= indexMerk < len(list_data):  # Memastikan index yang dimasukkan ada dalam rentang list.
            nama_merek = list_data[indexMerk]["Merek"]
            del list_data[indexMerk]  # Menghapus item pada index yang ditentukan dari list.
            kembali = input("Serius mau dihapus (ya/tidak): ").lower()  # Konfirmasi penghapusan.
            if kembali == "ya":
                daftarSparepart()
                print(f"{nama_merek} berhasil dihapus dari kategori {nama_kategori}")
                break  # Menghentikan program (keluar dari loop while True).
            elif kembali == "tidak":
                continue  # Kembali ke awal loop while True.
        else:
            print("Index merek tidak valid.")


    elif pilihKategori == '4':  # Logika untuk Menu 4: Mengubah Sparepart.
        pilihIndex = int(input('Masukkan Index kategori sparepart : '))
        # Logika pemilihan list_data.
        if pilihIndex == 0:
            list_data, nama_kategori = ban, "Ban"
        elif pilihIndex == 1:
            list_data, nama_kategori = oli, "Oli"
        elif pilihIndex == 2:
            list_data, nama_kategori = lampu, "Lampu"
        else:
            print("Indeks kategori tidak valid.")
            continue

        daftarSparepart()

        merekIndex = int(input('Masukkan Index merek sparepart yang ingin diubah: '))
        if not (0 <= merekIndex < len(list_data)):  # Memastikan index merek valid.
            print("Index merek tidak valid.")
            continue
        kolomPart = input('Masukkan kolom sparepart yang ingin diubah (Stok atau Harga) : ').strip().title()
        if kolomPart not in ["Stok", "Harga"]:  # Memastikan input kolom adalah "Stok" atau "Harga".
            print("Kolom yang dimasukkan tidak valid. Pilih 'Stok' atau 'Harga'.")
            continue
        valuePart = int(input(f'Masukkan {kolomPart} baru untuk sparepart: '))

        # Mengubah nilai pada dictionary yang ditargetkan (list_data[merekIndex]) dengan key kolomPart.
        list_data[merekIndex][kolomPart] = valuePart
        kembali = input(
            "Serius mau dihapus (ya/tidak): ").lower()  # Konfirmasi (tertulis "dihapus" padahal operasi "ubah").
        if kembali == "ya":
            daftarSparepart()
            print(f"Data {kolomPart} sparepart {list_data[merekIndex]["Merek"]} berhasil diubah.")
            break  # Menghentikan program (keluar dari loop while True).
        elif kembali == "tidak":
            continue


    elif pilihKategori == '5':  # Logika untuk Menu 5: Membeli Sparepart.
        cart = []  # Inisialisasi keranjang belanja kosong.
        total_final = 0

        while True:  # Loop untuk memungkinkan pembelian banyak item secara berurutan.
            kategoriSparepart()
            pilihIndex = int(input('Masukkan indeks kategori sparepart yang ingin dibeli : '))
            # Logika pemilihan list_data.
            if pilihIndex == 0:
                list_data, nama_kategori = ban, "Ban"
            elif pilihIndex == 1:
                list_data, nama_kategori = oli, "Oli"
            elif pilihIndex == 2:
                list_data, nama_kategori = lampu, "Lampu"
            else:
                print("Indeks kategori tidak valid.")
                continue

            daftarSparepart()

            indexMerk = int(input('Masukkan Indeks Merek yang ingin dibeli: '))

            if 0 <= indexMerk < len(list_data):
                merek_pilihan = list_data[indexMerk]
                banyakPart = int(input(f"Silahkan masukkan jumlah {merek_pilihan['Merek']} yang ingin dibeli: "))

                if banyakPart > 0:

                    if banyakPart <= merek_pilihan["Stok"]:  # Pengecekan stok.

                        item_di_cart = None
                        for item in cart:  # Loop untuk mencari item di keranjang belanja.
                            if item["Merek"] == merek_pilihan["Merek"]:
                                item_di_cart = item
                                break

                        if item_di_cart:
                            item_di_cart["Qty"] += banyakPart  # Jika sudah ada, tambahkan kuantitas (Qty).
                        else:
                            cart.append({  # Jika belum ada, tambahkan item baru ke cart.
                                "Merek": merek_pilihan["Merek"],
                                "Qty": banyakPart,
                                "Harga": merek_pilihan["Harga"]
                            })

                        merek_pilihan["Stok"] -= banyakPart  # Mengurangi stok di inventaris utama.
                        print(f"\n{banyakPart} pcs {merek_pilihan['Merek']} berhasil ditambahkan ke keranjang.")

                    else:
                        print(f"Stok tidak cukup. Stok {merek_pilihan['Merek']} tersisa {merek_pilihan['Stok']}.")
                else:
                    print("Kuantitas harus lebih dari 0.")
            else:
                print("Index Merek tidak valid.")

            # Perhitungan dan Tampilan Keranjang
            total_final = 0
            if len(cart) == 0:
                print("\nKeranjang belanja kosong.")
            else:
                # Menampilkan header tabel keranjang.
                print("\n--- Isi Keranjang Belanja ---")
                # ... (Logika pencetakan tabel dan perhitungan subtotal) ...
                for item in cart:
                    subtotal = item['Qty'] * item['Harga']
                    total_final += subtotal  # Akumulasi total belanja.
                # ... (Pencetakan TOTAL BELANJA) ...

            lanjut = input("\nLanjut belanja item lain? (ya/tidak): ").strip().lower()
            if lanjut != 'ya':
                break  # Keluar dari loop belanja, lanjut ke proses pembayaran.

        # Proses Pembayaran
        if len(cart) > 0:
            print("\n--- Proses Pembayaran ---")
            print(f"TOTAL YANG HARUS DIBAYAR: {format_rupiah(total_final)}")
            while True:
                jumlah_bayar = int(input("Masukkan jumlah uang yang dibayarkan: "))

                if jumlah_bayar > total_final:
                    kembalian = jumlah_bayar - total_final
                    # Mencetak struk transaksi berhasil.
                    print("\n=== Transaksi Berhasil ===")
                    print(f"Uang Dibayarkan : {format_rupiah(jumlah_bayar)}")
                    print(f"Total Belanja   : {format_rupiah(total_final)}")
                    print(f"Kembalian       : {format_rupiah(kembalian)}")
                    print("Terima kasih atas pembelian Anda!")
                    cart = []  # Mengosongkan keranjang.
                    break
                elif jumlah_bayar < total_final:
                    # Mencetak pesan error kekurangan uang. (Ada typo 'mencukupiprint')
                    print(
                        f"\nPembayaran Gagal. Jumlah uang yang dibayarkan tidak mencukupiprint uangnya kurang sebesar {format_rupiah(total_final - jumlah_bayar)}.")
                    continue
                else:  # Jika jumlah_bayar == total_final
                    # Mencetak struk tanpa kembalian.
                    # ...
                    cart = []
                    break
        else:
            print("Tidak ada item di keranjang untuk diproses pembayaran.")

    elif pilihKategori == '6':  # Logika untuk Menu 6: Exit Program.
        print("Terimakasih Sudah Berkunjung !")
        break  # Keluar dari loop utama, mengakhiri program.
    else:
        print("Input yang dimasukkan tidak valid !")

    # Logika Kembali ke Menu/Exit
    kembali = input("Apakah anda ingin kembali ke menu? (ya/tidak): ").lower()
    if kembali == "ya":
        continue  # Melanjutkan ke awal loop while True (kembali ke menu utama).
    elif kembali == "tidak":
        print("Terimakasih Sudah Berkunjung !")
        break  # Keluar dari loop, mengakhiri program.

