---
id: TC-GS-FILEMGR-E2E-024-konflik-file-tidak-tersedia-aksi-baca-dan-delete
title: "Konflik File Tidak Tersedia: Buka, Download, Delete Single, dan Bulk Delete Setelah Diproses Pihak Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-53
  - TC-GS-FILEMGR-57
  - TC-GS-FILEMGR-68
  - TC-GS-FILEMGR-70
  - TC-GS-FILEMGR-85
  - TC-GS-FILEMGR-258
  - TC-GS-FILEMGR-263
coverage:
  web: automated
---

# Konflik File Tidak Tersedia: Buka, Download, Delete Single, dan Bulk Delete Setelah Diproses Pihak Lain

## Prerequisites

- Mode: FE+BE (kelas multi-konteks; pelaku lain hanya memicu perubahan state lewat sesi API, P-2).
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Pelaku lain (sesi API, tanpa sesi UI kedua, P-2; disediakan tim FE/BE): hanya memicu (a) penghapusan permanen file lewat fixture BE, (b) penghapusan user (TC-GS-FILEMGR-258), dan (c) penggantian foto profil oleh pemilik (TC-GS-FILEMGR-70). Tidak ada asersi di sesi lain.
- Data Dinamis (seeding fixture BE di hook `before`, bersuffix per run; pemilik adalah user klon milik spec, disediakan tim FE agar baris Pre-setup tidak diubah, S-06):
  - `staff-photo-01-{runId}-024.jpg` (TC-GS-FILEMGR-53), `staff-photo-02-{runId}-024.jpg` (TC-GS-FILEMGR-57), `staff-photo-03-{runId}-024.jpg` (TC-GS-FILEMGR-68), `staff-photo-04-{runId}-024.jpg` dan `staff-photo-05-{runId}-024.jpg` (TC-GS-FILEMGR-85), `staff-photo-15-{runId}-024.jpg` dan `staff-photo-16-{runId}-024.jpg` (TC-GS-FILEMGR-263): JPG, foto profil aktif.
  - `dewi-kartika-{runId}-024.jpg` (JPG, foto profil aktif milik user klon `Dewi Kartika` berdasarkan email `dewikartika+{runId}-024@qwertysystem.net`, disediakan tim FE) untuk TC-GS-FILEMGR-258.
  - `budi-avatar-{runId}-024.jpg` (JPG, foto profil aktif milik user klon `Budi Santoso`) dan `budi-new-{runId}-024.png` (file foto pengganti) untuk TC-GS-FILEMGR-70.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tercantum di TC; lihat Temuan untuk QA): penghapusan permanen file oleh proses lain (fixture BE, D-seri); penghapusan user klon beserta cascade purge dan pengamatan selesainya (polling lewat sesi API); sesi API sebagai pemilik klon untuk mengganti foto; membaca respons tab baru (respons tidak ditemukan); membaca jumlah entri Changelog File Manager per File Name (baseline dicatat di hook `before`).
- Jeda nyata: langkah 16 menunggu cascade purge dengan polling per 5 detik, batas 120 detik (batas harness, TC tidak menyebut angka).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): hapus permanen sisa file seed, hapus user klon, tutup tab tambahan.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-FILEMGR-53: Buka file yang sudah dihapus permanen

1. Ketik Search `{runId}-024`, tekan Enter
2. Verifikasi baris `staff-photo-01-{runId}-024.jpg` tampil pada tabel utama
3. [Sesi API] Hapus permanen `staff-photo-01-{runId}-024.jpg` lewat fixture BE hingga tersimpan
4. Klik teks `staff-photo-01-{runId}-024.jpg` di kolom File Name
5. Verifikasi tab browser baru terbuka dan menampilkan respons tidak ditemukan
6. Tutup tab baru dan kembali ke tab asal
7. Verifikasi tab asal tidak menampilkan toast
8. Verifikasi tab asal tidak menampilkan dialog

### TC-GS-FILEMGR-57: Download file yang sudah tidak tersedia

9. [Sesi API] Hapus permanen `staff-photo-02-{runId}-024.jpg` lewat fixture BE hingga tersimpan
10. Klik ikon `⋯` baris `staff-photo-02-{runId}-024.jpg`
11. Klik `Download`
12. Verifikasi toast info: "This file is no longer available."
13. Verifikasi tidak ada file terunduh
14. Verifikasi tabel di-refresh

### TC-GS-FILEMGR-258: Buka file milik user yang dihapus setelah halaman dimuat

