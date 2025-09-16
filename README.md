Kadek Chandra Rasmi | 2406426473 | PBP E

URL Deployment : https://kadek-chandra-topcornershop.pbp.cs.ui.ac.id/



<details>
<summary>Tugas 2 : Implementasi Model-View-Template (MVT) pada Django</summary>
 
### Jelaskan bagaimana cara kamu mengimplementasikan checklist yang ada secara step-by-step 
Saya mengimplementasikan tugas ini dengan memahami secara mendalam, mengikuti tutorial yang ada dengan perlahan, serta mencari informasi lebih lanjut di internet. Berikut tahapan yang saya lakukan:
- [x] **Membuat sebuah proyek Django baru**

Saya membuat direktori project baru bernama `topcorner-shop`. Membuat virtual environment dan bekerja di dalamnya untuk mengisolasi project saat ini dengan dependencies projek lainnya. Membuat berkas `requirements.txt`, dan menginstall dependencies yang diperlukan sesuai dengan yang ada pada `requirements.txt`. Membuat project Django bernama `topcorner_shop` dan mengatur konfigurasi environment variable. Saya membuat file `.env` dan `.env.prod` untuk konfigurasi production yang berisi kredensial database. Saya mengatur `SCHEMA=tugas_individu` untuk project ini. Lalu, modifikasi `settings.py` untuk menerapkan konfigurasi yang ada. 

- [x] **Membuat aplikasi dengan nama main pada proyek tersebut**

Saya membuat aplikasi `main` dalam project `topcorner-shop` dengan menjalankan perintah `python manage.py startapp main`. Lalu menambahkan main ke dalam `INSTALLED_APPS` pada `settings.py`.

- [x] **Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**

Konfigurasi routing URL project dilakukan dengan memodifikasi `urls.py` pada direktori project `topcorner-shop`. Menambahkan `path('', include('main.urls')),` agar aplikasi `main` dapat diakses.

- [x] **Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib**

Modifikasi berkas `models.py` dalam aplikasi `main`. Buat model `Product` yang akan merepresentasikan tabel di database. Implementasikan attribute wajib yang ditentukan pada tugas dengan tambahan attribute `stock`, `brand`, `rating`, `created_at` untuk memperlengkap fungsionalitas aplikasi nantinya. Seluruh attribute ini akan menjadi kolom pada tabel di database. Lakukan migrasi model dengan menjalankan perintah `python manage.py makemigrations`. Lalu terapakan migrasi ke dalam database lokal dengan perintah `python manage.py migrate`.

- [x] **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu**

Saya membuat fungsi `show_main` di `views.py` yang akan mengirimkan context berisi:
```
context = {
        'title': 'Topcorner Shop',
        'name': 'Kadek Chandra Rasmi',
        'npm': '2406426473',
        'class': 'PBP E',
        'products': products,
    }
```
Saya menambahkan npm dan products untuk coba ditampilkan. Fungsi `show_main` akan dipanggil dan me-render tampilan pada template `main.html`.

Pada `main.html` dalam direktori `templates` pada app `main`, gunakan struktur kode Django untuk menampilkan data dengan menggunakan `{{ }}`. Variable dengan kurung kurawal ganda tersebut akan diganti dengan nilai yang sesuai berdasarkan `context` yang telah didefinisikan sebelumnya di `views.py`.

- [x] **Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`**

Saya membuat file `urls.py` di dalam aplikasi main. Import fungsi `show_main` dan konfigurasi urlpatterns untuk memanggil view `show_main` seperti ini:
```
urlpatterns = [
    path('', show_main, name='show_main'),
]
```
sehingga saar url `http://localhost:8000/` atau `https://kadek-chandra-topcornershop.pbp.cs.ui.ac.id/` diakses, urlpatterns akan dicocokkan di tinggak project dan app. Jika cocok, akan menjalankan `show_main` yang akan mencari template `main.html`, memasukkan data context ke dalamnya dan mengirim balik ke browser.

