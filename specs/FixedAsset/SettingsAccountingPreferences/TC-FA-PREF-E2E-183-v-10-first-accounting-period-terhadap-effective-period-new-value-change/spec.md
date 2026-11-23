---
id: TC-FA-PREF-E2E-183-v-10-first-accounting-period-terhadap-effective-period-new-value-change
title: "V-10: First Accounting Period terhadap Effective period New value change May 2026 (bulan setelah ditolak, bulan yang sama diterima)"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-637
  - TC-FA-PREF-638
sourceRules: ["D-01", "PV-04", "F-FAPREF-01.k23", "V-10", "FAPREF-LOGIC-02n", "E-FAPREF-42", "T-01"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 13]
  "PV-04": [3, 13]
  "F-FAPREF-01.k23": [5, 7, 16]
  "V-10": [6, 17]
  "FAPREF-LOGIC-02n": [6, 17]
  "E-FAPREF-42": [6, 17]
  "T-01": [15]
coverage:
  web: automated
---

# V-10: First Accounting Period terhadap Effective period New value change May 2026 (bulan setelah ditolak, bulan yang sama diterima)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas (28 Oktober 2026 pukul 10:00 Asia/Jakarta), dasar hitungan "The period calendar will have 7 accounting periods." dan "The period calendar will have 8 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PC (TC-FA-PREF-362-643), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), belum ada posting penyusutan. Satu New value change yang tidak dibatalkan dengan Effective period May 2026 (PC-23); tidak ada baris Disposal Executed atau Posted. Kedua TC memakai fixture PC-23 yang sama; fixture dibentuk di hook `before`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): baca state Preferences di server (First Accounting Period tersimpan), dipakai untuk Expected "tidak ada yang tersimpan"; seed New value change (data modul pemilik, `ASTD-LOGIC-26`).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal PC-1 dan menghapus fixture PC-23.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-637: Ubah First Accounting Period ke bulan setelah Effective period New value change ditolak dengan caption V-10

1. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
4. Klik `[Save]` pada dialog "Save Changes"
5. Verifikasi dialog "Save Changes" tertutup
6. Verifikasi caption "First accounting period cannot be later than May 2026, the earliest disposal or value change." tampil pada field First Accounting Period
7. Verifikasi form tetap memuat Jun 2026 sebagai perubahan yang belum disimpan
8. Verifikasi tidak ada toast
9. Verifikasi tidak ada yang tersimpan: First Accounting Period tersimpan tetap Mar 2026
10. Klik `[Cancel]`

### TC-FA-PREF-638: Ubah First Accounting Period ke bulan yang sama dengan Effective period New value change berhasil

11. Pilih bulan "May" dan tahun "2026" pada Select First Accounting Period
12. Klik `[Save changes]`
13. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 8 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
14. Klik `[Save]` pada dialog "Save Changes"
15. Verifikasi toast "Success, accounting preferences have been saved." tampil
16. Verifikasi First Accounting Period menampilkan May 2026
17. Verifikasi tidak ada caption V-10 pada First Accounting Period

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Kedua TC adalah TC UI (Save lewat form); tidak ada TC hanya-BE dan tidak ada asersi respons API langsung di spec ini.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 10. Kedua TC memakai fixture PC-23 yang sama dan Save TC-FA-PREF-637 ditolak sehingga First Accounting Period tetap Mar 2026; tidak ada seed ulang atau buka ulang halaman di antara keduanya.
- Urutan TC mengikuti urutan TC (637 lalu 638): Save yang ditolak lebih dulu, lalu Save yang berhasil (S-10).
- Rujukan keputusan: aturan V-10 / FAPREF-LOGIC-02n didefinisikan ulang pada Changelog 2026-11-23 (V-10 dan threshold): New value change yang tidak dibatalkan menahan First Accounting Period pada bulan Effective period; bulan yang sama diterima.
- Temuan untuk QA:
  - TC-FA-PREF-637 dan 638 menulis langkah "Amati dialog Save Changes dan klik [Save]"; spec memecahnya menjadi Verifikasi dialog lalu klik `[Save]`.
  - TC-FA-PREF-637 Expected d ("Tidak ada toast dan tidak ada yang tersimpan") memuat dua klausa dan ditulis dua `Verifikasi` (langkah 8 dan 9, S-01); langkah 8 memakai caption V-10 (langkah 6) sebagai anchor positif.
  - TC-FA-PREF-637 dan 638 menulis First Accounting Period tersimpan pada Post Condition tanpa langkah observasi tersendiri (TC-FA-PREF-638: "May 2026"); Expected c TC-FA-PREF-638 diasersi (langkah 16) dan Post Condition tidak diasersi terpisah.
  - TC-FA-PREF-637 menyebut caption dengan bulan penahan "May 2026" pada Effective period New value change May 2026; format bulan penahan "[MMM YYYY]" mengikuti TC.
  - Post Condition TC yang tidak punya langkah observasi di TC tidak diasersi; tidak ada Expected log, sehingga tidak ada rujukan ke spec absence (S-05).
  - TC-FA-PREF-632 sampai 634 ada di spec 181; TC-FA-PREF-635, 636, dan 639 di spec 182; TC-FA-PREF-640 dan 641 di spec 184.
