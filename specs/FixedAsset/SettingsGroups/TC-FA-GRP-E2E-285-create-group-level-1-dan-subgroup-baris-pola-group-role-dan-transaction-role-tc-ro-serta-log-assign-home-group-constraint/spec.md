---
id: TC-FA-GRP-E2E-285-create-group-level-1-dan-subgroup-baris-pola-group-role-dan-transaction-role-tc-ro-serta-log-assign-home-group-constraint
title: "Create Group Level 1 dan Subgroup: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk, Mengabaikan Home Group Constraint, dan Log Assign per Baris"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1289
  - TC-FA-GRP-1291
coverage:
  web: automated
---

# Create Group Level 1 dan Subgroup: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk, Mengabaikan Home Group Constraint, dan Log Assign per Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (Create Subgroup TC-FA-GRP-1291): Manage Group R+C scope Region West, Pre-setup No 6 `manageGroupCreate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MGRC_PASSWORD`. Ganti akun eksplisit di langkah; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Region West); user Total Control No 1, Default User No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net`, dan Read Only No 3 `readOnlyGroups_automated_{namaCompany}@qwertysystem.net`.
- Data tambahan untuk TC-FA-GRP-1291 (di-seed lewat API di hook `before`, dihapus di hook `after`; Home Group `Home Luar {runId}-285` berada di luar node baru): user Total Control dengan Home Group constraint `Fixture.groupsPola.tcHome.email` dan user Read Only dengan Home Group constraint `Fixture.groupsPola.roHome.email`. Email kedua user tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data Dinamis (dibuat oleh langkah spec, dihapus di hook `after` lewat API):

| TC | Nama dibuat | Induk |
|---|---|---|
| TC-FA-GRP-1289 | `Pola Baru {runId}-285` | level 1 |
| TC-FA-GRP-1289 | `Pola Baru Sub {runId}-285` | `Pola Baru {runId}-285` |
| TC-FA-GRP-1291 | `Pola Home {runId}-285` | level 1 |
| TC-FA-GRP-1291 | `West Pola Home {runId}-285` | Region West |

