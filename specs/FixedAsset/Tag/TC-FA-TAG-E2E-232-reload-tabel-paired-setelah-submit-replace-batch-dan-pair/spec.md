---
id: TC-FA-TAG-E2E-232-reload-tabel-paired-setelah-submit-replace-batch-dan-pair
title: "Reload Tabel Paired setelah Submit Replace, Batch Replace, dan Pair dengan State Dipertahankan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-977
  - TC-FA-TAG-978
  - TC-FA-TAG-979
coverage:
  web: automated
---

# Reload Tabel Paired setelah Submit Replace, Batch Replace, dan Pair dengan State Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri (Paired, Available), dan stok Global; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired | `aset220` |
| Aset Batch Replace | 'Excavator 20 Ton - 220' (`RF-00130`) dan 'Excavator 20 Ton - 221' (`RF-00140`), keduanya Group Plant A dengan satu Tag RFID Paired | `aset221` |
| Aset Pair | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Stok Global | Tag RFID `RF-00412` dan `RF-00415` berstatus Available, Tag NFC `NF-00500` berstatus Available | `stokAvailable` |
| Halaman 2 tab Paired | Pada Search `Excavator`, Filter TAG Type `RFID`, dan Sort Asset Name Z-A (page size 10) tab Paired memuat lebih dari 10 grup, dan grup Excavator 20 Ton / Plant A berada di halaman 2 | `grupHalaman2` |

- State yang diubah dan pemulihannya: Tag pada aset 220 dan 221, `RF-00412` (Available menjadi Paired), serta aset 51 (Not Paired Yet menjadi Paired). Langkah 13 dan 22 memulihkan semuanya lewat fixture backend sebelum blok berikutnya; hook `after` memulihkan keadaan awal walau spec gagal di tengah.

## Test Steps

### Reload setelah Close ringkasan Batch Replace (TC-FA-TAG-978)

1. Ketik Search `Excavator`, tekan Enter
2. Klik header Asset Name hingga terurut Z-A
3. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant A untuk membuka Popup Detail
4. Centang aset 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
5. Klik Bulk `Batch Replace TAG`
6. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
7. Klik [Submit & next]
8. Klik [Skip]
9. Klik [Close]
10. Verifikasi toast "Success, asset has been replaced."
11. Verifikasi tabel dimuat ulang dengan Search `Excavator` dipertahankan
12. Verifikasi tabel dimuat ulang dengan Sort Asset Name Z-A dipertahankan
13. Pulihkan aset 220 dan 221 ke Tag Paired semula serta `RF-00412` ke Available lewat fixture backend hingga tersimpan

### Reload setelah Submit Pair (TC-FA-TAG-979)

14. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant A untuk membuka Popup Detail
15. Klik tombol teks `Show` di samping `Not Paired Yet`
16. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Klik [Submit]
19. Verifikasi toast "Success, TAG has been paired."
20. Verifikasi tabel dimuat ulang dengan Search `Excavator` dipertahankan
21. Verifikasi tabel dimuat ulang dengan Sort Asset Name Z-A dipertahankan
22. Pulihkan aset 51 ke Not Paired Yet serta `RF-00412` ke Available lewat fixture backend hingga tersimpan

### Reload setelah Submit Replace (TC-FA-TAG-977)

23. Klik ikon Filter
24. Pilih TAG Type `RFID`
25. Klik `[Apply]`
26. Pindah ke halaman 2
27. Klik Asset Name `Excavator 20 Ton` pada baris grup Plant A untuk membuka Popup Detail
28. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
29. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
30. Klik [Submit]
31. Verifikasi toast "Success, TAG has been replaced."
32. Verifikasi tabel dimuat ulang dengan Search `Excavator` dipertahankan
33. Verifikasi tabel dimuat ulang dengan Filter TAG Type RFID dipertahankan
34. Verifikasi tabel dimuat ulang dengan Sort Asset Name Z-A dipertahankan
35. Verifikasi halaman yang sama (halaman 2) tetap aktif

## Notes

- Urutan TC pada spec: TC-FA-TAG-978, 979, 977. Search `Excavator` dan Sort Asset Name Z-A diatur pada langkah 1 dan 2 (TC-FA-TAG-978) dan dipertahankan tabel, terbukti pada langkah 11, 12, 20, dan 21. Karena itu langkah Search dan Sort milik TC-FA-TAG-979 (langkah 1 dan 2) dan TC-FA-TAG-977 (langkah 1 dan 3) tidak diketik ulang; TC-FA-TAG-977 menambah Filter dan halaman 2 (langkah 23 sampai 26). Tiap TC tetap dimulai dari data yang dipulihkan langkah 13 dan 22 (S-10).
- Langkah penghubung (S-03): langkah 13 dan 22 (pemulihan data lewat fixture backend, karena `RF-00412` dan Tag aset 220 dipakai bergantian oleh ketiga TC) dan langkah 26 (TC-FA-TAG-977 langkah 4: "pindah ke halaman 2 jika tersedia" ditulis tanpa syarat karena Prerequisites menjamin halaman 2).
- Temuan untuk QA:
  - TC-FA-TAG-977 langkah 4 "Pindah ke halaman 2 jika tersedia" adalah langkah bersyarat; Precondition f ("memuat lebih dari 10 grup") tidak menyebut Search, Filter, dan Sort yang berlaku maupun grup mana yang berada di halaman 2. Spec menetapkan data di Prerequisites (`grupHalaman2`).
  - TC-FA-TAG-977, 978, dan 979 tidak menyebut apakah Popup Detail masih terbuka setelah aksi selesai. Spec mengasumsikan popup tertutup dan tabel Paired terlihat (Expected "tabel dimuat ulang"), sehingga langkah berikutnya membuka popup lagi tanpa langkah penutup; QA perlu menegaskan.
  - TC-FA-TAG-977 langkah 6 menyebut slot `RFID TAG` untuk Replace tanpa menyebut langkah scan Tag lama atau Dialog Replace TAG; spec mengikuti teks TC.
  - Ketiga TC memakai Tag `RF-00412` sebagai pengganti; spec memulihkan stok di antara blok (langkah 13 dan 22).
  - Filter TAG Type RFID masih aktif di akhir spec; state ini hilang saat hook `beforeEach` suite membuka halaman TAG untuk spec berikutnya.
