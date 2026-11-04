---
id: TC-AC-LCS-E2E-146-approval-adopter-warning-ulang-dan-status-final
title: "Approval Settings Konsumen: Pengiriman Ulang Warning, Recalculation Berurutan, Reset, Progress Approver AND, dan Pengajuan Trial Activation"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-512
  - TC-AC-LCS-513
  - TC-AC-LCS-514
  - TC-AC-LCS-515
  - TC-AC-LCS-516
  - TC-AC-LCS-517
coverage:
  web: automated
---

# Approval Settings Konsumen: Pengiriman Ulang Warning, Recalculation Berurutan, Reset, Progress Approver AND, dan Pengajuan Trial Activation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Device Allocation uji berstatus `Waiting for Approval` (atau `Approved`, `Rejected`, `Canceled` pada TC-AC-LCS-516) dan pengajuan trial PT Cahaya Baru (`Fixture.lifecycleSettings.clientCahayaBaru`) diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC); akun pemohon dan approver aktif disediakan tim FE (tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan menunda dan melepaskan Recalculate Job, kueri status job, serta pembacaan jumlah notifikasi per penerima (pemohon dan approver aktif).
- Jendela amat notifikasi: asersi absence notifikasi in-app (TC-AC-LCS-514, langkah 35-36) didahului anchor positif (toast langkah 33) dan langkah "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 34); lima detik adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (8b.11, bagian 6).
- Waktu: jam server dan jam browser dimajukan bersama; jam dipulihkan sesudah tiap TC (S-09, R-08). Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-512: Pengajuan yang sudah menerima warning H-24 dan kini memiliki sisa waktu lebih dari 24 jam mengirim warning lagi pada H-24 baru

1. Atur lewat Fixture BE: Device Allocation berstatus `Waiting for Approval` yang diajukan 2,2 hari lalu dan sudah menerima warning H-24
2. Klik tab `Approval Settings`
3. Ubah Approval Timeout dari `3` menjadi `7`
4. Catat jumlah notifikasi warning H-24 approver aktif lewat kemampuan baca notifikasi sebagai baseline
5. Catat jumlah notifikasi warning H-24 pemohon lewat kemampuan baca notifikasi sebagai baseline
6. Klik `[Save]` dan tunggu toast sukses
7. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
8. Majukan jam server dan jam browser hingga sisa waktu pengajuan kurang dari 24 jam menuju batas baru lewat Fixture BE, lalu picu job pemeriksaan
9. Verifikasi jumlah notifikasi warning H-24 approver aktif bertambah tepat satu dari baseline (warning H-24 kedua; penanda warning direset oleh recalculation)
10. Verifikasi jumlah notifikasi warning H-24 pemohon bertambah tepat satu dari baseline (warning H-24 kedua; penanda warning direset oleh recalculation)

### TC-AC-LCS-513: Save Approval Timeout berikutnya saat recalculation sebelumnya berjalan: job sebelumnya digantikan

11. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 1 hari lalu dan Recalculate Job ditunda lewat fixture BE agar masih berjalan saat Save kedua, lalu buka Plans & Licensing > Lifecycle Settings
12. Klik tab `Approval Settings`
13. Ubah Approval Timeout dari `3` menjadi `2`
14. Klik `[Save]` dan tunggu toast sukses
15. Sebelum job pertama selesai, ubah Approval Timeout menjadi `5`
16. Klik `[Save]` dan tunggu toast sukses
17. Lepaskan penundaan job lewat Fixture BE dan tunggu seluruh job selesai lewat kueri status job (batas tunggu 2 menit)
18. Majukan jam server dan jam browser hingga 3 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
19. Buka halaman daftar pengajuan Device Allocation
20. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
21. Buka pengajuan Device Allocation tersebut
22. Verifikasi status pengajuan tetap `Waiting for Approval` (batas mengikuti nilai tersimpan terakhir `5`, bukan `2`)

### TC-AC-LCS-514: Reset to Default Approval Timeout menjalankan recalculation hanya bila nilai sebelumnya berbeda dari 3

23. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Approval Timeout tersimpan `7` dan Device Allocation berstatus `Waiting for Approval` yang diajukan 4 hari lalu, lalu buka Plans & Licensing > Lifecycle Settings
24. Klik tab `Approval Settings`
25. Klik `[Reset to Default]`
26. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
27. Verifikasi batas pengajuan dihitung ulang menjadi 3 hari sejak pengajuan awal (sudah terlewat) sehingga mendapat toleransi 24 jam dari waktu Reset
28. Verifikasi warning H-24 terkirim
29. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
30. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
31. Catat jumlah Recalculate Job modul Device Allocation lewat kueri status job Fixture BE sebagai baseline
32. Klik `[Reset to Default]` lagi saat nilai sudah `3`
33. Verifikasi toast sukses "Success, approval settings have been reset to default." tampil
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi jumlah notifikasi approver aktif tidak berubah dari baseline (selisih 0)
36. Verifikasi jumlah notifikasi pemohon tidak berubah dari baseline (selisih 0)
37. Verifikasi jumlah Recalculate Job tidak bertambah dari baseline sehingga tidak ada perubahan batas baru pada pengajuan (selisih 0)

### TC-AC-LCS-515: Partial progress approver AND tidak mereset countdown timeout

38. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` dengan dua approver AND, satu approver sudah menyetujui, Approval Timeout `3`, dan pengajuan diajukan 2 hari lalu
39. Majukan jam server dan jam browser hingga melewati batas 3 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
40. Buka halaman daftar pengajuan Device Allocation
41. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
42. Buka pengajuan Device Allocation tersebut
43. Verifikasi status pengajuan `Canceled` pada batas awal (persetujuan sebagian tidak memperpanjang atau mereset window timeout)

### TC-AC-LCS-516: Pengajuan yang sudah Approved, Rejected, atau Canceled tidak disentuh job timeout

44. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: tiga Device Allocation masing-masing berstatus `Approved`, `Rejected`, dan `Canceled` yang diajukan lebih dari 3 hari lalu
45. Buka halaman daftar pengajuan Device Allocation
46. Ketik Search nomor pengajuan Device Allocation berstatus `Canceled` hasil seeding Fixture BE, tekan Enter
47. Buka pengajuan Device Allocation berstatus `Canceled` tersebut
48. Catat jumlah log pembatalan sistem pada pengajuan tersebut sebagai baseline
49. Picu job Timeout Auto-Cancel modul Device Allocation lewat Fixture BE
50. Buka halaman daftar pengajuan Device Allocation
51. Ketik Search nomor pengajuan Device Allocation berstatus `Approved` hasil seeding Fixture BE, tekan Enter
52. Verifikasi status pengajuan `Approved` tetap `Approved`
53. Ganti isi kotak search dengan nomor pengajuan Device Allocation berstatus `Rejected` hasil seeding Fixture BE, tekan Enter
54. Verifikasi status pengajuan `Rejected` tetap `Rejected`
55. Ganti isi kotak search dengan nomor pengajuan Device Allocation berstatus `Canceled` hasil seeding Fixture BE, tekan Enter
56. Verifikasi status pengajuan `Canceled` tetap `Canceled`
57. Buka pengajuan Device Allocation berstatus `Canceled` tersebut
58. Verifikasi jumlah log pembatalan sistem tidak bertambah dari baseline (selisih 0)

### TC-AC-LCS-517: Pengajuan Trial Activation ikut dihitung ulang sebagai adopter Client Subscription

59. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Switch `Require Approval for Trial Activation` tersimpan `ON` dan trial Client PT Cahaya Baru diajukan Distributor 1 hari lalu berstatus `Waiting for Approval`, lalu buka Plans & Licensing > Lifecycle Settings
60. Klik tab `Approval Settings`
61. Ubah Approval Timeout dari `3` menjadi `2`
62. Klik `[Save]` dan tunggu toast sukses
63. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
64. Majukan jam server dan jam browser hingga 2 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel modul Client Subscription
65. Buka Allocation > Client Subscription > List Subscriptions
66. Ketik Search `PT Cahaya Baru`, tekan Enter
67. Verifikasi status trial PT Cahaya Baru `Canceled` pada batas 2 hari sejak pengajuan awal

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab", "Atur lewat Fixture BE ..." (precondition TC), "Tunggu Recalculate Job ..." (idiom polling kueri status job, batas 2 menit), "Majukan jam ...", "Lepaskan penundaan job ...", dan "Pulihkan ..." antar TC, yang pada langkah 11, 23, dan 59 diakhiri "lalu buka Plans & Licensing > Lifecycle Settings" karena layar terakhir adalah detail pengajuan atau List Subscriptions (S-03, S-07, S-09, R-10); "Buka pengajuan Device Allocation tersebut" (langkah 21, 42) sebelum `Verifikasi` status di detail pengajuan; "Ketik Search ..., tekan Enter" dan "Ganti isi kotak search dengan ..., tekan Enter" (langkah 20, 41, 46, 51, 53, 55, 66) sebelum membuka atau `Verifikasi` baris pengajuan atau trial (R-16, R-23, 8b.9); "Buka halaman daftar pengajuan Device Allocation" (langkah 19, 40, 45, 50) sebelum Search pertama tiap blok atau sesudah job dipicu, agar Search dan `Verifikasi` baris berada di halaman yang benar (S-07, R-23); "Buka pengajuan Device Allocation berstatus `Canceled` tersebut" (langkah 47, 57) untuk membaca log; "Catat jumlah ... sebagai baseline" (langkah 4, 5 sebelum `[Save]` pada TC-AC-LCS-512 agar warning H-24 kedua diasersi sebagai selisih satu per penerima; langkah 29, 30, 31 sebelum `[Reset to Default]` kedua pada TC-AC-LCS-514 agar absence memakai selisih 0; langkah 48 sebelum job pada TC-AC-LCS-516) (S-12); "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 34) sebelum absence notifikasi in-app pada TC-AC-LCS-514 dengan toast langkah 33 sebagai anchor positif (8b.11, bagian 6).
- Urutan TC-AC-LCS-516: pembacaan baseline log pembatalan pengajuan `Canceled` dilakukan sebelum job dipicu sehingga pengajuan `Canceled` dibuka lebih dulu (langkah 45-48); pengecekan `Approved`, `Rejected`, `Canceled` sesudah job tetap berurutan seperti Expected a, b, c.
- Temuan untuk QA: nama dan jalur menu halaman daftar pengajuan Device Allocation tidak tertulis di TC-AC-LCS-512 sampai 516 maupun PRD; langkah "Buka halaman daftar pengajuan Device Allocation" memakai deskripsi generik sampai TC menetapkannya. TC-AC-LCS-514 Expected a menulis "warning H-24 terkirim" tanpa menyebut penerima dan tanpa baseline; spec mengasersinya apa adanya (langkah 28) sampai TC menetapkan penerimanya.
- Temuan untuk QA: TC-AC-LCS-514 Expected b "tidak ada ... perubahan batas baru pada pengajuan" tidak menyebut cara mengamatinya; spec mengasersi jumlah Recalculate Job tidak bertambah (langkah 37). Nomor pengajuan Device Allocation uji tidak tertulis di Pre-setup TC; spec memakai nomor hasil seeding Fixture BE.
- Alasan lebih dari sekitar 35 langkah (67 langkah): spec memuat enam TC (TC-AC-LCS-512 sampai 517) dengan 10, 12, 15, 6, 15, dan 9 langkah; tiap TC diseed ulang lewat Fixture BE di langkah pertamanya. TC-AC-LCS-514 dan TC-AC-LCS-516 paling panjang karena Expected-nya menuntut absence dengan baseline per penerima dan pembacaan tiga status pengajuan.
- Temuan untuk QA: TC-AC-LCS-514 mengklik `[Reset to Default]` lagi saat nilai sudah `3`; TC tidak menyebut apakah tombol aktif pada kondisi itu, dan Expected butir b hanya menyebut toast dan tidak adanya notifikasi atau perubahan batas baru. Langkah TC "→ Approval Timeout `3`" tanpa Expected tidak diasersi (S-02).
- Temuan untuk QA: TC-AC-LCS-516 memuat Expected "tanpa log pembatalan sistem baru" tanpa baseline; spec menambah baseline jumlah log pembatalan sistem (langkah 48) dan memecahnya dari status `Canceled` tetap menjadi dua `Verifikasi` (langkah 56 dan 58, S-01). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
- Temuan untuk QA: mekanisme menunda Recalculate Job, mengajukan trial lewat Distributor, kueri status job, dan pembacaan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
