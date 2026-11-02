---
id: TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access
title: "Tab Assets Download Isi Berkas Kolom Bergerbang: Asset Value (Commercial), Warranty Expiry, Custom Field, dan Sel No Access per Aktor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1220
  - TC-FA-GRP-1227
  - TC-FA-GRP-1237
  - TC-FA-GRP-1247
coverage:
  web: automated
---

# Tab Assets Download Isi Berkas Kolom Bergerbang: Asset Value (Commercial), Warranty Expiry, Custom Field, dan Sel No Access per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login pertama di hook `before` spec ini: viewAssetValueGroups; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite):
  - viewAssetValueGroups (Pre-setup No 12): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`; Group Role View asset value pada Value Gate Node A.
  - managePurchaseGroups (Pre-setup No 14): `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`; Group Role Manage purchase pada Value Gate Node A.
  - allValueAccess (Pre-setup No 17): `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`; Manage purchase pada Value Gate Node A dan Manage accounting Global, lisensi FA-7 aktif.
  - noValueAccess (Pre-setup No 16): `noValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`; tanpa View asset value, Manage purchase, maupun Manage accounting.
- Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md`.
- Data: Value Gate Node A (Tabel Dinamis No 10, Assignable, level 1) berisi hanya aset G1 sampai G6. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 belum ada, G4 20/05/2028, G5 belum ada, G6 01/01/2026. Cost Center: G1 `CC-ALPHA`, G2 `CC-GAMMA`, G3 belum diisi, G4 `CC-ALPHA`, G5 di luar Scope, G6 `CC-BETA`; Insurance Policy: G1 dan G6 `INS-2026`, lainnya di luar Scope; PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`; Purchase Date: G1 10/02/2026; Cost Account: G1 `CA-100`, G3 belum diisi. Pemindaian Audit (Tabel Dinamis No 15): G3 01/09/2026, G1 10/10/2026, G5 20/10/2026. Custom Field Tabel Dinamis No 13. Data dibaca apa adanya dan tidak diubah spec; di-seed idempotent oleh hook `before` (kemampuan disediakan tim FE/BE).
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (prasyarat state, tidak diubah spec; disediakan tim FE/BE).
- Kemampuan teknis: membaca isi berkas unduhan CSV (nilai sel, hyphen `-`, header kolom) disediakan tim FE; asersi berkas memakai kemampuan itu.
- Preferensi kolom Setup Column tiap akun dikosongkan di hook `before` dan dihapus di hook `after` (hapus preferensi kolom di browser, bukan [Reset to Default]; kemampuan disediakan tim FE). Spec mengasumsikan konfigurasi kolom Tab Assets tersimpan per akun (lihat Temuan untuk QA).
- State global: tidak ada yang diubah selain preferensi kolom di browser. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1220: Kolom Asset Value (Commercial) ditulis nilai asli, — ditulis - (viewAssetValueGroups)

1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column
3. Centang Asset Value (Commercial)
4. Klik [Save]
5. Klik icon Download
6. Pilih Download as CSV
7. Verifikasi tidak ada toast sukses
8. Buka berkas
9. Verifikasi kolom Asset Value (Commercial): G1 = `1500`, G2 = `0`, G4 = `8000`, G5 = `120`, G6 = `2300` ditulis nilai asli (bukan teks `No access`)
10. Verifikasi sel Asset Value (Commercial) G3 ditulis hyphen tunggal `-`
11. Tutup Popup Detail Group

### TC-FA-GRP-1227: Kolom Warranty Expiry mengikuti format General Settings, — ditulis - (managePurchaseGroups)

12. Ganti akun: Logout
13. Login dengan email `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`
14. Buka Fixed Asset > Settings > Groups
15. Buka Detail Value Gate Node A (Tab Assets)
16. Buka Popup Setup Column
17. Centang Warranty Expiry
18. Klik [Save]
19. Klik icon Download
20. Pilih Download as CSV
21. Verifikasi tidak ada toast sukses
22. Buka berkas
23. Verifikasi kolom Warranty Expiry: G6 = `01/01/2026`, G2 = `20/01/2027`, G1 = `15/03/2027`, G4 = `20/05/2028` ditulis tanggal sesuai format General Settings (nilai asli)
24. Verifikasi sel Warranty Expiry G3 dan G5 ditulis hyphen tunggal `-`
25. Tutup Popup Detail Group

### TC-FA-GRP-1237: Kolom Custom Field ditulis nilai (tanggal mengikuti General Settings), — ditulis - (allValueAccess)

26. Ganti akun: Logout
27. Login dengan email `allValueAccess_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`
28. Buka Fixed Asset > Settings > Groups
29. Buka Detail Value Gate Node A (Tab Assets)
30. Buka Popup Setup Column
31. Centang Cost Center, Insurance Policy, PO Number, Purchase Date, dan Cost Account
32. Klik [Save]
33. Klik icon Download
34. Pilih Download as CSV
35. Verifikasi tidak ada toast sukses
36. Buka berkas
37. Verifikasi kolom Cost Center, Insurance Policy, PO Number, Purchase Date, dan Cost Account hadir dengan nilai asli (G1 = `CC-ALPHA`, `INS-2026`, `PO-001`, `10/02/2026`, `CA-100`)
38. Verifikasi sel yang belum diisi atau di luar Scope (mis. Cost Center G3 dan G5) ditulis hyphen tunggal `-`
39. Tutup Popup Detail Group

### TC-FA-GRP-1247: Sel No access ditulis teks No access; kolom tidak bergerbang tetap bernilai (noValueAccess)

40. Ganti akun: Logout
41. Login dengan email `noValueAccess_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_GRP_NOVALUEACCESS_PASSWORD`
42. Buka Fixed Asset > Settings > Groups
43. Buka Detail Value Gate Node A (Tab Assets)
44. Buka Popup Setup Column
45. Centang Asset Value (Commercial), Warranty Expiry, dan Last Scanned
46. Klik [Save]
47. Klik icon Download
48. Pilih Download as CSV
49. Verifikasi tidak ada toast sukses
50. Buka berkas
51. Verifikasi kolom Asset Value (Commercial) dan Warranty Expiry: seluruh baris ditulis teks `No access` (bukan nilai asli dan bukan `-`)
52. Verifikasi kolom Last Scanned tetap bernilai (G1 = `10/10/2026`)
53. Verifikasi sel Last Scanned untuk aset yang belum pernah dipindai (G2, G4, G6) ditulis `-`

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular. Kelas harness f (isi berkas) untuk seluruh spec.
- Langkah penghubung (S-03): menutup Popup Detail Group antar blok; Logout dan Login pada Ganti akun (akun pertama login di hook `before`; ganti akun punya langkah eksplisit, S-07); Buka Fixed Asset > Settings > Groups sesudah login akun baru karena hook `beforeEach` hanya membuka halaman untuk akun pertama. Asersi tidak ada toast sukses diletakkan segera sesudah memilih format Download dan sebelum membuka berkas (8b butir 11); anchor positifnya adalah Verifikasi isi berkas sesudahnya.
- Spec ini 53 langkah, di atas smell 35 langkah: seluruh blok satu kelas harness (isi berkas unduhan kolom bergerbang) pada dataset yang sama (Value Gate Node A) dengan alur yang sama, dan ganti akun eksplisit di antara blok (bagian sesudah ganti akun tetap bermakna walau blok sebelumnya gagal); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (S-15): (1) TC-1220 dan TC-1247 menulis "centang kolom Asset Value" padahal Setup Column memuat dua kolom `Asset Value (Commercial)` dan `Asset Value (Fiscal)`; spec memakai `Asset Value (Commercial)` mengikuti Catatan TC. (2) TC-1237 tidak menyebut nilai konkret kolom Insurance Policy dan Cost Account selain G1; spec mengasersi nilai G1 yang tertulis di TC. (3) TC-1247 butir b menulis tanggal pemindaian G1 sebagai "mis. G1 = 10/10/2026" tanpa jam.
