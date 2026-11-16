---
id: TC-FA-TDC-E2E-174-popup-changelog-kolom-old-new-value-modified-by-urutan-bawaan-dan-sort-date
title: "Popup Changelog: Kolom Old Value, New Value, Modified By, Urutan Bawaan, dan Sort Date"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-621
  - TC-FA-TDC-622
  - TC-FA-TDC-623
  - TC-FA-TDC-624
sourceRules: ["§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r32", "§4.1.1#r45", "§4.1.1#r46", "L-03", "§4.1.1#r43", "§4.1.1#r31", "§4.1.1#r33", "§4.1.1#p8", "§4.1.1#r25", "§4.1.1#r47", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r29": [2, 4, 5, 6]
  "§4.1.1#r30": 2
  "§4.1.1#r32": [2, 8, 13]
  "§4.1.1#r45": 4
  "§4.1.1#r46": 5
  "L-03": 6
  "§4.1.1#r43": 6
  "§4.1.1#r31": [8, 9, 11]
  "§4.1.1#r33": 9
  "§4.1.1#p8": 13
  "§4.1.1#r25": [13, 15, 17, 19]
  "§4.1.1#r47": 13
  "§4.1.1#r26": [21, 23]
  "§4.1.1#r27": 25
  "§4.1.1#r28": 27
coverage:
  web: automated
---

# Popup Changelog: Kolom Old Value, New Value, Modified By, Urutan Bawaan, dan Sort Date

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD (6 `Create`, 1 `Delete`, 9 `Edit`; entri terbaru 28/10/26 09:15, entri terlama 01/01/26 00:05). User `Rina P` bernama lengkap `Rina Putri`; user `Budi` bernama lengkap `Budi Hartono`. Modified By memuat `Budi` (3 baris), `Rina P` (10 baris), dan `System` (3 baris). Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); mengarahkan kursor (hover) untuk tooltip; mengganti page size Popup.
- State global yang diubah: sort dan page size Popup Changelog; page size dikembalikan ke 10 di langkah 28 dan Popup ditutup di langkah 29.

## Test Steps

### TC-FA-TDC-621: Kolom Old Value dan New Value

1. Klik icon Changelog
2. Verifikasi baris Delete NB-3 (28/10/26): Old Value `NB-3`, New Value `—`
3. Klik halaman berikutnya (halaman 2)
4. Verifikasi baris Create BLD-P Class Code (14/01/26): Old Value `—`, New Value `BLD-P`
5. Verifikasi baris Create BLD-P Asset Type (14/01/26): Old Value `—`, New Value `Building`
6. Verifikasi baris Edit NB-4 Useful Life (03/03/26): Old Value `16`, New Value `20`
7. Klik halaman pertama (halaman 1)

### TC-FA-TDC-622: Kolom Modified By

8. Verifikasi Modified By baris 28/10/26 `Rina P`
9. Verifikasi Modified By baris 27/10/26 `System`
10. Arahkan kursor ke Modified By `Rina P` pada baris 28/10/26
11. Verifikasi tooltip nama lengkap `Rina Putri`

### TC-FA-TDC-623: Urutan bawaan dan siklus sort Date

12. Ganti page size menjadi 25
13. Verifikasi urutan awal Newest First: `28/10/26 09:15` di baris teratas dan `01/01/26 00:05` di baris terbawah
14. Klik header Date satu kali
15. Verifikasi urutan Oldest First: `01/01/26 00:05` di baris teratas dan `28/10/26 09:15` di baris terbawah
16. Klik header Date untuk kedua kalinya
17. Verifikasi urutan Newest First: `28/10/26 09:15` di baris teratas dan `01/01/26 00:05` di baris terbawah
18. Klik header Date untuk ketiga kalinya
19. Verifikasi urutan netral kembali ke default Newest First

### TC-FA-TDC-624: Sort kolom teks Action, Class Code, dan Field

20. Klik header Action satu kali
21. Verifikasi Action Ascending: grup `Create` (6 baris) di atas, lalu `Delete` (1 baris), lalu `Edit` (9 baris)
22. Klik header Action untuk kedua kalinya
23. Verifikasi Action Descending: grup `Edit` (9 baris) di atas, lalu `Delete` (1 baris), lalu `Create` (6 baris)
24. Klik header Class Code satu kali
25. Verifikasi Class Code Ascending (tidak case-sensitive): BLD-NP, BLD-NP (Jan 2027), BLD-P, NB-1, NB-2 (Jan 2027), NB-3, NB-4, NB-KHS, NB-OLD, NB-SL
26. Klik header Field satu kali
27. Verifikasi Field Ascending: Allowed Methods, Asset Type, Class Code, Class Name, Current Version, Effective From, Last Posted Tax Year, Regulation Reference, Scheduled Version, Status, Useful Life
28. Ganti page size kembali menjadi 10
29. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah 1 TC-FA-TDC-622, TC-FA-TDC-623, dan TC-FA-TDC-624 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1.
- Urutan asersi TC-FA-TDC-621 mengikuti urutan state (8b.5): baris Delete NB-3 di halaman 1 lebih dulu, lalu baris halaman 2.
- TC-FA-TDC-623 dan TC-FA-TDC-624 dijalankan pada page size 25 (langkah 12) supaya baris teratas dan terbawah dari 16 entri teramati pada satu halaman (S-14).
- Langkah penghubung (S-03): langkah 3 dan 7 (pindah halaman), langkah 12 dan 28 (ganti page size), langkah 29 (menutup Popup, yang membuang sort Popup).
- Interpretasi TC-FA-TDC-623: "Klik header Date dua kali" dan "ketiga kali" dibaca kumulatif (klik kedua dan klik ketiga sejak klik pertama), sesuai urutan butir Expected b, c, dan d.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-621 tidak menyebut halaman tempat baris bertanggal 14/01/26 dan 03/03/26 berada; berdasarkan TC-FA-TDC-638 (halaman 2 memuat 6 entri terlama dari 18/08/26 sampai 01/01/26) spec berpindah ke halaman 2.
  - TC-FA-TDC-623 menyebut "01/01/26 00:05 di bawah" tanpa menyebut halaman terakhir (di page size 10 baris itu berada di halaman 2); spec memakai page size 25.
  - Isi Popup Changelog memakai jumlah entri absolut (16 entri, jumlah baris per grup) pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec mengikuti TC dan membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog dengan 16 entri Example Data (tidak disebut TC, PRD, atau LLD).
  - TC-FA-TDC-624 tidak menyatakan keadaan sort Popup sebelum langkah (sort Date bawaan) dan cara mengembalikannya.
