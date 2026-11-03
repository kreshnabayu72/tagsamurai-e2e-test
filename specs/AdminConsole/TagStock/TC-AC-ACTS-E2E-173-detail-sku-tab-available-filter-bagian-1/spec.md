---
id: TC-AC-ACTS-E2E-173-detail-sku-tab-available-filter-bagian-1
title: "Detail SKU Tab Available: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-403
  - TC-AC-ACTS-404
  - TC-AC-ACTS-405
coverage:
  web: automated
---

# Detail SKU Tab Available: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Rentang tanggal Registered At diturunkan dari seeding (bagian 8b butir 10, S-11): `D1` dan `D2` dua tanggal berbeda yang mencakup sebagian baris (`D1` lebih awal dari `D2`), `D3` satu tanggal yang dimiliki sebagian baris.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-403: Screening Filter Panel

2. Klik icon Filter
3. Verifikasi field berurutan sesuai kolom: Status [All statuses] | Registered At [Select date] | Registered By [All users]
4. Verifikasi dropdown bertipe multi-select searchable
5. Verifikasi field tanggal bertipe date range picker
6. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
7. Verifikasi icon Filter berubah gelap saat panel terbuka

### TC-AC-ACTS-404: Filter dropdown multi-select

8. Pilih opsi `Available` pada field `Status`
9. Klik `[Apply]`
10. Verifikasi tabel memuat sedikitnya satu baris data
11. Verifikasi hanya baris dengan nilai `Available` yang tampil
12. Klik `[Clear Field]`
13. Klik `[Apply]`
14. Verifikasi semua baris kembali tampil (N entri pada footer)
15. Pilih opsi `Budi S` pada field `Registered By`
16. Klik `[Apply]`
17. Verifikasi tabel memuat sedikitnya satu baris data
18. Verifikasi hanya baris dengan nilai `Budi S` yang tampil
19. Klik `[Clear Field]`
20. Klik `[Apply]`
21. Verifikasi semua baris kembali tampil (N entri pada footer)

### TC-AC-ACTS-405: Filter date range Registered At

22. Verifikasi field `Registered At` menampilkan placeholder `Select date` sebelum dipilih
23. Pilih rentang tanggal `D1` sampai `D2` pada field `Registered At`
24. Klik `[Apply]`
25. Verifikasi tabel memuat sedikitnya satu baris data
26. Verifikasi hanya baris dengan Registered At dalam rentang inklusif (`D1` <= tanggal <= `D2`) yang tampil
27. Pilih rentang satu hari `D3` sampai `D3` pada field `Registered At`
28. Klik `[Apply]`
29. Verifikasi tabel memuat sedikitnya satu baris data
30. Verifikasi hanya baris pada hari `D3` yang tampil
31. Klik `[Clear Field]`
32. Klik `[Apply]`
33. Klik icon Filter untuk menutup panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` di akhir mengosongkan filter sebelum panel ditutup; menutup panel Filter. Pembanding "sedikitnya satu baris" mendahului tiap asersi "hanya baris ..." (bagian 8b butir 2).
- Temuan untuk QA: TC-AC-ACTS-405 tidak menyebut nilai tanggal; spec memakai `D1`, `D2`, dan `D3` dari seeding. TC-AC-ACTS-404 mengulang `[Clear Field]` lalu `[Apply]` tanpa membuka kembali panel; spec mengikuti urutan TC.
