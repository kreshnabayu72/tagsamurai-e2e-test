---
id: TC-GS-POS-E2E-013-duplikat-dan-double-submit
title: Duplikat nama dan guard double-submit
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-97
  - TC-GS-POS-250
coverage:
  web: automated
---

# Duplikat nama dan guard double-submit

## Prerequisites

- Sudah login sebagai Role Total Control. Kredensial diambil lewat `Spectra.env.ADMIN_USERNAME` dan
  `Spectra.env.ADMIN_PASSWORD`.
- Berada di `Global Settings > User > Position` pada entitas uji utama.
- `Fixture.globalSettingsPosition.captions.toast.created` adalah toast sukses Create, yaitu
  `Success, position has been created.`
- `Fixture.globalSettingsPosition.captions.validation.duplicate` adalah pesan error duplikat, yaitu
  `Name already exists`.
- `Fixture.globalSettingsPosition.captions.form.actions.submit` adalah tombol submit, yaitu `Submit`.
- `Fixture.globalSettingsPosition.form.create.duplicateTarget` adalah nama yang sudah ada di entitas
  uji, yaitu `IT Manager`.
- `Fixture.globalSettingsPosition.form.create.duplicateTargetUpperCase` adalah varian huruf besar
  penuh dari nama tersebut, yaitu `IT MANAGER`.
- `Fixture.globalSettingsPosition.form.create.doubleSubmitName` adalah nama valid untuk uji
  double-submit, yaitu `Sales Coordinator 2`.
- Jumlah toast sukses yang muncul per aksi Create dihitung di spec, bukan diasumsikan satu. Kalau
  guard double-submit hilang, dua request create akan sama-sama sukses dan toast akan muncul dua kali
  tanpa error yang terlihat.
- Jumlah baris yang namanya cocok dengan nilai uji setelah aksi create juga dihitung di spec, bukan
  hanya membaca tampilan tabel. Dua record dengan nama sama bisa muncul sebagai satu baris kalau
  tabel melakukan trims atau paginasi dengan cara yang salah.
- Uji re-check atomik dilakukan dengan menekan Submit secepatnya tanpa menunggu deteksi real-time.
  Ini yang membedakan validasi di klien dari validasi di server.

## Test Steps

### Double-klik Submit tidak membuat record ganda

1. Catat jumlah baris yang namanya cocok dengan
   `Fixture.globalSettingsPosition.form.create.doubleSubmitName`, yaitu harus nol
2. Klik tombol `[+ Position]` untuk membuka modal Create
3. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.doubleSubmitName`
4. Verifikasi field Name menampilkan nilai tersebut tanpa inline error
5. Verifikasi jumlah baris yang namanya cocok masih nol
6. Klik tombol `[Submit]` dua kali dengan cepat tanpa jeda berarti
7. Verifikasi hanya satu request create yang terkirim ke server
8. Verifikasi tidak ada toast error yang muncul akibat request kedua
9. Verifikasi toast sukses muncul paling banyak satu kali
10. Verifikasi modal Create tertutup
11. Verifikasi jumlah baris yang namanya cocok dengan nilai tersebut tepat satu
12. Verifikasi baris tersebut menampilkan nama yang persis sama dengan yang diisi
13. Verifikasi jumlah total data bertambah tepat satu, bukan dua
14. Muat ulang halaman browser
15. Verifikasi jumlah baris yang namanya cocok tetap satu setelah muat ulang
16. Verifikasi tidak ada record duplikat tersembunyi di halaman lain

### Re-check atomik saat Submit memblokir nama duplikat

17. Verifikasi nama `Fixture.globalSettingsPosition.form.create.duplicateTarget` ada di tabel
18. Klik tombol `[+ Position]` untuk membuka modal Create baru
19. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.duplicateTargetUpperCase` secara
    cepat supaya deteksi real-time belum sempat selesai
20. Klik tombol `[Submit]` segera setelah mengetik, tanpa menunggu jeda deteksi duplikat
21. Verifikasi inline error `Fixture.globalSettingsPosition.captions.validation.duplicate` muncul
22. Verifikasi pesan error muncul meski pengecekan real-time di klien belum sempat berjalan, sehingga
    ada lapisan validasi kedua di server
23. Verifikasi tidak ada toast sukses yang muncul
24. Verifikasi modal Create tetap terbuka
25. Verifikasi field Name tetap berisi nilai yang diketik supaya pengguna bisa memperbaikinya
26. Verifikasi tidak ada baris baru yang masuk ke tabel
27. Verifikasi jumlah baris yang namanya cocok secara case-insensitive dengan nilai tersebut tetap
    satu, yaitu yang sudah ada sebelumnya
28. Verifikasi nama yang sudah ada itu tidak ikut berubah
29. Verifikasi jumlah total data tidak bertambah
30. Muat ulang halaman browser
31. Verifikasi tidak ada record tambahan setelah muat ulang, sehingga penolakan benar-benar terjadi di
    server dan bukan hanya di tampilan

### Nama duplikat setelah ada record lain dibuat

32. Buat satu Position baru dengan nama yang berbeda dari seluruh nama yang sudah ada di entitas uji,
    sehingga ada kondisi yang harus membuat re-check tetap berjalan
33. Verifikasi Position baru tersebut berhasil dibuat
34. Klik tombol `[+ Position]` untuk membuka modal Create baru
35. Isi field Name dengan `Fixture.globalSettingsPosition.form.create.doubleSubmitName`
36. Klik tombol `[Submit]`
37. Verifikasi inline error duplikat muncul untuk nama yang sama persis dengan yang dipakai pada
    subbagian double-submit
38. Verifikasi tidak ada toast sukses yang muncul
39. Verifikasi jumlah baris dengan nama tersebut tetap satu
40. Verifikasi jumlah total data tidak bertambah lagi

## Notes

- Guard double-submit diuji lewat jumlah request, jumlah toast, dan jumlah baris sekaligus.
  Masing-masing bisa lolos sendiri-sendiri: satu request tapi dua baris, atau dua request
  tapi satu toast karena toast kedua menimpa yang pertama.
- Langkah 7 sengaja memeriksa jumlah request, bukan hanya hasil akhir. Kalau guard hilang tapi server
  punya unique constraint, hasilnya tetap satu baris, dan test hanya akan lulus karena ada
  jalur lain yang menutupinya, bukan karena guard di klien bekerja.
- Re-check atomik diuji dengan menekan Submit sebelum debounce selesai. Ini satu-satunya cara
  membuktikan ada validasi kedua di server, karena kalau menunggu deteksi real-time, implementasinya
  yang salah tetap lulus.
- Varian huruf besar penuh dipilih karena perbedaan casing harus tidak berpengaruh. Kalau pengecekan
  server memakai query yang case-sensitive, varian ini akan lolos dan membuat record yang berbeda
  dari `IT Manager`.
- Jumlah baris yang namanya cocok dihitung ulang setelah muat ulang pada langkah 15 dan 31, bukan
  hanya dari tampilan. Tabel bisa saja menampilkan satu baris untuk dua record kalau ada
  de-duplikasi di sisi klien.
- Subbagian ketiga sengaja dibuat setelah ada record baru dibuat. Gunanya membuktikan re-check
  duplikat bukan hanya bekerja pada nama yang sudah ada sejak awal spec, tapi juga setelah tabel
  berubah.
- Perlakukan `Sales Coordinator 2` dan `IT MANAGER` sebagai dua nilai yang berbeda. Keduanya uji hal
  berbeda, yaitu pengulangan record dan ketidaksamaan huruf besar kecil.
