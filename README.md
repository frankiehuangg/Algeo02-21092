# Project Name
> Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri
> Aplikasi Nilai **Eigen** dan **EigenFace** pada Pengenalan Wajah (Face Recognition)
> ***link video***

## Daftar isi
* [Tentang Tubes](#tentang-tubes)
* [Fitur](#fitur)
* [Screenshots](#screenshots)
* [Requirement](#requirement)
* [Setup](#setup)
* [Usage](#usage)
* [Status Proyek](#status-proyek)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)


## Tentang Tubes
- Teknologi *face recognition* sederhana menggunakan nilai eigen dan EigenFace
- Penggunaan EigenFace memungkinkan pencocokan wajah tanpa membutuhkan fitur-fitur wajah, serta relatif mudah diimplementasikan
- Penggunaan program face recognition dengan EigenFace membutuhkan pencahayaan yang baik dan posisi wajah yang tepat di tengah gambar


## Fitur
Program dapat menjalankan fitur-fitur:
- Face recognition sebuah file gambar
- Face recognition melalui kamera
**Perlu diperhatikan bahwa dataset pengenalan wajah perlu disediakan sendiri**


## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Requirement
- Python    3.11.0
- Numpy     1.23.4
- OpenCv    4.6.0.66
- Tcl/Tk    8.6


## Setup
Pastikan telah ter-instal python dan library-library yang diperlukan pada [Requirement](#requirement) untuk instalasi Python dapat diikuti langkah-langkah ini: [Instalasi Python](https://www.python.org/about/gettingstarted/)


## Usage
<!-- How does one go about using it? -->
<!-- Provide various use cases and code examples here. -->

## Status Proyek
Proyek telah: _selesai_.
*Tidak terdapat rencana dalam jangka waktu dekat untuk perubahan, penambahan, maupun optimisasi program dalam jangka waktu dekat.*


## Room for Improvement
Room for improvement:
- Algoritma QR untuk mencari nilai eigen dapat dioptimisasi dengan mengkonversi matriks masukan ke dalam bentuk *upper hessenberg matrix*, yang dapat mengurangi jumlah iterasi untuk mencapai kekonvergenan nilai eigen.
- Dapat ditambahkan modul untuk menyimpan data-data pre-processing dataset untuk mempercepat proses pre-process untuk dataset yang sama pada saat program dijalankan selanjutnya.


## Acknowledgements
- Tugas ini dipelopori oleh mata kuliah IF2123 Teknik Informatika Institut Teknologi Bandung, yang telah diorganisasikan dengan baik oleh tim pengajar dan asisten-asisten IF2123 - 2022
- Instruksi dan langkah-langkah pengerjaan dapat dilihat pada [Spesifikasi Tubes 2 Algeo 2022](https://docs.google.com/document/d/1-5JH-SmcUdFCGRMl5z_C9s9-SexH68UX/)
- Proyek ini didasari oleh metode face recognition dengan metode EigenFace melalui [ML | Face Recognition Using Eigenfaces (PCA Algorithm)](https://www.geeksforgeeks.org/ml-face-recognition-using-eigenfaces-pca-algorithm/).
- Template README oleh [@flynerdpl](https://www.flynerd.pl/): [README](https://github.com/ritaly/README-cheatsheet)
- Terima kasih kepada sumber-sumber referensi dan metode sebagai dasar yang telah dicantumkan pada bagian-bagian yang bersangkutan dalam source code


