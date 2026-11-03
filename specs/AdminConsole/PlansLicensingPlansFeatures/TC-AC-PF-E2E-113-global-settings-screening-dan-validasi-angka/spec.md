---
id: TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka
title: "Global Settings: Screening Tab dan Validasi Angka Max custom fields dan Max depreciation methods"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-284
  - TC-AC-PF-285
  - TC-AC-PF-286
  - TC-AC-PF-287
  - TC-AC-PF-288
  - TC-AC-PF-289
coverage:
  web: automated
---

# Global Settings: Screening Tab dan Validasi Angka Max custom fields dan Max depreciation methods

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA). General Settings baseline (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton dan tidak dapat dimiliki spec (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 16). Efek yang tersisa: entri Changelog Global Settings, System Log, dan Activity Log bertambah dan bersifat permanen (tidak dapat dihapus lewat UI).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca nilai tersimpan Global FAMS Settings untuk asersi "nilai tersimpan"; dialog `beforeunload` bawaan browser dapat dikonfirmasi atau dibatalkan oleh spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-284: Screening tab Global Settings

1. Klik tab `Global Settings`
2. Susuri halaman dari atas ke bawah
3. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Global Settings` (segmen pertama dan terakhir statis; `Plans & Features` dapat diklik)
4. Verifikasi Tab `Default | Custom | Global Settings (aktif)`
5. Verifikasi Tanpa sub-tab Active/Archive
6. Verifikasi Card berjudul `FAMS` dengan subjudul `Platform-wide limits that apply to all FAMS plans.`
7. Verifikasi Ikon Changelog di pojok kanan atas Card
8. Verifikasi Number input `Max custom fields per asset name` bernilai `5`
9. Verifikasi Number input `Max depreciation methods (Multi Depreciation tier)` bernilai `2`
10. Verifikasi Footer memuat `[Clear Field]` dan `[Save]`

### TC-AC-PF-285: Validasi Max custom fields per asset name

11. Isi `Max custom fields per asset name` dengan `0`, lalu klik `[Save]`
12. Verifikasi Pesan inline `Value must be a whole number of at least 1` tampil setelah Save
13. Verifikasi Nilai tersimpan `Max custom fields per asset name` tetap `5` (tidak ada perubahan tersimpan)
14. Ubah `Max custom fields per asset name` menjadi `1`, lalu klik `[Save]`
15. Verifikasi Toast sukses: "Success, global FAMS settings has been saved."
16. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-286: Validasi Max depreciation methods (Multi Depreciation tier)

17. Isi `Max depreciation methods (Multi Depreciation tier)` dengan `1`, lalu klik `[Save]`
18. Verifikasi Pesan inline `Value must be a whole number of at least 2` tampil setelah Save
19. Verifikasi Nilai tersimpan `Max depreciation methods (Multi Depreciation tier)` tetap `2` (tidak ada perubahan tersimpan)
20. Ubah `Max depreciation methods (Multi Depreciation tier)` menjadi `2`, lalu klik `[Save]`
21. Verifikasi Toast sukses: "Success, global FAMS settings has been saved."

### TC-AC-PF-287: Nilai desimal pada Max custom fields per asset name

22. Isi `Max custom fields per asset name` dengan `2.5`, lalu klik `[Save]`
23. Verifikasi Pesan inline `Value must be a whole number of at least 1` tampil
24. Verifikasi Nilai tersimpan `Max custom fields per asset name` tetap `5`

### TC-AC-PF-288: Nilai desimal pada Max depreciation methods (Multi Depreciation tier)

25. Klik `[Clear Field]`
26. Isi `Max depreciation methods (Multi Depreciation tier)` dengan `3.5`, lalu klik `[Save]`
27. Verifikasi Pesan inline `Value must be a whole number of at least 2` tampil
28. Verifikasi Nilai tersimpan `Max depreciation methods (Multi Depreciation tier)` tetap `2`

### TC-AC-PF-289: Input number hanya menerima karakter angka

29. Klik `[Clear Field]`
30. Ketik `abc` pada `Max custom fields per asset name` dan pada `Max depreciation methods (Multi Depreciation tier)`
31. Verifikasi Huruf tidak masuk ke `Max custom fields per asset name` (nilai tetap `5`)
32. Verifikasi Huruf tidak masuk ke `Max depreciation methods (Multi Depreciation tier)` (nilai tetap `2`)

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition tiap TC (langkah 1), pemulihan Global FAMS Settings lewat Fixture BE dan muat ulang halaman (langkah 16), dan klik `[Clear Field]` untuk membuang input tidak valid sebelum TC berikutnya (langkah 25 dan 29, S-09).
- Pembagian TC lintas spec: TC-AC-PF-290 sampai TC-AC-PF-293 ada di spec 115; TC-AC-PF-294 sampai TC-AC-PF-296 ada di spec 116.
- Temuan untuk QA:
  - TC-AC-PF-286 Expected butir b mengharapkan toast sukses saat nilai `2` disimpan, padahal nilai tersimpan awal sudah `2`; TC-AC-PF-293 menyatakan Save tanpa perubahan menghasilkan toast netral "No changes to save." Spec mengikuti TC-AC-PF-286 (langkah 21); perlu konfirmasi QA mana yang benar.
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Butir Lampiran A-6 menyebut plan Pre-setup, bukan Global FAMS Settings. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-PF-285 ("Max custom fields per asset name bernilai 1") dan TC-AC-PF-286 ("Max depreciation methods (Multi Depreciation tier) bernilai 2").
  - TC-AC-PF-287 dan TC-AC-PF-288 tidak menyatakan cara membaca "nilai tersimpan"; spec memakai kemampuan baca nilai tersimpan yang disediakan tim FE/BE tanpa endpoint karangan.
