---
id: TC-GS-NLU-E2E-132-bulk-deactivate-dan-activate-dialog-dua-belas-nama-tanpa-ringkasan
title: "Bulk Deactivate dan Activate: Dialog 12 Nama Tanpa Ringkasan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-222
  - TC-GS-NLU-223
coverage:
  web: automated
---

# Bulk Deactivate dan Activate: Dialog 12 Nama Tanpa Ringkasan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): 12 Non-Login User `Populasi 01 {runId}-132` sampai `Populasi 12 {runId}-132`. Search `{runId}-132` menyaring tepat 12 baris (N = 12 dari seeding, dua halaman pada page size 10). TC-223 memakai 12 baris yang sama setelah Bulk Deactivate pada TC-222 (Dependensi TC-223 adalah TC-222).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-222: Dialog Bulk Deactivate 12 baris Active

1. Ketik Search `{runId}-132`, tekan Enter
2. Centang satu baris lalu klik button `Select All (12 records)` untuk memilih 12 baris Active
3. Pilih `Bulk Action` > `Deactivate`
4. Gulir daftar bullet pada dialog
5. Verifikasi dialog dengan Title `Deactivate Non-Login Users`
6. Verifikasi 12 bullet nama `Populasi 01 {runId}-132` sampai `Populasi 12 {runId}-132` tampil dalam container scrollable
7. Verifikasi tidak ada ringkasan `...and N more`
8. Verifikasi body dialog: `They will be hidden from dropdown selection across products. Current transactions will not be affected. Are you sure you want to deactivate them?`
9. Verifikasi tombol `[Cancel]` dan `[Deactivate]` tampil
10. Klik `[Deactivate]`
11. Verifikasi toast sukses: `Success, non-login user has been deactivated.`
12. Verifikasi seluruh 12 baris OFF

### TC-GS-NLU-223: Dialog Bulk Activate 12 baris Inactive

13. Centang satu baris lalu klik button `Select All (12 records)` untuk memilih 12 baris Inactive
14. Pilih `Bulk Action` > `Activate`
15. Verifikasi dialog dengan Title `Activate Non-Login Users`
16. Verifikasi 12 bullet nama tampil tanpa diringkas
17. Verifikasi body dialog: `They will be made available for dropdown selection across products. Are you sure you want to activate them?`
18. Verifikasi tombol `[Cancel]` dan `[Activate]` tampil
19. Klik `[Activate]`
20. Verifikasi toast sukses: `Success, non-login user has been activated.`
21. Verifikasi seluruh 12 baris ON

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 2, 13.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1.
- Pembagian TC lintas spec: TC-222 dan TC-223 ada di spec ini; tombol tampil sesuai status, collapse single, dan Cancel (TC-220, TC-221, TC-224, TC-448) ada di spec 062.
- Memilih 12 baris ditulis sebagai satu langkah penghubung (checkbox satu baris lalu `Select All (12 records)`) karena Search menyaring tepat 12 baris milik spec.
- Temuan untuk QA:
  - TC-222 dan TC-223 "Pilih 12 baris" tidak menyebut cara memilih; spec memakai `Select All`.
  - TC-222 Expected a menyebut container scrollable tanpa menyebut cara mengamati scroll; spec memverifikasi keberadaan container scrollable dan seluruh 12 bullet.