- State client: Addon Audit tidak berlisensi (dipakai sebagai precondition TC-FA-GRP-1289, tidak diubah dan tidak diasersi oleh spec ini; keadaan itu dipastikan fixture BE yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Role dan tab Transaction Role (Settings > Role & Permission) per node dan per user, serta log Role & Permission (Action dan Modified By per entri). Node yang baru dibuat memakai nama bersuffix unik sehingga baseline entri log untuk penanda nama node adalah nol (S-12).

## Test Steps

### TC-FA-GRP-1289: Create Group level 1 dan Subgroup oleh Total Control

1. Klik [+] Group
2. Isi Group Name `Pola Baru {runId}-285`
3. Klik [Submit]
4. Verifikasi toast sukses `Success, group has been created.` untuk Create Group level 1
5. Klik (⋯) pada node `Pola Baru {runId}-285` di sidebar
6. Klik `Add Subgroup`
7. Isi Group Name `Pola Baru Sub {runId}-285`
8. Klik [Submit]
9. Verifikasi toast sukses `Success, group has been created.` untuk Create Subgroup
10. Baca tab Group Role pada `Pola Baru {runId}-285` dan `Pola Baru Sub {runId}-285` lewat kemampuan baca modul Role & Permission
11. Verifikasi pada kedua node, baris pola Group Role terbentuk untuk setiap user Total Control (Pre-setup No 1 dan Default User) dengan seluruh baris Group Role CRUD penuh
12. Verifikasi pada kedua node, baris pola Group Role terbentuk untuk setiap user Read Only (Pre-setup No 3) dengan seluruh baris Group Role Read saja
13. Baca tab Transaction Role pada kedua node lewat kemampuan baca modul Role & Permission
14. Verifikasi pada kedua node, setiap Jenis Transaksi (tujuh, termasuk Addon yang lisensinya belum aktif) memuat baris Asset Admin dan Approver untuk setiap user Total Control (termasuk Default User)
15. Verifikasi pada kedua node, setiap Jenis Transaksi (tujuh) memuat baris Monitoring & Report saja untuk setiap user Read Only, tanpa baris Approver
16. Verifikasi tier Total Control user Total Control (termasuk Default User) dan tier Read Only user Read Only tetap terpasang pada pembacaan Role & Permission (tidak terlepas)
17. Verifikasi kedua node sudah memuat baris pola Group Role dan Transaction Role lengkap pada pembacaan pertama sesudah toast sukses Create masing-masing (tidak ada kondisi node tanpa baris pola)

### TC-FA-GRP-1291: Create Group level 1 oleh Total Control dan Subgroup oleh Manage Group R+C, user dengan Home Group constraint

18. Klik [+] Group
19. Isi Group Name `Pola Home {runId}-285`
20. Klik [Submit]
21. Verifikasi toast sukses `Success, group has been created.` untuk Create Group level 1
22. Tunggu aksi selesai
23. Ganti akun: Logout, lalu login sebagai Manage Group R+C dengan `Spectra.env.FA_MGRC_PASSWORD`
24. Buka Fixed Asset > Settings > Groups
25. Klik (⋯) pada node Region West di sidebar
26. Klik `Add Subgroup`
27. Isi Group Name `West Pola Home {runId}-285`
28. Klik [Submit]
29. Verifikasi toast sukses `Success, group has been created.` untuk Create Subgroup
30. Baca tab Group Role pada `Pola Home {runId}-285` dan `West Pola Home {runId}-285` lewat kemampuan baca modul Role & Permission
31. Verifikasi pada kedua node, baris pola Group Role terbentuk untuk user Total Control dengan Home Group constraint dan Default User dengan seluruh baris Group Role CRUD penuh, mengabaikan Home Group constraint
32. Verifikasi pada kedua node, baris pola Group Role terbentuk untuk user Read Only dengan Home Group constraint dengan seluruh baris Group Role Read saja, mengabaikan Home Group constraint
33. Baca log Role & Permission untuk `Pola Home {runId}-285` dan `West Pola Home {runId}-285`
34. Verifikasi log memuat satu entri `Assign` biasa per baris pola Group Role yang dibaca pada langkah 30, untuk kedua node
35. Verifikasi Modified By entri pada `Pola Home {runId}-285` adalah aktor Total Control dan pada `West Pola Home {runId}-285` adalah aktor Manage Group R+C (format `[First Name] [Last Initial]`)

## Notes

- Spec memiliki 35 langkah, pada batas 35 langkah. Dua TC satu topik (Create Group level 1 dan Subgroup) pada pola yang sama dan aktor yang berbeda; tiap TC berdiri sendiri.
- Langkah penghubung (S-03): langkah 22 (tunggu aksi selesai sebelum ganti akun, 8b butir 8), langkah 23 dan 24 (ganti akun eksplisit, membuka halaman Groups sesudah login, S-07 dan S-14), dan pembacaan pada langkah 10, 13, 30, dan 33 (observasi lewat kemampuan baca, bukan aksi UI).
- Pembagian TC lintas spec: TC-1289 dan TC-1291 muncul di `sourceTc` spec ini dan spec 288 (absence, S-05). Spec ini mengasersi presence: toast Create (Expected a), baris pola Group Role dan Transaction Role (b0 dan b), tier tidak terlepas (c), kelengkapan baris pola pada pembacaan pertama (d) untuk TC-1289; baris pola Group Role mengabaikan Home Group constraint (a), entri `Assign` per baris dan Modified By (b) untuk TC-1291. Asersi tidak adanya entri `Auto-Revert` (TC-1289 c; TC-1291 b "bukan entri Auto-Revert") dan tidak adanya notifikasi in-app ke user Total Control/Read Only (TC-1291 c) ada di spec 288 dengan baseline sendiri.
- Temuan untuk QA:
  - TC-1291 langkah 3 dan 4 membaca Settings > Role & Permission, log, dan notifikasi oleh aktor Manage Group R+C yang tidak jelas berhak membuka modul itu (sama dengan temuan spec 020); spec memakai kemampuan baca yang disediakan tim FE/BE.
  - Email user Total Control dan Read Only dengan Home Group constraint tidak ada di Pre-setup TC; spec memakai fixture baru yang ditetapkan tim FE.
  - TC-1289 Expected d ("dalam transaksi yang sama dengan Create") tidak teramati langsung dari UI; spec mengasersi hasil yang teramati (tidak ada node tanpa baris pola pada pembacaan pertama). Atomisitas transaksi diuji lewat kegagalan tulis di spec 289 untuk jalur Import; TC untuk jalur Create tidak memberi pemicunya.
  - TC-1291 Expected b menyebut "satu entri `Assign` biasa per baris pola" tanpa menyebut tab; spec membatasinya pada baris pola Group Role (tab yang dibuka di langkah 3 TC).
