---
id: TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning
title: "Delete Group: Dialog Warning User Ter-Scope, Warning User di Descendant, dan [Cancel] pada Dialog Warning"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-223
  - TC-FA-GRP-224
  - TC-FA-GRP-1033
coverage:
  web: automated
---

# Delete Group: Dialog Warning User Ter-Scope, Warning User di Descendant, dan [Cancel] pada Dialog Warning

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): `Del Users` (tanpa aset aktif, dua user ber-Group Role di node: `User GR 1` dan `User GR 2`, email `userGr1+{runId}-072@qwertysystem.net` dan `userGr2+{runId}-072@qwertysystem.net`); `Del Users Parent` dengan child `Del Users Child` (tanpa aset; di child: `User GR 3` ber-Group Role, `User GM 1` ber-tier Group Manager dengan baris pola GM di child, dan `User TR 1` ber-Transaction Role approver, email bersuffix `{runId}-072`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog user pada Settings > Role & Permission sebelum dan sesudah aksi (audit trail permanen; 8b butir 10). Password user seed tidak dipakai (spec hanya membaca Role & Permission).
- Baseline log: N0 = jumlah entri Changelog `User GR 1` yang dicatat pada langkah 3, sebelum aksi pemicu pertama yang diasersi (S-12). R = jumlah baris pola GM `User GM 1` di `Del Users Child` dan M0 = jumlah entri `Remove (Group Deleted)` pada Changelog `User GM 1`, keduanya dicatat pada langkah 4 sebelum aksi Delete TC-224 (audit trail permanen dibaca lewat kemampuan baca, 8b butir 10). Pembentukan baris pola GM `User GM 1` di child disediakan tim FE/BE tanpa endpoint karangan.
- Cleanup di `after`: hapus data milik spec yang tersisa (`Del Users`, user seed) lewat API.

## Test Steps

### Baseline Changelog user

1. Buka Settings > Role & Permission, pilih `User GR 1`, klik icon Changelog
2. Verifikasi sedikitnya satu entri tampil di Changelog `User GR 1`
3. Catat jumlah entri Changelog `User GR 1` sebagai baseline N0
4. Buka Settings > Role & Permission, pilih `User GM 1`, baca baris pola GM pada `Del Users Child` lewat kemampuan baca, lalu klik icon Changelog; catat jumlah baris pola GM sebagai R dan jumlah entri `Remove (Group Deleted)` pada Changelog `User GM 1` sebagai baseline M0
5. Tutup Changelog dan buka Fixed Asset > Settings > Groups

### TC-FA-GRP-223: Screening dialog Warning Delete, user ter-scope

6. Ketik Search `Del Users`, tekan Enter
7. Buka elipsis `⋯` baris `Del Users`, pilih `Delete`
8. Verifikasi dialog dengan title "Delete Group", bullet `Del Users`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?", tombol [Cancel] dan [Delete]

### TC-FA-GRP-1033: [Cancel] pada dialog Warning

9. Klik [Cancel] pada dialog
10. Verifikasi dialog tertutup
11. Verifikasi `Del Users` tetap ada di tabel
12. Verifikasi `Del Users` tetap ada di sidebar
13. Verifikasi tidak ada toast yang tampil
14. Buka Settings > Role & Permission, pilih `User GR 1`
15. Verifikasi Group Role `User GR 1` di `Del Users` tidak dicabut
16. Klik icon Changelog
17. Verifikasi jumlah entri Changelog `User GR 1` sama dengan baseline N0 (tanpa baris Delete baru)
18. Tutup Changelog dan buka Fixed Asset > Settings > Groups

### TC-FA-GRP-224: Warning untuk user ter-scope di descendant, lalu commit

19. Ketik Search `Del Users Parent`, tekan Enter
20. Buka elipsis `⋯` baris `Del Users Parent`, pilih `Delete`
21. Verifikasi dialog varian warning memuat himpunan node dan descendant: title "Delete Group", bullet `Del Users Parent` dan `Del Users Child`, isi "This group has users assigned — deleting it will remove their group roles. This action cannot be undone. Are you sure you want to delete it?"
22. Klik [Delete] pada dialog warning
23. Verifikasi toast sukses "Success, group has been deleted."
24. Verifikasi `Del Users Parent` dan `Del Users Child` terhapus dari tabel dan sidebar
25. Buka Settings > Role & Permission, pilih `User GR 3`
26. Verifikasi nama user `User GR 3` tampil pada detail user di Role & Permission
27. Verifikasi assignment Group Role `User GR 3` terlepas
28. Buka Settings > Role & Permission, pilih `User GM 1`
29. Verifikasi nama user `User GM 1` tampil pada detail user di Role & Permission
30. Verifikasi assignment Group Manager `User GM 1` terlepas
31. Verifikasi tidak ada sisa baris pola GM `User GM 1` pada `Del Users Child`
32. Klik icon Changelog
33. Verifikasi jumlah entri `Remove (Group Deleted)` pada Changelog `User GM 1` bertambah tepat R dibanding baseline M0, satu entri per baris pola GM yang terhapus
34. Buka Settings > Role & Permission, pilih `User TR 1`
35. Verifikasi nama user `User TR 1` tampil pada detail user di Role & Permission
36. Verifikasi assignment Transaction Role `User TR 1` terlepas

## Notes

- Spec melewati sekitar 35 langkah (36 langkah): seluruh blok satu topik Delete dengan dialog Warning pada dataset `Del Users` yang sama dan tiap blok berdiri sendiri; Expected c baru TC-224 (baris pola GM ikut terhapus beserta penugasan GM) menambah empat langkah (langkah 4, 31, 32, 33).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3, 4 dan 5, 14, 16, 18, 25, 28, 32, 34: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pencarian baris target (S-03, R-16): langkah 6 dan 19 (Ketik Search `Del Users` dan `Del Users Parent`, tekan Enter) menemukan baris yang dibuka elipsisnya; Search kosong sesudah langkah 18 karena halaman Groups dibuka ulang; client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Urutan: TC-223 dan TC-1033 memakai satu pembukaan dialog `Del Users` (diasersi lalu dibatalkan); Delete yang menghapus data (TC-224) paling akhir (S-10).
- Klausa "tanpa toast dan tanpa baris Delete baru di Changelog" (TC-1033) diasersi pada langkah 13 dan 17; anchor positif: langkah 2 (entri lain tampil) dan langkah 11 (`Del Users` tetap ada). Baris hilang sesudah Delete memakai toast sukses sebagai anchor (8b butir 2). Asersi "terlepas" pada langkah 27, 30, dan 36 didahului `Verifikasi` nama user tampil di Role & Permission (langkah 26, 29, 35) sebagai anchor permukaan (8b butir 2); asersi tidak ada sisa baris pola GM `User GM 1` (langkah 31) memakai anchor nama user tampil yang sama (langkah 29).
- Temuan untuk QA:
  - TC-1033 langkah 5 ("Klik icon Changelog") tidak menyebut Changelog mana; spec memakai Changelog user pada Role & Permission sesuai langkah 4 TC. Changelog Group tidak diasersi.
  - TC-224 Expected c menyebut Transaction Role, sedangkan Precondition hanya menyebut user Group Role dan Group Manager; spec menambah `User TR 1` ber-Transaction Role di seeding supaya Expected c dapat diasersi.
  - TC-224 Post Condition a (entri log pencabutan per assignment) dan b (tidak ada notifikasi in-app) tidak punya langkah observasi; tidak diasersi (S-01). Post Condition c (satu entri `Remove (Group Deleted)` per baris pola GM) diasersi lewat selisih jumlah entri Changelog `User GM 1` (langkah 33); surface System Log dan Activity Log tidak diasersi di spec ini (diasersi di spec 200 untuk TC-889).
  - TC-224 Pre c dan Expected c menyebut baris pola GM `User GM 1` di child tanpa mekanisme seeding yang ditegaskan; spec menuliskannya sebagai kemampuan tim FE/BE tanpa endpoint karangan. Dialog Warning pada TC-224 mengikuti TC; apakah baris pola GM ikut menghitung kondisi 5 guard Delete masih NC-12 (Menunggu konfirmasi, PRD FAGRP-LOGIC-03k).
