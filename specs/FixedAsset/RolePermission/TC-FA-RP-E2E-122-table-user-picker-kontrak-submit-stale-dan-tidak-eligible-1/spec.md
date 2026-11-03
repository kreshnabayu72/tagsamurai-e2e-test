---
id: TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1
title: "Table User Picker: kontrak submit stale dan tidak eligible (1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-413
  - TC-FA-RP-414
  - TC-FA-RP-415
  - TC-FA-RP-416
coverage:
  web: automated
---

# Table User Picker: kontrak submit stale dan tidak eligible (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. Sesi 2 pada TC sumber hanya memicu perubahan state (menghapus identitas pengguna, meng-Assign Total Control) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; Sesi 2 bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso, Budi Setiawan, Dimas Pranata, Citra Lestari, Endah Susanti). Kolam #15 disiapkan ulang lewat seeding API di awal tiap TC karena langkah menghapus identitas pengguna (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus identitas pengguna, meng-Assign Total Control, dan membaca tingkat akses lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi, Budi Santoso, dan Budi Setiawan dihapus dan tingkat akses Total Control Ahmad Fauzi ditetapkan. Hook `after` memulihkan kolam Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-413: Submit Assign, satu user stale menolak seluruh submit, hanya centangan user itu auto-clear

1. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
2. Klik `[+ Assign]` di Tab `Total Control`
3. Centang Ahmad Fauzi dan Budi Santoso
4. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
5. Klik `[Assign]`
6. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
7. Verifikasi tidak ada penugasan Total Control dibuat untuk Budi Santoso lewat kemampuan baca
8. Verifikasi centangan Ahmad Fauzi auto-clear
9. Verifikasi Budi Santoso tetap tercentang
10. Verifikasi daftar picker di-refetch sehingga Ahmad Fauzi tidak lagi tampil di daftar
11. Klik `[Cancel]`

### TC-FA-RP-414: Submit Assign, tiga user stale menyebut semua nama dalam satu alert

12. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
13. Klik `[+ Assign]` di Tab `Total Control`
14. Centang Ahmad Fauzi, Budi Santoso, Budi Setiawan, dan Dimas Pranata
15. Hapus identitas Ahmad Fauzi, Budi Santoso, dan Budi Setiawan lewat sesi API hingga terhapus
16. Klik `[Assign]`
17. Verifikasi alert inline `Ahmad Fauzi, Budi Santoso, and Budi Setiawan no longer exist. Please select another.`
18. Verifikasi Dimas Pranata tetap tercentang
19. Verifikasi tidak ada penugasan Total Control dibuat lewat kemampuan baca
20. Klik `[Cancel]`

### TC-FA-RP-415: Submit Assign, dua user stale tanpa koma sebelum and

21. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
22. Klik `[+ Assign]` di Tab `Total Control`
23. Centang Ahmad Fauzi dan Budi Santoso
24. Hapus identitas Ahmad Fauzi dan Budi Santoso lewat sesi API hingga terhapus
25. Klik `[Assign]`
26. Verifikasi alert inline `Ahmad Fauzi and Budi Santoso no longer exist. Please select another.`
27. Klik `[Cancel]`

### TC-FA-RP-416: Submit Assign, satu user tidak lagi eligible menolak seluruh submit

28. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
29. Klik `[+ Assign]` di Tab `Total Control`
30. Centang Ahmad Fauzi dan Budi Santoso
31. Tetapkan Total Control kepada Ahmad Fauzi lewat sesi API hingga tersimpan
32. Klik `[Assign]`
33. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
34. Verifikasi tidak ada penugasan Total Control dibuat untuk Budi Santoso lewat kemampuan baca
35. Verifikasi centangan Ahmad Fauzi auto-clear
36. Verifikasi Budi Santoso tetap tercentang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 12, 21, dan 28 (menyiapkan kolam pengguna per TC lewat sesi API karena langkah menghapus identitas pengguna, Pre-setup #32), langkah 11, 20, dan 27 (menutup popup Assign dengan `[Cancel]`).
- Pembagian TC lintas spec: klausa "Tidak ada entri log" pada TC-FA-RP-413 butir d diasersi di spec absence log (spec 291); spec ini mengasersi alert, penugasan, centangan, dan refetch. Id TC tetap di `sourceTc` spec ini.
- Langkah 7, 19, dan 34 ("tidak ada penugasan dibuat") memakai kemampuan baca tingkat akses karena TC tidak menyebut indikator UI.
- Alasan di atas sekitar 35 langkah (36 langkah): empat TC satu topik (kontrak submit stale dan tidak eligible pada popup Assign Total Control) dengan satu langkah seeding per TC. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-413 butir c menyebut "daftar picker di-refetch" tanpa indikator yang teramati; spec mengasersi Ahmad Fauzi tidak lagi tampil di daftar (langkah 10).
  - TC-FA-RP-416 menulis "meng-Assign Total Control ke Ahmad Fauzi" oleh Sesi 2 tanpa menyebut cara; spec memakai sesi API.
