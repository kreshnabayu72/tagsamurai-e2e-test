---
id: TC-AC-ACTS-E2E-002-isi-sel-stock-list-tanpa-kuota-icon-tag-type-badge-dan-device-name-panjang
title: "Isi Sel Stock List: Tanpa Kuota Allocated, Icon TAG Type, Badge Brand dan Model Terpotong, Device Name Panjang, dan Header Tidak Wrap"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-14
  - TC-AC-ACTS-20
  - TC-AC-ACTS-21
  - TC-AC-ACTS-22
  - TC-AC-ACTS-23
  - TC-AC-ACTS-854
coverage:
  web: automated
---

# Isi Sel Stock List: Tanpa Kuota Allocated, Icon TAG Type, Badge Brand dan Model Terpotong, Device Name Panjang, dan Header Tidak Wrap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1, #12 sampai #15 (SKU RFID, NFC, BLE, GPS untuk TC-AC-ACTS-854).
- Data seed milik spec (nama bersuffix `{runId}-002`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): (a) SKU Unit dengan 3 unit Available; (b) SKU Brand23 dengan Brand `Zebra Technologies Intl` (23 karakter) dan Model/Type `Handheld Reader Pro Model` (25 karakter); (c) SKU Brand35 dengan Brand `Jakarta Selatan Distribution Center` (35 karakter); (d) SKU Nama80 dengan Device Name 80 karakter termasuk suffix.
- Brand bernilai persis `Zebra Technologies Intl` (23 karakter) dan `Jakarta Selatan Distribution Center` (35 karakter) tidak dapat diberi suffix tanpa mengubah nilai dan panjangnya (A-7); Brand memakai nama literal dari Data Uji TC, di-seed idempotent (dilewati bila sudah ada) dan tidak dihapus spec (S-12). SKU yang memakainya tetap bersuffix.
- Kemampuan teknis: mengatur ukuran viewport browser (disediakan tim FE); viewport dipulihkan di langkah penghubung dan hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-14: Tidak ada kuota Allocated; Available = hitungan unit

1. Amati header kolom Stock List
2. Verifikasi Kolom hanya Photo, Device Name, SKU, TAG Type, Type, Brand, Model/Type, Total Registered, Available, In Use, Damaged/Missing, Last Updated
3. Klik icon Filter
4. Verifikasi Filter Panel memuat field Device Name
5. Verifikasi Tidak ada kolom maupun field filter `Allocated`
6. Klik icon Filter untuk menutup Filter Panel
7. Ketik Search SKU Unit, tekan Enter
8. Catat nilai kolom Available baris SKU Unit
9. Klik teks Device Name baris SKU Unit untuk membuka Detail SKU, lalu hitung baris berstatus Available di Tab Available
10. Verifikasi Nilai kolom `Available` sama dengan jumlah unit berstatus Available di Tab Available (bukan sisa kuota Stock Ledger)
11. Klik breadcrumb `Stock` untuk kembali ke Stock List

### TC-AC-ACTS-20: Badge sampai 25 karakter tampil penuh

12. Ganti isi kotak search dengan SKU Brand23, tekan Enter
13. Verifikasi Nama Brand `Zebra Technologies Intl` dan Model/Type `Handheld Reader Pro Model` tampil penuh tanpa `..`
14. Verifikasi Badge Brand dan Model/Type berwarna Dark (severity dark)

### TC-AC-ACTS-21: Badge lebih dari 25 karakter terpotong

15. Ganti isi kotak search dengan SKU Brand35, tekan Enter
16. Verifikasi Badge Brand menampilkan 12 huruf pertama `Jakarta Sela` + `..` + 12 huruf terakhir `ution Center`
17. Hover badge Brand
18. Verifikasi Hover menampilkan nama penuh `Jakarta Selatan Distribution Center`

### TC-AC-ACTS-22: Device Name 80 karakter

19. Ganti isi kotak search dengan SKU Nama80, tekan Enter
20. Hover teks Device Name baris SKU Nama80
21. Verifikasi Device Name 80 karakter tampil utuh (wrap natural), tidak dipotong `..`, tanpa tooltip

### TC-AC-ACTS-23: Header kolom tidak wrap

22. Klik `(←)` pada kotak Search untuk mengosongkan pencarian
23. Persempit viewport sampai label header hampir melebihi lebar kolom
24. Amati header kolom `Damaged/Missing` dan `Total Registered`
25. Verifikasi Header `Damaged/Missing` dan `Total Registered` tetap satu baris
26. Pulihkan viewport ke ukuran semula

### TC-AC-ACTS-854: Kolom TAG Type sebagai icon dengan accessibility label

27. Amati kolom `TAG Type`
28. Verifikasi Kolom `TAG Type` berisi icon per jenis tanpa teks badge
29. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter, lalu hover icon TAG Type baris SKU itu
30. Verifikasi Hover menampilkan accessibility label `RFID`
31. Ganti isi kotak search dengan `Fixture.tagStock.skuNfc`, tekan Enter, lalu hover icon TAG Type baris SKU itu
32. Verifikasi Hover menampilkan accessibility label `NFC`
33. Ganti isi kotak search dengan `Fixture.tagStock.skuBle`, tekan Enter, lalu hover icon TAG Type baris SKU itu
34. Verifikasi Hover menampilkan accessibility label `BLE`
35. Ganti isi kotak search dengan `Fixture.tagStock.skuGps`, tekan Enter, lalu hover icon TAG Type baris SKU itu
36. Verifikasi Hover menampilkan accessibility label `GPS`
37. Ganti isi kotak search dengan `gps`, tekan Enter
38. Verifikasi Search `gps` menemukan baris SKU bertipe GPS
39. Klik `(←)` pada kotak Search
40. Klik icon Filter, lalu buka dropdown `TAG Type`
41. Verifikasi Opsi dropdown `TAG Type` berlabel `RFID`, `NFC`, `BLE`, `GPS`
42. Tutup dropdown dan Filter Panel

## Notes

- Sekitar 35 langkah (di atas smell, 42 langkah): semua blok satu kelas harness (pembacaan sel Stock List), memakai dataset seed yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): Search SKU seed dan SKU Pre-setup (`Fixture.tagStock.*`) dipakai untuk menemukan baris target sebelum hover (R-16); menutup Filter Panel dan dropdown; memulihkan viewport.
- Temuan untuk QA (S-15): TC-AC-ACTS-23 menulis "bila kepanjangan terpotong dengan tooltip" (kondisional) tanpa menyebut lebar yang memicu; spec hanya mengasersi header tetap satu baris dan tidak mengasersi tooltip. TC-AC-ACTS-14 butir c membandingkan Available dengan jumlah baris Tab Available; spec memakai SKU seed 3 unit agar jumlah dapat dihitung dari satu halaman. Brand bernilai persis 23 dan 35 karakter bertentangan dengan S-12 (tidak bersuffix); ditangani lewat seeding idempotent di Prerequisites (A-7).
