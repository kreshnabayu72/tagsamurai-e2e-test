---
id: TC-FA-LIC-E2E-153-state-tenant-auto-cancel-approval-saat-plan-diturunkan-dan-downgrade-berlaku
title: "State Tenant: Auto-cancel Sistem Saat Plan Kehilangan Approval Workflow Melepas Reserved"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-397
coverage:
  web: automated
---

# State Tenant: Auto-cancel Sistem Saat Plan Kehilangan Approval Workflow Melepas Reserved

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki, alokasi grup, kuota, plan, status aset, dan jam fixture dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data Pre-setup: #12 (License Summary Reserved 15, Used 4320, Remaining 665; Divisi IT beralokasi dengan Reserved by This Group 0 dan Remaining Quota 40) dan #20 (aset Waiting for Approval di Divisi IT; client Professional). Kondisi blok TC-FA-LIC-397 (diatur fixture BE): aset Waiting for Approval dan plan diturunkan dari Professional ke Growth (kehilangan FA-1) saat downgrade berlaku.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup dan aset Pre-setup #12 dan #20 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dan #20 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung. Efek: Used, Reserved, dan Remaining, status aset, plan, dan Last Updated berubah; fixture memulihkannya. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: jam fixture digeser maju; sesi UI dan sesi API aktor tetap valid selama jam digeser (dinyatakan di `suite.md`) dan jam serta plan dipulihkan di hook `after` serta pada langkah 9.

## Test Steps

### TC-FA-LIC-397: Auto-cancel sistem saat plan kehilangan Approval Workflow melepas Reserved

1. Jalankan fixture BE pemulih Pre-setup #12 dan #20 dengan aset Waiting for Approval dan plan diturunkan dari Professional ke Growth saat downgrade berlaku hingga tersimpan
2. Buka License > All License; catat Reserved dan Remaining pada License Summary kolom Asset
3. Geser jam fixture ke saat downgrade berlaku
4. Buka daftar aset
5. Verifikasi aset yang Waiting for Approval otomatis kembali berstatus `Draft`
6. Buka License > All License
7. Verifikasi Reserved turun sesuai jumlah aset yang di-cancel dibanding nilai pada langkah 2
8. Verifikasi Remaining naik sama banyak dibanding nilai pada langkah 2
9. Pulihkan jam fixture dan plan ke Pre-setup #12 hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Spec berkelas h (state tenant: perubahan plan tier) dengan pemicu jam fixture (kelas d) sebagai pemicu waktu downgrade, bukan objek uji; satu TC.
- Langkah penghubung (S-03, aksi tanpa `Verifikasi`): langkah 1 dan 9 (fixture BE pemulih dan penyetel state), langkah 3 (menggeser jam fixture), langkah 4 (membuka daftar aset), serta navigasi License. Langkah 2 mencatat nilai License Summary sebagai baseline langkah 7 dan 8 (S-12).
- Pemulihan jam dan plan dilakukan pada langkah 9 sebelum akun aktor membuka halaman lain (S-09).
- TC-FA-LIC-397 menyebut Expected "Reserved turun sesuai jumlah aset yang di-cancel" tanpa jumlah; spec mengasersi dibanding baseline langkah 2.
- Pembagian TC lintas spec: TC-FA-LIC-394 sampai TC-FA-LIC-396 ada di spec 119 dan TC-FA-LIC-398 sampai TC-FA-LIC-400 di spec 146.
- Temuan untuk QA:
  - TC-FA-LIC-397 tidak menyebut tempat mengamati status `Draft` aset; spec memakai daftar aset.
