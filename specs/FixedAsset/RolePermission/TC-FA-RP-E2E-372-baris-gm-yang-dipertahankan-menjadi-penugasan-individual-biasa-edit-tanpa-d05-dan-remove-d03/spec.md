---
id: TC-FA-RP-E2E-372-baris-gm-yang-dipertahankan-menjadi-penugasan-individual-biasa-edit-tanpa-d05-dan-remove-d03
title: "Baris yang dipertahankan setelah auto-revert Group Manager menjadi penugasan individual biasa: edit tanpa D-05 dan Remove memakai D-03"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1204
coverage:
  web: automated
---

# Baris yang dipertahankan setelah auto-revert Group Manager menjadi penugasan individual biasa: edit tanpa D-05 dan Remove memakai D-03

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto) dan #18 (pohon Group; `Rack A1` adalah descendant `Data Center`).
- Kondisi awal yang di-seed di hook `before` (precondition TC, tidak diasersi): state pasca auto-revert. Kevin Susanto sudah tidak Group Manager di `Data Center` tetapi masih memegang baris eks-pola `Manage group` dan `Manage files` di `Data Center` dan `Rack A1` dengan CRUD penuh sesuai kolom berlaku. Seeding lewat kemampuan seeding API yang disediakan tim FE/BE (tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri `Auto-Revert` Object `Group Manager` untuk Kevin Susanto pada Changelog Tab Group Manager sebagai baseline (langkah 1).
- State yang diubah dan pemulihannya: Delete baris `Manage group` Kevin Susanto di `Rack A1` diubah oleh langkah 5 lalu baris itu dihapus oleh langkah 11. Hook `after` memulihkan Kevin Susanto ke state Pre-setup #13 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #13 oleh automation baseline"), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1204: baris yang dipertahankan setelah auto-revert menjadi penugasan individual biasa

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri `Auto-Revert` Object `Group Manager` untuk Kevin Susanto pada Changelog Tab `Group Manager`
2. Klik Tab `System`
3. Buka Detail Role `Manage group`
4. Klik node `Rack A1` pada Sidebar Group Tree
5. Hapus centang Delete pada baris Kevin Susanto
6. Verifikasi toast sukses `Success, permissions have been updated.`
7. Verifikasi dialog auto-revert `D-05` tidak tampil
8. Klik `[⋯]` baris Kevin Susanto lalu `Remove`
9. Verifikasi dialog Remove biasa `D-03` tampil: Title `Remove User`, bullet `• Kevin S`
10. Verifikasi dialog `D-05` tidak tampil
11. Klik `[Remove]` pada dialog
12. Verifikasi toast sukses `Success, user has been removed.`
13. Klik Tab `Group Manager`
14. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
15. Verifikasi Kevin Susanto tidak ada di Tab `Group Manager`
16. Klik ikon Changelog di toolbar Tab `Group Manager`
17. Verifikasi modal Changelog Tab `Group Manager` tampil
18. Verifikasi jumlah entri `Auto-Revert` Object `Group Manager` untuk Kevin Susanto sama dengan baseline langkah 1

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 18 langkah.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog, S-12), langkah 2 sampai 4, 13, dan 16 (navigasi Tab, Detail Role, node, membuka modal Changelog). Langkah 6 menjadi anchor positif atas asersi absence dialog langkah 7, langkah 9 atas langkah 10, dan langkah 14 atas langkah 15; langkah 17 menjadi anchor atas asersi jumlah entri langkah 18.
- Langkah 18 adalah asersi jumlah entri terhadap baseline (S-12), bukan asersi kelas g (S-05, P-1): state pasca auto-revert di-seed hook `before` dan aksi edit serta Remove dijalankan spec ini sendiri. TC hanya menyebut "tidak memuat entri `Auto-Revert` baru untuk Kevin Susanto".
- Pembagian TC lintas spec: TC-FA-RP-1204 hanya ada di spec ini; spec ini men-seed state pasca auto-revert dan tidak memicu auto-revert.
- Temuan untuk QA:
  - TC-FA-RP-1204 Precondition d menyatakan state pasca auto-revert di-seed, sedangkan Pre-setup #13 menyatakan Kevin Susanto Group Manager di `Data Center`; spec men-seed state pasca auto-revert di hook `before` dan memulihkan ke #13 di hook `after`.
  - Langkah 5 dan 11 memakai baris yang sama (Delete diubah lalu baris dihapus); TC tidak menyebut apakah pengeditan memakai baris yang sama atau berbeda.
  - Expected c tidak menyebut surface log untuk "tidak memuat entri `Auto-Revert` baru"; spec memakai Changelog Tab `Group Manager` (surface tempat entri `Auto-Revert` Object `Group Manager` dicatat).
  - Post Condition "Kevin Susanto dipulihkan ke state Pre-setup #13" tidak punya langkah observasi di TC; tidak diasersi, dipulihkan di hook `after`.
  - Copy toast dan dialog D-03 diambil dari TC apa adanya.
