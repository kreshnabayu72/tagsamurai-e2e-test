---
id: TC-FA-GRP-E2E-197-log-marked-restored-excess-wizard-isi-baris-changelog-system-log-activity-log
title: "Pencatatan Log Excess via Wizard: Marked as Excess dan Restored from Excess"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-877
  - TC-FA-GRP-878
coverage:
  web: automated
---

# Pencatatan Log Excess via Wizard: Marked as Excess dan Restored from Excess

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Kelas h (state tenant/plan): suite berjalan serial (`parallel: false`). Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): hook uji handler plan-efektif pada tanggal T-0 di lingkungan non-produksi (menunggu transaksi T-0 commit), penjadwalan dan pembatalan downgrade plan serta perubahan plan lewat Admin Console, dan pembacaan status Excess group.
- State global yang diubah spec: plan client, jadwal downgrade, dan status Excess group; dipulihkan di hook `after` (plan dikembalikan ke Professional, jadwal downgrade dibatalkan, seluruh group dipulihkan menjadi usable) dan tidak bergantung pada hasil spec lain (S-06, R-08).
- Data (Pre-setup tambahan, di-seed lewat API di hook `before`, nama bersuffix `{runId}-197`): plan dijadwalkan downgrade Professional ke Growth (cap 3), T-30 berjalan; client punya 6 group termasuk `Head Office`, `Warehouse A`, `Branch Office` (Pre-setup No 9, dibaca dan tidak diubah) dan `Warehouse B {runId}-197` (Assignable); tidak ada seleksi Wizard tersimpan. Total Control (aktor) melakukan submit terakhir Wizard dan dipakai membaca log.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.
- Kolom Date baris Changelog TC-877 dibandingkan dengan waktu penerapan seleksi di T-0 (langkah 7) dengan toleransi satu menit; jam server dan jam browser sinkron.

## Test Steps

1. Catat baseline sebelum aksi: jumlah baris Changelog Group, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Warehouse B {runId}-197`

### TC-877: Marked as Excess (Wizard)

2. Buka Wizard Reconciliation, klik Step Group Consolidation
3. Centang `Head Office`, `Warehouse A`, dan `Branch Office`
4. Klik [Save Selection]
5. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal, tunggu transaksi T-0 commit
6. Buka Fixed Asset > Settings > Groups
7. Catat waktu penerapan seleksi di T-0
8. Buka Modal Changelog: Group
9. Filter Changelog dengan Group Name `Warehouse B {runId}-197`
10. Verifikasi baris Changelog: Action `Marked as Excess (Group Consolidation)`, Group Name `Warehouse B {runId}-197`, Field `Excess`, Old Value `Usable`, New Value `Excess`, Modified By user yang melakukan submit terakhir Wizard (format `[First Name] [Last Initial]`), Date waktu penerapan seleksi di T-0
11. Verifikasi jumlah baris Changelog untuk `Warehouse B {runId}-197` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
12. Tutup Modal Changelog
13. Buka Detail User aktor, klik Tab System Log
14. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
15. Verifikasi baris System Log aktor baru (Note memuat `Warehouse B {runId}-197`): object `Groups` pada System Log user pemicu (submit terakhir Wizard)
16. Buka Activity Log FAMS
17. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Warehouse B {runId}-197` bertambah 1 dibanding baseline
18. Verifikasi baris Activity Log baru (Note memuat `Warehouse B {runId}-197`): kolom Modified By

### TC-878: Restored from Excess (Wizard)

19. Catat baseline sebelum aksi: jumlah baris Changelog Group yang memuat nama `Warehouse B {runId}-197`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS yang memuat nama `Warehouse B {runId}-197`
20. Buka Fixed Asset > Settings > Groups
21. Klik [Choose Groups] pada Alert Group Consolidation
22. Ubah centang: centang kembali `Warehouse B {runId}-197`
23. Klik [Save Selection]
24. Verifikasi toast "Success, group consolidation has been updated."
25. Buka Modal Changelog: Group
26. Filter Changelog dengan Group Name `Warehouse B {runId}-197`
27. Verifikasi baris Changelog: Action `Restored from Excess (Group Consolidation)`, Field `Excess`, Old Value `Excess`, New Value `Usable`, Modified By user yang melakukan submit terakhir Wizard (format `[First Name] [Last Initial]`)
28. Verifikasi jumlah baris Changelog untuk `Warehouse B {runId}-197` bertambah tepat 1 per node per field yang berubah dibanding baseline (tidak duplikat, tidak ada baris untuk field yang tidak berubah atau node lain)
29. Tutup Modal Changelog
30. Buka Detail User aktor, klik Tab System Log
31. Verifikasi jumlah baris System Log aktor bertambah 1 dibanding baseline
32. Verifikasi baris System Log aktor baru (Note memuat `Warehouse B {runId}-197`): object `Groups` pada System Log user pemicu
33. Buka Activity Log FAMS
34. Verifikasi jumlah baris Activity Log FAMS yang memuat nama `Warehouse B {runId}-197` bertambah 1 dibanding baseline
35. Verifikasi baris Activity Log baru (Note memuat `Warehouse B {runId}-197`): kolom Modified By

## Notes

- Baseline (S-12) dicatat per surface sebelum aksi tiap TC (langkah 1 untuk TC-877 dan langkah 19 untuk TC-878, karena aksi TC-877 sudah menambah baris pada node dan surface yang sama). Baris System Log dan Activity Log dicari lewat Note atau nama bersuffix dan asersi jumlah memakai selisih 1 terhadap baseline. Langkah penghubung (S-03): baseline, hook T-0, filter Changelog, dan menutup Modal Changelog. Urutan TC-877 sebelum TC-878 mengikuti keadaan: pemilihan ulang hanya mungkin sesudah T-0 menandai Warehouse B.
- Untuk TC-877 Modified By dan Date mengikuti Expected TC: user yang melakukan submit terakhir Wizard dan waktu penerapan seleksi di T-0 (bukan waktu submit).
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- P-1: TC-878 bergantung pada state berat (Warehouse B Excess hasil T-0) yang dibangun TC-877 di spec yang sama.
- Temuan untuk QA:
  - TC-877 dan 878 menulis "Lakukan aksi" tanpa langkah; spec menyalin langkah dari TC-303 (Wizard submit dan T-0) dan TC-305 (pilih ulang setelah T-0). TC-877 menyebut "Warehouse B" sebagai group yang ditandai; pada Pre-setup Tabel A Warehouse B sudah berstatus Excess, sehingga spec memakai group `Warehouse B {runId}-197` bersuffix milik spec.
  - Mekanisme hook T-0 dan perubahan plan tidak ada di TC, PRD, atau LLD; ditulis sebagai kemampuan tim FE/BE (S-13).
