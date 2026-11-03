---
id: TC-AC-DN-E2E-048-create-berhasil-trim-batas-dan-simbol
title: "Create Device Name Berhasil: Trim Spasi, 120 Karakter, Spasi Melewati Batas, dan Simbol Umum"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-89
  - TC-AC-DN-90
  - TC-AC-DN-92
  - TC-AC-DN-100
coverage:
  web: automated
---

# Create Device Name Berhasil: Trim Spasi, 120 Karakter, Spasi Melewati Batas, dan Simbol Umum

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`).
- Data Dinamis (dibuat lewat form Create, semua bersuffix `{runId}-048`):
  - TC-AC-DN-89: tiga spasi, `Trim Gateway {runId}-048`, tiga spasi (tersimpan ter-trim).
  - TC-AC-DN-90: nama 120 karakter A, pola `Alat Pemindai Gudang Besar ` diulang lalu dipotong sehingga total tepat 120 karakter termasuk suffix ` {runId}-048`.
  - TC-AC-DN-92: nama 120 karakter B, pola `Pemindai Gudang Alat Besar ` diulang lalu dipotong sehingga total tepat 120 karakter termasuk suffix ` {runId}-048`, diikuti lima spasi di akhir.
  - TC-AC-DN-100: `Pemindai (Industri) - #1 & Co. 50% @Gudang {runId}-048`.
  - Hook `after` menghapus keempat record lewat fixture BE (kemampuan hapus record Device Name disediakan tim FE/BE; pembersihan tidak berasumsi setup berhasil penuh).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-89: Spasi di awal dan akhir menyimpan nilai ter-trim

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik tiga spasi, `Trim Gateway {runId}-048`, lalu tiga spasi pada field Device Name
3. Verifikasi field Device Name menampilkan nilai yang diketik dan tidak ada pesan error di bawah field
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi toast sukses: "Success, device name has been created."
8. Ketik Search `Trim Gateway {runId}-048`, tekan Enter
9. Verifikasi hasil Search menemukan baris `Trim Gateway {runId}-048`
10. Verifikasi sel Device Name baris tersebut bernama `Trim Gateway {runId}-048` tanpa spasi di awal atau akhir

### TC-AC-DN-90: Device Name tepat 120 karakter

11. Klik tombol `+ Device Name` pada toolbar
12. Ketik nama 120 karakter A pada field Device Name
13. Verifikasi field Device Name menampilkan nilai yang diketik dan tidak ada error `Max. 120 characters`
14. Klik field Measurement lalu pilih `Unit`
15. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
16. Klik `[Submit]`
17. Verifikasi toast sukses: "Success, device name has been created."
18. Ganti isi kotak search dengan nama 120 karakter A, tekan Enter
19. Verifikasi sel Device Name baris baru menampilkan nama utuh 120 karakter tanpa pemotongan
20. Arahkan kursor ke sel Device Name baris baru
21. Verifikasi tidak ada tooltip pada sel Device Name

### TC-AC-DN-92: Spasi di akhir yang melewati 120 karakter

22. Klik tombol `+ Device Name` pada toolbar
23. Ketik nama 120 karakter B diikuti lima spasi pada field Device Name
24. Verifikasi field Device Name menampilkan nilai yang diketik dan tidak ada error `Max. 120 characters` karena panjang dihitung setelah trim
25. Klik field Measurement lalu pilih `Unit`
26. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
27. Klik `[Submit]`
28. Verifikasi toast sukses: "Success, device name has been created."

### TC-AC-DN-100: Tanda baca dan simbol umum diterima

29. Klik tombol `+ Device Name` pada toolbar
30. Ketik `Pemindai (Industri) - #1 & Co. 50% @Gudang {runId}-048` pada field Device Name
31. Verifikasi field Device Name menampilkan nilai yang diketik dan tidak ada pesan error karakter
32. Klik field Measurement lalu pilih `Unit`
33. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
34. Klik `[Submit]`
35. Verifikasi toast sukses: "Success, device name has been created."
36. Ganti isi kotak search dengan `Pemindai (Industri) - #1 & Co. 50% @Gudang {runId}-048`, tekan Enter
37. Verifikasi List memuat baris `Pemindai (Industri) - #1 & Co. 50% @Gudang {runId}-048`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Keempat TC bertanda FE Test "Need API".
- Alasan sekitar 35 langkah (satu topik, satu dataset, satu kelas harness): keempat TC adalah Create sukses dengan variasi isi Device Name pada form yang sama dan record milik spec sendiri; tiap bagian tetap bermakna bila bagian sebelumnya gagal. Jumlah langkah 37, terdiri atas pembukaan form per TC (prinsip 13, "Halaman yang sama dipakai berulang": tidak dapat dibagi karena tiap TC berakhir dengan Submit sukses yang menutup popup) dan pemecahan `Verifikasi` per klausa (S-01).
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 8, 18, dan 36 (Search untuk menemukan baris target, R-16; langkah 18 dan 36 mengganti isi kotak search sebelumnya).
- Asersi `Verifikasi` absence error pada langkah 3, 13, 24, dan 31 diletakkan sebelum [Submit] karena popup menutup setelah sukses; nilai yang tampil di field menjadi anchor positifnya.
- TC-AC-DN-92 tidak mengasersi baris di List karena Expected TC hanya toast sukses dan tidak adanya error batas karakter.
- Panjang nama pada TC-AC-DN-90 dan TC-AC-DN-92 dihitung termasuk suffix (R-06); nama A dan B dibuat berbeda supaya dua record tidak bentrok.
- Temuan untuk QA:
  - Post Condition TC-AC-DN-89, TC-AC-DN-90, TC-AC-DN-92, dan TC-AC-DN-100 ("Record tersimpan ...") tidak punya langkah observasi di TC sehingga tidak diasersi, kecuali yang sudah menjadi Expected.
  - TC-AC-DN-90 Data Uji menulis nama literal 120 karakter; spec memakai nama bersuffix 120 karakter sesuai S-12.
