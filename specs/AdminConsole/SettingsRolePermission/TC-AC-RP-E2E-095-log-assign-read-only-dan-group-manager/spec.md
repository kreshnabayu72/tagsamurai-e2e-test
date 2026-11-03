---
id: TC-AC-RP-E2E-095-log-assign-read-only-dan-group-manager
title: "Pencatatan Assign Read Only, Assign Total Control dari Read Only, Assign dan Remove GM"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-320
  - TC-AC-RP-321
  - TC-AC-RP-322
coverage:
  web: automated
---

# Pencatatan Assign Read Only, Assign Total Control dari Read Only, Assign dan Remove GM

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard), #13 (pemegang Read Only: `Dewi Anggraini`), dan #14 (penugasan Group Manager: `Fajar Nugroho` di `Region Jawa` dan `Sumatera`). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log) untuk `Siti Nurhaliza` dan halaman Admin Console > Activity Log tersedia untuk akun Total Control.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-320: Assign Read Only dari Group Manager mencatat Remove Group Manager

1. Klik tab `Read Only`
2. Catat baseline jumlah entri: Changelog Tab Read Only dan Changelog Tab Group Manager
3. Klik tombol "+ Assign"
4. Centang `Fajar Nugroho` lalu klik `[Assign]`
5. Klik ikon Changelog
6. Verifikasi jumlah entri Changelog Tab Read Only bertambah 1 dibanding baseline langkah 2
7. Verifikasi entri baru: Action `Assign`, Old Value "—", New Value `Read Only`
8. Tutup modal Changelog
9. Klik tab `Group Manager`
10. Klik ikon Changelog
11. Verifikasi jumlah entri Changelog Tab Group Manager bertambah tepat 2 dibanding baseline langkah 2
12. Verifikasi entri `Remove` "Fajar Nugroho — Region Jawa": Field `Group Manager`, Old Value `Assigned`, New Value "—"
13. Verifikasi entri `Remove` "Fajar Nugroho — Sumatera": Field `Group Manager`, Old Value `Assigned`, New Value "—"
14. Tutup modal Changelog
15. Pulihkan baseline: `Fajar Nugroho` kembali Group Manager `Region Jawa` dan `Sumatera`

### TC-AC-RP-321: Assign Total Control dari Read Only mencatat Old Value Read Only

16. Buka halaman `Settings > Role & Permission`
17. Catat baseline jumlah entri Changelog Tab Total Control
18. Klik tombol "+ Assign"
19. Centang `Dewi Anggraini` lalu klik `[Assign]`
20. Klik ikon Changelog
21. Verifikasi jumlah entri Changelog Tab Total Control bertambah 1 dibanding baseline langkah 17
22. Verifikasi entri baru: Action `Assign`, Old Value `Read Only`, New Value `Total Control`
23. Tutup modal Changelog
24. Pulihkan baseline: `Dewi Anggraini` kembali Read Only

### TC-AC-RP-322: Assign dan Remove Group Manager tercatat tiga surface

25. Buka halaman `Settings > Role & Permission`
26. Klik tab `Group Manager`
27. Catat baseline jumlah entri: Changelog Tab Group Manager, System Log `Siti Nurhaliza`, dan Activity Log Admin Console
28. Klik tombol "+ Assign"
29. Buka field Group lalu pilih node `Region A`
30. Ketik Search `John Dohan`, tekan Enter
31. Centang `John Dohan`
32. Klik `[Assign]`
33. Klik `⋯` baris `John Dohan` — `Region A` lalu klik `Remove`
34. Klik `[Remove]`
35. Klik ikon Changelog
36. Verifikasi jumlah entri Changelog Tab Group Manager bertambah tepat 2 dibanding baseline langkah 27
37. Verifikasi entri `Assign` "John Dohan — Region A": Field `Group Manager`, Old Value "—", New Value `Assigned`
38. Verifikasi entri `Remove` "John Dohan — Region A": Field `Group Manager`, Old Value `Assigned`, New Value "—"
39. Tutup modal Changelog
40. Buka Detail User `Siti Nurhaliza` > Tab System Log
41. Verifikasi jumlah entri System Log bertambah tepat 2 dibanding baseline langkah 27
42. Verifikasi kedua entri baru ber-Object `Group Manager`, Name "John Dohan", Field "Group Manager — Region A"
43. Buka Activity Log Admin Console
44. Verifikasi jumlah entri Activity Log bertambah tepat 2 dibanding baseline langkah 27
45. Verifikasi kedua entri baru ber-Object `Group Manager`, Name "John Dohan", Field "Group Manager — Region A", Modified By "Siti N"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 2, 8, 14, 15, 16, 17, 23, 24, 25, 27, 39.
- Search `John Dohan` pada popup Assign adalah langkah penghubung untuk menemukan baris target (R-16, bagian 8b butir 9).
- Assign dan Remove GM `John Dohan` di `Region A` (TC-AC-RP-322) saling membatalkan sehingga tidak memerlukan langkah pemulihan baseline.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (45 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-322 menyebut "Detail User `Siti Nurhaliza` > Tab System Log dan Activity Log Admin Console" tanpa menyatakan apakah System Log dan Activity Log dibaca di halaman yang sama; spec membuka Tab System Log di Detail User aktor lalu Activity Log di Admin Console.
  - TC-AC-RP-320 dan 321 tidak menyebut Field entri Changelog; spec hanya mengasersi Action, Old Value, dan New Value sesuai Expected.
  - TC-AC-RP-322 tidak menyebut langkah Assign GM (pilih Group dan user); spec mengikuti alur Assign GM pada spec Assign Group Manager (pilih node `Region A`, Search, centang, `[Assign]`).
