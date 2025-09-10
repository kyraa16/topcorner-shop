# Tugas Individu 2 : Implementasi Model-View-Template (MVT) pada Django
Kadek Chandra Rasmi | 2406426473 | PBP E

URL Deployment : https://kadek-chandra-topcornershop.pbp.cs.ui.ac.id/
 
## Jelaskan bagaimana cara kamu mengimplementasikan checklist yang ada secara step-by-step 
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

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

## Jelaskan peran settings.py dalam proyek Django!

`settings.py` berperan sebagai pusat konfigurasi project Django, berisi pengaturan seperti database, installed apps, middleware, template, static files, secret key, dan konfigurasi environment lainnya. Semua komponen Django berjalan mengikuti pengaturan yang diinginkan sesuai dengan isi dari `settings.py`. 

## Bagaimana cara kerja migrasi database di Django?

Migrasi database adalah cara Django mengubah struktur tabel sesuai dengan models. Tahap pertama dilakukan `makemigrations` untuk membuat file migrasi berdasarkan perubahan di `models.py`. Lalu, dilakukan `migrate` untuk menerapkan migrasi ke database sehingga tabel dibuat/diubah sesuai dengan model yang diinginkan. 

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Penggunakan framework Django cocok digunakan untuk pengenalan pemrograman berbasis platform karena sytnaxnya yang mudah, yaitu menggunakan bahasa `Python` yang sudah kami pelajari sebelumnya. Selain itu, konsep MVT pada Django sangat terstruktur dan mudah dipahami sehingga memudahkan pembelajaran. Django juga telah digunakan secara luas sehingga source untuk belajar mudah ditemukan. Django juga menyediakan banyak fitur bawaan seperti authentication, admin, dan lainnya. Fitur-fitur ini mempermudah pengembangan aplikasi, terutama bagi pemula.

## Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Tutorial 1 sebelumnya sudah sangat baik. Tidak ada kendala dan instruksi tutorial juga sudah sangat baik. Terima kasih kakak asdos!!
