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
Berikut langkah-langkah yang saya lakukan untuk mengimplementasikan checklist yang ada:
1. Membuat form input data product. Buat berkas `forms.py` pada direktori `main` yang akan digunakan untuk membuat struktur form. Buat object ProductForm dengan fields yang berisi attribute dari model Product. 
2. Pada views.py di direktori `main`.  Buat function untuk menambahkan produk baru dan untuk menampilkan product, yaitu function `create_product`, `show_product`, `show_product_xml`, `show_product_json`, `show_product_xml_by_id`, `show_product_json_by_id`. 
3. Pada urls.py di direktori main. import seluruh function yang sudah kita buat di views.py sebelumnya. Lalu, set url path ke dalam variable urlpatterns menjadi seperti ini:
```
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', crate_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_products_xml, name='show_products_xml'),
    path('json/', show_products_json, name='show_products_json'),
    path('xml/<str:id>/', show_product_xml_by_id, name='show_product_xml_by_id'),
    path('json/<str:id>/', show_product_json_by_id, name='show_product_json_by_id'),
]

```
4. Update berkas main.html. extend `base.html` sebagai template dari keseluruhan page hmtl kita. Gunakan block content dan tambahkan elemen seperti button dan cetak daftar product jika ada data product. Saya membuat hyperlink pada nama produk, sehingga jika diklik akan mengarahkan ke halaman detail produk tersebut.

`<h2><a href="{% url 'main:show_product' product.id %}">{{ product.name }}</a></h2>`

6. Buat berkas baru dengan nama `create_product.html` pada direktori `main/templates` sebagai tampilan dari form yang sudah dibuat sebelumnya. Object form Django ditampilkan dalam bentuk tabel sehingga nantinya user bisa memberikan inputan untuk dikirim ke server menggunakan method POST. Digunakan pula `{% csrf_token %} ` sebagai token keamanan yang mencegah serangan CSRF. Tambahkan button submit dengan text `Add Product` 
7. Karena kita menggunakan csrf token, buka `settings.py` pada root project dan tambahkan url deployment pws pada `CSRF_TRUSTED_ORIGINS` seperti ini:
```
CSRF_TRUSTED_ORIGINS = [
    "https://kadek-chandra-topcornershop.pbp.cs.ui.ac.id"
]
```
7. Buat berkas baru dengan nama `product_detail.html` pada direktori `main/templates`. Gunakan block content dan extende `base.html`. Tampilkan detail informasi suatu product sesuai dengan parameter berupa id product yang digunakan pada url nya. Attribute produk ditampilkan menggunakan kurung kurawal ganda. contoh :  `{{ product.desciption }}`
8. Jalankan project Django dan buka pada http://localhost:8000/
9. Saya juga mencoba mengakses 4 URL berikut menggunakan Postman:  
- Mengakses `http://localhost:8000/xml/`
<img width="1987" height="1383" alt="image" src="https://github.com/user-attachments/assets/30987bf3-6ac4-4495-8f18-04b7041d1c33" />
- Mengakses `http://localhost:8000/json/`
<img width="2019" height="1343" alt="image" src="https://github.com/user-attachments/assets/a2fbf69e-053c-44b8-a087-223c41ed664d" />
- Mengakses `http://localhost:8000/xml/fade12d1-b255-466b-88c6-ff10dc8b673e/`
<img width="2007" height="1016" alt="image" src="https://github.com/user-attachments/assets/3a02c85a-1fdf-46c4-b73a-eed91115c8c0" />
- Mengakses `http://localhost:8000/json/fade12d1-b255-466b-88c6-ff10dc8b673e/`
<img width="1994" height="1030" alt="image" src="https://github.com/user-attachments/assets/5cc566dc-e2cf-446f-b8f9-c5d34bc0b870" />

### Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Secara keseluruhan aman dan berjalan lancar. Mungkin jika ada sesi penjelasan dari asdos, lebih menunjukkan hasil akhir yang menjadi ekspektasi di tutorial tersebut atau mention hal hal tricky yang sering menjadi kesalahan.
</details>

<details>
<summary>Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django</summary>

### Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya
Django AuthenticationForm merupakan komponen bawaan Django yang terdapat dalam modul `django.contrib.auth.forms.AuthenticationForm`. Form ini secara khusus dirancang untuk menangani proses autentikasi pengguna. Menyederhanakan implementasi sistem login dengan menyediakan validasi otomatis untuk username dan password yang terintegrasi langsung dengan backend autentikasi Django.

Kelebihan dari Django AuthenticationForm adalah kemudahan pengimplementasiannya, dengan keamanan bawaan (seperti hashing password, protection terhadap serangan brute force). Namun, form ini memiliki keterbatasan dalam fleksibilitas karena hanya mendukung field standar username-password dan ketergantungan pada model User bawaan Django, sehingga kurang cocok untuk skenario autentikasi kompleks seperti login dengan email, OTP, atau Multi-Factor Authentication.

### Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Authentikasi -> proses verifikasi identitas pengguna/siapa pengguna itu. Seperti ketika seseorang login menggunakan username dan password. Pada penerapannya di Django, proses ini ditangani oleh modul `django.contrib.auth` yang menyediakan fungsi seperti `authenticate()` untuk memvalidasi kredensial dan `login()` untuk membuat session pengguna. 

Sedangkan Otorisasi -> mengatur hak akses pengguna/apa yang boleh dilakukan oleh seorang pengguna. Pada Django diimplementasikan seperti pada decoration `@login_required` untuk membatasi akses laman tersebut hanya kepada pengguna yang telah login. Selain itu ada `@permission_required` untuk izin akses yang spesifik, serta sistem Group/Permission untuk kontrol yang lebih terstruktur. 


### Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Cookies disimpan sepenuhnya di client-side (browser), sehingga lebih ringan dan mudah diimplementasikan tanpa beban server. Cocok untuk data non-sensitif. Namun, kapasitasnya terbatas, rentan terhadap pencurian data jika tidak diamankan, dan dapat dihapus atau dinonaktifkan oleh pengguna kapan saja.

Session menyimpan data utama di server, dengan hanya ID session yang disimpan di cookie client. Session jauh lebih aman, cocok untuk informasi yang sensitif karena data tidak dapat diakses atau diubah langsung oleh client. Session juga mampu menangani data yang lebih besar dan kompleks. Kelemahannya adalah membutuhkan penyimpanan server yang dapat memengaruhi performa dan memerlukan prosedur yang lebih rumit, serta membutuhkan sinkronisasi antar server juga pada lingkungan yang lebih besar.


### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman secara default. Terdapat risiko yang harus diwaspadai, diantaranya: Cross-Site Scripting (XSS) dimana penyerang dapat mencuri cookies melalui script berbahaya. Cross-Site Request Forgery (CSRF) yang memanfaatkan cookies session untuk melakukan aksi tidak sah, serta pencurian data melalui jaringan yang tidak aman terutama jika tidak menggunakan HTTPS.

