---
id: TC-AC-RP-E2E-096-log-assign-user-to-role
title: "Pencatatan Assign dan Remove User to Role, Termasuk Suffix Group"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-323
  - TC-AC-RP-324
coverage:
  web: automated
---

# Pencatatan Assign dan Remove User to Role, Termasuk Suffix Group

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `Alex Tan`), dan #15 (penugasan peran individual). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log) untuk `Siti Nurhaliza` tersedia untuk akun Total Control.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-323: Assign dan Remove User to Role tercatat di Changelog role dan System Log

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage language` lalu klik `Detail`
3. Catat baseline jumlah entri: Changelog Detail Role `Manage language` dan System Log `Siti Nurhaliza`
4. Klik "+ Assign"
5. Centang `Alex Tan` lalu klik `[Assign]`
6. Klik `⋯` baris `Alex Tan` lalu klik `Remove`
7. Klik `[Remove]`
8. Klik ikon Changelog
9. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 2 dibanding baseline langkah 3
10. Verifikasi entri `Assign` "Manage language — Alex Tan": Field `Access`, Old Value "—", New Value `Assigned`
11. Verifikasi entri `Remove` "Manage language — Alex Tan": Field `Access`, Old Value `Assigned`, New Value "—"
12. Tutup modal Changelog
13. Buka Detail User `Siti Nurhaliza` > Tab System Log
14. Verifikasi jumlah entri System Log bertambah tepat 2 dibanding baseline langkah 3
15. Verifikasi kedua entri baru ber-Object `Global Role`, Name "Alex Tan", Field "Manage language"

### TC-AC-RP-324: Assign User to Group Role tercatat dengan suffix Group

16. Buka halaman `Settings > Role & Permission`
17. Klik tab `System`
18. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
19. Klik node `Sumatera`
20. Catat baseline jumlah entri: Changelog Detail Role `Manage distributor` dan System Log `Siti Nurhaliza`
21. Klik "+ Assign"
22. Centang `Alex Tan` lalu klik `[Assign]`
23. Klik ikon Changelog
24. Verifikasi jumlah entri Changelog Detail Role bertambah 1 dibanding baseline langkah 20
25. Verifikasi entri baru ber-Object "Manage distributor — Alex Tan — Sumatera"
26. Tutup modal Changelog
27. Buka Detail User `Siti Nurhaliza` > Tab System Log
28. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 20
29. Verifikasi entri baru ber-Object `Group Role` dan Field "Manage distributor — Sumatera"
30. Pulihkan baseline: `Alex Tan` dilepas dari `Manage distributor` di `Sumatera`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 3, 12, 16, 20, 26, 30.
- Assign dan Remove `Alex Tan` pada `Manage language` (TC-AC-RP-323) saling membatalkan sehingga tidak memerlukan langkah pemulihan; Assign pada `Manage distributor` `Sumatera` (TC-AC-RP-324) dipulihkan.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (30 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-323 dan 324 menyebut "System Log aktor" tanpa menyatakan halaman; spec membuka Tab System Log pada Detail User `Siti Nurhaliza`.
  - TC-AC-RP-324 tidak menyatakan Name pada System Log; spec hanya mengasersi Object dan Field sesuai Expected.