- [x] **Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**

Akses halaman PWS dan login ke dalamnya. Create new project dengan nama project `topcornershop`. Pada tab Environs, buka raw editor dan isi dengan konten pada `.env.prod` yang sudah dibuat sebelumnya untuk konfigurasi production. Tambahkan URL `kadek-chandra-topcornershop.pbp.cs.ui.ac.id` pada `ALLOWED_HOSTS` agar project Django dapat diakses melalui URL deployment PWS. Lakukan git add, commit, dan push. Lalu lakukan project command pada pws. Jika telah berhasil, buka URL deployment dan project django telah berjalan. 

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img width="2302" height="1388" alt="Bagan" src="https://github.com/user-attachments/assets/e7fb4c1f-6cbf-4cdd-952c-0ede95f0e109" />

Alur request dan response pada Django :
1. Client mengakses URL dan mengirimkan `HTTP Request` ke server Django
2. `urls.py` (Routing) memeriksa apakah URL yang diminta sesuai dengan pola yang ada. Jika pola cocok, teruskan ke `views.py`. Jika tida ada pola yang cocok, kembalikan error `404 Not Found`.
3. `views.py` berperan sebagai penghubung antara request, model, dan template. 
4. Jika view membutuhkan data dari database, dia akan memanggil `models.py` untuk read/write data.
5. View akan merender template HTML dengan data dari model. 
6. Hasil render template akan menjadi HTTP Response dalam bentuk HTML. HTML ini dikirim kembali ke browser user untuk ditampilkan.

### Jelaskan peran settings.py dalam proyek Django!

`settings.py` berperan sebagai pusat konfigurasi project Django, berisi pengaturan seperti database, installed apps, middleware, template, static files, secret key, dan konfigurasi environment lainnya. Semua komponen Django berjalan mengikuti pengaturan yang diinginkan sesuai dengan isi dari `settings.py`.

### Bagaimana cara kerja migrasi database di Django?

Migrasi database adalah cara Django mengubah struktur tabel sesuai dengan models. Tahap pertama dilakukan `makemigrations` untuk membuat file migrasi berdasarkan perubahan di `models.py`. Lalu, dilakukan `migrate` untuk menerapkan migrasi ke database sehingga tabel dibuat/diubah sesuai dengan model yang diinginkan. 

### Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Penggunakan framework Django cocok digunakan untuk pengenalan pemrograman berbasis platform karena sytnaxnya yang mudah, yaitu menggunakan bahasa `Python` yang sudah kami pelajari sebelumnya. Selain itu, konsep MVT pada Django sangat terstruktur dan mudah dipahami sehingga memudahkan pembelajaran. Django juga telah digunakan secara luas sehingga source untuk belajar mudah ditemukan. Django juga menyediakan banyak fitur bawaan seperti authentication, admin, dan lainnya. Fitur-fitur ini mempermudah pengembangan aplikasi, terutama bagi pemula.

### Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tutorial 1 sebelumnya sudah sangat baik. Tidak ada kendala dan instruksi tutorial juga sudah sangat baik. Terima kasih kakak asdos!!

</details>

<details>
<summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan sebagai proses yang menjadi jembatan antara data pada server dengan kebutuhan informasi di sisi client. Tanpa mekanisme data delivery, aplikasi di sisi pengguna tidak akan bisa mendapatkan informasi/data yang disimpan di backend.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
XML dan JSON adalah format untuk data delivery. XML (eXtensible Markup Language) menggunakan struktur berbasis tag mirip HTML. Data dibungkus dengan tag pembuka dan penutup sehingga bentuknya hierarkis dan fleksibel. Namun, kelemahannya adalah ukuran file yang lebih besar karena banyaknya tag, dan parsing data bisa lebih berat. Sedangkan JSON (JavaScript Object Notation) menggunakan struktur pasangan key-value yang ringkas dan sederhana. JSON berbentuk objek dan array, sehingga lebih mudah dibaca manusia dan langsung kompatibel dengan JavaScript serta banyak bahasa pemrograman modern. JSON tidak membutuhkan tag berulang, sehingga ukuran data lebih kecil dan proses parsing lebih cepat. XML unggul pada validasi data yang ketat, sementara JSON unggul pada formatnya yang sederhana dan cepat. 

