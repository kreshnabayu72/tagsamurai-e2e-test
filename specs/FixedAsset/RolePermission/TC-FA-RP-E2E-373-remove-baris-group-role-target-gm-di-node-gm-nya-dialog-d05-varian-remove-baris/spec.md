---
id: TC-FA-RP-E2E-373-remove-baris-group-role-target-gm-di-node-gm-nya-dialog-d05-varian-remove-baris
title: "Remove baris Group Role target Group Manager di node GM-nya: dialog D-05 varian Remove baris, GM lepas, baris pola lain dipertahankan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-397
coverage:
  web: automated
---

# Remove baris Group Role target Group Manager di node GM-nya: dialog D-05 varian Remove baris, GM lepas, baris pola lain dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`: Group Role katalog selain `Manage user & role` CRUD penuh sesuai kolom berlaku dan Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah entri Changelog Detail Role `Manage group` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya sebagai baseline (langkah 1 dan 2), serta membaca baris pola GM lain Kevin Susanto (langkah 12).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas dan baris Kevin Susanto pada `Manage group` `Data Center` dihapus oleh langkah 8 (baris pola GM lainnya dipertahankan sebagai penugasan biasa). Hook `before` memastikan state Pre-setup #13 dan hook `after` memulihkannya lewat fixture backend yang disediakan tim FE/BE (TC: Kevin Susanto dipulihkan ke state Pre-setup #13), tidak berasumsi langkah spec berhasil penuh. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-397: Remove baris Group Role target Group Manager di node GM-nya, dialog D-05 varian Remove baris

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Detail Role `Manage group`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Detail Role `Manage group`
3. Klik Tab `System`
4. Buka Detail Role `Manage group`
5. Klik node `Data Center` pada Sidebar Group Tree
6. Klik `[⋯]` baris Kevin Susanto lalu `Remove`
7. Verifikasi dialog severity danger dengan Title `Remove Group Manager`, Body `These users will lose Group Manager access:` lalu `• Kevin S`, dan `Are you sure you want to remove it?` (tanpa klausa tambahan di antaranya), serta tombol `[Cancel]` dan `[Remove]` (copy usulan, PRD 12 #7)
8. Klik `[Remove]`
9. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Data Center.`
10. Verifikasi sedikitnya satu baris lain tampil pada `Manage group` di `Data Center`
11. Verifikasi baris Kevin Susanto yang di-Remove pada `Manage group` di `Data Center` terhapus
12. Verifikasi lewat kemampuan baca seluruh baris pola GM lain Kevin Susanto di `Data Center` dan `Rack A1` (Group Role, Asset Admin, Approver) tetap ada
13. Klik ikon Changelog Detail Role `Manage group`
14. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 1
15. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 2
16. Tutup modal Changelog
17. Klik Tab `Group Manager`
18. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
19. Verifikasi baris Kevin Susanto di `Data Center` tidak ada di Tab `Group Manager` (GM lepas dalam satu transaksi dengan baris dihapus)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 19 langkah.
- Spec ini berdiri sendiri (tidak digabung ke spec 117): TC-FA-RP-397 melepas Group Manager Kevin Susanto di `Data Center` sehingga di spec 117 membutuhkan pemulihan penugasan lewat sesi API di tengah spec dan membuat spec itu melewati 50 langkah. Di spec ini hook `before` memastikan state Pre-setup #13.
- Langkah penghubung (S-03): langkah 1 dan 2 (baseline Changelog, S-12), langkah 3 sampai 5, 13, 16, dan 17 (navigasi Tab, Detail Role, node, membuka dan menutup modal Changelog). Langkah 10 dan 18 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 11 dan 19 (bagian 8b butir 2); langkah 14 adalah anchor positif atas asersi langkah 15.
- Langkah 14 dan 15: asersi jumlah entri terhadap baseline (S-12), bukan asersi kelas g (S-05, P-1): state auto-revert dibangun oleh spec ini sendiri pada langkah 6 sampai 8. Entri baru dibaca sebagai selisih jumlah, tanpa asersi urutan (S-14).
- Pembagian TC lintas spec: TC-FA-RP-397 hanya ada di spec ini.
- Temuan untuk QA:
  - TC-FA-RP-397 Expected b (seluruh baris pola GM lain di `Data Center` dan `Rack A1`, termasuk Role Transaksi, tetap ada) tidak punya langkah buka per baris di TC kecuali Detail Role dan Tab Transaction Role; spec memakai kemampuan baca (langkah 12). Teks copy dialog bertanda `copy usulan, PRD 12 #7` di TC.
  - Interpretasi "baris yang di-Remove oleh aksi pemicu tetap terhapus, bukan dikembalikan" menunggu konfirmasi PM.