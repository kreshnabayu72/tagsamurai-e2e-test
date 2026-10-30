---
id: TC-GS-ROLE-E2E-094-isolasi-akses-produk-lain-assign-total-control
title: "Isolasi Akses Produk Lain pada Assign Total Control Global Settings"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-283
coverage:
  web: automated
---

# Isolasi Akses Produk Lain pada Assign Total Control Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control. Ahmad Fauzi dapat membuka Admin Console > Settings > Role & Permission (akses Admin Console aktor disediakan tim FE; TC tidak menyebutnya).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah: Sari Wulandari (Pre-setup #11, Active, Access Global Settings) dengan Access Admin Console tanpa access level Admin Console (Given lewat API di hook `before`, disediakan tim FE; precondition b TC), dan tanpa access level Global Settings. Langkah 1 sampai 3 meng-assign Total Control Global Settings; langkah 9 sampai 12 me-Remove-nya (pemulihan state, S-09). Hook `after` memulihkan Sari Wulandari ke state itu bila langkah pemulihan tidak selesai. Efek yang tidak dipulihkan: Last Updated dan entri log (bersifat immutable).
- Kemampuan teknis: mengakses dua produk (Global Settings dan Admin Console) dengan satu sesi aktor; seeding Access Admin Console dan pemulihan access level lewat API.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Assign]`
2. Centang Sari Wulandari
3. Klik `[Assign]`
4. Ketik Search `Sari Wulandari`, tekan Enter
5. Verifikasi Sari Wulandari tampil di Tab Total Control Global Settings
6. Buka Admin Console > Settings > Role & Permission > Tab Total Control
7. Ketik Search `Sari Wulandari`, tekan Enter
8. Verifikasi empty state `No results found` tampil di Tab Total Control Admin Console
9. Buka Global Settings > Role & Permission > Tab Total Control, ketik Search `Sari Wulandari`, tekan Enter
10. Klik Remove pada baris Sari Wulandari
11. Klik `[Remove]`
12. Tunggu aksi selesai

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search baris target (langkah 4, 7, 9); membuka Admin Console dan kembali ke Global Settings (langkah 6, 9); pemulihan state Sari Wulandari (langkah 9 sampai 12).
- Langkah 8 memverifikasi Expected b bagian pertama ("tidak tampil di Tab Total Control Admin Console"). Klausa kedua ("akses Admin Console-nya tidak berubah") tidak punya langkah observasi sendiri di TC dan tidak ada tabel atau layar yang menunjukkan akses Admin Console selain Tab Total Control; ia diamati lewat langkah 8 yang sama (Sari Wulandari tetap tanpa access level Admin Console).
- Absence pada langkah 8 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); langkah 5 membuktikan Assign sebagai pemicu telah berhasil.
- Temuan untuk QA:
  - TC-GS-ROLE-283 Expected b klausa "akses Admin Console-nya tidak berubah" tidak punya langkah observasi di Langkah Uji; spec tidak menambah asersi baru dan mengandalkan langkah 8.
  - TC-GS-ROLE-283 tidak menyebut hasil Assign (toast) dan tidak menyebut akses Admin Console aktor Ahmad Fauzi; spec mengasumsikan aktor dapat membuka Admin Console (disediakan tim FE).
  - TC-GS-ROLE-283 tidak menyebut cara menyiapkan Access Admin Console Sari Wulandari; spec memakai Given lewat API yang disediakan tim FE (mekanisme tidak didefinisikan TC).
