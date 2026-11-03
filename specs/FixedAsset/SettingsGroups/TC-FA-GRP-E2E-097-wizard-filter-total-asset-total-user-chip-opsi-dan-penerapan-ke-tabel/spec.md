---
id: TC-FA-GRP-E2E-097-wizard-filter-total-asset-total-user-chip-opsi-dan-penerapan-ke-tabel
title: "Wizard: Filter Group/Total Asset/Total User dan Chip Opsi Filter Group (Hapus via (X) dan via Uncheck)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-959
  - TC-FA-GRP-1041
  - TC-FA-GRP-1042
coverage:
  web: automated
---

# Wizard: Filter Group/Total Asset/Total User dan Chip Opsi Filter Group (Hapus via (X) dan via Uncheck)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.

## Test Steps

### TC-FA-GRP-959: Filter Group, Total Asset, Total User

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Klik icon Filter
3. Verifikasi Filter Group berupa multi-select searchable dengan placeholder "All groups"
4. Verifikasi Filter Total Asset dan Total User berupa Range Min-Max
5. Pilih opsi `Warehouse A` pada Group, isi Total Asset Min `1`
6. Klik [Apply]
7. Verifikasi sedikitnya satu baris tampil
8. Verifikasi tabel hanya menampilkan baris yang memenuhi seluruh filter (`Warehouse A`)
9. Hapus seluruh filter

### TC-FA-GRP-1041: Chip opsi dihapus via (X) pada chip

10. Klik icon Filter
11. Centang opsi A (`Warehouse A`) lalu opsi B (`Warehouse B`) pada Group
12. Tutup dropdown
13. Verifikasi chip A dan chip B tampil di dalam field (chip B tidak menggantikan chip A)
14. Klik (X) pada chip A
15. Verifikasi chip A hilang dari field
16. Verifikasi checkbox A di dropdown ikut ter-uncheck
17. Verifikasi chip B tetap ada
18. Klik [Apply]
19. Verifikasi sedikitnya satu baris tampil
20. Verifikasi tabel hanya menyaring Group = opsi B (`Warehouse B`)
21. Hapus seluruh filter

### TC-FA-GRP-1042: Chip opsi dihapus via uncheck di dalam dropdown

22. Klik icon Filter
23. Centang opsi A lalu opsi B pada Group
24. Buka lagi dropdown dan uncheck opsi A dari dalam dropdown
25. Verifikasi chip A hilang dari field
26. Verifikasi chip B tetap ada
27. Klik [Apply]
28. Verifikasi sedikitnya satu baris tampil
29. Verifikasi tabel hanya menyaring Group = opsi B (`Warehouse B`)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 9, 21: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Filter dibersihkan antar TC (langkah penghubung, S-09). Asersi universal "hanya menyaring ... opsi B" didahului pembanding generik "sedikitnya satu baris tampil" (8b butir 2).
- Temuan untuk QA:
  - TC-959 menyebut Total Asset Min `1` sebagai contoh; nilai Min dan Max lain tidak diasersi.
  - Pagination Step Group Consolidation (TC-1065, TC-1066) membutuhkan 25 group dan diuji pada spec 282.
