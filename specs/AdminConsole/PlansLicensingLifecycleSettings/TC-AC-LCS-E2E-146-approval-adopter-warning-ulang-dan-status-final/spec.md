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
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan menunda dan melepaskan Recalculate Job, kueri status job, serta pembacaan notifikasi pemohon dan approver aktif.
- Waktu: jam server dan jam browser dimajukan bersama; jam dipulihkan sesudah tiap TC (S-09, R-08). Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab).
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-512: Pengajuan yang sudah menerima warning H-24 dan kini memiliki sisa waktu lebih dari 24 jam mengirim warning lagi pada H-24 baru

1. Atur lewat Fixture BE: Device Allocation berstatus `Waiting for Approval` yang diajukan 2,2 hari lalu dan sudah menerima warning H-24
2. Klik tab `Approval Settings`
3. Ubah Approval Timeout dari `3` menjadi `7`
4. Klik `[Save]` dan tunggu toast sukses
5. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
6. Majukan jam server dan jam browser hingga sisa waktu pengajuan kurang dari 24 jam menuju batas baru lewat Fixture BE, lalu picu job pemeriksaan
7. Verifikasi approver aktif menerima warning H-24 kedua (penanda warning direset oleh recalculation)
8. Verifikasi pemohon menerima warning H-24 kedua (penanda warning direset oleh recalculation)

### TC-AC-LCS-513: Save Approval Timeout berikutnya saat recalculation sebelumnya berjalan: job sebelumnya digantikan

9. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` yang diajukan 1 hari lalu dan Recalculate Job ditunda lewat fixture BE agar masih berjalan saat Save kedua
10. Klik tab `Approval Settings`
11. Ubah Approval Timeout dari `3` menjadi `2`
12. Klik `[Save]` dan tunggu toast sukses
13. Sebelum job pertama selesai, ubah Approval Timeout menjadi `5`
14. Klik `[Save]` dan tunggu toast sukses
15. Lepaskan penundaan job lewat Fixture BE dan tunggu seluruh job selesai lewat kueri status job (batas tunggu 2 menit)
16. Majukan jam server dan jam browser hingga 3 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
17. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
18. Buka pengajuan Device Allocation tersebut
19. Verifikasi status pengajuan tetap `Waiting for Approval` (batas mengikuti nilai tersimpan terakhir `5`, bukan `2`)

### TC-AC-LCS-514: Reset to Default Approval Timeout menjalankan recalculation hanya bila nilai sebelumnya berbeda dari 3

20. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Approval Timeout tersimpan `7` dan Device Allocation berstatus `Waiting for Approval` yang diajukan 4 hari lalu, lalu muat ulang halaman Lifecycle Settings
21. Klik tab `Approval Settings`
22. Klik `[Reset to Default]`
23. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
24. Verifikasi batas pengajuan dihitung ulang menjadi 3 hari sejak pengajuan awal (sudah terlewat) sehingga mendapat toleransi 24 jam dari waktu Reset
25. Verifikasi warning H-24 terkirim
26. Catat jumlah notifikasi approver aktif lewat kemampuan baca notifikasi sebagai baseline
27. Catat jumlah notifikasi pemohon lewat kemampuan baca notifikasi sebagai baseline
28. Catat jumlah Recalculate Job modul Device Allocation lewat kueri status job Fixture BE sebagai baseline
29. Klik `[Reset to Default]` lagi saat nilai sudah `3`
30. Verifikasi toast sukses "Success, approval settings have been reset to default." tampil
31. Verifikasi jumlah notifikasi approver aktif tidak berubah dari baseline (selisih 0)
32. Verifikasi jumlah notifikasi pemohon tidak berubah dari baseline (selisih 0)
33. Verifikasi jumlah Recalculate Job tidak bertambah dari baseline sehingga tidak ada perubahan batas baru pada pengajuan (selisih 0)

### TC-AC-LCS-515: Partial progress approver AND tidak mereset countdown timeout

34. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Device Allocation berstatus `Waiting for Approval` dengan dua approver AND, satu approver sudah menyetujui, Approval Timeout `3`, dan pengajuan diajukan 2 hari lalu
35. Majukan jam server dan jam browser hingga melewati batas 3 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel
36. Ketik Search nomor pengajuan Device Allocation uji hasil seeding Fixture BE, tekan Enter
37. Buka pengajuan Device Allocation tersebut
38. Verifikasi status pengajuan `Canceled` pada batas awal (persetujuan sebagian tidak memperpanjang atau mereset window timeout)

### TC-AC-LCS-516: Pengajuan yang sudah Approved, Rejected, atau Canceled tidak disentuh job timeout

39. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: tiga Device Allocation masing-masing berstatus `Approved`, `Rejected`, dan `Canceled` yang diajukan lebih dari 3 hari lalu
40. Picu job Timeout Auto-Cancel modul Device Allocation lewat Fixture BE
41. Ketik Search nomor pengajuan Device Allocation berstatus `Approved` hasil seeding Fixture BE, tekan Enter
42. Verifikasi status pengajuan `Approved` tetap `Approved`
43. Ketik Search nomor pengajuan Device Allocation berstatus `Rejected` hasil seeding Fixture BE, tekan Enter
44. Verifikasi status pengajuan `Rejected` tetap `Rejected`
45. Ketik Search nomor pengajuan Device Allocation berstatus `Canceled` hasil seeding Fixture BE, tekan Enter
46. Verifikasi status pengajuan `Canceled` tetap `Canceled` tanpa log pembatalan sistem baru

### TC-AC-LCS-517: Pengajuan Trial Activation ikut dihitung ulang sebagai adopter Client Subscription

47. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Switch `Require Approval for Trial Activation` tersimpan `ON` dan trial Client PT Cahaya Baru diajukan Distributor 1 hari lalu berstatus `Waiting for Approval`
48. Klik tab `Approval Settings`
49. Ubah Approval Timeout dari `3` menjadi `2`
50. Klik `[Save]` dan tunggu toast sukses
51. Tunggu Recalculate Job selesai lewat kueri status job Fixture BE (batas tunggu 2 menit)
52. Majukan jam server dan jam browser hingga 2 hari sejak pengajuan awal lewat Fixture BE, lalu picu job Timeout Auto-Cancel modul Client Subscription
53. Buka Allocation > Client Subscription > List Subscriptions
54. Ketik Search `PT Cahaya Baru`, tekan Enter
55. Verifikasi status trial PT Cahaya Baru `Canceled` pada batas 2 hari sejak pengajuan awal

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab", "Atur lewat Fixture BE ..." (precondition TC), "Tunggu Recalculate Job ..." (idiom polling kueri status job, batas 2 menit), "Majukan jam ...", "Lepaskan penundaan job ...", dan "Pulihkan ..." antar TC (S-03, S-09, R-10); "Ketik Search ..., tekan Enter" (langkah 17, 36, 41, 43, 45, 54) sebelum membuka atau `Verifikasi` baris pengajuan atau trial (R-16, R-23); "Catat jumlah ... sebagai baseline" (langkah 26, 27, 28) sebelum `[Reset to Default]` kedua pada TC-AC-LCS-514 agar absence memakai selisih 0 (S-12).
- Temuan untuk QA: TC-AC-LCS-514 Expected b "tidak ada ... perubahan batas baru pada pengajuan" tidak menyebut cara mengamatinya; spec mengasersi jumlah Recalculate Job tidak bertambah (langkah 33). Nomor pengajuan Device Allocation uji tidak tertulis di Pre-setup TC; spec memakai nomor hasil seeding Fixture BE.
- Alasan lebih dari sekitar 35 langkah: enam blok TC mengambil pola yang sama (state pengajuan diseed, Approval Timeout diubah, jam dimajukan, job dipicu), semuanya satu kelas harness yang sama, dan tiap blok diseed ulang sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC-AC-LCS-514 mengklik `[Reset to Default]` lagi saat nilai sudah `3`; TC tidak menyebut apakah tombol aktif pada kondisi itu, dan Expected butir b hanya menyebut toast dan tidak adanya notifikasi atau perubahan batas baru. Langkah TC "→ Approval Timeout `3`" tanpa Expected tidak diasersi (S-02).
- Temuan untuk QA: TC-AC-LCS-516 memuat Expected "tanpa log pembatalan sistem baru" tanpa baseline; spec mencatatnya dalam `Verifikasi` yang sama dengan status `Canceled` tetap (S-01). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
- Temuan untuk QA: mekanisme menunda Recalculate Job, mengajukan trial lewat Distributor, kueri status job, dan pembacaan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
