---
id: TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection
title: "Wizard Group Consolidation: Screening Step, Counter Real-Time, Melebihi Cap dan 0 Tercentang Menonaktifkan [Save Selection], dan Centang Kurang dari Cap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-300
  - TC-FA-GRP-301
  - TC-FA-GRP-302
  - TC-FA-GRP-304
  - TC-FA-GRP-962
coverage:
  web: automated
---

# Wizard Group Consolidation: Screening Step, Counter Real-Time, Melebihi Cap dan 0 Tercentang Menonaktifkan [Save Selection], dan Centang Kurang dari Cap

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.

## Test Steps

### TC-FA-GRP-300 dan TC-FA-GRP-962: Screening step dan keadaan 0 tercentang

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Verifikasi header "Choose which groups stay active"
3. Verifikasi subtitle "You can keep up to 3 groups. The rest will become read-only until you free up space."
4. Verifikasi tabel memuat kolom Checkbox Keep usable, Group (nama dan full path), Total Asset, dan Total User berisi keenam group client
5. Verifikasi seluruh checkbox unchecked (tanpa pra-isi)
6. Verifikasi counter "0 of 3 selected" tampil netral (bukan severity danger)
7. Verifikasi footer memuat [Cancel] dan [Save Selection] (primary)
8. Verifikasi [Save Selection] disabled

### TC-FA-GRP-962: Centang lalu uncheck sampai 0

9. Centang 1 group
10. Verifikasi [Save Selection] enabled
11. Uncheck group tersebut
12. Verifikasi [Save Selection] disabled kembali
13. Verifikasi counter "0 of 3 selected" tanpa severity danger

### TC-FA-GRP-301: Counter real-time

14. Centang 2 group
15. Verifikasi counter "2 of 3 selected"
16. Uncheck 1 group
17. Verifikasi counter "1 of 3 selected"
18. Uncheck group yang tersisa

### TC-FA-GRP-302: Melebihi cap menonaktifkan [Save Selection]

19. Centang 4 group
20. Verifikasi [Save Selection] disabled
21. Verifikasi counter "4 of 3 selected" tampil dengan severity danger (merah)
22. Verifikasi tidak ada dialog dan tidak ada toast yang tampil
23. Uncheck seluruh group yang tercentang

### TC-FA-GRP-304: Boleh mencentang lebih sedikit dari cap

24. Centang 1 group (`Head Office`)
25. Klik [Save Selection]
26. Verifikasi toast "Success, group consolidation has been updated."
27. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
28. Buka Fixed Asset > Settings > Groups
29. Verifikasi `Head Office` usable (tidak di-dim)
30. Verifikasi kelima group lain berstatus Excess (di-dim)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 18, 23, 27 dan 28: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Verifikasi langkah 8 mencakup Expected d TC-300 dan Expected a TC-962 (keadaan 0 tercentang), dan verifikasi netral/bukan merah pada langkah sebelumnya mencakup TC-300 c dan TC-962 a; tiap klausa tetap punya `Verifikasi` (S-01). Anchor positif untuk absence dialog dan toast pada langkah sesudah 21: counter severity danger (R-03, 8b butir 2).
- Langkah T-0 pada TC-304 ditambahkan sebagai pemicu hook uji karena Expected b menyebut hasil di T-0 (TC tidak menyebut pemicunya).
- Spec kelas h: kejadian T-0 hanya pemicu keadaan yang diasersi pada TC-304.
- Temuan untuk QA:
  - TC-304 Langkah tidak memuat pemicu T-0 padahal Expected b mengasersi hasil di T-0; spec memakai hook uji yang sama dengan TC-303.
  - TC-300 menyebut "nama + full path" tanpa contoh nilai; spec mengasersi kolom Group memuat nama dan full path.
