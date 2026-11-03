---
id: TC-AC-ACTS-E2E-015-filter-stock-list-dropdown-date-range-dan-opsi-distinct
title: "Filter Stock List: Dropdown Multi-Select, Date Range, dan Opsi Dropdown Distinct"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-52
  - TC-AC-ACTS-53
  - TC-AC-ACTS-55
coverage:
  web: automated
---

# Filter Stock List: Dropdown Multi-Select, Date Range, dan Opsi Dropdown Distinct

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 (akun Total Control) dan Stock List terisi minimal 5 SKU dari RFID, NFC, BLE, dan GPS dengan nilai beragam pada tiap kolom (#12 sampai #15 dan SKU pendukung).
- Data seed milik spec untuk TC-AC-ACTS-53 (SKU bersuffix `{runId}-015`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU D1 dengan Last Updated tanggal T1 dan SKU D2 dengan Last Updated tanggal T2 (T1 dan T2 berbeda, ditetapkan seeding), sehingga rentang T1 sampai T2 mencakup sebagian baris.
- Field dropdown yang diuji (dipakai pengulangan langkah TC-AC-ACTS-52):

| Field | Opsi |
|---|---|
| `Device Name` | `RFID Asset Tag` |
| `TAG Type` | `RFID` |
| `Type` | `Object TAG` |
| `Brand` | `Core` |
| `Model/Type` | `R5` |

- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-52: Filter dropdown multi-select

1. Untuk setiap baris tabel field dropdown pada Prerequisites lakukan langkah 2 sampai 5 (lima field)
2. Klik icon Filter, pilih opsi pada field, klik `[Apply]`
3. Verifikasi Sedikitnya satu baris tampil dan hanya baris dengan nilai opsi tersebut yang tampil
4. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
5. Verifikasi Semua baris kembali tampil setelah Clear Field dan Apply

### TC-AC-ACTS-53: Filter date range Last Updated

6. Klik icon Filter
7. Verifikasi Field Last Updated menampilkan placeholder `Select date` sebelum dipilih
8. Pilih rentang tanggal T1 sampai T2 pada field Last Updated, klik `[Apply]`
9. Verifikasi Baris SKU D1 dan SKU D2 tampil (dalam rentang inklusif startDate <= tanggal <= endDate)
10. Verifikasi Tabel tidak memuat baris di luar rentang
11. Klik icon Filter, pilih rentang satu hari (Start = End = T1), klik `[Apply]`
12. Verifikasi Baris SKU D1 tampil
13. Verifikasi Baris SKU D2 tidak tampil (pilihan satu hari menampilkan baris pada hari itu saja)
14. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-55: Opsi dropdown Filter = DISTINCT data tabel

15. Klik icon Filter, lalu buka dropdown `Device Name`
16. Bandingkan opsi dengan nilai kolom Device Name yang tampil di tabel
17. Verifikasi Opsi `Device Name` hanya berisi nilai yang ada di baris tabel saat ini
18. Verifikasi Nilai Device Name yang tidak dimiliki baris mana pun (mis. `Nama Tidak Terdaftar {runId}`) tidak menjadi opsi
19. Tutup dropdown dan Filter Panel

## Notes

- Langkah penghubung (S-03): `[Clear Field]` dan `[Apply]` mengosongkan Filter antar field dan sebelum TC berikutnya (S-09); menutup dropdown dan Filter Panel.
- Ekspansi lima field pada langkah 2 sampai 5 tidak melewati sekitar 35 langkah dari nominal (8b.7).
- Temuan untuk QA (S-15): TC-AC-ACTS-53 butir a menyebut placeholder `Select date` pada "setiap field tanggal (Last Updated)" sedangkan Stock List hanya punya satu field tanggal; spec mengasersi satu field. TC-AC-ACTS-55 butir b tidak menyebut nilai yang tidak boleh jadi opsi; spec memakai nama yang tidak didaftarkan di data.
