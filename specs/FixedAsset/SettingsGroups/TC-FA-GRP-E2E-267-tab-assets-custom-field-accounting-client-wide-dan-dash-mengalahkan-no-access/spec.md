---
id: TC-FA-GRP-E2E-267-tab-assets-custom-field-accounting-client-wide-dan-dash-mengalahkan-no-access
title: "Tab Assets Custom Field Accounting: Pemegang Manage Accounting Melihat Nilai Client-Wide dan Dash Mengalahkan No Access"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1233
  - TC-FA-GRP-1260
coverage:
  web: automated
---

# Tab Assets Custom Field Accounting: Pemegang Manage Accounting Melihat Nilai Client-Wide dan Dash Mengalahkan No Access

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: manageAccountingGroups (Pre-setup No 13: Global Role Manage accounting, lisensi FA-7 aktif, Manage Group R pada node yang sama dengan No 12) `manageAccountingGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEACCOUNTING_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): managePurchaseGroups (Pre-setup No 14) `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`.
- Data Pre-setup tambahan (hanya dibaca, tidak diubah): Value Gate Node A (Tabel Dinamis No 10, G1-G6), Value Gate Node B (No 11, B1-B3), Value Gate Parent > Value Gate Child (No 12, aset C1). Semua node memakai nama literal Pre-setup yang dibaca bersama (tanpa seeding per spec dan tanpa cleanup; sama seperti 253 sampai 265); langkah dan asersi memakai nama itu. Lisensi FA-7 aktif pada client uji.
- Nilai uji (diacu dari fixture spec): Cost Account G1 `CA-100`, G2 `CA-150`, G6 `CA-200`, G3/G4/G5 tanpa nilai; B1 `CA-300`, B2 dan B3 tanpa nilai; C1 `CA-400`. TC-1260: PO Number (Scope Laptop Dell, Printer HP, Monitor LG), Cost Center (General), Purchase Date (Scope General), Asset Value, dan Warranty Expiry pada B1 `Laptop Dell - 3`, B2 `Monitor LG - 2`, B3 `Kabel Roll - 2`; aktor TC-1260 tidak memegang Manage purchase pada Value Gate Node B.
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah.

## Test Steps

### TC-1233: Custom field Accounting: pemegang Manage accounting melihat nilai di seluruh group (client-wide)
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Cost Account, klik [Save]
3. Verifikasi Cost Account Value Gate Node A: G1 `CA-100`, G2 `CA-150`, G6 `CA-200`
4. Verifikasi Cost Account G3, G4, G5 `—`
5. Tutup Popup Detail Group; buka Detail Value Gate Node B
6. Verifikasi kolom Cost Account tampil pada Value Gate Node B tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
7. Verifikasi Cost Account Value Gate Node B: B1 `CA-300`
8. Verifikasi Cost Account B2 dan B3 `—`
9. Tutup Popup Detail Group; buka Detail Value Gate Child
10. Verifikasi kolom Cost Account tampil pada Value Gate Child tanpa dicentang ulang (preferensi Setup Column per akun, berlaku lintas group)
11. Verifikasi Cost Account Value Gate Child: C1 `CA-400`
12. Verifikasi tidak ada sel `No access` pada Value Gate Child
### TC-1260: `—` mengalahkan `No access` untuk custom field yang tidak berlaku bagi Asset Name aset
13. Ganti akun: Logout, login sebagai managePurchaseGroups (`managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`), buka Fixed Asset > Settings > Groups
14. Buka Detail Value Gate Node B (Tab Assets)
15. Buka Popup Setup Column, centang kolom Asset Value, Warranty Expiry, Cost Center, PO Number, dan Purchase Date, klik [Save]
16. Verifikasi PO Number B1 dan B2 `No access` (field berlaku, aktor tidak berhak)
17. Verifikasi PO Number B3 `—` (field tidak berlaku bagi Kabel Roll, tanpa memandang hak)
18. Verifikasi Cost Center (General) B3 `—` (di luar Scope)
19. Verifikasi Purchase Date (Scope General) B1, B2, dan B3 `No access`
20. Verifikasi Asset Value dan Warranty Expiry B1, B2, dan B3 `No access`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Tutup Popup Detail Group" sebelum membuka node lain pada TC-1233 (langkah 5 dan 9); satu langkah Ganti akun sebelum TC-1260 (aktor berbeda; bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal). Navigasi ke Value Gate Node B dan Value Gate Child mengikuti Langkah TC.
- Temuan untuk QA:
  - TC-1260 Expected b menulis Cost Center (General) hanya untuk B3; nilai B1/B2 tidak diasersi karena tidak ada di Expected.
