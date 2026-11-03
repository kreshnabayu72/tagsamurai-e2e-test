---
id: TC-FA-PREF-E2E-175-save-ditolak-akun-capitalization-offset-dan-found-asset-credit-berubah-sebelum-save-tanpa-dialog
title: "Save ditolak karena akun Default Capitalization Offset atau Found Asset Credit Account berubah sebelum Save (alur Save tanpa dialog)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-216
  - TC-FA-PREF-217
coverage:
  web: automated
---

# Save ditolak karena akun Default Capitalization Offset atau Found Asset Credit Account berubah sebelum Save (alur Save tanpa dialog)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PB (TC-FA-PREF-176-361), company `PT Contoh Konstruksi` plan Growth (PB-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open, tidak ada penyusutan diposting, Tax Depreciation Class hanya versi pertama tanpa Effective From, tidak ada transaksi bertanggal.
- Data: Chart of Accounts PB-2: `4-9100 – Laba Pelepasan Aset` (Active, Gain on Disposal), `5-9100 – Rugi Pelepasan Aset` (Active, Loss on Disposal), `1-2900 – Biaya Dikapitalisasi` (Active, Capitalization Offset), `1-1001 – Kas Utama` (Active, Asset Cost); Asset Class IT Equipment, Vehicles, Furniture (PB-3).
- Kemampuan teknis: fixture BE untuk mengubah status, menghapus, dan mengubah function akun Chart of Accounts (DB-5), disediakan tim FE/BE; hanya pemicu state. Langkah pemicu ditulis "... hingga ... tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-216: Save ditolak saat function akun Default Capitalization Offset berubah dan tidak lagi sesuai sebelum Save

1. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Default Capitalization Offset
2. Lewat fixture BE, ubah function akun 1-2900 menjadi bukan Capitalization Offset hingga tersimpan
3. Klik `[Save changes]`
4. Verifikasi caption "This default capitalization offset no longer exists. Please select another." tampil pada Select Default Capitalization Offset
5. Verifikasi Select Default Capitalization Offset dikosongkan otomatis dan menampilkan placeholder "Select account"
6. Buka daftar opsi Select Default Capitalization Offset
7. Verifikasi opsi akun pada Select Default Capitalization Offset dimuat ulang dan akun "1-2900 – Biaya Dikapitalisasi" tidak lagi ada pada opsi
8. Verifikasi tidak ada toast sukses

### TC-FA-PREF-217: Save ditolak saat akun Found Asset Credit Account yang dipilih menjadi Inactive sebelum Save

9. Pulihkan function akun `1-2900 – Biaya Dikapitalisasi` ke Capitalization Offset lewat fixture BE hingga tersimpan
10. Buka ulang Fixed Asset > Settings > Accounting > Preferences
11. Pilih "1-1001 – Kas Utama" pada Select Found Asset Credit Account
12. Lewat fixture BE, ubah status akun 1-1001 menjadi Inactive hingga tersimpan
13. Klik `[Save changes]`
14. Verifikasi caption "This found asset credit account no longer exists. Please select another." tampil pada Select Found Asset Credit Account
15. Verifikasi Select Found Asset Credit Account dikosongkan otomatis dan menampilkan placeholder "Select account"
16. Buka daftar opsi Select Found Asset Credit Account
17. Verifikasi opsi akun pada Select Found Asset Credit Account dimuat ulang dan akun "1-1001 – Kas Utama" tidak lagi ada pada opsi
18. Verifikasi tidak ada toast sukses

## Notes
- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 9; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 10.
- TC-FA-PREF-216 dan 217 langsung ditolak tanpa dialog, mengikuti TC. Akun dipulihkan lewat fixture BE pada awal blok berikutnya dan oleh hook `after` setelah blok terakhir; tidak ada `[Cancel]` setelah penolakan karena Select akun dikosongkan otomatis menyamai nilai tersimpan (kosong).
- Langkah verifikasi bahwa akun terdampak tidak lagi ada pada opsi memperinci Expected "opsi akun dimuat ulang" mengikuti pola TC-FA-PREF-142 sampai 145 (S-03).
- Temuan untuk QA:
  - Expected d TC-FA-PREF-216 dan 217 ("opsi akun dimuat ulang") tidak menyebut isi opsi; spec mengasersi akun terdampak tidak lagi ada pada opsi, mengikuti rumusan TC-FA-PREF-142 sampai 145.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
