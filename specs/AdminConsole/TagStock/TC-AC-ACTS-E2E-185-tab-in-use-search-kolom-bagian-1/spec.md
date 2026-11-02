---
id: TC-AC-ACTS-E2E-185-tab-in-use-search-kolom-bagian-1
title: "Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-440
  - TC-AC-ACTS-441
  - TC-AC-ACTS-442
coverage:
  web: automated
---

# Detail SKU Tab In Use: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Search" (Search hanya menyaring saat Enter):

| TC | Kolom | Keyword huruf kecil | Keyword huruf besar | Keyword tidak ada | Nilai yang dicari |
|---|---|---|---|---|---|
| 440 | TAG Code | tag-5d | TAG-5D | zzz-tidak-ada-tag | unit `TAG-5D8J2LM6` |
| 440 | Identifier | e280 | E280 | zzz-tidak-ada-ide | unit dengan EPC `E280...` |
| 440 | Identifier (UID, RFID) | a1b2 | A1B2 | zzz-tidak-ada-ide | unit dengan UID `A1B2...` |
| 441 | Client | maju | MAJU | zzz-tidak-ada-cli | unit milik `PT Maju Bersama` |
| 442 | Status | damaged | DAMAGED | zzz-tidak-ada-con | unit berkondisi Damaged/Missing |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-440, 441, 442: Search kelas id, teks, dan badge

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
- Langkah yang diulang per kolom: langkah 3 sampai 9 (iterasi dari tabel "Kolom uji Search" di Prerequisites, 5 iterasi; TAG Code, Identifier, dan Identifier (UID, RFID) milik TC-AC-ACTS-440, Client milik TC-AC-ACTS-441, Status milik TC-AC-ACTS-442); `Verifikasi` tetap satu per klausa (bagian 8b butir 7).
- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap iterasi mereset tabel.
- Temuan untuk QA: keyword tidak ada TC-AC-ACTS-442 (`zzz-tidak-ada-con`) dan TC-AC-ACTS-440 untuk Identifier dan Identifier (UID, RFID) (`zzz-tidak-ada-ide`) memakai potongan nama kolom lain; spec mengikuti TC.
