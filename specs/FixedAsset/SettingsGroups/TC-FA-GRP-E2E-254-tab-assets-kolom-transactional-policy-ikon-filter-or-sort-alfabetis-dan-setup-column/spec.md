---
id: TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column
title: "Tab Assets Kolom Transactional Policy: Ikon Transaksi On, Filter OR Nama Transaksi, Sort Alfabetis Label Ikon, dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1204
  - TC-FA-GRP-1205
  - TC-FA-GRP-1206
  - TC-FA-GRP-1208
coverage:
  web: automated
---

# Tab Assets Kolom Transactional Policy: Ikon Transaksi On, Filter OR Nama Transaksi, Sort Alfabetis Label Ikon, dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Policy per Asset Name (Tabel Dinamis No 14): Laptop Dell (Piece; Borrow On, Self Service Borrow Off, Assign On, Transfer On), Printer HP (Piece; semua Off), Monitor LG (Piece; hanya Self Service Borrow On), Forklift Toyota (Unit; hanya Transfer On), Kabel Roll (Meter; hanya Assign On). Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- Ikon uji hover (dipakai langkah 15 sampai 16):
  | Baris aset | Ikon | Label hover |
  |---|---|---|
  | G1 | ikon Borrow | `Borrow` |
  | G1 | ikon Assign | `Assign` |
  | G1 | ikon Transfer | `Transfer` |
  | G3 | ikon Self Service Borrow | `Self Service Borrow` |
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Konfigurasi kolom Tab Assets tersimpan per akun dan berlaku lintas group (Expected TC-1208).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin/scroll horizontal); hook `after` memulihkan viewport (S-03).

## Test Steps

### TC-FA-GRP-1204: Kolom curated Transactional Policy, ikon transaksi policy On, urutan tetap

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Amati header kolom (default)
4. Verifikasi header tabel memuat kolom `Name`
5. Verifikasi kolom Transactional Policy tidak tampil pada kondisi default
6. Buka Popup Setup Column
7. Verifikasi kolom Transactional Policy berstatus curated (unchecked, enabled)
8. Centang Transactional Policy
9. Klik [Save]
10. Amati kolom Transactional Policy pada G1 sampai G6
11. Verifikasi G1 dan G6 (Asset Name sama Laptop Dell) menampilkan ikon yang sama: Borrow, Assign, Transfer (urutan tetap Borrow, Self Service Borrow, Assign, Transfer; Self Service Borrow tidak tampil)
12. Verifikasi G3 hanya ikon Self Service Borrow, G4 hanya Transfer, G5 hanya Assign
13. Verifikasi G2 (semua policy Off) menampilkan `—`
14. Untuk setiap baris tabel Ikon uji hover (langkah 15 sampai 16):
15. Hover ikon pada baris aset
16. Verifikasi hover ikon menampilkan nama transaksi pada kolom Label hover
17. Verifikasi kolom mencerminkan policy Asset Name (bukan kelayakan transaksi saat ini): ikon tiap baris sesuai policy Asset Name di Tabel Dinamis No 14

### TC-FA-GRP-1205: Filter by Transactional Policy, opsi nama transaksi (OR)

18. Klik icon Filter
19. Buka dropdown field Transactional Policy
20. Verifikasi field Transactional Policy berupa dropdown multi-select searchable dengan placeholder `All transactions`
21. Verifikasi opsi memuat `Borrow`, `Self Service Borrow`, `Assign`, dan `Transfer`
22. Centang opsi `Assign`, tutup dropdown
23. Klik [Apply]
24. Verifikasi G1, G5, dan G6 tampil (policy Assign On)
25. Verifikasi G2, G3, dan G4 tidak tampil
26. Klik icon Filter
27. Klik [Clear Field]
28. Buka dropdown field Transactional Policy, centang opsi `Borrow` dan `Self Service Borrow`, tutup dropdown
29. Klik [Apply]
30. Verifikasi G1, G6, dan G3 tampil (OR di dalam field)
31. Verifikasi G2 tidak tampil
32. Klik icon Filter
33. Klik [Clear Field]
34. Klik [Apply]

### TC-FA-GRP-1206: Sort by Transactional Policy, alfabetis atas label ikon

