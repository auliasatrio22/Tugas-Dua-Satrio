Link Aplikasi TodoList App: https://tugas2project.herokuapp.com/todolist/login/

Akun Dummy
1. username: satsatsatrio, pass: satrio123
2. username: satsatsatrio1, pass: satrio2206

Jawaban Pertanyaan:

Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

-> {% csrf_token %} dalam elemen form berguna untuk melindungi dari serangan siber atau menghindari beberapa link yang nantinya dapat disalahgunakan oleh orang lain.

Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

-> Untuk membuat elemen form secara manual, kita bisa menggunakan method "POST" dan menambahkan {% csrf_token %}. Selanjutnya, kita bisa menambahkan tag table dengan berisikan tr, th, td. Dengan method request.POST.get{{xxx}} bertujuan untuk mengakses input dari user.

Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

-> Submisi yang dilakukan oleh user dapat diakses melalui request.POST.get{{xxx}} atau nama input. Data tersebut akan dibandingkan lalu disesuaikan pada file models.py. Setelah dibandingkan, data tersebut akan disimpan pada database.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

-> Langkah pertama yang saya lakukan adalah menjalankan startapp todolist untuk membuat proyek todolist pada django. Lalu mendaftarkan path aplikasi todolist ini pada urls.py di project django. Kemudian, membuat class Task yang berisi:
user = models.ForeignKey(User, on_delete=models.CASCADE)
date = models.DateTimeField(auto_now_add=True)
title = models.TextField()
description = models.TextField()
Kemudian, saya menambahkan beberapa fungsi pada views.py yang berupa register, login, dan logout. Setelah itu, saya membuat todolist.html dengan menambahkan username pengguna dan membuat beberapa button untuk logout, create new task, tabel yang berisi date, title, dan description. Lalu membuat addTask.html untuk menambahkan todolist user yang berupa judul dan deskripsi todolist. Kemudian, saya mendaftarkan beberapa fungsi yang sudah dibuat kedalam path yang berada pada urls.py pada todolist app. Setelah selesai semua, saya melakukan push dan commit yang bertujuan untuk deployment ke Heroku terhadap aplikasi yang sudah saya buat sehingga nantinya dapat diakses oleh teman-teman saya melalui internet. Yang terakhir saya mencoba membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