15. Verifikasi baris `dewi-kartika-{runId}-024.jpg` tampil pada tabel utama
16. [Sesi API] Hapus user klon `Dewi Kartika` hingga tersimpan, lalu tunggu cascade purge selesai (polling sesi API sampai `dewi-kartika-{runId}-024.jpg` tidak ada)
17. Klik teks `dewi-kartika-{runId}-024.jpg` di kolom File Name pada tabel yang belum di-refresh
18. Verifikasi tab browser baru terbuka dan menampilkan respons tidak ditemukan
19. Tutup tab baru dan kembali ke tab asal
20. Verifikasi tab asal tidak menampilkan toast
21. Verifikasi tab asal tidak menampilkan dialog

### TC-GS-FILEMGR-68: Delete single pada file yang sudah dihapus proses lain

22. Muat ulang halaman, ketik Search `{runId}-024`, tekan Enter
23. Verifikasi baris `staff-photo-03-{runId}-024.jpg` tampil pada tabel utama
24. [Sesi API] Hapus permanen `staff-photo-03-{runId}-024.jpg` lewat fixture BE hingga tersimpan
25. Klik ikon `⋯` baris `staff-photo-03-{runId}-024.jpg`, lalu klik `Delete`
26. Klik [Delete] pada dialog
27. Verifikasi toast info: "This file is no longer available."
28. Verifikasi tabel di-refresh
29. Verifikasi baris `staff-photo-03-{runId}-024.jpg` hilang dari tabel
30. Klik ikon Changelog di toolbar, ketik Search `staff-photo-03-{runId}-024`, tekan Enter
31. Verifikasi jumlah entri Changelog untuk `staff-photo-03-{runId}-024.jpg` sama dengan baseline (tidak ada entri log baru)
32. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-85: Bulk Delete dengan sebagian file sudah dihapus proses lain

33. Centang baris `staff-photo-04-{runId}-024.jpg` dan `staff-photo-05-{runId}-024.jpg`
34. [Sesi API] Hapus permanen `staff-photo-05-{runId}-024.jpg` lewat fixture BE hingga tersimpan
35. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
36. Verifikasi toast sukses: "Success, file has been deleted. Some items were skipped."
37. Verifikasi Bulk Action Bar hilang dan seleksi kembali 0
38. Buka modal Recycle Bin, ketik Search `staff-photo-04-{runId}-024`, tekan Enter
39. Verifikasi `staff-photo-04-{runId}-024.jpg` pindah ke Recycle Bin
40. Tutup modal Recycle Bin dengan `✕` di header
41. Klik ikon Changelog di toolbar, ketik Search `staff-photo-05-{runId}-024`, tekan Enter
42. Verifikasi jumlah entri Changelog untuk `staff-photo-05-{runId}-024.jpg` sama dengan baseline (tidak ada entri log)
43. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-263: Bulk Delete saat seluruh file terseleksi sudah dihapus proses lain

44. Centang baris `staff-photo-15-{runId}-024.jpg` dan `staff-photo-16-{runId}-024.jpg`
45. [Sesi API] Hapus permanen `staff-photo-15-{runId}-024.jpg` dan `staff-photo-16-{runId}-024.jpg` lewat fixture BE hingga tersimpan
46. Klik `Bulk Action`, klik `Delete`, lalu klik [Delete] pada dialog
47. Verifikasi toast info: "This file is no longer available."
48. Verifikasi tabel di-refresh
49. Verifikasi kedua baris hilang dari tabel
50. Verifikasi tidak ada toast sukses
51. Verifikasi tidak ada toast error
52. Klik ikon Changelog di toolbar, ketik Search `staff-photo-1`, tekan Enter
53. Verifikasi jumlah entri Changelog untuk `staff-photo-15-{runId}-024.jpg` dan `staff-photo-16-{runId}-024.jpg` sama dengan baseline (tidak ada entri log baru)
54. Tutup modal Changelog dengan `✕` di header

### TC-GS-FILEMGR-70: File aktif saat dialog dibuka lalu diganti pemilik sebelum Confirm Delete

