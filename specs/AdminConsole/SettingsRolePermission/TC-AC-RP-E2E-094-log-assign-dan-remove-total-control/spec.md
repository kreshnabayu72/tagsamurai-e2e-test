---
id: TC-AC-RP-E2E-094-log-assign-dan-remove-total-control
title: "Pencatatan Assign dan Remove Total Control di Changelog dan Changelog: User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-317
  - TC-AC-RP-319
  - TC-AC-RP-336
  - TC-AC-RP-433
coverage:
  web: automated
---

# Pencatatan Assign dan Remove Total Control di Changelog dan Changelog: User

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `Alex Tan`, `Sarah Kimura`, `Dewi Anggreni`), #13 (pemegang Total Control: `John Doe`), dan #15 (penugasan peran individual). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab Changelog, sub-tab Changelog: User) tersedia untuk akun Total Control; dibuka lewat sidebar `Settings > User`.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-317: Assign Total Control tercatat di Changelog Total Control dan Changelog: User

1. Catat baseline jumlah entri: Changelog Tab Total Control dan Changelog: User `Alex Tan`
2. Klik tombol "+ Assign"
3. Centang `Alex Tan` lalu klik `[Assign]`
4. Klik ikon Changelog
5. Verifikasi jumlah entri Changelog Tab Total Control bertambah 1 dibanding baseline langkah 1
6. Verifikasi entri baru: Action `Assign`, User Name "Alex Tan", Field `Access Level`, Old Value "—", New Value `Total Control`, Modified By "Siti N"
7. Tutup modal Changelog
8. Buka `Settings > User > Detail User` `Alex Tan` > Changelog
9. Verifikasi jumlah baris `Changelog: User` milik `Alex Tan` bertambah 1 dibanding baseline langkah 1
10. Verifikasi baris baru sama dengan entri Changelog Total Control (Field `Access Level`)
11. Verifikasi tidak ada baris cascade per role pada `Changelog: User` (baris baru tepat satu)
12. Pulihkan baseline: `Alex Tan` kembali Standard

### TC-AC-RP-433: Assign Total Control ke beberapa user mencatat satu entri Changelog per user

13. Buka halaman `Settings > Role & Permission`
14. Catat baseline jumlah entri: Changelog Tab Total Control dan Changelog: User `Sarah Kimura`
15. Klik "+ Assign", centang `Sarah Kimura` dan `Dewi Anggreni`, klik `[Assign]`
16. Buka Changelog Tab Total Control
17. Verifikasi jumlah entri Changelog Tab Total Control bertambah tepat 2 dibanding baseline langkah 14 (tanpa entri gabungan)
18. Verifikasi entri `Assign` untuk `Sarah Kimura`: Field `Access Level`, Old Value "—", New Value `Total Control`
19. Verifikasi entri `Assign` untuk `Dewi Anggreni`: Field `Access Level`, Old Value "—", New Value `Total Control`
20. Tutup modal Changelog
21. Buka Settings > User > Detail `Sarah Kimura` > Changelog: User
22. Verifikasi jumlah baris `Changelog: User` milik `Sarah Kimura` bertambah 1 dibanding baseline langkah 14
23. Verifikasi baris baru adalah Assign Total Control
24. Pulihkan baseline: `Sarah Kimura` dan `Dewi Anggreni` kembali Standard

### TC-AC-RP-319: Remove Total Control mencatat cascade per seluruh Global Role yang berlaku

25. Buka halaman `Settings > Role & Permission`
26. Catat baseline jumlah entri: Changelog Tab Total Control dan Changelog Tab System
27. Klik `⋯` baris `John Doe` lalu klik `Remove`
28. Klik `[Remove]`
29. Buka Changelog Tab Total Control
30. Verifikasi jumlah entri Changelog Tab Total Control bertambah 1 dibanding baseline langkah 26
31. Verifikasi entri baru: Action `Remove`, Old Value `Total Control`, New Value "—"
32. Tutup modal Changelog
33. Klik tab `System`
34. Buka Changelog Tab System
35. Verifikasi jumlah entri Changelog Tab System bertambah tepat 10 dibanding baseline langkah 26 (satu per Global Role yang berlaku untuk Principal, tanpa entri Group Role)
36. Verifikasi kesepuluh entri baru ber-Action `Remove (via Total Control)`
37. Tutup modal Changelog
38. Pulihkan baseline: `John Doe` kembali Total Control

### TC-AC-RP-336: Remove Total Control tidak menduplikasi cascade di aggregate Changelog: User

39. Buka halaman `Settings > Role & Permission`
40. Catat baseline jumlah entri: Changelog: User (aggregate) `John Doe`
41. Klik `⋯` baris `John Doe` lalu klik `Remove`
42. Klik `[Remove]`
43. Buka Settings > User > Detail User `John Doe` > Changelog: User (aggregate)
44. Verifikasi jumlah baris aggregate bertambah tepat 1 dibanding baseline langkah 40
45. Verifikasi baris baru aggregate ber-Field `Access Level`
46. Buka Changelog: User > Global Role milik `John Doe`
47. Verifikasi entri `Remove (via Total Control)` tampil di Changelog: User > Global Role
48. Pulihkan baseline: `John Doe` kembali Total Control

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 1, 7, 12, 13, 14, 20, 24, 25, 26, 32, 37, 38, 39, 40, 48.
- Baseline 1, 14, 26, dan 40 mencatat jumlah entri sebelum aksi pemicu (S-12); jumlah bertambah diasersi sebagai selisih, bukan angka absolut.
- Klausa "tanpa entri Group Role" TC-AC-RP-319 dan "aggregate hanya memuat 1 baris" TC-AC-RP-336 diasersi lewat selisih jumlah entri yang tepat (asersi jumlah, bukan kelas g); entri cascade di aggregate tidak diasersi absen secara terpisah.
- Jumlah 10 entri cascade mengikuti Expected TC-AC-RP-319 ("10 entri" Global Role yang berlaku untuk Principal).
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (48 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - Email akun user Standard `Alex Tan`, `Sarah Kimura`, dan `Dewi Anggreni` tidak tertulis di Pre-setup #1 sampai #10; spec hanya memakai nama tampil sebagai target dan tidak login sebagai user ini.
  - TC-AC-RP-317 dan 433 tidak menyebut langkah penutupan modal Changelog; spec menutup modal sebelum pindah ke Settings > User.
  - TC-AC-RP-336 Expected "entri Remove (via Total Control) hanya tampil di Changelog: User > Global Role" tidak memberi cara observasi absen di aggregate; spec mengasersi selisih jumlah aggregate tepat 1 dan keberadaan entri di sub-tab Global Role.
