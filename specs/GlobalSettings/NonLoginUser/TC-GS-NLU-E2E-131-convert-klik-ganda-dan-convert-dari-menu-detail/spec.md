---
id: TC-GS-NLU-E2E-131-convert-klik-ganda-dan-convert-dari-menu-detail
title: "Convert: Klik Ganda pada Konfirmasi dan Convert dari Menu Detail"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-450
  - TC-GS-NLU-237
coverage:
  web: automated
---

# Convert: Klik Ganda pada Konfirmasi dan Convert dari Menu Detail

## Prerequisites

- Mode: FE+BE (backend nyata).
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): `Konversi Enam {runId}-131` (Email `konversienam+{runId}-131@qwertysystem.net`) dan `Siti Rahayu {runId}-131` (tanpa Position dan Employee ID, Division Warehouse, Email `sitirahayu+{runId}-131@qwertysystem.net`). Pengganti Konversi Enam dan Siti Rahayu Pre-setup No. 11 karena Convert mengubah tipe record (S-06).
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`). Login User hasil Convert dihapus hook `after` lewat API.
- Mail-catcher: inbox per alamat email dapat dibaca dan jumlah email per alamat dapat dicatat sebelum aksi (baseline; kemampuan disediakan tim FE/BE).
- Kemampuan teknis: menghitung jumlah request yang dikirim browser untuk satu aksi konfirmasi tanpa mengubah respons (pemantauan jaringan Spectra, tanpa mengarang endpoint); membuka Modal Changelog agregat (icon Changelog pada Table Tools).
- State global yang diubah: tidak ada. Entri Changelog bersifat permanen; asersi entri memakai nama bersuffix unik (baseline nol).

## Test Steps


### TC-GS-NLU-450: Klik ganda cepat pada konfirmasi Convert

1. Catat baseline jumlah email di mail-catcher untuk `konversienam+{runId}-131@qwertysystem.net`
2. Ketik Search `Konversi Enam {runId}-131`, tekan Enter
3. Klik `⋯` baris `Konversi Enam {runId}-131` > `Convert to Login User`
4. Klik ganda cepat `[Convert]`
5. Verifikasi hanya satu request Convert yang dikirim dan diproses
6. Verifikasi tepat satu toast sukses: `Success, Konversi Enam {runId}-131 has been converted to a login user.`
7. Klik icon `Changelog` pada Table Tools untuk membuka Modal Changelog agregat
8. Verifikasi tepat satu entri dengan Action `Convert to Login User` dan nama `Konversi Enam {runId}-131`
9. Tutup Modal Changelog dengan `✕`
10. Verifikasi jumlah email di mail-catcher untuk `konversienam+{runId}-131@qwertysystem.net` bertambah tepat satu dari baseline (hanya satu email aktivasi)

### TC-GS-NLU-237: Convert dari menu Detail

11. Ketik Search `Siti Rahayu {runId}-131`, tekan Enter
12. Klik teks Name `Siti Rahayu {runId}-131` untuk membuka Detail
13. Klik `⋯` di header > `Convert to Login User`
14. Klik `[Convert]`
15. Verifikasi toast sukses: `Success, Siti Rahayu {runId}-131 has been converted to a login user.`
16. Verifikasi badge `Non Login` hilang dari Detail
17. Verifikasi tab Detail sesuai Login User: Role, Responsibilities, Non-Login User, Changelog, System Log, dan User Log
18. Verifikasi Represented By tidak ditampilkan

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 1, 7, 9.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 2, 11.
- Pembagian TC lintas spec: Convert dari row, Cancel, dan Confirm (TC-232, TC-233, TC-234, TC-236) ada di spec 065.
- Temuan untuk QA:
  - TC-450 Expected b menyebut "satu entri log" tanpa menyebut surface log; spec memakai Modal Changelog agregat. Pengamatan "hanya satu email aktivasi" memakai baseline mail-catcher (R-11).
  - TC-237 Expected b menyebut daftar tab Login User; spec menulis tab persis seperti TC.
  - TC-450 "hanya satu request diproses" tidak menyebut cara mengamatinya; spec memakai pemantauan jaringan (disediakan tim FE/BE).
