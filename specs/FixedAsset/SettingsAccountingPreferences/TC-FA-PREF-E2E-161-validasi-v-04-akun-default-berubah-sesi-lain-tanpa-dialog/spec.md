---
id: TC-FA-PREF-E2E-161-validasi-v-04-akun-default-berubah-sesi-lain-tanpa-dialog
title: "Validasi V-04: function Default Capitalization Offset berubah dan Found Asset Credit Account menjadi Inactive oleh sesi lain sebelum Save (tanpa dialog)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-144
  - TC-FA-PREF-145
coverage:
  web: automated
---

# Validasi V-04: function Default Capitalization Offset berubah dan Found Asset Credit Account menjadi Inactive oleh sesi lain sebelum Save (tanpa dialog)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1, PA-2): Preferences nilai awal tidak terkunci (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Disposal Documents keenam jenis Optional, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open.
- Data: Chart of Accounts PA-3: `1-2900 – Biaya Dikapitalisasi` (Active, Capitalization Offset), `4-1500 – Pendapatan Lain-lain` (Active, Depreciation Expense); Asset Class sesuai PA-16. Akun Total Control kedua (PA-8): email tidak tertulis di Pre-setup TC, disediakan tim FE.
- Kemampuan teknis: sesi API Total Control (butir "Sesi API aktor" di `suite.md`): pelaku kedua yang hanya memicu perubahan state; token tidak dihitung sebagai sesi web. Dipakai untuk mengubah function akun `1-2900 – Biaya Dikapitalisasi` dan menonaktifkan akun `4-1500 – Pendapatan Lain-lain` sebagai pelaku kedua; keduanya hanya pemicu state.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-144: Save dengan akun Default Capitalization Offset yang menjadi function tidak sesuai sejak form dibuka ditolak dengan caption V-04

1. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Default Capitalization Offset
2. Lewat sesi API Total Control kedua (PA-8), ubah function akun "1-2900 – Biaya Dikapitalisasi" hingga bukan Capitalization Offset tersimpan
3. Klik `[Save changes]`
4. Verifikasi Save langsung berlanjut tanpa dialog "Save Changes" karena setting tidak berdampak
5. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
6. Verifikasi caption "This default capitalization offset no longer exists. Please select another." tampil di bawah Select Default Capitalization Offset
7. Verifikasi Select Default Capitalization Offset dikosongkan otomatis
8. Buka daftar opsi Select Default Capitalization Offset
9. Verifikasi opsi akun dimuat ulang dan akun "1-2900 – Biaya Dikapitalisasi" tidak lagi ada pada opsi

### TC-FA-PREF-145: Save dengan akun Found Asset Credit Account yang menjadi Inactive sejak form dibuka ditolak dengan caption V-04

10. Pulihkan function akun `1-2900 – Biaya Dikapitalisasi` ke Capitalization Offset lewat seed API hingga tersimpan
11. Buka ulang Fixed Asset > Settings > Accounting > Preferences
12. Pilih "4-1500 – Pendapatan Lain-lain" pada Select Found Asset Credit Account
13. Lewat sesi API Total Control kedua (PA-8), nonaktifkan akun "4-1500 – Pendapatan Lain-lain" hingga tersimpan Inactive
14. Klik `[Save changes]`
15. Verifikasi Save langsung berlanjut tanpa dialog "Save Changes" karena setting tidak berdampak
16. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
17. Verifikasi caption "This found asset credit account no longer exists. Please select another." tampil di bawah Select Found Asset Credit Account
18. Verifikasi Select Found Asset Credit Account dikosongkan otomatis
19. Buka daftar opsi Select Found Asset Credit Account
20. Verifikasi opsi akun dimuat ulang dan akun "4-1500 – Pendapatan Lain-lain" tidak lagi ada pada opsi

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 10; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 11.
- Pemicu perubahan akun lewat sesi API; TC menyebutnya "sesi 2" (lihat Temuan untuk QA). Akun yang diubah dipulihkan lewat seed pada awal blok berikutnya dan oleh hook `after` setelah blok terakhir. Tidak ada `[Cancel]` setelah penolakan karena Select akun dikosongkan otomatis menyamai nilai tersimpan (kosong).
- Temuan untuk QA:
  - TC-FA-PREF-142 sampai 145 menyebut "sesi 2 (pengguna lain)" tanpa menyatakan UI atau API dan email akun Total Control kedua (PA-8) tidak tertulis di Pre-setup; spec memakai sesi API Total Control kedua (disediakan tim FE).
  - Expected b TC-FA-PREF-142 sampai 145 ("form tetap memuat seluruh perubahan yang belum disimpan") dan d ("Select dikosongkan otomatis") saling berhimpitan karena satu-satunya perubahan di form adalah Select akun yang dikosongkan; spec mengasersi keduanya apa adanya.
  - Kolom Data TC-FA-PREF-142 sampai 145 menyebut "sesi kedua mengubah status/function akun" tanpa membedakan kasus; spec memakai aksi di langkah TC (nonaktifkan, hapus, ubah function).
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
