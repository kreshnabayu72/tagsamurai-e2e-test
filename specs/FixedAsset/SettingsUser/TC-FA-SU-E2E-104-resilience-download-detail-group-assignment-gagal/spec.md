---
id: TC-FA-SU-E2E-104-resilience-download-detail-group-assignment-gagal
title: "Resilience Download Detail Group Assignment Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-904
coverage:
  web: automated
---

# Resilience Download Detail Group Assignment Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23). Pengguna target: Wawan Setiawan (Pre-setup #23: Manage files pada IT Infrastructure dan Branch Surabaya; Manage purchase pada General Affairs dan Logistics Warehouse; Manage group pada Branch Surabaya, Finance & Accounting, dan Logistics Warehouse). Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP Download popup Detail Group Assignment (5xx). Intercept dilepas segera setelah pemicu selesai (S-09).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-904: Download popup Detail Group Assignment gagal

1. Intercept respons Download menjadi 5xx
2. Buka Detail Wawan Setiawan > Tab Role > Sub-tab Group Role lalu klik `[Detail]` pada baris Manage purchase
3. Klik Download lalu pilih CSV
4. Lepas intercept Download
5. Verifikasi toast error "Error, failed to download Group-Assignment-Wawan-Setiawan-Manage-purchase-document." tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec berisi satu kelas harness (b, fault injection) dengan intercept di atas backend nyata; modenya FE+BE (bagian 6).
- Langkah penghubung (tanpa awalan `Verifikasi`): melepas intercept (S-09).
- Temuan untuk QA (S-15): TC-FA-SU-904 tidak punya Post Condition.
