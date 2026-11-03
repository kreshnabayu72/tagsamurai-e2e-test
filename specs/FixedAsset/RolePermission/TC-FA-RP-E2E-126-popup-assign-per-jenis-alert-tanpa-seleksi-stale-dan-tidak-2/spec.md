---
id: TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2
title: "Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (2/4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-431
  - TC-FA-RP-432
  - TC-FA-RP-433
  - TC-FA-RP-434
  - TC-FA-RP-435
coverage:
  web: automated
---

# Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (2/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. "Sesi lain" pada TC sumber hanya memicu perubahan state (menghapus identitas pengguna, mengubah kelayakan) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; sesi lain bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #18 (pohon group, group `Helpdesk`). Kolam #15 disiapkan ulang lewat seeding API di awal TC yang menghapus identitas atau menetapkan penugasan (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus identitas pengguna, menetapkan Group Manager dan Global Role, serta membaca penugasan lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi dihapus, Ahmad Fauzi ditetapkan Group Manager `Helpdesk` dan Global Role `Manage Open API` oleh langkah sesi API. Hook `after` memulihkan kolam Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-431: Assign Group Manager, user tidak lagi eligible menolak seluruh submit dengan alert

1. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
2. Klik Tab `Group Manager`
3. Klik `[+ Assign]` di Tab `Group Manager`
4. Pilih group `Helpdesk`
5. Centang Ahmad Fauzi dan Budi Santoso
6. Tetapkan Ahmad Fauzi sebagai Group Manager `Helpdesk` lewat sesi API hingga tersimpan
7. Klik `[Assign]`
8. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
9. Verifikasi tidak ada penugasan Group Manager dibuat untuk Budi Santoso lewat kemampuan baca
10. Verifikasi Budi Santoso tetap tercentang
11. Klik `[Cancel]`

### TC-FA-RP-432: Assign User Global Role, klik `[Assign]` tanpa seleksi menampilkan alert inline

12. Klik Tab `System`
13. Buka Detail Role `Manage Open API`
14. Klik `[+ Assign]`
15. Klik `[Assign]` tanpa memilih user
16. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
17. Verifikasi popup tetap terbuka
18. Verifikasi tidak ada penugasan `Manage Open API` tersimpan lewat kemampuan baca
19. Klik `[Cancel]`

### TC-FA-RP-433: Assign User Global Role, user stale menolak seluruh submit dengan alert

20. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
21. Klik `[+ Assign]`
22. Centang Ahmad Fauzi dan Budi Santoso
23. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
24. Klik `[Assign]`
25. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
26. Verifikasi tidak ada penugasan dibuat lewat kemampuan baca
27. Verifikasi Budi Santoso tetap tercentang
28. Klik `[Cancel]`

### TC-FA-RP-434: Assign User Global Role, user tidak lagi eligible menolak seluruh submit dengan alert

29. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
30. Klik `[+ Assign]`
31. Centang Ahmad Fauzi dan Budi Santoso
32. Tetapkan `Manage Open API` kepada Ahmad Fauzi lewat sesi API hingga tersimpan
33. Klik `[Assign]`
34. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
35. Verifikasi tidak ada penugasan dibuat untuk Budi Santoso lewat kemampuan baca
36. Verifikasi Budi Santoso tetap tercentang
37. Klik `[Cancel]`

### TC-FA-RP-435: Assign User Group Role, klik `[Assign]` tanpa seleksi menampilkan alert inline

38. Kembali ke Tab `System`
39. Buka Detail Role `Manage files`
40. Klik `[+ Assign]`
41. Pilih group `Helpdesk`
42. Klik `[Assign]` tanpa memilih user
43. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
44. Verifikasi popup tetap terbuka
45. Verifikasi tidak ada penugasan `Manage files` tersimpan lewat kemampuan baca
46. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 20, dan 29 (menyiapkan kolam pengguna per TC lewat sesi API, Pre-setup #32), langkah 11, 19, 28, 37, dan 46 (menutup popup Assign dengan `[Cancel]`), langkah 38 (kembali ke Tab `System`).
- Langkah 9, 18, 26, 35, dan 45 ("tidak ada penugasan tersimpan atau dibuat") memakai kemampuan baca penugasan karena TC tidak menyebut indikator UI.
- Alasan di atas sekitar 35 langkah (46 langkah): lima TC satu topik (alert popup Assign pada Group Manager, Global Role, dan Group Role) dengan struktur langkah seragam dan satu langkah seeding per TC. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-431, TC-FA-RP-434, dan TC-FA-RP-437 menyebut "mengubah kelayakan Ahmad Fauzi (sudah memegang penugasan yang sama)" tanpa menyebut cara; spec menetapkan penugasan yang sama lewat sesi API.
  - TC-FA-RP-432 dan TC-FA-RP-435 menyebut `UI Only` pada kolom FE Test tetapi Expected "tidak ada penugasan tersimpan" menyentuh state server; spec memakai FE+BE dan kemampuan baca.
