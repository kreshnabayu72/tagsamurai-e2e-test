---
id: TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris
title: "Pemotongan Badge, Klik Area Baris, Scrollbar Tablet, dan Tinggi Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-14
  - TC-FA-CF-19
  - TC-FA-CF-611
  - TC-FA-CF-614
coverage:
  web: automated
---

# Pemotongan Badge, Klik Area Baris, Scrollbar Tablet, dan Tinggi Baris

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12) dan tab Purchasing (Pre-setup #13: field `Long Option Field` Dropdown dengan opsi `Industrial Compressor Unit 7000` (31 karakter, Pre-setup #32) dan `Class A`), dirujuk lewat fixture baru `Fixture.faCustomFields.baselineGeneral` dan `Fixture.faCustomFields.baselinePurchasing`. Baseline dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Kemampuan teknis: hover; mengatur ukuran viewport browser (tablet lebar 768 px) dan memulihkannya ke ukuran desktop; menggulir tabel secara horizontal.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain ukuran viewport (dipulihkan pada langkah 13 dan oleh hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-614: Sel single-value tidak wrap dan tinggi baris konsisten

1. Verifikasi sel Data Type, Required, Modified By, dan Last Updated tampil satu baris tanpa wrap
2. Verifikasi header kolom satu baris dengan tinggi tetap
3. Verifikasi tinggi kedelapan baris tabel konsisten

### TC-FA-CF-19: Klik area baris di luar switch, checkbox, dan row action tidak melakukan aksi

4. Klik teks Field Name baris `Asset Serial Tag`
5. Klik sel Data Type baris `Asset Serial Tag`
6. Verifikasi tidak ada modal, popup, atau navigasi yang terbuka
7. Verifikasi Field Name baris `Asset Serial Tag` tidak berupa tautan

### TC-FA-CF-611: Tablet menampilkan horizontal scrollbar dengan kolom Actions tetap terlihat

8. Atur viewport browser ke tablet (lebar 768 px)
9. Verifikasi tabel mengaktifkan horizontal scrollbar
10. Verifikasi tabel tidak memotong kolom
11. Gulir tabel ke kanan secara horizontal
12. Verifikasi kolom Actions (⋯) tetap terlihat (sticky) saat tabel digulir ke kanan
13. Pulihkan viewport ke ukuran desktop

### TC-FA-CF-14: Badge opsi lebih dari 25 karakter dipotong dengan tooltip nama penuh

14. Klik tab `Purchasing`
15. Verifikasi badge opsi panjang pada kolom Value Setting baris `Long Option Field` tampil `Industrial C..or Unit 7000`
16. Verifikasi badge `Class A` pada baris `Long Option Field` tampil penuh
17. Arahkan kursor ke badge `Industrial C..or Unit 7000`
18. Verifikasi hover menampilkan nama penuh `Industrial Compressor Unit 7000`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec hanya membaca; subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 614, 19, 611, 14. TC-FA-CF-14 ditempatkan di akhir karena satu-satunya TC di tab Purchasing sehingga spec tidak perlu kembali ke tab General; viewport tablet (TC-FA-CF-611) diselesaikan dan dipulihkan (langkah 13) sebelum pindah tab (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 dan 13 (mengatur dan memulihkan viewport), langkah 11 (menggulir tabel), langkah 14 (pindah tab sesuai langkah 2 TC-FA-CF-14), dan langkah 17 (hover).
- Langkah 10 adalah klausa kedua Expected a TC-FA-CF-611 ("tanpa memotong kolom"); langkah 16 mendahului hover karena Expected c TC-FA-CF-14 tidak bergantung pada hover dan diasersi sebelum state hover (8b butir 5).
- Langkah 6 dan 7 (absence) beranchor baris tabel yang sudah diverifikasi tampil pada langkah 1 sampai 3.
- Temuan untuk QA:
  - TC-FA-CF-611 Expected a ("tanpa memotong kolom") tidak menyebut cara mengukurnya; spec mengasersi bahwa semua kolom dapat dijangkau lewat scrollbar horizontal.
  - TC-FA-CF-614 Expected a menyebut "tanpa wrap" tanpa kriteria teknis (mis. tinggi sel); kriteria diputuskan penulis skrip.