Menurut saya JSON lebih unggul dan memang terbukti JSON lebih populer digunakan. JSON lebih ringkas, mudah dipahami, parsing lebih cepat, dan sangat natural digunakan di ekosistem web modern. Hampir semua API RESTful saat ini menggunakan JSON sebagai format default, sementara XML mulai jarang dipakai kecuali pada sistem lama atau kebutuhan khusus. 

### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Dalam Django, setiap form yang kita buat bertujuan untuk menerima input dari pengguna. Namun, data yang dimasukkan tidak selalu benar atau sesuai aturan. Bisa saja pengguna lupa mengisi data yang wajib diisi, memasukkan teks pada field angka, atau memilih opsi yang tidak tersedia. Di sinilah fungsi is_valid() berguna. 

Method is_valid() digunakan untuk memeriksa apakah data yang dikirim melalui form memenuhi semua aturan validasi yang sudah ditentukan oleh field dalam form maupun validasi tambahan yang kita buat. Ketika dipanggil, Django akan menjalankan proses pemeriksaan untuk setiap field. Jika semua data valid, maka is_valid() mengembalikan True dan data tersebut akan disimpan ke dalam form.cleaned_data, siap digunakan atau disimpan ke database. Namun, jika ada data yang tidak valid, is_valid() mengembalikan False dan Django otomatis menyediakan informasi error melalui form.errors, sehingga kita bisa menampilkan pesan kesalahan kepada pengguna. Tanpa validasi ini, aplikasi bisa menerima data yang salah atau bahkan berbahaya, yang pada akhirnya dapat menimbulkan error, kerusakan data, atau celah keamanan.

### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Ketika kita membuat form di Django, dibutuhkan penggunaan csrf_token. Token ini merupakan mekanisme perlindungan terhadap serangan yang dikenal sebagai CSRF atau Cross-Site Request Forgery. Serangan ini terjadi ketika seorang penyerang membuat sebuah halaman berbahaya yang diam-diam mengirim permintaan ke situs yang sedang kita gunakan, dengan memanfaatkan fakta bahwa browser korban masih menyimpan cookie autentikasi. Misalnya, tanpa disadari korban bisa saja diarahkan untuk melakukan perubahan password, mengirim data, atau bahkan melakukan transaksi, hanya karena ia sedang login di situs tersebut.

Untuk mencegah hal itu, Django menyisipkan csrf_token ke dalam setiap form. Token ini bersifat unik untuk setiap sesi pengguna, sehingga server bisa memverifikasi bahwa permintaan yang masuk benar-benar berasal dari halaman sah, bukan dari sumber asing. Dengan kata lain, csrf_token bertindak sebagai tanda keamanan yang membuktikan bahwa form benar-benar dikirim dari aplikasi kita sendiri.

Jika kita tidak menambahkan csrf_token, maka form yang menggunakan metode POST akan sangat rentan dieksploitasi. Penyerang dapat dengan mudah membuat permintaan palsu yang seolah-olah sah, dan server tidak punya cara untuk membedakan mana permintaan asli dan mana yang palsu.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- [x] Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1
- [x] Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek
- [x] Membuat halaman form untuk menambahkan objek model pada app sebelumnya
- [x] Membuat halaman yang menampilkan detail dari setiap data objek model
- [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Secara keseluruhan aman dan berjalan lancar. Mungkin jika ada sesi penjelasan dari asdos, lebih menunjukkan hasil akhir yang menjadi ekspektasi di tutorial tersebut atau mention hal hal tricky yang sering menjadi kesalahan.
</details>
