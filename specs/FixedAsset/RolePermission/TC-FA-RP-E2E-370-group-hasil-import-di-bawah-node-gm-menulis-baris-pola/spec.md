---
id: TC-FA-RP-E2E-370-group-hasil-import-di-bawah-node-gm-menulis-baris-pola
title: "Group hasil Import di bawah node Group Manager menulis baris pola GM dengan log Assign biasa tanpa pewarisan Standard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1184
coverage:
  web: automated
---

# Group hasil Import di bawah node Group Manager menulis baris pola GM dengan log Assign biasa tanpa pewarisan Standard

## Prerequisites

- Mode: FE+BE.
- Akun (login di hook `before`):

  | Urutan | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|---|
  | 1 (hook `before`) | Total Control, Siti Rahmawati | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login akun urutan 1 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE; hanya dibaca): #5 (Fajar Nugroho, Group Manager di `IT Infrastructure`), #13 (Kevin Susanto, Group Manager di `Data Center`), #18 (pohon Group: `Head Office` > `IT Infrastructure` > `Data Center` > `Rack A1`), #21 (seed pemegang Update `Manage asset & TAG`; tidak diasersi), #43 (seed Group Manager: Fajar Nugroho, Kevin Susanto, dan Lina Marlina di `Head Office`).
- Data Dinamis (Tabel Data Uji Dinamis TC #13; nama bersuffix `{runId}` dan nomor spec 370): Group hasil Import `GM Import {runId}-370` sebagai anak `IT Infrastructure`. Berkas Import `Fixture.fixedAssetRolePermission.berkasImportGroupGm` (belum ada; disediakan tim FE) memuat satu Group bernama `GM Import {runId}-370` dengan parent `IT Infrastructure`. Pembuatan Group (langkah 2 dan 3) adalah aksi TC yang hasilnya diasersi lewat baris pola, bukan seeding.
- Pengecualian S-11 atas pembersihan: Group dinamis tetap ada sampai akhir sesi pengujian sesuai kolom Lifecycle Tabel Data Uji Dinamis TC (#13) dan tidak dihapus di hook `after`. Alasan TC: Group menjadi bagian pohon uji sampai akhir sesi. Nama bersuffix unik per run sehingga tidak bentrok antar run.
- Kemampuan teknis: nama Group bersuffix unik sehingga baseline entri Changelog nol (S-12).
- State yang diubah dan pemulihannya: spec hanya menambah Group dinamis dan baris pola-nya (lihat pengecualian S-11 di atas); penugasan Pre-setup tidak diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1184: Group hasil Import di bawah node GM menulis baris pola GM tanpa pewarisan Standard

1. Buka Fixed Asset > Settings > Groups
2. Import Group `GM Import {runId}-370` sebagai anak `IT Infrastructure` lewat Import di Settings > Groups dengan berkas `Fixture.fixedAssetRolePermission.berkasImportGroupGm`
3. Tunggu aksi selesai: Group `GM Import {runId}-370` tampil di pohon Group
4. Buka Tab `System` lalu Detail Role `Manage files`
5. Klik node `GM Import {runId}-370` pada Sidebar Group Tree
6. Verifikasi Fajar Nugroho tampil dengan CRUD penuh sesuai kolom berlaku
7. Verifikasi Kevin Susanto dan Budi Santoso tidak tampil pada node `GM Import {runId}-370`
8. Klik Tab `Transaction Role`
9. Klik node `GM Import {runId}-370`
10. Klik sub-tab `Disposal`
11. Verifikasi Fajar Nugroho tampil di section Asset Admin dan Approver
12. Verifikasi tidak ada penugasan Standard (mis. Nadia Putri, Pandu Wijaya) pada keempat section
13. Buka Tab `System` lalu Detail Role `Manage files`
14. Klik ikon Changelog di toolbar Detail Role
15. Verifikasi entri Action `Assign` biasa (bukan `Assign (via Group Manager)`) per baris pola GM pada node `GM Import {runId}-370`
16. Verifikasi entri tersebut memuat Old Value `—`, New Value `Assigned`, dan Modified By `Siti R`
17. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 17 langkah, di bawah batas sekitar 35.
- Langkah penghubung (S-03): langkah 1 sampai 5, 8 sampai 10, 13, 14 (navigasi dan Import Group yang bukan Expected), langkah 3 (tunggu aksi selesai, 8b butir 8), langkah 17 (menutup modal Changelog). Langkah 6 dan 11 (Fajar Nugroho tampil) menjadi anchor atas langkah 7 dan 12.
- Tanpa Search pada tabel Detail Role dan tabel Role Transaksi: Group baru memuat paling banyak delapan baris dalam satu halaman, sehingga TC "cari" dipenuhi dengan membaca baris pada node itu.
- Teks Action `Assign` biasa (bukan `Assign (via Group Manager)`) mengikuti TC dan menunggu keputusan PM (Open Item #7c).
- Temuan untuk QA:
  - TC-FA-RP-1184 mengandaikan berkas Import dapat menaruh Group di bawah `IT Infrastructure` (kolom parent Import milik `settings-groups`); spec memakai berkas fixture yang disediakan tim FE dan belum dapat memastikan format kolom parent. Langkah 2 mengikuti TC.
  - TC-FA-RP-1184 Expected c hanya menyebut Changelog toolbar Detail Role `Manage files`; spec tidak mengasersi Changelog role lain.
