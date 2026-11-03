---
id: TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1
title: "Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (1/4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-426
  - TC-FA-RP-427
  - TC-FA-RP-428
  - TC-FA-RP-429
  - TC-FA-RP-430
coverage:
  web: automated
---

# Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (1/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. "Sesi lain" pada TC sumber hanya memicu perubahan state (menghapus identitas pengguna, mengubah kelayakan) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; sesi lain bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso), #18 (pohon group, group `Helpdesk`). Kolam #15 disiapkan ulang lewat seeding API di awal TC yang menghapus identitas atau menetapkan penugasan (Pre-setup #32).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus identitas pengguna, menetapkan Read Only dan Group Manager, serta membaca penugasan lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi dihapus, Ahmad Fauzi ditetapkan Read Only dan Group Manager `Helpdesk` oleh langkah sesi API. Hook `after` memulihkan kolam Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

### TC-FA-RP-426: Assign Read Only, klik `[Assign]` tanpa seleksi menampilkan alert inline

1. Klik Tab `Read Only`
2. Klik `[+ Assign]` di Tab `Read Only`
3. Klik `[Assign]` tanpa memilih user
4. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
5. Verifikasi popup tetap terbuka
6. Verifikasi tidak ada penugasan Read Only tersimpan lewat kemampuan baca
7. Klik `[Cancel]`

### TC-FA-RP-427: Assign Read Only, user stale menolak seluruh submit dengan alert

8. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
9. Klik `[+ Assign]` di Tab `Read Only`
10. Centang Ahmad Fauzi dan Budi Santoso
11. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
12. Klik `[Assign]`
13. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
14. Verifikasi tidak ada penugasan Read Only dibuat lewat kemampuan baca
15. Verifikasi Budi Santoso tetap tercentang
16. Klik `[Cancel]`

### TC-FA-RP-428: Assign Read Only, user tidak lagi eligible menolak seluruh submit dengan alert

17. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
18. Klik `[+ Assign]` di Tab `Read Only`
19. Centang Ahmad Fauzi dan Budi Santoso
20. Tetapkan Read Only kepada Ahmad Fauzi lewat sesi API hingga tersimpan
21. Klik `[Assign]`
22. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
23. Verifikasi tidak ada penugasan Read Only dibuat untuk Budi Santoso lewat kemampuan baca
24. Verifikasi Budi Santoso tetap tercentang
25. Klik `[Cancel]`

### TC-FA-RP-429: Assign Group Manager, klik `[Assign]` tanpa seleksi menampilkan alert inline

26. Klik Tab `Group Manager`
27. Klik `[+ Assign]` di Tab `Group Manager`
28. Pilih group `Helpdesk`
29. Klik `[Assign]` tanpa memilih user
30. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
31. Verifikasi popup tetap terbuka
32. Verifikasi tidak ada penugasan Group Manager tersimpan lewat kemampuan baca
33. Klik `[Cancel]`

### TC-FA-RP-430: Assign Group Manager, user stale menolak seluruh submit dengan alert

34. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
35. Klik `[+ Assign]` di Tab `Group Manager`
36. Pilih group `Helpdesk`
37. Centang Ahmad Fauzi dan Budi Santoso
38. Hapus identitas Ahmad Fauzi lewat sesi API hingga terhapus
39. Klik `[Assign]`
40. Verifikasi alert inline `Ahmad Fauzi no longer exists. Please select another.`
41. Verifikasi tidak ada penugasan Group Manager dibuat lewat kemampuan baca
42. Verifikasi Budi Santoso tetap tercentang
43. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 17, dan 34 (menyiapkan kolam pengguna per TC lewat sesi API, Pre-setup #32), langkah 7, 16, 25, 33, dan 43 (menutup popup Assign dengan `[Cancel]`).
- Langkah 6, 14, 23, 32, dan 41 ("tidak ada penugasan tersimpan atau dibuat") memakai kemampuan baca penugasan karena TC tidak menyebut indikator UI.
- Alasan di atas sekitar 35 langkah (43 langkah): lima TC satu topik (alert popup Assign pada Tab `Read Only` dan Tab `Group Manager`) dengan struktur langkah seragam dan satu langkah seeding per TC. Kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-428 dan TC-FA-RP-431 menyebut "mengubah kelayakan Ahmad Fauzi (sudah memegang penugasan yang sama)" tanpa menyebut cara; spec menetapkan penugasan yang sama lewat sesi API.
  - TC-FA-RP-426 dan TC-FA-RP-429 menyebut `UI Only` pada kolom FE Test tetapi Expected "tidak ada penugasan tersimpan" menyentuh state server; spec memakai FE+BE dan kemampuan baca.
