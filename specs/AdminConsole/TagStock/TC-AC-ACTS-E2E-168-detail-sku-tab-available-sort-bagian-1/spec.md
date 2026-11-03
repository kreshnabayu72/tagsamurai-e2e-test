---
id: TC-AC-ACTS-E2E-168-detail-sku-tab-available-sort-bagian-1
title: "Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-390
  - TC-AC-ACTS-391
  - TC-AC-ACTS-392
coverage:
  web: automated
---

# Detail SKU Tab Available: Sort 3-State Per Kelas Kolom (Bagian 1)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Tabel "Kolom uji Sort kelas id":

| Kolom | Urutan Ascending |
|---|---|
| TAG Code | A-Z, kosong `—` di akhir |
| Identifier | A-Z, kosong `—` di akhir |
| Identifier (UID, RFID) | A-Z, kosong `—` di akhir |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-390: Sort 3-state kelas id

3. Untuk setiap baris tabel "Kolom uji Sort kelas id" di Prerequisites, lakukan langkah 4 sampai 9
4. Klik header kolom `<kolom pada iterasi>` sekali
5. Verifikasi kolom `<kolom pada iterasi>` Ascending (↑) sesuai kolom "Urutan Ascending" pada tabel
6. Klik header kolom `<kolom pada iterasi>` kedua kali
7. Verifikasi kolom `<kolom pada iterasi>` Descending (↓) dengan urutan terbalik
8. Klik header kolom `<kolom pada iterasi>` ketiga kali
9. Verifikasi indikator sort kolom `<kolom pada iterasi>` hilang (netral) dan urutan kembali Registered At Newest First

### TC-AC-ACTS-391: Sort 3-state kelas badge

10. Klik header kolom `Status` sekali
11. Verifikasi kolom `Status` Ascending (↑) (A-Z menurut label badge)
12. Klik header kolom `Status` kedua kali
13. Verifikasi kolom `Status` Descending (↓) dengan urutan terbalik
14. Klik header kolom `Status` ketiga kali
15. Verifikasi indikator sort kolom `Status` hilang (netral) dan urutan kembali Registered At Newest First

### TC-AC-ACTS-392: Sort 3-state kelas tanggal

16. Klik header kolom `Registered At` sekali
17. Verifikasi kolom `Registered At` Ascending (↑) (Oldest First)
18. Klik header kolom `Registered At` kedua kali
19. Verifikasi kolom `Registered At` Descending (↓) dengan urutan terbalik
20. Klik header kolom `Registered At` ketiga kali
21. Verifikasi indikator sort kolom `Registered At` hilang (netral) dan urutan kembali Registered At Newest First

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah yang diulang per kolom: langkah 4 sampai 9 (iterasi dari tabel "Kolom uji Sort kelas id" di Prerequisites, 3 iterasi); `Verifikasi` tetap satu per klausa (bagian 8b butir 7).
- Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi urutan (bagian 8b butir 2). Data memuat sedikitnya dua nilai distinct pada tiap kolom (S-11).
