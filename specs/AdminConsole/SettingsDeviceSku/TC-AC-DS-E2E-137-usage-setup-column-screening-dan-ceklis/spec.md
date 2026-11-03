---
id: TC-AC-DS-E2E-137-usage-setup-column-screening-dan-ceklis
title: "Setup Column Usage: Screening Overlay dan Popup serta Ceklis dan Unceklis Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-454
  - TC-AC-DS-455
  - TC-AC-DS-456
coverage:
  web: automated
---

# Setup Column Usage: Screening Overlay dan Popup serta Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Kolom yang diuji (parameter langkah 21 sampai 24): `Company`, `Entity Type`, `Total Stock`.
- Data Dinamis: tidak ada. Spec menyimpan konfigurasi kolom (ketiga kolom tercentang, sama dengan bawaan) pada langkah 25.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column popup Usage di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil

### TC-AC-DS-454: Screening Overlay Column Visibility popup Usage by Company

3. Klik header kolom Actions (⋯) pada popup
4. Verifikasi Overlay Column Visibility tampil
5. Verifikasi tombol `Setup Column...` tampil di bagian bawah overlay
6. Verifikasi daftar kolom `Company | Entity Type | Total Stock`
7. Verifikasi ketiga kolom tercentang dan enabled (Hideable)
8. Verifikasi setiap kolom memiliki drag handle

### TC-AC-DS-455: Screening Popup Setup Column popup Usage by Company dan Preview Table

9. Klik `Setup Column...`
10. Verifikasi Popup Setup Column tampil
11. Verifikasi header memuat judul "Setup Column"
12. Verifikasi header memuat deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
13. Verifikasi header memuat ikon close `[✕]`
14. Verifikasi body memuat tiga kolom dengan checkbox tercentang
15. Verifikasi setiap kolom memiliki drag handle
16. Verifikasi setiap kolom memiliki ikon Pin
17. Verifikasi section Live Preview menampilkan urutan header dan data Usage
18. Verifikasi footer memuat tombol `[Reset to Default]` dan `[Save]`
19. Verifikasi footer tidak memuat tombol `[Cancel]`

### TC-AC-DS-456: Ceklis dan unceklis kolom Setup Column Usage by Company

20. Untuk setiap baris tabel "Kolom yang diuji" lakukan langkah 21 sampai 24
21. Hilangkan centang kolom
22. Verifikasi kolom tersebut hilang dari preview
23. Centang kembali kolom
24. Verifikasi kolom tersebut tampil kembali di preview
25. Klik `[Save]`
26. Verifikasi tabel Usage memuat ketiga kolom `Company`, `Entity Type`, `Total Stock`

### Pemulihan state akhir

27. Tutup popup `Device SKU Detail` dengan ikon close `[✕]`

## Notes

- Langkah 21 sampai 24 diulang per kolom pada tabel "Kolom yang diuji" (3 iterasi, ekspansi 12 langkah; total ekspansi spec sekitar 35 langkah). Semua langkah satu kelas (Setup Column popup Usage) dan tiap kolom berdiri sendiri.
- Langkah penghubung tanpa `Verifikasi`: langkah 27 (S-03). Popup Setup Column dari TC-AC-DS-455 tetap terbuka dan dipakai TC-AC-DS-456 tanpa perubahan state sebelumnya.
- Expected 455 butir b.i dipecah menjadi langkah 14 sampai 16 (S-01).
- Temuan untuk QA:
  - S-15: Expected 456 menyebut kolom hilang "pada preview dan tabel", tetapi TC hanya memiliki satu `[Save]` di akhir sehingga tabel tidak teramati per kolom; spec mengasersi preview per kolom (langkah 22, 24) dan tabel setelah Save (langkah 26).
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
