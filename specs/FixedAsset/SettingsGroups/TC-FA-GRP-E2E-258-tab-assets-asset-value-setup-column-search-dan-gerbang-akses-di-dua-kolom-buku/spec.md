---
id: TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku
title: "Tab Assets Asset Value: Setup Column (Centang, Geser, Pin), Search Nilai Tampil, dan Kedua Kolom Buku Hidden Secara Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1221
  - TC-FA-GRP-1265
  - TC-FA-GRP-1285
coverage:
  web: automated
---

# Tab Assets Asset Value: Setup Column (Centang, Geser, Pin), Search Nilai Tampil, dan Kedua Kolom Buku Hidden Secara Default

## Prerequisites

- Mode: FE+BE.
- Akun Total Control (Pre-setup No 1): `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Akun noValueAccess (Pre-setup No 16; tanpa View asset value, Manage purchase, maupun Manage accounting): `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1285: Kedua kolom Asset Value Hidden secara default

1. Buka Detail Value Gate Node A (Tab Assets)
2. Verifikasi header tabel default tidak memuat `Asset Value (Commercial)` maupun `Asset Value (Fiscal)`
3. Buka Popup Setup Column
4. Verifikasi Popup Setup Column memuat kedua kolom `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` berstatus curated (unchecked, enabled), berurutan, tanpa kolom Asset Value lain
5. Centang hanya `Asset Value (Fiscal)`, klik [Save]
6. Verifikasi hanya `Asset Value (Fiscal)` tampil pada header tabel
7. Verifikasi `Asset Value (Commercial)` tetap tersembunyi
8. Buka Popup Setup Column, hilangkan centang kolom Asset Value (Fiscal), klik [Save]

### TC-FA-GRP-1221: Setup Column kolom curated Asset Value (Commercial)

9. Buka Popup Setup Column, centang `Asset Value (Commercial)`, klik [Save]
10. Verifikasi kolom Asset Value (Commercial) tampil
11. Muat ulang halaman (F5)
12. Buka Detail Value Gate Node A (Tab Assets)
13. Verifikasi kolom Asset Value (Commercial) tetap tampil setelah F5
14. Buka Popup Setup Column, geser kolom Asset Value (Commercial) ke posisi setelah Status, klik [Save]
15. Verifikasi urutan kolom tabel mengikuti posisi baru (Asset Value (Commercial) setelah Status)
16. Muat ulang halaman (F5)
17. Buka Detail Value Gate Node A (Tab Assets)
18. Verifikasi urutan kolom tetap mengikuti posisi baru setelah F5
19. Buka Popup Setup Column, pin kolom Asset Value (Commercial), klik [Save]
20. Scroll tabel secara horizontal
21. Verifikasi kolom Asset Value (Commercial) membeku (sticky) saat scroll horizontal
22. Muat ulang halaman (F5)
23. Buka Detail Value Gate Node A (Tab Assets)
24. Buka Popup Setup Column, hilangkan pin kolom Asset Value (Commercial), klik [Save]
25. Scroll tabel secara horizontal
26. Verifikasi kolom Asset Value (Commercial) ikut scroll setelah unpin
27. Buka Popup Setup Column, hilangkan centang kolom Asset Value (Commercial), klik [Save]
28. Logout
29. Login sebagai akun viewAssetValueGroups

### TC-FA-GRP-1265: Search kolom Asset Value (Commercial)

30. Buka Detail Value Gate Node A (Tab Assets)
31. Centang kolom Asset Value (Commercial) di Popup Setup Column, klik [Save]
32. Catat teks nilai sel G1 dan G5 persis seperti tampil di sel (format currency §32)
33. Ketik Search teks nilai sel G1, tekan Enter
34. Verifikasi hanya G1 tampil
35. Ganti isi kotak search dengan teks nilai sel G5, tekan Enter
36. Verifikasi hanya G5 tampil
37. Buka Popup Setup Column, hilangkan centang kolom Asset Value (Commercial), klik [Save]
38. Logout
39. Login sebagai akun noValueAccess
40. Buka Detail Value Gate Node A (Tab Assets)
41. Centang kolom Asset Value (Commercial) di Popup Setup Column, klik [Save]
42. Ketik Search teks nilai sel G1 yang dicatat sebelumnya, tekan Enter
43. Verifikasi empty state tampil dengan Illustration, title "No results found", dan body "Try adjusting your search or filter." (sel `No access` tidak cocok dengan nilai G1)
44. Ganti isi kotak search dengan `No access`, tekan Enter
45. Verifikasi empty state tampil dengan Illustration, title "No results found", dan body "Try adjusting your search or filter." (teks `No access` pada sel tidak dicari)

## Notes

- Urutan TC: TC-1285 (screening state default) di awal, TC-1221 (Total Control), lalu ganti akun ke VAV dan NVA untuk TC-1265 (S-10).
- Langkah penghubung (S-03): menghilangkan centang kolom antar blok; mencatat teks nilai sel G1 dan G5 untuk dipakai Search (aksi tanpa asersi); membuka ulang Detail Value Gate Node A sesudah tiap Muat ulang halaman (F5).
- Alasan di atas ~35 langkah: satu dataset (Value Gate Node A, kolom Asset Value); tiga blok berdiri sendiri dan blok setelah ganti akun tetap bermakna walau blok sebelumnya gagal.
- Temuan untuk QA:
  - TC-1265 butir a merujuk 'langkah 3' dan 'langkah 4' padahal aksi Search berada di langkah TC nomor 4 dan 5; spec mengikuti urutan aksi TC.
  - TC-1265 tidak menulis teks nilai persis yang dicari (hanya 'seperti tampil di sel'); nilai diambil dari sel saat run.
  - TC-1221 tidak menyatakan Expected pada langkah F5 setelah pin dan hasil unpin selain butir c; spec mengasersi sesuai butir c; TC-1221 juga tidak menyatakan apakah Popup Detail Group tetap terbuka sesudah F5, spec membuka ulang Detail.
  - TC-1265 butir a memuat klausa teks `No access` tidak cocok tanpa langkah Search sendiri; spec menambah Search `No access` dan Verifikasi empty state.
