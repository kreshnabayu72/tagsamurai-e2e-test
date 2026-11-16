---
id: TC-FA-PREF-E2E-043-validasi-v-09-fiscal-year-start-versi-tax-depreciation-class-alur-edit
title: "Validasi V-09: perubahan Fiscal Year Start ditolak saat ada versi Tax Depreciation Class ber-Effective From (alur edit)"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-152
  - TC-FA-PREF-153
  - TC-FA-PREF-154
  - TC-FA-PREF-578
sourceRules: ["D-01", "PV-04", "PV-05", "F-FAPREF-01.k19d", "V-09", "D-03", "E-FAPREF-38", "F-FAPREF-01.k19a", "F-FAPREF-01.k20e", "T-01", "FAPREF-LOGIC-02k"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 12, 22, 30]
  "PV-04": [3, 12, 22, 30]
  "PV-05": [3, 12, 30]
  "F-FAPREF-01.k19d": [5, 6, 15, 16]
  "V-09": [7, 14]
  "D-03": 8
  "E-FAPREF-38": 8
  "F-FAPREF-01.k19a": [17, 18]
  "F-FAPREF-01.k20e": 23
  "T-01": [25, 32]
  "FAPREF-LOGIC-02k": 33
coverage:
  web: automated
---

# Validasi V-09: perubahan Fiscal Year Start ditolak saat ada versi Tax Depreciation Class ber-Effective From (alur edit)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1, PA-2): Preferences nilai awal tidak terkunci (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Disposal Documents keenam jenis Optional, Journal Grouping Group), periode Mar 2026 sampai Dec 2026 Open. Untuk TC-FA-PREF-152 dan 153 kelas Tax Depreciation Class `Kelompok 1` memiliki versi kedua dengan Effective From 1 Januari 2026 (PA-11); untuk TC-FA-PREF-154 semua kelas hanya memiliki versi pertama tanpa Effective From (PA-12). Asset Class PA-16 (3 Asset Class memakai threshold default). Penyusutan belum diposting dan semua periode Open.
- Data: TC-FA-PREF-578 memakai seri PC (PC-3): Fiscal Year Start tersimpan January, belum terkunci, satu kelas Tax Depreciation Class memiliki versi kedua ber-Effective From.
- Seri fixture PA, PB, dan PC bernilai awal setara (PA-2, PB-1, PC-1); spec yang memuat TC dari lebih dari satu seri men-seed ulang lewat API di antara TC sesuai Precondition TC.
- State global: jam sistem server dan browser dikendalikan pada 28 Oktober 2026 pukul 10:00 Time Zone entitas Asia/Jakarta (PA-1; bulan berjalan Oktober 2026) dan dipulihkan di hook `after` (kendali jam sistem: butir di `suite.md`).
- Kemampuan teknis: Baca state Preferences, periode akuntansi, dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-152: Save mengubah Fiscal Year Start saat ada versi Tax Depreciation Class berEffective From ditolak dengan caption V-09

1. Ubah Select Fiscal Year Start dari "January" menjadi "April"
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
4. Klik `[Save]` pada dialog
5. Verifikasi dialog "Save Changes" ditutup karena server menolak Save
6. Verifikasi form tetap memuat Fiscal Year Start "April" yang belum disimpan
7. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil di bawah Fiscal Year Start
8. Verifikasi tidak ada toast sukses dan tidak ada dialog blok "Cannot Save Preferences"
9. Klik `[Cancel]`

### TC-FA-PREF-578: Save Fiscal Year Start saat ada versi Tax Depreciation Class berEffective From menampilkan caption V-09 (seri PC)

10. Pilih "April" pada Select Fiscal Year Start
11. Klik `[Save changes]`
12. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
13. Klik `[Save]` pada dialog "Save Changes"
14. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada field Fiscal Year Start
15. Verifikasi dialog "Save Changes" tertutup
16. Verifikasi form tetap memuat April sebagai perubahan yang belum disimpan
17. Verifikasi periode akuntansi tidak dibangun ulang
18. Verifikasi tidak ada yang tersimpan: Fiscal Year Start tersimpan tetap January
19. Klik `[Cancel]`

### TC-FA-PREF-153: Save yang hanya mengubah First Accounting Period tidak terpengaruh versi Tax Depreciation Class berEffective From

20. Ubah First Accounting Period dari "March 2026" menjadi "February 2026"
21. Klik `[Save changes]`
22. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "11 accounting periods will be rebuilt.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
23. Verifikasi dialog "Save Changes" tidak memuat baris "Tax year start also follows Fiscal Year Start." karena hanya First Accounting Period yang berubah
24. Klik `[Save]` pada dialog
25. Verifikasi toast "Success, accounting preferences have been saved." tampil

### TC-FA-PREF-154: Versi pertama Tax Depreciation Class yang tidak bertanggal tidak menghalangi perubahan Fiscal Year Start

26. Siapkan Preferences nilai awal PA-2 dan seed PA-12 (semua kelas Tax Depreciation Class hanya memiliki versi pertama tanpa Effective From) lewat seed API hingga tersimpan
27. Buka ulang Fixed Asset > Settings > Accounting > Preferences
28. Ubah Select Fiscal Year Start dari "January" menjadi "April"
29. Klik `[Save changes]`
30. Verifikasi dialog "Save Changes" tampil dengan daftar bullet: "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` (text, contrast) dan `[Save]`
31. Klik `[Save]` pada dialog
32. Verifikasi toast "Success, accounting preferences have been saved." tampil
33. Verifikasi tidak ada caption V-09 pada Fiscal Year Start

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 9, 19; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 26; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 27.
- Urutan: TC-FA-PREF-152 dan 578 (Save ditolak) lebih dulu, lalu TC-FA-PREF-153 dan 154 (Save sukses) sesuai S-10. Seed TC-FA-PREF-154 mengganti varian Tax Depreciation Class ke PA-12; hook `after` memulihkan state server.
- Temuan untuk QA:
  - TC-FA-PREF-153 dan 154 punya Post Condition (First Accounting Period atau Fiscal Year Start tersimpan, periode akuntansi dibangun ulang, entri Changelog) tanpa langkah observasi; tidak diasersi.
  - Precondition e TC-FA-PREF-152 sampai 154 menyebut tanggal sistem uji tanpa Expected yang bergantung padanya; dipakai sebagai kendali jam di Prerequisites.
  - Rumusan dialog TC-FA-PREF-578 tidak memuat "(text, contrast)" pada tombol `[Cancel]` seperti TC-FA-PREF-152; spec mengikuti masing-masing TC.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
