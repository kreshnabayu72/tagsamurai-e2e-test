---
id: TC-FA-GRP-E2E-281-wizard-log-ditulis-saat-diterapkan-di-t0-system-log-user-submit-terakhir-dan-siklus-downgrade-berikutnya
title: "Wizard: Submit Sebelum T-0 Tidak Menulis Log, Log dan System Log Ditulis Saat Diterapkan di T-0 (Submit Terakhir), dan Siklus Downgrade Berikutnya"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-989
  - TC-FA-GRP-990
coverage:
  web: automated
---

# Wizard: Submit Sebelum T-0 Tidak Menulis Log, Log dan System Log Ditulis Saat Diterapkan di T-0 (Submit Terakhir), dan Siklus Downgrade Berikutnya

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Modal Changelog: Group, Activity Log, dan System Log aktor sebelum dan sesudah aksi (audit trail permanen; 8b butir 10).
- Jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah transaksi T-0 commit dengan toleransi satu menit (S-12).
- Akun pelaku kedua: User B (Total Control client Wizard; email dan password disediakan tim FE, tidak tertulis di Pre-setup TC) menyimpan seleksi B lewat sesi API aktor (suite.md); User A adalah akun hook `before`. Kemampuan membaca System Log per user (User A dan User B) disediakan tim FE/BE tanpa endpoint karangan.
- Baseline log: N0 (Modal Changelog: Group), A0 (Activity Log), SA0 (System Log User A), SB0 (System Log User B) dicatat pada langkah 3, 5, dan 6, sebelum aksi pemicu pertama yang diasersi (S-12).
- Untuk siklus 2 (TC-990) hook mengatur enam group `G1` (terlama) sampai `G6` dibuat berurutan, cap 3, seleksi G4, G5, G6 sudah diterapkan, dan downgrade berikutnya dijadwalkan (cap baru 2), T-30 berjalan; keadaan dipulihkan lewat fixture BE sebagai langkah penghubung.

## Test Steps

### Baseline log

1. Buka Modal Changelog: Group
2. Verifikasi sedikitnya satu entri tampil di Modal Changelog: Group
3. Catat jumlah entri Modal Changelog: Group sebagai baseline N0 (jumlah total pada footer pagination)
4. Tutup Modal Changelog: Group
5. Catat jumlah entri Activity Log sebagai baseline A0 (kemampuan baca disediakan tim FE/BE)
6. Catat jumlah entri System Log User A sebagai SA0 dan System Log User B sebagai SB0

### TC-FA-GRP-989: Log ditulis saat diterapkan di T-0

7. Buka Wizard Reconciliation > Step Group Consolidation
8. Centang `Head Office`, `Warehouse A`, dan `Branch Office` (seleksi A)
9. Klik [Save Selection] sebagai User A
10. Tunggu aksi selesai
11. User B (sesi API) menyimpan seleksi B (`Warehouse B`, `Disposal Yard`, `Global HQ`) hingga seleksi tersimpan
12. Buka Modal Changelog: Group
13. Verifikasi jumlah entri Modal Changelog: Group sama dengan baseline N0
14. Tutup Modal Changelog: Group
15. Verifikasi jumlah entri Activity Log sama dengan baseline A0
16. Verifikasi jumlah entri System Log User A sama dengan SA0 dan System Log User B sama dengan SB0
17. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
18. Catat waktu sesudah transaksi T-0 commit
19. Buka Modal Changelog: Group, lalu ketik Search `{runId}-281`, tekan Enter
20. Verifikasi entri Action `Marked as Excess (Group Consolidation)` untuk `Head Office`, `Warehouse A`, dan `Branch Office` dengan Modified By = User B (submit terakhir)
21. Verifikasi Date entri sesuai waktu penerapan di T-0 (toleransi satu menit)
22. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group
23. Verifikasi entri Activity Log `Marked as Excess (Group Consolidation)` untuk ketiga group tersebut (dibaca lewat kemampuan baca)
24. Verifikasi System Log User B memuat entri untuk penerapan seleksi di T-0
25. Verifikasi System Log User A tidak bertambah (sama dengan SA0)

### TC-FA-GRP-990: Siklus downgrade berikutnya memulai siklus baru

26. Pulihkan state siklus 2 lewat fixture BE: G1 sampai G6, cap 3, seleksi G4, G5, G6 diterapkan (G1, G2, G3 Excess), downgrade berikutnya dijadwalkan (cap baru 2), customer belum submit
27. Buka Wizard Reconciliation > Step Group Consolidation
28. Verifikasi seleksi siklus 1 dibuang dan Wizard memuat seluruh 6 group (termasuk G1 sampai G3 yang Excess)
29. Verifikasi seluruh checkbox unchecked
30. Klik [Cancel]
31. Picu hook uji handler plan-efektif pada tanggal T-0 downgrade terjadwal di lingkungan non-produksi, tunggu transaksi T-0 commit
32. Buka Fixed Asset > Settings > Groups
33. Verifikasi `G1` dan `G2` (terlama) usable
34. Verifikasi `G3` sampai `G6` berstatus Excess
35. Buka Modal Changelog: Group, lalu ketik Search `{runId}-281`, tekan Enter
36. Verifikasi `G1` dan `G2` memiliki entri Action `Restored from Excess (Group Consolidation)`
37. Verifikasi `G4`, `G5`, dan `G6` memiliki entri Action `Marked as Excess (Group Consolidation)`
38. Verifikasi `G3` tanpa entri baru pada siklus ini
39. Verifikasi Modified By seluruh entri baru = System
40. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 3 sampai 7, 10 sampai 12, 14, 17 sampai 19, 22, 26 dan 27, 30 sampai 32, 35, 40: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Dua TC memakai kelas h (T-0 penerapan seleksi) dengan pemicu hook uji; User B hanya memicu perubahan state lewat sesi API dan bukan konteks kedua (P-2 2026-10-30, tanpa butir Notes).
- Klausa "tidak ada baris Marked/Restored baru" sebelum T-0 (TC-989 Expected a) diasersi pada langkah 13, 15, dan seterusnya dengan baseline jumlah entri; anchor positif: langkah 2 (entri lain tampil) dan toast/penyimpanan seleksi. Absence `G3` tanpa baris baru (TC-990) didahului entri `G1` dan `G2` pada Changelog (anchor, 8b butir 2). Absence System Log User A didahului entri System Log User B (langkah 24).
- Spec berisi lebih dari 35 langkah. Alasan: dua TC satu kelas (h, penerapan T-0) dan berdiri sendiri; sekitar 17 langkah adalah penghubung seeding, pemicu T-0, dan pembacaan log berpola, bukan asersi baru.
- P-1 (state berat): TC-990 memakai siklus 1 yang dibangun lewat fixture BE; pembangunan ulang state dilakukan di langkah penghubung.
- Temuan untuk QA:
  - TC-989 Expected c tidak menyebut surface System Log (halaman mana) maupun cara membuka System Log User A dan User B; spec memakai kemampuan baca disediakan tim FE/BE.
  - TC-989 Pre-setup tidak menyebut akun User B; spec menulis akun disediakan tim FE tanpa mengarang email.
  - TC-990 Expected a ("status pernah submit di-reset") tidak punya langkah observasi selain isi Wizard; spec mengasersi seleksi dibuang dan seluruh checkbox unchecked.
