---
id: TC-AC-ACTS-E2E-207-approvals-tab-history-sc-urutan-pin
title: "Approvals Tab History: Setup Column: Geser Urutan serta Pin dan Unpin"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-640
  - TC-AC-ACTS-641
coverage:
  web: automated
---

# Approvals Tab History: Setup Column: Geser Urutan serta Pin dan Unpin

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`
2. Klik header kolom Column Visibility (⋯)
3. Klik `[Setup Column]`

### TC-AC-ACTS-640: Setup Column geser urutan kolom

4. Geser kolom `Type` ke bawah kolom `Device Name (SKU)`
5. Verifikasi Live Preview mengikuti urutan baru
6. Klik `[Save]`
7. Verifikasi tabel mengikuti urutan baru
8. Muat ulang halaman (F5)
9. Verifikasi urutan baru bertahan setelah F5

### TC-AC-ACTS-641: Setup Column pin dan unpin kolom

10. Klik header kolom Column Visibility (⋯)
11. Klik `[Setup Column]`
12. Klik icon Pin kolom `Type`
13. Klik `[Save]`
14. Scroll tabel secara horizontal
15. Verifikasi kolom ter-pin tetap diam di sisi kiri saat scroll horizontal
16. Klik header kolom Column Visibility (⋯)
17. Klik `[Setup Column]`
18. Klik icon Pin kolom `Type` lagi (unpin)
19. Klik `[Save]`
20. Scroll tabel secara horizontal
21. Verifikasi kolom `Type` ikut bergeser lagi setelah unpin

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): scroll horizontal kedua sebelum `Verifikasi` unpin membawa tabel ke keadaan yang diasersi (S-14).
- Temuan untuk QA: TC-AC-ACTS-641 tidak menyebut lebar viewport yang membuat tabel dapat di-scroll horizontal; langkah 8 TC tidak memuat scroll sesudah unpin padahal Expected b memerlukannya.
