---
id: TC-FA-TAG-E2E-244-tabel-to-be-returned-search-per-kolom-bagian-1
title: "Tabel To Be Returned: Search per Kolom, Pembukaan Input, dan Label Ikon Tipe (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-980
  - TC-FA-TAG-981
  - TC-FA-TAG-982
  - TC-FA-TAG-983
  - TC-FA-TAG-984
  - TC-FA-TAG-985
  - TC-FA-TAG-986
coverage:
  web: automated
---

# Tabel To Be Returned: Search per Kolom, Pembukaan Input, dan Label Ikon Tipe (Bagian 1)

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
- State global: tidak ada. Spec ini tidak mengubah data bisnis; Search dikosongkan pada tiap akhir kasus.

## Test Steps

### TC-FA-TAG-980: ikon Search membuka input

1. Klik tab `To Be Returned`
2. Klik ikon Search
3. Verifikasi input search muncul dengan placeholder "Search TAG code, asset name..."
4. Verifikasi kursor berada di input search

### TC-FA-TAG-981: Search kolom TAG Code

5. Ketik Search `RF-00088`, tekan Enter
6. Verifikasi tabel hanya menampilkan baris RF-00088
7. Klik `(←)` pada kotak Search

### TC-FA-TAG-982: Search kolom Last Asset

8. Ketik Search `Laptop`, tekan Enter
9. Verifikasi tabel hanya menampilkan baris NF-00092
10. Klik `(←)` pada kotak Search

### TC-FA-TAG-983: Search kolom Reason

11. Ketik Search `Disposal`, tekan Enter
12. Verifikasi tabel hanya menampilkan baris RF-00071, RF-00088, NF-00092, dan RF-00110
13. Klik `(←)` pada kotak Search

### TC-FA-TAG-984: Search kolom Return Group

14. Ketik Search `HQ`, tekan Enter
15. Verifikasi tabel hanya menampilkan baris NF-00092
16. Klik `(←)` pada kotak Search

### TC-FA-TAG-985: Search kolom Current Holder

17. Ketik Search `Rina`, tekan Enter
18. Verifikasi tabel hanya menampilkan baris NF-00092
19. Klik `(←)` pada kotak Search

### TC-FA-TAG-986: Search "RFID" lewat label aksesibilitas ikon tipe

20. Ketik Search `RFID`, tekan Enter
21. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110
22. Verifikasi NF-00092 tidak tampil
23. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-980 s.d. 986). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-987 s.d. 991 ada di spec 245 (Search tab To Be Returned, bagian 2).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 7, 10, 13, 16, 19, 23 (mengosongkan Search lewat `(←)` yang menutup input dan mereset tabel).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-981 s.d. 986 tidak menyebut cara mengosongkan Search antar kasus; spec menambah `(←)` sebagai langkah penghubung.
  - TC-FA-TAG-986 Expected tidak menyebut label aksesibilitas ikon tipe yang dicari; spec mengasersi hasil Search "RFID" apa adanya.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
