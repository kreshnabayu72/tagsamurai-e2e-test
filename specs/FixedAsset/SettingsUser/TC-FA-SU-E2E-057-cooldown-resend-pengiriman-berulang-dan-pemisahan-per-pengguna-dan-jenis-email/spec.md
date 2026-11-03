---
id: TC-FA-SU-E2E-057-cooldown-resend-pengiriman-berulang-dan-pemisahan-per-pengguna-dan-jenis-email
title: "Cooldown Resend: Pengiriman Berulang dan Pemisahan per Pengguna dan Jenis Email"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-140
  - TC-FA-SU-141
  - TC-FA-SU-142
coverage:
  web: automated
---

# Cooldown Resend: Pengiriman Berulang dan Pemisahan per Pengguna dan Jenis Email

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Hana Kusuma (Pending Activation), Kartika Sari (Pending Activation, Inactive), dan Indra Wijaya (Pending Email Confirmation). Cooldown Resend ketiganya belum berjalan saat tiap blok dimulai; dipulihkan lewat seed API di hook `before`, langkah 11, dan langkah 21.
- Jam (kelas d): countdown UI berjalan di jam browser dan batas 60 detik dihitung server, sehingga jam server dan jam browser dibekukan dan disetel bersama. Acuan T0 dibaca dari waktu terbit pengiriman Resend lewat kemampuan baca (disediakan tim FE/BE); jam diset absolut ke T0 + N detik (bagian 8b butir 3).
- Tabel "Titik pengiriman berulang" (langkah 6 sampai 9, TC-FA-SU-140): offset jam dari T0 untuk pengiriman kedua dan ketiga:

  | Pengiriman | Offset jam dari T0 |
  |---|---|
  | Kedua | T0 + 60 detik |
  | Ketiga | T0 + 120 detik |

- State global dan pemulihan: jam server dan jam browser dilepas pada langkah 29 dan dipulihkan hook `after`; cooldown Hana, Kartika, dan Indra dipulihkan lewat seed API di hook `after`; entri log Resend bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-140: Tidak ada batas harian Resend

1. Bekukan jam server dan jam browser bersamaan
2. Ketik Search `Hana`, tekan Enter di User List
3. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
4. Baca T0 dari waktu terbit pengiriman Resend Hana Kusuma
5. Verifikasi toast "Success, activation email has been sent."
6. Untuk setiap baris tabel "Titik pengiriman berulang" (langkah 6 sampai 9): setel jam server dan jam browser ke T0 + offset pada baris tabel itu
7. Verifikasi aksi `Resend Activation Email` pada baris Hana Kusuma Enabled kembali (menu ⋯ dibuka)
8. Klik `Resend Activation Email` pada menu ⋯ baris Hana Kusuma
9. Verifikasi toast "Success, activation email has been sent."
10. Verifikasi tidak ada pesan batas harian yang tampil

### TC-FA-SU-141: Cooldown dipisah per pengguna dan jenis email

11. Pulihkan Hana Kusuma dan Indra Wijaya tanpa cooldown lewat seed API
12. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`, baca T1 dari waktu terbit pengiriman, lalu setel jam server dan jam browser ke T1 + 10 detik
13. Ganti isi kotak search dengan `Indra`, tekan Enter, klik nama Indra Wijaya untuk membuka Detail
14. Verifikasi tombol `[Resend Confirmation Email]` Enabled di header Detail Indra Wijaya
15. Klik `[Resend Confirmation Email]`
16. Verifikasi toast "Success, confirmation email has been sent to Indra Wijaya."
17. Hover tombol `[Resend Confirmation Email]`
18. Verifikasi tombol `[Resend Confirmation Email]` Disabled dengan tooltip "Please wait 60 seconds before resending."
19. Kembali ke User List, ketik Search `Hana`, tekan Enter, klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
20. Verifikasi tooltip "Please wait 50 seconds before resending." pada `Resend Activation Email` baris Hana Kusuma (cooldown Hana tidak direset oleh Resend Indra)

### TC-FA-SU-142: Cooldown dihitung per pengguna

21. Pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API
22. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
23. Ganti isi kotak search dengan `Kartika`, tekan Enter, klik ⋯ pada baris Kartika Sari
24. Verifikasi `Resend Activation Email` Enabled di menu ⋯ baris Kartika Sari dalam masa cooldown Hana
25. Klik `Resend Activation Email`
26. Verifikasi toast "Success, activation email has been sent."
27. Klik ⋯ pada baris Kartika Sari lagi, hover `Resend Activation Email`
28. Verifikasi `Resend Activation Email` pada baris Kartika Sari Disabled dengan tooltip "Please wait 60 seconds before resending." (cooldown Kartika berjalan terpisah)
29. Lepaskan pembekuan jam

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Pembagian TC lintas spec: TC-FA-SU-138 dan 139 (hitung mundur dan batas T+60 detik) ada di spec 043.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 29 (pembekuan dan pelepasan jam), langkah 2, 13, 19, dan 23 (Search untuk menemukan baris target, R-16), langkah 4 dan 12 (membaca T0 dan T1; langkah 12 juga menyetel jam), langkah 6 (menyetel jam), langkah 11 dan 21 (memulihkan cooldown lewat seed API).
- Asersi tambahan di luar Expected TC: langkah 7 (tombol Enabled sebelum pengiriman kedua dan ketiga, sesuai Expected b TC-FA-SU-140 "tombol tetap kembali Enabled setelah tiap cooldown"); langkah 20 (nilai 50 = 60 dikurangi 10 detik jam yang disetel di langkah 12) membuktikan bahwa kalimat "dan sebaliknya" pada Expected b TC-FA-SU-141 (Resend Indra tidak memengaruhi Hana) terpenuhi.
- Penghitungan langkah: langkah 6 sampai 9 berulang dua kali (ekspansi 8 langkah), sehingga ekspansi spec ini 33 langkah (29 langkah nominal).
- Temuan untuk QA:
  - Post Condition TC-FA-SU-140 ("tiga entri `Resend Activation Email` tercatat pada tiga permukaan log"), TC-FA-SU-141, dan TC-FA-SU-142 tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-SU-141 menyebut Hana (Pending Activation) dan Indra (Pending Email Confirmation) sebagai dua pengguna dengan jenis email berbeda; TC tidak menjelaskan apakah satu pengguna dapat memiliki dua jenis cooldown sekaligus, karena status keduanya saling eksklusif. Spec mengikuti TC dengan dua pengguna berbeda.
  - Expected TC-FA-SU-142 butir a ("tetap Enabled") tidak memberi cara membedakan dari kondisi tanpa cooldown selain Resend Kartika berhasil; spec mengasersi tombol Enabled lalu toast sukses dan cooldown terpisah.
