---
id: TC-AC-ACTS-E2E-018-setup-column-stock-list-ceklis-dan-unceklis-kolom
title: "Setup Column Stock List: Ceklis dan Unceklis Dua Belas Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-59
coverage:
  web: automated
---

# Setup Column Stock List: Ceklis dan Unceklis Dua Belas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Kolom yang diuji (dipakai pengulangan langkah TC-AC-ACTS-59): `Photo`, `Device Name`, `SKU`, `TAG Type`, `Type`, `Brand`, `Model/Type`, `Total Registered`, `Available`, `In Use`, `Damaged/Missing`, `Last Updated`.
- Pemulihan Setup Column: langkah akhir mencentang kembali `Photo` dan `Device Name` lalu `[Save]`; hook `after` menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik header kolom Column Visibility (⋯)
2. Klik `[Setup Column]`
3. Untuk setiap baris tabel kolom pada Prerequisites lakukan langkah 4 sampai 7 (dua belas kolom)
4. Hilangkan centang kolom, amati preview
5. Verifikasi Preview langsung menyembunyikan kolom saat tidak dicentang
6. Centang kembali kolom tersebut
7. Verifikasi Preview menampilkan kolom lagi saat dicentang
8. Hilangkan centang kolom `Photo` dan `Device Name`, klik `[Save]`
9. Verifikasi Kolom `Photo` dan `Device Name` hilang dari tabel setelah Save
10. Muat ulang halaman (F5)
11. Verifikasi Kolom `Photo` dan `Device Name` tetap hilang setelah F5
12. Buka Setup Column, centang kembali `Photo` dan `Device Name`, klik `[Save]`
13. Verifikasi Kolom `Photo` dan `Device Name` tampil lagi setelah dicentang kembali dan Save

## Notes

- Ekspansi di atas 35 langkah (13 langkah nominal; dua belas kolom mengulang langkah 4 sampai 7 sehingga 57 langkah setelah ekspansi): satu objek uji (ceklis kolom Setup Column) dan satu dataset; langkah diulang per kolom diparameterkan di Prerequisites (8b.7).
- Langkah penghubung (S-03): tidak ada selain pemulihan kolom di akhir spec.
