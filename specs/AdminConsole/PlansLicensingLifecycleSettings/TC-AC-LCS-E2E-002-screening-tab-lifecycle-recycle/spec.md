---
id: TC-AC-LCS-E2E-002-screening-tab-lifecycle-recycle
title: "Screening Tab Client Lifecycle dan Recycle Bin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-4
  - TC-AC-LCS-5
coverage:
  web: automated
---

# Screening Tab Client Lifecycle dan Recycle Bin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-4: Screening tab Client Lifecycle: Breadcrumb, tab bar, field, addon, dan footer

1. Klik tab Client Lifecycle pada tab bar
2. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
3. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > Client Lifecycle"
4. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
5. Verifikasi Header: tab `Trial Settings | Free Plan Settings | License Timing | Client Lifecycle (aktif) | Recycle Bin | Approval Settings | System Limits`
6. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
7. Verifikasi Body: Card Plan Owner Notification > Notify Plan Owner Before Event nilai `45`, addon `day(s)`
8. Verifikasi Body: Card Pre-Event Reminders > First Reminder Before Event nilai `30`, addon `day(s)`
9. Verifikasi Body: Card Pre-Event Reminders > Second Reminder Before Event nilai `7`, addon `day(s)`
10. Verifikasi Body: Card Pre-Event Reminders > Final Reminder Before Event nilai `1`, addon `day(s)`
11. Verifikasi Body: Card Post-Event Periods > Grace Period Duration nilai `30`, addon `day(s)`
12. Verifikasi Body: Card Post-Event Periods > Archive Period Duration nilai `30`, addon `day(s)`
13. Verifikasi Body: Card Purge Warnings > Purge Warning Email nilai `10`, addon `day(s) before`
14. Verifikasi Body: Card Purge Warnings > Purge Urgent Warning Email nilai `2`, addon `day(s) before`
15. Verifikasi Body: Card Post-Purge Archive > Post-Purge Retention nilai `730`, addon `day(s)`
16. Verifikasi Body: warning note kondisional tidak tampil (form clean)
17. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
18. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

### TC-AC-LCS-5: Screening tab Recycle Bin: Breadcrumb, tab bar, field, addon, dan footer

19. Klik tab Recycle Bin pada tab bar
20. Susuri halaman dari atas ke bawah tanpa mengklik elemen lain
21. Verifikasi Header: Breadcrumb "Plans & Licensing > Lifecycle Settings > Recycle Bin"
22. Verifikasi Header: segmen pertama dan segmen terakhir Breadcrumb bukan link
23. Verifikasi Header: tab `Trial Settings | Free Plan Settings | License Timing | Client Lifecycle | Recycle Bin (aktif) | Approval Settings | System Limits`
24. Verifikasi Header: icon Changelog di pojok kanan atas panel tab
25. Verifikasi Body: Permanently Delete Recycle Bin nilai `30`, addon `day(s)`
26. Verifikasi Body: warning note kondisional tidak tampil (form clean)
27. Verifikasi Footer: `[Reset to Default]` (Text, primary) tampil enabled
28. Verifikasi Footer: `[Save]` (filled, success) tampil disabled, kedua tombol rata kanan dengan urutan `[Reset to Default]` lalu `[Save]`

## Notes

- Langkah penghubung (S-03): klik tab pada tiap blok TC adalah langkah sumber TC; blok TC 5 dimulai dari tab Client Lifecycle yang masih aktif tanpa perubahan data. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Absence warning note kondisional ditulis sesudah `Verifikasi` seluruh field pada tab yang sama (anchor positif, bagian 8b butir 2).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
