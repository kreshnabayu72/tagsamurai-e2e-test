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
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before`, dihapus di hook `after`; nama bersuffix `{runId}-200`): group `Del Users {runId}-200` dengan user A (Group Role), user B (Group Manager), dan user C (Transaction Role approver) ber-assignment di group itu (email fixture baru `Fixture.groupsLog.userA.email`, `userB`, `userC`); group `Del Notif {runId}-200` dengan user D yang punya Group Role di group itu (`Fixture.groupsLog.userD.email`). Password user: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog User, System Log, dan Activity Log sebelum aksi (baseline).

## Test Steps

1. Catat baseline sebelum aksi, per surface: jumlah baris Changelog: Group yang memuat `Del Users {runId}-200`; jumlah baris Changelog: User, System Log, dan Activity Log FAMS yang kolom Note-nya memuat `Del Users {runId}-200` (penanda baris)

### TC-889: Log pencabutan assignment saat Delete

2. Buka Fixed Asset > Settings > Groups
3. Ketik Search `Del Users {runId}-200`, tekan Enter
4. Buka elipsis `Del Users {runId}-200`, pilih Delete
5. Klik [Delete]
6. Verifikasi toast sukses "Success, group has been deleted."
7. Buka Changelog: User
8. Filter dengan user A
9. Verifikasi entri pencabutan Group Role untuk user A (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus (format `[First Name] [Last Initial]`)
10. Filter dengan user B
11. Verifikasi entri pencabutan Group Manager untuk user B (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus
12. Filter dengan user C
13. Verifikasi entri pencabutan Transaction Role untuk user C (Note memuat `Del Users {runId}-200`) dengan pelaku admin penghapus
14. Buka System Log
15. Verifikasi entri pencabutan sama untuk A, B, dan C pada System Log
16. Buka Activity Log FAMS
17. Verifikasi entri pencabutan sama untuk A, B, dan C pada Activity Log
18. Buka Fixed Asset > Settings > Groups
19. Buka Modal Changelog: Group
20. Filter Changelog dengan Group Name `Del Users {runId}-200`
21. Verifikasi Changelog: Group hanya berisi baris Delete `Del Users {runId}-200` (jumlah baris bertambah 1 dibanding baseline)
22. Tutup Modal Changelog
23. Buka Changelog: User
24. Verifikasi jumlah baris Changelog: User yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 dibanding baseline (hanya entri user A, B, dan C; tanpa entri Home Group)
25. Buka System Log
26. Verifikasi jumlah baris System Log yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 dibanding baseline (hanya entri user A, B, dan C; tanpa entri Home Group)
27. Buka Activity Log FAMS
28. Verifikasi jumlah baris Activity Log yang Note-nya memuat `Del Users {runId}-200` bertambah tepat 3 dibanding baseline (hanya entri user A, B, dan C; tanpa entri Home Group)

### TC-895: Tanpa notifikasi in-app

29. Buka Fixed Asset > Settings > Groups
30. Ketik Search `Del Notif {runId}-200`, tekan Enter
31. Buka elipsis `Del Notif {runId}-200`, pilih Delete
32. Klik [Delete]
33. Verifikasi toast sukses "Success, group has been deleted."
34. Tunggu aksi selesai
35. Ganti akun: Logout, lalu login sebagai user D
36. Buka lonceng notifikasi
37. Verifikasi lonceng notifikasi terbuka dan daftar notifikasi tampil
38. Verifikasi tidak ada notifikasi terkait penghapusan group atau perubahan Excess

## Notes

- Aksi dan objek entri pencabutan (Action dan Object) mengikuti kebijakan pemilik (`settings-role-permission` §8) dan tidak diasersi (Expected TC-889 a).
- Langkah penghubung (S-03): baseline, Buka Fixed Asset > Settings > Groups sebelum aksi tiap blok dan sebelum membuka Modal Changelog: Group (baseline dan log meninggalkan halaman Groups; S-14), filter, menutup Modal Changelog, dan Tunggu aksi selesai sebelum Ganti akun ke user D (akun aktor login di hook `before`; hook `after` memulihkan sesi ke akun default).
- Baris target dicari lewat Search nama bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Spec memiliki 38 langkah, di atas smell 35 langkah. Alasan: dua blok satu topik (pencatatan pencabutan assignment saat Delete dan tanpa notifikasi in-app) dengan pola baca-log yang sama pada empat surface; tiap TC berdiri sendiri.
- Temuan untuk QA:
  - TC-889 dan 895 tidak menyebut cara membuka Changelog: User, System Log, dan lonceng notifikasi secara rinci; spec memakai penamaan TC. Assert absence notifikasi (TC-895) memakai anchor `Verifikasi` daftar notifikasi tampil (8b butir 2); TC tidak memberi pembanding notifikasi lain.
  - Email user A..D tidak ada di TC; spec memakai fixture baru ditetapkan tim FE.
  - TC-889 c: tanpa entri Home Group diasersi lewat selisih jumlah baris terhadap baseline pada penanda baris (Note memuat nama group `Del Users` bersuffix): Changelog: Group +1 (baris Delete), tiga surface lain +3 (hanya entri A, B, dan C), dengan entri pencabutan A, B, C sebagai anchor positif (langkah 9 sampai 17).
