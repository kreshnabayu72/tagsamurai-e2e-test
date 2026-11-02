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
- Ikon uji hover (dipakai langkah 14 sampai 15):
  | Baris aset | Ikon | Label hover |
  |---|---|---|
  | G1 | ikon Borrow | `Borrow` |
  | G1 | ikon Assign | `Assign` |
  | G1 | ikon Transfer | `Transfer` |
  | G3 | ikon Self Service Borrow | `Self Service Borrow` |
- Preferensi kolom Setup Column: dikosongkan di hook `before` supaya tabel mulai dari kolom default, dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Konfigurasi kolom Tab Assets tersimpan per akun dan berlaku lintas group (Expected TC-1208).
- State global: tidak ada yang diubah; hanya preferensi kolom di browser (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1204: Kolom curated Transactional Policy, ikon transaksi policy On, urutan tetap

1. Buka Detail Value Gate Node A (Tab Assets)
2. Amati header kolom (default)
3. Verifikasi header tabel memuat kolom `Name`
4. Verifikasi kolom Transactional Policy tidak tampil pada kondisi default
5. Buka Popup Setup Column
6. Verifikasi kolom Transactional Policy berstatus curated (unchecked, enabled)
7. Centang Transactional Policy
8. Klik [Save]
9. Amati kolom Transactional Policy pada G1 sampai G6
10. Verifikasi G1 dan G6 (Asset Name sama Laptop Dell) menampilkan ikon yang sama: Borrow, Assign, Transfer (urutan tetap Borrow, Self Service Borrow, Assign, Transfer; Self Service Borrow tidak tampil)
11. Verifikasi G3 hanya ikon Self Service Borrow, G4 hanya Transfer, G5 hanya Assign
12. Verifikasi G2 (semua policy Off) menampilkan `—`
13. Untuk setiap baris tabel Ikon uji hover (langkah 14 sampai 15):
14. Hover ikon pada baris aset
15. Verifikasi hover ikon menampilkan nama transaksi pada kolom Label hover
16. Verifikasi kolom mencerminkan policy Asset Name (bukan kelayakan transaksi saat ini): ikon tiap baris sesuai policy Asset Name di Tabel Dinamis No 14

### TC-FA-GRP-1205: Filter by Transactional Policy, opsi nama transaksi (OR)

17. Klik icon Filter
18. Buka dropdown field Transactional Policy
19. Verifikasi field Transactional Policy berupa dropdown multi-select searchable dengan placeholder `All transactions`
20. Verifikasi opsi memuat `Borrow`, `Self Service Borrow`, `Assign`, dan `Transfer`
21. Centang opsi `Assign`, tutup dropdown
22. Klik [Apply]
23. Verifikasi G1, G5, dan G6 tampil (policy Assign On)
24. Verifikasi G2, G3, dan G4 tidak tampil
25. Klik icon Filter
26. Klik [Clear Field]
27. Buka dropdown field Transactional Policy, centang opsi `Borrow` dan `Self Service Borrow`, tutup dropdown
28. Klik [Apply]
29. Verifikasi G1, G6, dan G3 tampil (OR di dalam field)
30. Verifikasi G2 tidak tampil
31. Klik icon Filter
32. Klik [Clear Field]
33. Klik [Apply]

### TC-FA-GRP-1206: Sort by Transactional Policy, alfabetis atas label ikon

34. Klik header Transactional Policy (Asc)
35. Verifikasi urutan Ascending: G5 (`Assign`), G1 dan G6 (`Assign, Borrow, Transfer`; `Assign` adalah awalan sehingga sel berjumlah ikon lebih sedikit lebih dulu), G3 (`Self Service Borrow`), G4 (`Transfer`), lalu baris `—` (G2) di akhir
36. Verifikasi urutan tampil ikon dalam sel tetap Borrow, Self Service Borrow, Assign, Transfer
37. Klik header Transactional Policy lagi (Desc)
38. Verifikasi urutan Descending kebalikan penuh: baris `—` (G2) di awal, lalu G4, G3, G1 dan G6, G5
39. Klik header Transactional Policy lagi (Netral)
40. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1208: Setup Column, kolom curated Transactional Policy: centang, geser (drag), dan pin

41. Buka Popup Setup Column
42. Uncheck Transactional Policy
43. Klik [Save]
44. Buka Popup Setup Column
45. Centang Transactional Policy
46. Klik [Save]
47. Verifikasi kolom Transactional Policy tampil di tabel
48. Verifikasi Popup Detail Group tetap terbuka setelah [Save]
49. Refresh F5
50. Verifikasi Popup Detail Group tertutup setelah F5
51. Buka Detail Value Gate Node A (Tab Assets)
52. Verifikasi kolom Transactional Policy tampil di tabel dan bertahan setelah F5
53. Buka Popup Setup Column
54. Drag Transactional Policy ke posisi setelah Status
55. Klik [Save]
56. Verifikasi urutan kolom tabel mengikuti posisi baru
57. Buka Popup Setup Column
58. Klik icon Pin Transactional Policy
59. Klik [Save]
60. Scroll tabel horizontal
61. Verifikasi kolom Transactional Policy membeku (sticky) saat scroll horizontal
62. Refresh F5
63. Buka Detail Value Gate Node A (Tab Assets)
64. Verifikasi urutan kolom tabel bertahan setelah F5
65. Buka Popup Setup Column
66. Klik icon Pin Transactional Policy untuk unpin
67. Klik [Save]
68. Scroll tabel horizontal
69. Verifikasi kolom Transactional Policy ikut scroll

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): membuka Filter Panel dengan klik icon Filter; [Clear Field] dan [Apply] untuk membersihkan filter sebelum TC-1206; Uncheck lalu Centang Transactional Policy sebelum TC-1208 supaya blok mulai dari unchecked (blok sebelumnya meninggalkannya tercentang); membuka ulang Detail Value Gate Node A sesudah Refresh F5 dan scroll horizontal ulang. Langkah 14 sampai 15 diulang per baris tabel Ikon uji hover (8b butir 7). Urutan G1 terhadap G6 pada sort tidak dinilai (ikon identik).
- Spec ini 69 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom Transactional Policy), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state dipulihkan di antaranya; langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh F5.
- NC-07 (ikon final tipe tag dan transaksi) belum final: spec tidak mengasersi bentuk visual (glyph) ikon, hanya keberadaan, urutan, dan label hover.
- Temuan untuk QA (S-15): (1) Expected TC-1204 butir e "kolom mencerminkan policy Asset Name, bukan kelayakan transaksi saat ini" tidak punya langkah pengamatan tersendiri; spec menulis Verifikasi atas ikon sesuai policy Asset Name. (2) TC-1205 tidak menyatakan apakah Filter Panel tertutup sesudah [Apply]; spec membuka ulang dengan klik icon Filter. (3) TC-1208 tidak menyebut kondisi awal kolom Transactional Policy; spec mengembalikannya ke unchecked sebelum blok. (4) Label hover setiap ikon transaksi tidak ditulis di Expected TC selain "nama transaksi"; spec memakai nama transaksi sebagai label. (5) TC-1208: Expected TC untuk pin hanya menyebut membeku (sticky) saat scroll horizontal dan ikut scroll setelah unpin; TC tidak menyebut pin bertahan setelah F5, sehingga spec tidak mengasersi pin pasca-F5.
