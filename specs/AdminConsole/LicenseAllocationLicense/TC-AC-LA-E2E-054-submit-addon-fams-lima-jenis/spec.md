---
id: TC-AC-LA-E2E-054-submit-addon-fams-lima-jenis
title: "Submit Allocate: Addon FAMS (Audit, Maintenance, Tracking, Maps, IT Inventory) ke Target Paid Active"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-158
coverage:
  web: automated
---

# Submit Allocate: Addon FAMS (Audit, Maintenance, Tracking, Maps, IT Inventory) ke Target Paid Active

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34). Harga kelima Addon (Audit, Maintenance, Tracking, Maps, IT Inventory) di-set pada Product Price kantong Distributor oleh fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan ke keadaan awal di hook `after` (lihat Temuan untuk QA). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: lima alokasi Addon +1 ke PT Sejahtera (Completed, Active). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Tabel "Addon" untuk langkah 1 sampai 6:

  | Addon (Type) | License Type di List |
  |---|---|
  | `Audit` | `Addon (Audit)` |
  | `Maintenance` | `Addon (Maintenance)` |
  | `Tracking` | `Addon (Tracking)` |
  | `Maps` | `Addon (Maps)` |
  | `IT Inventory` | `Addon (IT Inventory)` |

- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum tiap `[Submit]` (langkah 1).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-158: Submit Addon FAMS ke Target Paid Active

Untuk setiap baris tabel "Addon" (langkah 1 sampai 6):

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type sesuai kolom Addon (Type), isi Additional Quantity `1`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, license has been allocated."
6. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 1) dengan License Type sesuai kolom "License Type di List" dan Status `Active`; lalu tunggu toast hilang otomatis

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Langkah 1 sampai 6 diulang untuk 5 baris tabel (bagian 8b butir 7); ekspansi: 6 langkah × 5 = 30 langkah, di bawah ambang 35 langkah. Buka form 5 kali, kejadian menutup 5 (modal tertutup oleh Submit di tiap iterasi).
- Langkah penghubung (S-03): langkah 1 (baseline) dan penantian toast hilang pada langkah 6 agar toast iterasi berikutnya dapat diasersi (R-12).
- Temuan untuk QA:
  - TC-AC-LA-158 mensyaratkan harga kelima Addon di-set, sedangkan Pre-setup #34 hanya mencantumkan Addon Audit $365 dan Addon IT Inventory $100; Pre-setup #36 men-set Addon Tracking $0 dan #37 membiarkan Addon Maps belum di-set (dipakai TC-AC-LA-146); pengaturan harga antar TC diserahkan ke fixture backend.
  - TC-AC-LA-158 Expected c ("Addon hanya membutuhkan Subscription Paid tanpa gate tambahan") bukan hasil yang dapat diamati terpisah; keberhasilan kelima Submit pada langkah 5 dan 6 menjadi bukti.
  - TC-AC-LA-158 Post Condition ("Lima record Addon tercatat") diwakili oleh lima baris baru pada langkah 6; TC tidak memberi langkah observasi lain.
