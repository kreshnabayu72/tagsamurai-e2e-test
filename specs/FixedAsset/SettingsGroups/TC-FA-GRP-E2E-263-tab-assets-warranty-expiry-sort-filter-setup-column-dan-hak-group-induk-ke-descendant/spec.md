---
id: TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant
title: "Tab Assets Warranty Expiry: Sort Oldest/Newest, Filter Rentang, Setup Column, dan Hak pada Group Induk Berlaku untuk Descendant"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1225
  - TC-FA-GRP-1226
  - TC-FA-GRP-1228
  - TC-FA-GRP-1229
coverage:
  web: automated
---

# Tab Assets Warranty Expiry: Sort Oldest/Newest, Filter Rentang, Setup Column, dan Hak pada Group Induk Berlaku untuk Descendant

## Prerequisites

- Mode: FE+BE.
- Akun managePurchaseGroups (Pre-setup No 14; Group Role Manage purchase pada Value Gate Node A): `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun Total Control (Pre-setup No 1): `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Akun valuePurchaseParent (Pre-setup No 15; Group Role View asset value dan Manage purchase pada Value Gate Parent): `valuePurchaseParent_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VALUEPURCHASEPARENT_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Value Gate Parent > Value Gate Child (Tabel Dinamis No 12, hanya dibaca): C1 `Laptop Dell - 4` (Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).
- Lebar viewport diatur supaya tabel Tab Assets dapat di-scroll horizontal (dipakai asersi pin/scroll horizontal); hook `after` memulihkan viewport (S-03).

## Test Steps

### TC-FA-GRP-1225: Sort Warranty Expiry

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
4. Klik header Warranty Expiry (Ascending)
5. Verifikasi urutan Oldest First: G6, G2, G1, G4, lalu baris `—` (G3, G5) di akhir
6. Klik header Warranty Expiry (Descending)
7. Verifikasi urutan Newest First: baris `—` (G3, G5) di awal, lalu G4, G1, G2, G6
8. Klik header Warranty Expiry (Netral)
9. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1226: Filter Warranty Expiry rentang tanggal

10. Klik icon Filter
11. Verifikasi field Warranty Expiry berupa date range picker dengan placeholder `Select date`
12. Pilih rentang 01/01/2027–31/12/2027, klik [Apply]
13. Verifikasi hanya G2 (20/01/2027) dan G1 (15/03/2027) tampil
14. Verifikasi G6 (2026), G4 (2028), dan baris `—` (G3, G5) tidak tampil
15. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
16. Verifikasi header tabel tidak memuat kolom Warranty Expiry
17. Verifikasi filter Warranty Expiry tetap berlaku: hanya G2 dan G1 tampil
18. Klik icon Filter, klik [Clear Field], klik [Apply]
19. Logout
20. Login sebagai akun Total Control
21. Buka Fixed Asset > Settings > Groups

### TC-FA-GRP-1228: Setup Column kolom curated Warranty Expiry

22. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
23. Buka Detail Value Gate Node A (Tab Assets)
24. Buka Popup Setup Column, centang Warranty Expiry, klik [Save]
25. Verifikasi kolom Warranty Expiry tampil
26. Verifikasi Popup Detail Group tetap terbuka setelah [Save]
27. Muat ulang halaman (F5)
28. Verifikasi Groups List tampil
29. Verifikasi Popup Detail Group tertutup setelah F5
30. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
31. Buka Detail Value Gate Node A (Tab Assets)
32. Verifikasi kolom Warranty Expiry tetap tampil setelah F5
33. Buka Popup Setup Column, geser kolom Warranty Expiry ke posisi setelah Asset Value, klik [Save]
34. Verifikasi urutan kolom tabel mengikuti posisi baru (Warranty Expiry setelah Asset Value)
35. Buka Popup Setup Column, pin kolom Warranty Expiry, klik [Save]
36. Atur lebar viewport supaya tabel Tab Assets dapat di-scroll horizontal
37. Scroll tabel secara horizontal
38. Verifikasi kolom Warranty Expiry membeku (sticky) saat scroll horizontal
39. Muat ulang halaman (F5)
40. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
41. Buka Detail Value Gate Node A (Tab Assets)
42. Verifikasi urutan kolom tetap mengikuti posisi baru setelah F5
43. Buka Popup Setup Column, hilangkan pin kolom Warranty Expiry, klik [Save]
44. Scroll tabel secara horizontal
45. Verifikasi kolom Warranty Expiry ikut scroll setelah unpin
46. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
47. Logout
48. Login sebagai akun valuePurchaseParent
49. Buka Fixed Asset > Settings > Groups

### TC-FA-GRP-1229: Hak pada group induk berlaku untuk descendant

50. Ketik Search `Value Gate Child` pada Groups List, tekan Enter
51. Buka Detail Value Gate Child (Tab Assets)
52. Centang Asset Value, Warranty Expiry, dan PO Number di Popup Setup Column, klik [Save]
53. Verifikasi C1 (Value Gate Child, descendant Value Gate Parent): Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`
54. Tutup Popup Detail Group
55. Ganti isi kotak Search Groups List dengan `Value Gate Node A`, tekan Enter
56. Buka Detail Value Gate Node A (Tab Assets)
57. Verifikasi seluruh baris Value Gate Node A (bukan descendant) menampilkan `No access` pada Asset Value, Warranty Expiry, dan PO Number
58. Verifikasi kolom Asset Value, Warranty Expiry, dan PO Number tampil pada Value Gate Node A tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)

## Notes

- Urutan TC: TC-1225 dan TC-1226 (akun MPU), TC-1228 (ganti akun ke Total Control), TC-1229 (ganti akun ke VPP); tiap ganti akun punya langkah eksplisit.
- Langkah penghubung (S-03): menghilangkan centang Warranty Expiry antar blok; menyembunyikan kolom untuk mengamati filter pada kolom tersembunyi (TC-1226 butir b); `[Clear Field]` dan `[Apply]` untuk membersihkan filter; menutup popup antar group; membuka ulang Detail Value Gate Node A sesudah tiap Muat ulang halaman (F5).
- Alasan di atas ~35 langkah: satu kelas, tiga akun pada dataset Value Gate Node A dan Parent > Child; tiap blok berdiri sendiri, dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (S-03): "Atur lebar viewport ..." sebelum scroll horizontal pertama supaya tabel dapat di-scroll horizontal (asersi pin sticky); hook `after` memulihkan viewport.
- Langkah penghubung (S-03, S-14): `Buka Fixed Asset > Settings > Groups` sesudah tiap login akun lain karena hook `beforeEach` hanya membuka halaman untuk akun pertama.
- Asersi tambahan (S-03, 8b butir 2): `Verifikasi Groups List tampil` sebagai anchor positif sebelum absence Popup Detail Group sesudah F5, supaya halaman yang gagal dimuat tidak meloloskan asersi.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`, `Value Gate Child`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
  - TC-1226 butir b mensyaratkan filter berlaku walau kolom di-hide tetapi tidak ada langkah hide; spec menambah langkah penghubung.
  - TC-1225 hingga TC-1226 bergantung pada tanggal fixture Warranty tetap; G6 (01/01/2026) berstatus danger, penandanya tidak diasersi di spec ini.
  - Value Gate Child adalah node level 2 di bawah Value Gate Parent; TC dan PRD tidak menyatakan apakah Search Groups List pada All Groups menjangkau node level 2. Spec memakai Search `Value Gate Child`; tim FE memastikan cakupan Search atau menentukan navigasi lewat Value Gate Parent.
