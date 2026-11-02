---
id: TC-FA-GRP-E2E-261-tab-assets-hak-sel-bergerbang-tier-read-only-dan-group-manager
title: "Tab Assets Hak Sel Bergerbang: Tier Read Only dan Group Manager (Group yang Di-assign + Descendant, Bukan Accounting)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1258
  - TC-FA-GRP-1259
coverage:
  web: automated
---

# Tab Assets Hak Sel Bergerbang: Tier Read Only dan Group Manager (Group yang Di-assign + Descendant, Bukan Accounting)

## Prerequisites

- Mode: FE+BE.
- Akun Read Only (Pre-setup No 3): `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_RO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun groupManagerValueGate (Pre-setup No 18; tier Group Manager di-assign pada Value Gate Node A dan Value Gate Parent): `groupManagerValueGate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_GMVALUEGATE_PASSWORD`. Dipakai lewat langkah ganti akun eksplisit.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Gate Node A (Tabel Dinamis No 10, hanya dibaca, tidak diubah): G1 `Laptop Dell - 1`, G2 `Printer HP - 1`, G3 `Monitor LG - 1`, G4 `Forklift Toyota - 1`, G5 `Kabel Roll - 1`, G6 `Laptop Dell - 2`. Asset Value (Commercial): G1 1500, G2 0, G3 belum ada, G4 8000, G5 120, G6 2300. Asset Value (Fiscal): G1 1200, G2 500, G3 belum ada, G4 7000, G5 150, G6 2000. Warranty Expiry: G1 15/03/2027, G2 20/01/2027, G3 dan G5 belum ada, G4 20/05/2028, G6 01/01/2026. PO Number: G1 `PO-001`, G2 `PO-002`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `PO-006`. Cost Account: G1 `CA-100`, G2 `CA-150`, G3 belum diisi, G4 dan G5 di luar Scope, G6 `CA-200`.
- Data Value Gate Node B (Tabel Dinamis No 11, hanya dibaca): B1 `Laptop Dell - 3` (Asset Value 900, Warranty Expiry 01/06/2027, PO Number `PO-B01`, Cost Account `CA-300`), B2 `Monitor LG - 2` (tanpa nilai), B3 `Kabel Roll - 2` (tanpa nilai; di luar Scope PO Number dan Cost Account). Value Gate Child (Tabel Dinamis No 12, hanya dibaca): C1 `Laptop Dell - 4` (Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`, Cost Account `CA-400`).
- Lisensi FA-7 aktif pada client (Cost Account adalah custom field Accounting).
- Value Gate Parent (Function None) > Value Gate Child (Tabel Dinamis No 12) dipakai hanya sebagai group yang di-assign untuk akun GMV.
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE).
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1258: Hak sel bergerbang tier Read Only

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
18. Login sebagai akun groupManagerValueGate

### TC-FA-GRP-1259: Hak sel bergerbang tier Group Manager

19. Buka Detail Value Gate Node A (Tab Assets)
20. Buka Popup Setup Column, centang kolom Asset Value, Warranty Expiry, dan PO Number, klik [Save]
21. Verifikasi Value Gate Node A kolom Asset Value: G1 1500, G2 currency nol, G3 `—`
22. Verifikasi Value Gate Node A kolom Warranty Expiry: G1 15/03/2027
23. Verifikasi Value Gate Node A kolom PO Number: G1 `PO-001` (tanpa `No access`)
24. Buka Popup Setup Column
25. Verifikasi kolom Cost Account (Accounting) tidak ada di Popup Setup Column
26. Verifikasi kolom Cost Center, Insurance Policy, PO Number, dan Purchase Date ada di Popup Setup Column
27. Tutup Popup Detail Group, buka Detail Value Gate Child (Tab Assets)
28. Verifikasi kolom Asset Value, Warranty Expiry, dan PO Number tampil pada Value Gate Child tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
29. Verifikasi C1 (descendant Value Gate Parent): Asset Value 700, Warranty Expiry 09/09/2027, PO Number `PO-C01`
30. Buka Popup Setup Column, hilangkan centang kolom Asset Value, Warranty Expiry, dan PO Number, klik [Save]

## Notes

- Dua akun berurutan dengan langkah ganti akun eksplisit; blok Group Manager tetap bermakna walau blok Read Only gagal. Akun pertama (Read Only) login di hook `before`.
- Langkah penghubung (S-03): menutup Popup Detail Group antar group dan menghilangkan centang kolom pada akhir tiap blok.
- Alasan di atas ~35 langkah: tidak melewati; blok Read Only menulis ulang langkah TC secara utuh.
- Temuan untuk QA:
  - TC-1258 menyebut Value Gate Child sedangkan plan data menyebut Parent; spec memakai Value Gate Child.
