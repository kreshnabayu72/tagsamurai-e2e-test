---
id: TC-FA-PREF-E2E-040-validasi-v-04-akun-default-berubah-sesi-lain-dengan-dialog
title: "Validasi V-04: akun Default Gain menjadi Inactive dan akun Default Loss dihapus oleh sesi lain sebelum Save (dengan dialog Save Changes)"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-142
  - TC-FA-PREF-143
sourceRules: ["FAPREF-LOGIC-10a", "F-FAPREF-01.k4c", "V-04", "FAPREF-LOGIC-06h"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-10a": [4, 17]
  "F-FAPREF-01.k4c": [6, 7, 11, 19, 20, 24]
  "V-04": [8, 9, 21, 22]
  "FAPREF-LOGIC-06h": [11, 24]
coverage:
  web: automated
---

# Validasi V-04: akun Default Gain menjadi Inactive dan akun Default Loss dihapus oleh sesi lain sebelum Save (dengan dialog Save Changes)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1, PA-2): Preferences nilai awal tidak terkunci (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Disposal Documents keenam jenis Optional, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open.
- Data: Chart of Accounts PA-3: `4-9100 – Laba Pelepasan Aset` (Active, Gain on Disposal), `5-9100 – Rugi Pelepasan Aset` (Active, Loss on Disposal); Asset Class sesuai PA-16. Akun Total Control kedua (PA-8): email tidak tertulis di Pre-setup TC, disediakan tim FE.
- Kemampuan teknis: sesi API Total Control (butir "Sesi API aktor" di `suite.md`): pelaku kedua yang hanya memicu perubahan state; token tidak dihitung sebagai sesi web. Dipakai untuk menonaktifkan akun `4-9100 – Laba Pelepasan Aset` dan menghapus akun `5-9100 – Rugi Pelepasan Aset` sebagai pelaku kedua; keduanya hanya pemicu state.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-142: Save dengan akun Default Gain on Disposal yang menjadi Inactive sejak form dibuka ditolak dengan caption V-04

1. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
2. Lewat sesi API Total Control kedua (PA-8), nonaktifkan akun "4-9100 – Laba Pelepasan Aset" hingga tersimpan Inactive
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" tampil lebih dulu karena Default Gain/Loss on Disposal adalah setting berdampak
5. Klik `[Save]` pada dialog "Save Changes"
6. Verifikasi dialog "Save Changes" ditutup karena server menolak Save
7. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
8. Verifikasi caption "This default gain on disposal no longer exists. Please select another." tampil di bawah Select Default Gain on Disposal
9. Verifikasi Select Default Gain on Disposal dikosongkan otomatis
10. Buka daftar opsi Select Default Gain on Disposal
11. Verifikasi opsi akun dimuat ulang dan akun "4-9100 – Laba Pelepasan Aset" tidak lagi ada pada opsi

### TC-FA-PREF-143: Save dengan akun Default Loss on Disposal yang menjadi tidak ditemukan sejak form dibuka ditolak dengan caption V-04

12. Pulihkan akun `4-9100 – Laba Pelepasan Aset` ke Active lewat seed API hingga tersimpan
13. Buka ulang Fixed Asset > Settings > Accounting > Preferences
14. Pilih "5-9100 – Rugi Pelepasan Aset" pada Select Default Loss on Disposal
15. Lewat sesi API Total Control kedua (PA-8), hapus akun "5-9100 – Rugi Pelepasan Aset" dari Chart of Accounts hingga terhapus
16. Klik `[Save changes]`
17. Verifikasi dialog "Save Changes" tampil lebih dulu karena Default Gain/Loss on Disposal adalah setting berdampak
18. Klik `[Save]` pada dialog "Save Changes"
19. Verifikasi dialog "Save Changes" ditutup karena server menolak Save
20. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
21. Verifikasi caption "This default loss on disposal no longer exists. Please select another." tampil di bawah Select Default Loss on Disposal
22. Verifikasi Select Default Loss on Disposal dikosongkan otomatis
23. Buka daftar opsi Select Default Loss on Disposal
24. Verifikasi opsi akun dimuat ulang dan akun "5-9100 – Rugi Pelepasan Aset" tidak lagi ada pada opsi

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 12; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 13.
- Pemicu perubahan akun lewat sesi API; TC menyebutnya "sesi 2" (lihat Temuan untuk QA). Akun yang diubah dipulihkan lewat seed pada awal blok berikutnya dan oleh hook `after` setelah blok terakhir. Tidak ada `[Cancel]` setelah penolakan karena Select akun dikosongkan otomatis menyamai nilai tersimpan (kosong).
- Temuan untuk QA:
  - TC-FA-PREF-142 sampai 145 menyebut "sesi 2 (pengguna lain)" tanpa menyatakan UI atau API dan email akun Total Control kedua (PA-8) tidak tertulis di Pre-setup; spec memakai sesi API Total Control kedua (disediakan tim FE).
  - Expected b TC-FA-PREF-142 sampai 145 ("form tetap memuat seluruh perubahan yang belum disimpan") dan d ("Select dikosongkan otomatis") saling berhimpitan karena satu-satunya perubahan di form adalah Select akun yang dikosongkan; spec mengasersi keduanya apa adanya.
  - Kolom Data TC-FA-PREF-142 sampai 145 menyebut "sesi kedua mengubah status/function akun" tanpa membedakan kasus; spec memakai aksi di langkah TC (nonaktifkan, hapus, ubah function).
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
