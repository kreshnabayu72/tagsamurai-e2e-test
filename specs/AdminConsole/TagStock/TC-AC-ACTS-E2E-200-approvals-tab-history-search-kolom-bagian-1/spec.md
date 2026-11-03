---
id: TC-AC-ACTS-E2E-200-approvals-tab-history-search-kolom-bagian-1
title: "Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-622
  - TC-AC-ACTS-623
  - TC-AC-ACTS-624
coverage:
  web: automated
---

# Approvals Tab History: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Search" (Search hanya menyaring saat Enter):

| TC | Kolom | Keyword huruf kecil | Keyword huruf besar | Keyword tidak ada | Nilai yang dicari |
|---|---|---|---|---|---|
| 622 | Type | collision | COLLISION | zzz-tidak-ada-typ | Subject Activation Collision |
| 622 | Approval | rejected | REJECTED | zzz-tidak-ada-app | Subject Rejected |
| 623 | Device Name (SKU) | beacon | BEACON | zzz-tidak-ada-dev | Subject SKU `BLE-BEACON-ALPHA-B1` |
| 623 | Category | ble - object | BLE - OBJECT | zzz-tidak-ada-cat | Subject kategori `BLE - Object TAG` |
| 624 | Matched Identifier | d4e5 | D4E5 | zzz-tidak-ada-mat | Subject dengan identifier `D4E5...` |
| 624 | Existing Record | tag-9n | TAG-9N | zzz-tidak-ada-exi | Subject dengan Existing Record `TAG-9N1Q6VX3` |
| 624 | TAG Code | tag-6r | TAG-6R | zzz-tidak-ada-tag | Subject dengan TAG Code baru `TAG-6R9V3ZL4` |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-622, 623, 624: Search kelas badge, teks, dan id

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
- Langkah yang diulang per kolom: langkah 3 sampai 9 (iterasi dari tabel "Kolom uji Search" di Prerequisites, 7 iterasi; Type dan Approval milik TC-AC-ACTS-622, Device Name (SKU) dan Category milik TC-AC-ACTS-623, Matched Identifier, Existing Record, dan TAG Code milik TC-AC-ACTS-624); `Verifikasi` tetap satu per klausa (bagian 8b butir 7).
- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap iterasi mereset tabel.
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Search Tab History), satu dataset, tanpa state tulis; ekspansi hanya dari 7 iterasi kolom, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Temuan untuk QA: keyword tidak ada TC-AC-ACTS-623 (`zzz-tidak-ada-dev`) dan TC-AC-ACTS-624 untuk Existing Record (`zzz-tidak-ada-exi`) memakai potongan nama kolom; spec mengikuti TC.
