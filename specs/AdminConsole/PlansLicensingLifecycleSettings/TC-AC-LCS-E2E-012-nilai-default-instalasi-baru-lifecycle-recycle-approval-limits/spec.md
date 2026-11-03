---
id: TC-AC-LCS-E2E-012-nilai-default-instalasi-baru-lifecycle-recycle-approval-limits
title: "Nilai Default Instalasi Baru: Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-36
  - TC-AC-LCS-37
  - TC-AC-LCS-38
  - TC-AC-LCS-39
coverage:
  web: automated
---

# Nilai Default Instalasi Baru: Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Data: platform baru (FRESH): tab yang diuji belum pernah disimpan, diatur lewat Fixture BE pada hook `before` spec ini (menggantikan pemulihan ke default untuk tab tersebut); hook `after` mengembalikan keadaan tab ke default tersimpan.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); Fixture BE untuk membuat keadaan tab belum pernah disimpan.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-36: Tab Client Lifecycle pada instalasi baru menampilkan nilai default

1. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
2. Klik tab Client Lifecycle pada tab bar
3. Amati nilai seluruh field pada tab
4. Verifikasi Field Notify Plan Owner Before Event berisi `45`
5. Verifikasi Field First Reminder Before Event berisi `30`
6. Verifikasi Field Second Reminder Before Event berisi `7`
7. Verifikasi Field Final Reminder Before Event berisi `1`
8. Verifikasi Field Grace Period Duration berisi `30`
9. Verifikasi Field Archive Period Duration berisi `30`
10. Verifikasi Field Purge Warning Email berisi `10`
11. Verifikasi Field Purge Urgent Warning Email berisi `2`
12. Verifikasi Field Post-Purge Retention berisi `730`
13. Verifikasi Tidak ada pesan error dan tidak ada empty state field
14. Verifikasi `[Save]` disabled

### TC-AC-LCS-37: Tab Recycle Bin pada instalasi baru menampilkan nilai default

15. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
16. Klik tab Recycle Bin pada tab bar
17. Amati nilai seluruh field pada tab
18. Verifikasi Field Permanently Delete Recycle Bin berisi `30`
19. Verifikasi Tidak ada pesan error dan tidak ada empty state field
20. Verifikasi `[Save]` disabled

### TC-AC-LCS-38: Tab Approval Settings pada instalasi baru menampilkan nilai default

21. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
22. Klik tab Approval Settings pada tab bar
23. Amati nilai seluruh field pada tab
24. Verifikasi Field Approval Timeout berisi `3`
25. Verifikasi Tidak ada pesan error dan tidak ada empty state field
26. Verifikasi `[Save]` disabled

### TC-AC-LCS-39: Tab System Limits pada instalasi baru menampilkan nilai default

27. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
28. Klik tab System Limits pada tab bar
29. Amati nilai seluruh field pada tab
30. Verifikasi Field Bulk Transaction Row Limit berisi `1000`
31. Verifikasi Field Selection Limit berisi `1000`
32. Verifikasi Field Register Asset Bulk Limit berisi `1000`
33. Verifikasi Field Hierarchy Depth Limit berisi `50`
34. Verifikasi Field Master Data Count Limit berisi `10000`
35. Verifikasi Field Max Visible Columns berisi `20`
36. Verifikasi Tidak ada pesan error dan tidak ada empty state field
37. Verifikasi `[Save]` disabled

## Notes

- Langkah penghubung (S-03): TC 36 sampai 39 menulis "klik menu ..., lalu klik tab ..." sebagai dua langkah. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Absence "tidak ada pesan error dan tidak ada empty state field" ditulis sesudah `Verifikasi` seluruh nilai field (anchor positif, bagian 8b butir 2).
- Temuan untuk QA: cara membuat keadaan "tab belum pernah disimpan" tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan Fixture BE yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
- Alasan di atas sekitar 35 langkah: seluruh blok memuat TC fungsional kelas yang sama (nilai default instalasi baru), tiap blok memeriksa satu tab dengan keadaan awal (belum pernah disimpan) sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
