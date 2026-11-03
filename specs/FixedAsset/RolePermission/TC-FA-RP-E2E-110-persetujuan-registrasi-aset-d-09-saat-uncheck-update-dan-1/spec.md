---
id: TC-FA-RP-E2E-110-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-1
title: "Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (1/2)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-374
  - TC-FA-RP-375
  - TC-FA-RP-376
coverage:
  web: automated
---

# Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada `Company Isolated` (Pre-setup #35). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup: #35 `Company Isolated` (struktur group sama dengan Pre-setup #18; node `Rack A1`: Dimas Pranata satu-satunya pemegang Update pada scope node dan ancestor, toggle registrasi ON, tanpa Group Manager; node `Dock 1`: pemegang Update Budi Setiawan dan Endah Susanti, tanpa ancestor holder, toggle registrasi ON).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca nilai tersimpan checkbox Update (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: Update Dimas Pranata pada `Rack A1` dicabut lalu dicentang kembali (langkah 13), baris Dimas Pranata pada `Rack A1` dihapus oleh langkah 18. Hook `after` memulihkan Pre-setup #35 (baris Dimas Pranata dengan Read dan Update, toggle registrasi ON) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage asset & TAG`
3. Klik node `Rack A1` pada Sidebar Group Tree

### TC-FA-RP-374: Uncheck Update terakhir saat toggle ON dan node tanpa Group Manager menampilkan D-09

4. Hapus centang Update pada baris Dimas Pranata
5. Verifikasi dialog severity danger dengan Title `Remove Last Approver`, Body `• Dimas P` lalu `Rack A1 will have no approver other than Total Control while approval is required.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
6. Klik `[Cancel]`
7. Verifikasi checkbox Update baris Dimas Pranata kembali tercentang
8. Verifikasi nilai tersimpan Update baris Dimas Pranata tidak berubah lewat kemampuan baca
9. Hapus centang Update pada baris Dimas Pranata
10. Klik `[Remove]` pada dialog
11. Verifikasi checkbox Update baris Dimas Pranata tidak tercentang
12. Verifikasi toggle `Require Approval for Registration` tetap ON

### TC-FA-RP-375: Remove baris pemegang Update terakhir saat toggle ON memakai D-09 sebagai pengganti dialog Remove biasa

13. Centang Update pada baris Dimas Pranata (pemulihan precondition TC: pemegang Update terakhir)
14. Tutup toast yang tampil
15. Klik `[⋯]` baris Dimas Pranata lalu `Remove`
16. Verifikasi dialog severity danger dengan Title `Remove Last Approver`, Body `• Dimas P` lalu `Rack A1 will have no approver other than Total Control while approval is required.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` dan `[Remove]`
17. Verifikasi dialog `Remove User` biasa tidak tampil
18. Klik `[Remove]`
19. Verifikasi toast sukses `Success, user has been removed.`
20. Verifikasi baris Dimas Pranata hilang
21. Verifikasi toggle `Require Approval for Registration` tetap ON

### TC-FA-RP-376: Bulk Remove pemegang Update terakhir saat toggle ON memakai D-09 bentuk jamak

22. Klik node `Dock 1` pada Sidebar Group Tree
23. Centang baris Budi Setiawan
24. Centang baris Endah Susanti
25. Klik `Bulk Action` lalu `Remove`
26. Verifikasi dialog D-09 menggantikan dialog Bulk Remove biasa dengan Title `Remove Last Approver`, bullet `• Budi S` dan `• Endah S`, `Dock 1 will have no approver other than Total Control while approval is required.`, dan penutup `Are you sure you want to remove them?`
27. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 13 dan 14 (mengembalikan Update Dimas Pranata dan menutup toast agar TC-FA-RP-375 berprecondition pemegang Update terakhir), langkah 27 (menutup dialog D-09 tanpa menghapus baris, karena TC-FA-RP-376 hanya mengasersi dialog).
- Langkah 8 memakai kemampuan baca nilai tersimpan agar "tidak ada perubahan" pada TC-FA-RP-374 butir b teramati; TC tidak memberi cara cek lain.
- Temuan untuk QA:
  - Email akun Total Control `Company Isolated` tidak tertulis di Pre-setup; akun disediakan tim FE.
  - TC-FA-RP-374 butir b menulis "tidak ada perubahan" tanpa indikator UI; spec memakai kemampuan baca nilai tersimpan (langkah 8).
  - TC-FA-RP-375 mengharapkan Dimas Pranata sebagai pemegang Update terakhir setelah TC-FA-RP-374 mencabut Update-nya; spec mengembalikan Update lewat langkah 13 karena TC tidak menyatakan urutan ini.
