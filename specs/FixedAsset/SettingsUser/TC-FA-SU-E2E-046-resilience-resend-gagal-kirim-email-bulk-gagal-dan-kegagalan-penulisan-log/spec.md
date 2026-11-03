---
id: TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log
title: "Resilience Resend: Gagal Kirim Email, Bulk Gagal, dan Kegagalan Penulisan Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-143
  - TC-FA-SU-144
  - TC-FA-SU-156
  - TC-FA-SU-158
coverage:
  web: automated
---

# Resilience Resend: Gagal Kirim Email, Bulk Gagal, dan Kegagalan Penulisan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37; Changelog #27): Hana Kusuma dan Kartika Sari (Pending Activation) serta Indra Wijaya (Pending Email Confirmation). Cooldown Resend belum berjalan saat tiap blok dimulai; dipulihkan lewat seed API di hook `before` dan langkah 30 dan 41.
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` atas respons HTTP request Resend (galat layanan email), bentuk respons bulk dengan satu item gagal (tidak tercantum di TC), dan pengendali layanan email (#37); pemicu kegagalan penulisan log di sisi server (TC-FA-SU-158 berstatus `Manual Only — BE`); mail-catcher dengan baseline jumlah email per alamat (R-11); kemampuan baca jumlah entri log (baseline, bagian 8b butir 10); seed API untuk mereset cooldown; jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC).
- Baseline log: hook `before` mencatat jumlah entri `Resend Activation Email` Hana dan Kartika, serta `Resend Confirmation Email` Indra, pada Tab Changelog target, Tab System Log aktor, dan Activity Log. Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Jam: jam server dan jam browser dibekukan bersama pada langkah 42 supaya tooltip cooldown bernilai tepat 60 detik, dilepas pada langkah 51; hook `after` memulihkan jam.
- State global dan pemulihan: intercept dilepas segera setelah pemicu (S-09); pemicu kegagalan log dan jam dipulihkan di hook `after`; cooldown Hana dipulihkan lewat seed API; entri log Resend yang berhasil bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-143: Cooldown tidak dimulai saat pengiriman email gagal

1. Ketik Search `Hana`, tekan Enter di User List
2. Cegat respons request Resend Activation Email menjadi galat layanan email (`Spectra.intercept()`)
3. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
4. Verifikasi toast error "Error, failed to send activation email to Hana Kusuma."
5. Klik ⋯ pada baris Hana Kusuma lagi
6. Verifikasi `Resend Activation Email` Enabled tanpa hitung mundur
7. Tunggu toast lama hilang otomatis
8. Klik `Resend Activation Email` lagi segera (retry)
9. Verifikasi toast error "Error, failed to send activation email to Hana Kusuma." tampil kembali
10. Lepaskan cegatan respons
11. Buka Detail Hana Kusuma > Tab Changelog
12. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma di Tab Changelog sama dengan baseline (tidak ada entri log baru)
13. Buka Tab System Log aktor
14. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma di Tab System Log aktor sama dengan baseline
15. Buka Activity Log
16. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma di Activity Log sama dengan baseline

### TC-FA-SU-144: Resend Confirmation gagal kirim

17. Kembali ke User List, ganti isi kotak search dengan `Indra`, tekan Enter
18. Cegat respons request Resend Confirmation Email menjadi galat layanan email (`Spectra.intercept()`)
19. Klik ⋯ pada baris Indra Wijaya lalu `Resend Confirmation Email`
20. Verifikasi toast error "Error, failed to send confirmation email to Indra Wijaya."
21. Klik ⋯ pada baris Indra Wijaya lagi
22. Verifikasi `Resend Confirmation Email` Enabled
23. Lepaskan cegatan respons
24. Buka Detail Indra Wijaya > Tab Changelog
25. Verifikasi jumlah entri `Resend Confirmation Email` Indra Wijaya di Tab Changelog sama dengan baseline (tidak ada entri log baru)

### TC-FA-SU-156: Bulk Resend sebagian gagal dan gagal total

26. Kembali ke User List, cegat respons bulk Resend Activation Email sehingga satu item gagal
27. Centang baris Hana Kusuma dan Kartika Sari
28. Klik Bulk Action, pilih `Resend Activation Email`
29. Verifikasi toast "Success, activation email has been sent. Some items failed."
30. Lepaskan cegatan, pulihkan Hana Kusuma dan Kartika Sari tanpa cooldown lewat seed API, buka Tab System Log aktor, muat ulang sampai entri `Resend Activation Email` item yang berhasil dari langkah 28 tampil, catat baseline jumlah entri `Resend Activation Email` di Tab System Log aktor, lalu cegat respons bulk Resend Activation Email sehingga seluruh item gagal
31. Muat ulang halaman User List, centang baris Hana Kusuma dan Kartika Sari
32. Klik Bulk Action, pilih `Resend Activation Email`
33. Verifikasi toast "Error, failed to send activation email."
34. Lepaskan cegatan respons
35. Klik ⋯ pada baris Hana Kusuma
36. Verifikasi `Resend Activation Email` baris Hana Kusuma Enabled tanpa hitung mundur
37. Klik ⋯ pada baris Kartika Sari
38. Verifikasi `Resend Activation Email` baris Kartika Sari Enabled tanpa hitung mundur
39. Buka Tab System Log aktor
40. Verifikasi jumlah entri `Resend Activation Email` di Tab System Log aktor sama dengan baseline langkah 30 (item gagal tidak menulis log)

### TC-FA-SU-158: Kegagalan penulisan log Resend tidak membatalkan email dan cooldown tetap berjalan

41. Pulihkan Hana Kusuma tanpa cooldown lewat seed API, lalu muat ulang halaman User List dan ketik Search `Hana`, tekan Enter
42. Bekukan jam server dan jam browser bersamaan
43. Picu kegagalan penulisan log di sisi server
44. Klik ⋯ pada baris Hana Kusuma lalu `Resend Activation Email`
45. Verifikasi toast "Success, activation email has been sent."
46. Verifikasi jumlah email aktivasi ke `hana.kusuma@corp.id` di mail-catcher bertambah tepat satu dibanding baseline
47. Klik ⋯ pada baris Hana Kusuma, hover `Resend Activation Email`
48. Verifikasi `Resend Activation Email` Disabled dengan tooltip "Please wait 60 seconds before resending." (cooldown 60 detik dimulai)
49. Pulihkan penulisan log di sisi server
50. Buka Detail Hana Kusuma > Tab Changelog
51. Lepaskan pembekuan jam
52. Verifikasi riwayat Hana Kusuma sebelumnya tampil di Tab Changelog (data Pre-setup #27)
53. Verifikasi jumlah entri `Resend Activation Email` Hana Kusuma di Tab Changelog sama dengan baseline (entri tidak tersedia karena penulisan gagal)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Kelas b: semua blok memakai kegagalan yang dipaksakan; tidak ada TC kelas lain di spec ini.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 17, dan 41 (Search untuk menemukan baris target atau kembali ke User List, R-16), langkah 7 (menunggu toast lama hilang otomatis, R-12), langkah 10, 23, 34 (melepas cegatan segera setelah pemicu, S-09), langkah 11, 13, 15, 24, 39, dan 50 (membuka surface log), langkah 26 dan 30 (menyetel cegatan, memulihkan cooldown, dan pada langkah 30 mencatat baseline System Log hanya sesudah entri item berhasil langkah 28 tampil, NC-03), langkah 42 dan 51 (pembekuan dan pelepasan jam), langkah 43 dan 49 (memicu dan memulihkan kegagalan penulisan log).
- Asersi tambahan di luar Expected TC: langkah 52 adalah anchor positif bagi asersi jumlah langkah 53 (bagian 8b butir 2); toast error langkah 4, 9, dan 20 serta toast langkah 29, 33, dan 45 menjadi anchor bagi asersi jumlah entri log.
- Spec ini 53 langkah. Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fault injection pada Resend), memakai dataset dan halaman yang sama, dan tiap blok berdiri sendiri karena cegatan dilepas dan cooldown dipulihkan lewat seed API di antara blok; kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - TC-FA-SU-156 langkah 1 tidak menyebut item mana yang gagal pada skenario sebagian; Expected c ("item gagal tidak memulai cooldown dan tidak menulis log") hanya dapat diasersi pada skenario gagal total (langkah 35 sampai 40). Bentuk respons bulk sebagian gagal tidak tercantum di TC dan disediakan tim FE/BE (S-13).
  - Expected c TC-FA-SU-143 menulis "tiga permukaan log"; TC-FA-SU-144 dan TC-FA-SU-156 hanya menulis "tidak ada entri log" tanpa surface. Spec memakai Tab Changelog target untuk TC-FA-SU-144 dan Tab System Log aktor untuk TC-FA-SU-156.
  - Expected b TC-FA-SU-158 ("penulisan dicoba ulang; bila tetap gagal, entri tidak tampil") bersyarat; spec mengasersi hasil akhir saat kegagalan penulisan tetap berlaku sampai pemeriksaan (entri tidak tampil) tanpa mengasersi percobaan ulang.
  - Post Condition TC-FA-SU-143, 144, 156, dan 158 tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01).
