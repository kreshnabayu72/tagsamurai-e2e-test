---
id: TC-FA-PREF-E2E-041-save-ditolak-akun-default-berubah-sebelum-save-versi-dialog
title: "Save ditolak karena akun Default Gain atau Loss on Disposal berubah sebelum Save (alur Save dengan dialog D-01)"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-214
  - TC-FA-PREF-215
sourceRules: ["F-FAPREF-01.k4c", "V-04", "FAPREF-LOGIC-06h", "E-FAPREF-04"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k4c": [5, 6, 10, 18, 19, 23]
  "V-04": [7, 8, 20, 21]
  "FAPREF-LOGIC-06h": [10, 23]
  "E-FAPREF-04": [11, 24]
coverage:
  web: automated
---

# Save ditolak karena akun Default Gain atau Loss on Disposal berubah sebelum Save (alur Save dengan dialog D-01)

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

### TC-FA-PREF-214: Save ditolak saat akun Default Gain on Disposal yang dipilih menjadi Inactive sebelum Save

1. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
2. Lewat fixture BE, ubah status akun 4-9100 menjadi Inactive hingga tersimpan
3. Klik `[Save changes]`
4. Klik `[Save]` pada dialog D-01
5. Verifikasi dialog D-01 ditutup
6. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
7. Verifikasi caption "This default gain on disposal no longer exists. Please select another." tampil pada Select Default Gain on Disposal
8. Verifikasi Select Default Gain on Disposal dikosongkan otomatis dan menampilkan placeholder "Select account"
9. Buka daftar opsi Select Default Gain on Disposal
10. Verifikasi opsi akun pada Select Default Gain on Disposal dimuat ulang dan akun "4-9100 – Laba Pelepasan Aset" tidak lagi ada pada opsi
11. Verifikasi tidak ada toast sukses

### TC-FA-PREF-215: Save ditolak saat akun Default Loss on Disposal yang dipilih dihapus sebelum Save

12. Pulihkan akun `4-9100 – Laba Pelepasan Aset` ke Active lewat fixture BE hingga tersimpan
13. Buka ulang Fixed Asset > Settings > Accounting > Preferences
14. Pilih "5-9100 – Rugi Pelepasan Aset" pada Select Default Loss on Disposal
15. Lewat fixture BE, hapus akun 5-9100 dari Chart of Accounts hingga terhapus
16. Klik `[Save changes]`
17. Klik `[Save]` pada dialog D-01
18. Verifikasi dialog D-01 ditutup
19. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
20. Verifikasi caption "This default loss on disposal no longer exists. Please select another." tampil pada Select Default Loss on Disposal
21. Verifikasi Select Default Loss on Disposal dikosongkan otomatis dan menampilkan placeholder "Select account"
22. Buka daftar opsi Select Default Loss on Disposal
23. Verifikasi opsi akun pada Select Default Loss on Disposal dimuat ulang dan akun "5-9100 – Rugi Pelepasan Aset" tidak lagi ada pada opsi
24. Verifikasi tidak ada toast sukses

## Notes
- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 12; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 13.
- Dialog D-01 muncul pada TC-FA-PREF-214 dan 215 (Default Gain/Loss on Disposal setting berdampak). Akun dipulihkan lewat fixture BE pada awal blok berikutnya dan oleh hook `after` setelah blok terakhir; tidak ada `[Cancel]` setelah penolakan karena Select akun dikosongkan otomatis menyamai nilai tersimpan (kosong).
- Langkah verifikasi bahwa akun terdampak tidak lagi ada pada opsi memperinci Expected "opsi akun dimuat ulang" mengikuti pola TC-FA-PREF-142 sampai 145 (S-03).
- Temuan untuk QA:
  - Expected d TC-FA-PREF-214 dan 215 ("opsi akun dimuat ulang") tidak menyebut isi opsi; spec mengasersi akun terdampak tidak lagi ada pada opsi, mengikuti rumusan TC-FA-PREF-142 sampai 145.
  - Expected a dan c TC-FA-PREF-214 dan 215 ("form tetap memuat seluruh perubahan yang belum disimpan" dan "Select dikosongkan otomatis") berhimpitan karena perubahan form hanya Select akun; spec mengasersi keduanya apa adanya.
  - TC-FA-PREF-214 dan 215 menulis "dialog D-01" tanpa judul dialog; spec memakai istilah TC.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
