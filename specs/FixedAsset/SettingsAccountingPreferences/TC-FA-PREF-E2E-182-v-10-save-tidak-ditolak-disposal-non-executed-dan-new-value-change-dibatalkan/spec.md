---
id: TC-FA-PREF-E2E-182-v-10-save-tidak-ditolak-disposal-non-executed-dan-new-value-change-dibatalkan
title: "V-10: Save First Accounting Period tidak ditolak oleh baris Disposal Waiting for Execution, Waiting for Approval, Rejected, Canceled, dan New value change yang dibatalkan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-635
  - TC-FA-PREF-636
  - TC-FA-PREF-639
sourceRules: ["D-01", "PV-04", "F-FAPREF-01.k23", "V-10", "FAPREF-LOGIC-02n", "E-FAPREF-42", "T-01"]
smoke: []
dependsOn: []
trace:
  "D-01": [3, 12, 21]
  "PV-04": [3, 12, 21]
  "F-FAPREF-01.k23": [6, 15, 24]
  "V-10": [7, 16, 25]
  "FAPREF-LOGIC-02n": [7, 16, 25]
  "E-FAPREF-42": [7, 16, 25]
  "T-01": [5, 14, 23]
coverage:
  web: automated
---

# V-10: Save First Accounting Period tidak ditolak oleh baris Disposal Waiting for Execution, Waiting for Approval, Rejected, Canceled, dan New value change yang dibatalkan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas (28 Oktober 2026 pukul 10:00 Asia/Jakarta), dasar hitungan "The period calendar will have 7 accounting periods."; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Data: seri PC (TC-FA-PREF-362-643), company `PT Contoh Konstruksi` plan Growth (PC-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong), belum ada posting penyusutan. Catatan per TC:
  - TC-FA-PREF-635 (PC-29): satu baris Disposal berstatus Waiting for Execution bertanggal 20 April 2026 dan satu baris Disposal berstatus Executed dengan Execution date 15 Juni 2026 (M = Jun 2026).
  - TC-FA-PREF-636 (PC-30): tiga baris Disposal berstatus Waiting for Approval (10 April 2026), Rejected (12 April 2026), dan Canceled (14 April 2026), dan satu baris Disposal berstatus Executed dengan Execution date 15 Juni 2026 (M = Jun 2026).
  - TC-FA-PREF-639 (PC-31): satu New value change berstatus dibatalkan dengan Effective period May 2026; tidak ada baris Disposal Executed atau Posted dan tidak ada New value change lain.
