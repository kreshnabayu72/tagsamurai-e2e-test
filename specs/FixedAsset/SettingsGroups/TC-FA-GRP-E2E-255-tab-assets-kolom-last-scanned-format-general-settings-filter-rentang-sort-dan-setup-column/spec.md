---
id: TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column
title: "Tab Assets Kolom Last Scanned: Tanggal Pemindaian Terbaru Mengikuti General Settings, Filter Rentang, Sort Oldest/Newest, dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1209
  - TC-FA-GRP-1210
  - TC-FA-GRP-1211
  - TC-FA-GRP-1213
coverage:
  web: automated
---

# Tab Assets Kolom Last Scanned: Tanggal Pemindaian Terbaru Mengikuti General Settings, Filter Rentang, Sort Oldest/Newest, dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun Total Control (Pre-setup No 1): `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`.
- Pemindaian Audit (Tabel Dinamis No 15): G3 01/09/2026, G1 10/10/2026, G5 20/10/2026; G2, G4, G6 belum pernah dipindai. Seeding pemindaian Audit disediakan tim FE/BE tanpa hardware; mekanismenya tidak didefinisikan di TC, PRD, atau LLD.
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE); membaca urutan baris tabel.
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Spec berjalan di suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1209: Kolom Last Scanned mengikuti General Settings

1. Buka Detail Value Gate Node A (Tab Assets)
2. Verifikasi header tabel default tidak memuat kolom Last Scanned
3. Buka Popup Setup Column
4. Verifikasi kolom Last Scanned di Popup Setup Column berstatus curated (unchecked, enabled)
5. Centang kolom Last Scanned, klik [Save]
6. Verifikasi G3 menampilkan Last Scanned 01/09/2026
7. Verifikasi G1 menampilkan Last Scanned 10/10/2026
8. Verifikasi G5 menampilkan Last Scanned 20/10/2026
9. Verifikasi G2, G4, dan G6 (belum pernah dipindai) menampilkan `—`
10. Verifikasi nilai Last Scanned hanya berasal dari pemindaian pada Audit dan pemindaian Search by Scan tidak dihitung

### TC-FA-GRP-1210: Filter Last Scanned rentang tanggal

11. Klik icon Filter
12. Verifikasi field Last Scanned berupa date range picker dengan placeholder `Select date`
13. Pilih rentang 01/10/2026–31/10/2026, klik [Apply]
14. Verifikasi hanya G1 (10/10/2026) dan G5 (20/10/2026) tampil
15. Verifikasi G3 (01/09/2026) dan baris `—` (G2, G4, G6) tidak tampil
16. Buka Popup Setup Column
17. Hilangkan centang kolom Last Scanned, klik [Save]
18. Verifikasi header tabel tidak memuat kolom Last Scanned
19. Verifikasi filter Last Scanned tetap berlaku: hanya G1 dan G5 tampil
20. Klik icon Filter, klik [Clear Field], klik [Apply]

### TC-FA-GRP-1211: Sort Last Scanned

21. Centang kolom Last Scanned di Popup Setup Column, klik [Save]
22. Klik header Last Scanned (Ascending)
23. Verifikasi urutan Oldest First: G3, G1, G5, lalu baris `—` (G2, G4, G6) di akhir
24. Klik header Last Scanned (Descending)
25. Verifikasi urutan Newest First: baris `—` (G2, G4, G6) di awal, lalu G5, G1, G3
26. Klik header Last Scanned (Netral)
27. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1213: Setup Column kolom curated Last Scanned

28. Buka Popup Setup Column, hilangkan centang kolom Last Scanned, klik [Save]
29. Centang kolom Last Scanned di Popup Setup Column, klik [Save]
30. Verifikasi kolom Last Scanned tampil
31. Muat ulang halaman (F5)
32. Buka Detail Value Gate Node A (Tab Assets)
33. Verifikasi kolom Last Scanned tetap tampil setelah F5
34. Buka Popup Setup Column, geser kolom Last Scanned ke posisi sebelum Last Updated, klik [Save]
35. Verifikasi urutan kolom tabel mengikuti posisi baru (Last Scanned sebelum Last Updated)
36. Muat ulang halaman (F5)
37. Buka Detail Value Gate Node A (Tab Assets)
38. Verifikasi urutan kolom tetap mengikuti posisi baru setelah F5
39. Buka Popup Setup Column, pin kolom Last Scanned, klik [Save]
40. Scroll tabel secara horizontal
41. Verifikasi kolom Last Scanned membeku (sticky) saat scroll horizontal
42. Muat ulang halaman (F5)
43. Buka Detail Value Gate Node A (Tab Assets)
44. Buka Popup Setup Column, hilangkan pin kolom Last Scanned, klik [Save]
45. Scroll tabel secara horizontal
46. Verifikasi kolom Last Scanned ikut scroll setelah unpin

## Notes

- Langkah penghubung (S-03): menghilangkan centang Last Scanned untuk mengamati filter pada kolom tersembunyi (TC-1210 butir c), `[Clear Field]` dan `[Apply]` untuk membersihkan filter (S-09), serta menghilangkan lalu mencentang ulang Last Scanned sebelum TC-1213 agar kolom mulai tidak tampil. Membuka ulang Detail Value Gate Node A sesudah tiap Muat ulang halaman (F5).
- TC-1211 prasyarat (e) kolom Last Scanned dicentang dipenuhi langkah centang pada blok TC-1211. Langkah unpin dan scroll horizontal TC-1213 ditulis eksplisit agar asersi sticky dan ikut scroll punya aksi.
- Alasan di atas ~35 langkah: empat blok satu kelas dan satu dataset (Value Gate Node A, kolom Last Scanned); tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-1209 butir d (Search by Scan tidak dihitung) tidak memberi data pemindaian Search by Scan pada Tabel Dinamis No 15; asersi hanya bermakna bila fixture memuat pemindaian Search by Scan pada aset uji.
  - TC-1213 tidak menyatakan Expected setelah F5 di langkah pin dan tidak menyatakan hasil unpin selain 'ikut scroll'; spec mengasersi sesuai butir c.
  - TC-1209 sampai TC-1213 tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5; spec membuka ulang Detail Value Gate Node A sesudah tiap F5.
