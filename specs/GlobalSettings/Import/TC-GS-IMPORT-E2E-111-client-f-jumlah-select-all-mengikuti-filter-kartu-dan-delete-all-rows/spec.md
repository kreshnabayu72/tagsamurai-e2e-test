---
id: TC-GS-IMPORT-E2E-111-client-f-jumlah-select-all-mengikuti-filter-kartu-dan-delete-all-rows
title: "Client F: jumlah Select All mengikuti filter kartu dan Delete All Rows menomori ulang Row # tanpa celah"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-691
  - TC-GS-IMPORT-696
coverage:
  web: automated
---

# Client F: jumlah Select All mengikuti filter kartu dan Delete All Rows menomori ulang Row # tanpa celah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client F (Hendra Wijaya) `totalControl_automated_qaTeam6@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTF_TC_PASSWORD` (nama env baru, didaftarkan pada tahap script). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client F.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis: D-10 (Draft Brand campuran 10 baris Client F dari `brand-mixed.csv`: 5 `pending`, 3 `error`, 2 `duplicate`), dibuat ulang lewat skrip fixture sebelum tiap TC: Row 1 `Nexus`, Row 2 `Orion`, Row 3 `Vertex`, Row 4 `Helios`, Row 5 `Samsung` (duplicate), Row 6 `Pioneer` (duplicate), Row 7 nama 121 karakter huruf `A` (error panjang), Row 8 `Rocket 🚀` (error), Row 9 `Star ⭐` (error), Row 10 `Pioneer`. Nama literal karena asersi bergantung pada urutan dan nama baris; Client F khusus draft campuran.
- Kemampuan teknis: skrip seed D-10 (disediakan tim FE/BE). Delete All Rows dikonfirmasi sungguhan karena environment automation terisolasi dan draft milik automation.
- State global: tidak ada yang diubah selain draft Client F dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): buang draft Brand Client F.

## Test Steps

### TC-GS-IMPORT-691: Jumlah Select All mengikuti filter kartu aktif

1. Seed draft D-10 di Client F lewat skrip fixture, lalu muat ulang halaman Import > Brand
2. Klik kartu Errors
3. Centang satu baris
4. Verifikasi tombol `[Select All (3 records)]` tampil
5. Klik `[Select All (3 records)]`
6. Verifikasi Bulk Action Bar menampilkan "3 Rows selected"
7. Klik kartu Total Rows
8. Verifikasi Bulk Action Bar tetap menampilkan "3 Rows selected"
9. Verifikasi tombol `[Select All (10 records)]` tampil
10. Klik `[Unselect All]`

### TC-GS-IMPORT-696: Delete All Rows menomori ulang Row # tanpa celah

11. Seed ulang draft D-10 di Client F lewat skrip fixture, lalu muat ulang halaman Import > Brand
12. Verifikasi Staging Metric Cards: Total Rows 10
13. Verifikasi kolom # menampilkan 1 sampai 10
14. Klik `[Delete All Rows]` pada baris pesan "Brand Name: Max. 120 characters" di Error Summary Callout
15. Verifikasi Total Rows 9, Ready to Import 5, Errors 2, dan Duplicates 2
16. Verifikasi kolom # menampilkan 1 sampai 9 tanpa celah
17. Verifikasi `Rocket 🚀` menjadi #7
18. Verifikasi `Star ⭐` menjadi #8
19. Verifikasi `Pioneer` (pending) menjadi #9

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-691 (tanpa menghapus) mendahului TC-696 yang menghapus baris (prinsip 5 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 11 menyiapkan D-10 (Kontrak Fixture R1); langkah 10 membersihkan seleksi.
- Pembagian TC lintas spec: TC-GS-IMPORT-458 (pembuatan D-10 lewat UI) ada di spec 187.
- Temuan untuk QA:
  - TC-GS-IMPORT-696 Expected a, b, c memuat banyak klausa dalam satu butir; dipecah per klausa (S-01). Expected c menyebut `Pioneer` (pending) menjadi #9 padahal Row 10 semula `Pioneer` berstatus `pending`; spec mengikuti TC.
  - Post Condition kedua TC kosong; tidak ada yang diasersi.
