---
id: TC-AC-RP-E2E-119-stale-group-terpilih-dihapus
title: "Target Berubah sejak Render: Group Terpilih Dihapus Admin Lain sebelum Submit Assign Group Manager dan Assign User to Role"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-402
  - TC-AC-RP-403
coverage:
  web: automated
---

# Target Berubah sejak Render: Group Terpilih Dihapus Admin Lain sebelum Submit Assign Group Manager dan Assign User to Role

## Prerequisites

- Mode: FE+BE (backend nyata; Sesi A lewat UI, Sesi B lewat sesi API)
- Akun aktor Sesi A: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`, Pre-setup #1), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun UI di tengah spec. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Pelaku kedua (Sesi B, Total Control; Pre-setup #24): sesi API untuk akun `Siti Nurhaliza` yang sama (`Spectra.env.AC_RP_TC_PASSWORD`); hanya memicu perubahan state, tanpa asersi di sesinya (bukan konteks kedua kelas c; tidak butuh `P-2`).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Region Jawa` dengan anak `Jakarta` dan `Surabaya`), #12 (`John Dohan`, `Alex Tan`), #14 (penugasan Group Manager), #15 (Group Role `Manage distributor`), dan #24 (dua sesi). Group `Surabaya` adalah data Pre-setup bersama yang dihapus Sesi B dan dipulihkan; tidak ada Data Dinamis bersuffix `+{runId}-119` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): sesi API aktor (dinyatakan di `suite.md`) untuk menghapus group; kemampuan membaca state data lewat fixture BE (penugasan Group Manager dan Group Role `John Dohan` dan `Alex Tan`).
- Pemulihan baseline: group `Surabaya` (anak `Region Jawa`) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated data yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-402: Group terpilih dihapus sebelum Submit Assign GM

1. Klik tab `Group Manager`
2. Sesi A: klik `+ Assign`
3. Pilih Group `Surabaya`
4. Centang `John Dohan`
5. Sesi B (sesi API `Siti Nurhaliza`, Total Control): hapus group `Surabaya` hingga tersimpan
6. Tunggu aksi selesai (Sesi B tersimpan)
7. Sesi A: klik `[Assign]`
8. Verifikasi error field-level Group (`422`) "This group no longer exists. Please select another."
9. Verifikasi field Group auto-clear
10. Verifikasi tree Group di-refresh
11. Verifikasi pilihan User dikosongkan
12. Verifikasi kandidat User diambil ulang
13. Tutup popup Assign dengan `✕`
14. Pulihkan baseline: group `Surabaya` kembali lewat kemampuan reset FE/BE

### TC-AC-RP-403: Group terpilih dihapus sebelum Submit Assign User to Role (Group Role)

15. Buka halaman `Settings > Role & Permission`
16. Klik tab `System`
17. Pada section Group Role, klik `⋯` pada baris `Manage distributor` lalu klik `Detail`
18. Sesi A: klik node `Surabaya`
19. Klik `+ Assign`
20. Centang `Alex Tan`
21. Sesi B (sesi API `Siti Nurhaliza`, Total Control): hapus group `Surabaya` hingga tersimpan
22. Tunggu aksi selesai (Sesi B tersimpan)
23. Sesi A: klik `[Assign]`
24. Verifikasi error field-level (`422`) "This group no longer exists. Please select another."
25. Verifikasi field Group auto-clear
26. Verifikasi pohon Group di-refresh
27. Verifikasi pilihan User dikosongkan
28. Tutup popup Assign dengan `✕`
29. Pulihkan baseline: group `Surabaya` kembali lewat kemampuan reset FE/BE

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-AC-RP-404 dan TC-AC-RP-405 ada di spec 137.
- Aktor: Sesi A adalah UI `Siti Nurhaliza`; Sesi B dijalankan lewat sesi API akun yang sama sesuai keputusan pelaku kedua memakai sesi API (bagian 3 prinsip 13).
- Langkah penghubung (S-03, S-09): langkah 5 dan 21 (pemicu pelaku kedua, ditulis "hingga tersimpan", R-20), langkah 6 dan 22 ("Tunggu aksi selesai", bagian 8b butir 8), langkah 13 dan 28 (menutup popup picker; popup picker bukan form sehingga tanpa dialog Unsaved Changes, dan isian sudah dikosongkan oleh Expected), langkah 14 dan 29 (pemulihan baseline), langkah 15 sampai 17 (membuka halaman dan Role Detail).
- Temuan untuk QA:
  - TC-AC-RP-402 dan 403 berautomation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API untuk Sesi B sehingga dapat diotomasi. Konfirmasi bila QA menghendaki sesi UI kedua (spec dipindah ke kelas c).
  - TC-AC-RP-402 dan 403 tidak menyebut akun Sesi B; spec memakai sesi API akun `Siti Nurhaliza` (Pre-setup #24 hanya menyebut "dua sesi paralel Total Control", S-13).
  - Group `Surabaya` memiliki entitas member `Distributor Jawa Timur` (Pre-setup #16); TC tidak menyatakan apakah penghapusan group yang berisi entitas member diizinkan. Spec mengikuti TC (Sesi B menghapus `Surabaya`). Mohon konfirmasi QA atau sediakan group Dinamis tanpa member.
  - TC-AC-RP-402: "kandidat diambil ulang" tidak menyebut hal yang teramati; spec mengasersi daftar kandidat User dimuat ulang tanpa pilihan.
  - TC-AC-RP-403: Expected tidak menyebut kandidat diambil ulang, berbeda dengan TC-AC-RP-402; spec mengikuti masing-masing TC.
  - TC-AC-RP-403: "pilihan User dikosongkan" dan "field Group auto-clear" diasersi pada popup yang tetap terbuka; TC tidak menyatakan popup tertutup atau tetap terbuka sesudah error, spec mengasumsikan popup tetap terbuka karena error bersifat field-level.
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
