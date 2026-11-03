---
id: TC-AC-ACTS-E2E-024-lintas-permukaan-pagination-halaman-tidak-valid-page-size-dan-sort
title: "Lintas Enam Permukaan: Pagination Nomor Halaman Tidak Valid, Ganti Page Size, dan Ganti Sort"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-78
  - TC-AC-ACTS-79
  - TC-AC-ACTS-80
coverage:
  web: automated
---

# Lintas Enam Permukaan: Pagination Nomor Halaman Tidak Valid, Ganti Page Size, dan Ganti Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Permukaan yang diuji (dipakai pengulangan langkah; satu TC mencakup enam permukaan):

| No | Permukaan | Cara membuka | Kata kunci Search | Kriteria Filter | Kolom sortable |
|---|---|---|---|---|---|
| 1 | Stock List | klik menu sidebar TAG > Stock | `core` | TAG Type = `RFID` | `Device Name` |
| 2 | Tab Available | Detail SKU `Fixture.tagStock.skuRfid` > Tab Available | nilai seed permukaan | nilai seed permukaan | kolom sortable pertama |
| 3 | Tab In Use | Detail SKU `Fixture.tagStock.skuRfid` > Tab In Use | nilai seed permukaan | nilai seed permukaan | kolom sortable pertama |
| 4 | Modal Event Log | Detail SKU `Fixture.tagStock.skuRfid` > Tab Available > `[Event Log]` | nilai seed permukaan | nilai seed permukaan | kolom sortable pertama |
| 5 | Approvals Tab Active | Tutup modal Event Log (permukaan 4), lalu Approvals > TAG Stock > Tab Active | nilai seed permukaan | nilai seed permukaan | kolom sortable pertama |
| 6 | Approvals Tab History | Approvals > TAG Stock > Tab History | nilai seed permukaan | nilai seed permukaan | kolom sortable pertama |

- Data seed milik spec (bersuffix `{runId}-NNN` sesuai nomor spec, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): pada tiap permukaan di atas, lebih dari 10 baris dengan nilai beragam pada kolom Search, Filter, dan Sort, termasuk sedikitnya satu baris yang memuat kata kunci permukaan itu. Nilai per permukaan selain Stock List disediakan tim FE karena TC hanya menulis "Data uji tiap permukaan cukup".
- Nomor halaman tidak valid yang diuji (dipakai pengulangan langkah TC-AC-ACTS-78): `0`, `-1`, `999` (melebihi halaman terakhir), `abc`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-78: Nomor halaman tidak valid diabaikan

1. Untuk setiap baris tabel «Permukaan yang diuji» lakukan langkah 2 sampai 15 (enam permukaan)
2. Buka permukaan sesuai kolom «Cara membuka» pada tabel Prerequisites
3. Pindah ke halaman 2
4. Untuk setiap nilai tidak valid pada Prerequisites lakukan langkah 5 sampai 6 (empat nilai)
5. Isi input halaman dengan nilai tidak valid, tekan Enter
6. Verifikasi Input diabaikan dan tabel tetap di halaman 2

### TC-AC-ACTS-79: Ganti page size kembali ke halaman 1

7. Pindah ke halaman 2
8. Ganti Rows per page ke 25
9. Verifikasi Tabel kembali ke halaman 1
10. Ganti Rows per page ke 10

### TC-AC-ACTS-80: Ganti sort tetap di halaman sekarang

11. Pindah ke halaman 2
12. Catat baris pertama halaman 2
13. Klik header salah satu kolom sortable
14. Verifikasi Nomor halaman tetap 2
15. Verifikasi Urutan dataset berubah (baris pertama halaman 2 berbeda dari yang dicatat)

## Notes

- Satu TC memuat enam permukaan ("pada setiap permukaan") dan tetap satu TC satu spec, sehingga langkah diulang per permukaan lewat tabel parameter Prerequisites (8b.7); ekspansi enam kali melewati 35 langkah dan blok yang diulang adalah langkah 2 sampai 15. Blok langkah 5 sampai 6 diulang empat kali di dalam tiap permukaan; perkiraan 121 langkah setelah ekspansi.
- Langkah penghubung (S-03): membuka permukaan dari menu sidebar atau tab sesuai kolom «Cara membuka»; mengembalikan Rows per page ke 10 sebelum TC berikutnya (S-09). Modal Event Log (permukaan 4) ditutup lewat kolom «Cara membuka» permukaan 5 sebelum pindah ke sidebar Approvals (S-09).
- Temuan untuk QA (S-15): TC tidak menyebut data uji per permukaan, jumlah baris minimum (lebih dari 10), maupun cara membuka modal Event Log (Tab Add Stock atau Tab Audit TAG); spec memakai tombol `[Event Log]` di Tab Available dan seeding disediakan tim FE. TC-AC-ACTS-80 butir "urutan dataset berubah" tidak menyebut kolom; spec mengasersi baris pertama halaman 2 berbeda dari yang dicatat.
