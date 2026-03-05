# Membangun Sistem Manajemen Inventaris Sparepart Motor dengan Python: Studi Kasus CRUD 

*Bagaimana prinsip CRUD yang dipakai industri bisa diimplementasikan dengan Python murni — tanpa framework, tanpa database, tanpa kompromi.*
Oleh : Hafizh Hariyanto & Saddam Fachriza
---

## Latar Belakang

Di dunia industri software, hampir semua sistem yang berinteraksi dengan data — mulai dari aplikasi POS toko retail, sistem ERP perusahaan manufaktur, hingga platform e-commerce berskala besar — semuanya berdiri di atas satu fondasi yang sama: **CRUD** (*Create, Read, Update, Delete*).

Pertanyaannya: seberapa dalam kita benar-benar memahami CRUD jika selama ini hanya mengandalkan ORM atau framework yang menyembunyikan logikanya?

Artikel ini membahas implementasi CRUD secara *bare-metal* melalui studi kasus **Webike Indonesia** — sebuah sistem manajemen inventaris dan transaksi sparepart motor yang dibangun dengan Python murni. Tanpa Django, tanpa SQLAlchemy, tanpa library pihak ketiga. Hanya logika, struktur data, dan pemahaman mendalam tentang bagaimana data seharusnya dikelola.

---

## Gambaran Umum Sistem

Webike Indonesia adalah sistem CLI (*Command Line Interface*) untuk mengelola inventaris dan transaksi sparepart motor — use case yang sangat relevan dengan kebutuhan bisnis otomotif skala kecil hingga menengah di Indonesia. Sistem ini mencakup tiga kategori produk:

- **Ban** — Bridgestone, Dunlop, Maxxis
- **Oli** — Motul, Shell, Castrol
- **Lampu** — Osram, Philips, Bosch

Setiap produk memiliki atribut **Merek**, **Stok**, dan **Harga** yang disimpan dalam struktur data List of Dictionaries.

---

## Fitur Utama

Aplikasi ini memiliki 6 menu utama:

1. **Menampilkan Kategori Sparepart** — Melihat daftar produk dalam satu kategori
2. **Menambah Sparepart** — Menambahkan produk baru ke dalam inventaris
3. **Menghapus Sparepart** — Menghapus produk dari daftar
4. **Mengubah Sparepart** — Memperbarui stok atau harga produk
5. **Membeli Sparepart** — Simulasi proses pembelian dengan keranjang belanja
6. **Exit Program** — Keluar dari aplikasi

---

## Deep Dive: Implementasi CRUD

CRUD (*Create, Read, Update, Delete*) adalah fondasi dari hampir semua aplikasi yang berinteraksi dengan data. Di Webike Indonesia, keempat operasi ini diimplementasikan secara manual tanpa bantuan database — murni menggunakan struktur data Python.

---

### 🟢 CREATE — Menambah Sparepart Baru

Operasi Create memungkinkan admin menambahkan produk baru ke dalam kategori yang dipilih. Setelah pengguna memilih kategori dan mengisi detail produk, program membuat Dictionary baru dan meng-append-nya ke list yang sesuai.

```python
elif pilihKategori == '2':  # Menu 2: Menambah Sparepart
    pilihIndex = int(input('Masukkan index kategori sparepart : '))

    if pilihIndex == 0:
        list_data, nama_kategori = ban, "Ban"
    elif pilihIndex == 1:
        list_data, nama_kategori = oli, "Oli"
    elif pilihIndex == 2:
        list_data, nama_kategori = lampu, "Lampu"

    merekPart = input('Masukkan merek sparepart : ').strip().title()
    stokPart  = int(input('Masukkan stok sparepart : '))
    hargaPart = int(input('Masukkan harga sparepart : '))

    # Append dictionary baru ke list inventaris
    list_data.append({"Merek": merekPart, "Stok": stokPart, "Harga": hargaPart})

    print(f"{merekPart} berhasil ditambah ke dalam kategori {nama_kategori}.")
    daftarSparepart()
```

> **Catatan teknis:** Karena `list_data` adalah referensi ke list asli (`ban`, `oli`, atau `lampu`), `.append()` langsung memodifikasi data sumber — tidak perlu mekanisme sinkronisasi tambahan.

---

### 🔵 READ — Menampilkan Daftar Sparepart

Operasi Read menampilkan semua item dalam kategori yang dipilih dalam format tabel yang rapi. Fungsi `daftarSparepart()` mengiterasi `list_data` dan mencetak setiap item menggunakan f-string alignment.

```python
def daftarSparepart():
    print(f"\n--- Daftar Sparepart Kategori {nama_kategori} ---")
    print("===============================================")
    print(f"|{'Index':<{lebar_indeks}}| {'Merek':{lebar_kategori}}| {'Stok':<{lebar_stok}}| {'Harga':<{lebar_harga}} |")
    print("===============================================")

    for j in range(len(list_data)):
        print(
            f"|{j:<{lebar_indeks}}| "
            f"{list_data[j]['Merek']:<{lebar_kategori}}| "
            f"{list_data[j]['Stok']:<{lebar_stok}}| "
            f"{list_data[j]['Harga']:<{lebar_harga}} |"
        )
    print("===============================================")
```

