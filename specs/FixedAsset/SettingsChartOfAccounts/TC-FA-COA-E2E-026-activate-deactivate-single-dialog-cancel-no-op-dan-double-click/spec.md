---
id: TC-FA-COA-E2E-026-activate-deactivate-single-dialog-cancel-no-op-dan-double-click
title: "Activate Deactivate Single: Dialog, Cancel, No-Op, dan Double Click"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-46
  - TC-FA-COA-47
  - TC-FA-COA-285
coverage:
  web: automated
---

# Activate Deactivate Single: Dialog, Cancel, No-Op, dan Double Click

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE, nama kunci ditetapkan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P3 | `4-7001 – Gain on Disposal` | Inactive, Used By 0; hanya dibaca (Cancel tidak mengubah data) | TC-46 |
  | P48 | `4-7101 – Gain on Disposal – Single Activate` | Inactive, Used By 0; sekali pakai, diaktifkan | TC-47 |
  | P84 | `CAP-8214 – Capitalization Clearing – Double Deactivate A` | Active, Used By 0; sekali pakai, dinonaktifkan | TC-285 |
  | P85 | `CAP-8215 – Capitalization Clearing – Double Deactivate B` | Active, Used By 0; sekali pakai, dinonaktifkan | TC-285 |

- Pengecualian A-18 (butir "Data bersama" di `suite.md`): akun sekali pakai P48, P84, dan P85 diubah statusnya spec ini dan dipakai spec ini saja. Seed idempotent dan pemulihan ke kondisi awal (termasuk status dan Last Updated) dijalankan fixture backend (disediakan tim FE/BE) di hook `before` dan `after` spec ini; suite berjalan serial. P3 hanya dibaca.
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-46: Dialog konfirmasi Activate single dan Cancel tidak mengubah status

1. Ketik Search `4-7001`, tekan Enter
2. Klik switch Status pada akun P3 (`4-7001`)
3. Verifikasi dialog "Activate Account" dengan bullet `• 4-7001 – Gain on Disposal` dan teks "Are you sure you want to activate it?"
4. Verifikasi tombol `[Cancel]` dan `[Activate]` tampil
5. Klik `[Cancel]`
6. Verifikasi switch Status P3 tetap Inactive

### TC-FA-COA-47: Activate single akun Inactive berhasil

7. Ganti isi kotak search dengan `4-7101`, tekan Enter
8. Klik switch Status pada akun P48 (`4-7101`)
9. Klik `[Activate]`
10. Verifikasi toast "Success, account has been activated."
11. Verifikasi switch Status P48 menjadi Active

### TC-FA-COA-285: Klik ganda `[Deactivate]` pada dialog D-02 menonaktifkan akun satu kali

12. Ganti isi kotak search dengan `Double Deactivate`, tekan Enter
13. Tunggu toast lama hilang otomatis
14. Centang akun P84 (`CAP-8214`) dan P85 (`CAP-8215`)
15. Klik Bulk `Deactivate`
16. Klik `[Deactivate]` pada dialog D-02 dua kali cepat
17. Verifikasi hanya satu toast "Success, account has been deactivated."
18. Verifikasi akun P84 dan P85 menjadi Inactive

## Notes

- Langkah penghubung (S-03, R-16): Search Account Code (langkah 1, 7) atau nama (langkah 12) untuk membuka baris target; langkah 12 menyaring tepat P84 dan P85; "Tunggu toast lama hilang otomatis" (langkah 13) sebelum hitungan toast.
- `A-18`: P48 (TC-47), P84 dan P85 (TC-285) menjadi target ubah status sekali pakai; syarat A-18 dinyatakan di `## Prerequisites`.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-47 (log L-03 di Changelog, System Log, Activity Log; dampak ke modul lain) dan TC-285 (satu entri L-03 per akun per surface) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-8214` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