Django menangani berbagai risiko ini melalui beberapa lapisan perlindungan. Untuk mencegah CSRF, Django menyertakan `csrf_token` yang wajib pada setiap form submission. Pengaturan keamanan cookies seperti `HttpOnly flag` mencegah akses JavaScript terhadap cookies, `Secure flag` memastikan cookies hanya dikirim melalui HTTPS, dan `SameSite` attribute membatasi pengiriman cookies lintas situs. Selain itu, Django hanya menyimpan session ID di cookie sementara data sensitif disimpan di server, serta menyediakan signed cookies yang dapat mendeteksi jika data diubah oleh pihak tidak berwenang.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
Berikut langkah-langkah yang saya lakukan untuk mengimplementasikan checklist yang ada:
1. Membuat Form Registrasi yang diawali dengan membuat fungsi `register`, `login_user`, `logout_user` pada `views.py` dengan menggunakan `AuthenticationForm` dan `UserCreationForm`.
2. Membuat template `register.html`, `login.html`. Tampilkan form sebagai table dan gunakan `{% csrf_token %}` untuk menjaga keamanan data form. Pada `main.html`, tambahkan pula button `logout`.
3. Tambahkan path url untuk mengakses halaman registrasi, login, dan logout pada `urlpatterns`. Sehingga halaman registrasi dapat diakses melalui `.../register/`, halaman login dapat diakses melalui `.../login/`, dan logout pada `.../logout/`.
4. Setelah membuat authentikasi, set retriksi pada halaman utama dan detail produk. Sehingga akses dibatasi kepada pengguna yang sudah login saja(terautentikasi). Restriksi ini dilakukan dengan menambahkan decorator `login required` :
```
@login_required(login_url='/login')
def show_main(request):
```
```
@login_required(login_url='/login')
def show_product(request, id):
```
5. Set cookie bernama `last_login` pada saat user baru saja login. Simpan informasi `last_login` ini dan tampilkan pada `main.html`. Saya juga menghapus cookie jika pengguna telah keluar/logout.
6. Saya juga melakukan test terhadap sistem autentikasi yang telah dibangun dengan mencoba membuat 2 akun pengguna dan masing-masing 3 dummy data. 
6. Menghubungkan model `Product` dengan `User` dengan hubungan `one-to-many relationship` dimana seorang user dapat membuat/memposting banyak product. Tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)` pada class model `Product` dan lakukan migration.
7. Tambahkan fitur filter sehingga dapat menampilkan keseluruhan item atau hanya item yang dibuat oleh pengguna itu saja. 
8. Tampilkan informasi pengguna berupa `username` pada halaman utama. Tampilkan pula `username` pengguna yang membuat suatu produk pada halaman detail produk.
9. Saya juga mencoba menggunakan `selenium` untuk menjalankan functional test di Django. Saya membuat suatu class `FootballShopFunctionalTest` yang berisi fungsi-fungsi untuk menguji fungsionalitas dari fitur yang saya buat. 
10. Terakhir, saya melakukan `push` ke github dan pws. 


</details>



<details>
<summary>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</summary>

### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
CSS selector memiliki urutan prioritas tertentu ketika beberapa selector menargetkan elemen yang sama. Urutan prioritas dari tertinggi ke terendah adalah:
1. style dengan deklarasi `!important`
2. `Inline styles`, yaitu CSS yang ditulis langsung pada atribut style elemen HTML
3. `ID selectors` , yaitu selector yang menggunakan ID (#id)
4. `Class selectors, Attribute selectors, dan Pseudo-classes` : Selector seperti `.class`, `[type="text"]`, `:hover`
5. `Element selectors dan Pseudo-elements` : Selector seperti `div`, `p`, `::before`

### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design memastikan bahwa sebuah website dapat menyesuaikan tampilannya secara otomatis sesuai dengan ukuran layar perangkat yang digunakan, baik itu komputer desktop, tablet, atau smartphone. Konsep ini menjadi sangat penting karena kebanyakan orang sekarang mengakses aplikasi/website melalui berbagai gadget mereka, terutama ponsel. 

Berikut adalah contoh website yang telah menerapkan responsive design:
https://www.netflix.com/id-en/

[Netflix Desktop View]
<img width="1500" alt="Screenshot 2025-10-01 103152" src="https://github.com/user-attachments/assets/88626bab-7fbe-4e05-b273-43ed5d56b817" />

[Netflix Mobile View]
<img height="800" alt="Screenshot 2025-10-01 103546" src="https://github.com/user-attachments/assets/a0420496-c34f-44d5-97e5-a70f2d73cc95" />

Bandingkan dengan website Aren:
https://aren.cs.ui.ac.id/

[Aren Desktop View]
<img width="1500" alt="Screenshot 2025-09-29 143257" src="https://github.com/user-attachments/assets/6b6cf966-7701-4948-8b1e-3c7bee43d533" />

[Aren Mobile View]
![aren-mobile](https://github.com/user-attachments/assets/6d6421f1-15dc-45ae-b30b-6fe16f19b561)

Dapat dilihat bahwa pada website Netfilx, tampilan desktop dan mobile berbeda. Ukuran text dan background imagenya telah disesuaikan. Sedangkan pada aren, tampilannya tidak responsive. Jika dibuka pada mobile, tampilannya tetap tampilan desktop dan ini sangat mengurangi kenyamanan pengguna karena text terlalu kecil dan sulit menavigasikan website. 

Selain untuk kenyamanan pengguna, responsive design juga berpengaruh pada peringkat website di mesin pencari seperti Google. Google sendiri secara terbuka menyatakan bahwa mereka memberikan nilai lebih tinggi pada website yang ramah untuk perangkat mobile. 

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
`Padding` adalah ruang di antara `content` dan `border`. Sedangkan `Border` adalah garis yang mengelilingi padding + content. Lalu, `Margin` adalah ruang di luar border yang memisahkan elemen satu sama lain. 

Misal kita memiliki suatu div  dengan `class="card"`. Kita dapat membuat:
```
.card {
box-sizing: border-box; 
width: 300px;
padding: 16px; /* ruang di dalam */
border: 1px solid #ccc; /* garis pembatas */
margin: 12px auto; /* jarak luar */

}
```

card ini mengimplementasikan ketiganya dengan `padding` sebesar 16px, `margin` 12px, dan `border` 1px sebagai garis pembatas.

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
`Flexbox` merupakan One-dimensional layout (satu arah : horizontal atau vertical). Flexbox digunakan untuk menyusun elemen dalam satu baris atau kolom. Penggunaan ini ideal untuk elemen-elemen seperti Navigation bars, card layouts, form, dan lainnya.

Sedangkan `Grid Layout` merupakan Two-dimensional layout (baris dan kolom sekaligus). Grid digunakan untuk layout kompleks dengan struktur grid. Grid ini akan sangat berguna untuk digunakan pada halaman seperti dashboard, atau gallery.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Cara saya mengimplementasikan checklist yang ada, yaitu dengan:
1. Menambahkan Tailwind ke dalam project menggunakan CDN. Menambahkan `<script src="https://cdn.tailwindcss.com"></script>` pada header `base.html`
2. Menambahkan fitur `edit` dan `delete` untuk produk yang dibuat oleh user itu sendiri. Saya membuat function `edit_product` dan `delete_product` pada `views.py`. Lalu, membuat berkas HTML `edit_product.html`. Menambahkan path pada `urls.py`. 
3. Terakhir saya melakukan styling terhadap seluruh page yang ada dengan menerapkan Tailwind CSS. Dimulai dari pembuatan `navbar`. Lalu saya juga membuat `global.css`, menambahkan beberapa image yang ingin sama tampilkan pada website saya, dan membuat favicon. Untuk design card product, saya membuat component card pada `card_product.html`. Implementasikan card product pada `main.html`. Saya juga membuat agar tampilan website responsive di berbagai ukuran perangkat. 

</details>
