---
id: TC-AC-ACTS-E2E-004-navigasi-stock-list-detail-sku-dan-add-stock-per-tag-type
title: "Navigasi dari Stock List: Klik Device Name, Row Action Detail, Add Stock per TAG Type, dan Ctrl+Klik Tab Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-5
  - TC-AC-ACTS-6
  - TC-AC-ACTS-7
  - TC-AC-ACTS-8
  - TC-AC-ACTS-752
  - TC-AC-ACTS-753
coverage:
  web: automated
---

# Navigasi dari Stock List: Klik Device Name, Row Action Detail, Add Stock per TAG Type, dan Ctrl+Klik Tab Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1 dan SKU #12 sampai #15 (RFID, NFC, BLE, GPS).
- Spec read-only: tidak membuat, mengubah, atau menghapus data. Halaman Scan dan Import/Manual hanya dibuka dan ditutup tanpa memindai atau mengirim data; tidak ada reader yang dibutuhkan.
- Kemampuan teknis: Ctrl+klik membuka tab baru dan klik kanan membuka menu browser (disediakan tim FE sebagai kemampuan konteks browser).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-5: Klik Device Name membuka Detail SKU; klik area baris dan SKU tidak menavigasi

1. Klik area kosong sebuah baris
2. Verifikasi Klik area kosong tidak menavigasi
3. Klik teks SKU
4. Verifikasi Klik teks SKU tidak menavigasi; teks SKU bukan link
5. Hover teks Device Name
6. Verifikasi Teks Device Name tampil sebagai link (berubah warna saat hover)
7. Verifikasi Highlight baris tampil saat hover
8. Klik teks Device Name
9. Verifikasi Detail SKU dari SKU baris itu terbuka di tab yang sama
10. Klik breadcrumb `Stock` untuk kembali ke Stock List

### TC-AC-ACTS-752: Klik Device Name membuka Detail SKU

11. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
12. Klik header `Total Registered` sekali sampai Ascending
13. Klik teks Device Name pada baris SKU `Fixture.tagStock.skuRfid`
14. Verifikasi Navigasi ke Detail SKU `Fixture.tagStock.skuRfid` di tab yang sama dengan breadcrumb `TAG > Stock > Detail`
15. Klik breadcrumb `Stock` untuk kembali ke Stock List
16. Verifikasi Search tetap `Fixture.tagStock.skuRfid`
17. Verifikasi Sort Total Registered Ascending tetap aktif
18. Klik `(←)` pada kotak Search, lalu klik header `Total Registered` dua kali lagi sampai kembali netral

### TC-AC-ACTS-6: Row action Detail membuka Detail SKU dengan Tab Available aktif

19. Klik (⋯) pada baris SKU `Fixture.tagStock.skuRfid`
20. Klik `Detail`
21. Verifikasi Navigasi ke Detail SKU dengan breadcrumb `TAG > Stock > Detail`
22. Verifikasi Tab `Available` aktif secara default
23. Verifikasi Tujuan sama dengan klik Device Name (Detail SKU `Fixture.tagStock.skuRfid`)
24. Klik breadcrumb `Stock`

### TC-AC-ACTS-7: Row action Add Stock SKU RFID, NFC, BLE membuka halaman Scan

25. Klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuRfid`
26. Verifikasi Halaman Scan terbuka langsung tanpa modal pilih SKU
27. Verifikasi Header `Add Stock` (tanpa kode SKU); SKU info card baris 1 `RFID Asset Tag (RFID-ASSET-CORE-R5)` dan `TAG Type:` icon sesuai baris
28. Kembali ke Stock List, klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuNfc`
29. Verifikasi Header `Add Stock`; SKU info card baris 1 `NFC Access Card (NFC-CARD-BETA-N2)` dan `TAG Type:` icon NFC
30. Kembali ke Stock List, klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuBle`
31. Verifikasi Header `Add Stock`; SKU info card baris 1 `BLE Beacon Alpha (BLE-BEACON-ALPHA-B1)` dan `TAG Type:` icon BLE

### TC-AC-ACTS-8: Row action Add Stock SKU GPS membuka halaman Import/Manual

32. Kembali ke Stock List, klik (⋯) > `Add Stock` pada SKU `Fixture.tagStock.skuGps`
33. Verifikasi Halaman Import/Manual IMEI terbuka langsung dengan header `Add Stock` (tanpa kode SKU); SKU info card baris 1 `GPS Tracker Core (GPS-TRACK-CORE-G3)` dan `TAG Type:` icon GPS
34. Kembali ke Stock List

### TC-AC-ACTS-753: Device Name adalah link nyata

35. Ctrl+klik teks Device Name pada satu baris
36. Verifikasi Detail SKU terbuka di tab baru; tab Stock List tidak berubah
37. Klik kanan teks Device Name
38. Verifikasi Menu browser menawarkan salin tautan

## Notes

- Spec ini melewati sekitar 35 langkah (38 langkah); alasan: semua blok satu permukaan (Stock List) dan satu topik navigasi dengan data Pre-setup yang sama, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-752 dijalankan sebelum TC-AC-ACTS-6 (keduanya membuka Detail SKU `Fixture.tagStock.skuRfid`).
- Langkah penghubung (S-03): kembali ke Stock List lewat breadcrumb `Stock` atau Back browser setelah tiap navigasi; state Search dan Sort dibangun di awal TC-AC-ACTS-752 untuk mengasersi butir c (retensi) lalu dikosongkan sebelum TC berikutnya (S-09).
- Temuan untuk QA (S-15): TC-AC-ACTS-7 menyebut nama kartu info (`NFC Access Card`, `BLE Beacon Alpha`) hanya pada Expected; Data Uji Pre-setup #13 sampai #15 hanya memuat kode SKU, sehingga nilai diambil dari Expected TC. Retensi nomor halaman dan jumlah baris per halaman (TC-AC-ACTS-752 butir c) tidak dibangun di spec ini; retensi lengkap diuji di spec 008. Klik kanan pada TC-AC-ACTS-753 membuka menu bawaan browser yang berada di luar DOM; kemampuan membacanya disediakan tim FE.