Output yang dihasilkan terlihat seperti ini:

```
--- Daftar Sparepart Kategori Ban ---
===============================================
|Index  | Merek         | Stok | Harga        |
===============================================
|0      | Bridgestone   | 30   | 800000       |
|1      | Dunlop        | 20   | 950000       |
|2      | Maxxis        | 15   | 500000       |
===============================================
```

> **Catatan teknis:** Operator `:<{lebar}` pada f-string berarti *left-align* dengan lebar kolom dinamis. Lebar setiap kolom didefinisikan sebagai variabel terpisah sehingga mudah disesuaikan.

---

### 🟡 UPDATE — Mengubah Stok atau Harga

Operasi Update memungkinkan admin mengubah nilai `Stok` atau `Harga` dari produk tertentu. Program memvalidasi input kolom sebelum melakukan perubahan.

```python
elif pilihKategori == '4':  # Menu 4: Mengubah Sparepart
    # ... (pilih kategori dan tampilkan tabel) ...

    merekIndex = int(input('Masukkan Index merek sparepart yang ingin diubah: '))

    # Validasi index
    if not (0 <= merekIndex < len(list_data)):
        print("Index merek tidak valid.")
        continue

    kolomPart = input('Masukkan kolom yang ingin diubah (Stok atau Harga) : ').strip().title()

    # Validasi kolom yang boleh diubah
    if kolomPart not in ["Stok", "Harga"]:
        print("Kolom yang dimasukkan tidak valid. Pilih 'Stok' atau 'Harga'.")
        continue

    valuePart = int(input(f'Masukkan {kolomPart} baru untuk sparepart: '))

    # Update nilai dictionary secara langsung menggunakan key dinamis
    list_data[merekIndex][kolomPart] = valuePart

    print(f"Data {kolomPart} sparepart {list_data[merekIndex]['Merek']} berhasil diubah.")
```

> **Catatan teknis:** `list_data[merekIndex][kolomPart] = valuePart` memanfaatkan *dynamic key access* pada Dictionary — `kolomPart` yang berisi string `"Stok"` atau `"Harga"` langsung digunakan sebagai key. Ini jauh lebih efisien daripada menulis dua blok `if/else` terpisah.

---

### 🔴 DELETE — Menghapus Sparepart

Operasi Delete menghapus produk dari list berdasarkan index yang dimasukkan pengguna. Ada validasi range dan konfirmasi sebelum penghapusan dieksekusi.

```python
elif pilihKategori == '3':  # Menu 3: Menghapus Sparepart
    # ... (pilih kategori dan tampilkan tabel) ...

    indexMerk = int(input('Masukkan Index Merek Sparepart yang ingin dihapus: '))

    # Validasi range index
    if 0 <= indexMerk < len(list_data):
        nama_merek = list_data[indexMerk]["Merek"]

        # Konfirmasi sebelum hapus
        kembali = input("Serius mau dihapus (ya/tidak): ").lower()

        if kembali == "ya":
            del list_data[indexMerk]  # Hapus item dari list
            daftarSparepart()
            print(f"{nama_merek} berhasil dihapus dari kategori {nama_kategori}")
        elif kembali == "tidak":
            continue
    else:
        print("Index merek tidak valid.")
```

> **Catatan teknis:** `del list_data[indexMerk]` menghapus item pada index tertentu dan otomatis **meng-shift** semua item setelahnya ke kiri. Validasi range `0 <= indexMerk < len(list_data)` sangat penting untuk menghindari `IndexError`.

---

## Struktur Data yang Digunakan

Salah satu keputusan desain terpenting dalam proyek ini adalah pemilihan struktur data. Saya menggunakan **List of Dictionaries** untuk menyimpan data inventaris:

```python
ban = [
    {"Merek": "Bridgestone", "Stok": 30, "Harga": 800000},
    {"Merek": "Dunlop",      "Stok": 20, "Harga": 950000},
    {"Merek": "Maxxis",      "Stok": 15, "Harga": 500000},
]
```

Kenapa pendekatan ini? Karena **Dictionary** memudahkan akses data berdasarkan nama key yang deskriptif (`item["Merek"]` jauh lebih mudah dipahami daripada `item[0]`), dan **List** memungkinkan operasi seperti append, delete, dan iterasi yang fleksibel.

---

## Logika Keranjang Belanja

Bagian yang paling menarik secara teknis adalah implementasi keranjang belanja. Sistem ini harus:

1. Mengecek ketersediaan stok sebelum menambahkan item
2. Menggabungkan item yang sama jika dibeli lebih dari sekali
3. Mengurangi stok di inventaris utama secara *real-time*
4. Menghitung total belanja secara akumulatif

