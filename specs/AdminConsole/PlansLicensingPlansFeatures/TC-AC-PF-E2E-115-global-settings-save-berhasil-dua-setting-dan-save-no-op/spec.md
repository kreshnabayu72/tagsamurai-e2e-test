---
id: TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op
title: "Global Settings: Save Berhasil Per Setting dan Sekaligus serta Save Tanpa Perubahan (No-Op)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-290
  - TC-AC-PF-291
  - TC-AC-PF-292
  - TC-AC-PF-293
coverage:
  web: automated
---

# Global Settings: Save Berhasil Per Setting dan Sekaligus serta Save Tanpa Perubahan (No-Op)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA). General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton dan tidak dapat dimiliki spec (S-06, pengecualian 2026-10-30): nilai awal `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 8, 15, dan 26). Efek yang tersisa: spec ini menambah entri Changelog Global Settings, System Log, dan Activity Log yang bersifat permanen (tidak dapat dihapus lewat UI).
- Baseline Changelog Global Settings untuk asersi "tidak ada entri baru" (TC-AC-PF-293) dicatat pada langkah 27 lewat kemampuan baca jumlah entri (audit trail permanen; S-12, bagian 8b butir 10).
- Baseline per Field untuk asersi "bertambah tepat satu" (TC-AC-PF-292) dicatat pada langkah 16 sebelum `[Save]` langkah 18. Changelog Global Settings tidak dibersihkan oleh spec (audit trail permanen, tidak ada hapus lewat UI); bila log perlu disetel atau dibersihkan sebelum spec, itu dilakukan fixture BE yang disediakan tim FE/BE di hook `before`, dan asersi spec tetap memakai selisih terhadap baseline.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca jumlah entri Changelog Global Settings.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-290: Save perubahan Max custom fields per asset name

1. Klik tab `Global Settings`
2. Ubah `Max custom fields per asset name` dari `5` menjadi `8`
3. Klik `[Save]`
4. Verifikasi Toast sukses: "Success, global FAMS settings has been saved."
5. Tekan F5
6. Verifikasi Setelah refresh `Max custom fields per asset name` bernilai `8`
7. Verifikasi Setelah refresh `Max depreciation methods (Multi Depreciation tier)` tidak berubah (`2`)
8. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-291: Save perubahan Max depreciation methods (Multi Depreciation tier)

9. Ubah `Max depreciation methods (Multi Depreciation tier)` dari `2` menjadi `4`
10. Klik `[Save]`
11. Verifikasi Toast sukses: "Success, global FAMS settings has been saved."
12. Tekan F5
13. Verifikasi Setelah refresh `Max depreciation methods (Multi Depreciation tier)` bernilai `4`
14. Verifikasi Setelah refresh `Max custom fields per asset name` tidak berubah (`5`)
15. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-292: Save kedua setting sekaligus

16. Catat jumlah baris Changelog Global Settings dengan Action `Edit` untuk Field `Max custom fields per asset name` dan untuk Field `Max depreciation methods (Multi Depreciation tier)` sebagai baseline per Field (kemampuan baca)
17. Ubah `Max custom fields per asset name` menjadi `10` dan `Max depreciation methods (Multi Depreciation tier)` menjadi `4`
18. Klik `[Save]`
19. Verifikasi Satu toast sukses: "Success, global FAMS settings has been saved."
20. Klik ikon Changelog di pojok kanan atas Card
21. Verifikasi Jumlah baris Action `Edit` untuk Field `Max custom fields per asset name` bertambah tepat satu dari baseline langkah 16
22. Verifikasi Changelog memuat baris Action `Edit`, Field `Max custom fields per asset name` (5 → 10)
23. Verifikasi Jumlah baris Action `Edit` untuk Field `Max depreciation methods (Multi Depreciation tier)` bertambah tepat satu dari baseline langkah 16
24. Verifikasi Changelog memuat baris Action `Edit`, Field `Max depreciation methods (Multi Depreciation tier)` (2 → 4)
25. Tutup modal Changelog
26. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE, muat ulang halaman, lalu klik tab `Global Settings`

### TC-AC-PF-293: Save tanpa perubahan (No-Op)

27. Catat jumlah entri Changelog Global Settings sebagai baseline (kemampuan baca)
28. Klik `[Save]` tanpa mengubah apa pun, lalu amati tab yang aktif
29. Verifikasi Toast netral: "No changes to save."
30. Verifikasi Pengguna tetap berada di tab Global Settings
31. Klik ikon Changelog di Card
32. Verifikasi Modal Changelog Global Settings tampil dengan entri sebelumnya (anchor)
33. Verifikasi Jumlah entri sama dengan baseline langkah 27 (tidak ada entri baru)
34. Verifikasi Nilai `Max custom fields per asset name` tetap `5` dan `Max depreciation methods (Multi Depreciation tier)` tetap `2`
35. Tutup modal Changelog

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition (langkah 1), pemulihan Global FAMS Settings lewat Fixture BE dan muat ulang halaman antar blok TC (langkah 8, 15, 26; S-09), pencatatan baseline jumlah entri Changelog per Field (langkah 16 dan 27; S-12), dan tutup modal Changelog (langkah 25 dan 35).
- Pembagian TC lintas spec: TC-AC-PF-284 sampai TC-AC-PF-289 ada di spec 113; TC-AC-PF-294 sampai TC-AC-PF-296 ada di spec 116; TC-AC-PF-300 ada di spec 128.
- Asersi "tidak ada entri baru" (TC-AC-PF-293 butir b) ditulis sebagai asersi jumlah terhadap baseline (S-12) dan bukan spec absence; id TC tetap di `sourceTc` spec ini.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-PF-290 butir b ("Satu entri log Edit untuk Max custom fields per asset name"), TC-AC-PF-291 butir b ("Satu entri log Edit untuk Max depreciation methods (Multi Depreciation tier)"), dan TC-AC-PF-292 ("Kedua setting tersimpan; dua entri log" selain yang sudah diasersi pada langkah 22 dan 24).
  - Judul TC-AC-PF-293 menyebut "timestamp tidak berubah" tetapi Expected dan tab Global Settings tidak memuat timestamp; tidak diasersi.
