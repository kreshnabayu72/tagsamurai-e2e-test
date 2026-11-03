---
id: TC-FA-GRP-E2E-079-delete-dan-bulk-delete-node-excess-auto-reset-excess-saat-count-di-bawah-cap
title: "Delete dan Bulk Delete Node Excess: Auto-Reset Excess Bila Count <= Cap dan Tidak Mereset Excess Lain Saat Count > Cap"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-240
  - TC-FA-GRP-241
  - TC-FA-GRP-269
coverage:
  web: automated
---

# Delete dan Bulk Delete Node Excess: Auto-Reset Excess Bila Count <= Cap dan Tidak Mereset Excess Lain Saat Count > Cap

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client plan Growth (cap 3 group; email dan `Spectra.env.FA_GROWTH_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC; Pre-setup No 8); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Kelas h (state tenant): plan Growth dengan cap 3 adalah state client; spec tidak mengubah plan, hanya men-seed ulang jumlah group dan status Excess per blok (langkah 1, 7, 16) dan memulihkannya di `after` lewat fixture BE.
- Data Dinamis (di-seed per blok): blok TC-241: 5 group termasuk `Exc 1` dan `Exc 2` (berstatus Excess); blok TC-240: 4 group, yaitu 2 usable, `Warehouse B` (Excess, kosong), dan `Excess Other` (Excess, kosong, milik spec ini); blok TC-269: 5 group dengan `Exc A` dan `Exc B` berstatus Excess serta `Emp 1` dan `Emp 2` kosong yang usable.
- Kemampuan teknis (disediakan tim FE/BE): menetapkan status Excess pada node dan men-seed jumlah group sesuai kebutuhan blok tanpa endpoint karangan; membaca status Excess node lewat UI (nama di-dim).
- Cleanup di `after`: hapus sisa data milik spec dan pulihkan status Excess lewat fixture BE.

## Test Steps

### TC-FA-GRP-241: Delete node Excess saat count masih di atas cap tidak mereset Excess lain

1. Seed ulang client Growth: 5 group dengan `Exc 1` dan `Exc 2` berstatus Excess, lalu muat ulang halaman
2. Verifikasi `Exc 1` dan `Exc 2` berstatus Excess (nama di-dim)
3. Buka elipsis `⋯` baris `Exc 1`, pilih `Delete`
4. Klik [Delete]
5. Verifikasi toast sukses "Success, group has been deleted."
6. Verifikasi `Exc 2` tetap berstatus Excess (nama di-dim, count 4 di atas cap 3)

### TC-FA-GRP-240: Delete node Excess dengan count mencapai cap memicu auto-reset

7. Seed ulang client Growth: 4 group, yaitu 2 usable, `Warehouse B` (Excess, kosong), dan `Excess Other` (Excess, kosong), lalu muat ulang halaman
8. Verifikasi `Warehouse B` dan `Excess Other` berstatus Excess (nama di-dim)
9. Buka elipsis `⋯` baris `Warehouse B`, pilih `Delete`
10. Klik [Delete]
11. Verifikasi toast sukses "Success, group has been deleted."
12. Verifikasi `Excess Other` kembali usable (tidak di-dim) pada count 3 yang sama dengan cap
13. Buka elipsis `Excess Other`
14. Verifikasi `Edit` dan `Add Subgroup` tampil pada menu node
15. Tutup menu elipsis

### TC-FA-GRP-269: Bulk Delete menurunkan count sampai cap memicu auto-reset

16. Seed ulang client Growth: 5 group dengan `Exc A` dan `Exc B` berstatus Excess serta `Emp 1` dan `Emp 2` kosong dan usable, lalu muat ulang halaman
17. Verifikasi `Exc A` dan `Exc B` berstatus Excess (nama di-dim)
18. Centang `Emp 1` dan `Emp 2`
19. Buka Bulk Action, pilih `Delete`
20. Klik [Delete]
21. Verifikasi toast sukses "Success, group has been deleted."
22. Verifikasi `Exc A` dan `Exc B` kembali usable (tidak di-dim)
23. Buka Modal Changelog: Group
24. Ketik Search `Exc A`, tekan Enter
25. Verifikasi entri Action `Restored from Excess (Group Consolidation)` untuk `Exc A` dengan Modified By = aktor (format [First Name] [Last Initial])
26. Ganti isi kotak search dengan `Exc B`, tekan Enter
27. Verifikasi entri Action `Restored from Excess (Group Consolidation)` untuk `Exc B` dengan Modified By = aktor (format [First Name] [Last Initial])
28. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 7, 15 dan 16, 23 dan 24, 26, 28: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Seeding ulang antar blok (langkah 1, 7, 16) memulihkan state tiap TC karena blok sebelumnya mengubahnya (S-09). Kelas h: perubahan Excess disiapkan fixture BE; spec tidak mengubah plan atau cap.
- Entri Changelog TC-269 dicari lewat Search nama group bersuffix unik sehingga baseline entri nol (S-12); Search untuk menemukan baris target adalah langkah penghubung (R-16). Langkah 21 (toast sukses) adalah asersi tambahan sebagai anchor untuk asersi status sesudah Delete (S-03); tidak ada di Expected TC-269.
- Temuan untuk QA:
  - TC-240 Post Condition (Changelog Restored from Excess untuk `Excess Other`) tidak punya langkah observasi; tidak diasersi (S-01).
  - TC-241 Expected hanya menyebut "Delete sukses" tanpa teks; spec mengasersi toast sukses standar Delete.
