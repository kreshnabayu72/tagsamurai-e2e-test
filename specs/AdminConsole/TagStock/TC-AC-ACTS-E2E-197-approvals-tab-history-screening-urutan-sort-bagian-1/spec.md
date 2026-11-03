---
id: TC-AC-ACTS-E2E-197-approvals-tab-history-screening-urutan-sort-bagian-1
title: "Approvals Tab History: Screening Header, Kolom, Footer dan Urutan Default; Sort 3-State Per Kelas Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-615
  - TC-AC-ACTS-616
  - TC-AC-ACTS-617
coverage:
  web: automated
---

# Approvals Tab History: Screening Header, Kolom, Footer dan Urutan Default; Sort 3-State Per Kelas Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-615: Screening header, kolom, footer

2. Verifikasi Header Breadcrumb `Approvals > TAG Stock` (dua segmen statis) tidak bisa diklik
3. Verifikasi Header Tab `Active | History` dengan History terpilih
4. Verifikasi Header Table Tools: `Search | Filter | Download`
5. Verifikasi Body kolom berurutan: `Type (sortable) | Device Name (SKU) (sortable) | Category (sortable) | Matched Identifier (sortable) | Existing Record (sortable) | Requested By (sortable) | Approval (sortable) | Approver (sortable) | TAG Code (sortable) | Requested At (sortable) | Resolved At (sortable) | Column Visibility (⋯) (unsortable)`
6. Verifikasi Footer pagination default 10 data per halaman

### TC-AC-ACTS-616: Default sort Resolved At Newest First

7. Verifikasi tabel memuat sedikitnya satu baris data
8. Verifikasi baris terurut Resolved At Newest First saat halaman dibuka
9. Verifikasi tidak ada panah sort aktif pada kolom lain

### TC-AC-ACTS-617: Sort 3-state kelas badge

10. Klik header kolom `Type` sekali
11. Verifikasi kolom `Type` Ascending (↑) (A-Z menurut label badge)
12. Klik header kolom `Type` kedua kali
13. Verifikasi kolom `Type` Descending (↓) dengan urutan terbalik
14. Klik header kolom `Type` ketiga kali
15. Verifikasi indikator sort kolom `Type` hilang (netral) dan urutan kembali Resolved At Newest First
16. Klik header kolom `Approval` sekali
17. Verifikasi kolom `Approval` Ascending (↑) (A-Z menurut label badge)
18. Klik header kolom `Approval` kedua kali
19. Verifikasi kolom `Approval` Descending (↓) dengan urutan terbalik
20. Klik header kolom `Approval` ketiga kali
21. Verifikasi indikator sort kolom `Approval` hilang (netral) dan urutan kembali Resolved At Newest First

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AC-ACTS-615 dan TC-AC-ACTS-616 memiliki langkah pembuka yang sama dan diamati pada satu pembukaan Tab History (langkah 1); tidak ada navigasi ulang (S-10).
- Temuan untuk QA: butir Expected b TC-AC-ACTS-615 menyisipkan keterangan "(sortable)" dan "(unsortable)" pada nama kolom; spec mengasersinya sebagai bagian daftar kolom, bukan uji sort (uji sort ada di spec ini bagian TC-AC-ACTS-617 dan spec 198 sampai 199). TC-AC-ACTS-615 menyebut "Tab `Active | History`" tanpa menyebut apakah tab History memuat hitungan.
