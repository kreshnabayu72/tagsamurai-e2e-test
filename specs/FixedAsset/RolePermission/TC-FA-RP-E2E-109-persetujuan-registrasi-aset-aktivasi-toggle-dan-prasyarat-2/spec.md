---
id: TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2
title: "Persetujuan registrasi aset: aktivasi toggle dan prasyarat (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1031
  - TC-FA-RP-1032
  - TC-FA-RP-1033
  - TC-FA-RP-1034
coverage:
  web: automated
---

# Persetujuan registrasi aset: aktivasi toggle dan prasyarat (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor kedua (langkah 8 dan 9, ganti akun eksplisit): Total Control pada `Company Isolated` (Pre-setup #35). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Pemicu state (status user Dimas Pranata, tingkat akses Read Only, toggle registrasi) memakai sesi API akun Total Control tenant yang sama; kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18, #21 (pemegang Update Manage asset & TAG: Ahmad Fauzi di `Head Office`, Budi Santoso di `IT Infrastructure`, Dimas Pranata di `Data Center`), #35 `Company Isolated` (Dimas Pranata pemegang Update hanya di `Rack A1`; toggle registrasi `Rack A1` ON pada seed awal; Approver Pandu Wijaya pada sub-tab `Disposal` `IT Infrastructure`; tanpa Group Manager).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: mengubah Status user dan tingkat akses lewat sesi API (disediakan tim FE/BE).
- State yang diubah dan pemulihannya: toggle registrasi `Rack A1` (Company Isolated) dan `Rack A1` (Company Alpha); Status Dimas Pranata (Inactive lalu Active); Dimas Pranata dijadikan Read Only. Hook `after` memulihkan Pre-setup #21 dan #35 (toggle registrasi `Rack A1` ON pada Company Isolated, Dimas Pranata Active dan bukan Read Only) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage asset & TAG`

### TC-FA-RP-1032: Aktivasi toggle registrasi menghitung pemegang Update di ancestor node

3. Klik node `Rack A1` pada Sidebar Group Tree
4. Aktifkan toggle `Require Approval for Registration`
5. Verifikasi toast sukses `Success, permissions have been updated.`
6. Verifikasi toggle `Require Approval for Registration` ON
7. Verifikasi dialog blok tidak tampil

8. Logout dari akun Total Control Company Alpha
9. Login sebagai Total Control `Company Isolated`
10. Klik Tab `System`
11. Buka Detail Role `Manage asset & TAG`

### TC-FA-RP-1031: Aktivasi toggle registrasi tidak menghitung pemegang Update di descendant maupun Approver Role Transaksi

12. Klik node `IT Infrastructure` pada Sidebar Group Tree
13. Aktifkan toggle `Require Approval for Registration`
14. Verifikasi dialog blok severity warning dengan Title `Cannot Require Approval`, Body `Grant Update access on Manage asset & TAG to at least one user in this group before enabling approval.`, dan satu tombol `[OK]`
15. Klik `[OK]`
16. Verifikasi toggle `Require Approval for Registration` kembali OFF

### TC-FA-RP-1033: Aktivasi toggle registrasi tidak menghitung pemegang Update berstatus Inactive

17. Matikan toggle registrasi node `Rack A1` lewat sesi API hingga tersimpan (precondition TC: toggle OFF)
18. Ubah Status Dimas Pranata menjadi Inactive lewat sesi API hingga tersimpan
19. Klik node `Rack A1` pada Sidebar Group Tree
20. Aktifkan toggle `Require Approval for Registration`
21. Verifikasi dialog blok severity warning dengan Title `Cannot Require Approval`, Body `Grant Update access on Manage asset & TAG to at least one user in this group before enabling approval.`, dan satu tombol `[OK]`
22. Klik `[OK]`
23. Verifikasi toggle `Require Approval for Registration` kembali OFF
24. Ubah Status Dimas Pranata menjadi Active lewat sesi API hingga tersimpan
25. Klik node `IT Infrastructure` pada Sidebar Group Tree
26. Klik node `Rack A1` pada Sidebar Group Tree
27. Aktifkan toggle `Require Approval for Registration`
28. Verifikasi toast sukses `Success, permissions have been updated.`
29. Verifikasi toggle `Require Approval for Registration` ON

### TC-FA-RP-1034: Aktivasi toggle registrasi tidak menghitung pemegang Update yang berstatus Read Only

30. Matikan toggle `Require Approval for Registration` pada node `Rack A1` (precondition TC: toggle OFF)
31. Tutup toast yang tampil
32. Tetapkan Dimas Pranata sebagai Read Only lewat sesi API hingga tersimpan
33. Aktifkan toggle `Require Approval for Registration`
34. Verifikasi dialog blok severity warning dengan Title `Cannot Require Approval`, Body `Grant Update access on Manage asset & TAG to at least one user in this group before enabling approval.`, dan satu tombol `[OK]`
35. Klik `[OK]`
36. Verifikasi toggle `Require Approval for Registration` kembali OFF

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 1032, 1031, 1033, 1034: TC-FA-RP-1032 memakai tenant Company Alpha sedangkan tiga TC lain memakai `Company Isolated`; ganti akun eksplisit (langkah 8 dan 9) dilakukan sekali.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 15 dan 22 dan 35 (menutup dialog blok), langkah 17 (toggle `Rack A1` Company Isolated disiapkan OFF karena Pre-setup #35 menyalakannya), langkah 24 sampai 26 (mengaktifkan kembali Dimas Pranata, lalu klik node lain dan `Rack A1` agar data node dimuat ulang), langkah 30 dan 31 (mengembalikan toggle ke OFF sebagai precondition TC-FA-RP-1034 dan menutup toast).
- Langkah TC yang mengubah Status Dimas Pranata di Settings > User (TC-FA-RP-1033) dan yang meng-Assign Read Only lewat Tab `Read Only` (TC-FA-RP-1034) dijalankan lewat sesi API (langkah 18, 24, 32) karena keduanya pemicu state dan bukan objek uji; hasil aktivasi toggle yang diasersi.
- Klausa penjelasan pada Expected TC-FA-RP-1031 butir b ("pemegang Update di descendant dan Approver Role Transaksi tidak dihitung") dan TC-FA-RP-1034 butir b ("Dimas Pranata Read Only tidak dihitung walau baris Update-nya tersimpan") tidak punya keadaan teramati terpisah; keduanya terbukti lewat dialog blok dan toggle OFF pada langkah 14, 16, 34, dan 36.
- Teks bertanda `copy usulan, PRD 12 #1` (Body dialog) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Alasan di atas sekitar 35 langkah (36 langkah): semua blok satu topik (prasyarat aktivasi toggle registrasi) pada Detail Role yang sama; pergantian tenant hanya satu kali. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Email akun Total Control `Company Isolated` tidak tertulis di Pre-setup; akun disediakan tim FE.
  - TC-FA-RP-1033 dan TC-FA-RP-1034 menyebut toggle registrasi `Rack A1` OFF, sedangkan Pre-setup #35 menyatakan toggle itu ON; spec menyiapkan OFF (langkah 17 dan 30).
  - TC-FA-RP-1033 tidak menyebut cara mengubah Status di Settings > User (kontrol dan label); spec memakai sesi API.
