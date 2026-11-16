---
id: TC-FA-FATR-E2E-024-changelog-download
title: "Download Changelog"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [§4.1#p88, §5#r6, EB-DL-1@changelog, EB-DL-2@changelog, EB-DL-3@changelog, EB-DL-4]
smoke: [EB-DL-4]
dependsOn: []
trace:
  §4.1#p88: [7, 11]
  §5#r6: [4, 7]
  EB-DL-1@changelog: [8, 16, 17, 33]
  EB-DL-2@changelog: [6]
  EB-DL-3@changelog: [7, 11]
  EB-DL-4: [21, 26, 27]
anchor: [2, 13, 32]
coverage:
  web: automated
---

# Download Changelog

## Prerequisites
- Aktor: Total Control pada entitas khusus `Wirasena Logistik {runId}` (DU-024-1), yang tidak dipakai spec lain.
- Layar awal: Settings > Transaction Settings.
- Data:
  - DU-024-1: entitas `Wirasena Logistik {runId}` dengan Changelog yang hanya berisi entri DU-024-2 sampai DU-024-5, total `12` entri.
  - DU-024-2: entri Changelog Category `Vehicle > Pool car {runId}`, Field `Borrow (Allow Borrow)`, Old Value `Inherit`, New Value `Deny`, Modified By `Budi Santoso` (tampil `Budi S`), Action `Edit`, Date `T0 − 3 hari`.
  - DU-024-3: entri Changelog Category `Vehicle > Pool car {runId}`, Field `Borrow (Max duration)`, Old Value `Inherit`, New Value `30 days`, Modified By `Rina Wulandari` (tampil `Rina W`), Action `Edit`, Date `T0 − 4 hari`.
  - DU-024-4: entri Changelog Category `Machinery {runId}`, Field `Transfer (Approval scope)`, Old Value `Inherit`, New Value `Origin only`, Modified By `Budi Santoso`, Action `Edit`, Date `T0 − 2 hari`.
  - DU-024-5: 9 entri Changelog Category `Machinery {runId}`, Field `Borrow (Max extensions)`, berantai menurut urutan tercatat: entri pertama Old Value `Inherit` dan New Value `1`, entri ke-n (n dari 2 sampai 9) Old Value `{n-1}` dan New Value `{n}`, Modified By `Budi Santoso`, Action `Edit`, Date `T0 − 1 hari`.
  - DU-024-6: kata kunci Search `Tidak Ditemukan {runId}` yang tidak cocok dengan entri mana pun.

## Test Steps

### Unduhan tanpa saringan memuat seluruh baris melewati satu halaman
1. Klik ikon Changelog di header
2. Verifikasi halaman pertama tabel menampilkan `10` baris
3. Klik ikon Download di toolbar dialog Changelog
4. Verifikasi opsi `Download as CSV` dan `Download as XLSX` tampil
5. Klik `Download as CSV`
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas terunduh bernama `Changelog-Transaction-Settings` dengan ekstensi csv
8. Verifikasi berkas memuat `12` baris data

### Unduhan XLSX memakai ekstensi xlsx
9. Klik ikon Download di toolbar dialog Changelog
10. Klik `Download as XLSX`
11. Verifikasi berkas terunduh bernama `Changelog-Transaction-Settings` dengan ekstensi xlsx

### Unduhan mengikuti hasil Search
12. Ketik Search `Vehicle > Pool car {runId}`, tekan Enter
13. Verifikasi baris Field `Borrow (Allow Borrow)` dan baris Field `Borrow (Max duration)` tampil
14. Klik ikon Download di toolbar dialog Changelog
15. Klik `Download as CSV`
16. Verifikasi berkas memuat `2` baris data
17. Verifikasi berkas tidak memuat baris dengan Field `Transfer (Approval scope)`

### Unduhan dengan hasil nol baris hanya berisi header
18. Ganti isi kotak search dengan `Tidak Ditemukan {runId}`, tekan Enter
19. Klik ikon Download di toolbar dialog Changelog
20. Klik `Download as CSV`
21. Verifikasi berkas berisi baris header kolom dan nol baris data

### Unduhan mengikuti Sort aktif
22. Klik `(←)` pada kotak Search
23. Klik header kolom `Field`
24. Klik ikon Download di toolbar dialog Changelog
25. Klik `Download as CSV`
26. Verifikasi baris data pertama berkas memiliki Field `Borrow (Allow Borrow)`
27. Verifikasi baris data terakhir berkas memiliki Field `Transfer (Approval scope)`

### Kolom yang disembunyikan tidak ikut diunduh
28. Klik header kolom Actions pada tabel Changelog
29. Nonaktifkan kolom `Old Value` pada Column Visibility
30. Klik ikon Download di toolbar dialog Changelog
31. Klik `Download as CSV`
32. Verifikasi header berkas memuat kolom `New Value`
33. Verifikasi tidak ada kolom `Old Value` pada header berkas
34. Aktifkan kembali kolom `Old Value` pada Column Visibility
