---
id: TC-GS-NLU-E2E-060-reactivate-temporary-until-hari-ini-cancel-tanggal-ditolak
title: "Reactivate: Temporary Until Hari Ini, Cancel, dan Tanggal Ditolak"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-203
  - TC-GS-NLU-208
  - TC-GS-NLU-209
  - TC-GS-NLU-467
coverage:
  web: automated
---

# Reactivate: Temporary Until Hari Ini, Cancel, dan Tanggal Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Dedi Hari Ini {runId}-060` (Inactive manual, Temporary Until hari ini, Position Contractor) dan `Agus Salim {runId}-060` (Inactive, Temporary-expired, Position Contractor). Pengganti Dedi Hari Ini dan Agus Salim Pre-setup No. 11 karena spec membuka dialog yang dapat mengubah statusnya (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE; TC-467 tidak menyebut mekanismenya): menyuntikkan nilai tanggal hari ini langsung ke state date picker dialog Reactivate tanpa memilihnya lewat UI (melewati penonaktifan tanggal di UI).
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-203: Temporary Until hari ini memakai dialog Activate biasa

1. Ketik Search `Dedi Hari Ini {runId}-060`, tekan Enter
2. Klik switch Active pada baris `Dedi Hari Ini {runId}-060` (OFF)
3. Verifikasi dialog standar dengan Title `Activate Non-Login User` tampil
4. Verifikasi dialog `Reactivate Temporary User` tidak tampil (Temporary Until hari ini belum expired)
5. Klik `[Cancel]` untuk menutup dialog

### TC-GS-NLU-208: Cancel pada dialog Reactivate

6. Ganti isi kotak search dengan `Agus Salim {runId}-060`, tekan Enter
7. Klik switch Active pada baris `Agus Salim {runId}-060`
8. Pilih opsi `Make permanent`
9. Klik `[Cancel]`
10. Verifikasi dialog menutup tanpa efek
11. Verifikasi switch baris tetap OFF

### TC-GS-NLU-209: Extend period menolak tanggal hari ini dan lampau

12. Klik switch Active pada baris `Agus Salim {runId}-060`
13. Pilih `Extend period` dan buka date picker
14. Verifikasi tanggal kemarin tidak dapat dipilih
15. Verifikasi tanggal hari ini tidak dapat dipilih

### TC-GS-NLU-467: Server menolak tanggal hari ini yang lolos date picker

16. Injeksi nilai tanggal hari ini langsung ke state date picker (melewati penonaktifan tanggal di UI)
17. Klik `[Reactivate]`
18. Verifikasi pesan inline di bawah field tanggal: `Please select a future date.`
19. Verifikasi dialog tetap terbuka
20. Verifikasi user tetap Inactive (switch baris OFF)
21. Klik `[Cancel]` untuk menutup dialog

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 5, 21.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 6.
- Langkah sesudah 13 melanjutkan dialog yang dibuka langkah 12 (TC-467 bergantung pada TC-204): opsi `Extend period` dan date picker yang masih terbuka dipakai oleh TC-467.
- P-5: TC-467 menyuntikkan nilai ke state date picker (manipulasi sisi klien kelas a); satu TC objek-uji ringan yang berada di spec fungsional topik Reactivate yang sama.
- Pembagian TC lintas spec: dialog Reactivate (TC-204) dan Reactivate sukses (TC-205, TC-206, TC-207) ada di spec 059.
- Temuan untuk QA:
  - TC-203 Expected hanya menyebut dialog Activate standar tampil; klausa "bukan dialog Reactivate Temporary User" diasersi sebagai absence dengan anchor dialog Activate tampil.
  - TC-209 Langkah 3 hanya menyebut "tanggal kemarin", sedangkan Expected menyebut tanggal kemarin dan hari ini; spec memverifikasi keduanya.
  - TC-467 tidak menyebut mekanisme injeksi nilai; kemampuan itu disediakan tim FE.
