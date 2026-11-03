---
id: TC-AC-RP-E2E-100-log-additional-approver
title: "Pencatatan Add dan Remove Additional Approver Global Role dan Group Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-332
  - TC-AC-RP-333
coverage:
  web: automated
---

# Pencatatan Add dan Remove Additional Approver Global Role dan Group Role

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `Alex Tan`), dan #17 (approver dan toggle: `Manage TAG stock` = `Sarah Kimura`; `Manage allocation` `Region Jawa` = `Dewi Anggraini`, `Dewi Anggreni`). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log) untuk `Siti Nurhaliza` tersedia untuk akun Total Control.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-332: Add dan Remove Additional Approver Global Role tanpa suffix Group

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Catat baseline jumlah entri: Changelog Detail Role `Manage TAG stock` dan System Log `Siti Nurhaliza`
4. Klik "+ Assign" pada section Approvers
5. Centang `Alex Tan` lalu klik `[Assign]`
6. Klik `⋯` baris `Alex Tan` lalu klik `Remove`
7. Klik `[Remove]`
8. Klik ikon Changelog
9. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 2 dibanding baseline langkah 3
10. Verifikasi entri `Add`: Object "Manage TAG stock", Field `Additional Approver`, Old Value "—", New Value "Alex Tan"
11. Verifikasi entri `Remove`: Object "Manage TAG stock", Field `Additional Approver`, Old Value "Alex Tan", New Value "—"
12. Tutup modal Changelog
13. Buka Detail User `Siti Nurhaliza` > Tab System Log
14. Verifikasi jumlah entri System Log bertambah tepat 2 dibanding baseline langkah 3
15. Verifikasi kedua entri baru ber-Object `Global Role`, Name "Manage TAG stock", Field `Additional Approver`

### TC-AC-RP-333: Add Additional Approver Group Role dengan suffix Group

16. Buka halaman `Settings > Role & Permission`
17. Klik tab `System`
18. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
19. Klik node `Sumatera`
20. Catat baseline jumlah entri Changelog Detail Role `Manage allocation`
21. Klik "+ Assign" pada section Approvers
22. Centang `Alex Tan` lalu klik `[Assign]`
23. Klik ikon Changelog
24. Verifikasi jumlah entri Changelog Detail Role bertambah 1 dibanding baseline langkah 20
25. Verifikasi entri baru: Action `Add`, Object "Manage allocation", Field "Additional Approver — Sumatera", New Value "Alex Tan"
26. Tutup modal Changelog
27. Pulihkan baseline: approver `Alex Tan` dilepas dari `Manage allocation` `Sumatera`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 3, 12, 16, 20, 26, 27.
- Add dan Remove `Alex Tan` pada `Manage TAG stock` (TC-AC-RP-332) saling membatalkan sehingga tidak memerlukan langkah pemulihan; Add pada `Manage allocation` `Sumatera` (TC-AC-RP-333) dipulihkan.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-332 dan 333 menyebut `Assign Approver` tanpa merinci alur; spec mengikuti alur popup Assign Approver pada section Approvers (centang user lalu `[Assign]`).