55. Ketik Search `budi-avatar-{runId}-024`, tekan Enter
56. Klik ikon `⋯` baris `budi-avatar-{runId}-024.jpg`, lalu klik `Delete`, dan biarkan dialog terbuka
57. [Sesi API] Sebagai pemilik klon `Budi Santoso`, ganti foto profil dengan `budi-new-{runId}-024.png` hingga tersimpan
58. Klik [Delete] pada dialog
59. Verifikasi toast info: "This file is no longer available."
60. Verifikasi tabel di-refresh dan `budi-avatar-{runId}-024.jpg` tidak ada di tabel utama
61. Verifikasi `budi-new-{runId}-024.png` tampil sebagai foto aktif di tabel utama
62. Buka modal Recycle Bin, ketik Search `budi-avatar-{runId}-024`, tekan Enter
63. Verifikasi `budi-avatar-{runId}-024.jpg` tampil satu kali di Recycle Bin dengan Deleted By `System`
64. Tutup modal Recycle Bin dengan `✕` di header
65. Buka Global Settings > User > Detail User Budi Santoso (klon milik spec)
66. Verifikasi foto profil Budi Santoso tetap `budi-new-{runId}-024.png` (tidak dikosongkan)

## Notes

- Mode: FE+BE. Kelas c multi-konteks. Butir P-2: pelaku lain (penghapusan permanen oleh proses lain, penghapusan user, penggantian foto oleh pemilik) hanya memicu perubahan state lewat sesi API dan tidak ada asersi di sesi lain, sesuai bagian 3 prinsip 13 pengecualian P-2. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (66 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas (konflik "file tidak tersedia" dengan pemicu sesi API), tiap blok memakai file seed sendiri yang dipicu dihapus di tengah blok, dan kegagalan satu blok (mis. pemicu fixture) tidak membuat blok lain kehilangan makna karena tidak ada data yang dipakai bersama.
- Urutan TC pada spec: 53, 57, 258, 68, 85, 263, 70. Aksi baca (buka, download) lebih dulu karena tidak mengubah data; TC-GS-FILEMGR-258 menghabisi user klon beserta file miliknya, dan TC-GS-FILEMGR-70 di akhir karena membuka modul User.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 22, 55 (Search untuk menemukan baris target), 6 dan 19 (menutup tab baru), 30, 32, 41, 43, 52, 54 (membuka dan menutup modal Changelog untuk absence log), 38 dan 40 (membuka modal Recycle Bin dan Search `staff-photo-04-{runId}-024`, lalu menutupnya, agar asersi langkah 39 dapat dieksekusi; Bulk Action Bar diverifikasi lebih dulu pada langkah 37), 62 dan 64 (membuka dan menutup Recycle Bin), 65 (navigasi ke modul User), 3, 9, 16, 24, 34, 45, 57 (pemicu sesi API, ditulis "hingga ... tersimpan").
- Asersi tambahan di luar Expected TC (S-03): langkah 2, 15, 23 (baris target tampil sebagai anchor sebelum pemicu), 50 dan 51 (TC-GS-FILEMGR-263 Expected c memuat "tidak ada toast sukses maupun toast error", dipecah per klausa).
- Absence log (TC-GS-FILEMGR-68 c, 85 c, 263 c) diasersi sebagai jumlah entri yang sama dengan baseline per File Name (keputusan D-1 pilihan B): langkah 31, 42, 53. Baseline dicatat di hook `before` (jumlah entri Changelog per File Name sebelum pemicu). Asersi ini bukan kelas g karena ada aksi nyata (Delete) di alur fungsionalnya.
- Temuan untuk QA:
  - Q-8: pemicu "dihapus permanen oleh proses lain" (TC-GS-FILEMGR-53, 57, 68, 85, 263) tidak didefinisikan di TC; spec memakai fixture BE lewat sesi API dan tanpa endpoint karangan (S-13).
  - TC-GS-FILEMGR-53 dan 258 Expected a "menampilkan respons tidak ditemukan" tidak menyebut isi halaman atau status HTTP; spec mengasersi "respons tidak ditemukan" tanpa teks.
  - TC-GS-FILEMGR-258 menyebut "Tunggu cascade purge selesai"; PRD tidak menetapkan batas atas jeda cascade purge. Spec memakai polling sesi API dengan batas harness 120 detik.
  - TC-GS-FILEMGR-70 langkah 2 menyebut "sesi lain, Budi Santoso mengganti foto lewat Global Settings > User"; spec memakai sesi API (P-2) bukan sesi UI kedua karena hasil di sesi itu tidak diasersi.
  - Q-5/Q-7: TC menargetkan baris Pre-setup (F04, F09 s.d. F13, F23, F24, F01) yang dihapus atau diubah; spec memakai file bersuffix dengan pemilik klon. Pemilik klon bernama literal belum terdaftar sebagai pengecualian S-12.
  - Post Condition semua TC bernilai `-`.
