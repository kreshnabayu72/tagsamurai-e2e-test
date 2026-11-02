---
id: TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris
title: "Pencatatan Log Excess: Marked as Excess (Fallback T-0), Restored from Excess (Plan Naik), dan Restored from Excess (Delete)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-879
  - TC-FA-GRP-880
  - TC-FA-GRP-881
coverage:
  web: automated
---

# Pencatatan Log Excess: Marked as Excess (Fallback T-0), Restored from Excess (Plan Naik), dan Restored from Excess (Delete)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Kelas h (state tenant/plan): suite berjalan serial (`parallel: false`). Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): hook uji handler plan-efektif pada tanggal T-0 di lingkungan non-produksi (menunggu transaksi T-0 commit), penjadwalan dan pembatalan downgrade plan serta perubahan plan lewat Admin Console, dan pembacaan status Excess group.
- State global yang diubah spec: plan client, jadwal downgrade, dan status Excess group; dipulihkan di hook `after` (plan dikembalikan ke Professional, jadwal downgrade dibatalkan, seluruh group dipulihkan menjadi usable) dan tidak bergantung pada hasil spec lain (S-06, R-08).
- Data (Pre-setup tambahan, di-seed lewat API di hook `before`, nama bersuffix `{runId}-198`): client dengan 6 group `G1`..`G6` (G1 terlama) tanpa seleksi Wizard tersimpan, dibuat berurutan; untuk TC-880 plan upgrade ke Professional dilakukan lewat Admin Console; untuk TC-881 state disiapkan oleh TC itu sendiri dan tidak bergantung pada state akhir TC-880, disediakan tim FE lewat fixture BE pada langkah awal blok TC-881: client plan Growth cap 3 dengan lima group `G1`..`G5` bersuffix (jumlah group melebihi cap), sebagian group berstatus Excess, `G1` dan `G2` kosong tanpa aset dan dihapus oleh aksi blok.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.

## Test Steps

### TC-879: Marked as Excess (fallback T-0)

1. Catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
2. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Marked as Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama `G1 {runId}-198` sampai `G6 {runId}-198`
3. Picu T-0 lewat hook uji handler plan-efektif di lingkungan non-produksi, tunggu transaksi T-0 commit
4. Buka Fixed Asset > Settings > Groups
5. Catat daftar group berstatus Excess di Groups List sesudah aksi (daftar sesudah); node = tiap group yang berubah Usable ke Excess, yaitu selisih daftar sesudah terhadap daftar sebelum
6. Buka Modal Changelog: Group
7. Filter Changelog dengan Group Name tiap node (nama bersuffix `{runId}-198`)
8. Verifikasi baris Changelog tiap node: Action `Marked as Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Usable`, New Value `Excess`, Modified By `System`
9. Verifikasi jumlah baris Changelog `Marked as Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
10. Tutup Modal Changelog
11. Buka Detail User aktor, klik Tab System Log
12. Verifikasi jumlah baris System Log aktor tidak bertambah dibanding baseline (fallback T-0 selalu tanpa System Log)
13. Buka Activity Log FAMS
14. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
15. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By `System`

### TC-880: Restored from Excess (plan naik)

16. Catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
17. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Restored from Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama group pada daftar sebelum
18. Simpan perubahan plan (upgrade ke Professional) di Admin Console
19. Tunggu aksi selesai
20. Buka Fixed Asset > Settings > Groups
21. Catat daftar group berstatus Excess di Groups List sesudah aksi (daftar sesudah); node = tiap group yang berubah Excess ke Usable, yaitu selisih daftar sebelum terhadap daftar sesudah
22. Buka Modal Changelog: Group
23. Filter Changelog dengan Group Name tiap node
24. Verifikasi baris Changelog tiap node: Action `Restored from Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Excess`, New Value `Usable`, Modified By `System`
25. Verifikasi jumlah baris Changelog `Restored from Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
26. Tutup Modal Changelog
27. Buka Detail User aktor, klik Tab System Log
28. Verifikasi jumlah baris System Log aktor tidak bertambah dibanding baseline (auto-reset karena plan naik berasal dari Admin Console, tanpa user pemicu)
29. Buka Activity Log FAMS
30. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
31. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By `System`

### TC-881: Restored from Excess (Delete)

32. Siapkan state TC-881 (disediakan tim FE lewat fixture BE, tidak bergantung pada state akhir TC-880): jumlah group melebihi cap plan Growth (cap 3), sebagian group berstatus Excess, `G1 {runId}-198` dan `G2 {runId}-198` kosong tanpa aset
33. Catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
34. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Restored from Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama group pada daftar sebelum
35. Centang `G1 {runId}-198` dan `G2 {runId}-198`, pilih Bulk Action Delete, klik [Delete]
36. Verifikasi toast sukses "Success, group has been deleted."
37. Catat daftar group berstatus Excess di Groups List sesudah aksi (daftar sesudah); node = tiap group yang berubah Excess ke Usable, yaitu selisih daftar sebelum terhadap daftar sesudah
38. Buka Modal Changelog: Group
39. Filter Changelog dengan Group Name tiap node
40. Verifikasi baris Changelog tiap node: Action `Restored from Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Excess`, New Value `Usable`, Modified By aktor Delete (format `[First Name] [Last Initial]`)
41. Verifikasi jumlah baris Changelog `Restored from Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
42. Tutup Modal Changelog
43. Buka Detail User aktor, klik Tab System Log
44. Verifikasi jumlah baris System Log aktor tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
45. Verifikasi baris System Log aktor baru tiap node (Note memuat nama node): object `Groups`
46. Buka Activity Log FAMS
47. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
48. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By aktor Delete

## Notes

- Baris log dicari lewat kolom Note yang memuat nama group node (penanda baris sesuai TC); node ditentukan dari selisih daftar Excess di Groups List sebelum dan sesudah aksi, bukan dari nama yang ditebak. Baseline (S-12) dicatat per nama sebelum aksi tiap TC pada keadaan client masing-masing; asersi jumlah memakai selisih terhadap baseline. Langkah penghubung (S-03): mencatat daftar Excess dan baseline, pembentukan state TC-881 (langkah 32), Tunggu aksi selesai, filter Changelog, dan menutup Modal Changelog.
- Untuk TC-879 dan TC-880 aktor tidak ada (hook T-0 dan Admin Console); Total Control hanya membaca log, sehingga Modified By diasersi `System`.
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec memiliki 48 langkah, di atas smell 35 langkah. Alasan: tiga blok satu kelas harness (state tenant/plan, kelas h) dengan pola baca-log yang sama; tiap TC berdiri sendiri.
- Temuan untuk QA:
  - TC-879 sampai 881 menulis "Lakukan aksi" tanpa langkah; spec menyalin dari TC-310 (fallback T-0), TC-319 (plan naik), dan TC-269 (Bulk Delete menurunkan count). TC-881 "Delete menurunkan count ≤ cap" tidak menyebut group yang dihapus; spec memakai dua group kosong seperti TC-269 (`G1` dan `G2`).
  - TC-881 tidak menyebut jumlah group Excess maupun jumlah baris log tepatnya; spec menentukan node dari selisih daftar Excess sebelum dan sesudah Delete.
