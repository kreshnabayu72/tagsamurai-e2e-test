---
id: TC-GS-FILEMGR-E2E-002-isi-sel-tabel-utama-format-size-nama-user-dan-link
title: "Isi Sel Tabel Utama: File Format, Nama User, Format Size, Nama Panjang, dan Link File Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-03
  - TC-GS-FILEMGR-04
  - TC-GS-FILEMGR-05
  - TC-GS-FILEMGR-06
  - TC-GS-FILEMGR-07
  - TC-GS-FILEMGR-08
coverage:
  web: automated
---

# Isi Sel Tabel Utama: File Format, Nama User, Format Size, Nama Panjang, dan Link File Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2, 33 file aktif, dengan baris yang dipakai: F01 `budi-avatar.jpg` (JPG, Budi Santoso, 2.516.582 byte), F02 `siti-profile.png` (PNG, Uploaded By System), F03 `alex-photo.jpeg` (JPEG, Alexander Graham Bell, 524.288 byte), F04 `dewi-kartika.jpg` (1.024 byte), F05 `rudi-hartono.png` (1.310.720 byte), F06 `big-banner.png` (1.610.612.736 byte), F07 `maya-wijaya.jpg` (1.048.576 byte), F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` (Upload Date 01/08/26 07:30). File fisik `budi-avatar.jpg` tersedia untuk dibuka dari link File Name.
- Data Dinamis: D06 `boundary-size-{runId}-002.jpg` (JPG, 1.048.575 byte, aktif) di-seed lewat fixture BE di hook `before` dan dihapus lewat API di hook `after`; menambah 1 baris sehingga tabel memuat 34 baris selama spec berjalan. Nama bersuffix agar kata kunci Search tidak cocok dengan data spec lain.
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE untuk Tabel A2 dan D06 (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); membaca warna teks terhitung (computed style), ring fokus, dan jumlah tab browser; mengirim tombol Tab dan Enter.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-03: Tampilan kolom File Format huruf kapital dari ekstensi

1. Buka Global Settings > File Manager dari sidebar
2. Baca nilai kolom File Format untuk `budi-avatar.jpg`, `siti-profile.png`, dan `alex-photo.jpeg`
3. Verifikasi `budi-avatar.jpg` menampilkan `JPG`
4. Verifikasi `siti-profile.png` menampilkan `PNG`
5. Verifikasi `alex-photo.jpeg` menampilkan `JPEG` sebagai nilai terpisah dari `JPG`

### TC-GS-FILEMGR-04: Tampilan nama user pada kolom User Name dan Uploaded By beserta tooltip nama lengkap

6. Baca nilai kolom User Name dan Uploaded By pada baris `alex-photo.jpeg`
7. Verifikasi User Name `alex-photo.jpeg` tampil sebagai teks polos `Alexander G`
8. Arahkan kursor ke nilai User Name `alex-photo.jpeg`
9. Verifikasi tooltip `Alexander Graham Bell`
10. Verifikasi Uploaded By `alex-photo.jpeg` tampil `Alexander G`
11. Arahkan kursor ke nilai Uploaded By `alex-photo.jpeg`
12. Verifikasi tooltip `Alexander Graham Bell`
13. Baca nilai Uploaded By pada baris `siti-profile.png`
14. Verifikasi Uploaded By `siti-profile.png` tampil `System` apa adanya

### TC-GS-FILEMGR-05: Tampilan kolom Size dengan satuan otomatis KB/MB/GB, satu desimal, pembulatan half-up

15. Baca nilai kolom Size pada baris `dewi-kartika.jpg`, `alex-photo.jpeg`, `maya-wijaya.jpg`, `rudi-hartono.png`, `budi-avatar.jpg`, dan `big-banner.png`
16. Verifikasi `dewi-kartika.jpg` menampilkan `1.0 KB`
17. Verifikasi `alex-photo.jpeg` menampilkan `512.0 KB`
18. Verifikasi `maya-wijaya.jpg` menampilkan `1.0 MB` (satuan naik pada 1024 KB)
19. Verifikasi `rudi-hartono.png` menampilkan `1.3 MB` (1.25 MB dibulatkan half-up)
20. Verifikasi `budi-avatar.jpg` menampilkan `2.4 MB`
21. Verifikasi `big-banner.png` menampilkan `1.5 GB`

### TC-GS-FILEMGR-06: Tampilan Size untuk nilai yang membulat tepat ke batas 1024 satuan

