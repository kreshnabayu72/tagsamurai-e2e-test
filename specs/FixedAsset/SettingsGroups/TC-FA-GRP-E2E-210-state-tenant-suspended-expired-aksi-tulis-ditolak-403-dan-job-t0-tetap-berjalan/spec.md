---
id: TC-FA-GRP-E2E-210-state-tenant-suspended-expired-aksi-tulis-ditolak-403-dan-job-t0-tetap-berjalan
title: "State Tenant: Client Suspended dan Expired Menolak Seluruh Aksi Tulis dengan 403 dan Toast Baku, serta Job Sistem T-0 pada Client Suspended Tetap Menandai Excess"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-995
  - TC-FA-GRP-996
  - TC-FA-GRP-1149
coverage:
  web: automated
---

# State Tenant: Client Suspended dan Expired Menolak Seluruh Aksi Tulis dengan 403 dan Toast Baku, serta Job Sistem T-0 pada Client Suspended Tetap Menandai Excess

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Kelas h (state tenant): suite berjalan serial (`parallel: false`). Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengubah status Client menjadi Suspended atau Expired lewat fixture BE atau sesi API dan memulihkannya; klien HTTP untuk request langsung ke server; sesi API aktor dengan token yang tetap berlaku; hook uji handler plan-efektif pada tanggal T-0 di lingkungan non-produksi; downgrade terjadwal plan Professional ke Growth (cap 3); pembacaan status Excess group dan jumlah baris Changelog, System Log, dan Activity Log lewat fixture BE.
- State global yang diubah spec: status Client (Suspended, Expired), plan terjadwal downgrade, dan status Excess group; dipulihkan di hook `after` (status Client Active, jadwal downgrade dibatalkan, group dipulihkan menjadi usable).
- Data Dinamis (Pre-setup tambahan, di-seed lewat API di hook `before` sebelum status Client diubah, dihapus di hook `after`; nama bersuffix `{runId}-210`): `Edit Target {runId}-210`, `Del Empty {runId}-210`, `Bulk E10 {runId}-210`, `Bulk E11 {runId}-210`; untuk TC-1149 client dengan 6 group (G1 terlama sampai G6, dibuat berurutan) tanpa seleksi Wizard tersimpan; seleksi Wizard terjadwal untuk request Set Group Consolidation Selection.

  | Status Client |
  |---|
  | Suspended |
  | Expired |

## Test Steps

1. Untuk setiap baris tabel Prerequisites (langkah 1 sampai 14): Atur status Client menjadi nilai pada baris tabel lewat fixture BE hingga tersimpan
2. Catat state data (Edit Target, Del Empty, Bulk E10, Bulk E11, jumlah group) serta jumlah baris Changelog, System Log, dan Activity Log sebagai baseline
3. Kirim request Create Group (level 1) dan Create Subgroup dengan token sesi API aktor
4. Verifikasi request Create Group dan Create Subgroup ditolak server `403 Forbidden`
5. Kirim request Edit `Edit Target {runId}-210`
6. Verifikasi request Edit ditolak server `403 Forbidden`
7. Kirim request Delete `Del Empty {runId}-210`
8. Verifikasi request Delete ditolak server `403 Forbidden`
9. Kirim request Bulk Delete `Bulk E10 {runId}-210` dan `Bulk E11 {runId}-210`
10. Verifikasi request Bulk Delete ditolak server `403 Forbidden`
11. Kirim request Set Group Consolidation Selection
12. Verifikasi request Set Group Consolidation Selection ditolak server `403 Forbidden`
13. Verifikasi data tidak berubah dibanding state yang dicatat dan jumlah baris Changelog, System Log, dan Activity Log sama dengan baseline
14. Pulihkan status Client menjadi Active lewat fixture BE hingga tersimpan

### TC-1149: Job sistem T-0 pada client Suspended

15. Atur status Client menjadi Suspended lewat fixture BE hingga tersimpan
16. Catat jumlah baris Changelog dan Activity Log serta jumlah baris System Log sebagai baseline
17. Picu hook uji handler plan-efektif pada tanggal T-0 (client tetap Suspended), tunggu transaksi T-0 commit
18. Verifikasi handler T-0 berjalan dan commit tanpa `403` (aksi sistem tanpa aktor tidak diblokir status Suspended)
19. Baca status Excess keenam group lewat API baca
20. Verifikasi 3 group tetap usable (terlama dibuat diprioritaskan) dan 3 group Excess
21. Verifikasi Changelog dan Activity Log memuat `Marked as Excess (Group Consolidation)` per group Excess dengan Modified By `System`
22. Verifikasi jumlah baris System Log sama dengan baseline (tanpa System Log)
23. Kirim request Edit Group pada salah satu group dengan token sesi API aktor
24. Verifikasi request Edit Group ditolak server `403 Forbidden`
25. Verifikasi data tidak berubah
26. Pulihkan status Client menjadi Active lewat fixture BE hingga tersimpan

## Notes

- Langkah 1 sampai 14 berulang untuk setiap baris tabel Prerequisites (Suspended, Expired). Langkah penghubung (S-03): mengatur dan memulihkan status Client, serta mencatat baseline. Asersi "tidak ada baris log baru" atas request yang ditolak (langkah 13 dan 22) tetap di spec fungsional ini, bukan di spec absence kelas g, berdasarkan keputusan pengguna (S-05 dibaca bersama prinsip 13g): asersi ditulis sebagai selisih jumlah baris Changelog, System Log, dan Activity Log terhadap baseline yang dicatat sebelum request (langkah 2 dan 16, S-12).
- Spec memiliki 26 langkah nominal dan 40 langkah setelah ekspansi (2 iterasi x 14 langkah + 12), di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (state tenant, kelas h) dan langkah dua status identik sehingga ekspansi berasal dari perulangan tanpa langkah bersyarat (8b butir 7); TC-1149 berdiri sendiri.
- K-1: TC-995, 996, dan 1149 adalah kelas a atau h dengan Expected respons API dan state data lewat fixture BE; tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec.
- P-2: job sistem T-0 pada TC-1149 adalah proses sistem yang hanya memicu kondisi yang diuji (Excess), bukan objek asersi aktor.
- Temuan untuk QA:
  - TC-995 dan 996 Expected b (toast error baku "Changes can't be saved while this workspace is suspended or expired." tanpa redirect dan UI di-refresh) adalah perilaku FE pada request langsung; tidak disalin ke spec (8b butir 1) dan perlu TC jalur form tersendiri. Sebagai gantinya spec mengasersi status 403 dan state data.
  - TC-995, 996, dan 1149 tidak punya baris `Login sbg Role` (ACC kosong); aktor ditulis Total Control sebagai default suite dan sesi API aktor yang sama (disediakan tim FE/BE). Mekanisme mengubah status Client dan hook T-0 tidak ada di TC, PRD, atau LLD (S-13).
