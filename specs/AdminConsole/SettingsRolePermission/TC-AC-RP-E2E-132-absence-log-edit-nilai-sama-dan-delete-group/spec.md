---
id: TC-AC-RP-E2E-132-absence-log-edit-nilai-sama-dan-delete-group
title: "Absence Log: Edit CRUD Nilai yang Sudah Sama dan Delete Group Tanpa Log Approver dan Toggle"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-335
  - TC-AC-RP-421
coverage:
  web: automated
---

# Absence Log: Edit CRUD Nilai yang Sudah Sama dan Delete Group Tanpa Log Approver dan Toggle

## Prerequisites

- Mode: FE+BE (backend nyata; aksi dan pembacaan log lewat UI).
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Hook suite (flag Guided Tooltip halaman ini, pemulihan baseline automation, pemulihan Setup Column, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: #11 (tree group Principal), #12 (user Standard: `Maya Putri`, `Dewi Anggreni`), #14 (penugasan Group Manager: `Fajar Nugroho` di `Sumatera`), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user, role, dan group Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini. Admin B (#24) memakai sesi API aktor (login API password, token tidak dihitung sebagai sesi web; dinyatakan di `suite.md`) yang hanya memicu perubahan state; Admin B adalah akun yang disediakan tim FE (Email akun ini tidak tertulis di Pre-setup TC; lihat Temuan untuk QA).
- Kemampuan teknis: membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) lewat kemampuan baca tanpa mengasersi angka absolut (disediakan tim FE/BE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum aksi; asersi memakai selisih terhadap baseline (S-12). Entri yang baru dibuat aksi spec ini dikenali lewat Action, Object, dan Modified By pada halaman pertama (Date Newest First).
- Kemampuan teknis: halaman `Settings > Group` (aksi hapus group) dan `Settings > User > Detail User` (Changelog: User, Tab System Log, Tab Activity Log) tersedia untuk akun Total Control; reset data Pre-setup (group `Sumatera` beserta GM, approver, dan toggle) disediakan tim FE/BE.
- Pemulihan baseline: kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; perlu didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Nilai data (nama user, group, role) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script); nama pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-421: Edit CRUD dengan nilai yang sudah sama di server menampilkan toast netral tanpa entri log

1. Buka halaman `Settings > Role & Permission`
2. Klik tab `System`
3. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
4. Catat baseline jumlah entri Changelog Detail Role `Manage device master data`
5. Admin B (sesi API) mencentang Create baris `Maya Putri` pada `Manage device master data` hingga tersimpan
6. Centang Create baris `Maya Putri`
7. Verifikasi toast netral "No changes to save."
8. Verifikasi Create baris `Maya Putri` tercentang
9. Klik ikon Changelog
10. Verifikasi jumlah entri Changelog Detail Role bertambah tepat 1 dibanding baseline langkah 4
11. Verifikasi entri baru: satu entri `Edit` Create `Inactive` menjadi `Active` untuk `Maya Putri`
12. Tutup modal Changelog
13. Pulihkan baseline: Create `Maya Putri` pada `Manage device master data` tidak tercentang

### TC-AC-RP-335: Delete Group mencatat Remove (Group Deleted) tanpa log Approver dan toggle

