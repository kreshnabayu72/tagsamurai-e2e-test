---
id: TC-FA-PREF-E2E-184-v-10-ditolak-setelah-disposal-posted-dan-bulan-terawal-di-antara-disposal-executed-dan-new-value-change
title: "V-10: First Accounting Period ditolak setelah Execution date Disposal Posted dan setelah bulan terawal di antara Disposal Executed dan New value change"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-640
  - TC-FA-PREF-641
sourceRules: ["D-01", "PV-04", "F-FAPREF-01.k23", "V-10", "FAPREF-LOGIC-02n", "E-FAPREF-42"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 15]
  "PV-04": [3, 15]
  "F-FAPREF-01.k23": [5, 7, 17, 19]
  "V-10": [6, 18]
  "FAPREF-LOGIC-02n": [6, 18]
  "E-FAPREF-42": [6, 18]
coverage:
  web: automated
---

# V-10: First Accounting Period ditolak setelah Execution date Disposal Posted dan setelah bulan terawal di antara Disposal Executed dan New value change

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas (28 Oktober 2026 pukul 10:00 Asia/Jakarta), dasar hitungan "The period calendar will have 7 accounting periods." dan "The period calendar will have 8 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PC (TC-FA-PREF-362-643), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), belum ada posting penyusutan. Catatan per TC:
  - TC-FA-PREF-640 (PC-24): satu baris Disposal berstatus Posted dengan Execution date 15 Mei 2026; tidak ada New value change.
  - TC-FA-PREF-641 (PC-25): satu baris Disposal berstatus Executed dengan Execution date 15 Juni 2026 dan satu New value change yang tidak dibatalkan dengan Effective period Apr 2026; bulan terawal M = Apr 2026.
- Fixture hook `before` membentuk keadaan TC-FA-PREF-640 (PC-24); fixture TC-FA-PREF-641 dibentuk lewat seed pada langkah penghubung (langkah 11). Seri PC (PC-24 dan PC-25) dan data modul pemilik (Disposal dan New value change di modul Asset) disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): baca state Preferences di server (First Accounting Period tersimpan), dipakai untuk Expected "tidak ada yang tersimpan"; seed fixture di atas dan pemulihan Preferences lewat API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal PC-1 dan menghapus fixture PC-24 dan PC-25.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-640: Ubah First Accounting Period ke bulan setelah Execution date baris Disposal Posted ditolak dengan caption V-10

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

### TC-FA-PREF-641: Bulan penahan adalah bulan terawal di antara baris Disposal Executed dan New value change

11. Seed ulang Preferences ke nilai awal PC-1 (First Accounting Period Mar 2026) dan fixture PC-25 (satu baris Disposal Executed 15 Juni 2026 dan satu New value change yang tidak dibatalkan dengan Effective period Apr 2026) lewat API hingga tersimpan
12. Buka ulang Fixed Asset > Settings > Accounting > Preferences
13. Pilih bulan "May" dan tahun "2026" pada Select First Accounting Period
14. Klik `[Save changes]`
15. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 8 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
16. Klik `[Save]` pada dialog "Save Changes"
17. Verifikasi dialog "Save Changes" tertutup
18. Verifikasi caption "First accounting period cannot be later than Apr 2026, the earliest disposal or value change." tampil pada field First Accounting Period
19. Verifikasi form tetap memuat May 2026 sebagai perubahan yang belum disimpan
20. Verifikasi tidak ada toast
21. Verifikasi tidak ada yang tersimpan: First Accounting Period tersimpan tetap Mar 2026
22. Klik `[Cancel]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Kedua TC adalah TC UI (Save lewat form, penolakan server tampil sebagai caption); tidak ada TC hanya-BE dan tidak ada asersi respons API langsung di spec ini.
- Langkah penghubung (S-03): mengembalikan form dirty ke nilai tersimpan dengan `[Cancel]` (S-09): langkah 10 dan 22; memulihkan state server dan membentuk fixture TC berikutnya lewat seed/API: langkah 11; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 12.
- Urutan TC mengikuti urutan TC (640 lalu 641); keduanya Save yang ditolak sehingga tidak ada Save berhasil yang perlu diakhirkan (S-10).
- Rujukan keputusan: aturan V-10 / FAPREF-LOGIC-02n didefinisikan ulang pada Changelog 2026-11-23 (V-10 dan threshold): baris Disposal Executed atau Posted (tanggal acuan Execution date) dan New value change yang tidak dibatalkan (tanggal acuan Effective period) menahan First Accounting Period; pesan memuat bulan penahan yaitu bulan terawal di antara keduanya.
- Temuan untuk QA:
  - TC-FA-PREF-640 dan 641 menulis langkah "Amati dialog Save Changes dan klik [Save]"; spec memecahnya menjadi Verifikasi dialog lalu klik `[Save]`.
  - TC-FA-PREF-640 dan 641 Expected d ("Tidak ada toast dan tidak ada yang tersimpan") memuat dua klausa dan ditulis dua `Verifikasi` (langkah 8 dan 9, 20 dan 21, S-01); `Verifikasi` absence toast memakai caption V-10 sebagai anchor positif (langkah 6 dan 18).
  - TC-FA-PREF-640 dan 641 menulis First Accounting Period tersimpan tetap Mar 2026 pada Post Condition; Expected d menyatakan "tidak ada yang tersimpan" dan diasersi lewat kemampuan baca state server, nilai Post Condition tidak diasersi terpisah.
  - TC-FA-PREF-641 memakai format bulan penahan "Apr 2026" pada caption padahal Execution date Disposal Executed 15 Juni 2026 dan Effective period New value change Apr 2026; spec mengikuti TC.
  - Post Condition TC yang tidak punya langkah observasi di TC tidak diasersi; tidak ada Expected log, sehingga tidak ada rujukan ke spec absence (S-05).
  - TC-FA-PREF-632 sampai 634 ada di spec 181; TC-FA-PREF-635, 636, dan 639 di spec 182; TC-FA-PREF-637 dan 638 di spec 183.
