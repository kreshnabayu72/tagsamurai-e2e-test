---
id: TC-FA-RP-E2E-321-role-matrix-gating-remove-baris-pola-transaction-role-per-peran
title: "Role Matrix: gating Remove baris pola Transaction Role per peran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1150
coverage:
  web: automated
---

# Role Matrix: gating Remove baris pola Transaction Role per peran

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Hendra Wijaya); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Identitas Pre-setup mengacu ke fixture `Fixture.fixedAssetRolePermission` (belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-FA-RP-1150 | Manage global user & role (Update) | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| TC-FA-RP-1150 | Group Manager | Fajar Nugroho (Pre-setup #5; Group Manager di `IT Infrastructure`) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup: #18 (pohon Group), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Monitoring & Report Oscar Pratama, Staff Putri Wulandari, Approver Pandu Wijaya; baris pola Asset Admin dan Approver untuk Rina Wulandari, Monitoring & Report untuk Maya Anggraeni), #3 (Rina Wulandari, Total Control), #12 (Maya Anggraeni, Read Only). Target baris manual Standard untuk `Remove` Enabled: Nadia Putri (Asset Admin). Tiap section pada sub-tab itu memuat paling banyak enam baris (Pre-setup #19), sehingga tabel tidak melewati satu halaman.
- Spec tidak mengubah data; tidak ada seeding dan pemulihan selain sesi yang dikembalikan hook `after`.
- Env var yang dipakai: `FA_MUR_GLOBAL_PASSWORD`, `FA_GM_PASSWORD`, `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1150: Gating Remove baris pola Transaction Role: Disabled bagi aktor selain Default User/Total Control pada seluruh role pola, termasuk Approver

#### Blok role: Manage global user & role (Update), Hendra Wijaya (login di hook `before`)

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Klik `[⋯]` baris Rina Wulandari pada section Asset Admin lalu hover `Remove`
5. Verifikasi aksi `Remove` untuk baris Asset Admin Rina Wulandari (Total Control) Disabled dengan tooltip `You don't have permission to edit.`
6. Tekan Esc untuk menutup dropdown
7. Klik `[⋯]` baris Rina Wulandari pada section Approver lalu hover `Remove`
8. Verifikasi aksi `Remove` untuk baris Approver Rina Wulandari (Total Control) Disabled dengan tooltip `You don't have permission to edit.`
9. Tekan Esc untuk menutup dropdown
10. Klik `[⋯]` baris Maya Anggraeni pada section Monitoring & Report lalu hover `Remove`
11. Verifikasi aksi `Remove` untuk baris Monitoring & Report Maya Anggraeni (Read Only) Disabled dengan tooltip `You don't have permission to edit.`
12. Tekan Esc untuk menutup dropdown
13. Klik `[⋯]` baris Nadia Putri pada section Asset Admin lalu hover `Remove`
14. Verifikasi aksi `Remove` untuk baris manual Nadia Putri (Standard) Enabled
15. Tekan Esc untuk menutup dropdown

#### Blok role: Group Manager, Fajar Nugroho (ganti akun)

16. Logout dari akun Hendra Wijaya
17. Login sebagai Group Manager Fajar Nugroho dengan `Spectra.env.FA_GM_PASSWORD`
18. Buka Fixed Asset > Settings > Role & Permission
19. Klik Tab `Transaction Role`
20. Klik node `IT Infrastructure` di Sidebar Group Tree
21. Klik sub-tab `Disposal`
22. Klik `[⋯]` baris Rina Wulandari pada section Asset Admin lalu hover `Remove`
23. Verifikasi aksi `Remove` untuk baris Asset Admin Rina Wulandari (Total Control) Disabled dengan tooltip `You don't have permission to edit.`
24. Tekan Esc untuk menutup dropdown
25. Klik `[⋯]` baris Rina Wulandari pada section Approver lalu hover `Remove`
26. Verifikasi aksi `Remove` untuk baris Approver Rina Wulandari (Total Control) Disabled dengan tooltip `You don't have permission to edit.`
27. Tekan Esc untuk menutup dropdown
28. Klik `[⋯]` baris Maya Anggraeni pada section Monitoring & Report lalu hover `Remove`
29. Verifikasi aksi `Remove` untuk baris Monitoring & Report Maya Anggraeni (Read Only) Disabled dengan tooltip `You don't have permission to edit.`
30. Tekan Esc untuk menutup dropdown
31. Klik `[⋯]` baris Nadia Putri pada section Asset Admin lalu hover `Remove`
32. Verifikasi aksi `Remove` untuk baris manual Nadia Putri (Standard) Enabled
33. Tekan Esc untuk menutup dropdown

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular; subjudul `####` memisahkan blok role. Spec ini memuat 33 langkah.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; langkah 16 sampai 18 adalah ganti akun, S-07). Langkah blok kedua mengulang langkah 1 sampai 15 sesuai langkah 3 TC ("Ulangi sebagai Group Manager").
- Langkah penghubung (S-03): langkah 1 sampai 3 dan 19 sampai 21 (membuka tabel Role Transaksi), langkah 6, 9, 12, 15, 24, 27, 30, 33 (menutup dropdown), langkah 16 sampai 18 (ganti akun dan membuka halaman).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Spec memuat polaritas campuran (Disabled untuk baris pola, Enabled untuk baris manual Standard) karena keduanya klausa satu TC (matriks visibilitas, bagian 3a).
- Temuan untuk QA:
  - TC-FA-RP-1150 kolom Acc memotong aktor ("Manage global user & role (Update) lalu Group Manager") tanpa akun Pre-setup eksplisit; spec mengasumsikan Hendra Wijaya (Pre-setup #6, `FA_MUR_GLOBAL_PASSWORD`) dan Fajar Nugroho (Pre-setup #5, `FA_GM_PASSWORD`), diambil dari `suite.md` dan langkah 3 TC yang menyebut Fajar Nugroho.
  - Expected c "baris manual target Standard" tidak menyebut nama; spec memakai Nadia Putri (Asset Admin, Pre-setup #19) sebagai asumsi.
  - Expected a menyebut dua baris Rina Wulandari (Asset Admin dan Approver) sebagai satu butir; spec memecahnya per baris menjadi dua `Verifikasi`.
  - Langkah 2 TC menyebut "baris pola Rina Wulandari (Asset Admin dan Approver)" tanpa menyebut section; spec membuka tiap baris pada section masing-masing.
  - Tidak ada Post Condition TC; tidak ada yang tidak diasersi.
