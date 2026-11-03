---
id: TC-GS-NLU-E2E-067-bulk-convert-dialog-cancel-temporary-expired-satu-baris
title: "Bulk Convert: Dialog, Cancel, Temporary-expired, dan Satu Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-242
  - TC-GS-NLU-243
  - TC-GS-NLU-246
  - TC-GS-NLU-501
coverage:
  web: automated
---

# Bulk Convert: Dialog, Cancel, Temporary-expired, dan Satu Baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Collapse Satu {runId}-067` (Active, Email `collapsesatu+{runId}-067@qwertysystem.net`), `Budi Kurniawan {runId}-067` dan `Siti Rahayu {runId}-067` (Active, Email bersuffix `{runId}-067`), `Agus Salim {runId}-067` (Inactive, Temporary-expired, Email bersuffix), dan 12 Non-Login User `Bulk Convert 01 {runId}-067` sampai `Bulk Convert 12 {runId}-067` (Active, Email bersuffix). Search `{runId}-067` menyaring 17 baris; page size diubah ke 100 sehingga seluruh baris tampil pada satu halaman. Pengganti Collapse Satu, Budi Kurniawan, Siti Rahayu, Agus Salim, dan Bulk Convert 01 sampai 12 Pre-setup No. 11 karena Convert mengubah tipe record (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`). Login User hasil Convert dihapus hook `after` lewat API.
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-501: Bulk Convert satu baris collapse ke dialog single

1. Ketik Search `{runId}-067`, tekan Enter
2. Ubah page size menjadi 100 sehingga 17 baris tampil dalam satu halaman
3. Centang baris `Collapse Satu {runId}-067`
4. Pilih `Bulk Action` > `Convert to Login User`
5. Verifikasi dialog single dengan Title `Convert to Login User` (singular), satu bullet `Collapse Satu {runId}-067`, body `This user will become a login user. An activation email will be sent to collapsesatu+{runId}-067@qwertysystem.net. This action cannot be undone. Are you sure you want to convert it?`, dan tombol `[Cancel]` dan `[Convert]`
6. Klik `[Cancel]` lalu klik icon `(X)` untuk membatalkan seleksi

### TC-GS-NLU-243: Cancel pada dialog Convert bulk

7. Centang baris `Budi Kurniawan {runId}-067` dan `Siti Rahayu {runId}-067`
8. Pilih `Bulk Action` > `Convert to Login User`, klik `[Cancel]`
9. Verifikasi dialog menutup
10. Verifikasi kedua baris tetap Non-Login User
11. Verifikasi seleksi dipertahankan (`2 Non-Login Users selected`)

### TC-GS-NLU-246: Bulk Convert tidak melewati baris Temporary-expired

12. Klik icon `(X)` untuk membatalkan seleksi
13. Centang baris `Agus Salim {runId}-067` (Temporary-expired) dan `Budi Kurniawan {runId}-067`
14. Pilih `Bulk Action` > `Convert to Login User`
15. Klik `[Convert]`
16. Verifikasi baris `Agus Salim {runId}-067` dan `Budi Kurniawan {runId}-067` hilang dari sub-tab Non-Login User
17. Verifikasi tidak ada dialog Extend period atau Make permanent
18. Klik sub-tab `Login User`
19. Ketik Search `Agus Salim {runId}-067`, tekan Enter
20. Verifikasi `Agus Salim {runId}-067` menjadi Login User dengan status Inactive

### TC-GS-NLU-242: Dialog Convert bulk 12 baris dan semua berhasil

21. Klik sub-tab `Non-Login User`
22. Ketik Search `Bulk Convert`, tekan Enter
23. Centang 12 baris `Bulk Convert 01 {runId}-067` sampai `Bulk Convert 12 {runId}-067` satu per satu
24. Pilih `Bulk Action` > `Convert to Login User`
25. Gulir daftar bullet pada dialog
26. Verifikasi dialog dengan Title `Convert to Login Users`, body `These non-login users will become login users. Activation emails will be sent to each. This action cannot be undone. Are you sure you want to convert them?`, dan tombol `[Cancel]` dan `[Convert]`
27. Verifikasi 12 bullet nama `Bulk Convert 01 {runId}-067` sampai `Bulk Convert 12 {runId}-067` tampil dalam container scrollable tanpa diringkas
28. Klik `[Convert]`
29. Verifikasi toast sukses: `Success, non-login user has been converted.`
30. Verifikasi 12 baris hilang dari sub-tab Non-Login User
31. Klik sub-tab `Login User`
32. Ketik Search `Bulk Convert`, tekan Enter
33. Verifikasi 12 baris `Bulk Convert 01 {runId}-067` sampai `Bulk Convert 12 {runId}-067` muncul di sub-tab Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 2, 6, 12, 21.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 19, 22, 32.
- Pencarian `Bulk Convert` pada TC-242 menyaring baris Pre-setup Bulk Convert 01 sampai 12 dan baris milik spec; 12 baris dipilih dengan nama bersuffix `{runId}-067` dan baris Pre-setup tidak disentuh.
- Pembagian TC lintas spec: Bulk Convert sebagian gagal, seluruh gagal, dan baris dihapus admin lain (TC-244, TC-245, TC-442) ada di spec 068.
- Temuan untuk QA:
  - TC-246 Expected b dan Langkah 3 tidak menyebut toast sukses; spec tidak mengasersi toast pada TC itu.
  - TC-242 Expected c "Dua belas baris hilang dari Non-Login User dan muncul di Login User" dipecah menjadi dua `Verifikasi` pada dua sub-tab.
  - TC-243 Expected "seleksi dipertahankan" tidak menyebut cara mengamatinya; spec memakai counter Bulk Action Bar.
