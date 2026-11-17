---
id: TC-FA-PREF-E2E-045-validasi-v-10-first-accounting-period-transaksi-bertanggal-paling-awal
title: "Validasi V-10: First Accounting Period terhadap transaksi bertanggal paling awal (satu bulan sebelum, sama, dan sesudah)"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-155
  - TC-FA-PREF-156
  - TC-FA-PREF-157
sourceRules: ["D-01", "PV-04", "F-FAPREF-01.k23", "V-10", "E-FAPREF-42", "T-01", "E-FAPREF-37"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 12, 20]
  "PV-04": [3, 12, 20]
  "F-FAPREF-01.k23": [5, 6]
  "V-10": 7
  "E-FAPREF-42": 8
  "T-01": [14, 22]
  "E-FAPREF-37": [15, 23]
coverage:
  web: automated
---

# Validasi V-10: First Accounting Period terhadap transaksi bertanggal paling awal (satu bulan sebelum, sama, dan sesudah)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1, PA-2): Preferences nilai awal tidak terkunci (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Disposal Documents keenam jenis Optional, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open. Transaksi bertanggal paling awal: aktivasi aset tanggal 15 Juni 2026 (PA-13, M = Jun 2026); penyusutan belum diposting dan semua periode Open; Asset Class PA-16 (3 Asset Class memakai threshold default).
- State global: jam sistem server dan browser dikendalikan pada 28 Oktober 2026 pukul 10:00 Time Zone entitas Asia/Jakarta (PA-1; bulan berjalan Oktober 2026) dan dipulihkan di hook `after` (kendali jam sistem: butir di `suite.md`).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-157: Ubah First Accounting Period ke July 2026 (satu bulan setelah bulan transaksi paling awal) ditolak dengan caption V-10

1. Ubah First Accounting Period dari "March 2026" menjadi "July 2026"
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "6 accounting periods will be rebuilt.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
4. Klik `[Save]` pada dialog
5. Verifikasi dialog "Save Changes" ditutup karena server menolak Save
6. Verifikasi form tetap memuat First Accounting Period "July 2026" yang belum disimpan
7. Verifikasi caption "First accounting period cannot be later than existing dated transactions." tampil di bawah First Accounting Period
8. Verifikasi tidak ada toast sukses dan tidak ada dialog blok "Cannot Save Preferences"
9. Klik `[Cancel]`

### TC-FA-PREF-155: Ubah First Accounting Period ke May 2026 (satu bulan sebelum bulan transaksi paling awal) berhasil

10. Ubah First Accounting Period dari "March 2026" menjadi "May 2026"
11. Klik `[Save changes]`
12. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "8 accounting periods will be rebuilt.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
13. Klik `[Save]` pada dialog
14. Verifikasi toast "Success, accounting preferences have been saved." tampil
15. Verifikasi tidak ada caption V-10 pada First Accounting Period

### TC-FA-PREF-156: Ubah First Accounting Period ke June 2026 (tepat bulan transaksi paling awal) berhasil

16. Pulihkan Preferences ke nilai awal PA-2 (First Accounting Period Mar 2026) lewat seed API hingga tersimpan
17. Buka ulang Fixed Asset > Settings > Accounting > Preferences
18. Ubah First Accounting Period dari "March 2026" menjadi "June 2026"
19. Klik `[Save changes]`
20. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "7 accounting periods will be rebuilt.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
21. Klik `[Save]` pada dialog
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Verifikasi tidak ada caption V-10 pada First Accounting Period

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 9; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 16; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 17.
- Urutan TC diubah dari 155, 156, 157 menjadi 157, 155, 156: Save yang ditolak lebih dulu agar tidak menunggu pemulihan seed (S-10, S-05).
- Temuan untuk QA:
  - TC-FA-PREF-156 menulis First Accounting Period tersimpan "Jun 2026" pada Post Condition sedangkan Expected memakai "June 2026"; Post Condition tanpa langkah observasi tidak diasersi.
  - TC-FA-PREF-155 dan 156 punya Post Condition (First Accounting Period tersimpan, periode dibangun ulang) tanpa langkah observasi; tidak diasersi.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
