---
id: TC-AC-LCS-E2E-013-tooltip-label-field-trial-free-license
title: "Tooltip Label Field: Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-40
  - TC-AC-LCS-41
  - TC-AC-LCS-42
coverage:
  web: automated
---

# Tooltip Label Field: Tab Trial Settings, Free Plan Settings, dan License Timing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); hover pada label field.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-40: Tooltip label field tab Trial Settings menampilkan teks sesuai spesifikasi

1. Hover label "Max Trial Duration"
2. Verifikasi Tooltip pada label "Max Trial Duration": "Maximum number of days a Principal, Distributor, or Partner can grant for a trial subscription. Enforced when activating a trial — see Client Subscription > Activate Trial."
3. Hover label "Max Trial Asset Quota"
4. Verifikasi Tooltip pada label "Max Trial Asset Quota": "Maximum asset quota a Principal, Distributor, or Partner can grant for a FAMS/SAMS trial. Enforced when activating a trial."
5. Hover label "Max Trial Concurrent User Quota"
6. Verifikasi Tooltip pada label "Max Trial Concurrent User Quota": "Maximum concurrent user quota a Principal, Distributor, or Partner can grant for a trial, any product. Enforced when activating a trial."
7. Hover label "Require Approval for Trial Activation"
8. Verifikasi Tooltip pada label "Require Approval for Trial Activation": "When enabled, trials activated by Distributor or Partner users go to Waiting for Approval before the trial subscription is created — reviewed by Principal's Total Control or Additional Approver (Manage allocation). Trials activated by Principal users are unaffected — Principal is the reviewing authority."
9. Hover label "First Notification"
10. Verifikasi Tooltip pada label "First Notification": "Days before trial expiry to send the first reminder notification to the client."
11. Hover label "Second Notification"
12. Verifikasi Tooltip pada label "Second Notification": "Days before trial expiry to send the final reminder notification to the client."

### TC-AC-LCS-41: Tooltip label field tab Free Plan Settings menampilkan teks sesuai spesifikasi

13. Klik tab Free Plan Settings pada tab bar
14. Hover label "Free Plan Duration"
15. Verifikasi Tooltip pada label "Free Plan Duration": "Number of days a Free subscription remains active before expiring. Applies to new Free subscriptions only."

### TC-AC-LCS-42: Tooltip label field tab License Timing menampilkan teks sesuai spesifikasi

16. Klik tab License Timing pada tab bar
17. Hover label "Managed Transition Time"
18. Verifikasi Tooltip pada label "Managed Transition Time": "Specifies the time interval required to transition an asset from an unmanaged state to a managed state"
19. Hover label "Managed Action Retry Delay"
20. Verifikasi Tooltip pada label "Managed Action Retry Delay": "Specifies the time interval to wait before retrying the 'Managed' action"
21. Hover label "Addon Reactivation Delay"
22. Verifikasi Tooltip pada label "Addon Reactivation Delay": "Specifies the time delay before the addon can be selected again after it has been unchecked. This ensures a waiting period before re-enabling the addon"

## Notes

- Langkah penghubung (S-03): klik tab pada blok TC 41 dan TC 42 (TC memulai dari tab itu menurut Precondition). Tiap tooltip diasersi tepat setelah hover label-nya dan sebelum hover berikutnya (bagian 8b butir 5). Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Langkah hover diulang per label (Untuk setiap label pada tab); satu `Verifikasi` per tooltip (S-01).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
