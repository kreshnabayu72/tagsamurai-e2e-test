---
id: TC-GS-ROLE-E2E-089-sinkron-rename-position-dan-status-custom-field
title: "Sinkronisasi Rename Position dan Status Custom Field pada Tab Total Control"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-237
  - TC-GS-ROLE-240
coverage:
  web: automated
---

# Sinkronisasi Rename Position dan Status Custom Field pada Tab Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah: Position `IT Manager` milik Ahmad Fauzi (Pre-setup #1, IT Manager, IT) di-rename menjadi `IT Head` pada TC-GS-ROLE-237 dan di-rename kembali menjadi `IT Manager` pada langkah 9 dan 10; hook `after` memulihkan nama Position lewat API bila langkah itu tidak selesai. Efek yang tidak dipulihkan: Last Updated Position dan entri Changelog Position (log bersifat immutable).
- Data milik spec (suffix per run dan nomor spec): Custom Field User `Region {runId}-089` (tipe Text, Active), di-seed lewat API di hook `before` sebagai pengganti `Region` pada precondition b TC-GS-ROLE-240; dinonaktifkan oleh TC-GS-ROLE-240 dan dihapus lewat API di hook `after`. Hook `after` juga menghapus preferensi Setup Column Tab Total Control di perangkat uji (tersimpan per perangkat, lokal di browser).
- Kemampuan teknis: seeding dan penghapusan Custom Field User lewat API (mekanisme tidak didefinisikan TC; disediakan tim FE/BE); mengubah Position lewat UI dan API; muat ulang halaman.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: nama Position dan status Custom Field (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-237: Rename Position tercermin di Tab Total Control

1. Buka Global Settings > User > Tab Position, ketik Search `IT Manager`, tekan Enter
2. Klik `⋯` pada baris `IT Manager`, pilih `Edit`
3. Ubah Position Name menjadi `IT Head`
4. Klik `[Save]`
5. Tunggu aksi selesai
6. Buka Role & Permission > Tab Total Control, ketik Search `Ahmad Fauzi`, tekan Enter
7. Verifikasi kolom Position baris Ahmad Fauzi menampilkan `IT Head`
8. Buka Global Settings > User > Tab Position, ketik Search `IT Head`, tekan Enter
9. Klik `⋯` pada baris `IT Head`, pilih `Edit`, ubah Position Name menjadi `IT Manager`, klik `[Save]`
10. Tunggu aksi selesai

### TC-GS-ROLE-240: Kolom Custom Field mengikuti status Custom Field

11. Buka Role & Permission > Tab Total Control
12. Klik `⋯` pada header kolom Actions
13. Klik item `Setup Column...`
14. Verifikasi kolom `Region {runId}-089` tersedia di Setup Column
15. Tampilkan kolom `Region {runId}-089`
16. Klik `[Save]`
17. Buka Global Settings > User > Tab Custom Field, ketik Search `Region {runId}-089`, tekan Enter
18. Matikan switch Active baris `Region {runId}-089`, klik `[Deactivate]` pada dialog
19. Tunggu aksi selesai
20. Buka Role & Permission > Tab Total Control, muat ulang halaman
21. Klik `⋯` pada header kolom Actions
22. Klik item `Setup Column...`
23. Verifikasi kolom `Position` tersedia di Setup Column
24. Verifikasi kolom `Region {runId}-089` tidak tersedia di Setup Column
25. Tutup modal Setup Column dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC mengikuti TC sumber; dua TC memakai data yang berbeda (Position Ahmad Fauzi dan Custom Field milik spec) sehingga tidak ada ketergantungan data.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search target (langkah 1, 6, 8, 17); "Tunggu aksi selesai" (langkah 5, 10, 19); pemulihan nama Position (langkah 8 sampai 10, S-09); membuka modal Setup Column lewat `⋯` header kolom Actions dan item `Setup Column...` (langkah 12 dan 13, 21 dan 22); menampilkan kolom dan menyimpan Setup Column (langkah 15 dan 16, bagian dari Langkah Uji 1 TC-GS-ROLE-240); menutup modal Setup Column (langkah 25).
- Urutan Expected TC-GS-ROLE-240: langkah 14 memverifikasi Expected a sebelum kolom ditampilkan; langkah 23 (kolom `Position` tersedia) adalah anchor positif bahwa daftar Setup Column sudah termuat sebelum asersi absence kolom Custom Field pada langkah 24 (Expected b, bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-ROLE-240 memakai Custom Field `Region` yang tidak ada di Tabel Data Uji Pre-setup TC; spec memakai `Region {runId}-089` milik spec yang di-seed lewat API (mekanisme seeding tidak didefinisikan TC).
  - TC-GS-ROLE-240 Data Uji `[Custom Field aktif]: Region` tidak menyebut tipe field; spec memakai tipe Text.
  - TC-GS-ROLE-237 mengubah Position Pre-setup #1 milik Ahmad Fauzi; Langkah Uji tidak menyebut pemulihannya.
  - TC-GS-ROLE-237 dan TC-GS-ROLE-240 tidak menyebut toast hasil Save dan Deactivate; spec tidak mengasersinya.
