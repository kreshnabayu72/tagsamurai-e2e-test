---
id: TC-AC-ACTS-E2E-016-filter-stock-list-kombinasi-and-dan-independen-dari-column-visibility
title: "Filter Stock List: Kombinasi AND dan Filter Independen dari Column Visibility"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-56
  - TC-AC-ACTS-790
coverage:
  web: automated
---

# Filter Stock List: Kombinasi AND dan Filter Independen dari Column Visibility

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Data Pre-setup SKU #22 (`skuPlain`: Device Name `Plain Tag`, Brand `Zenith`); kata `zenith` hanya ada di kolom Brand.
- Pemulihan Setup Column: TC-AC-ACTS-790 menyembunyikan kolom `Brand`; langkah penghubung menampilkannya kembali dan hook `after` menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-56: Kombinasi AND dua field Filter

1. Klik icon Filter
2. Pilih `RFID Asset Tag` pada `Device Name` dan `RFID-ASSET-CORE-R5` pada `SKU`, klik `[Apply]`
3. Verifikasi Hanya baris yang memenuhi kedua kriteria tampil (irisan)
4. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-790: Filter independen dari Column Visibility

5. Klik icon Filter, pilih `Zenith` pada `Brand`, klik `[Apply]`
6. Verifikasi Baris SKU `Fixture.tagStock.skuPlain` tampil
7. Klik header (⋯), lalu hilangkan centang kolom `Brand`
8. Verifikasi Filter `Brand` = `Zenith` tetap menyaring tabel (baris SKU `Fixture.tagStock.skuPlain` tetap tampil)
9. Klik icon Filter
10. Verifikasi Field `Brand` tetap ada di Filter Panel dengan nilai ter-Apply `Zenith`
11. Tutup Filter Panel, klik icon Search, ketik `zenith`, tekan Enter
12. Verifikasi Empty state `No results found` tampil (Search `zenith` tidak mencocokkan baris melalui kolom `Brand` yang disembunyikan)
13. Klik `(←)` pada kotak Search, klik header (⋯), lalu centang kembali kolom `Brand`
14. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` mengosongkan Filter; mengembalikan kolom `Brand` dan mengosongkan Search di akhir.
- Temuan untuk QA (S-15): TC-AC-ACTS-56 memilih field `SKU` di Filter Panel padahal TC-AC-ACTS-51 dan 853 menyatakan Filter Panel tidak memiliki field `SKU`; kontradiksi antar TC. Spec mengikuti TC-AC-ACTS-56 apa adanya dan langkah kedua akan gagal sampai TC diperbaiki. TC-AC-ACTS-790 butir c menggabungkan Search dengan Filter ter-Apply; spec mengosongkan hasil Filter Brand lewat Search yang berbasis kolom tersembunyi.