14. Buka halaman `Settings > Role & Permission`
15. Pastikan lewat sesi API: `Sumatera` memiliki GM `Fajar Nugroho`, approver `Dewi Anggreni` pada `Manage allocation`, dan toggle ON hingga tersimpan
16. Catat baseline jumlah entri: Changelog Tab Group Manager, Changelog Detail Role `Manage allocation`, Changelog: User `Fajar Nugroho`, System Log `Fajar Nugroho`, dan Activity Log `Fajar Nugroho`
17. Hapus group `Sumatera` dari Settings > Group
18. Tunggu aksi selesai
19. Buka halaman `Settings > Role & Permission`
20. Klik tab `Group Manager`
21. Klik ikon Changelog
22. Verifikasi jumlah entri Changelog Tab Group Manager bertambah 1 dibanding baseline langkah 16
23. Verifikasi entri baru: Action `Remove (Group Deleted)`, Object "Fajar Nugroho — Sumatera", Old Value `Assigned`, New Value "—", Modified By admin penghapus
24. Tutup modal Changelog
25. Buka Changelog: User `Fajar Nugroho`
26. Verifikasi jumlah record bertambah 1 dibanding baseline langkah 16
27. Verifikasi record baru sama dengan entri Changelog Tab Group Manager langkah 23
28. Buka Detail User `Fajar Nugroho` > Tab System Log
29. Verifikasi jumlah entri System Log bertambah 1 dibanding baseline langkah 16
30. Verifikasi entri baru System Log: Action `Remove`, Object `Group Manager (Group Deleted)`, Field "Group Manager — Sumatera"
31. Klik Tab Activity Log
32. Verifikasi jumlah entri Activity Log bertambah 1 dibanding baseline langkah 16
33. Verifikasi entri baru Activity Log: Action `Remove`, Object `Group Manager (Group Deleted)`, Field "Group Manager — Sumatera"
34. Buka halaman `Settings > Role & Permission`
35. Klik tab `System`
36. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
37. Klik ikon Changelog
38. Verifikasi jumlah entri Changelog Detail Role `Manage allocation` sama dengan baseline langkah 16 (tidak ada entri log untuk penghapusan approver dan nilai toggle `Sumatera`)
39. Pulihkan baseline: group `Sumatera`, GM `Fajar Nugroho`, approver, dan toggle dipulihkan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness g (absence log); aksi pemicu (Assign Total Control, perubahan oleh Admin B lewat sesi API, Delete Group) adalah pembentuk kondisi yang diasersi tidak tercatat (P-5 butir a), bukan objek uji.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 1, 4, 12, 13, 14, 15, 16, 18, 19, 24, 28, 31, 34, 39.
- Spec absence (kelas g): TC-AC-RP-335 adalah TC yang terbelah antara presence dan absence; Verifikasi pencatatan (anchor positif) berada di spec ini dengan baseline jumlah entri sendiri, dan asersi absence mengikuti anchor yang terhubung ke pemicu yang sama (S-05, bagian 8b butir 2).
- Alasan spec berada di atas sekitar 35 langkah (39 langkah): kedua blok TC (TC-AC-RP-421 dan TC-AC-RP-335) memakai satu kelas harness (g, absence log), satu akun, dan tiap blok mencatat baseline serta anchor positif sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; Verifikasi anchor, selisih baseline, dan satu Verifikasi per surface log (Changelog, System Log, Activity Log) menaikkan jumlah langkah (S-01, bagian 8b butir 2).
- Pelaku kedua (Admin B) lewat sesi API hanya memicu perubahan state (langkah 5); sesuai konvensi tidak memakai butir `P-2`. Pelaku pertama TC-AC-RP-421 diposisikan pada sesi API sehingga sesi UI Siti menjadi pengirim kedua (stale) yang hasilnya (toast netral) diasersi.
- Urutan blok: TC-AC-RP-421 mendahului TC-AC-RP-335 karena TC-AC-RP-335 menghapus group `Sumatera` dan aksi menghapus data diletakkan di akhir (S-10).
- TC-AC-RP-335: Delete Group `Sumatera` memakai Settings > Group; pemulihan group, GM, approver, dan toggle lewat kemampuan reset FE/BE.
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan sebagai langkah penghubung "Pulihkan baseline" dan di hook `after`.
- Temuan untuk QA:
  - Mekanisme "dipulihkan automation baseline" (kolom Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
  - Expected TC menyebut entri log tanpa baseline jumlah entri; karena audit trail permanen, spec mencatat baseline lewat kemampuan baca yang disediakan tim FE/BE dan mengasersi selisih (S-12).
  - Post Condition TC "Data dipulihkan automation baseline" tidak punya langkah observasi di TC sehingga tidak diasersi; spec hanya menjalankan langkah pemulihan.
  - TC-AC-RP-421 Expected memuat toast sukses "Success, permissions have been updated." dari pengirim pertama; karena pengirim pertama memakai sesi API (keputusan 2026-10-21/30), toast itu tidak teramati di UI dan tidak diasersi di spec ini.
  - TC-AC-RP-421 menamai pengirim kedua "Sesi A (tampilan belum diperbarui)"; spec memakai satu sesi UI sebagai pengirim kedua.
  - TC-AC-RP-335 langkah 1 menyatakan `Sumatera` toggle ON dan approver `Dewi Anggreni` pada `Manage allocation`, sedangkan Pre-setup #17 menyatakan `Sumatera` OFF tersimpan dan approver hanya di `Region Jawa`; spec menyiapkan kondisi itu lewat sesi API.
  - Email Admin B (Pre-setup #24) tidak tertulis di Pre-setup TC; disediakan tim FE.
  - TC-AC-RP-335 Expected b2 dan b3 (System Log dan Activity Log) tidak menyebut halaman atau user pemilik log; spec membuka Detail User `Fajar Nugroho` > Tab System Log dan Tab Activity Log, sama dengan surface log di spec 100 (S-13, S-15). Langkah 27 hanya mengasersi record Changelog: User (Expected b1); Expected b2 dan b3 diasersi pada langkah 28 sampai 33.
  - TC-AC-RP-335 tidak menyatakan alur penghapusan group di Settings > Group; spec mengikuti teks TC "Hapus group `Sumatera` dari Settings > Group".
