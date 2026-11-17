---
id: TC-FA-TDC-E2E-152-sort-active-effective-from-last-updated-guard-dan-urutan-deterministik
title: "Sort: Active, Effective From, Last Updated, Guard Kolom, dan Urutan Deterministik"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-532
  - TC-FA-TDC-533
  - TC-FA-TDC-534
  - TC-FA-TDC-535
  - TC-FA-TDC-536
  - TC-FA-TDC-537
  - TC-FA-TDC-538
sourceRules: ["§4.1.1#r1", "§4.1.1#b8", "§9.5#r1", "§4.1.1#r13", "§4.4#r10", "§4.1.1#r3", "§4.4#r11", "§9.5#r3", "§5#b6"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [2, 4]
  "§4.1.1#b8": [6, 8]
  "§9.5#r1": 10
  "§4.1.1#r13": [15, 17]
  "§4.4#r10": [23, 29]
  "§4.1.1#r3": 24
  "§4.4#r11": 28
  "§9.5#r3": 39
  "§5#b6": 42
anchor: [25, 26, 38]
coverage:
  web: automated
---

# Sort: Active, Effective From, Last Updated, Guard Kolom, dan Urutan Deterministik

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman untuk TC-FA-TDC-532 sampai 536. NB-OLD berstatus Inactive dan 8 class lain Active; NB-1 dan NB-4 memiliki Effective From `Jan 2026`, class lain `—`; Used By NB-1 `5`, NB-SL `4`, NB-2 `3`, BLD-P `1`, class lain `0`. Last Updated: BLD-NP `22/10/26`, NB-SL `18/08/26`, NB-4 `03/03/26`, BLD-P `14/01/26`, LAND, NB-1, NB-2, NB-KHS, dan NB-OLD `01/01/26`. Kolom Last Updated Hidden (default) dan ditampilkan oleh langkah spec.
- Data Dinamis (milik spec, dibuat lewat seeding API pada langkah 31, idempotent, dihapus di `after`): 17 class Active tambahan `TDC-01` sampai `TDC-17` (Asset Type `Building`, Allowed Methods `Straight Line`, Class Name `Kelas uji 01` sampai `Kelas uji 17`) sehingga tabel berisi 26 class untuk TC-FA-TDC-537 dan 538; urutan default Class Code A-Z (9 class Example Data lalu TDC-01 sampai TDC-17). Kode class memakai literal TC tanpa suffix `{runId}-<NNN>` karena batas Class Code 15 karakter (lihat Temuan untuk QA).
- Kemampuan teknis: seeding sembilan class Example Data dan 17 class tambahan lewat API (`suite.md`); Overlay Column Visibility; membaca indikator sort pada header; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: Sort dan nomor halaman pada tabel (direset `beforeEach` suite), konfigurasi kolom (Last Updated ditampilkan lalu disembunyikan kembali oleh langkah di spec), dan 17 class tambahan (dihapus hook `after`). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### Sort kolom Active (TC-FA-TDC-532)

1. Klik header Active
2. Verifikasi Active First: 8 class Active urut Class Code (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-SL) lalu NB-OLD (Inactive)
3. Klik header Active
4. Verifikasi Inactive First: NB-OLD di atas lalu 8 class Active urut Class Code

### Sort kolom Effective From: nilai kosong dianggap paling awal (TC-FA-TDC-533)

5. Klik header Effective From
6. Verifikasi Oldest First: 7 baris `—` di awal (BLD-NP, BLD-P, LAND, NB-2, NB-KHS, NB-OLD, NB-SL) lalu NB-1 dan NB-4 (`Jan 2026`)
7. Klik header Effective From
8. Verifikasi Newest First: NB-1 dan NB-4 (`Jan 2026`) di awal lalu 7 baris `—` urut Class Code
9. Klik header Effective From
10. Verifikasi netral: kembali ke urutan default Class Code A-Z

### Sort kolom Last Updated (TC-FA-TDC-534)

11. Klik header Actions `⋯`
12. Centang kolom Last Updated
13. Tutup Overlay Column Visibility
14. Klik header Last Updated
15. Verifikasi Oldest First: LAND, NB-1, NB-2, NB-KHS, NB-OLD (01/01/26), BLD-P, NB-4, NB-SL, BLD-NP
16. Klik header Last Updated
17. Verifikasi Newest First: BLD-NP, NB-SL, NB-4, BLD-P, lalu LAND, NB-1, NB-2, NB-KHS, NB-OLD
18. Klik header Actions `⋯`
19. Hapus centang kolom Last Updated
20. Tutup Overlay Column Visibility

### Berpindah kolom sort (TC-FA-TDC-535)

21. Klik header Used By dua kali (Descending)
22. Klik header Class Name
23. Verifikasi indikator sort Used By hilang (netral)
24. Verifikasi Class Name Ascending: BLD-P, BLD-NP, NB-1, NB-2, NB-4, NB-OLD, NB-KHS, NB-SL, LAND

### Guard kolom tanpa sort (TC-FA-TDC-536)

25. Verifikasi header Class Name menampilkan ikon sort
26. Verifikasi kolom checkbox dan kolom Actions tidak memiliki ikon sort
27. Klik header Actions `⋯`
28. Verifikasi Overlay Column Visibility terbuka
29. Verifikasi urutan baris tidak berubah (Class Name Ascending)
30. Tutup Overlay Column Visibility

### Baris bernilai sama berurutan deterministik antar halaman (TC-FA-TDC-537)

31. Tambahkan 17 class `TDC-01` sampai `TDC-17` lewat seeding API hingga tabel berisi 26 class, lalu muat ulang halaman
32. Klik header Asset Type
33. Catat 10 baris halaman 1
34. Pindah ke halaman 2
35. Catat baris halaman 2
36. Pindah ke halaman 3
37. Catat baris halaman 3
38. Verifikasi baris dengan Asset Type sama mengikuti Class Code A-Z
39. Verifikasi tidak ada baris ganda dan tidak ada baris terlewat antar halaman 1, 2, dan 3 (total 26 baris unik)

### Mengganti sort tetap di nomor halaman sekarang (TC-FA-TDC-538)

40. Pindah ke halaman 2
41. Klik header Class Name
42. Verifikasi tabel tetap di halaman 2 dengan urutan dataset baru

## Notes

- Urutan TC dalam spec: TC-FA-TDC-532 sampai 538; TC-FA-TDC-537 dan 538 terakhir karena butuh tabel 26 class yang dibangun pada langkah 31, sedangkan TC lain mengasersi sembilan class Example Data.
- Langkah penghubung (S-03, S-09): langkah 11 sampai 13 (menampilkan kolom Last Updated yang Hidden), langkah 18 sampai 20 (pemulihan Setup Column agar Last Updated kembali Hidden; 8b.14, R-24), langkah 30 (menutup Overlay), langkah 31 (menambah 17 class lewat seeding API), langkah 33, 35, dan 37 ("Catat" adalah aksi TC-FA-TDC-537 tanpa asersi), langkah 40 (pindah ke halaman 2 sebagai langkah TC-FA-TDC-538; sort Asset Type dari TC-FA-TDC-537 diganti oleh langkah 41), langkah 25 (anchor positif ikon sort pada header lain untuk asersi absence langkah 26; 8b.2, tidak ada di TC).
- Spec ini 42 langkah, di atas ~35 langkah. Alasan: satu topik (Sort tabel utama) pada dataset Example Data yang sama untuk TC-FA-TDC-532 sampai 536 dan dataset 26 class untuk dua TC terakhir (pagination butuh lebih dari 10 baris), tiap blok TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan S-01 mengharuskan satu `Verifikasi` per klausa.
- Temuan untuk QA:
  - Class Code maksimal 15 karakter: suffix `{runId}-<NNN>` (S-12) tidak muat, jadi kode `TDC-01` sampai `TDC-17` memakai literal TC dengan syarat seeding idempotent, cleanup oleh spec, dan suite serial. Kode yang sama dipakai spec 146, 157, dan 158; Lampiran A belum punya butir modul ini.
  - TC-FA-TDC-537 langkah 2 ("Catat 10 baris halaman 1, pindah ke halaman 2 dan 3, lalu catat baris") tanpa cara mencatat; spec menuliskan "Catat" sebagai aksi dan mengasersi sesudah halaman 3.
  - TC-FA-TDC-538 tidak menyebut sort yang aktif sebelum langkah; spec memakai sort Asset Type sisa TC-FA-TDC-537 sebagai keadaan awal dan mengikuti langkah TC (pindah ke halaman 2 lalu klik header Class Name).
  - TC-FA-TDC-534 menyebut tanggal Last Updated tanpa nilai format General Settings; spec mengikuti nilai TC.
  - Email akun Total Control tidak tertulis di TC.
