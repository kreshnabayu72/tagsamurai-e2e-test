---
id: TC-AC-ACTS-E2E-003-metrik-stock-list-sku-tanpa-unit-total-registered-dan-available
title: "Metrik Stock List: SKU Tanpa Unit, Total Registered, Available, Damaged/Missing, Add Stock pada SKU Kosong, dan Sort Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-2
  - TC-AC-ACTS-3
  - TC-AC-ACTS-9
  - TC-AC-ACTS-10
  - TC-AC-ACTS-11
  - TC-AC-ACTS-12
  - TC-AC-ACTS-13
  - TC-AC-ACTS-888
coverage:
  web: automated
---

# Metrik Stock List: SKU Tanpa Unit, Total Registered, Available, Damaged/Missing, Add Stock pada SKU Kosong, dan Sort Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup #1, #16 (`skuEmpty`, SKU tanpa unit) dan #23 (`skuGpsNew`, SKU GPS baru tanpa unit).
- Data seed milik spec (nama bersuffix `{runId}-003`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU A (10 Available, 2 Waiting for Approval); SKU B (10 Available, 1 Rejected); SKU C (5 Available, 3 Damaged/Missing, 4 In Use, 2 Waiting for Approval, 1 Rejected; juga dipakai TC-AC-ACTS-12); SKU D (3 Damaged/Missing); SKU E (tanpa Damaged/Missing, 1 Available); satu SKU dengan aktivitas (Last Updated terisi) untuk TC-AC-ACTS-2.
- Hitungan unit pada Expected TC adalah hitungan seed spec ini; tidak ada angka absolut dari data bersama (S-12).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-2: Sort Last Updated, SKU tanpa aktivitas selalu di akhir

1. Pindah ke halaman terakhir Stock List
2. Verifikasi Baris SKU `Fixture.tagStock.skuEmpty` (Last Updated `—`) berada di kelompok baris paling akhir dan tidak ada baris bertanggal di bawahnya (Newest First)
3. Klik header `Last Updated` sampai Ascending (Oldest First)
4. Pindah ke halaman terakhir Stock List
5. Verifikasi Baris SKU `Fixture.tagStock.skuEmpty` (Last Updated `—`) tetap berada di kelompok baris paling akhir (Oldest First)
6. Klik header `Last Updated` dua kali lagi sampai kembali ke urutan netral (Last Updated Newest First)

### TC-AC-ACTS-3: SKU baru tanpa unit tetap tampil dengan metrik 0

7. Ketik Search `Fixture.tagStock.skuGpsNew`, tekan Enter
8. Verifikasi Baris SKU `Fixture.tagStock.skuGpsNew` tampil dengan Total Registered `0`, Damaged/Missing `0`, In Use `0`, Last Updated `—`

### TC-AC-ACTS-9: Add Stock tersedia pada SKU tanpa unit

9. Ganti isi kotak search dengan `Fixture.tagStock.skuEmpty`, tekan Enter
10. Klik (⋯) pada baris SKU tanpa unit
11. Verifikasi Menu row action memuat `Add Stock` dan `Detail`
12. Tekan Esc untuk menutup menu row action

### TC-AC-ACTS-10: Total Registered tidak menghitung Waiting for Approval

13. Ganti isi kotak search dengan nama SKU A, tekan Enter
14. Verifikasi Total Registered baris SKU A `10`

### TC-AC-ACTS-11: Total Registered tidak menghitung Rejected

15. Ganti isi kotak search dengan nama SKU B, tekan Enter
16. Verifikasi Total Registered baris SKU B `10`

### TC-AC-ACTS-12: Total Registered menghitung Available, In Use, dan Damaged/Missing

17. Ganti isi kotak search dengan nama SKU C, tekan Enter
18. Verifikasi Total Registered baris SKU C `12`
19. Verifikasi Available baris SKU C `5`
20. Verifikasi In Use baris SKU C `4`
21. Verifikasi Damaged/Missing baris SKU C `3`

### TC-AC-ACTS-888: Available hanya menghitung unit berstatus Available

22. Verifikasi Available baris SKU C `5`
23. Verifikasi Total Registered baris SKU C `12` = Available + In Use + Damaged/Missing
24. Verifikasi Unit Waiting for Approval dan Rejected tidak dihitung di kolom mana pun pada baris SKU C

### TC-AC-ACTS-13: Damaged/Missing lebih dari 0 tampil bold danger

25. Ganti isi kotak search dengan nama SKU D, tekan Enter
26. Verifikasi Angka Damaged/Missing `3` baris SKU D tampil bold dengan severity danger
27. Ganti isi kotak search dengan nama SKU E, tekan Enter
28. Verifikasi Angka Damaged/Missing `0` baris SKU E tampil normal

## Notes

- TC-AC-ACTS-888 memakai SKU C dan pembacaan yang sama dengan TC-AC-ACTS-12; Expected TC-AC-ACTS-888 butir a dan b diasersi ulang di bawah heading TC-nya agar tiap TC punya Verifikasi sendiri.
- Langkah penghubung (S-03): Search nama SKU seed untuk menemukan baris target (R-16); Esc menutup menu row action; dua klik header `Last Updated` terakhir pada TC-AC-ACTS-2 mengembalikan urutan netral.
- Temuan untuk QA (S-15): TC-AC-ACTS-2 menyebut "SKU tanpa aktivitas selalu di akhir" tanpa menyebut urutan antar SKU `—`; spec hanya mengasersi bahwa kelompok `—` ada di akhir. Cara menghasilkan unit Waiting for Approval dan Rejected tidak dijelaskan TC; dibuat lewat fixture BE (disediakan tim FE/BE).
