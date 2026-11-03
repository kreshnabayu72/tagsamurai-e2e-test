---
id: TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred
title: "Notifikasi In-App [DEFERRED]: Remove Total Control, Read Only, Group Manager, Assign GM Dua Group"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-337
  - TC-AC-RP-338
  - TC-AC-RP-339
  - TC-AC-RP-417
coverage:
  web: unsupported
---

# Notifikasi In-App [DEFERRED]: Remove Total Control, Read Only, Group Manager, Assign GM Dua Group

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec ke akun target notifikasi: `John Doe` (TC-AC-RP-337), `Lisa Wong` (TC-AC-RP-338), dan `Fajar Nugroho` (TC-AC-RP-339 dan 417) untuk membuka notifikasi masing-masing; email dan password akun target ini tidak tertulis di Pre-setup #1 sampai #10 dan disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA). Setelah tiap blok sesi dikembalikan ke `Siti Nurhaliza`.
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #13 (pemegang Total Control `John Doe` dan Read Only `Lisa Wong`), dan #14 (penugasan Group Manager: `Fajar Nugroho` di `Region Jawa` dan `Sumatera`). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini. Pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia (`[DEFERRED]`, kontrak event normatif PRD §8.8); spec dijalankan setelah modul Notification tersedia.
- Kemampuan teknis: format tanggal General Settings entitas uji (contoh `15 Jun 2026, 10:05`) dipakai untuk [Date] pada Body notifikasi; waktu aksi dicatat sesaat setelah tombol konfirmasi dan dibandingkan dengan toleransi satu menit (S-12). Jam server dan jam browser sinkron.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-337: [DEFERRED] Notifikasi Remove Total Control ke target

1. Klik `⋯` baris `John Doe` lalu klik `Remove`
2. Klik `[Remove]`
3. Catat waktu aksi sesaat setelah klik `[Remove]`
4. Ganti akun: Logout, lalu login sebagai `John Doe`
5. Buka notifikasi
6. Verifikasi notifikasi in-app `view-only` dengan Title "Your Total Control access was removed" dan Body "Siti Nurhaliza removed your Total Control access on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
7. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
8. Pulihkan baseline: `John Doe` kembali Total Control

### TC-AC-RP-338: [DEFERRED] Notifikasi Remove Read Only ke target

9. Buka halaman `Settings > Role & Permission`, lalu klik tab `Read Only`
10. Klik `⋯` baris `Lisa Wong` lalu klik `Remove`
11. Klik `[Remove]`
12. Catat waktu aksi sesaat setelah klik `[Remove]`
13. Ganti akun: Logout, lalu login sebagai `Lisa Wong`
14. Buka notifikasi
15. Verifikasi notifikasi in-app `view-only` dengan Title "Your Read Only access was removed" dan Body "Siti Nurhaliza removed your Read Only access on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
16. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
17. Pulihkan baseline: `Lisa Wong` kembali Read Only

### TC-AC-RP-339: [DEFERRED] Notifikasi Remove Group Manager ke target

18. Buka halaman `Settings > Role & Permission`
19. Klik tab `Group Manager`
20. Klik `⋯` baris `Fajar Nugroho` — `Sumatera` lalu klik `Remove`
21. Klik `[Remove]`
22. Catat waktu aksi sesaat setelah klik `[Remove]`
23. Ganti akun: Logout, lalu login sebagai `Fajar Nugroho`
24. Buka notifikasi
25. Verifikasi notifikasi in-app `view-only` dengan Title "You are no longer Group Manager for Sumatera" dan Body "Siti Nurhaliza removed your Group Manager status for Sumatera on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
26. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
27. Pulihkan baseline: `Fajar Nugroho` kembali GM `Sumatera`

### TC-AC-RP-417: [DEFERRED] Assign Read Only ke Group Manager di dua group mengirim satu notifikasi per group

28. Buka halaman `Settings > Role & Permission`
29. Klik tab `Read Only`
30. Klik tombol "+ Assign"
31. Centang `Fajar Nugroho` lalu klik `[Assign]`
32. Catat waktu aksi sesaat setelah klik `[Assign]`
33. Ganti akun: Logout, lalu login sebagai `Fajar Nugroho`
34. Buka notifikasi
35. Verifikasi tepat dua notifikasi in-app `view-only`, satu per group yang dilepas, dengan template yang sama
36. Verifikasi notifikasi pertama: Title "You are no longer Group Manager for Region Jawa" dan Body "Siti Nurhaliza removed your Group Manager status for Region Jawa on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
37. Verifikasi notifikasi kedua: Title "You are no longer Group Manager for Sumatera" dan Body "Siti Nurhaliza removed your Group Manager status for Sumatera on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
38. Verifikasi tidak ada notifikasi gabungan satu untuk dua group
39. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
40. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan `Sumatera`, `Fajar Nugroho` bukan Read Only

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness d (harness eksternal: notifikasi in-app dari modul Admin Console > Notification) dan `[DEFERRED]`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 3, 7, 8, 12, 16, 17, 18, 22, 26, 27, 28, 32, 39, 40; langkah 9 memuat pembukaan halaman `Settings > Role & Permission` sebagai penghubung sesudah ganti akun.
- `[DEFERRED]`: pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia; spec ditandai `coverage.web: unsupported` karena modul Notification belum ada dan pengiriman notifikasi tidak dapat diverifikasi; spec diaktifkan lagi (`coverage.web: automated`) saat modul Notification selesai.
- Ganti akun eksplisit pada langkah 4, 13, 23, dan 33 (S-07); pengembalian sesi ke `Siti Nurhaliza` adalah langkah penghubung.
- Asersi "tidak ada notifikasi gabungan" (TC-AC-RP-417) didahului Verifikasi dua notifikasi per group sebagai anchor positif (bagian 8b butir 2 dan 11).
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (40 langkah): semua blok adalah kelas d (notifikasi in-app) yang berdiri sendiri; tiap blok punya aksi, akun target, dan pemulihan sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - Email dan password akun `John Doe`, `Lisa Wong`, dan `Fajar Nugroho` sebagai penerima notifikasi tidak tertulis di Pre-setup #1 sampai #10 (hanya nama tampil di #13 dan #14); disediakan tim FE.
  - TC-AC-RP-337 sampai 339 dan 417 menyebut [Date] "format General Settings" tanpa nilai; spec membandingkan dengan waktu aksi dicatat dengan toleransi satu menit.
  - TC-AC-RP-417 Expected menyebut "tepat dua notifikasi" tanpa baseline jumlah notifikasi; `Fajar Nugroho` diasumsikan tanpa notifikasi lain dari kondisi ini.
  - `[DEFERRED]`: `coverage.web: unsupported` sampai modul Notification tersedia; kolom Automation TC menyatakan `Automatable`, sehingga spec diaktifkan lagi saat modul Notification selesai.
