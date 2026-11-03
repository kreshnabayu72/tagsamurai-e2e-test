---
id: TC-AC-LCS-E2E-133-log-save-lifecycle-recycle-approval-limits
title: "Pencatatan Log: Save Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Menulis Entri di System Log dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-481
  - TC-AC-LCS-482
  - TC-AC-LCS-483
  - TC-AC-LCS-484
coverage:
  web: automated
---

# Pencatatan Log: Save Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Menulis Entri di System Log dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- General Settings: Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC (tidak diubah spec ini). Jam server dan jam browser tidak digeser.
- Data: user `Andi Wijaya` (Total Control) memiliki Detail user dengan tab System Log; entri System Log dan Activity Log bersifat permanen sehingga spec memakai baseline jumlah entri sebelum aksi (S-12), bukan angka absolut.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan ketujuh tab ke nilai default; kemampuan membaca jumlah entri System Log aktor dan Activity Log Admin Console sebelum aksi.
- Pemulihan: ketujuh tab dipulihkan ke nilai default oleh langkah penghubung antar TC dan hook `after` suite; entri log yang ditulis spec ini permanen dan tidak dihapus.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-481: Save tab Client Lifecycle menulis entri pada System Log aktor dan Activity Log Admin Console

1. Klik tab `Client Lifecycle`
2. Ubah Notify Plan Owner Before Event dari `45` menjadi `46`
3. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
4. Klik `[Save]` dan tunggu toast sukses
5. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
6. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Notify Plan Owner Before Event`, Old Value `45`, New Value `46`, Date sesuai General Settings, tanpa kolom Modified By
7. Buka Activity Log (Admin Console)
8. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Notify Plan Owner Before Event`, Old Value `45`, New Value `46`, Modified By `Andi W`
9. Hover nilai Modified By pada entri baru Activity Log
10. Verifikasi tooltip `Andi Wijaya` tampil
11. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-482: Save tab Recycle Bin menulis entri pada System Log aktor dan Activity Log Admin Console

12. Klik tab `Recycle Bin`
13. Ubah Permanently Delete Recycle Bin dari `30` menjadi `31`
14. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
15. Klik `[Save]` dan tunggu toast sukses
16. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
17. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Permanently Delete Recycle Bin`, Old Value `30`, New Value `31`, Date sesuai General Settings, tanpa kolom Modified By
18. Buka Activity Log (Admin Console)
19. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Permanently Delete Recycle Bin`, Old Value `30`, New Value `31`, Modified By `Andi W`
20. Hover nilai Modified By pada entri baru Activity Log
21. Verifikasi tooltip `Andi Wijaya` tampil
22. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-483: Save tab Approval Settings menulis entri pada System Log aktor dan Activity Log Admin Console

23. Klik tab `Approval Settings`
24. Ubah Approval Timeout dari `3` menjadi `4`
25. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
26. Klik `[Save]` dan tunggu toast sukses
27. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
28. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Approval Timeout`, Old Value `3`, New Value `4`, Date sesuai General Settings, tanpa kolom Modified By
29. Buka Activity Log (Admin Console)
30. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Approval Timeout`, Old Value `3`, New Value `4`, Modified By `Andi W`
31. Hover nilai Modified By pada entri baru Activity Log
32. Verifikasi tooltip `Andi Wijaya` tampil
33. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-484: Save tab System Limits menulis entri pada System Log aktor dan Activity Log Admin Console

34. Klik tab `System Limits`
35. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`
36. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
37. Klik `[Save]` dan tunggu toast sukses
38. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
39. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Bulk Transaction Row Limit`, Old Value `1000`, New Value `1001`, Date sesuai General Settings, tanpa kolom Modified By
40. Buka Activity Log (Admin Console)
41. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Bulk Transaction Row Limit`, Old Value `1000`, New Value `1001`, Modified By `Andi W`
42. Hover nilai Modified By pada entri baru Activity Log
43. Verifikasi tooltip `Andi Wijaya` tampil

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab terkait), "Catat jumlah entri ... sebagai baseline" (S-12), dan "Pulihkan ketujuh tab ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (S-03, S-09).
- Entri baru pada System Log dan Activity Log dikenali lewat kenaikan satu dari baseline dan kolom Field, Old Value, New Value, bukan lewat posisi "teratas", karena audit trail permanen tumbuh (S-12, S-14). Satu `Verifikasi` memuat seluruh kolom satu entri log dan keterangan "tanpa kolom Modified By" pada System Log (S-01).
- Temuan untuk QA: TC menulis "amati entri teratas" tanpa baseline; kolom `Name` bernilai `—` dan mekanisme membaca jumlah entri tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC (entri tercatat pada kedua surface) tidak punya langkah observasi di luar Expected dan tidak diasersi terpisah (S-01).
- Alasan lebih dari sekitar 35 langkah: empat blok memakai pola yang sama (Save satu tab lalu membaca System Log dan Activity Log), semuanya satu kelas pencatatan log, dan tiap blok dimulai dari state default yang dipulihkan langkah penghubung sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
