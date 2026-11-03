---
id: TC-AC-DN-E2E-047-create-berhasil-variasi-category-measurement
title: "Create Device Name Berhasil: Variasi Category dan Measurement"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-79
  - TC-AC-DN-80
  - TC-AC-DN-81
coverage:
  web: automated
---

# Create Device Name Berhasil: Variasi Category dan Measurement

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`, `Meter`, `Box`; #14 Pohon Uji Kategori (`Hardware` > `Smart Fixed Reader` > `Antenna`; `Hardware` > `Handheld Reader` > `UHF Handheld`; `TAG` > `NFC` > `Tag`); #20 General Settings entitas uji (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).
- Data Dinamis (dibuat lewat form Create): `Wireless Gateway {runId}-047` (`Unit`, `Antenna`), `Rugged Handheld {runId}-047` (`Box`, `UHF Handheld`), dan `Tag Roll Mini {runId}-047` (`Meter`, `Tag`). Hook `after` menghapus ketiga record lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- Kemampuan teknis untuk Last Modified (TC-AC-DN-79): jam server dan jam browser sinkron; waktu dicatat sesudah [Submit] dan dibandingkan dengan toleransi satu menit (S-12).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-79: Create berhasil dengan Measurement Unit dan Category Antenna

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `Wireless Gateway {runId}-047` pada field Device Name
3. Klik field Measurement lalu pilih `Unit`
4. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
5. Klik `[Submit]`
6. Catat waktu sesudah `[Submit]` sebagai waktu aksi
7. Verifikasi toast sukses: "Success, device name has been created."
8. Verifikasi popup form tertutup
9. Ketik Search `Wireless Gateway {runId}-047`, tekan Enter
10. Verifikasi List memuat baris `Wireless Gateway {runId}-047` dengan Category badge `Antenna`
11. Verifikasi baris `Wireless Gateway {runId}-047` menampilkan Brand `—`
12. Verifikasi baris `Wireless Gateway {runId}-047` menampilkan Model/Type `—`
13. Verifikasi baris `Wireless Gateway {runId}-047` menampilkan Measurement `Unit`
14. Verifikasi kolom Last Modified baris `Wireless Gateway {runId}-047` menampilkan waktu pembuatan sesuai waktu aksi langkah 6 (toleransi satu menit) dalam format General Settings Pre-setup #20

### TC-AC-DN-80: Create berhasil dengan Category leaf tiga level UHF Handheld dan Measurement Box

15. Klik tombol `+ Device Name` pada toolbar
16. Ketik `Rugged Handheld {runId}-047` pada field Device Name
17. Klik field Measurement lalu pilih `Box`
18. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih leaf `UHF Handheld`
19. Klik `[Submit]`
20. Verifikasi toast sukses: "Success, device name has been created."
21. Ganti isi kotak search dengan `Rugged Handheld {runId}-047`, tekan Enter
22. Verifikasi List memuat baris `Rugged Handheld {runId}-047` dengan Category badge `UHF Handheld`
23. Verifikasi baris `Rugged Handheld {runId}-047` menampilkan Measurement `Box`

### TC-AC-DN-81: Create berhasil dengan Category leaf Tag dan Measurement Meter

24. Klik tombol `+ Device Name` pada toolbar
25. Ketik `Tag Roll Mini {runId}-047` pada field Device Name
26. Klik field Measurement lalu pilih `Meter`
27. Klik field Category, expand `TAG` lalu `NFC`, pilih leaf `Tag`
28. Klik `[Submit]`
29. Verifikasi toast sukses: "Success, device name has been created."
30. Ganti isi kotak search dengan `Tag Roll Mini {runId}-047`, tekan Enter
31. Verifikasi List memuat baris `Tag Roll Mini {runId}-047` dengan Category badge `Tag`
32. Verifikasi baris `Tag Roll Mini {runId}-047` menampilkan Measurement `Meter`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Ketiga TC bertanda FE Test "Need API".
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 6 (mencatat waktu aksi untuk asersi Last Modified, S-12), langkah 9, 21, dan 30 (Search untuk menemukan baris target di tabel berisi lebih dari satu halaman, R-16; kotak search tidak dikosongkan di antara TC karena langkah 21 dan 30 menggantinya), serta langkah 27 (expand `TAG` lalu `NFC` agar leaf `Tag` terlihat).
- Langkah 8 hanya ditulis untuk TC-AC-DN-79 karena hanya Expected TC itu yang menyebut popup tertutup; popup juga tertutup pada TC-AC-DN-80 dan TC-AC-DN-81 (langkah 15 dan 24 membuka popup baru).
- Ketiga TC membuat record milik spec sendiri dengan variasi Category dan Measurement (satu topik, satu kelas harness); tiap bagian tetap bermakna bila bagian sebelumnya gagal. Jumlah langkah (32) di bawah ambang sekitar 35.
- Pencatatan Create di Changelog, Activity Log, dan System Log (Post Condition TC-AC-DN-79) dicakup spec pencatatan log modul ini; spec ini tidak mengasersinya (S-05).
- Temuan untuk QA:
  - TC-AC-DN-81 menulis "pilih leaf `Tag`" tanpa langkah expand, padahal `Tag` berada di `TAG` > `NFC` > `Tag` (Pre-setup #14); spec menambah expand sebagai langkah penghubung.
  - TC-AC-DN-79 Post Condition b dan c (entri log dan opsi Device Name pada dropdown Device SKU) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini.
  - TC-AC-DN-80 dan TC-AC-DN-81 tidak menyebut cara menemukan baris baru di List; spec memakai Search.
