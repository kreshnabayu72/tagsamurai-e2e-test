---
id: TC-FA-TAG-E2E-260-modal-event-log-sort-column-visibility-dan-pagination-bagian-1
title: "Modal Event Log To Be Returned: Sort Tiga Tahap Kolom Received At, TAG Code, Last Asset, dan Return Group (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1055
  - TC-FA-TAG-1056
  - TC-FA-TAG-1057
  - TC-FA-TAG-1058
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Sort Tiga Tahap Kolom Received At, TAG Code, Last Asset, dan Return Group (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup Event Log To Be Returned (kunci `Fixture.fixedAssetTag.eventLog3`; tanpa suffix `{runId}`; Event Log berisi tepat tiga entri ini; 'Disposal Center' berada di bawah group induk 'Operations'; 'Dedi K.' bernama lengkap Dedi Kurniawan):

| Received At | TAG Code | Last Asset | Return Group | Handed Over By | Received By | Method | Final Status |
|---|---|---|---|---|---|---|---|
| 27 Okt 2026 14:15 | RF-00093 (RFID) | Excavator 20 Ton - 5 | Disposal Center | Dedi K. | Budi S. | Assigned | Paired |
| 26 Okt 2026 10:02 | RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal Center | Dedi K. | Budi S. | Scan | Available |
| 26 Okt 2026 09:40 | NF-00092 (NFC) | Laptop Pro 14 - 8 | HQ Warehouse | Rina T. | Sari W. | Manual | Damaged/Missing |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend bila seeding mengubahnya.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`. Spec ini sendiri tidak menyimpan konfigurasi kolom.

## Test Steps

### TC-FA-TAG-1055: sort tiga tahap kolom Received At

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Klik ikon sort kolom "Received At" pada tabel modal (klik pertama)
4. Verifikasi klik pertama (Oldest First, panah naik): urutan NF-00092, RF-00071, RF-00093
5. Klik ikon sort kolom "Received At" pada tabel modal (klik kedua)
6. Verifikasi klik kedua (Newest First, panah turun): urutan RF-00093, RF-00071, NF-00092
7. Klik ikon sort kolom "Received At" pada tabel modal (klik ketiga)
8. Verifikasi klik ketiga: indikator netral dan urutan kembali ke bawaan Received At terbaru di atas (RF-00093, RF-00071, NF-00092)

### TC-FA-TAG-1056: sort tiga tahap kolom TAG Code

9. Klik ikon sort kolom "TAG Code" pada tabel modal (klik pertama)
10. Verifikasi klik pertama (A-Z, panah naik): urutan NF-00092, RF-00071, RF-00093
11. Klik ikon sort kolom "TAG Code" pada tabel modal (klik kedua)
12. Verifikasi klik kedua (Z-A, panah turun): urutan RF-00093, RF-00071, NF-00092
13. Klik ikon sort kolom "TAG Code" pada tabel modal (klik ketiga)
14. Verifikasi klik ketiga: indikator netral dan urutan kembali ke bawaan Received At terbaru di atas (RF-00093, RF-00071, NF-00092)

### TC-FA-TAG-1057: sort tiga tahap kolom Last Asset

15. Klik ikon sort kolom "Last Asset" pada tabel modal (klik pertama)
16. Verifikasi klik pertama (A-Z, panah naik): urutan RF-00071 (Excavator 20 Ton - 2), RF-00093 (Excavator 20 Ton - 5), NF-00092 (Laptop Pro 14 - 8)
17. Klik ikon sort kolom "Last Asset" pada tabel modal (klik kedua)
18. Verifikasi klik kedua (Z-A, panah turun): urutan NF-00092, RF-00093, RF-00071
19. Klik ikon sort kolom "Last Asset" pada tabel modal (klik ketiga)
20. Verifikasi klik ketiga: indikator netral dan urutan kembali ke bawaan Received At terbaru di atas (RF-00093, RF-00071, NF-00092)

### TC-FA-TAG-1058: sort tiga tahap kolom Return Group

21. Klik ikon sort kolom "Return Group" pada tabel modal (klik pertama)
22. Verifikasi klik pertama (A-Z, panah naik): baris Disposal Center (RF-00071, RF-00093) di atas baris HQ Warehouse (NF-00092)
23. Klik ikon sort kolom "Return Group" pada tabel modal (klik kedua)
24. Verifikasi klik kedua (Z-A, panah turun): baris HQ Warehouse (NF-00092) di atas baris Disposal Center
25. Klik ikon sort kolom "Return Group" pada tabel modal (klik ketiga)
26. Verifikasi klik ketiga: indikator netral dan urutan kembali ke bawaan Received At terbaru di atas (RF-00093, RF-00071, NF-00092)
27. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1055 s.d. 1058). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Kasus sort tiga tahap memakai satu `Verifikasi` per butir Expected TC (a, b, c); indikator panah dan urutan baris pada satu butir ditulis dalam satu `Verifikasi` karena TC menyebutnya dalam satu butir.
- Tiap kasus berakhir pada klik ketiga sehingga sort kembali ke netral; tidak ada langkah pemulihan sort.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 27 (menutup modal Event Log).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1058 butir a dan b menyebut urutan antar grup Return Group tanpa urutan baris di dalam grup; spec mengasersi hanya posisi grup.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
