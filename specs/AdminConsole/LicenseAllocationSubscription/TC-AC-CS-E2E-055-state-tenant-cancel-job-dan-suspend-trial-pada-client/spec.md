---
id: TC-AC-CS-E2E-055-state-tenant-cancel-job-dan-suspend-trial-pada-client
title: "State Tenant: Cancel, Job, dan Suspend Trial pada Client Suspended atau Expired"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-549
  - TC-AC-CS-268
  - TC-AC-CS-531
coverage:
  web: automated
---

# State Tenant: Cancel, Job, dan Suspend Trial pada Client Suspended atau Expired

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan langsung PT Maju Bersama; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A sampai D): Client `PT Sejahtera+{runId}-055` dengan trial Active (Subscription ID seed A; Start Date `10/08/26`, End Date `08/09/26`; padanan Pre-setup #60); Client `Toko Rejeki Suspended+{runId}-055` (status Suspended) dengan term paid (Subscription ID seed B; padanan Pre-setup #45, #117), pengajuan Waiting for Approval (Subscription ID seed C; padanan #118), dan term Pending SIEM Start Date `15/09/26` (Subscription ID seed D). Tanggal acuan uji `19/08/26`.
- Data Dinamis: tidak ada data baru. Perubahan status Client seed dan term seed yang di-Cancel dipulihkan oleh fixture backend pemulihan state (disediakan tim FE/BE) di hook `before`, `after`, dan sebagai langkah penghubung, lalu seed dihapus di hook `after`. Pre-setup #45, #60, #117, #118 tidak disentuh.
- Kemampuan teknis (disediakan tim FE/BE): mengatur status Client (Active, Suspended) lewat fixture backend; fixture waktu untuk jam server dan jam browser (nilai absolut, diatur ke tanggal acuan `19/08/26` di hook `before`, dipulihkan di hook `after`); memicu atau mem-poll job sistem (auto-expire Trial, Timeout Auto-Cancel, scheduled flip) dengan idiom polling muat ulang tiap 5 detik batas 2 menit; fixture backend pemulihan state Client.

## Test Steps

### TC-AC-CS-549: Suspend Client di tengah trial tidak mem-pause trial dan trial Expired tanpa fallback plan

1. Ketik Search `PT Sejahtera+{runId}-055`, tekan Enter, lalu catat jumlah baris Client `PT Sejahtera+{runId}-055` di tab Current sebagai baseline
2. Ubah status Client `PT Sejahtera+{runId}-055` menjadi Suspended pada tanggal acuan `19/08/26` lewat fixture backend
3. Buka Detail trial `Subscription ID seed A`
4. Verifikasi trial tetap berstatus Active
5. Verifikasi End Date trial `08/09/26` tidak berubah (timer tidak di-pause)
6. Geser jam server melewati End Date ke `09/09/26` lewat fixture waktu, tunggu satu siklus job lifecycle, lalu pulihkan jam server dan jam browser ke `19/08/26`
7. Buka List tab Current dan ketik Search `PT Sejahtera+{runId}-055`, tekan Enter
8. Verifikasi baris trial `Subscription ID seed A` berstatus Expired
9. Buka Detail trial
10. Verifikasi status trial tetap Expired dan tidak kembali Active
11. Verifikasi jumlah baris Client `PT Sejahtera+{runId}-055` sama dengan baseline (tidak ada term paid baru, plan tier lebih rendah, atau plan pengganti)

### TC-AC-CS-268: Cancel Subscription tetap diizinkan pada Client Suspended

12. Pulihkan Client `PT Sejahtera+{runId}-055` ke status Active lewat fixture backend, ketik Search `Toko Rejeki Suspended+{runId}-055`, tekan Enter
13. Klik ikon `⋯` pada baris `Subscription ID seed B` lalu pilih `Cancel Subscription`
14. Klik `[Cancel Subscription]`
15. Verifikasi toast sukses "Success, subscription has been canceled."
16. Klik tab `History`
17. Verifikasi term `Subscription ID seed B` berstatus Archive walau Client Suspended

### TC-AC-CS-531: Job Timeout Auto-Cancel dan scheduled flip tetap berjalan pada Client Suspended

18. Klik tab `Current`, pulihkan term `Subscription ID seed B` dan Client `Toko Rejeki Suspended+{runId}-055` ke keadaan awal lewat fixture backend
19. Geser jam server dan jam browser ke `15/09/26` (melewati SLA dan Start Date) lewat fixture waktu, tunggu satu siklus job, lalu pulihkan jam ke `19/08/26`
20. Ketik Search `Toko Rejeki Suspended+{runId}-055`, tekan Enter, lalu klik tab `History`
21. Verifikasi pengajuan Waiting for Approval `Subscription ID seed C` berstatus Canceled oleh sistem
22. Klik tab `Current`
23. Verifikasi term Pending `Subscription ID seed D` berstatus Active oleh scheduled flip

## Notes

- Pemicu job sistem (auto-expire Trial pada TC-AC-CS-549, Timeout Auto-Cancel dan scheduled flip pada TC-AC-CS-531) hanya memicu kondisi yang diuji pada kelas h; tidak ada konteks kedua (P-2, KEPUTUSAN 2026-10-21). Tidak ada TC kelas d lain di spec ini.
- TC-AC-CS-532 dan TC-AC-CS-533 (trial Expired pada dropdown, Convert, dan Activate Trial) ada di spec 150.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); pemulihan status Client, trial, dan jam; `✕` dengan `[Leave]` menutup form dirty (S-08).
- Temuan untuk QA: (1) TC-AC-CS-549 tidak menyebut cara pengamatan "tidak ada plan pengganti"; spec memakai jumlah baris Client sebagai baseline. (2) TC-AC-CS-531 tidak menyebut layar pengamatan "Canceled oleh sistem"; spec mengamati status Canceled di tab History.
