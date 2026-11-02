---
id: TC-AC-ACTS-E2E-170-detail-sku-tab-available-search-kolom-bagian-1
title: "Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-395
  - TC-AC-ACTS-396
  - TC-AC-ACTS-397
coverage:
  web: automated
---

# Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Search" (Search hanya menyaring saat Enter):

| TC | Kolom | Keyword huruf kecil | Keyword huruf besar | Keyword tidak ada | Nilai yang dicari |
|---|---|---|---|---|---|
| 395 | TAG Code | tag-4f | TAG-4F | zzz-tidak-ada-tag | unit `TAG-4F7K2XQ9` |
| 395 | Identifier | e280 | E280 | zzz-tidak-ada-ide | unit dengan EPC `E280...` |
| 395 | Identifier (UID, RFID) | a1b2 | A1B2 | zzz-tidak-ada-ide | unit dengan UID `A1B2...` |
| 396 | Status | available | AVAILABLE | zzz-tidak-ada-sta | unit berstatus Available |
| 397 | Registered By | budi | BUDI | zzz-tidak-ada-reg | unit yang didaftarkan Budi |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-395, 396, 397: Search kelas id, badge, dan user

2. Untuk setiap baris tabel "Kolom uji Search" di Prerequisites, lakukan langkah 3 sampai 9
3. Ketik Search `<keyword huruf kecil pada iterasi>`, tekan Enter
4. Verifikasi tabel memuat baris yang cocok dengan `<nilai yang dicari pada iterasi>` pada kolom `<kolom pada iterasi>`
5. Ganti isi kotak search dengan `<keyword huruf besar pada iterasi>`, tekan Enter
6. Verifikasi tabel memuat baris yang cocok dengan `<nilai yang dicari pada iterasi>` pada kolom `<kolom pada iterasi>`
7. Ganti isi kotak search dengan `<keyword tidak ada pada iterasi>`, tekan Enter
8. Verifikasi empty state `No results found`
9. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 3 sampai 9 (iterasi dari tabel "Kolom uji Search" di Prerequisites, 5 iterasi; kolom TAG Code, Identifier, dan Identifier (UID, RFID) milik TC-AC-ACTS-395, Status milik TC-AC-ACTS-396, Registered By milik TC-AC-ACTS-397); `Verifikasi` tetap satu per klausa (bagian 8b butir 7).
- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap iterasi mereset tabel dan mengosongkan keyword.
- Temuan untuk QA: keyword `zzz-tidak-ada-ide` dipakai untuk kolom Identifier dan Identifier (UID, RFID) (TC-AC-ACTS-395 langkah 8 dan 10); spec mengikuti TC.
