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
- State global yang diubah spec: plan client, jadwal downgrade, dan status Excess group; dipulihkan di hook `after` (sesi aktor dikembalikan ke client (a), client (b) dihapus, plan dikembalikan ke Professional, jadwal downgrade dibatalkan, seluruh group dipulihkan menjadi usable) dan tidak bergantung pada hasil spec lain (S-06, R-08).
- Data (Pre-setup tambahan, nama bersuffix `{runId}-198`; dua client terpisah agar tiap blok berdiri sendiri, S-06; mekanisme client kedua adalah langkah, bukan hook: client (a) di-seed lewat API di hook `before`, client (b) hanya disediakan pada langkah 35 dan 36): (a) client TC-879 dan TC-880, client yang dibuka sesi aktor sejak hook `before`: plan efektif Professional dengan downgrade ke Growth (cap 3) sudah dijadwalkan lewat Admin Console dan berlaku pada T-0, enam group usable `G1 {runId}-198` sampai `G6 {runId}-198` (G1 terlama, dibuat berurutan) tanpa seleksi Wizard tersimpan; pada T-0 hook uji menandai group yang melebihi cap sebagai Excess (TC-879), lalu TC-880 menaikkan plan ke Professional lewat Admin Console; (b) client TC-881, dibuka sesi aktor pada langkah 36: plan Growth cap 3 dengan lima group `G1 {runId}-198` sampai `G5 {runId}-198` (jumlah group melebihi cap), sebagian group berstatus Excess, `G1` dan `G2` kosong tanpa aset dan dihapus oleh aksi blok; state client ini disediakan tim FE lewat fixture BE pada langkah 35, sesi aktor berpindah ke client ini pada langkah 36, dan state tidak bergantung pada state akhir TC-880.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Changelog Group, System Log user aktor, dan Activity Log FAMS sebelum aksi (baseline, 8b butir 10); fixture "Pre-setup tambahan" di-seed lewat API di hook `before` dan dihapus di hook `after`.

## Test Steps

### TC-879: Marked as Excess (fallback T-0)

1. Ketik Search `{runId}-198`, tekan Enter, lalu catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
2. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Marked as Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama `G1 {runId}-198` sampai `G6 {runId}-198`
3. Picu T-0 lewat hook uji handler plan-efektif di lingkungan non-produksi, tunggu transaksi T-0 commit
4. Buka Fixed Asset > Settings > Groups
5. Ketik Search `{runId}-198`, tekan Enter, lalu catat daftar group berstatus Excess di Groups List sesudah aksi (daftar sesudah); node = tiap group yang berubah Usable ke Excess, yaitu selisih daftar sesudah terhadap daftar sebelum
6. Verifikasi selisih daftar sesudah terhadap daftar sebelum memuat sedikitnya satu node
7. Buka Modal Changelog: Group
8. Filter Changelog dengan Group Name tiap node (nama bersuffix `{runId}-198`)
9. Verifikasi baris Changelog tiap node: Action `Marked as Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Usable`, New Value `Excess`, Modified By `System`
10. Verifikasi jumlah baris Changelog `Marked as Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
11. Tutup Modal Changelog
12. Buka Detail User aktor, klik Tab System Log
13. Verifikasi jumlah baris System Log aktor tidak bertambah dibanding baseline (fallback T-0 selalu tanpa System Log)
14. Buka Activity Log FAMS
15. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
16. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By `System`

### TC-880: Restored from Excess (plan naik)

17. Buka Fixed Asset > Settings > Groups
18. Ketik Search `{runId}-198`, tekan Enter, lalu catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
19. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Restored from Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama group pada daftar sebelum
20. Simpan perubahan plan (upgrade ke Professional) di Admin Console
21. Tunggu aksi selesai
22. Buka Fixed Asset > Settings > Groups
23. Ketik Search `{runId}-198`, tekan Enter, lalu catat daftar group berstatus Excess di Groups List sesudah aksi (daftar sesudah); node = tiap group yang berubah Excess ke Usable, yaitu selisih daftar sebelum terhadap daftar sesudah
24. Verifikasi selisih daftar sebelum terhadap daftar sesudah memuat sedikitnya satu node
25. Buka Modal Changelog: Group
26. Filter Changelog dengan Group Name tiap node
27. Verifikasi baris Changelog tiap node: Action `Restored from Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Excess`, New Value `Usable`, Modified By `System`
28. Verifikasi jumlah baris Changelog `Restored from Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
29. Tutup Modal Changelog
30. Buka Detail User aktor, klik Tab System Log
31. Verifikasi jumlah baris System Log aktor tidak bertambah dibanding baseline (auto-reset karena plan naik berasal dari Admin Console, tanpa user pemicu)
32. Buka Activity Log FAMS
33. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
34. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By `System`

### TC-881: Restored from Excess (Delete)

