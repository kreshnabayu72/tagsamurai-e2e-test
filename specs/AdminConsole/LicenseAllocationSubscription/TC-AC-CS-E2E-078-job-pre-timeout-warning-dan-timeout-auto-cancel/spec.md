---
id: TC-AC-CS-E2E-078-job-pre-timeout-warning-dan-timeout-auto-cancel
title: "Job: Pre-timeout Warning dan Timeout Auto-Cancel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-292
  - TC-AC-CS-625
  - TC-AC-CS-294
coverage:
  web: automated
---

# Job: Pre-timeout Warning dan Timeout Auto-Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD` (akun pertama, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite). Ganti akun: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9, `Spectra.env.AC_SUB_DIST_TC_PASSWORD`) sebagai approver aktif. Hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-078`; dibuat lewat sesi API Fajar Nugroho hingga pengajuan tersimpan di hook `before`, dihapus di hook `after`, dan di-seed ulang antar blok oleh fixture backend): Client `Toko Timeout+{runId}-078` (binaan langsung PT Maju Bersama; padanan Pre-setup #133) dengan dua pengajuan Waiting for Approval, FAMS `{idFams}` (Reserve $4,000.00) dan SAMS `{idSams}` (Reserve $3,000.00), plan Growth, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N`, disubmit pada T0 dengan Approval Timeout 3 hari (padanan #134). Subscription ID `{idFams}` dan `{idSams}` dibaca lewat API seeding setiap pengajuan di-seed (dan di-seed ulang) dan dirujuk di langkah sebagai nilai terbaca. Approval Timeout platform 3 hari (#26) dan General Settings Principal PT ABC (#28: Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`) tidak diubah spec.
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (ke T0 + durasi, lihat butir Acuan waktu), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Acuan waktu (T0, bagian 8b butir 3): T0 adalah waktu submit pengajuan seed yang dibaca lewat API seeding setelah pengajuan tersimpan, bukan diperkirakan dari waktu hook atau waktu nyata; `16/08/26 09:00` pada TC hanya contoh. T0 dibaca ulang setiap pengajuan di-seed ulang. Jam server dan jam browser diatur absolut ke T0 + durasi: H-24 pada `T0 + 2 hari`, batas timeout pada `T0 + 3 hari` (Approval Timeout 3 hari). Margin terhadap batas adalah 1 menit, dihitung `T0 + 3 hari ± 1 menit` untuk batas timeout dan `T0 + 2 hari ± 1 menit` untuk batas H-24. Margin kurang dari 5 menit berisiko: selisih beberapa detik antara T0 yang dibaca dan jam yang diatur dapat menukar sisi batas, sehingga T0 dibaca dengan presisi detik dari API dan jam diatur dari nilai itu.
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- Kemampuan teknis (disediakan tim FE/BE): picu satu siklus job pre-timeout warning H-24 dan Timeout Auto-Cancel, dan seed ulang pengajuan dengan waktu submit baru, dan membaca waktu submit pengajuan seed (T0) lewat API seeding.
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after` dan antar blok); pengajuan seed milik spec di-seed ulang antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-292: Pre-timeout warning H-24 terkirim sekali ke approver aktif dan requester

1. Atur jam server dan jam browser ke `T0 + 2 hari`, picu satu siklus job, dan poll hingga job selesai
2. Atur jam server dan jam browser ke `T0 + 2 hari + 3 jam`, picu satu siklus job lagi, dan poll hingga job selesai
3. Buka Notification Center requester `Fajar N`
4. Verifikasi requester menerima notifikasi view-only "Your subscription request is expiring soon" dengan Body "Your request is awaiting decision and will expire in 24 hours if not resolved." (informasional, tanpa frasa "Please finish")
5. Verifikasi requester menerima satu notifikasi warning saja (siklus job kedua tidak mengirim lagi)
6. Logout, lalu login sebagai Total Control Distributor Eko Saputra dan buka Notification Center approver
7. Verifikasi approver aktif menerima notifikasi actionable "Subscription request expiring soon" dengan Body "Request {idFams} will be automatically canceled in 24 hours if no decision is made. Please finish reviewing this request."
8. Verifikasi approver menerima satu notifikasi warning saja (siklus job kedua tidak mengirim lagi)
9. Pulihkan jam server dan jam browser ke jam normal
10. Buka menu Allocation > Client Subscription
11. Buka modal Changelog, ketik Search `{idFams}`, tekan Enter
12. Verifikasi sedikitnya satu entri lain milik `{idFams}` tampil di Changelog
13. Verifikasi warning H-24 tidak ditulis ke Changelog (jumlah entri sama dengan baseline)
14. Tutup modal Changelog dengan `✕`, buka Activity Log, ketik Search `{idFams}`, tekan Enter
15. Verifikasi sedikitnya satu entri lain tampil di Activity Log
16. Verifikasi warning H-24 tidak ditulis ke Activity Log (jumlah entri sama dengan baseline)
17. Buka System Log, ketik Search `{idFams}`, tekan Enter
18. Verifikasi sedikitnya satu entri lain tampil di System Log
19. Verifikasi warning H-24 tidak ditulis ke System Log (jumlah entri sama dengan baseline)
20. Seed ulang pengajuan lewat fixture backend, lalu logout dan login sebagai Create-Only Distributor Fajar Nugroho

### TC-AC-CS-625: Pre-timeout warning H-24 belum terkirim satu menit sebelum batas H-24

21. Atur jam server dan jam browser ke `T0 + 2 hari - 1 menit`, picu satu siklus job, dan poll hingga job selesai
22. Buka Notification Center requester `Fajar N`
23. Verifikasi Notification Center requester tampil
24. Verifikasi belum ada notifikasi "Your subscription request is expiring soon" untuk requester pada `T0 + 2 hari - 1 menit`
25. Logout, login sebagai Total Control Distributor Eko Saputra, dan buka Notification Center approver
26. Verifikasi Notification Center approver tampil
27. Verifikasi belum ada notifikasi "Subscription request expiring soon" untuk approver pada `T0 + 2 hari - 1 menit`
28. Atur jam server dan jam browser ke `T0 + 2 hari`, picu satu siklus job, dan poll hingga job selesai, lalu muat ulang Notification Center approver
29. Verifikasi approver menerima satu notifikasi warning pada `T0 + 2 hari`
30. Logout, login sebagai Create-Only Distributor Fajar Nugroho, dan buka Notification Center requester
31. Verifikasi requester menerima satu notifikasi warning pada `T0 + 2 hari`
32. Buka menu Allocation > Client Subscription
33. Ketik Search `{idSams}`, tekan Enter
34. Verifikasi pengajuan tetap Waiting for Approval
35. Seed ulang pengajuan lewat fixture backend

### TC-AC-CS-294: Batas timeout: tepat pada batas tidak dibatalkan dan setelah batas dibatalkan

36. Atur jam server dan jam browser ke `T0 + 3 hari` (tepat pada batas), picu job Timeout, dan poll hingga job selesai
37. Ganti isi kotak search dengan `Toko Timeout+{runId}-078`, tekan Enter
38. Verifikasi kedua pengajuan `{idFams}` dan `{idSams}` tetap Waiting for Approval pada tepat batas
39. Atur jam server dan jam browser ke `T0 + 3 hari + 1 menit`, picu job Timeout lagi, dan poll hingga job selesai
40. Klik tab "History", ganti isi kotak search dengan `Toko Timeout+{runId}-078`, tekan Enter
41. Verifikasi kedua pengajuan berstatus Canceled satu menit setelah batas
42. Buka Notification Center requester
43. Verifikasi warning H-24 sudah terkirim lebih dulu sebelum pembatalan

## Notes

- Langkah penghubung: Search (R-16: untuk menemukan baris target), penutupan modal, seed ulang pengajuan lewat fixture antar blok, ganti akun dengan `Buka menu Allocation > Client Subscription` sebelum Search atau modal Changelog (S-14), dan pemulihan jam; `Verifikasi Notification Center tampil` mendahului tiap absence notifikasi (8b.2, 8b.11).
- P-1: asersi absence "warning tidak ditulis ke Changelog, System Log, maupun Activity Log" pada TC-AC-CS-292 butir d tetap di spec ini karena bergantung pada state berat (job H-24 dengan jam server digeser); tiap surface didahului Verifikasi entri lain sebagai anchor positif dan memakai baseline jumlah entri (S-12). Jam dipulihkan sebelum membuka log (S-09).
- Alasan spec lebih dari sekitar 35 langkah: ketiga TC satu jenis harness (jam server dan job H-24 atau Timeout) dengan akun requester dan approver yang sama; tiap blok berdiri sendiri dengan seed ulang pengajuan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan pembacaan tiga surface log pada TC-AC-CS-292 memakai blok baca-log berpola.
- Urutan TC: TC-AC-CS-292 dan TC-AC-CS-625 memakai pengajuan berbeda (FAMS dan SAMS) tetapi jam di-seed ulang antar blok karena kedua pengajuan disubmit pada waktu yang sama.
- Temuan untuk QA: (1) TC-AC-CS-294 butir c ("Warning H-24 sudah terkirim lebih dulu") tidak menyebut tempat pengamatannya; spec memakai Notification Center requester. (2) TC-AC-CS-294 langkah 1 pada tepat `T0 + 3 hari` memungkinkan warning H-24 terkirim dalam siklus yang sama dengan pembatalan; urutan kejadian tidak dapat dibuktikan lewat UI. (3) TC-AC-CS-625 akun aktor Create-Only Fajar Nugroho tetapi langkah 3 meminta login sebagai approver; spec menulis ganti akun eksplisit.
