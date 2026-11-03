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
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin/scroll horizontal); hook `after` memulihkan viewport (S-03).

## Test Steps

### TC-FA-GRP-1209: Kolom Last Scanned mengikuti General Settings

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Verifikasi header tabel default tidak memuat kolom Last Scanned
4. Buka Popup Setup Column
5. Verifikasi kolom Last Scanned di Popup Setup Column berstatus curated (unchecked, enabled)
6. Centang kolom Last Scanned, klik [Save]
7. Verifikasi G3 menampilkan Last Scanned 01/09/2026
8. Verifikasi G1 menampilkan Last Scanned 10/10/2026
9. Verifikasi G5 menampilkan Last Scanned 20/10/2026
10. Verifikasi G2, G4, dan G6 (belum pernah dipindai) menampilkan `—`
11. Verifikasi nilai Last Scanned hanya berasal dari pemindaian pada Audit dan pemindaian Search by Scan tidak dihitung

### TC-FA-GRP-1210: Filter Last Scanned rentang tanggal

12. Klik icon Filter
13. Verifikasi field Last Scanned berupa date range picker dengan placeholder `Select date`
14. Pilih rentang 01/10/2026–31/10/2026, klik [Apply]
15. Verifikasi hanya G1 (10/10/2026) dan G5 (20/10/2026) tampil
16. Verifikasi G3 (01/09/2026) dan baris `—` (G2, G4, G6) tidak tampil
17. Buka Popup Setup Column
18. Hilangkan centang kolom Last Scanned, klik [Save]
19. Verifikasi header tabel tidak memuat kolom Last Scanned
20. Verifikasi filter Last Scanned tetap berlaku: hanya G1 dan G5 tampil
21. Klik icon Filter, klik [Clear Field], klik [Apply]

### TC-FA-GRP-1211: Sort Last Scanned

22. Centang kolom Last Scanned di Popup Setup Column, klik [Save]
23. Klik header Last Scanned (Ascending)
24. Verifikasi urutan Oldest First: G3, G1, G5, lalu baris `—` (G2, G4, G6) di akhir
25. Klik header Last Scanned (Descending)
26. Verifikasi urutan Newest First: baris `—` (G2, G4, G6) di awal, lalu G5, G1, G3
27. Klik header Last Scanned (Netral)
28. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1213: Setup Column kolom curated Last Scanned

29. Buka Popup Setup Column, hilangkan centang kolom Last Scanned, klik [Save]
30. Centang kolom Last Scanned di Popup Setup Column, klik [Save]
31. Verifikasi kolom Last Scanned tampil
32. Muat ulang halaman (F5)
33. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
34. Buka Detail Value Gate Node A (Tab Assets)
35. Verifikasi kolom Last Scanned tetap tampil setelah F5
36. Buka Popup Setup Column, geser kolom Last Scanned ke posisi sebelum Last Updated, klik [Save]
37. Verifikasi urutan kolom tabel mengikuti posisi baru (Last Scanned sebelum Last Updated)
38. Muat ulang halaman (F5)
39. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
40. Buka Detail Value Gate Node A (Tab Assets)
41. Verifikasi urutan kolom tetap mengikuti posisi baru setelah F5
42. Buka Popup Setup Column, pin kolom Last Scanned, klik [Save]
43. Atur lebar viewport supaya tabel Tab Assets dapat di-scroll horizontal
44. Scroll tabel secara horizontal
45. Verifikasi kolom Last Scanned membeku (sticky) saat scroll horizontal
46. Muat ulang halaman (F5)
47. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
48. Buka Detail Value Gate Node A (Tab Assets)
49. Buka Popup Setup Column, hilangkan pin kolom Last Scanned, klik [Save]
50. Scroll tabel secara horizontal
51. Verifikasi kolom Last Scanned ikut scroll setelah unpin

## Notes

- Langkah penghubung (S-03): menghilangkan centang Last Scanned untuk mengamati filter pada kolom tersembunyi (TC-1210 butir c), `[Clear Field]` dan `[Apply]` untuk membersihkan filter (S-09), serta menghilangkan lalu mencentang ulang Last Scanned sebelum TC-1213 agar kolom mulai tidak tampil. Membuka ulang Detail Value Gate Node A sesudah tiap Muat ulang halaman (F5).
- TC-1211 prasyarat (e) kolom Last Scanned dicentang dipenuhi langkah centang pada blok TC-1211. Langkah unpin dan scroll horizontal TC-1213 ditulis eksplisit agar asersi sticky dan ikut scroll punya aksi.
- Alasan di atas ~35 langkah: empat blok satu kelas dan satu dataset (Value Gate Node A, kolom Last Scanned); tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung (S-03): "Atur lebar viewport ..." sebelum scroll horizontal pertama supaya tabel dapat di-scroll horizontal (asersi pin sticky); hook `after` memulihkan viewport.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-1209 butir d (Search by Scan tidak dihitung) tidak memberi data pemindaian Search by Scan pada Tabel Dinamis No 15; asersi hanya bermakna bila fixture memuat pemindaian Search by Scan pada aset uji.
  - TC-1213 tidak menyatakan Expected setelah F5 di langkah pin dan tidak menyatakan hasil unpin selain 'ikut scroll'; spec mengasersi sesuai butir c.
  - TC-1209 sampai TC-1213 tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5; spec membuka ulang Detail Value Gate Node A sesudah tiap F5.
