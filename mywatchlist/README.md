Jelaskan perbedaan antara JSON, XML, dan HTML!

=> JavaScript Object Notation atau yang biasa disebut dengan JSON adalah suatu format yang memiliki fungsi untuk membaca dan menyimpan data dan informasi dari server web. Sedangkan Extensible Markup Language atau yang biasa disebut dengan XML adalah sarana untuk membuat format dan data yang digunakan di World Wide Web, intranet, dan di platform lain. XML akan lebih mengutamakan transfer data dan struktur dibanding HTML (HyperText Markup Language) yang lebih mengutamakan pada penyajian datanya dan tampilan format dari data.

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

=> Kita perlu mengirimkan data dari suatu stack ke stack lainnya untuk bisa mengembangkan suatu platform. JSON, XML, dan HTML adalah contoh-contoh yang termasuk kedalam format data yang biasanya digunakan.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

=> Step atau langkah pertama yang perlu dilakukan adalah membuat sebuah aplikasi baru bernama “mywatchlist” melalui command prompt yang telah sesuai dengan folder penyimpanan dengan mengetik "python manage.py startapp". Setelah itu, langkah berikutnya adalah memasukkan mywatchlist pada url_patterns yang bertujuan untuk menambahkan path melalui urls.py pada project_django. Lalu menambahkan variabel dan fieldnya pada models.py. Berikutnya membuat beberapa data pada file fixtures. Yang selanjutnya adalah membuat beberapa fungsi pada views.py yang saling terhubung dengan JSON, XML, dan HTML serta melakukan routing menggunakan urls.py pada mywatchlist. Setelah menambahkan unit test pada tests.py, kita dapat melakukan push dan commit.

Screenshot Postman:

![image](https://user-images.githubusercontent.com/112611041/191597003-8f1b4c08-0d3e-42a5-9ece-9d9d4c22a86f.png)

![image](https://user-images.githubusercontent.com/112611041/191597048-5cc7c514-61bf-472d-9b69-42336c2513f1.png)

![image](https://user-images.githubusercontent.com/112611041/191597065-d2273836-3c84-46ee-a000-6690e612de83.png)
