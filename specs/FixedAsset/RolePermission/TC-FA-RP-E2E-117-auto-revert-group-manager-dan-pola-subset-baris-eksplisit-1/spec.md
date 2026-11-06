---
id: TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1
title: "Auto-Revert Group Manager dan pola subset baris eksplisit (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-395
  - TC-FA-RP-396
  - TC-FA-RP-398
coverage:
  web: automated
---

# Auto-Revert Group Manager dan pola subset baris eksplisit (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #13 (Kevin Susanto, Group Manager di `Data Center`; baris pola GM di `Data Center` dan `Rack A1`: Group Role katalog selain `Manage user & role` CRUD penuh sesuai kolom berlaku dan Role Transaksi Asset Admin dan Approver pada tiap Jenis Transaksi; baris non-pola: Group Role `Manage user & role` di `Data Center`, `Manage files` Read dan Delete di `Helpdesk`, Global Role `Manage accounting` hanya Read), #18 (pohon group).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca nilai tersimpan baris Detail Role, serta membaca jumlah entri Changelog Detail Role `Manage group` dan jumlah entri ber-Action `Remove (via Group Manager)` di dalamnya sebagai baseline (langkah 1 dan 2).
- State yang diubah dan pemulihannya: penugasan Group Manager Kevin Susanto di `Data Center` dilepas oleh langkah 27 (seluruh baris pola GM dipertahankan sebagai penugasan biasa; baris `Manage group` `Data Center` berubah menjadi Delete tidak tercentang); nilai Update pada `Manage files` `Helpdesk` dan Create pada `Manage accounting` diubah oleh TC-FA-RP-398. Hook `after` memulihkan Pre-setup #13 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Changelog Detail Role `Manage group`
2. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri ber-Action `Remove (via Group Manager)` pada Changelog Detail Role `Manage group`
3. Buka Detail Role `Manage group` dari Tab `System`
4. Klik node `Data Center` pada Sidebar Group Tree

### TC-FA-RP-395: Edit CRUD baris Group Role target Group Manager di node GM-nya, dialog D-05 dan Cancel

