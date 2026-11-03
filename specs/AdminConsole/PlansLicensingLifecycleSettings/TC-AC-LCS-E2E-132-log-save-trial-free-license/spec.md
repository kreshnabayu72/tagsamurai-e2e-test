---
id: TC-AC-LCS-E2E-132-log-save-trial-free-license
title: "Pencatatan Log: Save Tab Trial Settings, Free Plan Settings, dan License Timing Menulis Entri di System Log dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-478
  - TC-AC-LCS-479
  - TC-AC-LCS-480
coverage:
  web: automated
---

# Pencatatan Log: Save Tab Trial Settings, Free Plan Settings, dan License Timing Menulis Entri di System Log dan Activity Log

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

### TC-AC-LCS-478: Save tab Trial Settings menulis entri pada System Log aktor dan Activity Log Admin Console

1. Ubah Max Trial Duration dari `30` menjadi `31`
2. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
3. Klik `[Save]` dan tunggu toast sukses
4. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
5. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Max Trial Duration`, Old Value `30`, New Value `31`, Date sesuai General Settings, tanpa kolom Modified By
6. Buka Activity Log (Admin Console)
7. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Max Trial Duration`, Old Value `30`, New Value `31`, Modified By `Andi W`
8. Hover nilai Modified By pada entri baru Activity Log
9. Verifikasi tooltip `Andi Wijaya` tampil
10. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-479: Save tab Free Plan Settings menulis entri pada System Log aktor dan Activity Log Admin Console

11. Klik tab `Free Plan Settings`
12. Ubah Free Plan Duration dari `365` menjadi `366`
13. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
14. Klik `[Save]` dan tunggu toast sukses
15. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
16. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Free Plan Duration`, Old Value `365`, New Value `366`, Date sesuai General Settings, tanpa kolom Modified By
17. Buka Activity Log (Admin Console)
18. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Free Plan Duration`, Old Value `365`, New Value `366`, Modified By `Andi W`
19. Hover nilai Modified By pada entri baru Activity Log
20. Verifikasi tooltip `Andi Wijaya` tampil
21. Pulihkan ketujuh tab ke nilai default lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-480: Save tab License Timing menulis entri pada System Log aktor dan Activity Log Admin Console

22. Klik tab `License Timing`
23. Ubah Managed Transition Time dari `24` menjadi `25`
24. Catat jumlah entri System Log `Andi Wijaya` dan Activity Log Admin Console sebagai baseline
25. Klik `[Save]` dan tunggu toast sukses
26. Buka Settings > User > Detail `Andi Wijaya` > Tab System Log
27. Verifikasi entri baru System Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Managed Transition Time`, Old Value `24`, New Value `25`, Date sesuai General Settings, tanpa kolom Modified By
28. Buka Activity Log (Admin Console)
29. Verifikasi entri baru Activity Log (jumlah entri bertambah satu dari baseline): Action `Edit`, Object `Lifecycle Settings`, Name `—`, Field `Managed Transition Time`, Old Value `24`, New Value `25`, Modified By `Andi W`
30. Hover nilai Modified By pada entri baru Activity Log
31. Verifikasi tooltip `Andi Wijaya` tampil

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab terkait), "Catat jumlah entri ... sebagai baseline" (S-12), dan "Pulihkan ketujuh tab ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (S-03, S-09).
- Entri baru pada System Log dan Activity Log dikenali lewat kenaikan satu dari baseline dan kolom Field, Old Value, New Value, bukan lewat posisi "teratas", karena audit trail permanen tumbuh (S-12, S-14). Satu `Verifikasi` memuat seluruh kolom satu entri log dan keterangan "tanpa kolom Modified By" pada System Log (S-01).
- Temuan untuk QA: TC menulis "amati entri teratas" tanpa baseline; kolom `Name` bernilai `—` dan mekanisme membaca jumlah entri tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC (entri tercatat pada kedua surface) tidak punya langkah observasi di luar Expected dan tidak diasersi terpisah (S-01).
