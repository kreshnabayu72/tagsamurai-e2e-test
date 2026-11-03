---
id: TC-FA-CAID-E2E-085-increment-melewati-pergantian-tahun
title: "Increment Melewati Pergantian Tahun Tanpa Reset Counter"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-339
coverage:
  web: automated
---

# Increment Melewati Pergantian Tahun Tanpa Reset Counter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Register (Pre-setup No 24; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_REGISTER_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Register (No 24) varian pergantian tahun: konfigurasi B1, tiga aset Draft hasil seed dengan Increment 1, 2, 3 dan Asset ID `JKT/LAP/T490/0000/1`, `JKT/LAP/T490/0000/2`, `JKT/LAP/T490/0000/3`; master data Group `Jakarta Office` (`JKT`), Category `Laptop` (`LAP`), Asset Name `ThinkPad T490` (`T490`), Brand `Lenovo`. Aset ketiga ini dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: aset keempat setelah pergantian tahun (Dinamis No 15); dibersihkan oleh seed reset Company.
- Kemampuan teknis: alat uji pengatur jam (Pre-setup No 26). Hook `before` mengatur jam server dan jam browser ke 31/12/2026 23:59; jam server dan jam browser diatur bersama (konvensi bagian 6; TC hanya menyebut jam server). Sesi API aktor dan seed API (suite.md).
- State global: jam server dan jam browser diubah; hook `after` memulihkan jam ke waktu nyata dan Company Register ke konfigurasi B1 tanpa aset, dan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`). Suite berjalan serial (`parallel: false`).
- Kelas harness: d (time-travel); spec ini satu TC.

## Test Steps

1. Atur jam server dan jam browser ke 01/01/2027 00:01 lewat alat uji
2. Buka Fixed Asset > Assets > Registration
3. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
4. Perhatikan Asset ID aset baru
5. Verifikasi aset baru terbit dengan Increment 4 (`JKT/LAP/T490/0000/4`), tidak kembali ke 1
6. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID dan perhatikan seluruh kontrol
7. Verifikasi Master Switch, Separator, dan daftar segmen tampil
8. Verifikasi tab Custom Asset ID tidak memuat kontrol untuk mengatur ulang counter Asset Increment

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Langkah penghubung: langkah 2 (buka halaman), 4 (perhatikan), 6 (perhatikan seluruh kontrol).
- Langkah 7 adalah anchor positif untuk asersi absence kontrol reset counter pada langkah 8 (konvensi bagian 8b butir 2); Expected TC tidak memuatnya, dicatat sebagai asersi tambahan beserta alasannya (S-03).
- Temuan untuk QA:
  - TC-FA-CAID-339 hanya menyebut jam server; jam browser diatur bersama sesuai konvensi bagian 6. Expected tidak mengasersi angka tahun dalam Asset ID.
  - Email akun Total Control Company Register tidak tertulis di Pre-setup TC.
