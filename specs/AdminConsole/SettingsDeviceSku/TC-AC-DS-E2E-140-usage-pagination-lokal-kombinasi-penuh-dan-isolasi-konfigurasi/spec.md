---
id: TC-AC-DS-E2E-140-usage-pagination-lokal-kombinasi-penuh-dan-isolasi-konfigurasi
title: "Usage: Pagination Lokal 13 Baris, Kombinasi Penuh Search/Filter/Sort, dan Isolasi Konfigurasi Kolom dari List dan Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-462
  - TC-AC-DS-585
  - TC-AC-DS-586
coverage:
  web: automated
---

# Usage: Pagination Lokal 13 Baris, Kombinasi Penuh Search/Filter/Sort, dan Isolasi Konfigurasi Kolom dari List dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `TAG-ARC-USR` dan `HHR-ARC-100` serta seed (#29, #30); data Usage `TAG-ARC-USR` 13 baris (`PT Arunika Prima` Principal dan 12 Client `PT Klien Uji 01` sampai `PT Klien Uji 12`) dan Usage `HHR-ARC-100` (#32, #24). Nilai dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Spec menyembunyikan kolom `Total Stock` Usage lewat overlay (langkah 26) dan menampilkannya kembali (langkah 28); preferensi kolom dihapus di hook `after` sebagai cadangan.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Usage, List, dan Changelog di browser (hook `before` agar ketiganya pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default].
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-462: Pagination lokal Usage by Company dengan 13 baris

1. Ketik Search `TAG-ARC-USR` pada List, tekan Enter
2. Klik SKU `TAG-ARC-USR`
3. Verifikasi Popup `Device SKU Detail` tampil
4. Verifikasi halaman 1 memuat 10 baris
5. Klik halaman 2
6. Verifikasi halaman 2 memuat 3 baris dari total 13 baris (`PT Arunika Prima` dan 12 Client `PT Klien Uji 01` sampai `PT Klien Uji 12`)
7. Klik selector ukuran halaman
8. Verifikasi selector ukuran halaman memuat opsi `10`, `25`, `50`, dan `100`

### Pemulihan state antar TC

9. Pilih ukuran halaman `10`; pindah ke halaman 1

### TC-AC-DS-586: Kombinasi Search, Filter, Sort, dan ukuran halaman berlaku bersamaan pada Usage by Company

10. Klik ikon Search pada popup, ketik Search `PT`, tekan Enter
11. Klik ikon Filter pada popup
12. Pada field Entity Type pilih `Client`
13. Klik `[Apply]` pada Filter Panel popup
14. Klik header kolom Company sekali
15. Klik header kolom Company sekali lagi
16. Ubah jumlah data per halaman menjadi 25
17. Verifikasi tabel memuat 12 baris Entity Type `Client` berurutan Descending dari `PT Klien Uji 12` sampai `PT Klien Uji 01` pada halaman 1
18. Verifikasi `PT Arunika Prima` (Entity Type `Principal`) tidak tampil karena Filter Entity Type `Client`
19. Verifikasi keempat kontrol tetap aktif tanpa saling menimpa: Search `PT`, Filter Entity Type `Client`, Sort Company Descending, dan 25 data per halaman

### Pemulihan state antar TC

20. Klik `(←)` pada kotak Search; klik `[Clear Field]`, klik `[Apply]`; klik header kolom Company sekali lagi (kembali ke default); ubah jumlah data per halaman menjadi 10; tutup popup `Device SKU Detail` dengan ikon close `[✕]`

### TC-AC-DS-585: Konfigurasi kolom Usage by Company tidak memengaruhi konfigurasi List dan modal Changelog

21. Ganti isi kotak search List dengan `HHR-ARC-100`, tekan Enter
22. Klik SKU `HHR-ARC-100`
23. Verifikasi Popup `Device SKU Detail` tampil
24. Klik header kolom Actions (⋯) pada popup
25. Verifikasi Overlay Column Visibility popup tampil
26. Hilangkan centang `Total Stock` pada overlay popup
27. Verifikasi kolom `Total Stock` hilang dari tabel Usage
28. Centang `Total Stock` kembali pada overlay popup
29. Tekan Esc
30. Verifikasi Overlay Column Visibility tertutup
31. Verifikasi Popup `Device SKU Detail` tetap tampil
32. Tekan Esc lagi
33. Verifikasi Popup `Device SKU Detail` tertutup
34. Klik header kolom Actions (⋯) pada List
35. Verifikasi Overlay Column Visibility List memuat `Photo`, `Device Name`, `SKU`, `Category`, `Brand`, `Model/Type`, `Current Stock`, dan `Last Modified` tercentang
36. Verifikasi Overlay Column Visibility List memuat `Hardware Type`, `Range Type`, dan `TAG Type` tidak tercentang
37. Tutup overlay List, lalu klik ikon Changelog
38. Klik header kolom Actions (⋯) pada modal
39. Verifikasi Overlay Column Visibility modal Changelog memuat ketujuh kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, dan `Modified By` tercentang

### Pemulihan state akhir

40. Tutup overlay modal, lalu tutup modal Changelog
41. Klik `(←)` pada kotak Search List

## Notes

- Spec berisi 41 langkah nominal, sedikit di atas sekitar 35 langkah, karena tiga blok TC berdiri sendiri pada permukaan Usage yang sama (pagination, kombinasi kontrol, isolasi konfigurasi); kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 20, 28, dan 40 hanya pemulihan (langkah 41 mengosongkan Search List).
- Urutan TC dalam spec: 462, 586, 585 (bukan urutan nomor); TC-AC-DS-585 terakhir karena menyembunyikan kolom Usage, sedangkan dua TC lain membutuhkan kolom bawaan (S-10).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 21 (Search List untuk menemukan baris `TAG-ARC-USR` dan `HHR-ARC-100`, R-16), langkah 9, 20, 28, 37, 40, dan 41 (S-03, S-09); langkah 28 menampilkan kembali kolom `Total Stock` Usage yang disembunyikan pada langkah 26.
- Expected 585 butir c ("cache tersimpan terpisah") adalah kesimpulan dari butir a dan b dan tidak teramati terpisah; tidak diberi `Verifikasi` sendiri (S-03).
- Expected 586 butir c dicatat satu `Verifikasi` (langkah 19, daftar keempat kontrol disebut utuh).
- Temuan untuk QA:
  - S-15: TC 462 Expected b menyebut opsi selector tanpa langkah yang membuka selector; langkah 7 ditambahkan sebagai langkah penghubung untuk mengamatinya.
  - S-14: TC tidak menyebut Search untuk menemukan baris `TAG-ARC-USR` dan `HHR-ARC-100`, padahal keduanya tidak berada di halaman pertama List (default sort SKU A-Z); spec menambah langkah Search (langkah 1 dan 21) sebagai langkah penghubung.
  - S-15: TC 585 menyatakan overlay Usage menyembunyikan kolom tanpa `[Save]`; kolom disembunyikan langsung (cache lokal). Pemulihan oleh hook `after`.
  - Fixture rancangan Pre-setup #32 dan #24 (12 Client uji) belum terverifikasi ada di environment; `Fixture.settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
