---
id: TC-FA-PREF-E2E-044-validasi-v-09-first-accounting-period-tidak-terpengaruh-versi-tdc
title: "Validasi V-09: hanya First Accounting Period tidak terpengaruh; versi pertama tanpa Effective From tidak menghalangi Fiscal Year Start"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-219
  - TC-FA-PREF-220
  - TC-FA-PREF-579
  - TC-FA-PREF-580
sourceRules: ["F-FAPREF-01.k19d", "V-09", "E-FAPREF-38", "F-FAPREF-01.k21b", "T-01", "F-FAPREF-01.k19c", "E-FAPREF-37", "D-01", "PV-04", "F-FAPREF-01.k20b", "PV-05", "FAPREF-LOGIC-02k"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k19d": [4, 5]
  "V-09": 6
  "E-FAPREF-38": 7
  "F-FAPREF-01.k21b": 12
  "T-01": [13, 22, 31]
  "F-FAPREF-01.k19c": 14
  "E-FAPREF-37": 15
  "D-01": [20, 29]
  "PV-04": [20, 29]
  "F-FAPREF-01.k20b": 24
  "PV-05": 29
  "FAPREF-LOGIC-02k": 32
coverage:
  web: automated
---

# Validasi V-09: hanya First Accounting Period tidak terpengaruh; versi pertama tanpa Effective From tidak menghalangi Fiscal Year Start

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "13 accounting periods will be rebuilt." dan "12 accounting periods will be rebuilt."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PB (TC-FA-PREF-176-361) untuk TC-FA-PREF-219 dan 220: Preferences nilai awal (PB-1) dan kelas Tax Depreciation Class `Commercial Building` dengan versi kedua Effective From 01/07/26 (PB-8); tidak terkunci.
- Data: seri PC (TC-FA-PREF-362-621) untuk TC-FA-PREF-579 dan 580: Fiscal Year Start tersimpan January, First Accounting Period tersimpan Mar 2026; TC-FA-PREF-579 dengan satu kelas Tax Depreciation Class berversi kedua ber-Effective From (PC-3) dan belum ada transaksi bertanggal; TC-FA-PREF-580 dengan Tax Depreciation Class seed dan kelas buatan pengguna masing-masing hanya versi pertama tanpa Effective From (PC-1).
- Seri fixture PA, PB, dan PC bernilai awal setara (PA-2, PB-1, PC-1); spec yang memuat TC dari lebih dari satu seri men-seed ulang lewat API di antara TC sesuai Precondition TC.
- Kemampuan teknis: modul Accounting Period (`settings-accounting-period/`) dibuka untuk membaca daftar periode pada TC-FA-PREF-579. Baca state Preferences, periode akuntansi, dan akun Chart of Accounts di server (kemampuan baca state BE) disediakan tim FE/BE tanpa endpoint karangan; dipakai untuk Expected "tidak ada yang tersimpan".
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-219: Save mengubah Fiscal Year Start ditolak V-09 saat sudah ada versi Tax Depreciation Class ber-Effective From

1. Ubah Select Fiscal Year Start dari "January" menjadi "April"
2. Klik `[Save changes]`
3. Klik `[Save]` pada dialog D-01
4. Verifikasi dialog D-01 ditutup
5. Verifikasi form tetap memuat seluruh perubahan yang belum disimpan
6. Verifikasi caption "Fiscal year start cannot be changed because tax depreciation class versions already exist." tampil pada Select Fiscal Year Start
7. Verifikasi tidak ada toast dan tidak ada dialog D-03
8. Klik `[Cancel]`

### TC-FA-PREF-220: Save hanya mengubah First Accounting Period tidak terpengaruh versi Tax Depreciation Class ber-Effective From

9. Ubah Select bulan First Accounting Period dari "March" menjadi "January"
10. Klik `[Save changes]`
11. Klik `[Save]` pada dialog D-01
12. Verifikasi dialog D-01 tertutup
13. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
14. Verifikasi tidak ada caption V-09
15. Verifikasi Select bulan First Accounting Period menampilkan "January"

### TC-FA-PREF-579: Save hanya First Accounting Period berhasil walau ada versi Tax Depreciation Class ber-Effective From (seri PC)

16. Siapkan Preferences nilai awal PC-1 dan seed PC-3 (satu kelas Tax Depreciation Class berversi kedua ber-Effective From; belum ada transaksi bertanggal) lewat seed API hingga tersimpan
17. Buka ulang Fixed Asset > Settings > Accounting > Preferences
18. Pilih bulan "January" dan tahun "2026" pada Select First Accounting Period
19. Klik `[Save changes]`
20. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "12 accounting periods will be rebuilt.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
21. Klik `[Save]` pada dialog "Save Changes"
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Buka daftar periode di modul Accounting Period (`settings-accounting-period/`) dan atur ukuran halaman ke 25
24. Verifikasi Accounting Period memuat 12 periode Jan 2026 sampai Dec 2026 berstatus Open

### TC-FA-PREF-580: Versi pertama Tax Depreciation Class tanpa Effective From tidak menghalangi perubahan Fiscal Year Start (seri PC)

25. Siapkan Preferences nilai awal PC-1 (Fiscal Year Start January) dan Tax Depreciation Class seed serta kelas buatan pengguna hanya berversi pertama tanpa Effective From lewat seed API hingga tersimpan
26. Buka Fixed Asset > Settings > Accounting > Preferences
27. Pilih "April" pada Select Fiscal Year Start
28. Klik `[Save changes]`
29. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "13 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
30. Klik `[Save]` pada dialog "Save Changes"
31. Verifikasi toast "Success, accounting preferences have been saved." tampil
32. Verifikasi tidak ada caption V-09 pada Fiscal Year Start

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 8; memulihkan state server lewat seed/API sebelum TC berikutnya: langkah 16, 25; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 17; berpindah modul atau kembali ke halaman Preferences: langkah 23, 26.
- Urutan: TC-FA-PREF-219 (Save ditolak) lebih dulu, lalu TC-FA-PREF-220, 579, dan 580 (Save sukses) sesuai S-10. TC-FA-PREF-579 berpindah ke modul Accounting Period; blok TC-FA-PREF-580 diawali langkah kembali ke halaman Preferences (S-14).
- Temuan untuk QA:
  - TC-FA-PREF-219 dan 220 tidak mencantumkan isi dialog D-01 pada Expected; spec tidak mengasersinya.
  - TC-FA-PREF-220 Post Condition b (periode akuntansi dibangun ulang dari Jan 2026) tanpa langkah observasi; tidak diasersi.
  - Seri PB (TC-FA-PREF-219 dan 220) dan seri PC (TC-FA-PREF-579 dan 580) dicampur dalam satu spec; nilai awal setara sehingga hanya seed varian Tax Depreciation Class yang diganti antar-blok.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, periode dibangun ulang, entri log) tidak diasersi; Post Condition "tidak ada entri log baru" dicatat sebagai rujukan ke spec absence (S-05) dan tidak diklaim teruji di spec ini.
