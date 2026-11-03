---
id: TC-FA-FAAM-E2E-160-tab-linked-custom-fields-tautan-dan-penambahan-scope
title: "Tab Linked Custom Fields: Tautan Open in Custom Fields dan Penambahan Custom Field Berscope"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-550
  - TC-FA-FAAM-551
coverage:
  web: automated
---

# Tab Linked Custom Fields: Tautan Open in Custom Fields dan Penambahan Custom Field Berscope

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.dellLatitude`): `Dell Latitude` (Pre-setup #10) dengan custom field berscope (Pre-setup #27): `Cost Center` (Dropdown, Global `Finance`), `Operating System` (Dropdown, Specific), dan `Warranty Notes` (Text, Global kosong), sehingga label tab `Linked Custom Fields (3)`.
- Data Dinamis: custom field `Extra Field {runId}-160` dengan scope `Dell Latitude`, dibuat langkah 6 lewat modul Custom Fields. Hook `after` menghapus field itu lewat sesi API sehingga `Dell Latitude` kembali memiliki tiga custom field berscope untuk spec lain. Detail form Custom Fields tidak ada di TC (lihat Temuan untuk QA).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah selain custom field di atas. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Klik tab `Linked Custom Fields (3)`

### TC-FA-FAAM-550: Tautan Open in Custom Fields membuka modul custom fields pada tab yang sama

4. Klik `Open in Custom Fields ↗`
5. Verifikasi halaman Custom Fields terbuka pada tab browser yang sama

### TC-FA-FAAM-551: Penambahan custom field berscope Asset Name menambah baris dan jumlah tab

6. Di modul Custom Fields tambahkan field baru `Extra Field {runId}-160` dengan scope `Dell Latitude`, lalu simpan
7. Tunggu aksi selesai (field tersimpan)
8. Buka Fixed Asset > Settings > Asset Master > Asset Name
9. Ketik Search `Dell Latitude`, tekan Enter
10. Klik nama `Dell Latitude`
11. Verifikasi label tab `Linked Custom Fields (4)` tampil
12. Klik tab `Linked Custom Fields (4)`
13. Verifikasi baris `Extra Field {runId}-160` tampil

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1 dan 9, R-16), menunggu field tersimpan sebelum pindah surface (langkah 7), dan kembali ke halaman Asset Name (langkah 8). TC-FA-FAAM-551 melanjutkan dari halaman Custom Fields yang dibuka TC-FA-FAAM-550, sehingga tidak ada navigasi tambahan.
- Pemicu pada langkah 6 dijalankan lewat UI modul Custom Fields karena TC menyebutnya sebagai langkah modul itu.
- Temuan untuk QA:
  - TC-FA-FAAM-551 langkah 1 ("tambahkan scope `Dell Latitude` pada field baru `Extra Field`") tidak merinci form Custom Fields (field wajib, Data Type, Global Value); spec menulis langkah ringkas dan mengandalkan tim FE untuk detailnya. Nama `Extra Field` diberi suffix per run (S-12).
  - TC-FA-FAAM-550 Expected ("pada tab yang sama") tidak menyebut path atau judul halaman Custom Fields; spec mengasersi bahwa halaman Custom Fields terbuka di tab browser yang sama.
