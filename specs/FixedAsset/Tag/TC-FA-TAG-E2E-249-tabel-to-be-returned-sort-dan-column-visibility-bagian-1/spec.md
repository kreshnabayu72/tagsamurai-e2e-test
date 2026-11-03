---
id: TC-FA-TAG-E2E-249-tabel-to-be-returned-sort-dan-column-visibility-bagian-1
title: "Tabel To Be Returned: Sort Tiga Tahap Kolom TAG Code, Last Asset, Since, Return Group, dan Current Holder (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1005
  - TC-FA-TAG-1006
  - TC-FA-TAG-1007
  - TC-FA-TAG-1008
  - TC-FA-TAG-1009
coverage:
  web: automated
---

# Tabel To Be Returned: Sort Tiga Tahap Kolom TAG Code, Last Asset, Since, Return Group, dan Current Holder (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr4`; tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah; tabel To Be Returned dalam scope akun berisi tepat empat Tag ini; Return Group 'Disposal Center' berada di bawah group induk 'Operations'):

| TAG Code | Last Asset | Reason | Return Group | Current Holder | Since |
|---|---|---|---|---|---|
| RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. | 01 Sep 2026 |
| RF-00088 (RFID) | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. | 20 Sep 2026 |
| NF-00092 (NFC) | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. | 22 Sep 2026 |
| RF-00110 (RFID) | Excavator 20 Ton - 10 | Disposal | Disposal Center | Dedi K. | 10 Sep 2026 |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Sort dikembalikan ke netral pada akhir tiap kasus.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`. Spec ini sendiri tidak menyimpan konfigurasi kolom.

## Test Steps

### TC-FA-TAG-1005: sort tiga tahap kolom TAG Code

1. Klik tab `To Be Returned`
2. Klik ikon sort kolom "TAG Code" (klik pertama)
3. Verifikasi klik pertama (A-Z, panah naik): urutan NF-00092, RF-00071, RF-00088, RF-00110
4. Klik ikon sort kolom "TAG Code" (klik kedua)
5. Verifikasi klik kedua (Z-A, panah turun): urutan RF-00110, RF-00088, RF-00071, NF-00092
6. Klik ikon sort kolom "TAG Code" (klik ketiga)
7. Verifikasi klik ketiga: indikator sort kolom "TAG Code" netral dan urutan kembali ke urutan bawaan Since terlama di atas (RF-00071, RF-00110, RF-00088, NF-00092)

### TC-FA-TAG-1006: sort tiga tahap kolom Last Asset

8. Klik ikon sort kolom "Last Asset" (klik pertama)
9. Verifikasi klik pertama (A-Z, panah naik): urutan Excavator 20 Ton - 2 (RF-00071), Excavator 20 Ton - 5 (RF-00088), Excavator 20 Ton - 10 (RF-00110), Laptop Pro 14 - 8 (NF-00092)
10. Klik ikon sort kolom "Last Asset" (klik kedua)
11. Verifikasi klik kedua (Z-A, panah turun): urutan Laptop Pro 14 - 8 (NF-00092), Excavator 20 Ton - 10 (RF-00110), Excavator 20 Ton - 5 (RF-00088), Excavator 20 Ton - 2 (RF-00071)
12. Klik ikon sort kolom "Last Asset" (klik ketiga)
13. Verifikasi klik ketiga: indikator sort kolom "Last Asset" netral dan urutan kembali ke urutan bawaan Since terlama di atas (RF-00071, RF-00110, RF-00088, NF-00092)

### TC-FA-TAG-1007: sort tiga tahap kolom Since

14. Klik ikon sort kolom "Since" (klik pertama)
15. Verifikasi klik pertama (Oldest First, panah naik): urutan RF-00071, RF-00110, RF-00088, NF-00092
16. Klik ikon sort kolom "Since" (klik kedua)
17. Verifikasi klik kedua (Newest First, panah turun): urutan NF-00092, RF-00088, RF-00110, RF-00071
18. Klik ikon sort kolom "Since" (klik ketiga)
19. Verifikasi klik ketiga: indikator sort kolom "Since" netral dan urutan kembali ke urutan bawaan Since terlama di atas (RF-00071, RF-00110, RF-00088, NF-00092)

### TC-FA-TAG-1008: sort kolom Return Group menurut abjad A-Z

20. Klik ikon sort kolom "Return Group" (klik pertama)
21. Verifikasi klik pertama: baris Return Group "Disposal Center" (RF-00071, RF-00088, RF-00110) berada di atas baris "HQ Warehouse" (NF-00092)
22. Klik ikon sort kolom "Return Group" (klik kedua)
23. Verifikasi klik kedua: baris "HQ Warehouse" berada di atas baris "Disposal Center"
24. Klik ikon sort kolom "Return Group" sekali lagi hingga indikator netral

### TC-FA-TAG-1009: sort kolom Current Holder menurut nama lengkap A-Z

25. Klik ikon sort kolom "Current Holder" (klik pertama)
26. Verifikasi klik pertama: baris "Dedi K." (3 baris) berada di atas baris "Rina T."
27. Klik ikon sort kolom "Current Holder" (klik kedua)
28. Verifikasi klik kedua: baris "Rina T." berada di atas baris "Dedi K."
29. Klik ikon sort kolom "Current Holder" sekali lagi hingga indikator netral

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1005 s.d. 1009). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1010 s.d. 1013 ada di spec 250, TC-FA-TAG-1014 dan 1015 ada di spec 269, dan TC-FA-TAG-1016 dan 1017 ada di spec 251.
- Kasus sort tiga tahap memakai satu `Verifikasi` per butir Expected TC (a, b, c); indikator panah dan urutan baris pada satu butir ditulis dalam satu `Verifikasi` karena TC menyebutnya dalam satu butir.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 24 (mengembalikan sort kolom Return Group ke netral); 29 (mengembalikan sort kolom Current Holder ke netral).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1008 dan 1009 hanya menyebut dua klik dan tidak menyebut klik ketiga; spec menambah satu langkah penghubung yang mengembalikan sort ke netral sebelum kasus berikutnya.
  - TC-FA-TAG-1005 s.d. 1007 butir c menulis "urutan bawaan Since terlama di atas" tanpa menyebut kode Tag-nya; spec menurunkan urutan RF-00071, RF-00110, RF-00088, NF-00092 dari tanggal Since pada Pre-setup TC.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
