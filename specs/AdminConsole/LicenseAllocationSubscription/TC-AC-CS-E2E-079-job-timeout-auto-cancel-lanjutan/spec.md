---
id: TC-AC-CS-E2E-079-job-timeout-auto-cancel-lanjutan
title: "Job: Timeout Auto-Cancel Lanjutan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-293
  - TC-AC-CS-296
  - TC-AC-CS-295
coverage:
  web: automated
---

# Job: Timeout Auto-Cancel Lanjutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD` (akun pertama, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite). Ganti akun: Eko Saputra, Total Control Distributor PT Maju Bersama (Pre-setup #9, `Spectra.env.AC_SUB_DIST_TC_PASSWORD`) sebagai approver aktif dan aktor TC-AC-CS-296. Hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data seed milik spec (bersuffix `{runId}-079`): Client `Toko Timeout+{runId}-079` dengan pengajuan Waiting for Approval ber-Reserve `{idFams}` (FAMS, plan Growth, Plan Owner PT Maju Bersama (Distributor)) disubmit pada T0 oleh Fajar Nugroho, Approval Timeout 3 hari (#26, #134); pengajuan Trial Waiting for Approval `{idTrial}` (Client `Toko Timeout+{runId}-079`, SIEM, plan SIEM, badge Trial) disubmit pada T0 oleh Eko Saputra dengan Toggle Trial ON (#24); pengajuan SAMS Growth `{idSams}` Waiting for Approval milik Fajar Nugroho yang disetujui approver tepat sebelum tick job Timeout (TC-AC-CS-295, Data Dinamis #3). Subscription ID `{idFams}`, `{idTrial}`, dan `{idSams}` dibaca lewat API seeding setiap pengajuan dibuat atau di-seed ulang dan dirujuk di langkah sebagai nilai terbaca (S-12). Semuanya dibuat lewat sesi API requester hingga pengajuan tersimpan di hook `before`, dihapus di hook `after`, dan di-seed ulang antar blok oleh fixture backend. General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (ke T0 + durasi, lihat butir Acuan waktu), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state Pre-setup yang diubah spec dilakukan fixture backend yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (suite.md; S-06 pengecualian 2026-10-30).
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Acuan waktu (T0, bagian 8b butir 3): T0 adalah waktu submit pengajuan seed yang dibaca lewat API seeding setelah pengajuan tersimpan, bukan diperkirakan dari waktu hook atau waktu nyata; `16/08/26 09:00` pada TC hanya contoh. T0 dibaca ulang setiap pengajuan di-seed ulang. Jam server dan jam browser diatur absolut ke T0 + durasi: batas timeout pada `T0 + 3 hari` (Approval Timeout 3 hari) dan pemicu job pada `T0 + 3 hari + 1 menit`, dihitung `T0 + 3 hari ± 1 menit`. Margin kurang dari 5 menit berisiko: selisih beberapa detik antara T0 yang dibaca dan jam yang diatur dapat menukar sisi batas, sehingga T0 dibaca dengan presisi detik dari API dan jam diatur dari nilai itu.
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- Kemampuan teknis (disediakan tim FE/BE): picu satu siklus job Timeout Auto-Cancel, picu Approve pelaku kedua (approver Total Control Distributor) lewat sesi API tepat sebelum tick job (TC-AC-CS-295), dan kemampuan baca saldo Wallet.
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after`, antar blok, dan sebelum membuka log); pengajuan di-seed ulang antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-293: Timeout Auto-Cancel membatalkan pengajuan tanpa pelaku manusia

1. Atur jam server dan jam browser ke `T0 + 3 hari + 1 menit`, picu satu siklus job, dan poll hingga job selesai
2. Klik tab "History", ketik Search `{idFams}`, tekan Enter
3. Verifikasi pengajuan berstatus Canceled tanpa pelaku manusia
4. Verifikasi Reserve term (dan Reserve alokasi bila ada) dilepas penuh
5. Klik ikon `⋯` pada baris Canceled
6. Verifikasi menu row action baris Canceled menampilkan Resubmit bagi requester original
7. Tutup menu, pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `{idFams}`, tekan Enter
8. Verifikasi entri baru Changelog mencatat Action `Timeout Auto-Cancel`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `System`
9. Tutup modal Changelog dengan `✕`, buka System Log, ketik Search `{idFams}`, tekan Enter
10. Verifikasi sedikitnya satu entri lain tampil di System Log
11. Verifikasi System Log tidak memuat entri baru karena tidak ada user aktor (jumlah entri sama dengan baseline)
12. Buka Notification Center requester `Fajar N`
13. Verifikasi requester menerima notifikasi "Subscription request canceled automatically" dengan Body "Your request has expired after 3 days without a decision and has been automatically canceled. Please resubmit if still needed."
14. Logout, lalu login sebagai Total Control Distributor Eko Saputra dan buka Notification Center approver
15. Verifikasi approver aktif menerima notifikasi "Subscription request canceled automatically" dengan Body "{idFams} · FAMS · Toko Timeout+{runId}-079"

### TC-AC-CS-296: Timeout Auto-Cancel pada pengajuan Trial

16. Seed ulang pengajuan lewat fixture backend, atur jam server dan jam browser ke `T0 + 3 hari + 1 menit`, picu satu siklus job, dan poll hingga job selesai
17. Buka menu Allocation > Client Subscription
18. Klik tab "History", ketik Search `{idTrial}`, tekan Enter
19. Verifikasi baris Trial berstatus Canceled dan Client tidak disentuh
20. Pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `{idTrial}`, tekan Enter
21. Verifikasi entri baru Changelog mencatat Action `Timeout Auto-Cancel (Trial)`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `System`
22. Tutup modal Changelog dengan `✕`, lalu buka Notification Center approver `Eko Saputra`
23. Verifikasi H-24 warning sudah terkirim lebih dulu ke approver
24. Logout, lalu login sebagai Create-Only Distributor Fajar Nugroho dan buka Notification Center requester `Fajar N`
25. Verifikasi H-24 warning sudah terkirim lebih dulu ke requester
26. Seed ulang pengajuan lewat fixture backend

### TC-AC-CS-295: Job Timeout melewati pengajuan yang sudah diputuskan atau dibatalkan

27. Buka Allocation > Client Subscription tab "Current"
28. Buka modal Changelog, ketik Search `{idSams}`, tekan Enter, catat jumlah entri sebagai baseline, lalu tutup modal dengan `✕`
29. Atur jam server dan jam browser ke `T0 + 3 hari + 1 menit`, approve pengajuan SAMS Growth lewat sesi API approver Total Control Distributor tepat sebelum tick job hingga keputusan tersimpan, lalu picu job Timeout pada tick berikutnya dan poll hingga job selesai
30. Ketik Search `{idSams}`, tekan Enter
31. Verifikasi pengajuan berstatus hasil Approve di tab "Current"
32. Pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `{idSams}`, tekan Enter
33. Verifikasi sedikitnya satu entri baru dibanding baseline tampil di Changelog
34. Verifikasi tidak ada entri baru dengan Action `Timeout Auto-Cancel`

## Notes

- Langkah penghubung: tab, Search (R-16: untuk menemukan baris target), penutupan modal dan menu, seed ulang pengajuan lewat fixture antar blok, ganti akun (dengan `Buka menu Allocation > Client Subscription` sebelum aksi List), serta pemulihan jam.
- P-1: asersi absence "System Log tidak memuat entri karena tidak ada user aktor" pada TC-AC-CS-293 butir c tetap di spec ini karena bergantung pada state berat (Timeout Auto-Cancel dengan jam server digeser); didahului Verifikasi entri lain sebagai anchor positif dan memakai baseline jumlah entri (S-12).
- Urutan TC: TC-AC-CS-296 sebelum TC-AC-CS-295 agar akun approver dipakai berurutan setelah TC-AC-CS-293. TC-AC-CS-296 berpindah dari akun Eko Saputra, yang aktif sejak akhir blok sebelumnya.
- Temuan untuk QA: (1) TC-AC-CS-295 berklasifikasi dua proses paralel dan precondition menyebut Data Dinamis #3 dari TC-AC-CS-147; spec men-seed pengajuan sendiri (S-06). (2) TC-AC-CS-295 tidak menyebut tempat pengamatan butir a dan b; spec memakai status pengajuan pada List dan Changelog; status akhir hasil Approve tidak disebut TC, sehingga spec mengasersi status hasil Approve tanpa nilai dan nilainya perlu diisi QA. (3) TC-AC-CS-296 butir c menyebut H-24 warning ke approver Principal dan requester tanpa langkah observasi; spec memakai Verifikasi sesuai Expected tanpa menambah langkah observasi sendiri (kemampuan baca notifikasi disediakan tim FE/BE). (4) TC-AC-CS-293 butir f menyebut Resubmit tersedia bagi requester original; spec mengamatinya sebagai Fajar Nugroho.
