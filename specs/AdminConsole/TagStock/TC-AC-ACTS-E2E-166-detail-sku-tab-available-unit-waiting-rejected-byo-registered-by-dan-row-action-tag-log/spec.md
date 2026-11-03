---
id: TC-AC-ACTS-E2E-166-detail-sku-tab-available-unit-waiting-rejected-byo-registered-by-dan-row-action-tag-log
title: "Detail SKU Tab Available: Unit Waiting, Rejected, dan BYO Tidak Tampil, Registered By Terisi, dan Row Action TAG Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-378
  - TC-AC-ACTS-382
  - TC-AC-ACTS-383
  - TC-AC-ACTS-384
  - TC-AC-ACTS-385
  - TC-AC-ACTS-814
coverage:
  web: automated
---

# Detail SKU Tab Available: Unit Waiting, Rejected, dan BYO Tidak Tampil, Registered By Terisi, dan Row Action TAG Log

## Prerequisites

- Mode: FE+BE. Data dan hasil tampilan berasal dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Nilai identitas data dirujuk lewat `Fixture.tagStock.<kunci>` (berkas `fixtures/tag-stock.json` belum ada; ditandai, disediakan tim FE): `Fixture.tagStock.skuRfid` = `RFID-ASSET-CORE-R5`.
- Data Pre-setup (dibaca saja): SKU `RFID-ASSET-CORE-R5` (Pre-setup #12) memiliki sedikitnya 5 unit berstatus Available dan Damaged/Missing dengan sedikitnya dua nilai distinct pada tiap kolom yang diuji; memuat unit Available `TAG-4F7K2XQ9` (Data Dinamis #5, U1), unit ber-Identifier EPC `E280...` dan UID `A1B2...` (Data Dinamis #1), dan unit yang didaftarkan `Budi Santoso` (Data Dinamis #3). `N` = jumlah total baris Tab Available, ditetapkan seeding (bagian 8b butir 10), bukan dibaca dari satu halaman.
- Data tambahan (disediakan fixture BE): Subject Register Duplicate pending untuk SKU `RFID-ASSET-CORE-R5` (unit Waiting for Approval), Subject Rejected (Data Dinamis #4, UID `A1B2C3D4E5F7`), Subject Activation Collision ber-SKU `RFID-ASSET-CORE-R5` dari Client `PT ABC Logistics`, dan Subject Activation Collision dari Client BYO tanpa SKU; unit hasil Add Stock Principal dan Distributor ada.

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

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`; pastikan Tab `Available` aktif

### TC-AC-ACTS-382: Registered By terisi dan filter tanpa opsi `—`

2. Verifikasi tabel memuat sedikitnya satu baris data
3. Verifikasi seluruh sel Registered By terisi nama berformat `[First Name] [Last Initial]`
4. Klik icon Filter, buka dropdown `Registered By`
5. Verifikasi opsi dropdown `Registered By` hanya nama user
6. Verifikasi dropdown `Registered By` tidak memuat opsi `—`
7. Klik icon Filter untuk menutup panel

### TC-AC-ACTS-383, 378, 814: Unit Rejected dan unit Waiting for Approval tidak tampil di Tab Available

8. Verifikasi tidak ada baris dengan UID `A1B2C3D4E5F7` pada kolom `Identifier (UID, RFID)` (unit Rejected tidak ada di tabel)
9. Verifikasi tidak ada baris dengan TAG Code `—` (unit Waiting for Approval hasil Register Duplicate tidak ada di tabel)
10. Verifikasi tidak ada baris dengan TAG Code `—` (unit Waiting for Approval hasil Activation Collision ber-SKU tidak ada di tabel)

### TC-AC-ACTS-385: Row action TAG Log

11. Klik (⋯) pada baris berstatus Available
12. Verifikasi menu baris memuat `TAG Log` dan `Delete`
13. Verifikasi menu baris tidak memuat `Detail` maupun `Review`
14. Klik `TAG Log`
15. Verifikasi Popup TAG Log unit tersebut terbuka
16. Tutup Popup TAG Log

### TC-AC-ACTS-384: Unit BYO tanpa SKU berstatus Waiting tidak tampil di Tab Available manapun

17. Untuk setiap baris tabel "SKU yang diperiksa" di Prerequisites, lakukan langkah 18 sampai 20
18. Klik menu sidebar TAG > Stock, klik row action `Detail` pada SKU `<SKU pada iterasi>`; pastikan Tab `Available` aktif
19. Verifikasi Summary bar `Total Registered | Available | In Use` SKU `<SKU pada iterasi>` tampil
20. Verifikasi Tab Available SKU `<SKU pada iterasi>` tidak memuat unit BYO tanpa SKU berstatus Waiting (tidak ada baris dengan TAG Code `—`)

### Approvals > TAG Stock > Tab Active (TC-AC-ACTS-378, 814, 384)

21. Klik menu sidebar Approvals > TAG Stock, klik Tab `Active`
22. Verifikasi Tab Active memuat Subject Register Duplicate untuk SKU `RFID-ASSET-CORE-R5`
23. Verifikasi Tab Active memuat Subject Activation Collision ber-SKU `RFID-ASSET-CORE-R5`
24. Verifikasi Tab Active memuat Subject Activation Collision BYO tanpa SKU (satu-satunya tempat melihat unit itu adalah Approvals > TAG Stock)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Expected tiap TC dikelompokkan per permukaan (Tab Available lebih dulu, Approvals > TAG Stock > Tab Active sesudahnya) agar tidak berpindah halaman berulang (S-10): butir a TC-AC-ACTS-378 dan 814 ada di subjudul TC-AC-ACTS-383, 378, 814, butir b TC-AC-ACTS-378 dan 814 serta butir b TC-AC-ACTS-384 ada di subjudul Approvals > TAG Stock > Tab Active. TC-AC-ACTS-384 mengulang langkah 18 sampai 20 untuk 5 SKU (bagian 8b butir 7).
- Langkah penghubung (S-03): menutup panel Filter, menutup Popup TAG Log. `Verifikasi` Summary bar pada langkah iterasi adalah anchor absence (bagian 8b butir 2), bukan Expected TC.
- Alasan melewati sekitar 35 langkah: jumlah langkah nominal di bawah ambang; ekspansi 5 iterasi TC-AC-ACTS-384 menaikkannya, dan seluruh blok memeriksa satu hal (unit yang tidak boleh muncul di Tab Available) pada satu kelas harness dengan data yang sama.
- Temuan untuk QA: TC-AC-ACTS-384 menyebut "semua SKU" tanpa daftar; spec memakai SKU Pre-setup #12 sampai #16. TC-AC-ACTS-383 dan 814 tidak menyebut identifier unit; Rejected diacu lewat UID Data Dinamis #4 dan unit Waiting lewat TAG Code `—`. TC-AC-ACTS-814 tidak menyebut SKU Client sebagai Device Name unit; spec memakai SKU `RFID-ASSET-CORE-R5`.
