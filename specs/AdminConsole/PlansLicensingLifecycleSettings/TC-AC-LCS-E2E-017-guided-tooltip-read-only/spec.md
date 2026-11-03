---
id: TC-AC-LCS-E2E-017-guided-tooltip-read-only
title: "Guided Tooltip: Walkthrough Read Only Melewati Step Reset to Default dan Save"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-57
coverage:
  web: automated
---

# Guided Tooltip: Walkthrough Read Only Melewati Step Reset to Default dan Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`), password dari `Spectra.env.AC_RO_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Read Only | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini untuk akun Read Only belum ada (hook `before` suite hanya menyetel flag akun aktor default); hook `before` spec ini memastikan flag itu belum ada lewat kemampuan yang disediakan tim FE/BE (pengecualian suite) dan hook `after` suite memulihkannya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); pengaturan dan penghapusan flag Guided Tooltip akun Read Only (disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-57: Walkthrough bagi Read Only melewati step yang menargetkan Reset to Default dan Save

1. Klik menu Plans & Features di sidebar untuk meninggalkan halaman
2. Klik menu Plans & Licensing > Lifecycle Settings di sidebar
3. Verifikasi Step 1 of 5 tampil dengan Title "Seven Independent Config Areas"
4. Klik `[Next]`
5. Verifikasi Step berikutnya tampil dengan Title "Hover for Field Help"
6. Klik `[Next]`
7. Verifikasi Step berikutnya tampil dengan Title "Each Tab Keeps Its Own Changelog"
8. Verifikasi Title "Reset to Platform Default" dan "Save Is Per-Tab" tidak tampil karena `[Reset to Default]` dan `[Save]` Hidden bagi Read Only
9. Klik `[Done]` pada step terakhir
10. Verifikasi Walkthrough tertutup

## Notes

- Pengecualian suite: spec ini mengatur flag Guided Tooltip akun Read Only sendiri (bagian 4 konvensi, KEPUTUSAN 2026-10-22).
- Langkah penghubung (S-03): "Klik menu Plans & Features" lalu klik menu Lifecycle Settings memulai walkthrough dari Step 1 setelah hook `beforeEach` membuka halaman. Pembukaan halaman Lifecycle Settings oleh hook `beforeEach` suite adalah layar awal; langkah klik menu sidebar atau klik tab pada spec ini adalah langkah TC sumber atau langkah penghubung yang dicatat di butir langkah penghubung.
- Temuan untuk QA: TC 57 langkah 2 meminta "catat Title tiap step"; spec mengasersi Title tiap step yang tampil (tiga step: Step 1, 2, dan 5 menurut TC 50) dan absennya dua Title lain sesudah ketiganya tampil (anchor positif). Nomor "Step n of 5" untuk Read Only tidak ditulis TC (jumlah step yang tampil bagi Read Only tampak 3).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