- Fixture hook `before` membentuk keadaan TC-FA-PREF-635 (PC-29); fixture TC berikutnya dibentuk lewat seed pada langkah penghubung (langkah 8 dan 17). Seri PC (PC-29 sampai PC-31) dan data modul pemilik (Disposal dan New value change di modul Asset) disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Kemampuan teknis (disediakan tim FE/BE): seed fixture di atas dan pemulihan Preferences lewat API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`. Hook `after` spec ini memulihkan state server yang diubah spec ke nilai awal PC-1 dan menghapus fixture PC-29 sampai PC-31.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-635: Baris Disposal Waiting for Execution bertanggal lebih awal tidak menolak Save

1. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
2. Klik `[Save changes]`
3. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
4. Klik `[Save]` pada dialog "Save Changes"
5. Verifikasi toast "Success, accounting preferences have been saved." tampil
6. Verifikasi First Accounting Period menampilkan Jun 2026
7. Verifikasi tidak ada caption V-10 pada First Accounting Period

### TC-FA-PREF-636: Baris Disposal Waiting for Approval, Rejected, dan Canceled bertanggal lebih awal tidak menolak Save

8. Seed ulang Preferences ke nilai awal PC-1 (First Accounting Period Mar 2026) dan fixture PC-30 (tiga baris Disposal Waiting for Approval 10 April 2026, Rejected 12 April 2026, dan Canceled 14 April 2026, serta satu baris Disposal Executed 15 Juni 2026) lewat API hingga tersimpan
9. Buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
11. Klik `[Save changes]`
12. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
13. Klik `[Save]` pada dialog "Save Changes"
14. Verifikasi toast "Success, accounting preferences have been saved." tampil
15. Verifikasi First Accounting Period menampilkan Jun 2026
16. Verifikasi tidak ada caption V-10 pada First Accounting Period

### TC-FA-PREF-639: New value change yang dibatalkan tidak menahan perubahan First Accounting Period

17. Seed ulang Preferences ke nilai awal PC-1 (First Accounting Period Mar 2026) dan fixture PC-31 (satu New value change dibatalkan dengan Effective period May 2026, tanpa baris Disposal Executed atau Posted) lewat API hingga tersimpan
18. Buka ulang Fixed Asset > Settings > Accounting > Preferences
19. Pilih bulan "June" dan tahun "2026" pada Select First Accounting Period
20. Klik `[Save changes]`
21. Verifikasi dialog "Save Changes" (severity warning) tampil dengan daftar bullet: "The period calendar will have 7 accounting periods.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
22. Klik `[Save]` pada dialog "Save Changes"
23. Verifikasi toast "Success, accounting preferences have been saved." tampil
24. Verifikasi First Accounting Period menampilkan Jun 2026
25. Verifikasi tidak ada caption V-10 pada First Accounting Period

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Ketiga TC adalah TC UI (Save lewat form); tidak ada TC hanya-BE dan tidak ada asersi respons API langsung di spec ini.
- Langkah penghubung (S-03): memulihkan state server lewat seed API dan membentuk fixture TC berikutnya sebelum TC itu: langkah 8 dan 17; membuka ulang halaman Preferences agar form memuat nilai tersimpan: langkah 9 dan 18.
- Ketiga TC berakhir dengan First Accounting Period tersimpan Jun 2026 dan tidak ada form dirty; tidak ada langkah `[Cancel]`. Pemulihan akhir ke nilai awal PC-1 dilakukan hook `after`.
- Urutan TC mengikuti urutan TC (635, 636, 639); semuanya Save yang berhasil sehingga tidak ada Save ditolak yang perlu didahulukan (S-10).
- Rujukan keputusan: aturan V-10 / FAPREF-LOGIC-02n didefinisikan ulang pada Changelog 2026-11-23 (V-10 dan threshold): baris Disposal Waiting for Approval, Waiting for Execution, Rejected, dan Canceled serta New value change yang dibatalkan tidak menahan First Accounting Period.
- Temuan untuk QA:
  - TC-FA-PREF-635, 636, dan 639 menulis langkah "Amati dialog Save Changes dan klik [Save]"; spec memecahnya menjadi Verifikasi dialog lalu klik `[Save]`.
  - TC-FA-PREF-635, 636, dan 639 menulis First Accounting Period tersimpan "Jun 2026" pada Post Condition tanpa langkah observasi tersendiri; Expected c diasersi dan Post Condition tidak diasersi terpisah.
  - TC-FA-PREF-639 d tidak menjelaskan cara New value change berstatus dibatalkan dibentuk (PC-31); cara seed perlu konfirmasi FE.
  - TC-FA-PREF-635 dan 636 menyebut tanggal baris Disposal non-Executed (20 April, 10, 12, dan 14 April 2026) tanpa menyebut kolom tanggalnya (Execution date atau tanggal pengajuan); spec menulis "bertanggal" mengikuti TC.
  - Post Condition TC yang tidak punya langkah observasi di TC tidak diasersi; tidak ada Expected log, sehingga tidak ada rujukan ke spec absence (S-05).
  - TC-FA-PREF-632 sampai 634 ada di spec 181; TC-FA-PREF-637 dan 638 di spec 183; TC-FA-PREF-640 dan 641 di spec 184.