```python
# Cek apakah item sudah ada di keranjang
item_di_cart = None
for item in cart:
    if item["Merek"] == merek_pilihan["Merek"]:
        item_di_cart = item
        break

if item_di_cart:
    item_di_cart["Qty"] += banyakPart  # Update kuantitas
else:
    cart.append({                       # Tambah item baru
        "Merek": merek_pilihan["Merek"],
        "Qty": banyakPart,
        "Harga": merek_pilihan["Harga"]
    })

merek_pilihan["Stok"] -= banyakPart    # Kurangi stok inventaris
```

Logika pencarian item di keranjang menggunakan **linear search** — sederhana namun efektif untuk skala data ini.

---

## Formatting Rupiah yang Elegan

Satu detail kecil yang saya sukai adalah fungsi `format_rupiah()`. Daripada menampilkan angka mentah seperti `800000`, fungsi ini mengubahnya menjadi format yang lebih mudah dibaca: `Rp 800.000,-`

```python
def format_rupiah(angka):
    rupiah_str = f"{int(angka):,.0f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"Rp {rupiah_str},-"
```

Trik di sini adalah chain `.replace()` untuk mengubah format pemisah ribuan dari gaya internasional (koma) menjadi gaya Indonesia (titik), menggunakan underscore sebagai karakter perantara agar tidak terjadi konflik saat penggantian.

---

## Tampilan Tabel yang Rapi

Aplikasi CLI tidak harus terlihat membosankan. Saya menggunakan **f-string formatting** dengan alignment operator untuk membuat tabel yang rapi di terminal:

```
===============================================
|Index  | Merek         | Stok| Harga         |
===============================================
|0      | Bridgestone   | 30  | 800000        |
|1      | Dunlop        | 20  | 950000        |
|2      | Maxxis        | 15  | 500000        |
===============================================
```

Lebarnya diatur menggunakan variabel global seperti `lebar_indeks`, `lebar_kategori`, dll., sehingga mudah disesuaikan tanpa harus mengubah kode di banyak tempat.

---

## Tantangan Teknis yang Relevan di Industri

### 1. Manajemen State — Masalah Klasik di Sistem Produksi
Sistem ini menggunakan variabel global `list_data` dan `nama_kategori` untuk berbagi state antar fungsi. Di skala ini masih manageable, tapi di sistem produksi nyata, pola ini berbahaya — global state adalah sumber bug yang sulit di-trace dan mustahil di-unit test. Industri menyelesaikan ini dengan dependency injection, singleton pattern, atau context object yang dioper secara eksplisit.

### 2. Validasi Input — Garis Pertama Pertahanan Sistem
Saat ini, konversi `int(input(...))` dilakukan tanpa `try-except`. Di lingkungan produksi, input validation adalah lapisan pertama keamanan sistem — mencegah crash, SQL injection, dan data corruption. Standar industri menggunakan skema validasi seperti Pydantic (Python), Zod (TypeScript), atau Bean Validation (Java).

### 3. Persistensi Data — Kebutuhan Fundamental Bisnis
Semua perubahan data hilang saat program ditutup — tidak ada persistensi. Ini adalah gap terbesar antara prototipe dan sistem produksi. Di industri, solusinya berjenjang: file JSON/CSV untuk tool internal sederhana, SQLite untuk aplikasi lokal, PostgreSQL/MySQL untuk multi-user, dan distributed database untuk skala enterprise.

---

## Roadmap Menuju Production-Ready

Jika sistem ini ingin didorong ke level produksi, berikut jalur pengembangannya:

- **Data persistence** — migrasi ke SQLite atau PostgreSQL dengan ORM seperti SQLAlchemy
- **Input validation** — implementasi schema validation dengan Pydantic
- **Refactoring ke OOP/Service Layer** — class `ProductService`, `CartService`, `PaymentService` dengan separation of concerns yang jelas
- **REST API layer** — expose operasi CRUD via FastAPI agar bisa diakses frontend atau mobile app
- **Audit log** — setiap operasi CRUD tercatat dengan timestamp dan user ID, standar wajib di sistem keuangan

---

## Kesimpulan

CRUD bukan sekadar akronim yang dihafal untuk wawancara kerja. Ia adalah pola berpikir tentang **bagaimana data hidup dalam sebuah sistem** — bagaimana ia lahir (Create), dibaca (Read), berevolusi (Update), dan akhirnya berakhir (Delete).

Membangun Webike Indonesia tanpa abstraksi framework memaksa setiap baris kode ditulis dengan sadar dan penuh pertimbangan. Hasilnya adalah pemahaman yang jauh lebih dalam tentang mengapa ORM ada, mengapa validasi itu penting, dan mengapa persistensi bukan fitur tambahan — melainkan kebutuhan fundamental.

Di industri, kita memang tidak akan sering menulis CRUD dari nol seperti ini. Tapi developer yang pernah melakukannya akan selalu lebih paham apa yang terjadi di balik `Model.objects.create()` atau `repo.save(entity)`.

Kode lengkap tersedia di repositori GitHub kami. Diskusi dan kritik sangat disambut.

---

*Ditulis oleh Hafizh Hariyanto dan Saddam Fachriza.*

*Tags: #Python #SoftwareEngineering #CRUD #BackendDevelopment #InventoryManagement #ECommerce #PythonProgramming*
