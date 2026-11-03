---
id: TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi
title: "Sub-tab Borrowed Assets: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-736
  - TC-GS-USER-737
  - TC-GS-USER-738
  - TC-GS-USER-753
  - TC-GS-USER-754
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Andi Wijaya`, `Doni Pratama` (No. 10 dan 11) sebagai PIC seed. Client FAMS aktif. `Joko Susilo` (Tabel Pre-setup No. 19) sudah punya borrowed asset Pre-setup (`B0` baris, nilainya tidak disebut TC). Baris itu tidak diubah dan ikut tampil di tabel. Asersi memakai nilai bersuffix `{runId}-117` (Name, Brand, Model / Type) sehingga tidak bentrok dengan `B0`; jumlah baris tabel = `B0` + baris seed.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 26 baris aset pinjaman; seluruhnya tanpa foto sehingga kolom Photo menampilkan `—`):
  - Grup L (8 baris): Name `Laptop 1 {runId}-117` sampai `Laptop 8 {runId}-117`; Brand `Lenovo {runId}-117`; Model / Type `ThinkPad {runId}-117`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 10 hari (`{tglL}`).
  - Grup P (10 baris): Name `Proyektor 1 {runId}-117` sampai `Proyektor 10 {runId}-117`; Brand `Epson {runId}-117`; Model / Type `EB-X06 {runId}-117`; PIC `Doni Pratama` (tampil `Doni P`); Due Return Date = hari uji + 20 hari (`{tglP}`).
  - Grup K (8 baris): Name `Kamera 1 {runId}-117` sampai `Kamera 8 {runId}-117`; Brand `Canon {runId}-117`; Model / Type `EOS-R10 {runId}-117`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 30 hari (`{tglK}`).
  - Seluruh nilai Name, Brand, dan Model / Type unik per spec dan per run; setiap kolom yang diuji punya sedikitnya dua nilai distinct (Brand dan Model / Type tiga nilai, PIC dua nilai, Due Return Date tiga nilai) (S-11). `{tglL}`, `{tglP}`, `{tglK}` adalah tanggal Due Return Date grup tersebut dalam Date Format General Settings client, dihitung di hook `before` dari hasil seeding. PIC memakai user Pre-setup `Andi Wijaya` dan `Doni Pratama` yang hanya dibaca.
- Jumlah baris tabel = `B0` + 26 (sedikitnya 27 baris; Data Uji TC-GS-USER-753 menyebut tabel berisi 25 baris pada fixture BE Pre-setup No. 29) sehingga page size 10 memberi sedikitnya tiga halaman dan page size 25 memberi tepat 25 baris pada halaman 1. Page size 100 memuat seluruh baris pada satu halaman (asumsi `B0` + 26 tidak lebih dari 100).
- Data uji per TC: TC-GS-USER-736 enam kolom teks (Transaction ID, Name, Asset ID, Brand, Model / Type, PIC); TC-GS-USER-737 kolom Due Return Date; TC-GS-USER-738 header Photo; TC-GS-USER-753 page size 25 dan 10, halaman 2; TC-GS-USER-754 Search `{runId}-117` (mencocokkan Name 26 baris seed), Filter PIC `Andi Wijaya`, sort Name descending, page size 25.
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- Kemampuan teknis tambahan: membaca urutan nilai kolom pada seluruh baris tabel; menyetel page size dan mengisi input nomor halaman.
- State yang diubah dan dipulihkan: Search dikosongkan dan ditutup, Filter dikosongkan, sort dikembalikan ke default, dan page size dikembalikan ke 10 di akhir spec; hook `after` sebagai cadangan. Aset dan transaksi seed dibersihkan di hook `after` tanpa mengandalkan seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-736: Sort 3-state kolom kelas teks A-Z

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Pilih 100 baris per halaman pada Pagination
6. Verifikasi sedikitnya satu baris tampil pada tabel (baris seed `Laptop 1 {runId}-117`)
7. Verifikasi urutan awal tabel adalah default sort: seluruh baris terurut `Due Return Date` ascending
8. Klik header Transaction ID
9. Verifikasi kolom Transaction ID terurut ascending A-Z pada seluruh baris (klik 1)
10. Klik header Transaction ID
11. Verifikasi kolom Transaction ID terurut descending Z-A pada seluruh baris (klik 2)
12. Klik header Transaction ID
13. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom Transaction ID)
14. Klik header Name
15. Verifikasi kolom Name terurut ascending A-Z pada seluruh baris (klik 1)
16. Klik header Name
17. Verifikasi kolom Name terurut descending Z-A pada seluruh baris (klik 2)
18. Klik header Name
19. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom Name)
20. Klik header Asset ID
21. Verifikasi kolom Asset ID terurut ascending A-Z pada seluruh baris (klik 1)
22. Klik header Asset ID
23. Verifikasi kolom Asset ID terurut descending Z-A pada seluruh baris (klik 2)
24. Klik header Asset ID
25. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom Asset ID)
26. Klik header Brand
27. Verifikasi kolom Brand terurut ascending A-Z pada seluruh baris (klik 1)
28. Klik header Brand
29. Verifikasi kolom Brand terurut descending Z-A pada seluruh baris (klik 2)
30. Klik header Brand
31. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom Brand)
32. Klik header Model / Type
33. Verifikasi kolom Model / Type terurut ascending A-Z pada seluruh baris (klik 1)
34. Klik header Model / Type
35. Verifikasi kolom Model / Type terurut descending Z-A pada seluruh baris (klik 2)
36. Klik header Model / Type
37. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom Model / Type)
38. Klik header PIC
39. Verifikasi kolom PIC terurut ascending A-Z pada seluruh baris (klik 1)
40. Klik header PIC
41. Verifikasi kolom PIC terurut descending Z-A pada seluruh baris (klik 2)
42. Klik header PIC
43. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3, kolom PIC)

### TC-GS-USER-737: Sort 3-state kolom kelas tanggal

44. Klik header Due Return Date
45. Verifikasi kolom Due Return Date terurut Oldest First pada seluruh baris (klik 1)
46. Klik header Due Return Date
47. Verifikasi kolom Due Return Date terurut Newest First pada seluruh baris (klik 2)
48. Klik header Due Return Date
49. Verifikasi kembali ke default sort tabel: seluruh baris terurut `Due Return Date` ascending (klik 3)

### TC-GS-USER-738: Kolom non-sortable tidak punya ikon sort

50. Arahkan kursor ke header Photo
51. Verifikasi header Photo tanpa ikon sort
52. Klik header Photo
53. Verifikasi urutan baris tidak berubah: seluruh baris tetap terurut `Due Return Date` ascending

### TC-GS-USER-753: Pagination ubah page size dan input nomor halaman

54. Ubah page size ke 25
55. Verifikasi tabel menampilkan 25 baris (maksimal 25 baris per halaman)
56. Ubah page size kembali ke 10
57. Ketik nomor halaman `2` pada input halaman, tekan Enter
58. Verifikasi tabel langsung berpindah ke halaman 2
59. Klik next
60. Verifikasi tabel berpindah ke halaman 3
61. Klik prev
62. Verifikasi tabel kembali ke halaman 2

### TC-GS-USER-754: Kombinasi Search, Filter, Sort, dan Pagination berjalan bersamaan

63. Klik icon Search, ketik `{runId}-117`, tekan Enter
64. Verifikasi hasil Search: baris `Laptop 1 {runId}-117`, `Proyektor 1 {runId}-117`, dan `Kamera 1 {runId}-117` tampil
65. Klik icon Filter
66. Buka dropdown PIC, pilih opsi `Andi Wijaya`
67. Klik `[Apply]`
68. Klik header Name
69. Klik header Name
70. Ubah page size ke 25
71. Verifikasi Search tetap aktif: input Search berisi `{runId}-117`
72. Verifikasi sedikitnya satu baris tampil pada tabel (baris seed `Laptop 1 {runId}-117`)
73. Verifikasi Filter tetap aktif: seluruh baris bernilai PIC `Andi W` (baris `Laptop 1` sampai `Laptop 8` dan `Kamera 1` sampai `Kamera 8`)
74. Verifikasi Sort tetap aktif: Name descending Z-A dengan baris pertama `Laptop 8 {runId}-117` dan baris terakhir `Kamera 1 {runId}-117`
75. Verifikasi page size 25 terpilih
76. Verifikasi tabel menampilkan 16 baris dalam satu halaman (irisan Search dan Filter)
77. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
78. Klik icon Filter
79. Klik `[Clear Field]`
80. Klik `[Apply]`
81. Klik header Name
82. Ubah page size ke 10

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (736, 737, 738, 753, 754) dipertahankan.
- Data target: TC sumber memakai `Ahmad Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman), sehingga asersi memakai nilai seed bersuffix.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 5 (100 baris per halaman supaya seluruh baris berada di satu halaman dan urutan teramati utuh); langkah 77 (mengosongkan Search); langkah 78, 79, 80 (mengosongkan Filter); langkah 81 (mengembalikan sort ke default); langkah 82 (memulihkan page size 10). Urutan sort diasersi pada seluruh baris dengan page size 100 karena `B0` tidak diketahui; arah urutan teramati bila kolom punya sedikitnya dua nilai distinct (S-11).
- Asersi tambahan (S-03): langkah 6 dan 72 (sedikitnya satu baris tampil) adalah pembanding bagi asersi universal "seluruh baris" pada langkah sesudahnya (bagian 8b butir 2); langkah 7 memverifikasi default sort sebelum klik pertama, sebagai pembanding bagi "kembali ke default sort tabel" (klik 3) tiap kolom; klik 1 Due Return Date (Oldest First) menghasilkan urutan yang sama dengan default karena default sort tabel adalah Due Return Date ascending.
- Search `{runId}-117` pada TC-GS-USER-754 dipilih sebagai keyword karena Name seed memuat suffix itu (Search mencocokkan Name, Brand, dan Model / Type); hasil Search = 26 baris seed tanpa baris `B0`, sehingga irisan dengan Filter PIC `Andi Wijaya` = 16 baris (grup Laptop dan Kamera) dan seluruhnya muat dalam page size 25.
- Spec melewati sekitar 35 langkah (82 langkah) karena TC-GS-USER-736 menguji enam kolom dengan blok identik (klik 1, 2, 3 beserta `Verifikasi` tiap klik); semuanya satu kelas harness (fungsional, baca saja) pada satu layar dan satu dataset seed, dan tiap blok kolom berdiri sendiri.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 ada di spec 114; TC-GS-USER-722 sampai 730 ada di spec 115; TC-GS-USER-731 sampai 735 ada di spec 116; TC-GS-USER-739 sampai 747 ada di spec 118; TC-GS-USER-389 dan 748 sampai 752 ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-736 dan 737: "kembali ke default sort tabel" sama dengan Due Return Date ascending; klik 1 Due Return Date (Oldest First) dan klik 3 (default) menghasilkan urutan yang sama sehingga keduanya dibedakan lewat nomor klik, bukan urutan baris.
  - TC-GS-USER-736: TC tidak menyebut urutan nilai kolom PIC; PRD mengurutkan menurut nama lengkap (user.md §4.1.3), tetapi kolom menampilkan `[First Name] [Last Initial]`; spec mengasersi urutan menurut nilai yang tampil.
  - TC-GS-USER-753: Data Uji menyebut tabel berisi 25 baris (fixture BE, Pre-setup No. 29) pada user `Volume Test User`; spec memakai `Joko Susilo` dengan `B0` + 26 baris milik spec (S-06) sehingga page size 25 dan halaman ke-3 teramati. Langkah "Kembali 10" dan "klik next lalu prev" tidak menyebut halaman awal; spec mengikuti urutan langkah (halaman 2, next ke halaman 3, prev ke halaman 2).
  - TC-GS-USER-754: "Terapkan filter bila tersedia" (bersyarat); spec menerapkan Filter PIC karena Filter Panel tersedia (PRD §4.1.3). "Sort kolom" tidak menyebut kolom; spec memakai Name descending.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