35. Siapkan client TC-881 lewat fixture BE (client kedua yang terpisah dari client TC-879 dan TC-880, disediakan tim FE; tidak bergantung pada state akhir TC-880): jumlah group melebihi cap plan Growth (cap 3), sebagian group berstatus Excess, `G1 {runId}-198` dan `G2 {runId}-198` kosong tanpa aset
36. Buka sesi aktor Total Control pada client TC-881 (client kedua; kemampuan pindah client disediakan tim FE/BE)
37. Buka Fixed Asset > Settings > Groups
38. Ketik Search `{runId}-198`, tekan Enter, lalu catat daftar group berstatus Excess di Groups List sebelum aksi (daftar sebelum)
39. Catat baseline sebelum aksi: jumlah baris Changelog Group dengan Action `Restored from Excess (Group Consolidation)`, jumlah baris System Log aktor, dan jumlah baris Activity Log FAMS, masing-masing per nama group pada daftar sebelum
40. Buka Fixed Asset > Settings > Groups
41. Ketik Search `{runId}-198`, tekan Enter
42. Centang `G1 {runId}-198` dan `G2 {runId}-198`, pilih Bulk Action Delete, klik [Delete]
43. Verifikasi toast sukses "Success, group has been deleted."
44. Catat daftar group berstatus Excess di Groups List (Search `{runId}-198` dari langkah 41 masih aktif) sesudah aksi (daftar sesudah); node = tiap group yang berubah Excess ke Usable, yaitu selisih daftar sebelum terhadap daftar sesudah
45. Verifikasi selisih daftar sebelum terhadap daftar sesudah memuat sedikitnya satu node
46. Buka Modal Changelog: Group
47. Filter Changelog dengan Group Name tiap node
48. Verifikasi baris Changelog tiap node: Action `Restored from Excess (Group Consolidation)`, Group Name nama node, Field `Excess`, Old Value `Excess`, New Value `Usable`, Modified By aktor Delete (format `[First Name] [Last Initial]`)
49. Verifikasi jumlah baris Changelog `Restored from Excess (Group Consolidation)` tiap node bertambah tepat 1 per field yang berubah dibanding baseline masing-masing (tidak duplikat, tidak ada baris untuk node di luar selisih)
50. Tutup Modal Changelog
51. Buka Detail User aktor, klik Tab System Log
52. Verifikasi jumlah baris System Log aktor tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
53. Verifikasi baris System Log aktor baru tiap node (Note memuat nama node): object `Groups`
54. Buka Activity Log FAMS
55. Verifikasi jumlah baris Activity Log FAMS tiap nama node (Note memuat nama node) bertambah 1 dibanding baseline masing-masing
56. Verifikasi baris Activity Log baru tiap node (Note memuat nama node): kolom Modified By aktor Delete

## Notes

- Baris log dicari lewat kolom Note yang memuat nama group node (penanda baris sesuai TC); node ditentukan dari selisih daftar Excess di Groups List sebelum dan sesudah aksi, bukan dari nama yang ditebak. Baseline (S-12) dicatat per nama sebelum aksi tiap TC pada keadaan client masing-masing; asersi jumlah memakai selisih terhadap baseline. Langkah penghubung (S-03): mencatat daftar Excess dan baseline, pembentukan state dan pindah sesi aktor ke client TC-881 (langkah 35 dan 36), Buka Fixed Asset > Settings > Groups sebelum langkah yang membaca atau mengubah Groups List sesudah baseline atau pembentukan state (S-14), Tunggu aksi selesai, filter Changelog, dan menutup Modal Changelog.
- Baris target dicari lewat Search nama bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Untuk TC-879 dan TC-880 aktor tidak ada (hook T-0 dan Admin Console); Total Control hanya membaca log, sehingga Modified By diasersi `System`.
- Anchor positif sebelum asersi universal "tiap node" (8b butir 2): `Verifikasi` selisih daftar Excess memuat sedikitnya satu node, supaya asersi tidak lulus kosong.
- Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, R-16).
- Asersi "tepat 1 baris" memakai baseline (S-12); kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- Spec memiliki 56 langkah, di atas smell 35 langkah. Alasan: tiga blok satu kelas harness (state tenant/plan, kelas h) dengan pola baca-log yang sama; tiap TC berdiri sendiri.
- Daftar Excess dicatat dengan Search `{runId}-198` aktif pada semua pencatatan (langkah 1, 5, 18, 23, 38, 44), sehingga daftar sebelum dan sesudah dibaca pada kondisi yang sama dan selalu muat satu halaman (client memiliki lebih dari 10 node level 1 dan page size 10; group `G1` sampai `G6` bersuffix). Search digabung ke langkah pencatatan dan dihitung langkah penghubung (S-03, S-09, S-14, R-16).
- Temuan untuk QA:
  - TC-879 sampai 881 menulis "Lakukan aksi" tanpa langkah; spec menyalin dari TC-310 (fallback T-0), TC-319 (plan naik), dan TC-269 (Bulk Delete menurunkan count). TC-881 "Delete menurunkan count ≤ cap" tidak menyebut group yang dihapus; spec memakai dua group kosong seperti TC-269 (`G1` dan `G2`).
  - TC-881 menyebut state "jumlah group > cap" yang disiapkan TC ini tanpa menyebut client; spec menafsirkan "dua client" (TC-879/880 dan TC-881 pada client terpisah) dan memilih satu mekanisme: langkah 35 menyiapkan client kedua lewat fixture BE dan langkah 36 membuka sesi aktor Total Control pada client itu (bukan hook `before`; hook hanya menyiapkan client TC-879/880). Kemampuan pindah client dan fixture disediakan tim FE/BE.
  - TC-881 tidak menyebut jumlah group Excess maupun jumlah baris log tepatnya; spec menentukan node dari selisih daftar Excess sebelum dan sesudah Delete.
