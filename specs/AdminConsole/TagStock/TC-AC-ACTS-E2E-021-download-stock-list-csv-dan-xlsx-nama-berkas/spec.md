---
id: TC-AC-ACTS-E2E-021-download-stock-list-csv-dan-xlsx-nama-berkas
title: "Download Stock List: Nama Berkas CSV dan XLSX"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-71
  - TC-AC-ACTS-72
coverage:
  web: automated
---

# Download Stock List: Nama Berkas CSV dan XLSX

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Spec read-only: tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: pembaca nama berkas unduhan dan penangkap toast (kemampuan standar kerangka); pembaca isi berkas dibahas di spec lain.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-71: Download CSV, nama file dan extension

1. Klik icon Download
2. Pilih `Download as CSV`
3. Verifikasi Tidak muncul toast sukses
4. Verifikasi File terunduh bernama `TAG-Stock.csv`

### TC-AC-ACTS-72: Download XLSX, nama file dan extension

5. Klik icon Download
6. Pilih `Download as XLSX`
7. Verifikasi Tidak muncul toast sukses
8. Verifikasi File terunduh bernama `TAG-Stock.xlsx`

## Notes

- Isi sel berkas unduhan TC-AC-ACTS-73 (kelas f, binary buffer) ada di spec 037 (Download Stock List: Isi Sel XLSX).
- Temuan untuk QA (S-15): TC-AC-ACTS-71 dan 72 mengasersi absence toast sukses tanpa anchor positif lain selain berkas terunduh yang menyusul; absence toast diasersi segera setelah pemicu dan sebelum berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada Verifikasi berkas terunduh (8b butir 11).
