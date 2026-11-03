---
id: TC-AC-ACTS-E2E-181-tab-in-use-screening-read-only-badge-status-registered-by-dan-unit-tanpa-sku
title: "Tab In Use: Screening Read-Only Tanpa Toolbar Tulis, Row Action TAG Log, Badge Status, Status Kosong, Registered By BYO, dan Unit Tanpa SKU"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-426
  - TC-AC-ACTS-427
  - TC-AC-ACTS-428
  - TC-AC-ACTS-429
  - TC-AC-ACTS-430
  - TC-AC-ACTS-431
  - TC-AC-ACTS-432
coverage:
  web: automated
---

# Tab In Use: Screening Read-Only Tanpa Toolbar Tulis, Row Action TAG Log, Badge Status, Status Kosong, Registered By BYO, dan Unit Tanpa SKU

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki unit In Use milik beberapa Client (sedikitnya 5 unit) dengan Status Available dan Damaged/Missing dan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit `TAG-5D8J2LM6` milik `PT Maju Bersama`, unit ber-Identifier EPC `E280...` dan UID `A1B2...`, dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab In Use, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data tambahan (disediakan fixture BE): unit In Use dengan Status Available dan Damaged/Missing; unit In Use yang belum menerima event Condition (Status `—`); unit BYO Jalur B dengan SKU (Registered By `—`); unit In Use hasil BYO tanpa SKU (TAG Code `Fixture.tagStock.byoNoSkuTagCode`) yang terlihat hanya di registri Global Settings > TAG.
- Tabel "SKU yang diperiksa" (Pre-setup #12 sampai #16):

| SKU |
|---|
| `RFID-ASSET-CORE-R5` |
| `NFC-CARD-BETA-N2` |
| `BLE-BEACON-ALPHA-B1` |
| `GPS-TRACK-CORE-G3` |
| `RFID-SEAL-DELTA-R1` |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan di spec): fixture BE untuk seeding dan pemulihan data Pre-setup dan Dinamis yang disebut di bawah.
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`, klik Tab `In Use`

### TC-AC-ACTS-426 dan 427: Screening read-only dan row action TAG Log

2. Verifikasi tabel memuat sedikitnya satu baris data
3. Verifikasi Toolbar hanya memuat `Search`, `Filter`, `Download`
4. Verifikasi Toolbar tanpa `[Event Log]`, `[Audit TAG]`, dan `[Add Stock]`
5. Hover baris tabel
6. Klik (⋯) pada kolom body baris tersebut
7. Verifikasi menu row action hanya memuat `TAG Log`
8. Verifikasi menu row action tidak memuat `Delete` maupun `Review`
9. Tekan Esc untuk menutup menu

### TC-AC-ACTS-428: Badge Status satu nilai gabungan

10. Verifikasi badge Status `Available` bergaya success
11. Verifikasi badge Status `Damaged/Missing` bergaya danger

### TC-AC-ACTS-429: Status `—` sebelum sinkron pertama dan filter Status

12. Verifikasi Status unit In Use yang belum menerima event Condition tampil `—` (bukan Available)
13. Klik icon Filter
14. Buka dropdown `Status`
15. Verifikasi dropdown `Status` hanya menawarkan `Available` dan `Damaged/Missing`
16. Pilih `Available` pada field `Status`
17. Klik `[Apply]`
18. Verifikasi tabel memuat sedikitnya satu baris data
19. Verifikasi baris dengan Status `—` tidak tampil saat filter Status dipakai
20. Klik `[Clear Field]`
21. Klik `[Apply]`
22. Verifikasi baris dengan Status `—` tampil saat filter Status tidak dipakai
23. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-430 dan 431: Registered By BYO dan Registered At

24. Verifikasi Registered By unit BYO Jalur B dengan SKU tampil `—`
25. Verifikasi kolom Registered At tampil di samping kolom Activated At

### TC-AC-ACTS-432: Unit In Use tanpa SKU tidak tampil di Tab In Use manapun

26. Untuk setiap baris tabel "SKU yang diperiksa" di Prerequisites, lakukan langkah 27 sampai 30
27. Klik menu sidebar TAG > Stock, klik row action `Detail` pada SKU `<SKU pada iterasi>`, klik Tab `In Use`
28. Verifikasi Summary bar SKU `<SKU pada iterasi>` tampil
29. Verifikasi Tab In Use SKU `<SKU pada iterasi>` tidak memuat unit BYO tanpa SKU (TAG Code `Fixture.tagStock.byoNoSkuTagCode`)
30. Verifikasi metrik In Use dan Total Registered pada Summary bar SKU `<SKU pada iterasi>` tidak menghitung unit BYO tanpa SKU
31. Klik menu sidebar Global Settings > TAG
32. Verifikasi unit BYO tanpa SKU terlihat di registri Global Settings > TAG

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- TC-AC-ACTS-426 butir b dan TC-AC-ACTS-427 memiliki Expected padanan (row action hanya `TAG Log`); keduanya diamati pada satu pembukaan menu baris.
- Langkah penghubung (S-03): menutup menu baris, `[Clear Field]` dan `[Apply]`, menutup panel Filter.
- TC-AC-ACTS-432 mengulang langkah 27 sampai 30 untuk 5 SKU (bagian 8b butir 7). Asersi absence pada langkah iterasi didahului Summary bar SKU yang sama sebagai anchor (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah bila dihitung dengan ekspansi: seluruh blok membaca satu permukaan (Tab In Use) tanpa mengubah data pada satu kelas harness; ekspansi hanya dari iterasi SKU TC-AC-ACTS-432.
- Temuan untuk QA: TC-AC-ACTS-432 menyebut "semua SKU" tanpa daftar; spec memakai SKU Pre-setup #12 sampai #16. TC-AC-ACTS-432 tidak menyebut identifier unit BYO tanpa SKU; spec memakai kunci fixture BE. TC-AC-ACTS-429 tidak menyebut langkah membuat unit belum sinkron; disediakan fixture BE. TC-AC-ACTS-431 Expected tidak menyebut urutan kolom selain "di samping".
