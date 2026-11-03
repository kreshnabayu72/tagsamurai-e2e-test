---
id: TC-AC-ACTS-E2E-184-tab-in-use-sort-bagian-2
title: "Detail SKU Tab In Use: Sort 3-State Per Kelas Kolom (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-437
  - TC-AC-ACTS-438
coverage:
  web: automated
---

# Detail SKU Tab In Use: Sort 3-State Per Kelas Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`
2. Verifikasi tabel memuat sedikitnya satu baris data

### TC-AC-ACTS-437: Sort 3-state kelas tanggal

3. Klik header kolom `Registered At` sekali
4. Verifikasi kolom `Registered At` Ascending (↑) (Oldest First)
5. Klik header kolom `Registered At` kedua kali
6. Verifikasi kolom `Registered At` Descending (↓) dengan urutan terbalik
7. Klik header kolom `Registered At` ketiga kali
8. Verifikasi indikator sort kolom `Registered At` hilang (netral) dan urutan kembali Activated At Newest First
9. Klik header kolom `Activated At` sekali
10. Verifikasi kolom `Activated At` Ascending (↑) (Oldest First)
11. Klik header kolom `Activated At` kedua kali
12. Verifikasi kolom `Activated At` Descending (↓) dengan urutan terbalik
13. Klik header kolom `Activated At` ketiga kali
14. Verifikasi indikator sort kolom `Activated At` hilang (netral) dan urutan kembali Activated At Newest First

### TC-AC-ACTS-438: Sort 3-state kelas user

15. Klik header kolom `Registered By` sekali
16. Verifikasi kolom `Registered By` Ascending (↑) (A-Z menurut nama lengkap user)
17. Klik header kolom `Registered By` kedua kali
18. Verifikasi kolom `Registered By` Descending (↓) dengan urutan terbalik
19. Klik header kolom `Registered By` ketiga kali
20. Verifikasi indikator sort kolom `Registered By` hilang (netral) dan urutan kembali Activated At Newest First

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembanding "sedikitnya satu baris" pada langkah 2 mendahului asersi urutan (bagian 8b butir 2). Data memuat sedikitnya dua nilai distinct pada tiap kolom (S-11).
