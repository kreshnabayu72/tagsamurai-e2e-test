---
id: TC-AC-ACTS-E2E-204-approvals-tab-history-filter-bagian-2
title: "Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-634
  - TC-AC-ACTS-635
  - TC-AC-ACTS-636
coverage:
  web: automated
---

# Approvals Tab History: Filter Panel: Screening, Dropdown, Date Range, Opsi Distinct, dan Kombinasi AND (Bagian 2)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya. Spec ini membuka Approvals > TAG Stock lewat sidebar pada langkah 1.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data (disediakan fixture BE): Tab History memuat Subject Approved, Rejected, dan Canceled (sedikitnya 5 baris) dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; Subject berisi Type `Register Duplicate` dan `Activation Collision`, SKU `BLE-BEACON-ALPHA-B1` (Category `BLE - Object TAG`) dan `RFID-ASSET-CORE-R5` (Category `RFID - Object TAG`), Matched Identifier ber-UID `A1B2C3D4E5F6` (mengandung `D4E5`), Existing Record `TAG-9N1Q6VX3`, TAG Code baru `TAG-6R9V3ZL4`, Requested By `PT ABC Logistics (Client)` dan `PT Maju Bersama (Distributor)`, dan Approver `Andi Wijaya` (Data Dinamis #3). `N` = jumlah total baris Tab History, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Rentang tanggal diturunkan dari seeding (bagian 8b butir 10, S-11) untuk Requested At dan Resolved At: `D1` dan `D2` dua tanggal berbeda yang mencakup sebagian baris (`D1` lebih awal dari `D2`), `D3` satu tanggal yang dimiliki sebagian baris.
- Tabel "Field tanggal uji Filter":

| Field |
|---|
| Requested At |
| Resolved At |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar, klik Tab `History`

### TC-AC-ACTS-634: Filter date range

2. Klik icon Filter
3. Untuk setiap baris tabel "Field tanggal uji Filter" di Prerequisites, lakukan langkah 4 sampai 14
4. Verifikasi field `<field pada iterasi>` menampilkan placeholder `Select date` sebelum dipilih
5. Pilih rentang tanggal `D1` sampai `D2` pada field `<field pada iterasi>`
6. Klik `[Apply]`
7. Verifikasi tabel memuat sedikitnya satu baris data
8. Verifikasi hanya baris dengan nilai `<field pada iterasi>` dalam rentang inklusif (`D1` <= tanggal <= `D2`) yang tampil
9. Pilih rentang satu hari `D3` sampai `D3` pada field `<field pada iterasi>`
10. Klik `[Apply]`
11. Verifikasi tabel memuat sedikitnya satu baris data
12. Verifikasi hanya baris pada hari `D3` yang tampil
13. Klik `[Clear Field]`
14. Klik `[Apply]`

### TC-AC-ACTS-635: Isi opsi dropdown Filter = DISTINCT data tabel

15. Buka dropdown `Type`
16. Verifikasi opsi `Type` hanya berisi nilai yang ada di baris tabel saat ini
17. Verifikasi nilai yang tidak muncul di tabel tidak menjadi opsi

### TC-AC-ACTS-636: Kombinasi AND dua field Filter

18. Pilih `Register Duplicate` pada `Type`
19. Pilih `RFID-ASSET-CORE-R5` pada `SKU`
20. Klik `[Apply]`
21. Verifikasi tabel memuat sedikitnya satu baris data
22. Verifikasi hanya baris yang memenuhi kedua kriteria (`Register Duplicate` dan `RFID-ASSET-CORE-R5`) yang tampil
23. Klik `[Clear Field]`
24. Klik `[Apply]`
25. Klik icon Filter untuk menutup panel

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per field tanggal: langkah 4 sampai 14 (iterasi dari tabel "Field tanggal uji Filter" di Prerequisites, 2 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7). Pembanding "sedikitnya satu baris" mendahului tiap asersi "hanya baris ..." (bagian 8b butir 2).
- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` mengosongkan filter; menutup panel Filter di akhir.
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok satu kelas harness (Filter Panel Tab History), satu dataset, tanpa state tulis; ekspansi hanya dari 2 iterasi field tanggal.
- Temuan untuk QA: TC-AC-ACTS-634 langkah 4 "Pada setiap field tanggal ... pilih rentang ... klik [Apply]" tidak menyatakan apakah kedua field diisi bersamaan atau satu per satu; spec memeriksa satu field per iterasi. TC-AC-ACTS-634 tidak menyebut nilai tanggal; spec memakai `D1`, `D2`, `D3` dari seeding. TC-AC-ACTS-635 tidak menyebut nilai Type yang tidak muncul; spec mengasersi tanpa menyebut nilai.
