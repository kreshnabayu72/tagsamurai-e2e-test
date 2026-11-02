---
id: TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang
title: "Tab Assets Asset Value (Commercial): Manage Purchase/Tanpa Hak No Access, Sort Numerik, dan Filter Rentang Min-Max"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1217
  - TC-FA-GRP-1218
  - TC-FA-GRP-1219
coverage:
  web: automated
---

# Tab Assets Asset Value (Commercial): Manage Purchase/Tanpa Hak No Access, Sort Numerik, dan Filter Rentang Min-Max

## Prerequisites

- Mode: FE+BE.
- Akun managePurchaseGroups (Pre-setup No 14; Group Role Manage purchase pada Value Gate Node A): `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun noValueAccess (Pre-setup No 16; tanpa View asset value, Manage purchase, maupun Manage accounting): `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1217: Manage purchase atau tanpa hak tidak memberi akses Asset Value

1. Buka Detail Value Gate Node A (Tab Assets)
2. Centang kolom Asset Value di Popup Setup Column, klik [Save]
3. Verifikasi G1 sampai G6 seluruhnya menampilkan `No access`, termasuk G3 (tanpa nilai) dan G2 (bernilai nol)
4. Hover salah satu sel `No access`
5. Verifikasi tooltip "Requires View asset value access in this group."
6. Verifikasi tidak ada nilai Asset Value yang tampil pada G1 sampai G6
7. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]
8. Logout
9. Login sebagai akun noValueAccess
10. Buka Detail Value Gate Node A (Tab Assets)
11. Centang kolom Asset Value di Popup Setup Column, klik [Save]
12. Verifikasi G1 sampai G6 seluruhnya menampilkan `No access`, termasuk G3 (tanpa nilai) dan G2 (bernilai nol)
13. Hover salah satu sel `No access`
14. Verifikasi tooltip "Requires View asset value access in this group."
15. Verifikasi tidak ada nilai Asset Value yang tampil pada G1 sampai G6
16. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]
17. Logout
18. Login sebagai akun viewAssetValueGroups

### TC-FA-GRP-1218: Sort Asset Value numerik

19. Buka Detail Value Gate Node A (Tab Assets)
20. Centang kolom Asset Value di Popup Setup Column, klik [Save]
21. Klik header Asset Value (Ascending)
22. Verifikasi urutan Ascending numerik: G2 (0), G5 (120), G1 (1500), G6 (2300), G4 (8000), lalu baris `—` (G3) di akhir
23. Klik header Asset Value (Descending)
24. Verifikasi urutan Descending: G3 (`—`) di awal, lalu G4, G6, G1, G5, G2
25. Klik header Asset Value (Netral)
26. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1219: Filter Asset Value rentang Min–Max

27. Klik icon Filter
28. Verifikasi field Asset Value berupa range dengan placeholder `Min` dan `Max`
29. Isi Min 100 dan Max 2000, klik [Apply]
30. Verifikasi hanya G1 (1500) dan G5 (120) tampil
31. Klik [Clear Field], isi hanya Min 5000, klik [Apply]
32. Verifikasi hanya G4 (8000) tampil
33. Klik [Clear Field], isi hanya Max 500, klik [Apply]
34. Verifikasi G2 (0) dan G5 (120) tampil
35. Verifikasi G3 (`—`) tidak cocok dengan rentang mana pun dan tidak tampil
36. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]
37. Verifikasi header tabel tidak memuat kolom Asset Value
38. Verifikasi filter Max 500 tetap berlaku: hanya G2 dan G5 tampil
39. Klik icon Filter, klik [Clear Field], klik [Apply]

## Notes

- TC-1217 memakai dua akun berurutan (MPU lalu NVA) dengan langkah ganti akun eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Ganti akun ketiga ke VAV untuk TC-1218 dan TC-1219.
- Langkah penghubung (S-03): menghilangkan centang Asset Value antar blok, `[Clear Field]` dan `[Apply]` untuk membersihkan filter, serta menyembunyikan kolom untuk mengamati filter pada kolom tersembunyi (TC-1219 butir d).
- Alasan di atas ~35 langkah: tiga akun pada satu dataset (Value Gate Node A, kolom Asset Value); tiap blok berdiri sendiri dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal.
- Kolom `Asset Value` dibaca sebagai `Asset Value (Commercial)` (Catatan TC).
- Temuan untuk QA:
  - TC-1217 menulis 'Ulangi langkah 1–4' untuk aktor kedua; ditulis utuh di spec sebagai blok kedua.
  - TC-1219 butir d mensyaratkan filter berlaku walau kolom di-hide tetapi tidak ada langkah hide; spec menambah langkah penghubung.
