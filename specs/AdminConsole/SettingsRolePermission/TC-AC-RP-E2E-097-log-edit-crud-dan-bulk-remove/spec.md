---
id: TC-AC-RP-E2E-097-log-edit-crud-dan-bulk-remove
title: "Pencatatan Edit CRUD Satu Entri per Perubahan, Group Role, dan Bulk Remove"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-325
  - TC-AC-RP-326
  - TC-AC-RP-329
coverage:
  web: automated
---

# Pencatatan Edit CRUD Satu Entri per Perubahan, Group Role, dan Bulk Remove

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #13 (pemegang Total Control: `Rina Wijaya`), dan #15 (penugasan peran individual: `Jane Smith` R, `John Dohan` C/R/U di `Region A` dan R di `Branch 1`). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log; Changelog: User > Global Role) tersedia untuk akun Total Control.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-325: Edit CRUD tercatat satu entri per perubahan

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
3. Catat baseline jumlah entri: Changelog Detail Role `Manage device master data`, System Log `Siti Nurhaliza`, dan Changelog: User > Global Role `Jane Smith`
4. Centang C baris `Jane Smith`
5. Centang D baris `Jane Smith`
6. Klik ikon Changelog
7. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 2 dibanding baseline langkah 3
8. Verifikasi entri `Edit` Field `Create`, Old Value `Inactive`, New Value `Active`, Object "Manage device master data — Jane Smith"
9. Verifikasi entri `Edit` Field `Delete`, Old Value `Inactive`, New Value `Active`, Object "Manage device master data — Jane Smith"
10. Tutup modal Changelog
11. Buka Detail User `Siti Nurhaliza` > Tab System Log
12. Verifikasi jumlah entri System Log bertambah tepat 2 dibanding baseline langkah 3
13. Verifikasi entri baru ber-Object `Global Role` dan Field "Manage device master data — Create"
14. Verifikasi entri baru ber-Object `Global Role` dan Field "Manage device master data — Delete"
15. Buka `Settings > User > Detail User` `Jane Smith` > Changelog: User > Global Role
16. Verifikasi jumlah record bertambah tepat 2 dibanding baseline langkah 3
17. Verifikasi record Create dan Delete sama dengan entri Changelog Detail Role
18. Pulihkan baseline: C dan D `Jane Smith` pada `Manage device master data` tidak tercentang

### TC-AC-RP-326: Edit CRUD Group Role tercatat dengan Group di Object dan Field

19. Buka halaman `Settings > Role & Permission`
20. Klik tab `System`
21. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
22. Catat baseline jumlah entri: Changelog Detail Role `Manage distributor` dan System Log `Siti Nurhaliza`
23. Centang U baris `John Dohan` — `Branch 1`
24. Klik ikon Changelog
25. Verifikasi jumlah entri Changelog Detail Role bertambah 1 dibanding baseline langkah 22
26. Verifikasi entri baru: Object "Manage distributor — John Dohan — Branch 1", Field `Update`
27. Tutup modal Changelog
28. Buka Detail User `Siti Nurhaliza` > Tab System Log
29. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 22
30. Verifikasi entri baru ber-Field "Manage distributor — Branch 1 — Update"
31. Pulihkan baseline: U `John Dohan` — `Branch 1` pada `Manage distributor` tidak tercentang

### TC-AC-RP-329: Bulk Remove mencatat entri per baris berhasil dan Auto-Revert per user tier

32. Buka halaman `Settings > Role & Permission`
33. Klik tab `System`
34. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
35. Catat baseline jumlah entri: Changelog Detail Role `Manage device master data` dan Changelog Tab Total Control
36. Centang baris `John Dohan` dan `Rina Wijaya`
37. Klik `Bulk Action` > `Remove` pada Bulk Action Bar
38. Klik `[Remove]`
39. Klik ikon Changelog
40. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 2 dibanding baseline langkah 35
41. Verifikasi kedua entri baru ber-Action `Remove` dan Field `Access`
42. Tutup modal Changelog
43. Buka halaman `Settings > Role & Permission`
44. Klik ikon Changelog
45. Verifikasi jumlah entri Changelog Tab Total Control bertambah tepat 1 dibanding baseline langkah 35
46. Verifikasi entri baru: Action `Auto-Revert` untuk `Rina Wijaya`
47. Pulihkan baseline: `John Dohan` dan `Rina Wijaya` kembali memegang `Manage device master data`, `Rina Wijaya` kembali Total Control

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 3, 10, 18, 19, 22, 27, 31, 32, 35, 42, 43, 47.
- Penutupan modal Changelog dan pemulihan antar TC adalah langkah penghubung supaya setiap TC mulai dari keadaan Pre-setup (S-09).
- Jumlah entri "satu entri per perubahan" TC-AC-RP-325 (dua perubahan C dan D menghasilkan tepat dua entri) diasersi lewat selisih tepat 2.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (47 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-326 Expected a memakai Object "Manage distributor — John Dohan — Branch 1" dan System Log Field "Manage distributor — Branch 1 — Update"; spec mengikuti TC.
  - TC-AC-RP-329 langkah 4 "Bulk Remove ... lalu konfirmasi" tidak merinci langkah Bulk Action; spec mengikuti alur Bulk Remove pada spec Bulk Remove (Bulk Action Bar, `[Remove]`).
  - TC-AC-RP-325 langkah 7 "Changelog: User > Global Role milik `Jane Smith`" tidak menyebut navigasi; spec membukanya lewat Detail User `Jane Smith` (Settings > User).
