---
id: TC-FA-GRP-E2E-297-absence-import-group-di-bawah-node-gm-tanpa-notifikasi-tanpa-auto-revert-dan-kegagalan-tulis-baris-pola-me-rollback-group
title: "Absence Import Group di Bawah Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Auto-Revert, dan Kegagalan Penulisan Baris Pola GM Me-Rollback Group (Group Tidak Terbentuk)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1300
coverage:
  web: automated
---

# Absence Import Group di Bawah Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Auto-Revert, dan Kegagalan Penulisan Baris Pola GM Me-Rollback Group (Group Tidak Terbentuk)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (sama dengan spec 287 dan 289). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (hanya dibaca, tidak login): gmPattern Pre-setup No 28, gmPatternNested Pre-setup No 29, dan gmPatternOther Pre-setup No 30, masing-masing `<nama>_automated_{namaCompany}@qwertysystem.net`. Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 21, di-seed lewat sesi API aktor Total Control hanya untuk seeding di hook `before`, dihapus di hook `after`): `GM Pattern Child {runId}-297` (Assignable) di bawah `GM Pattern Parent {runId}-297` (Function None, level 1), dengan penugasan Group Manager gmPattern dan gmPatternNested yang mencakup Child dan baris pola GM yang sudah terbentuk, serta gmPatternOther di `GM Pattern Other {runId}-297`. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas di hook `after`.
- Data Dinamis yang dibuat oleh langkah spec (nama bersuffix `{runId}-297`; dihapus di hook `after`): berkas Import Group `Fixture.groupsGmPattern.importAbsen` memuat group `GM Abs Imp Sub {runId}-297` dengan parent `GM Pattern Child {runId}-297`, dan berkas `Fixture.groupsGmPattern.importGagal` memuat group `GM Gagal Imp Sub {runId}-297` dengan parent yang sama. Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).
- State client: Addon Audit tidak berlisensi (dipastikan fixture BE yang disediakan tim FE/BE, tidak diubah oleh spec ini).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission (Action dan jumlah entri per user dan per node), membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11), dan membaca keberadaan group beserta baris polanya lewat fixture BE.
- Pemicu kegagalan penulisan baris pola GM (TC-FA-GRP-1300 Expected e): disediakan oleh tim FE/BE. TC, PRD, dan LLD tidak memuat mekanisme pemicunya (S-13), sehingga spec ini tidak menyebut endpoint atau cara memaksa kegagalan, sama dengan spec 289; pemicu diaktifkan sebelum Import dan dimatikan sesudahnya (langkah 14), dengan hook `after` sebagai cadangan.

## Test Steps

### TC-FA-GRP-1300 (Expected c dan d): Import tanpa notifikasi in-app dan tanpa Auto-Revert

1. Catat baseline sebelum pemicu: jumlah notifikasi in-app dan jumlah entri `Auto-Revert` pada log Role & Permission untuk tiap penerima (gmPattern, gmPatternNested, gmPatternOther)
2. Buka modul Import, unggah berkas Group `Fixture.groupsGmPattern.importAbsen`
3. Jalankan import
4. Tunggu aksi selesai
5. Baca log Role & Permission untuk `GM Abs Imp Sub {runId}-297`
6. Verifikasi log memuat entri `Assign` untuk baris pola GM gmPattern dan gmPatternNested pada `GM Abs Imp Sub {runId}-297` (anchor: Import diproses dan log tercatat)
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Verifikasi jumlah notifikasi in-app tiap penerima sama dengan baseline langkah 1
9. Verifikasi jumlah entri `Auto-Revert` tiap penerima sama dengan baseline langkah 1

### TC-FA-GRP-1300 (Expected e): Kegagalan penulisan baris pola GM me-rollback group

10. Aktifkan pemicu kegagalan penulisan baris pola GM (kemampuan disediakan tim FE/BE)
11. Buka modul Import, unggah berkas Group `Fixture.groupsGmPattern.importGagal`
12. Jalankan import
13. Tunggu aksi selesai
14. Matikan pemicu kegagalan penulisan baris pola GM
15. Buka Fixed Asset > Settings > Groups
16. Ketik Search `GM Gagal Imp Sub {runId}-297`, tekan Enter
17. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `GM Gagal Imp Sub {runId}-297`
18. Baca keberadaan group bernama `GM Gagal Imp Sub {runId}-297` dan baris polanya lewat fixture BE
19. Verifikasi group `GM Gagal Imp Sub {runId}-297` tidak terbentuk dan tidak ada group tanpa baris pola GM
20. Klik `(←)` pada kotak Search

## Notes

- Spec memiliki 20 langkah. Langkah penghubung (S-03): langkah 4 dan 13 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), langkah 5 dan 18 (observasi lewat kemampuan baca), langkah 7 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), langkah 14 (mematikan pemicu segera sesudah Import, S-09), langkah 15 dan 16 (membuka Groups dan Search untuk menemukan baris target, R-16), dan langkah 20 (menutup Search).
- Pembagian TC lintas spec (S-05): TC-1300 muncul di `sourceTc` spec ini dan spec 296 (spec asal). Spec ini memuat aksi nyata (Import `GM Abs Imp Sub` dan Import `GM Gagal Imp Sub`) dengan baseline sendiri untuk asersi absence notifikasi in-app dan `Auto-Revert` (TC-1300 Expected c bagian absence, Expected d bagian `Auto-Revert`), dan untuk Expected e (group tidak terbentuk saat penulisan baris pola gagal). Presence diasersi di spec 296. Expected e disimpan di spec absence ini karena pemicu kegagalan hanya membentuk kondisi yang diasersi (group tidak ada), sama seperti spec 289 dan spec 201 (P-5 butir a).
- Temuan untuk QA:
  - TC-1300 Expected e ("jika penulisan baris pola gagal, group tidak terbentuk") tidak punya langkah pemicu kegagalan di TC, PRD, maupun LLD. Spec menuliskan pemicu sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan; tanpa pemicu itu langkah 10 sampai 19 tidak dapat dijalankan. Pemicu dan hasil Import yang gagal (pesan atau status di modul Import) perlu dilengkapi di TC.
  - TC-1300 tidak menyebut apa yang tampil di modul Import saat penulisan gagal; spec hanya mengasersi hasil data (group tidak terbentuk), bukan pesan.
  - Atomisitas diasersi lewat fixture BE (tidak ada group tanpa baris pola) karena UI hanya memperlihatkan group yang terbentuk.
  - Email Pre-setup No 28 sampai 30 dan akun importer belum punya nilai nyata di TC; berkas Import `importAbsen` dan `importGagal` adalah fixture yang disediakan tim FE/BE.
