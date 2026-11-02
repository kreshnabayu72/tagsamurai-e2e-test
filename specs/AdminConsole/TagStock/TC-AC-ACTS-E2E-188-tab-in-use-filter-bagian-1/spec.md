---
id: TC-AC-ACTS-E2E-188-tab-in-use-filter-bagian-1
title: "Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-449
  - TC-AC-ACTS-450
  - TC-AC-ACTS-451
coverage:
  web: automated
---

# Detail SKU Tab In Use: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, dicatat lewat kemampuan baca fixture BE pada langkah 2 sebelum aksi (bagian 8b butir 10), bukan diturunkan dari seeding atau dibaca dari satu halaman.
- Rentang tanggal diturunkan dari seeding (bagian 8b butir 10, S-11) untuk Registered At dan Activated At: `D1` dan `D2` dua tanggal berbeda yang mencakup sebagian baris (`D1` lebih awal dari `D2`), `D3` satu tanggal yang dimiliki sebagian baris.
- Tabel "Dropdown uji Filter":

| Field | Opsi |
|---|---|
| Client | PT Maju Bersama |
| Status | Available |
| Registered By | Budi S |

- Tabel "Field tanggal uji Filter":

| Field |
|---|
| Registered At |
| Activated At |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total baris Tab In Use SKU `RFID-ASSET-CORE-R5` sebagai baseline `N` (selain teks footer pagination), disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

2. Catat jumlah total baris Tab In Use SKU `RFID-ASSET-CORE-R5` sebagai `N` (kemampuan baca fixture BE)

### TC-AC-ACTS-449: Screening Filter Panel

3. Klik icon Filter
4. Verifikasi field berurutan sesuai kolom: Client [All clients] | Status [All statuses] | Registered At [Select date] | Registered By [All users] | Activated At [Select date]
5. Verifikasi dropdown bertipe multi-select searchable
6. Verifikasi field tanggal bertipe date range picker
7. Verifikasi tombol footer `[Clear Field]` (kiri) dan `[Apply]` (kanan)
8. Verifikasi icon Filter berubah gelap saat panel terbuka

### TC-AC-ACTS-450: Filter dropdown multi-select

9. Untuk setiap baris tabel "Dropdown uji Filter" di Prerequisites, lakukan langkah 10 sampai 16
10. Pilih opsi `<opsi pada iterasi>` pada field `<field pada iterasi>`
11. Klik `[Apply]`
12. Verifikasi tabel memuat sedikitnya satu baris data
13. Verifikasi hanya baris dengan nilai `<opsi pada iterasi>` yang tampil
14. Klik `[Clear Field]`
15. Klik `[Apply]`
16. Verifikasi semua baris kembali tampil (jumlah entri pada footer sama dengan `N` yang dicatat pada langkah 2)

### TC-AC-ACTS-451: Filter date range

17. Untuk setiap baris tabel "Field tanggal uji Filter" di Prerequisites, lakukan langkah 18 sampai 28
18. Verifikasi field `<field pada iterasi>` menampilkan placeholder `Select date` sebelum dipilih
19. Pilih rentang tanggal `D1` sampai `D2` pada field `<field pada iterasi>`
20. Klik `[Apply]`
21. Verifikasi tabel memuat sedikitnya satu baris data
22. Verifikasi hanya baris dengan nilai `<field pada iterasi>` dalam rentang inklusif (`D1` <= tanggal <= `D2`) yang tampil
23. Pilih rentang satu hari `D3` sampai `D3` pada field `<field pada iterasi>`
24. Klik `[Apply]`
25. Verifikasi tabel memuat sedikitnya satu baris data
26. Verifikasi hanya baris pada hari `D3` yang tampil
27. Klik `[Clear Field]`
28. Klik `[Apply]`
29. Klik icon Filter untuk menutup panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang: langkah 10 sampai 16 (tabel "Dropdown uji Filter", 3 iterasi) dan langkah 18 sampai 28 (tabel "Field tanggal uji Filter", 2 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Pembanding "sedikitnya satu baris" mendahului tiap asersi "hanya baris ..." (bagian 8b butir 2).
- Langkah penghubung (S-03, S-12): langkah 2 mencatat `N` sebelum aksi pada surface bersama; tidak ada `Verifikasi` karena hanya mencatat baseline.
- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` di tiap iterasi mengosongkan filter; menutup panel Filter di akhir.
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Filter Panel Tab In Use), satu dataset, tanpa state tulis; ekspansi hanya dari iterasi field.
- Temuan untuk QA: TC-AC-ACTS-451 langkah 6 "Pada setiap field tanggal ... pilih rentang ... klik [Apply]" tidak menyatakan apakah kedua field diisi bersamaan atau satu per satu; spec memeriksa satu field per iterasi. TC-AC-ACTS-451 tidak menyebut nilai tanggal; spec memakai `D1`, `D2`, `D3` dari seeding.
