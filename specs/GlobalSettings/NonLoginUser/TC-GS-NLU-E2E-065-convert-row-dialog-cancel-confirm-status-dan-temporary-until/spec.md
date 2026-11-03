---
id: TC-GS-NLU-E2E-065-convert-row-dialog-cancel-confirm-status-dan-temporary-until
title: "Convert Row: Dialog, Cancel, Confirm, serta Status dan Temporary Until"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-232
  - TC-GS-NLU-233
  - TC-GS-NLU-234
  - TC-GS-NLU-236
coverage:
  web: automated
---

# Convert Row: Dialog, Cancel, Confirm, serta Status dan Temporary Until

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Rani Lestari {runId}-065` (Active, Position Driver, Email `rani.lestari+{runId}-065@qwertysystem.net`), `Pertahan Satu {runId}-065` (Inactive, Temporary Until masa depan +30 hari, Email `pertahansatu+{runId}-065@qwertysystem.net`). Pengganti Rani Lestari dan Pertahan Satu Pre-setup No. 11 karena Convert mengubah tipe record (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Mail-catcher: inbox per alamat email dapat dibaca dan jumlah email per alamat dapat dicatat sebelum aksi (baseline; kemampuan disediakan tim FE/BE).
- Entri Login User hasil Convert dibersihkan hook `after` (hapus lewat API); Changelog bersifat permanen, asersi entri memakai nama bersuffix unik (baseline nol).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-232: Screening dialog Convert to Login User row

1. Ketik Search `Rani Lestari {runId}-065`, tekan Enter
2. Klik `⋯` pada baris `Rani Lestari {runId}-065` > `Convert to Login User`
3. Verifikasi dialog dengan Title `Convert to Login User`, body bullet `Rani Lestari {runId}-065` lalu `This user will become a login user. An activation email will be sent to rani.lestari+{runId}-065@qwertysystem.net. This action cannot be undone. Are you sure you want to convert it?`, dan tombol `[Cancel]` dan `[Convert]`

### TC-GS-NLU-233: Cancel pada dialog Convert row

4. Klik area gelap di luar dialog
5. Verifikasi backdrop tidak menutup dialog
6. Klik `[Cancel]`
7. Verifikasi dialog menutup
8. Verifikasi `Rani Lestari {runId}-065` tetap di tabel Non-Login User

### TC-GS-NLU-234: Confirm Convert row

9. Klik `⋯` pada baris `Rani Lestari {runId}-065` > `Convert to Login User`
10. Klik `[Convert]`
11. Verifikasi toast sukses: `Success, Rani Lestari {runId}-065 has been converted to a login user.`
12. Verifikasi baris `Rani Lestari {runId}-065` hilang dari sub-tab Non-Login User
13. Klik sub-tab `Login User`
14. Ketik Search `Rani Lestari {runId}-065`, tekan Enter
15. Verifikasi baris `Rani Lestari {runId}-065` muncul di sub-tab Login User
16. Verifikasi badge `Pending Activation` pada baris itu

### TC-GS-NLU-236: Convert mempertahankan status Inactive dan Temporary Until

17. Klik sub-tab `Non-Login User`
18. Ketik Search `Pertahan Satu {runId}-065`, tekan Enter
19. Klik `⋯` pada baris `Pertahan Satu {runId}-065` > `Convert to Login User`
20. Klik `[Convert]`
21. Verifikasi toast sukses: `Success, Pertahan Satu {runId}-065 has been converted to a login user.`
22. Klik sub-tab `Login User`
23. Ketik Search `Pertahan Satu {runId}-065`, tekan Enter
24. Klik teks Name `Pertahan Satu {runId}-065` untuk membuka Detail Login User
25. Verifikasi user tetap Inactive (switch header OFF)
26. Verifikasi Temporary Until tetap sama dengan nilai seeding
27. Verifikasi akun berstatus Pending Activation

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 17, 22, 24.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 14, 18, 23.
- Setelah toast sukses TC-234 dan TC-236 baris dikonversi; langkah penghubung ke sub-tab `Login User` dan kembali ke `Non-Login User` mengikuti Langkah Uji TC-234 dan TC-236.
- Pembagian TC lintas spec: Convert dengan klik ganda (TC-450) dan Convert dari menu Detail (TC-237) ada di spec 131.
- Last Name memuat suffix; nama toast memakai Full Name bersuffix sesuai teks `[Full Name]` pada TC-237.
- Temuan untuk QA:
  - TC-234 Post Condition (tipe Login User berstatus Pending Activation tanpa Access, Tab Non-Login User Represented By lama tidak lagi memuat Rani Lestari, entri Changelog/Activity Log/System Log `Convert to Login User`, email aktivasi terkirim) tanpa langkah observasi di TC; tidak diasersi.
  - TC-236 Expected a hanya menyebut "Toast sukses" tanpa teks; spec memakai teks toast Convert dari TC-234.
