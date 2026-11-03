---
id: TC-AC-DN-E2E-108-filter-empty-dan-nilai-tidak-ada
title: "Filter Panel List: Empty State Kombinasi dan Nilai Filter yang Hilang dari Data"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-315
  - TC-AC-DN-309
  - TC-AC-DN-316
coverage:
  web: automated
---

# Filter Panel List: Empty State Kombinasi dan Nilai Filter yang Hilang dari Data

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal), password `Spectra.env.AC_DN_TC2_PASSWORD` (disediakan tim FE). Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web, lihat `suite.md`) hanya untuk memicu perubahan data (TC-AC-DN-316); tidak ada sesi UI kedua.
- Env var `AC_TC_PASSWORD` dan `AC_DN_TC2_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup: #13 Measurement `Unit`, `Meter`, `Box`; #15 Brand `Brand A`; #16 Device Name inti beserta SKU-nya (`Gate Antenna`, `NFC Tag`, `RFID Reader` ber-Brand A; `Tag Reel` ber-Measurement `Meter`); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified (`Cable Tester` 10/09/26 12:25, `NFC Tag` 08/09/26 15:40, `Gate Antenna` 05/09/26 13:15, `Tag Reel` 15/09/26 10:10, lainnya 01/09/26 06:00); #20 General Settings (Date Format `dd/MM/yy`). Seluruh data hanya dibaca kecuali `Tag Reel` pada TC-AC-DN-316.
- Pengecualian S-06 untuk TC-AC-DN-316: `Tag Reel` adalah satu-satunya Device Name ber-Measurement `Meter`, sehingga data tidak dapat dimiliki spec. Measurement `Tag Reel` diubah `Meter` menjadi `Box` oleh pelaku kedua lewat sesi API dan dipulihkan ke `Meter` oleh fixture backend yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan sebagai langkah penghubung sesudah TC-AC-DN-316, dan di hook `before` serta hook `after` spec ini. Efeknya: Last Modified `Tag Reel` berubah dari 15/09/26 10:10 dan dua entri Changelog Edit (`Meter` > `Box` dan `Box` > `Meter`) ditambahkan; pemulihan Last Modified ke 15/09/26 10:10 oleh fixture backend disediakan tim FE/BE.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: TC-AC-DN-315 menyembunyikan kolom `Brand` (preferensi kolom tabel List tersimpan di browser) dan memulihkannya pada langkah 6; hook `before` dan `after` menghapus preferensi kolom di browser (kemampuan `suite.md`). Selain itu tidak ada yang diubah selain pengecualian di atas. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-315: Menyembunyikan kolom Brand tidak menghilangkan field filter dan tidak membatalkan filter

1. Klik ikon Filter, klik field `Brand`, centang `Brand A`, lalu klik `[Apply]`
2. Klik header kolom Actions `⋯`, hapus centang `Brand`
3. Klik ikon Filter
4. Verifikasi tabel tetap menampilkan 3 baris: Gate Antenna, NFC Tag, RFID Reader
5. Verifikasi field `Brand` tetap ada di Filter Panel dengan chip `Brand A`
6. Klik header kolom Actions `⋯`, centang `Brand` kembali
7. Klik ikon Filter
8. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-309: Kombinasi filter tanpa hasil menampilkan empty state

9. Klik ikon Filter, klik field `Brand`, centang `Brand A`
10. Klik field `Last Modified`, pilih 10/09/26 sampai 15/09/26
11. Klik `[Apply]`
12. Verifikasi tabel menampilkan empty state Title "No results found" dan Description "Try adjusting your search or filter."
13. Verifikasi tidak ada pesan error
14. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-316: Nilai filter yang sudah tidak ada di data dibersihkan saat filter diterapkan ulang

15. Klik ikon Filter, klik field `Measurement`, centang `Meter` dan `Unit`
16. Klik `[Apply]`
17. Maya Putri (sesi API) mengubah Measurement `Tag Reel` dari `Meter` menjadi `Box` hingga perubahan tersimpan
18. Klik ikon Filter
19. Klik `[Apply]` tanpa mengubah kriteria
20. Verifikasi filter diterapkan ulang tanpa crash dan tabel tampil
21. Verifikasi tidak ada pesan error
22. Klik ikon Filter
23. Verifikasi chip `Unit` tampil pada field `Measurement`
24. Verifikasi nilai `Meter` yang tidak lagi ada di data dibersihkan dari kriteria (chip `Meter` tidak tampil)
25. Verifikasi tabel mengikuti kriteria yang tersisa (`Unit`): sedikitnya satu baris tampil dan seluruh baris ber-Measurement `Unit`
26. Verifikasi Tag Reel (kini Measurement `Box`) tidak tampil
27. Klik `[Clear Field]`, lalu klik `[Apply]`
28. Maya Putri (sesi API) memulihkan Measurement `Tag Reel` ke `Meter` lewat fixture backend hingga tersimpan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 6, 8, 14, dan 27 memulihkan kolom dan filter; langkah 7 membuka kembali Filter Panel karena klik header kolom Actions menutupnya; langkah 18 membuka kembali Filter Panel karena panel menutup setelah `[Apply]`; langkah 28 memulihkan Pre-setup `Tag Reel` (S-06, pengecualian 2026-10-30).
- Urutan: TC-AC-DN-309 dijalankan sebelum TC-AC-DN-316 (berbeda dari urutan TC-AC-DN-315, TC-AC-DN-316, TC-AC-DN-309 di indeks) supaya aksi yang mengubah data Pre-setup berada di akhir spec.
- Pelaku kedua lewat sesi API bukan konteks kedua (tidak memakai `P-2`).
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-316 bertanda Manual Only (dua sesi paralel) di kolom Automation; spec memakai sesi API untuk pelaku kedua sesuai keputusan harness dan tetap mengasersi hasilnya di sesi UI pertama.
  - TC-AC-DN-316 memakai `Tag Reel` Pre-setup yang dipakai spec lain sebagai data baca-saja; kemampuan fixture backend memulihkan Last Modified 15/09/26 10:10 tidak disebut TC dan disediakan tim FE/BE.