22. Ketik Search `boundary-size-{runId}-002`, tekan Enter
23. Baca nilai kolom Size baris `boundary-size-{runId}-002.jpg`
24. Verifikasi Size `boundary-size-{runId}-002.jpg` tampil `1.0 MB` (satuan ditentukan setelah pembulatan)
25. Verifikasi nilai `1024.0 KB` tidak tampil
26. Klik `(←)` pada kotak Search

### TC-GS-FILEMGR-07: Nama file panjang di kolom File Name tampil utuh tanpa pemotongan

27. Urutkan kolom Upload Date dengan Oldest First
28. Pindah ke halaman 3 pada Pagination sampai baris `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` terlihat
29. Baca teks kolom File Name pada baris itu
30. Verifikasi nama file tampil utuh `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` tanpa `..`
31. Arahkan kursor ke nama file itu
32. Verifikasi tidak ada tooltip pemotongan
33. Verifikasi lebar kolom File Name mengikuti konten tanpa batas lebar buatan
34. Verifikasi tinggi baris tabel tetap satu baris
35. Buka ulang Global Settings > File Manager dari sidebar sehingga sort kembali ke urutan default

### TC-GS-FILEMGR-08: Hover dan fokus keyboard pada tautan File Name

36. Arahkan kursor ke teks `budi-avatar.jpg` di kolom File Name
37. Verifikasi warna teks berubah ke warna primary Global Settings (hitam)
38. Verifikasi tidak ada garis bawah pada teks saat hover
39. Pindahkan kursor menjauh dari tautan
40. Tekan Tab sampai tautan `budi-avatar.jpg` menerima fokus
41. Verifikasi ring fokus tampil pada tautan `budi-avatar.jpg`
42. Tekan Enter
43. Verifikasi file `budi-avatar.jpg` terbuka di satu tab browser baru
44. Verifikasi tidak ada dialog atau modal yang tampil
45. Verifikasi tab asal tetap di Global Settings > File Manager tanpa perubahan
46. Tutup tab browser baru dan kembali ke tab asal

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-06 (Search) dan TC-07 (sort) ditaruh sebelum TC-08 yang membuka tab baru; TC-08 terakhir karena mengubah fokus dan konteks tab. Urutan TC-03 sampai TC-05 mengikuti sumber.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 26 (mengosongkan Search lewat `(←)`), langkah 28 (pindah ke halaman 3 supaya baris F08 terlihat), langkah 35 (buka ulang dari sidebar untuk mereset sort), langkah 46 (menutup tab baru).
- Langkah 22 memakai kata kunci bersuffix `boundary-size-{runId}-002` (TC sumber memakai `boundary-size`); langkah 2 TC-06 menulis "Klik ikon Search, ketik ..., tekan Enter" dan di sini ditulis sebagai satu langkah atomik (8b butir 9).
- Langkah 7 dan 10 memakai bentuk `[First Name] [Last Initial]` sesuai Expected TC-04.
- Langkah 28: sort Oldest First menempatkan 25 file `staff-photo-` (Upload Date 01/07/26 sampai 25/07/26) sebelum F08 (01/08/26), sehingga F08 berada di baris ke-26 (halaman 3 pada page size 10).
- Alasan spec di atas sekitar 35 langkah (S-10): enam TC satu topik (isi sel tabel utama) pada satu dataset Pre-setup tanpa mengubah data; langkah membengkak karena `Verifikasi` dipecah per klausa (S-01), bukan karena alur yang bergantung. Tiap blok TC membaca sel yang berbeda dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Tidak ada kelas harness selain screening/fungsional; TC-08 terakhir karena membuka tab baru.
- Temuan untuk QA:
  - TC-07 langkah 2 mengurutkan Upload Date Oldest First "untuk mencari baris" F08, tetapi pada Tabel A2 F08 sudah berada di baris ke-8 urutan default (halaman 1); sort Oldest First memindahkannya ke halaman 3. Spec tetap mengikuti TC dan menambah navigasi halaman 3.
  - TC-06 tidak menyebut Upload Date `boundary-size.jpg` (D06) sehingga posisi baris pada tabel default tidak diketahui; spec mencarinya lewat Search.
  - Mekanisme seeding Tabel A2 dan D06 ("fixture BE") tidak disebut di TC, PRD, atau LLD; dicatat di Prerequisites sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
