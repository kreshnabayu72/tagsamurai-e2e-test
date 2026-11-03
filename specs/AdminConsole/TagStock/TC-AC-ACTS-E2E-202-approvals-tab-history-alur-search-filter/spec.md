---
id: TC-AC-ACTS-E2E-202-approvals-tab-history-alur-search-filter
title: "Approvals Tab History: Alur Search lalu Filter dan Filter lalu Search"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-630
  - TC-AC-ACTS-631
coverage:
  web: automated
---

# Approvals Tab History: Alur Search lalu Filter dan Filter lalu Search

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-630: Alur Search lalu Filter

2. Ketik Search `approved`, tekan Enter
3. Klik icon Filter
4. Pilih `Register Duplicate` pada field `Type`
5. Klik `[Apply]`
6. Verifikasi tabel memuat sedikitnya satu baris data
7. Verifikasi seluruh baris yang tampil cocok dengan keyword `approved` dan bernilai Type `Register Duplicate` (irisan Search dan Filter)
8. Verifikasi kotak Search masih berisi `approved` (menerapkan Filter tidak mengosongkan keyword Search)
9. Klik `[Clear Field]`
10. Klik `[Apply]`
11. Klik icon Filter untuk menutup panel
12. Klik `(←)` pada kotak Search

### TC-AC-ACTS-631: Alur Filter lalu Search

13. Klik icon Filter
14. Pilih `Register Duplicate` pada field `Type`
15. Klik `[Apply]`
16. Klik icon Filter untuk menutup panel
17. Ketik Search `approved`, tekan Enter
18. Verifikasi tabel memuat sedikitnya satu baris data
19. Verifikasi hasil tabel identik dengan hasil pada langkah 7
20. Klik icon Filter
21. Verifikasi field `Type` masih berisi `Register Duplicate` (kriteria Filter tetap aktif setelah Search)
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik icon Filter untuk menutup panel
25. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): `[Clear Field]`, `[Apply]`, menutup panel Filter, dan klik `(←)` pada kotak Search mereset state antar TC (S-09). Hasil alur TC-AC-ACTS-631 dibandingkan dengan hasil TC-AC-ACTS-630 pada langkah 7.
- Temuan untuk QA: TC-AC-ACTS-631 butir b "Kriteria Filter tetap aktif setelah Search" tidak menyebut cara cek; spec membuka Filter Panel dan memeriksa field `Type`.
