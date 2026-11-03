---
id: TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3
title: "Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (3/4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-436
  - TC-FA-RP-437
  - TC-FA-RP-438
  - TC-FA-RP-439
coverage:
  web: automated
---

# Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (3/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. "Sesi lain" pada TC sumber hanya memicu perubahan state (menghapus identitas pengguna, mengubah kelayakan) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; sesi lain bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #18 (pohon group, group `Helpdesk`), #19 (Role Transaksi `IT Infrastructure` sub-tab `Disposal`; Approver Pandu Wijaya). Kolam #15 disiapkan ulang lewat seeding API di awal TC yang menghapus identitas atau menetapkan penugasan (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus identitas pengguna, menetapkan Group Role dan Approver, serta membaca penugasan lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi dihapus, Ahmad Fauzi ditetapkan `Manage files` di `Helpdesk` dan Approver pada `IT Infrastructure` sub-tab `Disposal` oleh langkah sesi API. Hook `after` memulihkan kolam Pre-setup #15 dan Pre-setup #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-436: Assign User Group Role, user stale menolak seluruh submit dengan alert

1. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
2. Klik Tab `System`
3. Buka Detail Role `Manage files`
4. Klik `[+ Assign]`
5. Pilih group `Helpdesk`
6. Centang Ahmad Fauzi dan Budi Santoso
7. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
8. Klik `[Assign]`
9. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
10. Verifikasi tidak ada penugasan dibuat lewat kemampuan baca
11. Verifikasi Budi Santoso tetap tercentang
12. Klik `[Cancel]`

### TC-FA-RP-437: Assign User Group Role, user tidak lagi eligible menolak seluruh submit dengan alert

13. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
14. Klik `[+ Assign]`
15. Pilih group `Helpdesk`
16. Centang Ahmad Fauzi dan Budi Santoso
17. Tetapkan `Manage files` di `Helpdesk` kepada Ahmad Fauzi lewat sesi API hingga tersimpan
18. Klik `[Assign]`
19. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
20. Verifikasi tidak ada penugasan dibuat untuk Budi Santoso lewat kemampuan baca
21. Verifikasi Budi Santoso tetap tercentang
22. Klik `[Cancel]`

### TC-FA-RP-438: Assign Approver, klik `[Assign]` tanpa seleksi menampilkan alert inline

23. Klik Tab `Transaction Role`
24. Klik node `IT Infrastructure` pada Sidebar Group Tree
25. Klik sub-tab `Disposal`
26. Klik `[+ Assign]` pada section Approver
27. Klik `[Assign]` tanpa memilih user
28. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
29. Verifikasi popup tetap terbuka
30. Verifikasi tidak ada penugasan Approver baru tersimpan lewat kemampuan baca
31. Klik `[Cancel]`

### TC-FA-RP-439: Assign Approver, user stale menolak seluruh submit dengan alert

32. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
33. Klik `[+ Assign]` pada section Approver
34. Centang Ahmad Fauzi dan Budi Santoso
35. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
36. Klik `[Assign]`
37. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
38. Verifikasi tidak ada penugasan dibuat lewat kemampuan baca
39. Verifikasi Budi Santoso tetap tercentang
40. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 13, dan 32 (menyiapkan kolam pengguna per TC lewat sesi API, Pre-setup #32), langkah 12, 22, 31, dan 40 (menutup popup Assign dengan `[Cancel]`).
- Langkah 10, 20, 30, dan 38 ("tidak ada penugasan tersimpan atau dibuat") memakai kemampuan baca penugasan karena TC tidak menyebut indikator UI.
- Alasan di atas sekitar 35 langkah (40 langkah): empat TC satu topik (alert popup Assign pada Group Role dan Approver) dengan struktur langkah seragam dan satu langkah seeding per TC. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-437 menyebut "mengubah kelayakan Ahmad Fauzi (sudah memegang penugasan yang sama)" tanpa menyebut cara; spec menetapkan penugasan yang sama lewat sesi API.
  - TC-FA-RP-438 menyebut `UI Only` pada kolom FE Test tetapi Expected "tidak ada penugasan tersimpan" menyentuh state server; spec memakai FE+BE dan kemampuan baca.
