---
id: TC-FA-GRP-E2E-200-log-pencabutan-assignment-saat-delete-di-log-user-dan-tanpa-notifikasi-in-app
title: "Pencatatan Log Pencabutan Assignment Saat Delete (di Log User, Bukan Changelog Group) dan Tanpa Notifikasi In-App"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-889
  - TC-FA-GRP-895
coverage:
  web: automated
---

# Pencatatan Log Pencabutan Assignment Saat Delete (di Log User, Bukan Changelog Group) dan Tanpa Notifikasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-200`): group `Del Users {runId}-200` dengan user A (Group Role), user B (Group Manager), dan user C (Transaction Role approver) ber-assignment di group itu; user Total Control dan Read Only (Pre-setup No 1 sampai 3) ada sehingga baris pola Group Role dan Transaction Role terbentuk di group itu (precondition TC-889, jumlahnya dibaca di langkah 2) (email fixture baru `Fixture.groupsLog.userA.email`, `userB`, `userC`); group `Del Notif {runId}-200` dengan user D yang punya Group Role di group itu (`Fixture.groupsLog.userD.email`). Password user: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog User, System Log, dan Activity Log sebelum aksi (baseline); membaca tab Group Role dan Transaction Role (Settings > Role & Permission) per node dan per user sebelum aksi.

## Test Steps
1. Catat baseline sebelum aksi, per surface: jumlah baris Changelog: Group yang memuat `Del Users {runId}-200`; jumlah baris Changelog: User, System Log, dan Activity Log FAMS yang kolom Note-nya memuat `Del Users {runId}-200` (penanda baris)

### TC-889: Log pencabutan assignment saat Delete

2. Baca jumlah baris pola Group Role dan Transaction Role user Total Control dan Read Only pada `Del Users {runId}-200` lewat kemampuan baca modul Role & Permission, lalu catat sebagai N (precondition TC-889, dipakai untuk asersi baris pola)
3. Buka Fixed Asset > Settings > Groups
4. Ketik Search `Del Users {runId}-200`, tekan Enter
5. Buka elipsis `Del Users {runId}-200`, pilih Delete
6. Klik [Delete]
7. Verifikasi toast sukses "Success, group has been deleted."
8. Buka Changelog: User
9. Filter dengan user A
10. Verifikasi entri pencabutan Group Role untuk user A (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus (format `[First Name] [Last Initial]`)
11. Filter dengan user B
12. Verifikasi entri pencabutan Group Manager untuk user B (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus
13. Filter dengan user C
14. Verifikasi entri pencabutan Transaction Role untuk user C (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus
15. Buka System Log
16. Verifikasi entri pencabutan sama untuk A, B, dan C pada System Log
17. Buka Activity Log FAMS
18. Verifikasi entri pencabutan sama untuk A, B, dan C pada Activity Log
19. Buka Fixed Asset > Settings > Groups
20. Buka Modal Changelog: Group
21. Filter Changelog dengan Group Name `Del Users {runId}-200`
22. Verifikasi Changelog: Group hanya berisi baris Delete `Del Users {runId}-200` (jumlah baris bertambah 1 dibanding baseline)
23. Tutup Modal Changelog
24. Buka Changelog: User
25. Verifikasi jumlah baris Changelog: User yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 + N dibanding baseline (entri user A, B, dan C serta N entri baris pola; tanpa entri Home Group)
26. Verifikasi pada Changelog: User terdapat N entri `Remove (Group Deleted)` yang memuat `Del Users {runId}-200`, satu entri per baris pola Group Role dan Transaction Role Total Control/Read Only (Group Role: seluruh baris per user; Transaction Role: Asset Admin dan Approver per user Total Control, Monitoring & Report per user Read Only, per Jenis Transaksi), bukan satu entri ringkas
27. Buka System Log
28. Verifikasi jumlah baris System Log yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 + N dibanding baseline (entri user A, B, dan C serta N entri baris pola; tanpa entri Home Group)
29. Verifikasi pada System Log terdapat N entri `Remove (Group Deleted)` yang memuat `Del Users {runId}-200`, satu entri per baris pola Group Role dan Transaction Role Total Control/Read Only (Group Role: seluruh baris per user; Transaction Role: Asset Admin dan Approver per user Total Control, Monitoring & Report per user Read Only, per Jenis Transaksi), bukan satu entri ringkas
30. Buka Activity Log FAMS
31. Verifikasi jumlah baris Activity Log yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 + N dibanding baseline (entri user A, B, dan C serta N entri baris pola; tanpa entri Home Group)
32. Verifikasi pada Activity Log terdapat N entri `Remove (Group Deleted)` yang memuat `Del Users {runId}-200`, satu entri per baris pola Group Role dan Transaction Role Total Control/Read Only (Group Role: seluruh baris per user; Transaction Role: Asset Admin dan Approver per user Total Control, Monitoring & Report per user Read Only, per Jenis Transaksi), bukan satu entri ringkas

### TC-895: Tanpa notifikasi in-app

33. Buka Fixed Asset > Settings > Groups
34. Ketik Search `Del Notif {runId}-200`, tekan Enter
35. Buka elipsis `Del Notif {runId}-200`, pilih Delete
36. Klik [Delete]
37. Verifikasi toast sukses "Success, group has been deleted."
38. Tunggu aksi selesai
39. Ganti akun: Logout, lalu login sebagai user D
40. Buka lonceng notifikasi
41. Verifikasi lonceng notifikasi terbuka dan daftar notifikasi tampil
42. Verifikasi tidak ada notifikasi terkait penghapusan group atau perubahan Excess

## Notes

- Aksi dan objek entri pencabutan (Action dan Object) mengikuti kebijakan pemilik (`settings-role-permission` §8) dan tidak diasersi (Expected TC-889 a).
- Langkah penghubung (S-03): baseline, Buka Fixed Asset > Settings > Groups sebelum aksi tiap blok dan sebelum membuka Modal Changelog: Group (baseline dan log meninggalkan halaman Groups; S-14), filter, menutup Modal Changelog, dan Tunggu aksi selesai sebelum Ganti akun ke user D (akun aktor login di hook `before`; hook `after` memulihkan sesi ke akun default).
- Baris target dicari lewat Search nama bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Spec memiliki 42 langkah, di atas smell 35 langkah. Alasan: dua blok satu topik (pencatatan pencabutan assignment saat Delete dan tanpa notifikasi in-app) dengan pola baca-log yang sama pada empat surface; tiap TC berdiri sendiri.
- Temuan untuk QA:
  - TC-889 dan 895 tidak menyebut cara membuka Changelog: User, System Log, dan lonceng notifikasi secara rinci; spec memakai penamaan TC. Assert absence notifikasi (TC-895) memakai anchor `Verifikasi` daftar notifikasi tampil (8b butir 2); TC tidak memberi pembanding notifikasi lain.
  - Email user A..D tidak ada di TC; spec memakai fixture baru ditetapkan tim FE.
  - TC-889 c: tanpa entri Home Group diasersi lewat selisih jumlah baris terhadap baseline pada penanda baris (Note memuat nama group `Del Users` bersuffix): Changelog: Group +1 (baris Delete), tiga surface lain +3 + N (entri A, B, dan C serta N entri baris pola Group Role dan Transaction Role yang memuat penanda yang sama), dengan entri pencabutan A, B, C sebagai anchor positif (langkah 10 sampai 18). TC-889 c menyebut "hanya entri A, B, dan C serta entri baris pola"; N dibaca dari precondition sebelum Delete (langkah 2).