5. Hapus centang Delete pada baris Kevin Susanto
6. Verifikasi dialog severity danger dengan Title `Remove Group Manager`, Body `• Kevin S` lalu `This edit will remove Group Manager status for this group.` lalu `Their individual role permissions will remain as edited.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
7. Klik `[Cancel]`
8. Verifikasi checkbox Delete baris Kevin Susanto kembali tercentang
9. Verifikasi tidak ada perubahan tersimpan pada Delete baris Kevin Susanto lewat kemampuan baca

### TC-FA-RP-398: Edit baris Group Role di node lain atau Global Role target Group Manager tidak terkunci dan tidak memicu auto-revert

10. Kembali ke Tab `System`
11. Buka Detail Role `Manage files`
12. Klik node `Helpdesk` pada Sidebar Group Tree
13. Centang Update pada baris Kevin Susanto
14. Verifikasi toast sukses `Success, permissions have been updated.`
15. Verifikasi dialog auto-revert tidak tampil
16. Kembali ke Tab `System`
17. Buka Detail Role `Manage accounting`
18. Centang Create pada baris Kevin Susanto
19. Verifikasi toast sukses `Success, permissions have been updated.`
20. Verifikasi dialog auto-revert tidak tampil
21. Klik Tab `Group Manager`
22. Verifikasi baris Kevin Susanto di `Data Center` tetap ada di Tab `Group Manager`

### TC-FA-RP-396: Confirm auto-revert Group Manager lewat edit CRUD, hanya penugasan GM di node itu yang lepas, seluruh baris pola GM dipertahankan termasuk baris yang diedit

23. Kembali ke Tab `System`
24. Buka Detail Role `Manage group`
25. Klik node `Data Center` pada Sidebar Group Tree
26. Hapus centang Delete pada baris Kevin Susanto
27. Klik `[Remove]` pada dialog
28. Verifikasi toast sukses `Success, permissions have been updated. Kevin Susanto is no longer Group Manager for Data Center.`
29. Verifikasi lewat kemampuan baca baris Kevin Susanto pada `Manage group` di `Data Center` tetap ada dengan Delete tidak tercentang (nilai hasil edit)
30. Verifikasi lewat kemampuan baca seluruh baris pola GM lainnya tetap ada tanpa perubahan (Group Role di `Data Center` dan `Rack A1`, Role Transaksi Asset Admin dan Approver)
31. Klik ikon Changelog Detail Role `Manage group`
32. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 1
33. Verifikasi entri `Edit` Field `Delete` untuk aksi pemicu tampil pada entri teratas sebanyak selisih
34. Verifikasi jumlah entri ber-Action `Remove (via Group Manager)` sama dengan baseline langkah 2
35. Tutup modal Changelog
36. Klik Tab `Group Manager`
37. Verifikasi sedikitnya satu baris Group Manager lain tampil di Tab `Group Manager`
38. Verifikasi baris Kevin Susanto di `Data Center` hilang dari Tab `Group Manager`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec ini memuat 38 langkah.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 395, 398, 396: TC-FA-RP-396 melepas Group Manager Kevin Susanto di `Data Center` sehingga diletakkan di akhir, dan TC-FA-RP-395 serta TC-FA-RP-398 membutuhkan Kevin Susanto masih Group Manager.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 2 (baseline Changelog, S-12), langkah 10, 16, dan 23 (kembali ke Tab `System`), langkah 35 (menutup modal Changelog). Langkah 37 adalah `Verifikasi` pembanding sebagai anchor absence atas langkah 38 (bagian 8b butir 2).
- Pembagian TC: TC-FA-RP-397 (Remove baris Group Role target Group Manager, dialog D-05 varian Remove baris) dipindah ke spec 373 pada fix pass 4 karena membutuhkan pemulihan penugasan Group Manager lewat sesi API dan akan membuat spec ini melewati 50 langkah; TC-FA-RP-397 tidak lagi ada di `sourceTc` spec ini.
- Langkah 32 sampai 34: asersi jumlah entri terhadap baseline (S-12), bukan asersi kelas g (S-05, P-1: state auto-revert dibangun oleh spec ini sendiri pada langkah 26 dan 27). Langkah 32 dan 33 adalah anchor positif (aksi pemicu tercatat) atas asersi langkah 34. Entri baru dibaca pada baris teratas urutan default Date terbaru sebanyak selisih (S-14).
- Pola toast PRD pada TC-FA-RP-396 butir d (`Success, permissions have been updated. [User Name] is no longer Group Manager for [Group Name].`) adalah penjelasan pola dari teks toast butir a; teks literal diasersi pada langkah 28.
- Post Condition TC-FA-RP-396 (log `Auto-Revert` Object `Group Manager` dan notifikasi in-app ke Kevin Susanto) tidak punya langkah observasi di TC ini (TC merujuk Section 5 dan TC-FA-RP-1189); tidak diasersi. Bagian Post Condition tentang tidak adanya entri `Remove (via Group Manager)` per baris pola diasersi pada langkah 34.
- Alasan di atas sekitar 35 langkah (38 langkah): tiga TC satu topik (Auto-Revert Group Manager Kevin Susanto) yang berbagi Detail Role, node, dan target; urutan menentukan keadaan Kevin Susanto. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-395 butir b dan TC-FA-RP-398 tidak memberi indikator UI untuk "tidak ada perubahan tersimpan"; spec memakai kemampuan baca (langkah 9).
  - TC-FA-RP-396 Expected b (baris Kevin Susanto yang diedit dan seluruh baris pola GM lain tetap ada, kini penugasan individual biasa) tidak punya langkah buka per baris di TC; spec memakai kemampuan baca (langkah 29 dan 30). Status "penugasan individual biasa" diuji TC-FA-RP-1204 (spec 372). Teks copy dialog TC-FA-RP-395 bertanda `copy usulan, PRD 12 #7` di TC.
  - TC tidak menyebut cara kembali dari Detail Role ke daftar Tab `System`; spec memakai langkah "Kembali ke Tab `System`".
