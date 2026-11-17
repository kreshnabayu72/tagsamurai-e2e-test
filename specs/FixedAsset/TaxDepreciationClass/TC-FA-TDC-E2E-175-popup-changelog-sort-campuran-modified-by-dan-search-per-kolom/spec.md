---
id: TC-FA-TDC-E2E-175-popup-changelog-sort-campuran-modified-by-dan-search-per-kolom
title: "Popup Changelog: Sort Kolom Campuran, Sort Modified By, dan Search per Kolom"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-625
  - TC-FA-TDC-626
  - TC-FA-TDC-627
  - TC-FA-TDC-628
sourceRules: ["§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r32", "ST-26", "§5#b2"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r29": [4, 5, 6, 23]
  "§4.1.1#r30": [8, 9, 10, 25]
  "§4.1.1#r31": [12, 27]
  "§4.1.1#r26": 17
  "§4.1.1#r27": 19
  "§4.1.1#r28": 21
  "§4.1.1#r32": 29
  "ST-26": 31
  "§5#b2": 31
anchor: [14]
coverage:
  web: automated
---

# Popup Changelog: Sort Kolom Campuran, Sort Modified By, dan Search per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. User `Budi` bernama lengkap `Budi Hartono`, `Rina P` bernama lengkap `Rina Putri`; Modified By memuat `Budi` (3 baris), `Rina P` (10 baris), dan `System` (3 baris). Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Tabel kata kunci Search TC-FA-TDC-627 (urutan langkah 16 sampai 27):

  | Kolom | Kata kunci | Hasil |
  |---|---|---|
  | Action | `Delete` | 1 baris (Delete NB-3) |
  | Class Code | `NB-KHS` | 1 baris |
  | Field | `Last Posted` | 2 baris Last Posted Tax Year |
  | Old Value | `Kelompok khusus SL` | 1 baris (Edit NB-SL Class Name) |
  | New Value | `Contoh referensi regulasi` | 1 baris (Create BLD-NP Regulation Reference) |
  | Modified By | `Budi` | 3 baris |

- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); mengganti page size Popup.
- State global yang diubah: sort, Search, dan page size Popup Changelog; Search dikosongkan di langkah 32, page size dikembalikan ke 10 di langkah 33, dan Popup ditutup di langkah 34.

## Test Steps

1. Klik icon Changelog
2. Ganti page size menjadi 25

### TC-FA-TDC-625: Sort kolom campuran tipe Old Value dan New Value

3. Klik header Old Value satu kali
4. Verifikasi Old Value Ascending: nilai angka lebih dulu (`16`, `2025`)
5. Verifikasi Old Value Ascending dilanjutkan nilai teks A-Z (`Active`, `Inactive`, `Jan 2025`, `Jan 2025`, `Jan 2027`, `Kelompok khusus SL`, `NB-3`)
6. Verifikasi Old Value Ascending diakhiri nilai kosong `—` (7 baris)
7. Klik header New Value satu kali
8. Verifikasi New Value Ascending: nilai angka lebih dulu (`8`, `20`, `2026`, `2026`)
9. Verifikasi New Value Ascending dilanjutkan nilai teks A-Z (`Active`, `BLD-P`, `Building`, `Contoh referensi regulasi`, `Inactive`, `Jan 2026`, `Jan 2026`, `Jan 2027`, `Kelompok khusus Straight Line`, `Straight Line`)
10. Verifikasi New Value Ascending diakhiri nilai kosong `—` (2 baris)

### TC-FA-TDC-626: Sort Modified By berdasarkan nama lengkap

11. Klik header Modified By satu kali
12. Verifikasi Modified By Ascending: `Budi` (3 baris), lalu `Rina P` (10 baris), lalu `System` (3 baris)
13. Klik header Modified By untuk kedua kalinya
14. Verifikasi Modified By Descending: `System` (3 baris), lalu `Rina P` (10 baris), lalu `Budi` (3 baris)
15. Klik header Modified By untuk ketiga kalinya

### TC-FA-TDC-627: Search per kolom

Search pada langkah 16 sampai 27 mengikuti tabel kata kunci pada Prerequisites.

16. Ketik Search `Delete`, tekan Enter
17. Verifikasi tabel menampilkan tepat 1 baris (Delete NB-3)
18. Ganti isi kotak search dengan `NB-KHS`, tekan Enter
19. Verifikasi tabel menampilkan tepat 1 baris
20. Ganti isi kotak search dengan `Last Posted`, tekan Enter
21. Verifikasi tabel menampilkan tepat 2 baris Last Posted Tax Year
22. Ganti isi kotak search dengan `Kelompok khusus SL`, tekan Enter
23. Verifikasi tabel menampilkan tepat 1 baris (Edit NB-SL Class Name)
24. Ganti isi kotak search dengan `Contoh referensi regulasi`, tekan Enter
25. Verifikasi tabel menampilkan tepat 1 baris (Create BLD-NP Regulation Reference)
26. Ganti isi kotak search dengan `Budi`, tekan Enter
27. Verifikasi tabel menampilkan tepat 3 baris

### TC-FA-TDC-628: Guard kolom Date tidak dicari lewat Search

28. Klik `(←)` pada kotak Search
29. Verifikasi tabel memuat entri bertanggal 28/10/26
30. Ketik Search `28/10/26`, tekan Enter
31. Verifikasi Popup menampilkan `No results found`
32. Klik `(←)` pada kotak Search
33. Ganti page size kembali menjadi 10
34. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah 1 TC-FA-TDC-625 sampai TC-FA-TDC-628 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1.
- TC-FA-TDC-625 sampai TC-FA-TDC-628 dijalankan pada page size 25 (langkah 2) supaya seluruh 16 entri teramati pada satu halaman (S-14); Expected TC-FA-TDC-625 menghitung 16 nilai per kolom.
- Langkah penghubung (S-03): langkah 2 dan 33 (ganti page size), langkah 15 (klik ketiga header Modified By mengembalikan sort ke bawaan), langkah 28 dan 32 (mengosongkan Search lewat `(←)`), langkah 29 (anchor bahwa entri bertanggal 28/10/26 ada sebelum Search `28/10/26`; Expected TC-FA-TDC-628 menyebut "walau ada entri bertanggal 28/10/26"), langkah 34 (menutup Popup).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-627 langkah 3 sampai 7 hanya menulis "Ganti keyword" tanpa menyebut Enter; spec menekan Enter sesuai aturan Search (hanya menyaring saat Enter).
  - Isi Popup Changelog memakai jumlah entri absolut (16 entri, jumlah baris per hasil Search dan per grup Modified By) pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec mengikuti TC dan membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog dengan 16 entri Example Data (tidak disebut TC, PRD, atau LLD).
  - TC-FA-TDC-625 tidak menyatakan keadaan sort sebelum klik header New Value (sort Old Value dilepas oleh sort New Value); spec mengikuti TC.
