---
id: TC-AC-RP-E2E-103-notifikasi-in-app-auto-revert-deferred
title: "Notifikasi In-App [DEFERRED]: Auto-Revert Total Control, Read Only, dan Group Manager"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-340
  - TC-AC-RP-341
  - TC-AC-RP-342
coverage:
  web: unsupported
---

# Notifikasi In-App [DEFERRED]: Auto-Revert Total Control, Read Only, dan Group Manager

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Ganti akun di tengah spec ke akun target notifikasi: `Rina Wijaya` (TC-AC-RP-340), `Dewi Anggraini` (TC-AC-RP-341, `readOnlyRP_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_RP_RO_PASSWORD`), dan `Fajar Nugroho` (TC-AC-RP-342). Email dan password `Rina Wijaya` dan `Fajar Nugroho` tidak tertulis di Pre-setup #1 sampai #10 dan disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA). Setelah tiap blok sesi dikembalikan ke `Siti Nurhaliza`.
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #13 (pemegang Total Control `Rina Wijaya` dan Read Only `Dewi Anggraini`), #14 (penugasan Group Manager: `Fajar Nugroho` di `Region Jawa`), dan #15 (penugasan peran individual). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini. Pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia (`[DEFERRED]`, kontrak event normatif PRD §8.8).
- Kemampuan teknis: format tanggal General Settings entitas uji dipakai untuk [Date] pada Body notifikasi; waktu aksi dicatat sesaat setelah tombol konfirmasi dan dibandingkan dengan toleransi satu menit (S-12). Jam server dan jam browser sinkron.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD`, `AC_RP_RO_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-340: [DEFERRED] Notifikasi Auto-Revert Total Control ke target

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
3. Hapus centang D baris `Rina Wijaya`
4. Klik `[Remove]` pada dialog auto-revert
5. Catat waktu aksi sesaat setelah klik `[Remove]`
6. Ganti akun: Logout, lalu login sebagai `Rina Wijaya`
7. Buka notifikasi
8. Verifikasi notifikasi in-app `view-only` dengan Title "Your Total Control access was removed" dan Body "Your Total Control access was automatically removed after Siti Nurhaliza edited your role on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
9. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
10. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan D `Manage preload` tercentang

### TC-AC-RP-341: [DEFERRED] Notifikasi Auto-Revert Read Only ke target

11. Buka halaman `Settings > Role & Permission`
12. Klik tab `System`
13. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
14. Centang C baris `Dewi Anggraini`
15. Klik `[Remove]` pada dialog auto-revert
16. Catat waktu aksi sesaat setelah klik `[Remove]`
17. Ganti akun: Logout, lalu login sebagai `Dewi Anggraini` (`readOnlyRP_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_RP_RO_PASSWORD`)
18. Buka notifikasi
19. Verifikasi notifikasi in-app `view-only` dengan Title "Your Read Only access was removed" dan Body "Your Read Only access was automatically removed after Siti Nurhaliza edited your role on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
20. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
21. Pulihkan baseline: `Dewi Anggraini` kembali Read Only dan C `Manage preload` tidak tercentang

### TC-AC-RP-342: [DEFERRED] Notifikasi Auto-Revert Group Manager ke target

22. Buka halaman `Settings > Role & Permission`
23. Klik tab `System`
24. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
25. Hapus centang U baris `Fajar Nugroho` pada node `Region Jawa`
26. Klik `[Remove]` pada dialog auto-revert
27. Catat waktu aksi sesaat setelah klik `[Remove]`
28. Ganti akun: Logout, lalu login sebagai `Fajar Nugroho`
29. Buka notifikasi
30. Verifikasi notifikasi in-app `view-only` dengan Title "You are no longer Group Manager for Region Jawa" dan Body "Your Group Manager status for Region Jawa was automatically removed after Siti Nurhaliza edited your role on [Date]." ([Date] sesuai waktu aksi dengan format General Settings)
31. Ganti akun: Logout, lalu login sebagai `Siti Nurhaliza`
32. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan U `Manage partner` `Region Jawa` tercentang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness d (harness eksternal: notifikasi in-app dari modul Admin Console > Notification) dan `[DEFERRED]`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 5, 9, 10, 11, 16, 20, 21, 22, 27, 31, 32.
- `[DEFERRED]`: pengiriman notifikasi berstatus future implementation sampai modul Admin Console > Notification tersedia; spec ditandai `coverage.web: unsupported` karena modul Notification belum ada dan pengiriman notifikasi tidak dapat diverifikasi; spec diaktifkan lagi (`coverage.web: automated`) saat modul Notification selesai.
- Ganti akun eksplisit pada langkah 6, 17, dan 28 (S-07); pengembalian sesi ke `Siti Nurhaliza` adalah langkah penghubung.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-341 langkah 4 "Auto-revert `Dewi Anggraini`" tidak menyebut cara memicu; spec memakai edit CRUD (centang C baris `Dewi Anggraini` lalu `[Remove]`) mengikuti spec Auto-Revert Read Only.
  - TC-AC-RP-340 sampai 342 menyebut [Date] "format General Settings" tanpa nilai; spec membandingkan dengan waktu aksi dicatat dengan toleransi satu menit.
  - Email dan password `Rina Wijaya` dan `Fajar Nugroho` sebagai penerima notifikasi tidak tertulis di Pre-setup #1 sampai #10; disediakan tim FE.
  - `[DEFERRED]`: `coverage.web: unsupported` sampai modul Notification tersedia; kolom Automation TC menyatakan `Automatable`, sehingga spec diaktifkan lagi saat modul Notification selesai.
