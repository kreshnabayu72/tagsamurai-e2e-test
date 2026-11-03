---
id: TC-FA-TAG-E2E-248-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-3
title: "Tabel To Be Returned: Indikator Titik Filter, Menutup Panel Tanpa Apply, dan Kombinasi Search dengan Filter (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1002
  - TC-FA-TAG-1003
  - TC-FA-TAG-1004
coverage:
  web: automated
---

# Tabel To Be Returned: Indikator Titik Filter, Menutup Panel Tanpa Apply, dan Kombinasi Search dengan Filter (Bagian 3)

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
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Filter dikosongkan di akhir tiap kasus.

## Test Steps

### TC-FA-TAG-1002: indikator titik pada ikon Filter

1. Klik tab `To Be Returned`
2. Klik ikon Filter
3. Pilih "NFC" pada "TAG Type"
4. Klik [Apply]
5. Klik ikon Filter untuk menutup panel Filter
6. Verifikasi ikon Filter menampilkan badge titik walau panel tertutup
7. Klik ikon Filter untuk membuka panel Filter
8. Klik [Clear Field]
9. Klik [Apply]
10. Verifikasi badge titik pada ikon Filter hilang
11. Verifikasi tabel menampilkan keempat Tag (RF-00071, RF-00088, NF-00092, RF-00110)

### TC-FA-TAG-1003: menutup panel tanpa Apply

12. Pilih "NFC" pada "TAG Type" tanpa klik [Apply]
13. Klik ikon Filter lagi untuk menutup panel
14. Klik ikon Filter untuk membuka kembali panel
15. Verifikasi tabel tetap menampilkan keempat Tag (RF-00071, RF-00088, NF-00092, RF-00110)
16. Verifikasi field "TAG Type" kembali kosong

### TC-FA-TAG-1004: Search dan Filter dikombinasikan

17. Klik field "Return Group"
18. Centang node "Disposal Center"
19. Klik [Select]
20. Klik [Apply]
21. Ketik Search `Excavator 20 Ton - 5`, tekan Enter
22. Verifikasi tabel menampilkan RF-00088 saja
23. Klik `(←)` pada kotak Search
24. Klik [Clear Field]
25. Klik [Apply]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1002 s.d. 1004). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-992 s.d. 1001 ada di spec 246 dan 247.
- TC-FA-TAG-1003 dimulai dari panel yang masih terbuka sesudah akhir TC-FA-TAG-1002.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 23 (mengosongkan Search lewat `(←)`); 24 (mengosongkan Filter lewat [Clear Field]); 25 (menerapkan Filter kosong lewat [Apply]).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1004 menulis "pilih Disposal Center pada Return Group" tanpa menyebut bahwa field itu berupa tree picker; spec memakai klik field, centang node, dan [Select] sesuai TC-FA-TAG-996.
  - TC-FA-TAG-1002 Expected butir a tidak menyebut bentuk badge titik selain "titik"; spec mengasersi keberadaan badge titik.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
