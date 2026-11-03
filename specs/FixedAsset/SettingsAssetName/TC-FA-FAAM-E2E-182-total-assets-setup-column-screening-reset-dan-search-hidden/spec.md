---
id: TC-FA-FAAM-E2E-182-total-assets-setup-column-screening-reset-dan-search-hidden
title: "Tab Total Assets Setup Column: Screening Overlay-Popup, Reset to Default, Discard, dan Guard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-526
  - TC-FA-FAAM-527
  - TC-FA-FAAM-540
coverage:
  web: automated
---

# Tab Total Assets Setup Column: Screening Overlay-Popup, Reset to Default, Discard, dan Guard

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Data: `Dell Latitude` (Total Asset 42, aset contoh Pre-setup #26). Kolom custom field Active yang tersedia bagi Total Control pada client utama (Pre-setup #33e) ikut tampil sebagai kolom curated.
- Data Pre-setup dirujuk lewat `Fixture.fa-settings-asset-name.<kunci>`; berkas fixture belum ada dan disediakan tim FE. Fixture bersifat baca-saja: spec ini tidak membuat, mengubah, atau menghapus data Pre-setup, sehingga tidak ada data Dinamis dan tidak ada suffix `{runId}`.
- Pemulihan konfigurasi kolom: hook `after` menghapus preferensi Setup Column di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE dan dinyatakan di `suite.md`. Spec ini menyimpan konfigurasi kolom.
- State global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-526: Screening kolom Actions dan overlay Column Visibility

1. Klik nama `Dell Latitude`, klik tab `Total Assets (42)`
2. Hover header kolom Actions (⋯) di ujung kanan
3. Verifikasi tooltip `Column Visibility`
4. Verifikasi kolom Actions (⋯) tanpa row action ada di ujung kanan
5. Klik header Actions (⋯)
6. Verifikasi overlay memuat kolom data sesuai urutan tabel Setup Column Tab Total Assets: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated` dengan checkbox `☑`
7. Verifikasi overlay memuat `Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value`, `Warranty Expiry`, dan satu kolom per custom field Active yang tersedia bagi aktor (field Purchasing dan Accounting mengikuti hak aktor) dengan checkbox `☐` curated
8. Verifikasi overlay memuat item `Setup Column...`

### TC-FA-FAAM-527: Screening Popup Setup Column

9. Klik item `Setup Column...`
10. Verifikasi popup `Setup Column` tampil dengan deskripsi standar
11. Verifikasi baris kolom 8 default `☑ Hideable`: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`
12. Verifikasi baris kolom `Measurement`, `Category`, `Label`, `Transactional Policy`, `Last Scanned`, `Asset Value`, `Warranty Expiry`, dan kolom custom field `☐ Curated`
13. Verifikasi Live Preview tampil
14. Verifikasi `[Reset to Default]` dan `[Save]` tampil
15. Tekan Esc untuk menutup popup

### TC-FA-FAAM-540: Reset to Default, discard, dan guard satu kolom

16. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Group, klik `[Save]`
17. Klik header Actions (⋯), pilih `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`
18. Verifikasi reset mengembalikan 8 kolom default pada tabel
19. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang 7 kolom sehingga tersisa satu kolom
20. Hover checkbox kolom yang tersisa
21. Verifikasi checkbox kolom tersisa disabled
22. Verifikasi tooltip `At least one column must remain visible.`
23. Tekan Esc untuk menutup popup tanpa menyimpan
24. Klik header Actions (⋯), pilih `Setup Column...`, hapus centang Name, tekan Esc
25. Verifikasi Esc membuang perubahan preview: kolom Name tetap tampil pada tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 526, 527, 540 (540 menyimpan konfigurasi kolom sehingga dikerjakan terakhir).
- Langkah penghubung: menutup popup dengan Esc setelah screening (TC-FA-FAAM-527) dan sesudah guard satu kolom (TC-FA-FAAM-540, tanpa menyimpan).
- Temuan untuk QA:
  - TC-FA-FAAM-527 menyebut "deskripsi standar" tanpa kutipan teks sehingga hanya keberadaannya yang diasersi.
  - TC-FA-FAAM-540 LK langkah 5 tidak menyebut kolom yang tersisa; spec menyisakan satu kolom Hideable default dan menahan popup tanpa `[Save]`.
  - TC-FA-FAAM-540 Expected a ("8 kolom default") mengandalkan Group disembunyikan lebih dulu pada langkah 3 TC; spec mengikuti urutan itu.
