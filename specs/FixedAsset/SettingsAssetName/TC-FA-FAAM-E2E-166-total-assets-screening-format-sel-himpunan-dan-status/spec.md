---
id: TC-FA-FAAM-E2E-166-total-assets-screening-format-sel-himpunan-dan-status
title: "Tab Total Assets: Screening, Format Sel, Himpunan Aset, dan Badge Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-501
  - TC-FA-FAAM-502
  - TC-FA-FAAM-504
coverage:
  web: automated
---

# Tab Total Assets: Screening, Format Sel, Himpunan Aset, dan Badge Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset contoh Pre-setup #26, Status beragam termasuk `Missing`, `Permanently Missing`, `Borrowed`, `Active`, `Draft`). Aset TC-FA-FAAM-504 berasal dari Pre-setup #26g (bagian dari 42 aset; data disediakan tim FE bila seed diperlukan): `Dell Latitude - 40` Lifecycle `Waiting for Approval`, `Dell Latitude - 39` Active dengan custody `Borrowed` dan overlay `Damaged`, `Dell Latitude - 38` Lifecycle `Draft`.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- Kemampuan teknis: seed Pre-setup oleh tim BE/FE. Blok TC-FA-FAAM-502 mengubah konfigurasi kolom (centang Label); dipulihkan oleh hook `after`.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-501: Screening Tab Total Assets

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Verifikasi toolbar `Search | Filter | Download` tampil
3. Verifikasi tombol Changelog dan tombol aksi tulis Hidden pada toolbar
4. Verifikasi kolom tabel `Name | Asset ID | TAG | Brand | Model/Type | Group | Status | Last Updated` tampil
5. Verifikasi kolom curated `Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value`, `Warranty Expiry`, dan kolom custom field tersembunyi secara default
6. Verifikasi default sort Last Updated Newest First
7. Verifikasi tabel berpaginasi (pagination tampil)

### TC-FA-FAAM-504: Badge Status Lifecycle dan hasil resolusi

8. Ketik Search `Dell Latitude - 38`, tekan Enter, sehingga baris aset Lifecycle Draft (Pre-setup #26g) tampil
9. Verifikasi aset `Dell Latitude - 38` (Lifecycle Draft) menampilkan badge `Draft`
10. Ketik Search `Dell Latitude - 40`, tekan Enter, sehingga baris aset Lifecycle Waiting for Approval (Pre-setup #26g) tampil
11. Verifikasi aset `Dell Latitude - 40` (Lifecycle Waiting for Approval) menampilkan badge `Waiting for Approval`
12. Ketik Search `Dell Latitude - 39`, tekan Enter, sehingga baris aset Active dengan status `Borrowed` dan overlay `Damaged` (Pre-setup #26g) tampil
13. Verifikasi aset `Dell Latitude - 39` (Active) menampilkan badge hasil resolusi custody dan overlay (mis. `Borrowed` dengan `Damaged`)

### TC-FA-FAAM-502: Format sel Tab Total Assets

14. Klik header Actions (⋯), pilih `Setup Column...`, centang Label, klik `[Save]` (precondition TC: kolom curated Label sudah ditampilkan; dipakai sebagai precondition, tidak diasersi)
15. Ketik Search `Dell Latitude - 42`, tekan Enter
16. Verifikasi Name berformat `[Asset Name] - [Increment]` (mis. `Dell Latitude - 42`)
17. Verifikasi TAG menampilkan satu ikon per tipe tag aktif tanpa Tag Code
18. Verifikasi Brand dan Model/Type berupa badge Dark
19. Verifikasi Group berupa badge Primary
20. Verifikasi Status berupa badge hasil resolusi status aset
21. Verifikasi Last Updated mengikuti format General Settings
22. Verifikasi Label berupa chip berwarna label (kolom curated)
23. Klik `(←)` pada kotak Search
24. Verifikasi label tab `Total Assets (42)`
25. Verifikasi jumlah total baris seluruh halaman tabel sama dengan 42 (jumlah total pada footer pagination)
26. Tutup popup Detail
27. Verifikasi kolom Total Asset baris `Dell Latitude` pada tabel utama bernilai 42

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di dalam spec: 501, 504, 502 (TC-FA-FAAM-502 menyimpan konfigurasi kolom sehingga ditaruh sesudah screening 501 yang mengasersi kolom default).
- Pembagian TC lintas spec: TC-FA-FAAM-503 dan 505 ada di spec 210 (`TC-FA-FAAM-E2E-210-total-assets-himpunan-aset-dan-empty-state-tanpa-aset`).
- Langkah penghubung: Search nama aset Pre-setup #26g untuk menemukan baris target pada blok TC-FA-FAAM-504 (langkah 8, 10, 12; tiap Search mengganti isi Search sebelumnya), Search `Dell Latitude - 42` dan `(←)` pada blok TC-FA-FAAM-502, serta menutup popup Detail.
- Asersi absence tombol Changelog dan tombol aksi tulis memakai anchor positif (toolbar `Search | Filter | Download` tampil).
- Temuan untuk QA:
  - TC-FA-FAAM-502 mengasersi chip Label, padahal kolom Label tersembunyi secara default (TC-FA-FAAM-501 butir b) dan LK TC-502 tidak menyebut langkah mencentangnya; spec menambah langkah penghubung centang Label pada blok TC-FA-FAAM-502 dan memperlakukannya sebagai precondition.
  - TC-FA-FAAM-502 butir c membandingkan himpunan dengan kolom Total Asset; cara membaca jumlah total pada footer pagination tidak dijelaskan TC.
  - Nomor Pre-setup `Warehouse Pallet` tidak tertulis di Precondition TC-FA-FAAM-505 (Total Asset 0 sesuai Pre-setup #13).
