---
id: TC-AC-LCS-E2E-021-role-matrix-read-only-trial-free-license
title: "Role Matrix: Read Only pada Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-70
  - TC-AC-LCS-71
  - TC-AC-LCS-72
coverage:
  web: automated
---

# Role Matrix: Read Only pada Tab Trial Settings, Free Plan Settings, dan License Timing

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

### TC-AC-LCS-70: Read Only pada tab Trial Settings: field Disabled, Save dan Reset to Default Hidden, ikon Changelog tampil

1. Hover field Max Trial Duration
2. Verifikasi Field Max Trial Duration tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
3. Hover field Max Trial Asset Quota
4. Verifikasi Field Max Trial Asset Quota tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
5. Hover field Max Trial Concurrent User Quota
6. Verifikasi Field Max Trial Concurrent User Quota tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
7. Hover field First Notification
8. Verifikasi Field First Notification tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
9. Hover field Second Notification
10. Verifikasi Field Second Notification tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
11. Hover field Require Approval for Trial Activation (Switch)
12. Verifikasi Field Require Approval for Trial Activation (Switch) tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
13. Verifikasi `[Save]` dan `[Reset to Default]` Hidden (tidak dirender)
14. Klik icon Changelog di pojok kanan atas panel
15. Verifikasi Modal "Changelog: Lifecycle Settings > Trial Settings" terbuka
16. Verifikasi Toolbar modal Changelog: Search, Filter, Download tampil
17. Tutup modal Changelog lewat `✕` di header

### TC-AC-LCS-71: Read Only pada tab Free Plan Settings: field Disabled, Save dan Reset to Default Hidden, ikon Changelog tampil

18. Klik tab Free Plan Settings pada tab bar
19. Hover field Free Plan Duration
20. Verifikasi Field Free Plan Duration tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
21. Verifikasi `[Save]` dan `[Reset to Default]` Hidden (tidak dirender)
22. Klik icon Changelog di pojok kanan atas panel
23. Verifikasi Modal "Changelog: Lifecycle Settings > Free Plan Settings" terbuka
24. Verifikasi Toolbar modal Changelog: Search, Filter, Download tampil
25. Tutup modal Changelog lewat `✕` di header

### TC-AC-LCS-72: Read Only pada tab License Timing: field Disabled, Save dan Reset to Default Hidden, ikon Changelog tampil

26. Klik tab License Timing pada tab bar
27. Hover field Managed Transition Time
28. Verifikasi Field Managed Transition Time tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
29. Hover field Managed Action Retry Delay
30. Verifikasi Field Managed Action Retry Delay tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
31. Hover field Addon Reactivation Delay
32. Verifikasi Field Addon Reactivation Delay tampil (visible) namun berstatus Disabled dengan tooltip "Read Only access cannot modify data."
33. Verifikasi `[Save]` dan `[Reset to Default]` Hidden (tidak dirender)
34. Klik icon Changelog di pojok kanan atas panel
35. Verifikasi Modal "Changelog: Lifecycle Settings > License Timing" terbuka
36. Verifikasi Toolbar modal Changelog: Search, Filter, Download tampil
37. Tutup modal Changelog lewat `✕` di header

## Notes

- Spec Role Matrix dengan satu role (Read Only); akun login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default suite. Langkah penghubung (S-03, S-09): klik tab dan menutup modal Changelog lewat `✕` di header (modal tidak punya `[Cancel]`; bagian 9).
- "Field tampil (visible) namun berstatus Disabled; hover menampilkan tooltip" ditulis satu `Verifikasi` per field sebagai komposit "Disabled dengan tooltip" (S-01, KEPUTUSAN 2026-10-30); `[Save]` dan `[Reset to Default]` Hidden ditulis satu `Verifikasi` karena daftar elemen yang sama-sama tidak ada disebut utuh; toolbar Search, Filter, Download satu `Verifikasi` karena daftar ikon disebut utuh (KEPUTUSAN 2026-10-29).
- Absence `[Save]` dan `[Reset to Default]` didahului `Verifikasi` field pada halaman yang sama (anchor permukaan, bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah: seluruh blok memuat TC Role Matrix Read Only yang sama, tiap blok memeriksa satu tab dengan akun dan keadaan awal yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
