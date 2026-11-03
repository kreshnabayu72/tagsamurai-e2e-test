---
id: TC-GS-NLU-E2E-058-toggle-active-switch-di-detail-temporary-expired-di-detail
title: "Toggle Active: Switch di Detail, Temporary-expired di Detail, dan Klik Ganda Konfirmasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-210
  - TC-GS-NLU-211
  - TC-GS-NLU-449
  - TC-GS-NLU-479
coverage:
  web: automated
---

# Toggle Active: Switch di Detail, Temporary-expired di Detail, dan Klik Ganda Konfirmasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Division Operations, Represented By Ahmad Fauzi): `Rina Marlina {runId}-058` (Active, Position Driver, Temporary +30 hari), `Agus Salim {runId}-058` (Inactive, Temporary-expired), `Hendra Delapan {runId}-058` (Active), `Aktif Ganda {runId}-058` (Inactive, bukan Temporary-expired). Pengganti Rina Marlina, Agus Salim, Hendra Delapan, dan Aktif Ganda Pre-setup No. 11 karena spec mengubah statusnya (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: menghitung jumlah request yang dikirim browser untuk satu aksi konfirmasi tanpa mengubah respons (pemantauan jaringan Spectra, tanpa mengarang endpoint); membuka Modal Changelog agregat (icon Changelog pada Table Tools).
- State global yang diubah: tidak ada. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix unik (baseline nol).

## Test Steps


### TC-GS-NLU-210: Switch Active di header Detail

1. Ketik Search `Rina Marlina {runId}-058`, tekan Enter
2. Klik teks Name `Rina Marlina {runId}-058` untuk membuka Detail
3. Klik switch Active di header (ON)
4. Verifikasi dialog dengan Title `Deactivate Non-Login User`
5. Klik `[Deactivate]`
6. Verifikasi toast sukses: `Success, non-login user has been deactivated.`
7. Verifikasi switch header menjadi OFF
8. Klik switch Active di header (OFF)
9. Verifikasi dialog dengan Title `Activate Non-Login User`
10. Klik `[Activate]`
11. Verifikasi toast sukses: `Success, non-login user has been activated.`
12. Verifikasi switch header menjadi ON

### TC-GS-NLU-211: Switch Active di header Detail Temporary-expired

13. Kembali ke list Non-Login User
14. Ganti isi kotak search dengan `Agus Salim {runId}-058`, tekan Enter
15. Klik teks Name `Agus Salim {runId}-058` untuk membuka Detail
16. Klik switch Active di header
17. Verifikasi dialog dengan Title `Reactivate Temporary User`
18. Verifikasi dialog memuat opsi `Extend period` dan `Make permanent`
19. Klik `[Cancel]` untuk menutup dialog

### TC-GS-NLU-449: Klik ganda cepat pada konfirmasi Deactivate

20. Kembali ke list Non-Login User
21. Ganti isi kotak search dengan `Hendra Delapan {runId}-058`, tekan Enter
22. Klik switch Active baris `Hendra Delapan {runId}-058` (ON)
23. Klik ganda cepat `[Deactivate]`
24. Verifikasi hanya satu request Deactivate yang dikirim dan diproses
25. Verifikasi tepat satu toast sukses: `Success, non-login user has been deactivated.`

### TC-GS-NLU-479: Klik ganda cepat pada konfirmasi Activate

26. Ganti isi kotak search dengan `Aktif Ganda {runId}-058`, tekan Enter
27. Klik switch Active baris `Aktif Ganda {runId}-058` (OFF)
28. Klik ganda cepat `[Activate]`
29. Verifikasi hanya satu request Activate yang dikirim dan diproses
30. Verifikasi tepat satu toast sukses: `Success, non-login user has been activated.`
31. Klik icon `Changelog` pada Table Tools untuk membuka Modal Changelog agregat
32. Verifikasi tepat satu entri dengan Action `Deactivate`, Field `Status`, dan nama `Hendra Delapan {runId}-058` (TC-449)
33. Verifikasi tepat satu entri dengan Action `Activate`, Field `Status`, dan nama `Aktif Ganda {runId}-058` (TC-479)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 13, 19, 20, 31.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 14, 21, 26.
- Verifikasi entri log TC-449 (langkah 32) dan TC-479 (langkah 33) ditaruh sesudah kedua klik ganda karena satu pembukaan Modal Changelog agregat memuat entri kedua aksi (tiap nama bersuffix unik, baseline nol; S-10 membatasi jumlah buka surface).
- Temuan untuk QA:
  - TC-449 dan TC-479 Expected menyebut "satu entri log" tanpa menyebut surface log; spec memakai Modal Changelog agregat.
  - TC-449 dan TC-479 "hanya satu request diproses" tidak menyebut cara mengamatinya; spec memakai pemantauan jaringan (disediakan tim FE/BE).
  - TC-211 hanya menyebut dialog Reactivate tampil; dialog ditutup dengan `[Cancel]` sebagai langkah penghubung.
