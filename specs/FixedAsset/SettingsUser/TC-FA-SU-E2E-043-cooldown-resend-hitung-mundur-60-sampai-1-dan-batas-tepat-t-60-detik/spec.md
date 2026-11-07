---
id: TC-FA-SU-E2E-043-cooldown-resend-hitung-mundur-60-sampai-1-dan-batas-tepat-t-60-detik
title: "Cooldown Resend: Hitung Mundur 60 sampai 1 dan Batas Tepat T+60 Detik"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-138
  - TC-FA-SU-139
coverage:
  web: automated
---

# Cooldown Resend: Hitung Mundur 60 sampai 1 dan Batas Tepat T+60 Detik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20): Hana Kusuma `hana.kusuma@corp.id` (Pending Activation). Cooldown Resend Hana belum berjalan saat tiap blok dimulai; dipulihkan lewat seed API di hook `before` dan di langkah 13.
- Jam (kelas d): countdown UI berjalan di jam browser sedangkan batas 60 detik dihitung server, sehingga jam server dan jam browser diatur bersama. Acuan T0 dibaca dari waktu terbit pengiriman Resend lewat kemampuan baca (disediakan tim FE/BE), bukan diperkirakan dari waktu langkah; jam diset absolut ke T0 + N detik (bagian 8b butir 3). Margin terhadap batas 60 detik adalah 0 detik dan 1 detik (batas eksak); T0 + 59 detik dan T0 + 60 detik dibedakan oleh jam yang dibekukan, bukan oleh waktu nyata.
- Tabel "Titik waktu hitung mundur" (langkah 7 sampai 8): offset dari T0 dan tooltip yang diharapkan, dengan `[Seconds]` = 60 dikurangi offset (dibulatkan ke atas):

  | Offset dari T0 | Tooltip yang diharapkan |
  |---|---|
  | T0 + 1 detik | "Please wait 59 seconds before resending." |
  | T0 + 30 detik | "Please wait 30 seconds before resending." |
  | T0 + 59 detik | "Please wait 1 seconds before resending." |

- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri `Resend Activation Email` Hana Kusuma pada Tab Changelog target (bagian 8b butir 10).
- Baseline log: langkah 14 mencatat jumlah entri `Resend Activation Email` Hana Kusuma pada Tab Changelog target sesudah Hana dipulihkan tanpa cooldown lewat seed API (langkah 13) dan sebelum Resend pertama TC-FA-SU-139; langkah 26 memakai selisih terhadap baseline langkah 14, bukan baseline hook yang juga memuat entri blok TC-FA-SU-138 (S-12).
- State global dan pemulihan: jam server dan jam browser dilepas pada langkah 24 dan dipulihkan hook `after`; cooldown Hana dipulihkan lewat seed API di hook `after`; tiga entri log Resend Hana bertambah permanen (audit trail). Log yang dibuat saat jam digeser dicari lewat selisih jumlah, bukan posisi teratas (S-12). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-138: Tooltip cooldown menghitung mundur dari 60 sampai 1

1. Ketik Search `Hana`, tekan Enter di User List
2. Bekukan jam server dan jam browser bersamaan
3. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
4. Baca T0 dari waktu terbit pengiriman Resend Hana Kusuma
5. Klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
6. Verifikasi tooltip "Please wait 60 seconds before resending." pada aksi `Resend Activation Email` yang Disabled
7. Untuk setiap baris tabel "Titik waktu hitung mundur" (langkah 7 sampai 8): setel jam server dan jam browser ke T0 + offset, lalu hover `Resend Activation Email` pada baris Hana Kusuma tanpa memuat ulang halaman
8. Verifikasi tooltip sesuai kolom "Tooltip yang diharapkan" pada baris tabel itu
9. Verifikasi label aksi tetap `Resend Activation Email` selama cooldown
10. Setel jam server dan jam browser ke T0 + 60 detik tanpa memuat ulang halaman
11. Verifikasi aksi `Resend Activation Email` pada baris Hana Kusuma kembali Enabled otomatis
12. Verifikasi tooltip cooldown pada aksi `Resend Activation Email` tidak tampil lagi

### TC-FA-SU-139: Resend tepat setelah cooldown berakhir diproses sebagai pengiriman baru

13. Pulihkan Hana Kusuma tanpa cooldown lewat seed API, lalu muat ulang halaman dan ganti isi kotak search dengan `Hana`, tekan Enter
14. Catat jumlah entri `Resend Activation Email` Hana Kusuma pada Tab Changelog target sebagai baseline TC-FA-SU-139
15. Bekukan jam server dan jam browser bersamaan
16. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
17. Baca T0 dari waktu terbit pengiriman Resend Hana Kusuma
18. Setel jam server dan jam browser ke T0 + 60 detik
19. Verifikasi aksi `Resend Activation Email` pada baris Hana Kusuma Enabled pada detik ke-60
20. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
21. Verifikasi toast "Success, activation email has been sent."
22. Klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
23. Verifikasi tooltip "Please wait 60 seconds before resending." (cooldown dimulai kembali dari 60)
24. Lepaskan pembekuan jam
25. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri tampil
26. Verifikasi entri kedua `Resend Activation Email` tercatat: selisih 2 dibanding baseline langkah 14 (dua dari blok ini)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Pembagian TC lintas spec: TC-FA-SU-140, 141, dan 142 (pengiriman berulang dan pemisahan cooldown) ada di spec 057.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 13 (Search untuk menemukan baris target, R-16; langkah 13 juga memulihkan Hana lewat seed API), langkah 14 (mencatat baseline jumlah entri, S-12), langkah 2, 15, dan 24 (pembekuan dan pelepasan jam), langkah 4 dan 17 (membaca T0), langkah 10 dan 18 (menyetel jam), langkah 25 (membuka Tab Changelog).
- Asersi tambahan di luar Expected TC: nilai tooltip T0 + 1 detik (59) dan T0 + 30 detik (30) diturunkan dari rumus 60 dikurangi offset yang disebut Expected b; TC menyebut titik waktu detik ke-1, ke-30, ke-59, dan setelah 60 detik pada Langkah Uji. Langkah 19 memeriksa tombol Enabled sebelum klik karena Expected a menyebut tombol Enabled pada detik ke-60.
- Penghitungan langkah: langkah 7 sampai 8 berulang tiga kali (ekspansi 6 langkah), sehingga ekspansi spec ini 30 langkah (26 langkah nominal).
- Temuan untuk QA:
  - Post Condition TC-FA-SU-138 ("satu entri `Resend Activation Email` tercatat pada tiga permukaan log") tidak punya langkah observasi dan tidak diasersi (S-01).
  - Post Condition TC-FA-SU-139 butir tiga permukaan log hanya diasersi pada Tab Changelog target (langkah 25 sampai 26, sesuai Expected b "entri log kedua"); Tab System Log aktor dan Activity Log tidak disebut di Langkah Uji.
  - Tooltip "Please wait 1 seconds before resending." mempertahankan bentuk jamak "seconds" untuk nilai 1 (tanpa pluralisasi sesuai NC-02); spec mengikuti TC.
