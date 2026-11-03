---
id: TC-AC-ACTS-E2E-190-tab-in-use-sc-ceklis
title: "Detail SKU Tab In Use: Setup Column: Ceklis dan Unceklis Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-456
coverage:
  web: automated
---

# Detail SKU Tab In Use: Setup Column: Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Setup Column":

| Kolom |
|---|
| `TAG Code` |
| `Identifier` |
| `Identifier (UID, RFID)` |
| `Client` |
| `Status` |
| `Registered At` |
| `Registered By` |
| `Activated At` |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`

### TC-AC-ACTS-456: Setup Column ceklis dan unceklis kolom

4. Untuk setiap baris tabel "Kolom uji Setup Column" di Prerequisites, lakukan langkah 5 sampai 8
5. Hilangkan centang kolom `<kolom pada iterasi>`
6. Verifikasi preview langsung menyembunyikan kolom `<kolom pada iterasi>`
7. Centang kembali kolom `<kolom pada iterasi>`
8. Verifikasi preview menampilkan kembali kolom `<kolom pada iterasi>`
9. Hilangkan centang kolom `TAG Code` dan `Identifier`
10. Klik `[Save]`
11. Verifikasi kolom `TAG Code` dan `Identifier` hilang dari tabel
12. Muat ulang halaman (F5)
13. Verifikasi kolom `TAG Code` dan `Identifier` tetap hilang dari tabel
14. Klik header kolom Column Visibility (⋯)
15. Klik `[Setup Column]`
16. Centang kembali kolom `TAG Code` dan `Identifier`
17. Klik `[Save]`
18. Verifikasi kolom `TAG Code` dan `Identifier` tampil kembali di tabel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah yang diulang per kolom: langkah 5 sampai 8 (iterasi dari tabel "Kolom uji Setup Column" di Prerequisites, 8 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Expected a sampai h TC-AC-ACTS-456 (satu butir per kolom) dipecah per klausa (sembunyikan, tampilkan kembali).
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Setup Column Tab In Use), satu dataset; ekspansi dari 8 iterasi kolom, dan blok akhir (Save, F5, buka kembali) adalah bagian dari TC yang sama.
- Temuan untuk QA: TC-AC-ACTS-456 langkah 15 "Muat ulang halaman (F5)" tidak menyebut tab yang aktif sesudah muat ulang; spec membuka Setup Column sesuai langkah 16 TC dan mengasumsikan Tab In Use tetap aktif.
