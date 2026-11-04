---
id: TC-AC-ACC-E2E-268-pencatatan-log-aksi-sistem-auto-archive-auto-reactivate-dan-send-activation-email
title: "Pencatatan Log Aksi Sistem: Auto-Archive, Auto-Reactivate, dan Send Activation Email dengan Modified By System"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-423
  - TC-AC-ACC-424
  - TC-AC-ACC-999
coverage:
  web: automated
---

# Pencatatan Log Aksi Sistem: Auto-Archive, Auto-Reactivate, dan Send Activation Email dengan Modified By System

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data seed milik spec (replika bersuffix `{runId}-268` dengan atribut setara fixture A3 asal TC; di-seed lewat skrip seed atau Fixture BE di hook `before`, bukan lewat UI, dan dihapus di hook `after`; kemampuan disediakan tim FE/BE; S-06; aksi sistem tidak dapat dibalik dari UI sehingga tiap run memakai replika baru): `PT Auto Arsip Uji {runId}-268` (setara C-AST-11: Active; FAMS Active sebagai satu-satunya term; Partner CV Mitra Sejati; Group Area Jakarta; TC-AC-ACC-423); `PT Arsip Uji Reaktivasi {runId}-268` (setara C-AST-9: Archived; FAMS Archive; Partner CV Mitra Sejati; Group Area Jakarta; TC-AC-ACC-424); `PT Catat Kirim Awal {runId}-268` (setara C-FX14-2: Active; Direct; Group Area Jakarta; belum pernah memiliki subscription; Default User Not Yet Activated dengan email `fx14-002+{runId}-268@qwertysystem.net`; belum ada baris Changelog Action `Send Activation Email`; TC-AC-ACC-999). Nama Client unik sehingga baseline log bernilai nol, tetap dicatat (S-12).
- Kemampuan teknis: pemicu aksi di modul lain, yaitu Admin Console > Client Subscription (Cancel term FAMS; menambah term FAMS baru mode New terotorisasi langsung dengan Plan Professional, Duration 1 year(s), Start Date hari ini; mengaktifkan term pertama), memakai UI modul itu atau sesi API aktor (disediakan tim FE); pembacaan Changelog: Client, System Log akun aktor, dan Activity Log (Tab User Action, disaring Object `Client`).
- Baseline (S-12): jumlah baris log dicatat dengan Search nama Client dan Action sebelum aksi, ukuran halaman 100; asersi memakai selisih terhadap baseline. Jam server dan jam browser sinkron; "tanggal hari ini" dibandingkan dengan tanggal pada Time Zone General Settings, toleransi satu menit untuk kolom Date.
- General Settings: Date Format, Time Format, dan Time Zone tidak diubah.
- State global: log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-423: Log Auto-Archive

1. Klik ikon Changelog di toolbar List, ketik Search "PT Auto Arsip Uji {runId}-268" di modal, tekan Enter, ubah ukuran halaman menjadi 100, catat jumlah baris Action `Auto-Archive` (C1), lalu tutup modal
2. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Auto Arsip Uji {runId}-268", tekan Enter, dan catat jumlah baris Action `Auto-Archive` (V1)
3. Cancel term FAMS "PT Auto Arsip Uji {runId}-268" dari Admin Console > Client Subscription hingga pembatalan tersimpan
4. Buka Admin Console > Client, klik sub-tab Archived, ketik Search "PT Auto Arsip Uji {runId}-268", tekan Enter
5. Verifikasi baris "PT Auto Arsip Uji {runId}-268" tampil di sub-tab Archived
6. Verifikasi sel Modified By baris itu `System` (teks biasa, bukan format nama orang)
7. Verifikasi sel Last Updated baris itu memuat tanggal hari ini
8. Klik ikon Changelog di toolbar List, ketik Search "PT Auto Arsip Uji {runId}-268" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
9. Verifikasi jumlah baris Action `Auto-Archive` = C1 + 1
10. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Auto-Archive`, Client Name `PT Auto Arsip Uji {runId}-268`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`
11. Tutup modal, buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, klik ikon Search, ketik "PT Auto Arsip Uji {runId}-268", tekan Enter
12. Verifikasi jumlah baris Action `Auto-Archive` = V1 + 1
13. Verifikasi baris teratas (Date terbaru): Action `Auto-Archive`, Object `Client`, Name `PT Auto Arsip Uji {runId}-268`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`

### TC-AC-ACC-424: Log Auto-Reactivate

14. Klik ikon Changelog di toolbar List, ketik Search "PT Arsip Uji Reaktivasi {runId}-268" di modal, tekan Enter, ubah ukuran halaman menjadi 100, catat jumlah baris Action `Auto-Reactivate` (C2), lalu tutup modal
15. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Arsip Uji Reaktivasi {runId}-268", tekan Enter, dan catat jumlah baris Action `Auto-Reactivate` (V2)
16. Tambah term FAMS baru (mode New, terotorisasi langsung, Plan Professional, Duration 1 year(s), Start Date hari ini) untuk "PT Arsip Uji Reaktivasi {runId}-268" dari Admin Console > Client Subscription hingga term tersimpan
17. Buka Admin Console > Client, klik sub-tab Active, ketik Search "PT Arsip Uji Reaktivasi {runId}-268", tekan Enter
18. Verifikasi baris "PT Arsip Uji Reaktivasi {runId}-268" tampil di sub-tab Active
19. Verifikasi sel Modified By baris itu `System` (teks biasa, bukan format nama orang)
20. Verifikasi sel Last Updated baris itu memuat tanggal hari ini
21. Klik ikon Changelog di toolbar List, ketik Search "PT Arsip Uji Reaktivasi {runId}-268" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
22. Verifikasi jumlah baris Action `Auto-Reactivate` = C2 + 1
23. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Auto-Reactivate`, Client Name `PT Arsip Uji Reaktivasi {runId}-268`, Field `Status`, Old Value `Archived`, New Value `Active`, Modified By `System`
24. Tutup modal, buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, klik ikon Search, ketik "PT Arsip Uji Reaktivasi {runId}-268", tekan Enter
25. Verifikasi jumlah baris Action `Auto-Reactivate` = V2 + 1
26. Verifikasi baris teratas (Date terbaru): Action `Auto-Reactivate`, Object `Client`, Name `PT Arsip Uji Reaktivasi {runId}-268`, Field `Status`, Old Value `Archived`, New Value `Active`, Modified By `System`

