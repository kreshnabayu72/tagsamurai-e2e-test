---
id: TC-FA-RP-E2E-111-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-2
title: "Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-377
  - TC-FA-RP-378
  - TC-FA-RP-379
coverage:
  web: automated
---

# Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor kedua (langkah 8 dan 9, ganti akun eksplisit): Total Control pada `Company Isolated` (Pre-setup #35). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Pemicu state (toggle registrasi, penugasan Group Manager) memakai sesi API akun Total Control tenant yang sama; kemampuan sesi API disediakan tim BE/FE.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18, #21 (pemegang Update Manage asset & TAG: Ahmad Fauzi di `Head Office`, Budi Santoso di `IT Infrastructure`, Dimas Pranata di `Data Center`), #35 `Company Isolated` (Dimas Pranata pemegang Update hanya di `Rack A1`, toggle registrasi `Rack A1` ON, tanpa Group Manager), Kevin Susanto (Pre-setup #13, dipakai sebagai Group Manager `Rack A1` pada TC-FA-RP-377).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: toggle registrasi dan Update Dimas Pranata pada `Data Center` (Company Alpha); penugasan Group Manager Kevin Susanto pada `Rack A1`; Update dan baris Dimas Pranata pada `Rack A1` (Company Isolated). Hook `after` memulihkan Pre-setup #21 dan #35 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Aktifkan toggle registrasi node `Data Center` lewat sesi API hingga tersimpan (precondition TC-FA-RP-378: toggle ON)
2. Klik Tab `System`
3. Buka Detail Role `Manage asset & TAG`
4. Klik node `Data Center` pada Sidebar Group Tree

### TC-FA-RP-378: Uncheck Update saat masih ada pemegang Update lain tidak memicu D-09

5. Hapus centang Update pada baris Dimas Pranata
6. Verifikasi toast sukses `Success, permissions have been updated.`
7. Verifikasi dialog tidak tampil

8. Logout dari akun Total Control Company Alpha
9. Login sebagai Total Control `Company Isolated`
10. Klik Tab `System`
11. Buka Detail Role `Manage asset & TAG`

### TC-FA-RP-377: Uncheck Update terakhir saat node punya Group Manager aktif tidak memicu D-09

12. Tugaskan Kevin Susanto sebagai Group Manager di `Rack A1` lewat sesi API hingga tersimpan (precondition TC)
13. Klik node `Rack A1` pada Sidebar Group Tree
14. Hapus centang Update pada baris Dimas Pranata
15. Verifikasi toast sukses `Success, permissions have been updated.`
16. Verifikasi checkbox Update baris Dimas Pranata tidak tercentang
17. Verifikasi dialog tidak tampil
18. Verifikasi toggle `Require Approval for Registration` tetap ON
19. Centang Update pada baris Dimas Pranata (pemulihan state pemegang Update terakhir)
20. Tutup toast yang tampil

### TC-FA-RP-379: Melepas penugasan Group Role lewat popup Assign Group Role di Settings > User tidak memicu D-09 dan tidak diblokir

21. Lepas penugasan Group Manager Kevin Susanto dari `Rack A1` lewat sesi API hingga tersimpan (precondition TC: tanpa Group Manager)
22. Buka Settings > User > Detail Dimas Pranata > Tab Role sub-tab Group Role
23. Buka popup Assign Group Role
24. Hapus penugasan `Manage asset & TAG` di `Rack A1`
25. Klik `[Save]`
26. Verifikasi pelepasan berhasil dan popup Assign Group Role tertutup
27. Verifikasi dialog D-09 tidak tampil
28. Buka menu Settings > Role & Permission dari sidebar
29. Klik Tab `System`
30. Buka Detail Role `Manage asset & TAG`
31. Klik node `Rack A1` pada Sidebar Group Tree
32. Verifikasi toggle `Require Approval for Registration` tetap ON
33. Verifikasi baris Dimas Pranata dihapus permanen dari tabel penugasan Detail Role `Manage asset & TAG` di `Rack A1`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 378, 377, 379: TC-FA-RP-378 memakai Company Alpha, dua TC lain memakai `Company Isolated`; ganti akun eksplisit (langkah 8 dan 9) dilakukan sekali.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 19 dan 20 (mengembalikan Update Dimas Pranata dan menutup toast agar TC-FA-RP-379 berprecondition pemegang Update terakhir), langkah 21 (melepas Group Manager Kevin Susanto karena TC-FA-RP-379 mensyaratkan tanpa Group Manager), langkah 28 sampai 31 (membuka kembali Detail Role).
- Langkah 5 memakai node `Data Center` pada Company Alpha; Update Dimas Pranata dipulihkan oleh hook `after`.
- Temuan untuk QA:
  - Email akun Total Control `Company Isolated` tidak tertulis di Pre-setup; akun disediakan tim FE.
  - TC-FA-RP-379 menyebut tombol "simpan" pada popup Assign Group Role tanpa label; spec memakai `[Save]` mengikuti konvensi label form Edit.
  - TC-FA-RP-379 butir a ("Pelepasan berhasil") tidak menyebut indikator selain popup tertutup; spec memakai itu (langkah 26).
  - TC-FA-RP-378 butir "Tidak ada dialog" tidak menyebut cara membuktikan state sesudah klik; spec mendahuluinya dengan toast sukses sebagai anchor (langkah 6).
