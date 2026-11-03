---
id: TC-AC-DN-E2E-112-setup-column-screening-dan-ceklis
title: "Setup Column List: Screening Overlay dan Modal, Live Preview, dan Ceklis/Unceklis Tiap Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-328
  - TC-AC-DN-329
  - TC-AC-DN-603
  - TC-AC-DN-330
coverage:
  web: automated
---

# Setup Column List: Screening Overlay dan Modal, Live Preview, dan Ceklis/Unceklis Tiap Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti dan #17 seed 120 baris sebagai isi tabel dan Live Preview. Tidak ada data Dinamis dan tidak ada aksi tulis ke server.
- Tabel "Kolom uji" untuk langkah berulang (langkah 18 sampai 22): `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`.
- Kemampuan teknis: hook `after` menghapus preferensi kolom di browser (konfigurasi Setup Column disimpan di cache browser tabel List); kemampuan itu disediakan tim FE (konvensi bagian 4).
- State global: konfigurasi kolom di browser; tiap kolom dikembalikan tercentang pada setiap iterasi. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-328: Screening Overlay Column Visibility

1. Arahkan kursor ke header kolom Actions `⋯`
2. Verifikasi tooltip `Column Visibility` tampil
3. Klik header kolom Actions `⋯`
4. Verifikasi daftar kolom berurutan: `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`
5. Verifikasi tiap kolom memiliki checkbox tercentang dan enabled serta drag handle
6. Verifikasi item `Setup Column...` tampil di bagian bawah overlay

### TC-AC-DN-329: Screening modal Setup Column dan Live Preview

7. Klik `Setup Column...`
8. Verifikasi judul `Setup Column` tampil di header modal
9. Verifikasi deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.` tampil di header modal
10. Verifikasi ikon close `(✕)` tampil di kanan atas
11. Verifikasi daftar kolom berurutan `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`, tiap baris dengan checkbox tercentang, drag handle, dan ikon Pin
12. Verifikasi section Live Preview menampilkan urutan header dan isi sel yang sama dengan tabel
13. Verifikasi footer memuat tombol `[Reset to Default]` dan `[Save]` rata kanan
14. Verifikasi tidak ada tombol `[Cancel]`

### TC-AC-DN-603: Modal Setup Column tidak mencantumkan kolom Checkbox dan Actions

15. Verifikasi daftar kolom hanya memuat enam kolom data: `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, `Last Modified`
16. Verifikasi kolom Checkbox dan kolom Actions tidak ada sebagai baris pada daftar

### TC-AC-DN-330: Ceklis dan unceklis tiap kolom List

17. Klik ikon close `(✕)` pada modal Setup Column
18. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`
19. Hapus centang kolom uji lalu klik `[Save]`
20. Verifikasi kolom uji hilang dari header dan baris tabel
21. Buka modal Setup Column lewat header `⋯` lalu `Setup Column...`, centang kolom uji kembali, lalu klik `[Save]`
22. Verifikasi kolom uji tampil lagi di posisi semula
23. Untuk setiap baris tabel "Kolom uji", ulangi langkah 18 sampai 22

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis ke server.
- Langkah penghubung (S-03): langkah 17 menutup modal Setup Column sebelum blok berulang. TC-AC-DN-603 tidak membuka ulang overlay dan modal karena modal yang dibuka langkah 3 dan 7 sudah berada pada keadaan awal TC itu (satu pembukaan dipakai bersama).
- Ukuran spec (23 langkah nominal, sekitar 47 langkah dengan ekspansi langkah 18 sampai 22 untuk enam kolom; di atas smell 35 langkah, kode R3 dan bagian 8b butir 7): satu topik (Setup Column List), satu dataset, satu kelas harness; langkah yang diulang per kolom memakai parameter tabel "Kolom uji" tanpa langkah bersyarat, dan tiap iterasi memulihkan kolom sehingga bagian sesudahnya tetap bermakna bila satu iterasi gagal.
- Urutan: mengikuti sourceTc; screening di awal, ceklis tiap kolom di akhir.
- Temuan untuk QA:
  - TC-AC-DN-330 Expected tiap kolom ("hilang dari header dan baris tabel") ditulis satu `Verifikasi` karena header dan sel kolom sama-sama bagian satu elemen kolom.
