---
id: TC-GS-NLU-E2E-087-list-download-isi-berkas-tipe-sel-bom-csv-format
title: "List Download isi berkas: tipe sel, BOM dan escape CSV, dan format tanggal General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-302
  - TC-GS-NLU-304
  - TC-GS-NLU-414
coverage:
  web: automated
---

# List Download isi berkas: tipe sel, BOM dan escape CSV, dan format tanggal General Settings

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 12 dan 16; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Budi Kurniawan` (Active, Represented By Ahmad Fauzi, foto), `Siti Rahayu` (tanpa Position dan Employee ID), dan `Putra, Budi`; General Settings Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Pre-setup No. 16, tidak diubah spec ini). Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis: tidak ada. Spec ini tidak menulis atau menghapus data.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis (kelas binary buffer): menangkap unduhan browser dan membaca isi berkas CSV sebagai byte dan sebagai teks (awalan BOM UTF-8, escape tanda kutip ganda, nilai sel per baris dan kolom).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-302: Isi file Download mengikuti tipe kolom

1. Klik Download > `Download as CSV`, buka berkas dan amati baris `Budi Kurniawan` dan `Siti Rahayu`
2. Verifikasi kolom Active berisi `Active` atau `Inactive` (bukan switch)
3. Verifikasi kolom Name tanpa foto
4. Verifikasi nilai kosong Position dan Employee ID (baris `Siti Rahayu`) berisi `-` (bukan `—`, bukan kosong)
5. Verifikasi Last Update mengikuti format General Settings
6. Verifikasi Represented By (baris `Budi Kurniawan`) ditulis nama penuh Login User

### TC-GS-NLU-304: CSV memakai encoding UTF-8 dengan BOM dan meng-escape koma

7. Klik Download > `Download as CSV`, buka berkas sebagai teks
8. Verifikasi berkas berawalan BOM UTF-8
9. Verifikasi nilai `Putra, Budi` dibungkus tanda kutip ganda

### TC-GS-NLU-414: Download memakai format tanggal General Settings

10. Klik Download > `Download as CSV`, buka kolom Last Update
11. Verifikasi nilai tanggal di berkas mengikuti General Settings

## Notes

- Spec kelas binary buffer: asersi nilai sel, BOM, dan tipe sel dipisah dari spec Download fungsional (spec 086, yang mengasersi nama berkas, header, dan jumlah baris).
- Asersi tambahan (S-03): tidak ada.
- Temuan untuk QA:
  - TC-GS-NLU-302 Expected a menyebut `Active`/`Inactive` tanpa menyebut baris yang dibaca; spec memakai `Budi Kurniawan` (Active) dan `Siti Rahayu`.
  - TC-GS-NLU-302 Expected b ("Name tanpa foto") tidak menyebut cara mengamati foto di CSV; spec mengasersi isi sel Name hanya berisi teks nama.
  - TC-GS-NLU-304 precondition menyebut Non-Login User `Putra, Budi` tanpa menyebut Email; Pre-setup No. 11 menulis `Putra\, Budi`.
  - TC-GS-NLU-414 precondition d merujuk "General Settings sama seperti TC format tanggal List" tanpa menyebut nilainya; spec memakai Pre-setup No. 16.
