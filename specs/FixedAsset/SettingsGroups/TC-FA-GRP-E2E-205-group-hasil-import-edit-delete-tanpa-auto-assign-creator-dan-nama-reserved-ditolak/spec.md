---
id: TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak
title: "Group Hasil Import: Edit dan Delete Identik dengan Group Manual, Tanpa Auto-Assign Creator, dan Import dengan Nama All Groups Ditolak"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-911
  - TC-FA-GRP-912
  - TC-FA-GRP-913
  - TC-FA-GRP-1026
coverage:
  web: automated
---

# Group Hasil Import: Edit dan Delete Identik dengan Group Manual, Tanpa Auto-Assign Creator, dan Import dengan Nama All Groups Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun importer: user ber-Global Role Import Data, `Fixture.groupsLog.importer.email`, password `Spectra.env.FA_GRP_IMPORTER_PASSWORD` (env baru; didaftarkan di tempat yang sama dengan `FA_TC_PASSWORD`); akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan; nama bersuffix `{runId}-205`; dibuat lewat Import oleh sesi API importer di hook `before`, dihapus di hook `after`): `Branch C {runId}-205` (Code kosong di berkas, Function sesuai berkas), `Branch D {runId}-205` (kosong), `Branch E {runId}-205` (dibuat oleh importer). Berkas Import Group dengan Group Name `  all groups  ` (`Fixture.groupsImport.reservedName`). Kemampuan import Group untuk importer disediakan tim FE/BE (alur dan berkas tidak ada di TC, PRD, atau LLD, S-13).

## Test Steps

1. Catat jumlah baris Changelog Group yang memuat `Branch C {runId}-205`

### TC-911: Edit identik dengan group manual

2. Amati baris `Branch C {runId}-205` pada Groups List
3. Verifikasi Code `Branch C {runId}-205` hasil auto-generate (tidak kosong)
4. Verifikasi Function `Branch C {runId}-205` sesuai berkas dan tampil sama seperti group manual
5. Buka elipsis `Branch C {runId}-205`, pilih Edit, ubah Description menjadi `Import notes`, klik [Save]
6. Verifikasi toast sukses "Success, group has been updated."
7. Buka Modal Changelog: Group
8. Filter Changelog dengan Group Name `Branch C {runId}-205`
9. Verifikasi baris Edit Description tampil (jumlah baris bertambah dibanding baseline)
10. Tutup Modal Changelog

### TC-912: Delete identik dengan group manual

11. Buka elipsis `Branch D {runId}-205`, pilih Delete
12. Verifikasi dialog konfirmasi Delete normal tampil
13. Klik [Delete]
14. Verifikasi toast sukses "Success, group has been deleted."

### TC-913: Tanpa auto-assign creator (akun importer)

15. Ganti akun: Logout, lalu login sebagai importer
16. Buka Settings > Role & Permission aktor
17. Verifikasi Global Role Import Data aktor tampil di Settings > Role & Permission aktor (anchor)
18. Verifikasi tidak ada assignment Manage Group otomatis untuk aktor di `Branch E {runId}-205`
19. Buka Fixed Asset > Settings > Groups
20. Verifikasi `Branch E {runId}-205` tetap valid sebagai group level 1

### TC-1026: Import dengan nama reserved ditolak

21. Catat jumlah baris Changelog Group yang memuat Group Name All Groups
22. Buka modul Import, unggah berkas Group `Fixture.groupsImport.reservedName`
23. Jalankan import
24. Verifikasi baris ditolak dengan pesan "'All Groups' is a reserved name and cannot be used"
25. Buka Fixed Asset > Settings > Groups, ketik Search `All Groups`, tekan Enter
26. Verifikasi tabel Groups List menampilkan empty state "No results found" (tidak memuat baris bernama All Groups)
27. Klik icon Changelog
28. Verifikasi Changelog tidak memuat baris Create dari baris import tersebut (jumlah baris sama dengan baseline)
29. Tutup Modal Changelog
30. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): baseline, filter Changelog, menutup Modal Changelog, `(←)` pada kotak Search, dan Ganti akun ke importer (akun aktor pertama login di hook `before`; hook `after` memulihkan sesi ke akun default). TC-911 dan 912 dijalankan sebagai Total Control, TC-913 dan 1026 sebagai importer.
- Temuan untuk QA:
  - TC-911 dan 912 tidak menyebut akun aktor (ACC kosong); spec memakai Total Control. TC-913 dan TC-1026 membutuhkan akun importer yang tidak ada di Pre-setup. Alur modul Import (menu, berkas, jalan import) tidak dirinci di TC; spec mengikuti teks TC.
  - TC-913 a: asersi absence assignment Manage Group memakai Global Role Import Data aktor (precondition a TC) sebagai anchor positif pada halaman Role & Permission yang sama (8b butir 2, S-03); TC tidak menyebut anchor itu.
  - TC-1026 asersi absence "tabel tidak memuat All Groups" memakai empty state hasil Search sebagai anchor positif (8b butir 2); baris Create dari import diasersi lewat selisih terhadap baseline.
