---
id: TC-FA-FAAL-E2E-072-pin-dan-unpin-kolom-tab-user-action
title: "Setup Column Tab User Action: Pin dan Unpin Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-151
coverage:
  web: automated
---
# Setup Column Tab User Action: Pin dan Unpin Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data precondition: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), seluruhnya bertanggal 18/06/26 (Asia/Jakarta); rincian baris dirujuk lewat butir seed di bawah. Spec ini hanya memakai kolom tabel dan tidak mengasersi nilai baris tertentu (precondition, tidak diasersi).
- Seed dan pemulihan data log lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Identitas data dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Spec hanya membaca baris log seed dan tidak membuat, mengubah, atau menghapus baris log maupun data Pre-setup.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Parameter iterasi (kolom Tab User Action, urutan default): `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Kemampuan teknis: menggulir tabel secara horizontal; lebar viewport browser cukup sempit sehingga delapan kolom tidak muat tanpa gulir horizontal (disediakan tim FE).
- Pemulihan Setup Column: hook `after` spec ini menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`; kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action

### TC-FA-FAAL-151: Pin dan unpin kolom Tab User Action

Untuk setiap kolom pada parameter iterasi (langkah 2 sampai 16):

2. Klik header kolom Actions (⋯)
3. Klik `Setup Column...`
4. Klik icon Pin pada kolom
5. Klik `[Save]`
6. Gulir tabel secara horizontal
7. Verifikasi kolom tetap terlihat saat tabel digulir horizontal
8. Muat ulang halaman (F5)
9. Gulir tabel secara horizontal
10. Verifikasi kolom tetap beku setelah muat ulang
11. Klik header kolom Actions (⋯)
12. Klik `Setup Column...`
13. Klik unpin pada kolom
14. Klik `[Save]`
15. Gulir tabel secara horizontal
16. Verifikasi kolom ikut bergulir

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal; popup dibuka ulang sesudah muat ulang karena muat ulang menutup popup; gulir horizontal ditulis eksplisit sebelum tiap `Verifikasi` yang bergantung pada posisi gulir (S-14); sesudah muat ulang tabel digulir lagi karena posisi gulir kembali ke awal.
- Langkah 2 sampai 16 diulang untuk delapan kolom; parameter iterasi ada di Prerequisites. Setiap iterasi diakhiri unpin sehingga konfigurasi kembali ke default sebelum iterasi berikutnya.
- Ukuran spec 16 langkah nominal (121 langkah setelah ekspansi iterasi), melewati sekitar 35 karena TC-FA-FAAL-151 satu TC berupa delapan iterasi identik per kolom ("Untuk tiap kolom pada Data Uji") dengan tiga klausa Expected per kolom; satu TC satu spec sehingga iterasinya tidak dapat dipecah. Blok satu kelas harness (fungsional), satu dataset (Pre-setup #12), tanpa menulis baris log.
- Pembagian TC lintas spec: TC-FA-FAAL-150, 152, dan 153 ada di spec 042.
- Temuan untuk QA:
  - TC-FA-FAAL-151 tidak menyebut lebar viewport yang membuat tabel dapat digulir horizontal; kebutuhan itu ditulis di Prerequisites sebagai kemampuan teknis.

