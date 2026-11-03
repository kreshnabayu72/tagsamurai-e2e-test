---
id: TC-AC-RP-E2E-098-log-auto-revert
title: "Pencatatan Auto-Revert Total Control dan Group Manager dengan Pelaku Admin Pengedit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-327
  - TC-AC-RP-328
coverage:
  web: automated
---

# Pencatatan Auto-Revert Total Control dan Group Manager dengan Pelaku Admin Pengedit

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #13 (pemegang Total Control: `Rina Wijaya`), #14 (penugasan Group Manager: `Fajar Nugroho` di `Region Jawa`), dan #15 (penugasan peran individual). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > User > Detail User` (Tab System Log; Changelog: User) untuk `Rina Wijaya` dan `Siti Nurhaliza` dan halaman Admin Console > Activity Log tersedia untuk akun Total Control.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses, penugasan Group Manager, peran individual, approver, toggle) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-327: Auto-revert Total Control tercatat dengan pelaku admin pengedit

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage preload` lalu klik `Detail`
3. Catat baseline jumlah entri: Changelog Detail Role `Manage preload`, Changelog Tab Total Control, System Log `Siti Nurhaliza`, Activity Log Admin Console, dan Changelog: User `Rina Wijaya`
4. Hapus centang D baris `Rina Wijaya`
5. Klik `[Remove]` pada dialog auto-revert
6. Klik ikon Changelog
7. Verifikasi jumlah entri Changelog Detail Role bertambah dibanding baseline langkah 3
8. Verifikasi entri baru: Action `Edit`, Field `Delete`, Old Value `Active`, New Value `Inactive`
9. Tutup modal Changelog
10. Buka halaman `Settings > Role & Permission`
11. Klik ikon Changelog
12. Verifikasi jumlah entri Changelog Tab Total Control bertambah 1 dibanding baseline langkah 3
13. Verifikasi entri baru: Action `Auto-Revert`, Old Value `Total Control`, New Value "—", Modified By "Siti N" (bukan `System`)
14. Tutup modal Changelog
15. Buka Detail User `Siti Nurhaliza` > Tab System Log
16. Verifikasi jumlah entri System Log bertambah dibanding baseline langkah 3
17. Verifikasi entri baru ber-Object `Total Control` dan Action `Auto-Revert`
18. Buka Activity Log Admin Console
19. Verifikasi jumlah entri Activity Log bertambah dibanding baseline langkah 3
20. Verifikasi entri baru ber-Modified By "Siti N"
21. Buka Changelog: User milik `Rina Wijaya`
22. Verifikasi jumlah entri bertambah dibanding baseline langkah 3
23. Verifikasi memuat entri yang sama dengan Changelog Tab Total Control
24. Pulihkan baseline: `Rina Wijaya` kembali Total Control dan D `Manage preload` tercentang

### TC-AC-RP-328: Auto-revert Group Manager tercatat di Changelog Group Manager

25. Buka halaman `Settings > Role & Permission`
26. Klik tab `System`
27. Pada section Group Role, klik `⋯` pada baris `Manage partner` lalu klik `Detail`
28. Klik node `Region Jawa`
29. Catat baseline jumlah entri: Changelog Tab Group Manager dan System Log `Siti Nurhaliza`
30. Hapus centang U baris `Fajar Nugroho`
31. Klik `[Remove]` pada dialog konfirmasi
32. Buka halaman `Settings > Role & Permission`
33. Klik tab `Group Manager`
34. Klik ikon Changelog
35. Verifikasi jumlah entri Changelog Tab Group Manager bertambah 1 dibanding baseline langkah 29
36. Verifikasi entri baru: Action `Auto-Revert`, Object "Fajar Nugroho — Region Jawa", Old Value `Assigned`, New Value "—", Modified By "Siti N"
37. Tutup modal Changelog
38. Buka Detail User `Siti Nurhaliza` > Tab System Log
39. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 29
40. Verifikasi entri baru ber-Object `Group Manager` dan Field "Group Manager — Region Jawa"
41. Pulihkan baseline: `Fajar Nugroho` kembali GM `Region Jawa` dan U `Manage partner` `Region Jawa` tercentang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 3, 9, 10, 14, 24, 25, 29, 32, 37, 41.
- Urutan surface pada TC-AC-RP-327 mengikuti lokasi navigasi (Role Detail dibaca sebelum meninggalkan halaman), bukan urutan butir Expected a, b, dan c; seluruh Expected tetap punya Verifikasi (S-10).
- Jumlah entri yang pasti hanya Changelog Tab Total Control (tepat 1); surface lain diasersi bertambah karena TC tidak menyatakan jumlah entri cascade.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Alasan sekitar 35 langkah (41 langkah): blok pencatatan satu kelas fungsional pada surface log yang sama; tiap blok punya aksi, target, dan baseline jumlah entri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-327 Expected c menyebut "Changelog: User memuat entri yang sama" tanpa menyebut Field; spec mengasersi kesamaan dengan entri Changelog Tab Total Control.
  - TC-AC-RP-327 langkah 5 membuka lima surface sekaligus tanpa urutan; spec membacanya satu per satu dengan baseline masing-masing.
