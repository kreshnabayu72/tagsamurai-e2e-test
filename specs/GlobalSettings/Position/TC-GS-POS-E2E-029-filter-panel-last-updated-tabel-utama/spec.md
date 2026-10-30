---
id: TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama
title: "Filter Panel Last Updated Tabel Position: Screening, Rentang Inklusif, Satu Hari, Clear Field, Tutup Tanpa Apply, dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-159
  - TC-GS-POS-160
  - TC-GS-POS-161
  - TC-GS-POS-162
  - TC-GS-POS-163
  - TC-GS-POS-164
coverage:
  web: automated
---

# Filter Panel Last Updated Tabel Position: Screening, Rentang Inklusif, Satu Hari, Clear Field, Tutup Tanpa Apply, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; spec tidak menguji navigasi sehingga tidak mengulang langkah buka di `## Test Steps`.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 `IT Manager`, 11 `Finance Analyst`, 12 `Warehouse Supervisor`, 13 `Customer Success Manager`, 14 `Procurement Officer`, 15 `Field Technician`, 16 `Sales Coordinator` (7 record).
- Data Dinamis (di-seed lewat API di hook `before`; nama bersuffix per run; fixture baru `Fixture.position.filterSeed029`). Hari uji disebut H. Last Updated dibuat bervariasi dalam tiga kelompok sehingga rentang tanggal batas dapat diuji:
  - Kelompok H-2 (Last Updated = H dikurangi 2 hari): `HR Business Partner {runId}-029`, `IT Support Specialist {runId}-029`, `Temporary Staff {runId}-029`.
  - Kelompok H-1 (Last Updated = H dikurangi 1 hari): `iOS Developer {runId}-029`, `Legal Counsel {runId}-029`, `Marketing Executive {runId}-029`.
  - Kelompok H (Last Updated = H, tanggal pembuatan data populasi): `Quality Assurance Analyst {runId}-029`, `Data Engineer {runId}-029`, `Office Administrator {runId}-029`, `Logistics Coordinator {runId}-029`, `Payroll Specialist {runId}-029`, `Security Officer {runId}-029`, dan `Training Coordinator {runId}-029`.
  Ke-13 Position ini adalah Data Dinamis No. 1-13; dengan 7 record Pre-setup, jumlah data total tepat 20 saat spec berjalan (2 halaman pada ukuran halaman 10), karena suite berjalan serial (`suite.md`) dan Position seed spec lain sudah dibersihkan hook `after` spec itu. Kemampuan menyetel Last Updated seed ke H-2 dan H-1 disediakan tim FE/BE (mekanismenya tidak didefinisikan di sumber modul). Tanggal Last Updated Pre-setup 10-16 tidak diketahui spec; asersi rentang dan satu hari mengenai baris kelompok bersuffix dan tidak bergantung pada baris Pre-setup. Ukuran halaman diubah ke 25 pada langkah 19 supaya seluruh hasil filter (paling banyak 20 baris) tampil pada satu halaman walau baris Pre-setup ikut masuk rentang.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-029` yang masih ada.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: pemilihan rentang tanggal pada date range picker; pembacaan nilai Start dan End yang tampil di Filter Panel dan nilai Last Updated tiap baris.
- State global: ukuran halaman diubah ke 25 (langkah 19) dan dikembalikan ke 10 (langkah 63); filter Last Updated dibersihkan dan kolom Last Updated ditampilkan kembali di langkah 58 sampai 62; hook `after` cadangan memulihkan Setup Column dan ukuran halaman ke bawaan.

## Test Steps

1. Catat nama sepuluh baris halaman 1 (ukuran halaman 10; total 20 baris, 2 halaman) sebelum uji

### TC-GS-POS-159: Screening Filter Panel tabel utama

2. Hover ikon Filter
3. Verifikasi tooltip "Filter"
4. Klik ikon Filter
5. Verifikasi ikon Filter berubah gelap saat panel terbuka
6. Verifikasi panel muncul di bawah Table Tools
7. Verifikasi panel memuat satu field dengan label "Last Updated"
8. Verifikasi field Last Updated berupa komponen date range picker
9. Verifikasi field Last Updated memuat placeholder "Select date"
10. Verifikasi tombol `[Clear Field]` tampil di kiri
11. Verifikasi tombol `[Apply]` tampil di kanan
12. Klik ikon Filter untuk menutup panel

### TC-GS-POS-160: Filter Last Updated rentang tanggal inklusif

13. Pindah ke halaman 2 pada Pagination
14. Klik ikon Filter untuk membuka panel
15. Pilih Start = H-2 dan End = H-1 pada field Last Updated
16. Klik `[Apply]` (Filter Panel tetap terbuka)
17. Klik ikon Filter untuk menutup panel
18. Verifikasi halaman aktif 1
19. Ubah ukuran halaman tabel ke 25
20. Verifikasi baris kelompok H-2 (batas awal) tampil
21. Verifikasi baris kelompok H-1 (batas akhir) tampil
22. Verifikasi tidak ada baris dengan Last Updated di luar rentang H-2 sampai H-1 (baris kelompok H tidak tampil)

### TC-GS-POS-161: Filter Last Updated satu hari (Start = End)

23. Klik ikon Filter untuk membuka panel
24. Pilih Start = H dan End = H pada field Last Updated
25. Klik `[Apply]` (Filter Panel tetap terbuka)
26. Klik ikon Filter untuk menutup panel
27. Verifikasi ketujuh baris kelompok H tampil
28. Verifikasi tidak ada baris dengan Last Updated selain H (baris kelompok H-2 dan H-1 tidak tampil)

### TC-GS-POS-162: Clear Field Filter Panel mengembalikan seluruh data

29. Klik ikon Filter untuk membuka panel
30. Pilih Start = H-1 dan End = H-1 pada field Last Updated
31. Klik `[Apply]` (Filter Panel tetap terbuka)
32. Klik `[Clear Field]`
33. Klik `[Apply]`
34. Verifikasi field Last Updated kosong kembali ke placeholder "Select date"
35. Verifikasi tabel menampilkan seluruh data (20 baris pada satu halaman)
36. Verifikasi sepuluh nama baris pertama sama dengan yang dicatat pada langkah 1
37. Klik ikon Filter untuk menutup panel

### TC-GS-POS-163: Menutup Filter Panel tanpa Apply membuang perubahan

38. Klik ikon Filter untuk membuka panel
39. Pilih rentang A: Start = H-2 dan End = H-1 pada field Last Updated
40. Klik `[Apply]` (Filter Panel tetap terbuka)
41. Ubah rentang menjadi B: Start = H dan End = H tanpa klik `[Apply]`
42. Klik ikon Filter untuk menutup panel
43. Verifikasi tabel tetap menampilkan hasil rentang A (baris kelompok H-2 dan H-1 tampil)
44. Verifikasi baris kelompok H tidak tampil
45. Klik ikon Filter untuk membuka panel kembali
46. Verifikasi panel menampilkan rentang A (Start = H-2, End = H-1)
47. Verifikasi panel tidak menampilkan rentang B

### TC-GS-POS-164: Filter tetap berlaku saat kolom Last Updated disembunyikan

48. Pilih Start = H dan End = H pada field Last Updated (panel masih terbuka dari langkah 45)
49. Klik `[Apply]` (Filter Panel tetap terbuka)
50. Klik ikon Filter untuk menutup panel
51. Buka Overlay Column Visibility, sembunyikan kolom Last Updated
52. Verifikasi tabel tetap tersaring sesuai filter (ketujuh baris kelompok H tampil)
53. Verifikasi baris kelompok H-2 dan H-1 tidak tampil
54. Tutup Overlay Column Visibility
55. Klik ikon Filter untuk membuka panel
56. Verifikasi field Last Updated tetap ada di Filter Panel
57. Verifikasi field Last Updated menampilkan nilai ter-apply (Start = H, End = H)

### Pemulihan state

58. Klik `[Clear Field]`
59. Klik `[Apply]`
60. Klik ikon Filter untuk menutup panel
61. Buka Overlay Column Visibility, tampilkan kembali kolom Last Updated
62. Tutup Overlay Column Visibility
63. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti urutan TC sumber. TC-GS-POS-164 mengubah visibilitas kolom sehingga ditaruh paling akhir; spec tidak menghapus data.
- Model Filter Panel mengikuti TC-GS-POS-160 sampai 164: panel tetap terbuka sesudah `[Apply]` dan ditutup dengan klik ikon Filter. Tiap TC membuka panel dengan klik ikon Filter (langkah 14, 23, 29, 38) dan menutupnya sesudah `[Apply]` (langkah 17, 26, 37, 42, 50). TC-GS-POS-164 melanjutkan panel yang masih terbuka dari langkah 45, sehingga langkah "Buka Filter" TC-GS-POS-164 langkah 1 terpenuhi (bagian 3 prinsip 8).
- TC-GS-POS-162 langkah 1 ("Apply filter Last Updated satu hari") memakai satu hari H-1 (langkah 30 dan 31); TC tidak menentukan harinya.
- TC-GS-POS-160 Expected b ("Tabel kembali ke halaman 1") membutuhkan posisi halaman 2 sebelum Apply; langkah 13 memindahkan ke halaman 2 (S-14) dan langkah 18 mengasersi halaman aktif 1 tepat sesudah panel ditutup, sebelum ukuran halaman diubah ke 25 pada langkah 19 (pada ukuran halaman 25 dengan 20 data tidak ada halaman 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencatat pembanding), langkah 12 (menutup panel sesudah screening), langkah 13 (pindah ke halaman 2), langkah 19 (ukuran halaman 25 agar hasil filter tidak terbagi ke halaman 2), langkah 54 (menutup Overlay Column Visibility), serta langkah 58 sampai 63 (`[Clear Field]`, `[Apply]`, menutup panel, menampilkan kembali kolom Last Updated, menutup overlay, dan mengembalikan ukuran halaman ke 10 untuk memulihkan state sebelum akhir spec).
- Langkah 36 (sepuluh nama baris pertama sama dengan yang dicatat pada langkah 1) adalah pembanding tambahan di luar Expected TC-GS-POS-162 untuk memastikan data kembali utuh; ukuran halaman pada langkah itu 25, sehingga hanya sepuluh nama pertama yang dibandingkan dengan catatan ukuran halaman 10.
- Pembagian TC lintas spec: kombinasi Search, Filter, Sort, dan Pagination di spec 030; Search tabel utama di spec 028; Overlay Column Visibility tabel utama di spec 031.
- Spec memuat 63 langkah (di atas smell sekitar 35 langkah). Seluruhnya satu kelas harness (Filter Panel tabel utama), satu akun, satu dataset; tiap blok TC menetapkan rentang tanggalnya sendiri dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC-GS-POS-160 mensyaratkan record dengan Last Updated pada tanggal batas awal dan batas akhir serta record di luar rentang, sedangkan Data Dinamis TC dibuat pada hari yang sama. Variasi Last Updated membutuhkan kemampuan menyetel Last Updated seed yang tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE di Prerequisites.
  - TC-GS-POS-160 tidak menyebut tanggal konkret rentang ("tanggal batas sesuai data") dan TC-GS-POS-161 menyebut "tanggal pembuatan data populasi"; spec memakai H-2, H-1, dan H.
  - TC-GS-POS-160 Expected b ("Tabel kembali ke halaman 1") tidak punya langkah menuju halaman >1 di TC; spec menambahkannya sebagai langkah 13.
  - TC-GS-POS-164 menyebut "Overlay Column Visibility" untuk menyembunyikan kolom, sedangkan TC-GS-POS-158 memakai Popup Setup Column; spec mengikuti masing-masing TC.
  - PRD (`position.md`) tidak menyatakan keadaan Filter Panel sesudah `[Apply]`; model "tetap terbuka, ditutup dengan klik ikon Filter" berasal dari TC-GS-POS-160 sampai 166 dan 170.
