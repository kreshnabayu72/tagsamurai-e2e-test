---
id: TC-FA-FAAC-E2E-105-versi-scheduled-job-penerapan-otomatis
title: "Versi Scheduled: Job Latar Menerapkan Versi Otomatis, Kegagalan Job, dan Pencatatan Log oleh System"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-326
  - TC-FA-FAAC-328
  - TC-FA-FAAC-329
  - TC-FA-FAAC-533
coverage:
  web: automated
---

# Versi Scheduled: Job Latar Menerapkan Versi Otomatis, Kegagalan Job, dan Pencatatan Log oleh System

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite. Aktor hanya pengamat; job dipicu lewat kemampuan di bawah (job latar adalah objek uji spec ini, kelas d).
- Data seed (kode literal TC, disediakan tim FE/BE lewat fixture BE): Asset Class `B-JOB` dipakai aset dengan versi Scheduled yang Effective From-nya bulan berjalan; `B-JOBF` dengan versi Scheduled yang jatuh tempo; `B-JOBI` Inactive dengan versi Scheduled yang jatuh tempo; `B-JOB2` dengan versi Scheduled yang jatuh tempo dan perubahan Useful Life Old 48 New 60 serta Declining Rate Old 50 New 40. Setiap versi Scheduled mengubah sedikitnya satu field (mis. Useful Life).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): memicu job latar penerapan versi Scheduled di lingkungan uji untuk satu Asset Class sasaran per pemicu (parameter kode Asset Class), termasuk dengan kegagalan yang disuntikkan untuk `B-JOBF`, dan membaca kembali jumlah entri Changelog, Activity Log FAMS, dan System Log Detail User aktor. Menunggu hasil job memakai idiom polling "muat ulang halaman tiap 5 detik, batas tunggu 2 menit" (bagian 6 konvensi).
- Pemicu job per Asset Class: keempat Asset Class seed jatuh tempo bersamaan, sehingga satu pemicu global akan menerapkan semuanya dan menghabiskan baseline blok lain (dan kegagalan `B-JOBF` tidak terjadi). Karena itu tiap langkah pemicu menyebut satu sasaran: `B-JOB` (langkah 3), `B-JOBI` (langkah 16), `B-JOBF` dengan kegagalan yang disuntikkan (langkah 27), `B-JOBF` putaran berikutnya tanpa kegagalan (langkah 35), dan `B-JOB2` (langkah 42); versi Scheduled Asset Class lain tetap Scheduled sampai blok miliknya.
- Pemicu job bersifat sinkron: setiap langkah pemicu baru kembali setelah job selesai, termasuk job dengan kegagalan yang disuntikkan, sehingga asersi absence TC-328 (langkah 29 sampai 33) dibaca sesudah job selesai tanpa polling (kemampuan disediakan tim FE/BE, S-13).
- Jam: bulan berjalan mengikuti zona waktu General Settings client (NC-11); spec ini tidak menggeser jam server atau jam browser.
- Audit trail permanen (Changelog, Activity Log, System Log) dibaca dengan baseline jumlah entri sebelum aksi dan asersi memakai selisih (S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: versi Scheduled keempat Asset Class dibuat ulang dan nilai berlaku dipulihkan; pemulihan injeksi kegagalan job dijamin hook `after`.
- Kode seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-JOB`, tekan Enter

### TC-FA-FAAC-326: Versi Scheduled berlaku otomatis pada Effective From oleh job sistem

2. Catat jumlah entri Changelog sebagai baseline N
3. Picu job penerapan versi terjadwal di lingkungan uji hanya untuk `B-JOB`
4. Verifikasi tidak ada toast yang tampil (tidak ada user aktor)
5. Klik link Class Code `B-JOB` di tabel
6. Muat ulang halaman tiap 5 detik sampai Alert versi Scheduled hilang (batas tunggu 2 menit)
7. Verifikasi Alert versi Scheduled hilang
8. Klik tab `Depreciation`
9. Verifikasi nilai berlaku berubah ke versi baru
10. Buka Changelog
11. Verifikasi jumlah entri Changelog bertambah sebanyak field yang berubah pada versi Scheduled
12. Verifikasi Changelog memuat Edit untuk tiap field yang berubah (mis. `Useful Life`) dengan Modified By `System`
13. Tutup modal Changelog

### TC-FA-FAAC-329: Versi Scheduled pada Asset Class Inactive tetap berlaku otomatis

14. Klik breadcrumb `Asset Class`
15. Catat jumlah entri Changelog sebagai baseline N
16. Picu job penerapan versi terjadwal hanya untuk `B-JOBI`
17. Klik link Class Code `B-JOBI` di tabel
18. Muat ulang halaman tiap 5 detik sampai Alert versi Scheduled hilang (batas tunggu 2 menit)
19. Verifikasi Alert versi Scheduled hilang
20. Klik tab `Depreciation`
21. Verifikasi versi Scheduled diterapkan walau Asset Class Inactive (nilai berlaku berubah ke versi baru)
22. Buka Changelog
23. Verifikasi Changelog memuat entri baru dengan Modified By `System` (jumlah entri bertambah dari N)
24. Tutup modal Changelog

### TC-FA-FAAC-328: Kegagalan job penerapan versi menjaga versi tetap Scheduled

25. Klik breadcrumb `Asset Class`
26. Catat jumlah entri Changelog sebagai baseline N
27. Picu job penerapan versi terjadwal hanya untuk `B-JOBF` dengan kegagalan yang disuntikkan
28. Klik link Class Code `B-JOBF` di tabel
29. Verifikasi versi tetap Scheduled dan Alert versi Scheduled masih tampil
30. Klik tab `Depreciation`
31. Verifikasi nilai berlaku tidak berubah
32. Buka Changelog
33. Verifikasi tidak ada entri Changelog baru (jumlah entri tetap N)
34. Tutup modal Changelog
35. Picu job penerapan versi terjadwal hanya untuk `B-JOBF` pada putaran berikutnya tanpa kegagalan
36. Muat ulang halaman tiap 5 detik sampai Alert versi Scheduled hilang (batas tunggu 2 menit)
37. Verifikasi versi berlaku (Alert versi Scheduled hilang)

### TC-FA-FAAC-533: Log versi terjadwal via job hanya di Changelog dan Activity Log

38. Klik breadcrumb `Asset Class`
39. Catat jumlah entri Changelog sebagai baseline N
40. Buka Detail User aktor, tab System Log, dan catat jumlah entri sebagai baseline Ns
41. Buka Activity Log FAMS dan catat jumlah entri sebagai baseline Na
42. Picu job penerapan versi terjadwal hanya untuk `B-JOB2`
43. Buka Fixed Asset > Settings > Accounting, lalu klik tab `Asset Class`
44. Muat ulang halaman Asset Class tiap 5 detik sampai jumlah entri Changelog bertambah dari N (batas tunggu 2 menit)
45. Buka ikon Changelog di toolbar tabel Asset Class
46. Verifikasi Changelog memuat baris per field yang berubah (mis. `Useful Life` Old 48 New 60 dan `Declining Rate` Old 50 New 40) dengan Modified By `System`
47. Tutup modal Changelog
48. Buka Activity Log FAMS
49. Verifikasi Activity Log memuat baris yang sama dengan Modified By `System` (jumlah entri bertambah dari Na)
50. Buka Detail User aktor, tab System Log
51. Verifikasi System Log tidak memuat entri untuk kejadian ini (jumlah entri tetap Ns)

## Notes

1. Urutan dalam spec: TC-326 (job normal) dan TC-329 (Asset Class Inactive) lebih dulu, lalu TC-328 yang memicu kegagalan job, dan TC-533 yang membaca log di tiga surface di akhir. Spec ini kelas d (harness eksternal: job latar sebagai objek uji); TC-328 (kegagalan job) dipertahankan di sini karena objek ujinya tetap job penerapan versi, bukan fault injection pada request browser.
2. Id P/K: tidak ada id P/K yang dipakai TC-328. Kegagalan job yang disuntikkan adalah bagian dari harness job latar yang sama dengan objek uji spec kelas d ini (bukan kelas b intercept request browser dan bukan pemicu `P-2`), sehingga tidak butuh pengecualian.
3. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), langkah 2, 15, 26, 39, 40, dan 41 (baseline audit trail, S-12), langkah 13, 24, 34, dan 47 (menutup modal Changelog), serta langkah 14, 25, dan 38 (kembali ke tabel) dan langkah 43 (kembali ke tab Asset Class di modul asal setelah membaca Detail User dan Activity Log, S-14). Langkah 44 menunggu hasil job dengan idiom polling (bagian 6).
4. Entri Changelog baru dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (S-14).
5. Absence System Log (langkah 51) adalah asersi cakupan log atas surface yang berbeda dengan anchor positif: entri Changelog dan Activity Log yang sudah terbukti muncul untuk pemicu yang sama (langkah 46 dan 49), dengan baseline Ns; ini bukan spec absence kelas g (bagian 3 prinsip 13g, scope exclusion dengan anchor positif).
6. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal dengan versi Scheduled jatuh tempo; kode dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
7. Alasan melebihi sekitar 35 langkah (51 langkah): spec ini berisi empat blok kelas d yang sama (job latar penerapan versi Scheduled) dan masing-masing berdiri sendiri pada Asset Class berbeda dengan versi Scheduled sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah pembacaan baseline dan polling job yang berulang pada tiap blok.
8. Temuan untuk QA: TC-533 Expected c menyebut "System Log setiap user"; spec hanya mengamati System Log Detail User aktor karena TC tidak menyebut daftar user lain. TC-326 tidak menyebut field yang berubah pada versi Scheduled (hanya "mis. Useful Life"); spec menuntut seed yang mengubah sedikitnya satu field. Pemicu job dan injeksi kegagalan tidak didefinisikan di TC maupun PRD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
