---
id: TC-FA-FAAL-E2E-071-sembunyi-dan-tampil-kolom-tab-user-action
title: "Setup Column Tab User Action: Sembunyikan dan Tampilkan Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-149
coverage:
  web: automated
---
# Setup Column Tab User Action: Sembunyikan dan Tampilkan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data precondition: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), seluruhnya bertanggal 18/06/26 (Asia/Jakarta); rincian baris dirujuk lewat butir seed di bawah. Spec ini hanya memakai kolom tabel dan tidak mengasersi nilai baris tertentu (precondition, tidak diasersi).
- Seed dan pemulihan data log lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Identitas data dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Spec hanya membaca baris log seed dan tidak membuat, mengubah, atau menghapus baris log maupun data Pre-setup.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Parameter iterasi (kolom Tab User Action, urutan default): `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Pemulihan Setup Column: hook `after` spec ini menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`; kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action

### TC-FA-FAAL-149: Sembunyikan dan tampilkan kolom lewat Popup Setup Column

Untuk setiap kolom pada parameter iterasi (langkah 2 sampai 17):

2. Klik header kolom Actions (⋯)
3. Klik `Setup Column...`
4. Hilangkan centang kolom
5. Verifikasi kolom-kolom selain kolom ini tampil di Live Preview
6. Verifikasi kolom hilang dari Live Preview
7. Klik `[Save]`
8. Verifikasi kolom-kolom selain kolom ini tampil di tabel
9. Verifikasi kolom hilang dari tabel
10. Muat ulang halaman (F5)
11. Verifikasi kolom tersisa pertama tampil di tabel
12. Verifikasi kolom tetap hilang dari tabel setelah muat ulang
13. Klik header kolom Actions (⋯)
14. Klik `Setup Column...`
15. Centang kembali kolom
16. Klik `[Save]`
17. Verifikasi kolom tampil kembali di tabel

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal; popup dibuka ulang sesudah muat ulang karena muat ulang menutup popup. Setiap iterasi diawali dan diakhiri dengan konfigurasi default (semua kolom tampil), sehingga iterasi tidak bergantung pada hasil iterasi sebelumnya.
- Langkah 2 sampai 17 diulang untuk delapan kolom; parameter iterasi ada di Prerequisites. Tiap iterasi memuat `Verifikasi` per klausa Expected (S-01); `Verifikasi` kolom lain tampil (langkah 5 dan 8) dan kolom tersisa pertama tampil (langkah 11, klausa "kolom tersisa pertama tampil" Expected TC-FA-FAAL-149) adalah anchor positif untuk asersi absence kolom (bagian 8b butir 2).
- Ukuran spec 17 langkah nominal (129 langkah setelah ekspansi iterasi), melewati sekitar 35 karena TC-FA-FAAL-149 satu TC berupa delapan iterasi identik per kolom ("Untuk tiap kolom pada Data Uji") dengan empat klausa Expected per kolom; satu TC satu spec sehingga iterasinya tidak dapat dipecah. Blok satu kelas harness (fungsional), satu dataset (Pre-setup #12), tanpa menulis baris log.
- Pembagian TC lintas spec: TC-FA-FAAL-147, 148, dan 154 ada di spec 041.

