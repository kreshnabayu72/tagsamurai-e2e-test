---
id: TC-AC-ACTS-E2E-023-lintas-permukaan-search-literal-dan-spasi-tengah
title: "Lintas Enam Permukaan: Search Teks Literal (Payload Script dan Karakter Pola) dan Spasi di Tengah Query"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-76
  - TC-AC-ACTS-77
coverage:
  web: automated
---

# Lintas Enam Permukaan: Search Teks Literal (Payload Script dan Karakter Pola) dan Spasi di Tengah Query

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
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
- Kemampuan teknis: mendeteksi dialog `alert` browser (kemampuan standar kerangka). Seed memuat sedikitnya satu baris pada tiap permukaan yang memuat frasa `rfid asset` pada kolom yang dapat dicari, dan tidak ada baris yang memuat karakter `%`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-76: Search teks literal

1. Untuk setiap baris tabel «Permukaan yang diuji» lakukan langkah 2 sampai 11 (enam permukaan)
2. Buka permukaan sesuai kolom «Cara membuka» pada tabel Prerequisites
3. Ketik Search `<script>alert(1)</script>`, tekan Enter
4. Verifikasi Tidak ada script yang berjalan (tidak ada dialog `alert`)
5. Verifikasi Teks `<script>alert(1)</script>` tampil literal di input dan tidak dirender sebagai HTML
6. Ganti isi kotak search dengan `%`, tekan Enter
7. Verifikasi Empty state `No results found` tampil (karakter khusus dicocokkan sebagai teks biasa)

### TC-AC-ACTS-77: Spasi di tengah query menjadi substring

8. Ganti isi kotak search dengan `rfid asset`, tekan Enter
9. Verifikasi Baris yang memuat frasa `rfid asset` persis tampil
10. Ganti isi kotak search dengan `asset rfid`, tekan Enter
11. Verifikasi Empty state `No results found` tampil (query tidak dipecah per kata)

## Notes

- Satu TC memuat enam permukaan ("pada setiap permukaan") dan tetap satu TC satu spec, sehingga langkah diulang per permukaan lewat tabel parameter Prerequisites (8b.7); ekspansi enam kali melewati 35 langkah dan blok yang diulang adalah langkah 2 sampai 11. Perkiraan 61 langkah setelah ekspansi.
- P-5 butir b: TC-AC-ACTS-76 (payload script sebagai teks literal, kelas a ringan) adalah objek-uji ringan tunggal di spec Search ini; tidak ada harness eksternal dan tidak ada state berat.
- Langkah penghubung (S-03): membuka permukaan dari menu sidebar atau tab sesuai kolom «Cara membuka». Modal Event Log (permukaan 4) ditutup lewat kolom «Cara membuka» permukaan 5 sebelum pindah ke sidebar Approvals (S-09).
- Temuan untuk QA (S-15): TC tidak menyebut data uji per permukaan, jumlah baris minimum (lebih dari 10), maupun cara membuka modal Event Log (Tab Add Stock atau Tab Audit TAG); spec memakai tombol `[Event Log]` di Tab Available dan seeding disediakan tim FE. TC-AC-ACTS-76 butir b menulis "empty state `No results found` bila tidak ada"; spec mengasersi empty state karena seed tidak memuat `%`.
