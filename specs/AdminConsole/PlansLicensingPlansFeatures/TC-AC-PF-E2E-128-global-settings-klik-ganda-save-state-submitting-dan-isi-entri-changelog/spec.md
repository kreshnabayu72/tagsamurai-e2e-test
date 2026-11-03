---
id: TC-AC-PF-E2E-128-global-settings-klik-ganda-save-state-submitting-dan-isi-entri-changelog
title: "Global Settings: Klik Ganda Save, State Submitting, dan Isi Entri Changelog Global Settings"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-300
  - TC-AC-PF-703
  - TC-AC-PF-531
coverage:
  web: automated
---

# Global Settings: Klik Ganda Save, State Submitting, dan Isi Entri Changelog Global Settings

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata untuk menunda respons Save pada TC-AC-PF-703).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 9, 18, dan 38). Efek yang tersisa: Save menambah entri Changelog Global Settings, System Log, dan Activity Log yang bersifat permanen (tidak dapat dihapus lewat UI).
- Baseline: jumlah baris Changelog Global Settings dengan Action `Edit` untuk Field `Max custom fields per asset name` dicatat pada langkah 2 lewat kemampuan baca (audit trail permanen; S-12, bagian 8b butir 10). Baseline per Field untuk `Max custom fields per asset name` dan `Max depreciation methods (Multi Depreciation tier)` dicatat pada langkah 19 sebelum kedua `[Save]` (langkah 20 dan 21). Changelog Global Settings tidak dibersihkan oleh spec (audit trail permanen, tidak ada hapus lewat UI); bila log perlu disetel atau dibersihkan sebelum spec, itu dilakukan fixture BE yang disediakan tim FE/BE di hook `before`, dan asersi tetap memakai selisih terhadap baseline.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog Global Settings per Field; `Spectra.intercept` parsial untuk menunda respons Save Global FAMS Settings dan melepasnya (TC-AC-PF-703); intercept dilepas segera sesudah asersi (S-09).
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-300: Klik ganda cepat pada Save Global Settings

1. Klik tab `Global Settings`
2. Catat jumlah baris Changelog Global Settings dengan Action `Edit` dan Field `Max custom fields per asset name` sebagai baseline (kemampuan baca)
3. Ubah `Max custom fields per asset name` menjadi `8`
4. Klik `[Save]` dua kali dengan cepat
5. Verifikasi Satu toast sukses: "Success, global FAMS settings has been saved."
6. Klik ikon Changelog di Card
7. Verifikasi Jumlah baris Action `Edit` untuk Field `Max custom fields per asset name` bertambah tepat satu dari baseline langkah 2
8. Tutup modal Changelog
9. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-703: Save berlangsung, tombol loading dan kontrol dibekukan

10. Pasang intercept yang menunda respons Save Global FAMS Settings
11. Ubah `Max custom fields per asset name` menjadi `9`
12. Klik `[Save]`, lalu amati tab sebelum respons diterima
13. Verifikasi Tombol `[Save]` menampilkan indikator loading
14. Verifikasi Tombol `[Save]` berstatus Disabled
15. Verifikasi Kedua input dan tombol `[Clear Field]` tidak dapat dipakai selama request berlangsung
16. Lepas tahanan respons dan lepas intercept
17. Tunggu aksi selesai (tombol `[Save]` aktif kembali)
18. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-531: Save Global FAMS Settings menulis entri Edit per setting di modal Changelog Global Settings

19. Catat jumlah baris Changelog Global Settings dengan Action `Edit` untuk Field `Max custom fields per asset name` dan untuk Field `Max depreciation methods (Multi Depreciation tier)` sebagai baseline per Field (kemampuan baca)
20. Ubah `Max custom fields per asset name` menjadi `8`, lalu klik `[Save]`
21. Ubah `Max depreciation methods (Multi Depreciation tier)` menjadi `4`, lalu klik `[Save]`
22. Klik ikon Changelog di Card
23. Verifikasi Jumlah baris Action `Edit` untuk Field `Max custom fields per asset name` bertambah tepat satu dari baseline langkah 19
24. Verifikasi Entri Action `Edit`, Field `Max custom fields per asset name` (5 → 8)
25. Verifikasi Jumlah baris Action `Edit` untuk Field `Max depreciation methods (Multi Depreciation tier)` bertambah tepat satu dari baseline langkah 19
26. Verifikasi Entri Action `Edit`, Field `Max depreciation methods (Multi Depreciation tier)` (2 → 4)
27. Tutup modal Changelog
28. Klik tab `Default`
29. Klik ikon Changelog pada toolbar tab Default
30. Verifikasi Modal Changelog Default tampil dengan entri sebelumnya (anchor)
31. Verifikasi Modal Changelog Default tidak memuat entri Field `Max custom fields per asset name` maupun `Max depreciation methods (Multi Depreciation tier)`
32. Tutup modal Changelog
33. Klik tab `Custom`
34. Klik ikon Changelog pada toolbar tab Custom
35. Verifikasi Modal Changelog Custom tampil dengan entri sebelumnya (anchor)
36. Verifikasi Modal Changelog Custom tidak memuat entri Field `Max custom fields per asset name` maupun `Max depreciation methods (Multi Depreciation tier)`
37. Tutup modal Changelog
38. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition (langkah 1), pemulihan Global FAMS Settings (langkah 9, 18, 38), pemasangan dan pelepasan intercept (langkah 10 dan 16), dan penutupan modal Changelog.
- Pembagian TC lintas spec: TC-AC-PF-290 sampai TC-AC-PF-293 ada di spec 115; TC-AC-PF-297 dan TC-AC-PF-298 ada di spec 129; TC-AC-PF-520 sampai TC-AC-PF-524 ada di spec 121.
- Asersi "bertambah tepat satu" (langkah 7, 23, dan 25) adalah asersi jumlah terhadap baseline (S-12), bukan spec absence. Asersi "tidak memuat entri" pada langkah 31 dan 36 didahului anchor positif (modal tampil dengan entri sebelumnya).
- Intercept menunda respons untuk mengamati state loading (bukan kegagalan yang dipaksakan), sehingga TC-AC-PF-703 tidak masuk kelas b dan tidak membutuhkan butir pengecualian.
- Alasan melewati sekitar 35 langkah (38 langkah): ketiga blok berdiri pada satu halaman dan satu dataset (Global FAMS Settings), tanpa kelas harness lain; blok baca-log TC-AC-PF-531 (langkah 22 sampai 27, 28 sampai 32, dan 33 sampai 37) mengikuti pola buka surface lalu Verifikasi, yang tidak dihitung pada ambang menurut bagian 3 prinsip 13. Tanpa blok itu spec ini 22 langkah.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - Post Condition TC-AC-PF-703 ("Tidak ada perubahan data") bertentangan dengan alur: sesudah respons yang ditunda dilepas, Save dengan nilai `9` tetap diproses server. Post Condition tanpa langkah observasi tidak diasersi (S-01); spec memulihkan nilai lewat Fixture BE pada langkah 18.
  - TC-AC-PF-531 Expected butir b ("Entri tidak muncul di modal Changelog Default maupun Custom") tidak menyatakan cara menyaring entri Global Settings dari modal lain; spec memeriksa tidak adanya entri dengan Field kedua setting tersebut.
  - TC-AC-PF-300 Expected butir b ("tepat satu baris Edit") tidak menyatakan baseline; spec memakai selisih terhadap baseline (S-12).