35. Klik header Transactional Policy (Asc)
36. Verifikasi urutan Ascending: G5 (`Assign`), G1 dan G6 (`Assign, Borrow, Transfer`; `Assign` adalah awalan sehingga sel berjumlah ikon lebih sedikit lebih dulu), G3 (`Self Service Borrow`), G4 (`Transfer`), lalu baris `—` (G2) di akhir
37. Verifikasi urutan tampil ikon dalam sel tetap Borrow, Self Service Borrow, Assign, Transfer
38. Klik header Transactional Policy lagi (Desc)
39. Verifikasi urutan Descending kebalikan penuh: baris `—` (G2) di awal, lalu G4, G3, G1 dan G6, G5
40. Klik header Transactional Policy lagi (Netral)
41. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1208: Setup Column, kolom curated Transactional Policy: centang, geser (drag), dan pin

42. Buka Popup Setup Column
43. Uncheck Transactional Policy
44. Klik [Save]
45. Buka Popup Setup Column
46. Centang Transactional Policy
47. Klik [Save]
48. Verifikasi kolom Transactional Policy tampil di tabel
49. Verifikasi Popup Detail Group tetap terbuka setelah [Save]
50. Refresh F5
51. Verifikasi Groups List tampil
52. Verifikasi Popup Detail Group tertutup setelah F5
53. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
54. Buka Detail Value Gate Node A (Tab Assets)
55. Verifikasi kolom Transactional Policy tampil di tabel dan bertahan setelah F5
56. Buka Popup Setup Column
57. Drag Transactional Policy ke posisi setelah Status
58. Klik [Save]
59. Verifikasi urutan kolom tabel mengikuti posisi baru
60. Buka Popup Setup Column
61. Klik icon Pin Transactional Policy
62. Klik [Save]
63. Atur lebar viewport supaya tabel Tab Assets dapat di-scroll horizontal
64. Scroll tabel horizontal
65. Verifikasi kolom Transactional Policy membeku (sticky) saat scroll horizontal
66. Refresh F5
67. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
68. Buka Detail Value Gate Node A (Tab Assets)
69. Verifikasi urutan kolom tabel bertahan setelah F5
70. Buka Popup Setup Column
71. Klik icon Pin Transactional Policy untuk unpin
72. Klik [Save]
73. Scroll tabel horizontal
74. Verifikasi kolom Transactional Policy ikut scroll

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka Filter Panel dengan klik icon Filter; [Clear Field] dan [Apply] untuk membersihkan filter sebelum TC-1206; Uncheck lalu Centang Transactional Policy sebelum TC-1208 supaya blok mulai dari unchecked (blok sebelumnya meninggalkannya tercentang); membuka ulang Detail Value Gate Node A sesudah Refresh F5 dan scroll horizontal ulang. Langkah 15 sampai 16 diulang per baris tabel Ikon uji hover (8b butir 7). Urutan G1 terhadap G6 pada sort tidak dinilai (ikon identik).
- Spec ini 74 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom Transactional Policy), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state dipulihkan di antaranya; langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh F5.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Langkah penghubung (S-03): "Atur lebar viewport ..." sebelum scroll horizontal pertama supaya tabel dapat di-scroll horizontal (asersi pin sticky); hook `after` memulihkan viewport.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Langkah penghubung (S-03, 8b butir 2): langkah 51 (Verifikasi Groups List tampil) menjadi anchor positif sebelum asersi Popup Detail Group tertutup setelah F5, supaya halaman yang gagal dimuat tidak meloloskan asersi absence.
- Temuan untuk QA (S-15): (1) Expected TC-1204 butir e "kolom mencerminkan policy Asset Name, bukan kelayakan transaksi saat ini" tidak punya langkah pengamatan tersendiri; spec menulis Verifikasi atas ikon sesuai policy Asset Name. (2) TC-1205 tidak menyatakan apakah Filter Panel tertutup sesudah [Apply]; spec membuka ulang dengan klik icon Filter. (3) TC-1208 tidak menyebut kondisi awal kolom Transactional Policy; spec mengembalikannya ke unchecked sebelum blok. (4) Label hover setiap ikon transaksi tidak ditulis di Expected TC selain "nama transaksi"; spec memakai nama transaksi sebagai label. (5) TC-1208: Expected TC untuk pin hanya menyebut membeku (sticky) saat scroll horizontal dan ikut scroll setelah unpin; TC tidak menyebut pin bertahan setelah F5, sehingga spec tidak mengasersi pin pasca-F5.
