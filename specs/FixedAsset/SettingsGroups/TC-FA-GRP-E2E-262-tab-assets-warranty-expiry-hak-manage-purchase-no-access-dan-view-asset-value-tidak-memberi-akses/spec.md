---
id: TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses
title: "Tab Assets Warranty Expiry: Hak Pemegang Manage Purchase pada Group, No Access di Group Lain, dan View Asset Value/Manage Accounting Tidak Memberi Akses Warranty"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1222
  - TC-FA-GRP-1223
  - TC-FA-GRP-1224
coverage:
  web: automated
---

# Tab Assets Warranty Expiry: Hak Pemegang Manage Purchase pada Group, No Access di Group Lain, dan View Asset Value/Manage Accounting Tidak Memberi Akses Warranty

## Prerequisites

- Mode: FE+BE.
- Akun managePurchaseGroups (Pre-setup No 14; Group Role Manage purchase pada Value Gate Node A): `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Akun manageAccountingGroups (Pre-setup No 13; Global Role Manage accounting, lisensi FA-7 aktif): `manageAccountingGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEACCOUNTING_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Data Value Gate Node B (Tabel Dinamis No 11, hanya dibaca; aktor MPU tidak memegang Manage purchase pada group ini): B1 `Laptop Dell - 3` (Asset Value 900, Warranty Expiry 01/06/2027, PO Number `PO-B01`, Cost Account `CA-300`), B2 `Monitor LG - 2` (tanpa nilai), B3 `Kabel Roll - 2` (tanpa nilai; di luar Scope PO Number dan Cost Account).
- Lisensi FA-7 aktif pada client (akun MAC).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1222: Pemegang Manage purchase melihat tanggal Warranty

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Verifikasi header tabel default tidak memuat kolom Warranty Expiry
4. Buka Popup Setup Column
5. Verifikasi kolom Warranty Expiry di Popup Setup Column berstatus curated (unchecked, enabled)
6. Centang kolom Warranty Expiry, klik [Save]
7. Verifikasi G6 = 01/01/2026, G2 = 20/01/2027, G1 = 15/03/2027, G4 = 20/05/2028 (format dan timezone General Settings)
8. Hover sel G6
9. Verifikasi G6 (tanggal lampau) tampil penuh dengan penanda danger dan tooltip "Warranty expired"
10. Verifikasi G3 dan G5 (belum ada nilai) menampilkan `—`
11. Verifikasi tidak ada sel `No access` pada Value Gate Node A
12. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]

### TC-FA-GRP-1223: Pemegang Manage purchase di group lain melihat No access

13. Tutup Popup Detail Group
14. Ganti isi kotak Search Groups List dengan `Value Gate Node B`, tekan Enter
15. Buka Detail Value Gate Node B (Tab Assets)
16. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
17. Verifikasi kolom Warranty Expiry tetap tersedia
18. Verifikasi B1, B2, dan B3 menampilkan `No access` (bukan 01/06/2027 dan bukan `—`)
19. Hover sel `No access`
20. Verifikasi tooltip "Requires Manage purchase access in this group."
21. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]

### TC-FA-GRP-1224: View asset value dan Manage accounting tidak memberi akses Warranty

22. Logout
23. Login sebagai akun viewAssetValueGroups
24. Buka Fixed Asset > Settings > Groups
25. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
26. Buka Detail Value Gate Node A (Tab Assets)
27. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
28. Verifikasi G1 sampai G6 seluruhnya menampilkan `No access` (termasuk G3 dan G5 yang tidak punya nilai)
29. Hover salah satu sel `No access`
30. Verifikasi tooltip "Requires Manage purchase access in this group."
31. Verifikasi tidak ada tanggal Warranty yang tampil
32. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]
33. Logout
34. Login sebagai akun manageAccountingGroups
35. Buka Fixed Asset > Settings > Groups
36. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
37. Buka Detail Value Gate Node A (Tab Assets)
38. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
39. Verifikasi G1 sampai G6 seluruhnya menampilkan `No access` (termasuk G3 dan G5 yang tidak punya nilai)
40. Hover salah satu sel `No access`
41. Verifikasi tooltip "Requires Manage purchase access in this group."
42. Verifikasi tidak ada tanggal Warranty yang tampil
43. Buka Popup Setup Column, hilangkan centang kolom Warranty Expiry, klik [Save]

## Notes

- Urutan TC: TC-1222 dan TC-1223 (akun MPU), lalu ganti akun ke VAV dan MAC untuk TC-1224 (S-07). 'Ulangi langkah 1–4' TC-1224 ditulis utuh untuk tiap akun (S-04).
- Penanda warna Warranty (TC-1222 butir b) diasersi sebagai danger beserta tooltip "Warranty expired" untuk G6; penanda G1, G2, dan G4 tidak diasersi di spec ini karena tanggal tetap; pengujian penanda masa garansi dengan tanggal relatif hari uji ada di spec 264 dan 265.
- Langkah penghubung (S-03): menghilangkan centang Warranty Expiry pada akhir tiap blok.
- Alasan di atas ~35 langkah: tiga akun pada satu dataset (kolom Warranty Expiry); tiap blok berdiri sendiri dan blok sesudah ganti akun tetap bermakna.
- Langkah penghubung (S-03, S-14): `Buka Fixed Asset > Settings > Groups` sesudah tiap login akun lain karena hook `beforeEach` hanya membuka halaman untuk akun pertama.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`, `Value Gate Node B`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Temuan untuk QA:
