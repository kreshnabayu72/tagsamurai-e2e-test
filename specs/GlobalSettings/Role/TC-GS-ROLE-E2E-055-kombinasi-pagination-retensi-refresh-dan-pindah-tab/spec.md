---
id: TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab
title: "Kombinasi Search, Filter, Sort, Pagination, Retensi Refresh, dan Pindah Tab Total Control dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-157
  - TC-GS-ROLE-158
  - TC-GS-ROLE-159
  - TC-GS-ROLE-160
  - TC-GS-ROLE-161
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, Pagination, Retensi Refresh, dan Pindah Tab Total Control dan Read Only

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup (hanya dibaca); data Dinamis milik spec di-seed di hook `before` dan dihapus di hook `after`.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > Total Control dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Tab Total Control dan Tab Read Only masing-masing berisi 11 user atau lebih (Pre-setup #17), termasuk Dewi Lestari (Total Control, Inactive; Pre-setup #3), Budi Santoso (Default User), Siti Nurhaliza (Read Only, Active) dan Rina Putri (Read Only, Inactive; Pre-setup #4).
- Data uji: keyword Search `a` dan `Dewi`; Filter Status `Active`; Sort Name Z-A (klik kedua pada header `Name`); page size `25`. Hasil Search `a` dengan Filter Status `Active` di Tab Total Control memuat sedikitnya 11 baris sehingga halaman 2 tersedia pada page size 10; jaminannya dari seeding milik spec di bawah (precondition TC tidak menjaminnya, lihat Temuan untuk QA).
- Data Dinamis milik spec (hook `before`, lewat seeding API): 11 user dengan Access Global Settings, Status `Active`, dan access level Total Control, bernama `Pagina Uji 01 {runId}-055` sampai `Pagina Uji 11 {runId}-055` (nama mengandung huruf `a`, email `paginauji01+{runId}-055@qwertysystem.net` sampai `paginauji11+{runId}-055@qwertysystem.net`). Nama tidak memuat `Dewi` sehingga tidak mengganggu Search `Dewi` (langkah 20 sampai 29). Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus 11 user tersebut.
- Tabel "Tab yang diuji" untuk TC-GS-ROLE-159:

  | Tab |
  |---|
  | Total Control |
  | Read Only |

- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab Total Control.
- Suite berjalan serial (`parallel: false`).
- State yang diubah dan dipulihkan: Search, Filter, Sort, dan page size dikembalikan ke default oleh langkah sidebar di antara blok TC; hook `after` sebagai cadangan.
- Kemampuan teknis (seeding): seeding API untuk membuat user ber-access level Total Control dan menghapusnya disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD dan tidak dikarang di spec.

## Test Steps

### TC-GS-ROLE-157: Kombinasi Search, Filter, Sort, dan Pagination

1. Ketik Search `a`, tekan Enter
2. Klik Filter
3. Pilih Status `Active`
4. Klik `[Apply]`
5. Klik header `Name` dua kali (A-Z lalu Z-A)
6. Ubah page size ke `25`
7. Verifikasi tabel memuat sedikitnya satu baris hasil
8. Verifikasi setiap baris cocok keyword `a`
9. Verifikasi setiap baris berstatus `Active`
10. Verifikasi baris terurut Name Z-A
11. Verifikasi tabel menampilkan paling banyak 25 baris per halaman
12. Klik Filter
13. Klik `[Clear Field]`
14. Klik `[Apply]`
15. Verifikasi Search `a` tetap berlaku
16. Verifikasi Sort Name Z-A tetap berlaku
17. Kosongkan isi kotak search, tekan Enter
18. Verifikasi Sort Name Z-A tetap berlaku

### TC-GS-ROLE-158: Pulih dari no-result saat satu saringan dilepas

19. Klik item sidebar `Role & Permission` untuk mereset Search, Filter, Sort, dan Pagination
20. Ketik Search `Dewi`, tekan Enter
21. Verifikasi baris Dewi Lestari tampil
22. Klik Filter
23. Pilih Status `Active`
24. Klik `[Apply]`
25. Verifikasi `No results found` tampil
26. Klik Filter
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Verifikasi baris Dewi Lestari tampil kembali

### TC-GS-ROLE-159: Pagination Tab Total Control dan Tab Read Only

30. Klik item sidebar `Role & Permission` untuk mereset Search, Filter, Sort, dan Pagination
Untuk setiap baris tabel "Tab yang diuji" (langkah 31 sampai 39):
31. Klik Tab sesuai baris tabel
32. Verifikasi tabel menampilkan 10 baris secara default
33. Buka dropdown page size
34. Verifikasi opsi page size `10`, `25`, `50`, `100`
35. Tutup dropdown page size dengan Esc
36. Klik halaman berikutnya
37. Verifikasi indikator halaman 2 aktif
38. Klik halaman sebelumnya
39. Verifikasi indikator halaman 1 aktif

### TC-GS-ROLE-160: Refresh F5 mempertahankan Search, Filter, Sort, dan halaman

40. Klik item sidebar `Role & Permission` untuk mereset Search, Filter, Sort, dan Pagination
41. Ketik Search `a`, tekan Enter
42. Klik Filter
43. Pilih Status `Active`
44. Klik `[Apply]`
45. Klik header `Name` dua kali (A-Z lalu Z-A)
46. Klik halaman 2
47. Verifikasi indikator halaman 2 aktif
48. Tekan F5
49. Verifikasi kotak Search berisi keyword `a`
50. Verifikasi tabel memuat sedikitnya satu baris hasil
51. Verifikasi setiap baris berstatus `Active`
52. Verifikasi baris terurut Name Z-A
53. Verifikasi indikator halaman 2 aktif
54. Verifikasi page size tetap `10`

### TC-GS-ROLE-161: State Search, Filter, dan Sort saat pindah Tab Total Control dan Read Only

55. Klik item sidebar `Role & Permission` untuk mereset Search, Filter, Sort, dan Pagination
56. Ketik Search `a`, tekan Enter
57. Klik Filter
58. Pilih Status `Active`
59. Klik `[Apply]`
60. Klik Tab `Read Only`
61. Verifikasi kotak Search kosong
62. Verifikasi baris Rina Putri (Read Only, Inactive) tampil sehingga Filter Status `Active` tidak berlaku
63. Klik Tab `Total Control`
64. Verifikasi kotak Search kosong
65. Verifikasi baris Dewi Lestari (Total Control, Inactive) tampil sehingga Filter Status `Active` tidak berlaku

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (tabel dimuat dari backend nyata; Search, Filter, Sort, dan Pagination bekerja terhadap data server).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (157, 158, 159, 160, 161) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 19, 30, 40, dan 55 (klik item sidebar `Role & Permission`, yang mereset Search, Filter, Sort, dan Pagination ke default sebelum blok TC berikutnya, bagian 4 konvensi).
- Langkah penghubung tambahan: langkah 35 (menutup dropdown page size dengan Esc; TC-GS-ROLE-159 tidak menyebutnya).
- Langkah 31 sampai 39 diulang untuk dua tab pada tabel "Tab yang diuji" (18 langkah setelah ekspansi). Langkah 31 untuk Tab Total Control hanya memastikan tab aktif.
- Spec melewati sekitar 35 langkah (sekitar 74 langkah setelah ekspansi) karena lima TC memakai dataset yang sama (tabel Tab Total Control dan Tab Read Only) dan satu kelas harness (fungsional, tanpa harness eksternal). Tiap blok TC dimulai dari state default lewat langkah sidebar (langkah 19 sampai 55), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemisahan menjadi lima spec hanya akan menambah login, hook, dan cleanup berulang.
- Pembagian TC lintas spec: TC-GS-ROLE-154 sampai 156 (Sort kolom lain) dan TC-GS-ROLE-162 sampai 173 (Setup Column) berada di spec lain; Pagination, retensi refresh, dan pindah tab untuk Tab System dan Detail tidak ada dalam TC sumber spec ini.
- Temuan untuk QA:
  - TC-GS-ROLE-157 Expected c: "Filter yang tersisa dan Sort tetap berlaku" tidak konsisten dengan langkah 5 TC, karena `[Clear Field]` lalu `[Apply]` sudah mengosongkan satu-satunya Filter; spec hanya mengasersi Sort Name Z-A tetap berlaku (langkah 18).
  - TC-GS-ROLE-157 Expected a: TC tidak menyebut jumlah baris hasil; spec mengasersi kecocokan tiap baris dan batas 25 baris per halaman.
  - TC-GS-ROLE-160: langkah "halaman 2" mensyaratkan hasil Search `a` dan Filter Status `Active` lebih dari 10 baris, sedangkan precondition TC hanya menjamin sedikitnya 3 user per tab; spec men-seed 11 user Active bernama mengandung `a` (Prerequisites) dan precondition TC-GS-ROLE-160 perlu ditulis ">10 baris hasil".
  - TC-GS-ROLE-161: judul menyebut Tab System, tetapi langkah dan Expected hanya mencakup Tab Total Control dan Tab Read Only; spec mengikuti langkah dan Expected.
  - TC-GS-ROLE-161 Expected a: "kondisi default" tidak menyebut cara mengamatinya; spec mengasersi kotak Search kosong dan baris Inactive tampil sebagai bukti Filter Status `Active` tidak berlaku.
