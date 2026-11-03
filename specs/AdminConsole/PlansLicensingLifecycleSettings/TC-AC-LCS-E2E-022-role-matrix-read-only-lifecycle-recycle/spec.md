---
id: TC-AC-LCS-E2E-022-role-matrix-read-only-lifecycle-recycle
title: "Role Matrix: Read Only pada Tab Client Lifecycle dan Recycle Bin"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-73
  - TC-AC-LCS-74
coverage:
  web: automated
---

# Role Matrix: Read Only pada Tab Client Lifecycle dan Recycle Bin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`), password dari `Spectra.env.AC_RO_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Read Only | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-73: Read Only pada tab Client Lifecycle: field Disabled, Save dan Reset to Default Hidden, ikon Changelog tampil

1. Klik tab Client Lifecycle pada tab bar
2. Hover field Notify Plan Owner Before Event
3. Verifikasi Field Notify Plan Owner Before Event tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
4. Hover field First Reminder Before Event
5. Verifikasi Field First Reminder Before Event tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
6. Hover field Second Reminder Before Event
7. Verifikasi Field Second Reminder Before Event tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
8. Hover field Final Reminder Before Event
9. Verifikasi Field Final Reminder Before Event tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
10. Hover field Grace Period Duration
11. Verifikasi Field Grace Period Duration tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
12. Hover field Archive Period Duration
13. Verifikasi Field Archive Period Duration tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
14. Hover field Purge Warning Email
15. Verifikasi Field Purge Warning Email tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
16. Hover field Purge Urgent Warning Email
17. Verifikasi Field Purge Urgent Warning Email tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
18. Hover field Post-Purge Retention
19. Verifikasi Field Post-Purge Retention tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
20. Verifikasi `[Save]` dan `[Reset to Default]` Hidden (tidak dirender)
21. Klik icon Changelog di pojok kanan atas panel
22. Verifikasi Modal "Changelog: Lifecycle Settings > Client Lifecycle" terbuka
23. Verifikasi Toolbar modal Changelog: Search, Filter, Download tampil
24. Tutup modal Changelog lewat `✕` di header

### TC-AC-LCS-74: Read Only pada tab Recycle Bin: field Disabled, Save dan Reset to Default Hidden, ikon Changelog tampil

25. Klik tab Recycle Bin pada tab bar
26. Hover field Permanently Delete Recycle Bin
27. Verifikasi Field Permanently Delete Recycle Bin tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
28. Verifikasi `[Save]` dan `[Reset to Default]` Hidden (tidak dirender)
29. Klik icon Changelog di pojok kanan atas panel
30. Verifikasi Modal "Changelog: Lifecycle Settings > Recycle Bin" terbuka
31. Verifikasi Toolbar modal Changelog: Search, Filter, Download tampil
32. Tutup modal Changelog lewat `✕` di header

## Notes

- Spec Role Matrix dengan satu role (Read Only); akun login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default suite. Langkah penghubung (S-03, S-09): klik tab dan menutup modal Changelog lewat `✕` di header (modal tidak punya `[Cancel]`; bagian 9).
- "Field tampil (visible) namun berstatus Disabled; hover menampilkan tooltip" ditulis satu `Verifikasi` per field sebagai komposit "Disabled dengan tooltip" (S-01, KEPUTUSAN 2026-10-30); `[Save]` dan `[Reset to Default]` Hidden ditulis satu `Verifikasi` karena daftar elemen yang sama-sama tidak ada disebut utuh; toolbar Search, Filter, Download satu `Verifikasi` karena daftar ikon disebut utuh (KEPUTUSAN 2026-10-29).
- Absence `[Save]` dan `[Reset to Default]` didahului `Verifikasi` field pada halaman yang sama (anchor permukaan, bagian 8b butir 2).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
