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
- Data Pre-setup yang diubah: Sari Wulandari (Pre-setup #11, Active, Access Global Settings) dengan Access Admin Console tanpa access level Admin Console (Given lewat API di hook `before`, disediakan tim FE; precondition b TC), dan tanpa access level Global Settings. Langkah 2 sampai 5 meng-assign Total Control Global Settings; langkah 12 sampai 16 me-Remove-nya (pemulihan state, S-09). Hook `after` memulihkan Sari Wulandari ke state itu bila langkah pemulihan tidak selesai. Efek yang tidak dipulihkan: Last Updated dan entri log (bersifat immutable).
- Kemampuan teknis: mengakses dua produk (Global Settings dan Admin Console) dengan satu sesi aktor; seeding Access Admin Console dan pemulihan access level lewat API; membaca access level Admin Console Sari Wulandari (kemampuan baca disediakan tim FE; TC tidak mendefinisikan mekanismenya, tanpa endpoint karangan).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Verifikasi (lewat kemampuan baca access level Admin Console, disediakan tim FE) Sari Wulandari tidak punya access level Admin Console (baseline sebelum Assign; precondition b TC)
2. Klik `[+ Assign]`
3. Ketik Search `Sari Wulandari`, tekan Enter
4. Centang Sari Wulandari
5. Klik `[Assign]`
6. Ketik Search `Sari Wulandari`, tekan Enter
7. Verifikasi Sari Wulandari tampil di Tab Total Control Global Settings
8. Buka Admin Console > Settings > Role & Permission > Tab Total Control
9. Ketik Search `Sari Wulandari`, tekan Enter
10. Verifikasi empty state `No results found` tampil di Tab Total Control Admin Console
11. Verifikasi (lewat kemampuan baca access level Admin Console, disediakan tim FE) access level Admin Console Sari Wulandari tidak berubah, sama dengan baseline langkah 1
12. Buka Global Settings > Role & Permission > Tab Total Control, ketik Search `Sari Wulandari`, tekan Enter
13. Klik `(⋯)` pada baris Sari Wulandari
14. Klik `Remove`
15. Klik `[Remove]`
16. Tunggu aksi selesai

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search baris target, termasuk Search di Popup Assign sebelum dicentang karena pool user bisa lebih dari satu halaman (langkah 3, 6, 9, 12; R-16); membuka Admin Console dan kembali ke Global Settings (langkah 8, 12); pemulihan state Sari Wulandari (langkah 12 sampai 16).
- Langkah 10 memverifikasi Expected b bagian pertama ("tidak tampil di Tab Total Control Admin Console"). Klausa kedua ("akses Admin Console-nya tidak berubah") diamati lewat kemampuan baca access level Admin Console yang disediakan tim FE: baseline sebelum Assign pada langkah 1 dan pembacaan sesudah Assign pada langkah 11. Empty state langkah 10 tidak cukup untuk klausa ini karena hanya menunjukkan Tab Total Control Admin Console.
- Absence pada langkah 10 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2); langkah 7 membuktikan Assign sebagai pemicu telah berhasil.
- Langkah penghubung (S-15, bukan dari TC sumber): row action `Remove` berada di overlay `(⋯)` baris, sehingga pemulihan "Klik Remove pada baris Sari Wulandari" ditulis `Klik (⋯)` pada baris (langkah 13) lalu `Klik Remove` (langkah 14).
- Temuan untuk QA:
  - TC-GS-ROLE-283 Expected b klausa "akses Admin Console-nya tidak berubah" tidak punya langkah observasi di Langkah Uji; spec mengamatinya lewat kemampuan baca access level Admin Console yang disediakan tim FE (langkah 1 dan 11), tanpa endpoint karangan.
  - TC-GS-ROLE-283 tidak menyebut hasil Assign (toast) dan tidak menyebut akses Admin Console aktor Ahmad Fauzi; spec mengasumsikan aktor dapat membuka Admin Console (disediakan tim FE).
  - TC-GS-ROLE-283 tidak menyebut cara menyiapkan Access Admin Console Sari Wulandari; spec memakai Given lewat API yang disediakan tim FE (mekanisme tidak didefinisikan TC).
