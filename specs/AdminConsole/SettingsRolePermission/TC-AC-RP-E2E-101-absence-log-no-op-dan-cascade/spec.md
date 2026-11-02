---
id: TC-AC-RP-E2E-101-absence-log-no-op-dan-cascade
title: "Absence Log: Edit No-Op dan Cascade Role yang Sudah Di-assign"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-318
  - TC-AC-RP-334
coverage:
  web: automated
---

# Absence Log: Edit No-Op dan Cascade Role yang Sudah Di-assign

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `John Dohan`), #15 (penugasan peran individual), dan #17 (approver dan toggle: `Manage allocation` `Sumatera` OFF tersimpan). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini. Admin B (#24) memakai sesi API aktor (login API password, token tidak dihitung sebagai sesi web; dinyatakan di `suite.md`) yang hanya memicu perubahan state; Admin B adalah akun yang disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA).
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: reset data Pre-setup (tingkat akses dan toggle) disediakan tim FE/BE.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-318: Assign Total Control mencatat cascade per Global Role yang belum di-assign

1. Klik tab `System`
2. Catat baseline jumlah entri Changelog Tab System
3. Klik tab `Total Control`
4. Klik tombol "+ Assign"
5. Centang `John Dohan` (memegang `Manage device master data`) lalu klik `[Assign]`
6. Klik tab `System`
7. Klik ikon Changelog
8. Verifikasi jumlah entri Changelog Tab System bertambah dibanding baseline langkah 2 sebanyak Global Role yang belum di-assign `John Dohan` (9 dari 10 Global Role Principal)
9. Verifikasi Changelog memuat entri baru ber-Action `Assign (via Total Control)`, Object "[Role Name] — John Dohan", Field `Access`, Old Value "—", New Value `Assigned`, Modified By "Siti N"
10. Verifikasi tidak ada entri baru ber-Object "Manage device master data — John Dohan" di antara entri baru
11. Verifikasi tidak ada entri baru untuk Group Role di antara entri baru (jumlah entri baru sama dengan jumlah Global Role yang belum di-assign)
12. Tutup modal Changelog
13. Pulihkan baseline: `John Dohan` kembali Standard

### TC-AC-RP-334: Edit No-Op tidak menghasilkan entri log

14. Buka halaman `Settings > Role & Permission`
15. Klik tab `System`
16. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
17. Klik node `Sumatera`
18. Catat baseline jumlah entri Changelog Detail Role `Manage allocation`
19. Admin B (sesi API) mengirim toggle `Manage allocation` `Sumatera` ON hingga tersimpan
20. Klik toggle "Require Approval for Allocation" sehingga ON (tampilan belum diperbarui, masih OFF)
21. Verifikasi toast netral "No changes to save."
22. Klik ikon Changelog
23. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 1 dibanding baseline langkah 18
24. Verifikasi entri baru: Action `Edit` Off menjadi On untuk "Require Approval — Sumatera"
25. Tutup modal Changelog
26. Pulihkan baseline: toggle `Manage allocation` `Sumatera` kembali OFF

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness g (absence log); aksi pemicu (Assign Total Control, perubahan oleh Admin B lewat sesi API, Delete Group) adalah pembentuk kondisi yang diasersi tidak tercatat (P-5 butir a), bukan objek uji.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 2, 12, 13, 14, 18, 25, 26.
- Spec absence (kelas g): TC-AC-RP-318 adalah TC yang terbelah antara presence dan absence; Verifikasi pencatatan (anchor positif) berada di spec ini dengan baseline jumlah entri sendiri, dan asersi absence mengikuti anchor yang terhubung ke pemicu yang sama (S-05, bagian 8b butir 2).
- Pelaku kedua (Admin B) lewat sesi API hanya memicu perubahan state (langkah 19); sesuai konvensi tidak memakai butir `P-2`. Pelaku pertama TC-AC-RP-334 diposisikan pada sesi API sehingga sesi UI Siti menjadi pengirim kedua (stale) yang hasilnya (toast netral) diasersi.
- TC-AC-RP-318: jumlah entri baru dikaitkan dengan jumlah Global Role yang belum di-assign `John Dohan` (10 Global Role Principal menurut Expected TC-AC-RP-319, dikurangi `Manage device master data` yang sudah di-assign). TC-AC-RP-421 ada di spec 132 dan TC-AC-RP-335 ada di spec 132.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-334 Expected memuat toast sukses "Success, permissions have been updated." dari pengirim pertama; karena pengirim pertama memakai sesi API (keputusan 2026-10-21/30), toast itu tidak teramati di UI dan tidak diasersi di spec ini.
  - TC-AC-RP-334 menamai pengirim kedua "Sesi B (tampilan lama)"; spec memakai satu sesi UI sebagai pengirim kedua dan Admin B lewat sesi API sebagai pengirim pertama.
  - Email Admin B (Pre-setup #24) tidak tertulis di Pre-setup TC; disediakan tim FE.
  - TC-AC-RP-318 Expected "setiap Global Role yang belum di-assign" tidak menyebut jumlah; jumlah 9 diturunkan dari TC-AC-RP-319 (10 Global Role).
