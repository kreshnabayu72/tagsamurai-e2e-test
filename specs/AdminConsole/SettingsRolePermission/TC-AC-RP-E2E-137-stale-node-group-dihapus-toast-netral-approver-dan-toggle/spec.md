---
id: TC-AC-RP-E2E-137-stale-node-group-dihapus-toast-netral-approver-dan-toggle
title: "Target Berubah sejak Render: Node Group Aktif Dihapus Admin Lain sebelum Assign Approver dan Perubahan Toggle"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-404
  - TC-AC-RP-405
coverage:
  web: automated
---

# Target Berubah sejak Render: Node Group Aktif Dihapus Admin Lain sebelum Assign Approver dan Perubahan Toggle

## Prerequisites

- Mode: FE+BE (backend nyata; Sesi A lewat UI, Sesi B lewat sesi API)
- Akun aktor Sesi A: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`, Pre-setup #1), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun UI di tengah spec. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Pelaku kedua (Sesi B, Total Control; Pre-setup #24): sesi API untuk akun `Siti Nurhaliza` yang sama (`Spectra.env.AC_RP_TC_PASSWORD`); hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Region Jawa` dengan anak `Jakarta` dan `Surabaya`), #12 (`Alex Tan`), #15 (Group Role `Manage allocation`), #17 (approver dan toggle `Manage allocation`: `Region Jawa` ON, `Sumatera` OFF tersimpan, group lain tanpa nilai), dan #24 (dua sesi). Group `Surabaya` adalah data Pre-setup bersama yang dihapus Sesi B dan dipulihkan; tidak ada Data Dinamis bersuffix `+{runId}-137` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): sesi API aktor (dinyatakan di `suite.md`) untuk menghapus group; kemampuan membaca state data lewat fixture BE (daftar approver `Manage allocation` pada `Surabaya`).
- Pemulihan baseline: group `Surabaya` (anak `Region Jawa`) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated data yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-404: Node aktif dihapus sebelum Submit Assign Approver dan Remove Approver

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Sesi A: klik node `Surabaya`
4. Buka popup Assign Approver
5. Centang `Alex Tan`
6. Sesi B (sesi API `Siti Nurhaliza`, Total Control): hapus group `Surabaya` hingga tersimpan
7. Tunggu aksi selesai (Sesi B tersimpan)
8. Sesi A: klik `[Assign]`
9. Verifikasi toast netral "This group is no longer available." (status penolakan 404)
10. Verifikasi Sidebar Group Tree di-refresh
11. Verifikasi lewat fixture BE bahwa `Alex Tan` tidak menjadi approver `Manage allocation` (tidak ada perubahan tersimpan)
12. Pulihkan baseline: group `Surabaya` kembali lewat kemampuan reset FE/BE

### TC-AC-RP-405: Node aktif dihapus sebelum perubahan toggle disimpan

13. Buka halaman `Settings > Role & Permission`
14. Klik tab `System`
15. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
16. Sesi A: klik node `Surabaya`
17. Catat posisi toggle Require Approval node `Surabaya` sebagai baseline
18. Sesi B (sesi API `Siti Nurhaliza`, Total Control): hapus group `Surabaya` hingga tersimpan
19. Tunggu aksi selesai (Sesi B tersimpan)
20. Sesi A: klik toggle
21. Verifikasi toast netral "This group is no longer available." (status penolakan 404)
22. Verifikasi Sidebar Group Tree di-refresh
23. Verifikasi toggle kembali ke posisi semula sesuai baseline langkah 17
24. Pulihkan baseline: group `Surabaya` kembali lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-402 dan TC-AC-RP-403 ada di spec 119.
- Aktor: Sesi A adalah UI `Siti Nurhaliza`; Sesi B dijalankan lewat sesi API akun yang sama sesuai keputusan pelaku kedua memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (S-03, S-09): langkah 6 dan 18 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 7 dan 19 ("Tunggu aksi selesai", bagian 8b butir 8), langkah 12 dan 24 (pemulihan baseline), langkah 13 sampai 15 (membuka halaman dan Role Detail), langkah 17 (baseline posisi toggle).
- Temuan untuk QA:
  - TC-AC-RP-404 dan 405 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua (spec dipindah ke kelas c).
  - TC-AC-RP-404 dan 405 tidak menyebut akun Sesi B; spec memakai sesi API akun `Siti Nurhaliza` (Pre-setup #24 hanya menyebut "dua sesi paralel Total Control", S-13).
  - TC-AC-RP-404: judul TC menyebut "dan Remove Approver" tetapi langkah dan Expected hanya Assign Approver; spec mengikuti langkah TC dan tidak menambah langkah Remove Approver. Mohon QA menambah TC atau menyesuaikan judul.
  - TC-AC-RP-404: TC tidak menyatakan apakah popup Assign Approver tetap terbuka sesudah toast; spec tidak menutup popup dan membuka halaman pada langkah 13 (halaman dimuat ulang).
  - TC-AC-RP-405: "toggle kembali ke posisi semula" tidak menyebut posisi awal node `Surabaya` (Pre-setup #17: group lain tanpa nilai); spec mencatat posisi toggle sebelum aksi sebagai baseline langkah 17.
  - Group `Surabaya` memiliki entitas member `Distributor Jawa Timur` (Pre-setup #16); TC tidak menyatakan apakah penghapusan group yang berisi entitas member diizinkan. Spec mengikuti TC (Sesi B menghapus `Surabaya`). Mohon konfirmasi QA atau sediakan group Dinamis tanpa member.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
