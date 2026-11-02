---
id: TC-FA-GRP-E2E-260-tab-assets-hak-sel-bergerbang-tier-total-control-dan-default-user
title: "Tab Assets Hak Sel Bergerbang: Tier Total Control dan Default User Berhak Atas Semua Kolom Bergerbang Client-Wide"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1256
  - TC-FA-GRP-1257
coverage:
  web: automated
---

# Tab Assets Hak Sel Bergerbang: Tier Total Control dan Default User Berhak Atas Semua Kolom Bergerbang Client-Wide

## Prerequisites

- Mode: FE+BE.
- Akun Total Control (Pre-setup No 1): `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun Default User (Pre-setup No 2): `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DU_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Data Value Gate Node B (Tabel Dinamis No 11, hanya dibaca): B1 `Laptop Dell - 3` (Asset Value 900, Warranty Expiry 01/06/2027, PO Number `PO-B01`, Cost Account `CA-300`), B2 `Monitor LG - 2` (tanpa nilai), B3 `Kabel Roll - 2` (tanpa nilai; di luar Scope PO Number dan Cost Account). Value Gate Child (Tabel Dinamis No 12, hanya dibaca): C1 `Laptop Dell - 4` (Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`, Cost Account `CA-400`).
- Lisensi FA-7 aktif pada client (Cost Account adalah custom field Accounting).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1256: Hak sel bergerbang tier Total Control

1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Asset Value, Warranty Expiry, PO Number, dan Cost Account, klik [Save]
3. Verifikasi Value Gate Node A kolom Asset Value: G1 1500, G2 currency nol (mis. `Rp 0,00`), G3 `—`, G4 8000, G5 120, G6 2300
4. Verifikasi Value Gate Node A kolom Warranty Expiry: G1 15/03/2027, G3 `—`, G4 20/05/2028
5. Verifikasi Value Gate Node A kolom PO Number: G1 `PO-001`, G3 `—`, G4 `—` (di luar Scope)
6. Verifikasi Value Gate Node A kolom Cost Account: G1 `CA-100`, G3 `—`
7. Tutup Popup Detail Group, buka Detail Value Gate Node B (Tab Assets)
8. Verifikasi keempat kolom tampil pada Value Gate Node B tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
9. Verifikasi B1: Asset Value 900, Warranty Expiry 01/06/2027, PO Number `PO-B01`, Cost Account `CA-300`
10. Verifikasi B2 menampilkan `—` pada seluruh kolom (tanpa nilai)
11. Verifikasi B3: Asset Value dan Warranty Expiry `—`, PO Number dan Cost Account `—` (di luar Scope)
12. Tutup Popup Detail Group, buka Detail Value Gate Child (Tab Assets)
13. Verifikasi keempat kolom tampil pada Value Gate Child tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
14. Verifikasi C1: Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`, Cost Account `CA-400`
15. Verifikasi tidak ada sel `No access` pada group mana pun walau aktor tidak memegang View asset value, Manage purchase, atau Manage accounting pada group (hak mengikuti tier)
16. Buka Popup Setup Column, hilangkan centang kolom Asset Value, Warranty Expiry, PO Number, dan Cost Account, klik [Save]
17. Logout
18. Login sebagai akun Default User

### TC-FA-GRP-1257: Hak sel bergerbang tier Default User

19. Buka Detail Value Gate Node A (Tab Assets)
20. Buka Popup Setup Column, centang kolom Asset Value, Warranty Expiry, PO Number, dan Cost Account, klik [Save]
21. Verifikasi Value Gate Node A kolom Asset Value: G1 1500, G2 currency nol (mis. `Rp 0,00`), G3 `—`, G4 8000, G5 120, G6 2300
22. Verifikasi Value Gate Node A kolom Warranty Expiry: G1 15/03/2027, G3 `—`, G4 20/05/2028
23. Verifikasi Value Gate Node A kolom PO Number: G1 `PO-001`, G3 `—`, G4 `—` (di luar Scope)
24. Verifikasi Value Gate Node A kolom Cost Account: G1 `CA-100`, G3 `—`
25. Tutup Popup Detail Group, buka Detail Value Gate Node B (Tab Assets)
26. Verifikasi keempat kolom tampil pada Value Gate Node B tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
27. Verifikasi B1: Asset Value 900, Warranty Expiry 01/06/2027, PO Number `PO-B01`, Cost Account `CA-300`
28. Verifikasi B2 menampilkan `—` pada seluruh kolom (tanpa nilai)
29. Verifikasi B3: Asset Value dan Warranty Expiry `—`, PO Number dan Cost Account `—` (di luar Scope)
30. Tutup Popup Detail Group, buka Detail Value Gate Child (Tab Assets)
31. Verifikasi keempat kolom tampil pada Value Gate Child tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
32. Verifikasi C1: Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`, Cost Account `CA-400`
33. Verifikasi tidak ada sel `No access` pada group mana pun walau aktor tidak memegang View asset value, Manage purchase, atau Manage accounting pada group (hak mengikuti tier)
34. Buka Popup Setup Column, hilangkan centang kolom Asset Value, Warranty Expiry, PO Number, dan Cost Account, klik [Save]

## Notes

- Dua blok identik dengan akun berbeda (Total Control lalu Default User); ganti akun eksplisit dan blok kedua tetap bermakna walau blok pertama gagal. Blok ditulis utuh per akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (S-03): menutup Popup Detail Group antar group dan menghilangkan centang keempat kolom pada akhir tiap blok.
- Alasan di atas ~35 langkah: dua akun pada satu dataset dan satu kelas; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-1256 dan TC-1257 menyebut 'Value Gate Child' sedangkan data akun memakai Value Gate Parent > Child; spec memakai Value Gate Child (Tabel Dinamis No 12).
  - TC-1256 butir a menyebut 'currency nol (mis. `Rp 0,00`)' tanpa menetapkan simbol mata uang client; spec mengasersi currency nol sesuai `prd-conventions.md` §32.
