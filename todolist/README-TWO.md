1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. 

-> Asynchronus Programming = merupakan pemrograman yang tidak terikat pada I/O protocol. User dapat berpindah ke tugas lain atau page lain sebelum yang hal sebelumnya selesai.

-> Synchronous Programming = sedangkan pada pemrograman ini, tugas hanya dilakukan satu persatu dan hanya selesai ketika yang sebelumnya selesai atau yang satunya selesai.

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. 

-> Dalam penerapan JavaScript dan Ajax, terdapat paradigma Evenet Driven Programming yang diterapkan ketika kita ingin menghandle / menanggapi suatu action atau event pada website. Ketika user merequest sesuatu pada website, paradigma ini akan merespon hal tersebut dan menanggapinya, misal ketika kita mengeklik suatu tombol/ikon.

3. Jelaskan penerapan asynchronous programming pada AJAX.

-> Pada JavaScript, AJAX akan menerapkan konsep asynchronous programming ketika akan mengeksekusi suatu task pada program. Pada tugas ini, AJAX berpengaruh dalam pengambilan data serta ketika menanggapi suatu response dalam bentuk JSON. Ketika kita menekan tombol add pada program, maka program akan melakukan AJAX POST yang mana akan mengirim data ke server. Kemudian, data akan ditangkap dan dikirimkan ke server tanpa adanya reload pada browser. Kita hanya perlu menambahkan library JQuery pada templates todolist.html, lalu JQuery tersebut akan melakukan pemanggilan function success dan error.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

-> Hal pertama yang saya lakukan adalah dengan menambahkan beberapa function baru pada views untuk mengambil suatu data yang direpresentasikan dengan JSON. Kemudian menambahkan beberapa path di urls.py untuk function yang sudah ditambahkan pada views.py. Selanjutnya pada todolist.html saya membuat fungsi GET untuk mengambil data yang akan ditampilkan. Kemudian, saya mengubah href atau link pemetaan ketika user menekan tombol create task agar program menghandle modal yang sudah dibuat sebelumnya. Kemudian saya membuat fungsi POST pada todolist.html untuk menambahkan data dari user/pengguna.
