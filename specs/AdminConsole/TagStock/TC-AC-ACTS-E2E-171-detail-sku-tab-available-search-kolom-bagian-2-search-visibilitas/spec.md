---
id: TC-AC-ACTS-E2E-171-detail-sku-tab-available-search-kolom-bagian-2-search-visibilitas
title: "Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-398
  - TC-AC-ACTS-399
  - TC-AC-ACTS-400
coverage:
  web: automated
---

# Detail SKU Tab Available: Search Per Kelas Kolom dan Kolom Tanpa Search (Bagian 2); Search Terikat Visibilitas Kolom

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data tambahan: salah satu unit memiliki Registered At `15 Jun 2026` (nilai yang tampil di tabel, TC-AC-ACTS-398).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Konfigurasi kolom Setup Column yang disimpan spec ini dihapus (preferensi kolom tabel di browser) di hook `before` dan `after`, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-398: Search tidak mencari kolom Registered At

3. Ketik Search `15 Jun 2026`, tekan Enter
4. Verifikasi empty state `No results found` (tabel tidak menemukan baris berdasarkan nilai kolom Registered At)
5. Klik `(←)` pada kotak Search
6. Klik icon Filter
7. Verifikasi field `Registered At` tersedia di Filter Panel (penyaringan kolom tersebut hanya lewat Filter Panel)
8. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-399: Search terikat visibilitas kolom, kolom `Status` di-hide

9. Klik header (⋯), hilangkan centang kolom `Status`
10. Verifikasi kolom `Status` tidak tampil
11. Ketik Search `damaged`, tekan Enter
12. Verifikasi keyword `damaged` tidak mencocokkan baris (tidak ada kolom lain yang memuat nilai itu): empty state `No results found`
13. Klik `(←)` pada kotak Search
14. Klik header (⋯), centang kembali kolom `Status`

### TC-AC-ACTS-400: Search terikat visibilitas kolom, kolom `Status` di-unhide kembali

15. Klik header (⋯), hilangkan lalu centang kembali kolom `Status`
16. Verifikasi kolom `Status` tampil kembali
17. Ketik Search `damaged`, tekan Enter
18. Verifikasi keyword `damaged` kembali mencocokkan baris unit Damaged/Missing melalui kolom `Status`
19. Klik `(←)` pada kotak Search

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Konfigurasi Setup Column yang disimpan spec ini dihapus lewat preferensi kolom di browser pada hook `before` dan `after`, bukan lewat `[Reset to Default]` (bagian 4 konvensi).
- Langkah penghubung (S-03): klik `(←)` pada kotak Search (reset tabel), menutup panel Filter. Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi absence. Klik header (⋯) untuk mencentang kembali kolom `Status` sesudah TC-AC-ACTS-399 (pemulihan state, S-09).
- Temuan untuk QA: (1) TC-AC-ACTS-399 dan 400 memakai keyword `damaged`; data harus memuat unit Damaged/Missing dan tidak ada kolom lain yang memuat nilai itu agar empty state pada TC-AC-ACTS-399 teramati. (2) TC-AC-ACTS-398 langkah 5 memakai contoh tanggal `15 Jun 2026`; data harus memuat tanggal itu.
