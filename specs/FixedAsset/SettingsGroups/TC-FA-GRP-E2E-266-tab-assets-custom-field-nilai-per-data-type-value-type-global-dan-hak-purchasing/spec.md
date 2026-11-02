---
id: TC-FA-GRP-E2E-266-tab-assets-custom-field-nilai-per-data-type-value-type-global-dan-hak-purchasing
title: "Tab Assets Custom Field: Nilai Sesuai Data Type, Dash untuk Belum Diisi/Di Luar Scope, Value Type Global, dan No Access Purchasing di Group Lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1230
  - TC-FA-GRP-1231
  - TC-FA-GRP-1232
coverage:
  web: automated
---

# Tab Assets Custom Field: Nilai Sesuai Data Type, Dash untuk Belum Diisi/Di Luar Scope, Value Type Global, dan No Access Purchasing di Group Lain

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: allValueAccess (Pre-setup No 17: Group Role Manage purchase pada Value Gate Node A, Global Role Manage accounting, lisensi FA-7 aktif) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; managePurchaseGroups (Pre-setup No 14: Group Role Manage purchase pada Value Gate Node A saja; Manage Group R pada node yang sama dengan No 12) `managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`.
- Data Pre-setup tambahan (hanya dibaca, tidak diubah): Value Gate Node A (Tabel Dinamis No 10, aset G1-G6) dan Value Gate Node B (No 11, aset B1-B3); custom field Cost Center, Insurance Policy, PO Number, Purchase Date, Cost Account (No 13). Kedua node memakai nama literal Pre-setup yang dibaca bersama (tanpa seeding per spec dan tanpa cleanup; sama seperti 253 sampai 265); semua langkah dan asersi memakai nama itu.
- Nilai uji (diacu dari fixture spec): Cost Center G1 `CC-ALPHA`, G2 `CC-GAMMA`, G4 `CC-ALPHA`, G6 `CC-BETA`, G3 belum diisi, G5 di luar Scope; PO Number G1 `PO-001`, G2 `PO-002`, G6 `PO-006`, G3 belum diisi, G4 dan G5 di luar Scope; Purchase Date G1 10/02/2026, G2 01/03/2026, G4 01/04/2026, G5 05/05/2026, G6 01/03/2026, G3 belum diisi; Cost Account G1 `CA-100`, G2 `CA-150`, G6 `CA-200`, G3, G4, G5 tanpa nilai; Insurance Policy `INS-2026` (Value Type Global, Scope Laptop Dell) untuk G1 dan G6.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser agar tabel berada pada konfigurasi default; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah.

## Test Steps

### TC-1230: Kolom Custom Field bernilai sesuai Data Type; belum diisi atau di luar Scope tampil `—`
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Cost Center, PO Number, Purchase Date, dan Cost Account, klik [Save]
3. Verifikasi Cost Center: G1 `CC-ALPHA`, G2 `CC-GAMMA`, G4 `CC-ALPHA`, G6 `CC-BETA`
4. Verifikasi Cost Center G3 `—` (belum diisi)
5. Verifikasi Cost Center G5 `—` (Asset Name Kabel Roll di luar Scope field)
6. Verifikasi PO Number: G1 `PO-001`, G2 `PO-002`, G6 `PO-006`
7. Verifikasi PO Number G3 `—` (belum diisi)
8. Verifikasi PO Number G4 dan G5 `—` (di luar Scope field)
9. Verifikasi Purchase Date (Data Type Date, Scope General): G1 10/02/2026, G2 01/03/2026, G4 01/04/2026, G5 05/05/2026, G6 01/03/2026 (format General Settings)
10. Verifikasi Purchase Date G3 `—` (belum diisi)
11. Verifikasi Cost Account: G1 `CA-100`, G2 `CA-150`, G6 `CA-200`
12. Verifikasi Cost Account G3, G4, G5 `—`
13. Verifikasi tidak ada sel `No access` pada keempat kolom
### TC-1231: Custom Field Value Type Global menampilkan nilai yang sama pada semua unit Asset Name dalam Scope
14. Ganti akun: Logout, login sebagai Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`), buka Fixed Asset > Settings > Groups
15. Buka Detail Value Gate Node A (Tab Assets)
16. Buka Popup Setup Column, centang kolom Insurance Policy, klik [Save]
17. Verifikasi Insurance Policy G1 dan G6 (Laptop Dell) sama-sama `INS-2026`
18. Verifikasi Insurance Policy G2, G3, G4, G5 (Asset Name di luar Scope) `—`
### TC-1232: Custom field Purchasing: pemegang Manage purchase di group lain melihat `No access`; field General tetap bernilai
19. Ganti akun: Logout, login sebagai managePurchaseGroups (`managePurchaseGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_MANAGEPURCHASE_PASSWORD`), buka Fixed Asset > Settings > Groups
20. Buka Detail Value Gate Node B (Tab Assets)
21. Buka Popup Setup Column, centang kolom Cost Center, Insurance Policy, PO Number, dan Purchase Date, klik [Save]
22. Verifikasi PO Number B1 dan B2 `No access`
23. Verifikasi PO Number B3 `—` (Kabel Roll di luar Scope; `—` mengalahkan `No access`)
24. Verifikasi Purchase Date (Scope General) B1, B2, dan B3 `No access`
25. Hover sel `No access`
26. Verifikasi tooltip sel "Requires Manage purchase access in this group."
27. Verifikasi Cost Center (General) B1 `CC-ALPHA`
28. Verifikasi Cost Center B2 `—` (belum diisi) dan B3 `—` (di luar Scope)
29. Verifikasi Insurance Policy B1 `INS-2026` (field grup General tidak bergerbang)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): dua langkah Ganti akun (aktor berhak berbeda per TC; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal).
- Urutan: TC-1230, TC-1231, TC-1232; TC-1232 terakhir karena mengganti akun ke aktor yang tidak berhak di Value Gate Node B.
- Alasan di atas ~35 langkah: ketiga TC satu kelas (fungsional baca kolom Custom Field Tab Assets), dataset sama, dan tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah ganti akun eksplisit, tanpa kelas harness lain.
- Temuan untuk QA:
  - TC-1230 Expected e dan TC-1232 menyebut aktor "berhak"; Pre-setup No 17 dan No 14 tidak menyebut email client khusus. Akun mengikuti Pre-setup, password dari env `FA_GRP_*` yang didaftarkan tim FE.
