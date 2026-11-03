---
id: TC-AC-LCS-E2E-014-tooltip-label-field-recycle-approval-limits-dan-addon
title: "Tooltip Label Field Recycle Bin, Approval Settings, System Limits, Fokus Keyboard, dan Addon Satuan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-44
  - TC-AC-LCS-45
  - TC-AC-LCS-46
  - TC-AC-LCS-47
  - TC-AC-LCS-48
coverage:
  web: automated
---

# Tooltip Label Field Recycle Bin, Approval Settings, System Limits, Fokus Keyboard, dan Addon Satuan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); hover pada label field dan fokus keyboard.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-44: Tooltip label field tab Recycle Bin menampilkan teks sesuai spesifikasi

1. Klik tab Recycle Bin pada tab bar
2. Hover label "Permanently Delete Recycle Bin"
3. Verifikasi Tooltip pada label "Permanently Delete Recycle Bin": "Specifies the number of days before items in the client's Recycle Bin are permanently deleted. Changing this value will recalculate the deletion countdown for all current Recycle Bin items"

### TC-AC-LCS-45: Tooltip label field tab Approval Settings menampilkan teks sesuai spesifikasi

4. Klik tab Approval Settings pada tab bar
5. Hover label "Approval Timeout"
6. Verifikasi Tooltip pada label "Approval Timeout": "Number of days a pending approval request waits for a decision before it's automatically canceled. A warning notification is sent 24 hours before cancellation. Applies platform-wide to Device Allocation, License Allocation, Wallet Allocation, and Client Subscription (including Trial Activation). Changes apply retroactively to pending requests."

### TC-AC-LCS-46: Tooltip label field tab System Limits menampilkan teks sesuai spesifikasi

7. Klik tab System Limits pada tab bar
8. Hover label "Bulk Transaction Row Limit"
9. Verifikasi Tooltip pada label "Bulk Transaction Row Limit": "Maximum number of assets allowed in a single bulk transaction request (e.g. Request Transfer, Request Disposal). Checked when the request is submitted, based on the number of assets included in that request — not the number of rows selected earlier in an asset list. Does not apply to file import, which is limited by file size instead."
10. Hover label "Selection Limit"
11. Verifikasi Tooltip pada label "Selection Limit": "Maximum number of rows that can be selected at once — applies to checkbox-based bulk actions in a table (e.g. mark as damaged, delete, activate) and to multi-select fields (e.g. assets, users). Additional rows beyond the limit cannot be checked. Using 'Select All' when the total exceeds this limit selects only the first 1000 rows."
12. Hover label "Register Asset Bulk Limit"
13. Verifikasi Tooltip pada label "Register Asset Bulk Limit": "Maximum number of assets allowed in a single multi-asset bulk registration submission. Checked in real time as you add rows."
14. Hover label "Hierarchy Depth Limit"
15. Verifikasi Tooltip pada label "Hierarchy Depth Limit": "Maximum tree depth allowed for hierarchical structures (e.g. Group, Category), regardless of plan tier. Applies as a hard technical ceiling beneath the plan-based depth cap."
16. Hover label "Master Data Count Limit"
17. Verifikasi Tooltip pada label "Master Data Count Limit": "Maximum number of records allowed per master data catalog per entity (e.g. Asset Name, Brand, Model/Type, SKU), regardless of plan tier."
18. Hover label "Max Visible Columns"
19. Verifikasi Tooltip pada label "Max Visible Columns": "Maximum number of columns that can be shown at once in a table's Setup Column/Column Visibility panel, across all modules. Additional columns beyond the limit cannot be checked until another column is unchecked."

### TC-AC-LCS-47: Accessibility tooltip: label Free Plan Duration menampilkan tooltip saat menerima fokus keyboard

20. Klik tab Free Plan Settings pada tab bar
21. Tekan Tab hingga label Free Plan Duration menerima fokus
22. Verifikasi Tooltip "Number of days a Free subscription remains active before expiring. Applies to new Free subscriptions only." tampil saat label menerima fokus keyboard

### TC-AC-LCS-48: Addon satuan field Max Trial Duration tidak dapat diedit

23. Klik tab Trial Settings pada tab bar
24. Klik label satuan `day(s)` di sisi kanan Max Trial Duration
25. Ketik `abc` setelah klik
26. Verifikasi Label satuan `day(s)` tidak masuk mode edit
27. Verifikasi Label satuan `day(s)` tidak berubah
28. Verifikasi Nilai field Max Trial Duration tetap `30`
29. Verifikasi `[Save]` disabled

## Notes

- Langkah penghubung (S-03): klik tab pada tiap blok TC (TC memulai dari tab itu menurut Precondition). Tiap tooltip diasersi tepat setelah hover atau fokus label-nya (bagian 8b butir 5). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: Expected TC 46 butir b memuat catatan editorial "(token nilai batas diganti nilai tersimpan 1000)"; spec mengasersi teks tooltip dengan nilai `1000` (nilai default tersimpan) tanpa catatan itu. Bila nilai tersimpan berbeda, teks tooltip berubah mengikuti nilai tersebut dan TC perlu menyatakannya sebagai Expected, bukan catatan.
- Temuan untuk QA: TC 48 tidak menyebut apa yang terjadi pada teks `abc` yang diketik setelah klik label satuan (tidak ada field fokus); spec hanya mengasersi butir Expected TC.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
