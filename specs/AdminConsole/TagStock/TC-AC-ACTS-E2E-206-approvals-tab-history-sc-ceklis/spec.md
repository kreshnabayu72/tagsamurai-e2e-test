---
id: TC-AC-ACTS-E2E-206-approvals-tab-history-sc-ceklis
title: "Approvals Tab History: Setup Column: Ceklis dan Unceklis Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-639
coverage:
  web: automated
---

# Approvals Tab History: Setup Column: Ceklis dan Unceklis Kolom

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Setup Column":

| Kolom |
|---|
| `Type` |
| `Device Name (SKU)` |
| `Category` |
| `Matched Identifier` |
| `Existing Record` |
| `Requested By` |
| `Approval` |
| `Approver` |
| `TAG Code` |
| `Requested At` |
| `Resolved At` |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`

### TC-AC-ACTS-639: Setup Column ceklis dan unceklis kolom

4. Untuk setiap baris tabel "Kolom uji Setup Column" di Prerequisites, lakukan langkah 5 sampai 8
5. Hilangkan centang kolom `<kolom pada iterasi>`
6. Verifikasi preview langsung menyembunyikan kolom `<kolom pada iterasi>`
7. Centang kembali kolom `<kolom pada iterasi>`
8. Verifikasi preview menampilkan kembali kolom `<kolom pada iterasi>`
9. Hilangkan centang kolom `Type` dan `Device Name (SKU)`
10. Klik `[Save]`
11. Verifikasi kolom `Type` dan `Device Name (SKU)` hilang dari tabel
12. Muat ulang halaman (F5)
13. Verifikasi kolom `Type` dan `Device Name (SKU)` tetap hilang dari tabel
14. Klik header kolom Column Visibility (⋯)
15. Klik `[Setup Column]`
16. Centang kembali kolom `Type` dan `Device Name (SKU)`
17. Klik `[Save]`
18. Verifikasi kolom `Type` dan `Device Name (SKU)` tampil kembali di tabel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah yang diulang per kolom: langkah 5 sampai 8 (iterasi dari tabel "Kolom uji Setup Column" di Prerequisites, 11 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Expected a sampai k TC-AC-ACTS-639 (satu butir per kolom) dipecah per klausa (sembunyikan, tampilkan kembali).
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Setup Column Tab History), satu dataset; ekspansi dari 11 iterasi kolom, dan blok akhir (Save, F5, buka kembali) adalah bagian dari TC yang sama.
- Temuan untuk QA: TC-AC-ACTS-639 langkah 17 "Muat ulang halaman (F5)" tidak menyebut tab yang aktif sesudah muat ulang; spec membuka Setup Column sesuai langkah 18 TC dan mengasumsikan Tab History tetap aktif.
