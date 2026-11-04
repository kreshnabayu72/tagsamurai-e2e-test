---
id: TC-FA-GRP-E2E-289-absence-import-group-pola-tanpa-notifikasi-in-app-dan-kegagalan-tulis-baris-pola-me-rollback-group
title: "Absence Import Group: Tanpa Notifikasi In-App ke User Total Control/Read Only, dan Kegagalan Penulisan Baris Pola Me-Rollback Group (Group Tidak Terbentuk)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-1292
coverage:
  web: automated
---

# Absence Import Group: Tanpa Notifikasi In-App ke User Total Control/Read Only, dan Kegagalan Penulisan Baris Pola Me-Rollback Group (Group Tidak Terbentuk)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: user ber-Global Role Import Data (bukan Total Control dan bukan Default User), `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Penerima yang diamati (user Total Control dan Read Only): Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`, user Total Control dengan Home Group constraint `Fixture.groupsPola.tcHome.email`, dan user Read Only dengan Home Group constraint `Fixture.groupsPola.roHome.email` (di-seed lewat API di hook `before`, dihapus di hook `after`).
- Data Dinamis (nama bersuffix `{runId}-289`; dihapus di hook `after`): berkas Import Group `Fixture.groupsImport.branchAbsen` memuat group `Branch Absen {runId}-289` (level 1), dan berkas `Fixture.groupsImport.branchGagal` memuat group `Branch Gagal {runId}-289` (level 1). Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca log Role & Permission per node (entri `Assign`), membaca jumlah notifikasi in-app per penerima (baseline per penerima, 8b butir 10), langkah `Tunggu 5 detik tanpa memuat ulang halaman` sebelum asersi absence notifikasi (8b butir 11), dan membaca keberadaan group beserta baris polanya lewat fixture BE.
- Pemicu kegagalan penulisan baris pola (TC-FA-GRP-1292 Expected d): disediakan oleh tim FE/BE. TC, PRD, dan LLD tidak memuat mekanisme pemicunya (S-13), sehingga spec ini tidak menyebut endpoint atau cara memaksa kegagalan; pemicu diaktifkan sebelum Import dan dimatikan sesudahnya (langkah 13), dengan hook `after` sebagai cadangan.

## Test Steps

### TC-FA-GRP-1292 (Expected c): Import tanpa notifikasi in-app

1. Catat baseline sebelum pemicu: jumlah notifikasi in-app tiap penerima (Default User, Read Only, user Total Control Home Group, user Read Only Home Group)
2. Buka modul Import, unggah berkas Group `Fixture.groupsImport.branchAbsen`
3. Jalankan import
4. Tunggu aksi selesai
5. Baca log Role & Permission untuk `Branch Absen {runId}-289`
6. Verifikasi log memuat entri `Assign` untuk baris pola pada `Branch Absen {runId}-289` (anchor: Import diproses dan log tercatat)
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Verifikasi jumlah notifikasi in-app tiap penerima sama dengan baseline langkah 1

### TC-FA-GRP-1292 (Expected d): Kegagalan penulisan baris pola me-rollback group

9. Aktifkan pemicu kegagalan penulisan baris pola (kemampuan disediakan tim FE/BE)
10. Buka modul Import, unggah berkas Group `Fixture.groupsImport.branchGagal`
11. Jalankan import
12. Tunggu aksi selesai
13. Matikan pemicu kegagalan penulisan baris pola
14. Buka Fixed Asset > Settings > Groups
15. Ketik Search `Branch Gagal {runId}-289`, tekan Enter
16. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Branch Gagal {runId}-289`
17. Baca keberadaan group bernama `Branch Gagal {runId}-289` dan baris polanya lewat fixture BE
18. Verifikasi group `Branch Gagal {runId}-289` tidak terbentuk dan tidak ada group tanpa baris pola
19. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 4 dan 12 (tunggu aksi selesai sebelum berpindah surface, 8b butir 8), langkah 5 dan 17 (observasi lewat kemampuan baca), langkah 7 (jeda 5 detik tanpa memuat ulang sebelum asersi absence notifikasi, 8b butir 11), langkah 13 (mematikan pemicu segera sesudah Import, S-09), langkah 14 dan 15 (membuka Groups dan Search untuk menemukan baris target, R-16), dan langkah 19 (menutup Search).
- Pembagian TC lintas spec: TC-1292 muncul di `sourceTc` spec ini dan spec 287 (spec asal, S-05). Spec ini memuat aksi nyata (Import `Branch Absen` dan Import `Branch Gagal`) dengan baseline sendiri untuk asersi absence notifikasi in-app (TC-1292 Expected c) dan untuk Expected d (group tidak terbentuk saat penulisan baris pola gagal). Presence (baris pola Group Role dan Transaction Role, user non-TC/RO tidak diturunkan, entri `Assign` dan Modified By) diasersi di spec 287. Expected d disimpan di spec absence ini karena pemicu kegagalan hanya membentuk kondisi yang diasersi (group tidak ada), sama seperti spec 201 yang memuat kegagalan tulis Activity Log.
- Temuan untuk QA:
  - TC-1292 Expected d ("jika penulisan baris pola gagal, group tidak terbentuk") tidak punya langkah pemicu kegagalan di TC, PRD, maupun LLD. Spec menuliskan pemicu sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan; tanpa pemicu itu langkah 9 sampai 18 tidak dapat dijalankan. Pemicu dan hasil Import yang gagal (pesan atau status di modul Import) perlu dilengkapi di TC.
  - TC-1292 tidak menyebut apa yang tampil di modul Import saat penulisan gagal; spec hanya mengasersi hasil data (group tidak terbentuk), bukan pesan.
  - Atomisitas diasersi lewat fixture BE (tidak ada group tanpa baris pola) karena UI hanya memperlihatkan group yang terbentuk.
  - Akun importer tidak ada di Pre-setup TC; berkas Import `branchAbsen` dan `branchGagal` adalah fixture yang disediakan tim FE/BE.
