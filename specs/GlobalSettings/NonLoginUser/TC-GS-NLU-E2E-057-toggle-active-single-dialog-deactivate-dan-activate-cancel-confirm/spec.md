---
id: TC-GS-NLU-E2E-057-toggle-active-single-dialog-deactivate-dan-activate-cancel-confirm
title: "Toggle Active Single: Dialog Deactivate dan Activate, Cancel, dan Confirm"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-197
  - TC-GS-NLU-198
  - TC-GS-NLU-199
  - TC-GS-NLU-200
  - TC-GS-NLU-201
  - TC-GS-NLU-202
coverage:
  web: automated
---

# Toggle Active Single: Dialog Deactivate dan Activate, Cancel, dan Confirm

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Rina Marlina {runId}-057` (Active, Position Driver, Division Logistics, Temporary +30 hari) dan `Joko Susilo {runId}-057` (Inactive manual, Position Contractor). Pengganti Rina Marlina dan Joko Susilo Pre-setup No. 11 karena spec mengubah statusnya (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Waktu: jam server dan jam browser sinkron; asersi Last Update dibandingkan dengan waktu yang dicatat sesudah aksi, toleransi satu menit (kolom berketelitian menit).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-197: Dialog konfirmasi Deactivate

1. Ketik Search `Rina Marlina {runId}-057`, tekan Enter
2. Klik switch Active pada baris `Rina Marlina {runId}-057` (ON)
3. Verifikasi dialog dengan Title `Deactivate Non-Login User`, body bullet `Rina Marlina {runId}-057`, `They will be hidden from dropdown selection across products.`, dan `Current transactions will not be affected. Are you sure you want to deactivate it?`, serta tombol `[Cancel]` dan `[Deactivate]`

### TC-GS-NLU-198: Cancel pada dialog Deactivate

4. Klik `[Cancel]`
5. Verifikasi dialog menutup tanpa efek
6. Verifikasi switch baris kembali ON

### TC-GS-NLU-199: Confirm Deactivate

7. Klik switch Active pada baris `Rina Marlina {runId}-057` (ON)
8. Klik `[Deactivate]`
9. Verifikasi toast sukses: `Success, non-login user has been deactivated.`
10. Verifikasi switch baris menjadi OFF
11. Catat waktu aksi sesudah toast sukses
12. Verifikasi Last Update baris sesuai waktu aksi (toleransi satu menit)

### TC-GS-NLU-200: Dialog konfirmasi Activate

13. Ganti isi kotak search dengan `Joko Susilo {runId}-057`, tekan Enter
14. Klik switch Active pada baris `Joko Susilo {runId}-057` (OFF)
15. Verifikasi dialog dengan Title `Activate Non-Login User`, body bullet `Joko Susilo {runId}-057`, `They will be made available for dropdown selection across products.`, dan `Are you sure you want to activate it?`, serta tombol `[Cancel]` dan `[Activate]`

### TC-GS-NLU-201: Cancel pada dialog Activate

16. Klik `[Cancel]`
17. Verifikasi dialog menutup tanpa efek
18. Verifikasi switch baris kembali OFF

### TC-GS-NLU-202: Confirm Activate

19. Klik switch Active pada baris `Joko Susilo {runId}-057` (OFF)
20. Klik `[Activate]`
21. Verifikasi toast sukses: `Success, non-login user has been activated.`
22. Verifikasi switch baris menjadi ON

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 11.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 13.
- Langkah 4 melanjutkan dialog yang dibuka langkah 2 (TC-198 bergantung pada TC-197) dan langkah 16 melanjutkan dialog langkah 14 (TC-201 bergantung pada TC-200); langkah 7 dan 19 membuka dialog lagi sesuai Langkah Uji TC-199 dan TC-202.
- Temuan untuk QA:
  - TC-199 Post Condition (status Inactive di tabel dan Detail, user hilang dari Select User produk lain, entri Changelog/Activity Log/System Log `Deactivate`) tanpa langkah observasi di TC; tidak diasersi.
  - TC-199 Expected b menyebut "Last Update baris diperbarui" tanpa nilai pembanding; spec membandingkan dengan waktu aksi (toleransi satu menit).