### TC-AC-ACC-999: Activation Email otomatis pertama tercatat sebagai Send Activation Email

27. Klik [Changelog] di toolbar List, ketik Search "PT Catat Kirim Awal {runId}-268" di modal, tekan Enter, ubah ukuran halaman menjadi 100, hitung baris Action `Send Activation Email` (N1), lalu tutup modal
28. Verifikasi jumlah baris Action `Send Activation Email` terbaca dan tercatat sebagai N1 (baseline; tidak diasumsikan 0)
29. Aktifkan term pertama FAMS "PT Catat Kirim Awal {runId}-268" (mode New, terotorisasi langsung, Plan Professional, Duration 1 year(s), Start Date hari ini) dari Admin Console > Client Subscription hingga term tersimpan
30. Buka Admin Console > Client, klik [Changelog] di toolbar List, ketik Search "PT Catat Kirim Awal {runId}-268" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
31. Verifikasi jumlah baris Action `Send Activation Email` (N2) = N1 + 1
32. Verifikasi baris teratas: Action `Send Activation Email`, Client Name `PT Catat Kirim Awal {runId}-268`, Field `Email`, Old Value `—`, New Value `fx14-002+{runId}-268@qwertysystem.net`, Modified By `System`
33. Tutup modal, buka Activity Log Admin Console (Tab User Action), saring Object `Client`, klik ikon Search, ketik "PT Catat Kirim Awal {runId}-268", tekan Enter
34. Verifikasi baris teratas: Action `Send Activation Email`, Object `Client`, Name `PT Catat Kirim Awal {runId}-268`, Field `Email`, Old Value `—`, New Value `fx14-002+{runId}-268@qwertysystem.net`, Modified By `System`

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): langkah 1, 2, 8, 11, 14, 15, 21, 24, 27, 30, 33 (Search nama Client, ukuran halaman 100, dan baseline jumlah baris log pada audit trail permanen, S-14; TC-AC-ACC-423 dan 424 tidak mencatat baseline), langkah 4 dan 17 (membuka sub-tab dan Search untuk mengamati baris Client).
- TC-AC-ACC-999 terbelah antara presence dan absence: butir d ("tidak ada baris Action `Send Activation Email` di System Log akun aktor") adalah asersi absence kelas g dan diasersi dengan aksi nyata dan baseline sendiri di spec 272; TC-AC-ACC-999 tercantum di `sourceTc` kedua spec (S-05).
- Aksi tulis pemicu (Cancel term, tambah term, aktifkan term pertama) menargetkan replika bersuffix `{runId}-268` (S-06), bukan fixture A3 C-AST-11, C-AST-9, dan C-FX14-2 yang dikonsumsi bersama.
- Pembagian TC lintas spec: log Create/Edit/Change Partner di spec 266; log Suspend/Unsuspend/Bulk di spec 267; log Resend dan BYO di spec 269; log Asset Control di spec 270; log Delete di spec 271.
- Temuan untuk QA:
  - TC-AC-ACC-423 dan 424 tidak menyebut langkah UI di modul Client Subscription (Cancel term, tambah term); spec menyebut aksi dan hasil, langkah rinci mengikuti TC modul Client Subscription. Auto-Archive dan Auto-Reactivate adalah aksi sistem dan tidak punya langkah baca System Log.
  - TC-AC-ACC-999 Expected a mencatat N1 sebagai baseline (tidak diasumsikan 0), sesuai bagian 8b butir 10 dan S-12 karena Changelog adalah audit trail permanen: replika `PT Catat Kirim Awal {runId}-268` unik per run sehingga N1 diharapkan nol, tetapi asersi utama tetap selisih N2 = N1 + 1.
