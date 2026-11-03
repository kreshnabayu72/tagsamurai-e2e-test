---
id: TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting
title: "Tab Assets Asset Value (Commercial): Hak Pemegang View Asset Value, Pemegang Manage Accounting (Client-Wide), dan No Access di Group Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1214
  - TC-FA-GRP-1215
  - TC-FA-GRP-1216
coverage:
  web: automated
---

# Tab Assets Asset Value (Commercial): Hak Pemegang View Asset Value, Pemegang Manage Accounting (Client-Wide), dan No Access di Group Lain

## Prerequisites

- Mode: FE+BE.
- Akun viewAssetValueGroups (Pre-setup No 12; Group Role View asset value pada Value Gate Node A): `viewAssetValueGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_VIEWASSETVALUE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun manageAccountingGroups (Pre-setup No 13; Global Role Manage accounting, lisensi FA-7 aktif): `manageAccountingGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEACCOUNTING_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Data Value Gate Node B (Tabel Dinamis No 11, hanya dibaca): B1 `Laptop Dell - 3` (Asset Value 900), B2 `Monitor LG - 2` dan B3 `Kabel Roll - 2` tanpa nilai. Value Gate Child (Tabel Dinamis No 12, hanya dibaca): C1 `Laptop Dell - 4` (Asset Value 700). Aktor VAV tidak memegang View asset value pada Value Gate Node B.
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE). Client memiliki lisensi FA-7 aktif (akun MAC).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1214: Pemegang View asset value melihat nilai pada Value Gate Node A

1. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
2. Buka Detail Value Gate Node A (Tab Assets)
3. Verifikasi header tabel default tidak memuat kolom Asset Value
4. Buka Popup Setup Column
5. Verifikasi kolom Asset Value di Popup Setup Column berstatus curated (unchecked, enabled)
6. Centang kolom Asset Value, klik [Save]
7. Verifikasi G1 menampilkan Asset Value 1500
8. Verifikasi G2 menampilkan currency nol sesuai `prd-conventions.md` §32 (mis. `Rp 0,00`), bukan `—` dan bukan `No access`
9. Verifikasi G4 = 8000, G5 = 120, dan G6 = 2300
10. Verifikasi format currency dan rata kanan mengikuti `prd-conventions.md` §32
11. Verifikasi G3 (nilai belum ada) menampilkan `—`
12. Verifikasi tidak ada sel `No access` pada Value Gate Node A
13. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]

### TC-FA-GRP-1216: Pemegang View asset value di group lain melihat No access

14. Tutup Popup Detail Group
15. Ganti isi kotak Search Groups List dengan `Value Gate Node B`, tekan Enter
16. Buka Detail Value Gate Node B (Tab Assets)
17. Centang kolom Asset Value di Popup Setup Column, klik [Save]
18. Verifikasi kolom Asset Value tetap tersedia di Popup Setup Column dan tabel
19. Verifikasi B1, B2, dan B3 menampilkan `No access` (bukan 900 dan bukan `—`, walau B2 dan B3 tidak punya nilai)
20. Hover sel `No access`
21. Verifikasi tooltip "Requires View asset value access in this group."
22. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]

### TC-FA-GRP-1215: Pemegang Manage accounting (Global) melihat nilai di seluruh group

23. Logout
24. Login sebagai akun manageAccountingGroups
25. Buka Fixed Asset > Settings > Groups
26. Ketik Search `Value Gate Node A` pada Groups List, tekan Enter
27. Buka Detail Value Gate Node A (Tab Assets)
28. Centang kolom Asset Value di Popup Setup Column, klik [Save]
29. Verifikasi Value Gate Node A: G1 = 1500, G2 = currency nol, G3 = `—`, G4 = 8000, G5 = 120, G6 = 2300
30. Verifikasi tidak ada sel `No access` pada Value Gate Node A (hak client-wide)
31. Tutup Popup Detail Group
32. Ganti isi kotak Search Groups List dengan `Value Gate Node B`, tekan Enter
33. Buka Detail Value Gate Node B (Tab Assets)
34. Verifikasi Value Gate Node B: B1 = 900, B2 = `—`, B3 = `—`
35. Verifikasi kolom Asset Value tampil pada Value Gate Node B tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
36. Verifikasi tidak ada sel `No access` pada Value Gate Node B walau aktor tidak memegang View asset value pada group itu (hak client-wide)
37. Tutup Popup Detail Group
38. Ganti isi kotak Search Groups List dengan `Value Gate Child`, tekan Enter
39. Buka Detail Value Gate Child (Tab Assets)
40. Verifikasi Value Gate Child: C1 = 700
41. Verifikasi kolom Asset Value tampil pada Value Gate Child tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
42. Verifikasi tidak ada sel `No access` pada Value Gate Child (hak client-wide)
43. Buka Popup Setup Column, hilangkan centang kolom Asset Value, klik [Save]

## Notes

- Urutan TC: TC-1214, TC-1216 (akun VAV), lalu ganti akun ke MAC untuk TC-1215; akun pertama login di hook `before` (S-07, S-10).
- Langkah penghubung (S-03): menghilangkan centang Asset Value pada akhir tiap blok agar blok berikutnya mulai dengan kolom tidak tampil; menutup popup antar group.
- Kolom `Asset Value` pada TC-1214 sampai TC-1216 dibaca sebagai `Asset Value (Commercial)` (Catatan TC: penyebutan tanpa nama buku berarti Commercial).
- Langkah penghubung (S-03, S-14): `Buka Fixed Asset > Settings > Groups` sesudah tiap login akun lain karena hook `beforeEach` hanya membuka halaman untuk akun pertama.
- Klausa Expected TC-1215 "tidak ada `No access`" dan "kolom Asset Value tampil tanpa dicentang ulang" dipecah per group (S-01) dan diletakkan tepat sesudah group itu terbuka, karena hanya satu Popup Detail Group yang terbuka pada satu waktu.
- Langkah penghubung (S-03, S-14, R-16): sebelum tiap `Buka Detail` ditambahkan Search Groups List dengan nama group target (`Value Gate Node A`, `Value Gate Node B`, `Value Gate Child`), karena client memiliki lebih dari 10 node level 1 dan page size 10 sehingga baris target tidak dijamin berada di halaman 1; Search hilang setelah F5, login, atau buka ulang halaman Groups sehingga dipasang lagi.
- Alasan di atas ~35 langkah: satu kelas harness dan satu dataset; tiap blok TC berdiri sendiri dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal; 11 langkah penghubung (Search Groups List, buka Filter, tutup popup) ditambahkan tanpa asersi baru.
- Temuan untuk QA:
  - TC-1214 butir b menulis nilai 'G1 = 1500' tanpa format currency persis; spec mengasersi nilai dan format sesuai `prd-conventions.md` §32 tanpa menebak simbol mata uang.
  - Value Gate Child adalah node level 2 di bawah Value Gate Parent; TC dan PRD tidak menyatakan apakah Search Groups List pada All Groups menjangkau node level 2. Spec memakai Search `Value Gate Child`; tim FE memastikan cakupan Search atau menentukan navigasi lewat Value Gate Parent.
