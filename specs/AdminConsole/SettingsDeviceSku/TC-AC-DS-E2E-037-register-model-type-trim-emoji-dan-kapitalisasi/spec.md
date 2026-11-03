---
id: TC-AC-DS-E2E-037-register-model-type-trim-emoji-dan-kapitalisasi
title: "Register SKU: Model/Type Trim Spasi, Emoji Diblok, dan Pembeda Huruf Besar-Kecil"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-126
  - TC-AC-DS-127
  - TC-AC-DS-128
coverage:
  web: automated
---

# Register SKU: Model/Type Trim Spasi, Emoji Diblok, dan Pembeda Huruf Besar-Kecil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-MT-TRIM-{runId}-037` (Model/Type `  H300  ` dengan dua spasi di awal dan akhir), `NEW-CS-01-{runId}-037` (Model/Type `iPhone`), dan `NEW-CS-02-{runId}-037` (Model/Type `iphone`). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-037`.
- Kemampuan teknis: clipboard browser (salin dan tempel/paste teks) untuk langkah 6, disediakan tim FE.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-127: Emoji pada Model/Type diblok saat mengetik dan saat paste

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Model/Type lalu ketik `H😊1`
3. Verifikasi field Model/Type berisi `H1`: emoji tidak pernah masuk
4. Verifikasi tidak ada pesan error pada Model/Type
5. Kosongkan isi field Model/Type
6. Salin teks `🔥X` ke clipboard
7. Tempel (paste) ke field Model/Type
8. Verifikasi field Model/Type berisi `X`: emoji dibuang

### TC-AC-DS-126: Spasi di awal dan akhir Model/Type dibuang saat disimpan

9. Klik `[Clear Field]`
10. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
11. Klik field Device Name lalu pilih `Asset TAG`
12. Klik field Brand lalu pilih `Arcturus`
13. Ketik `NEW-MT-TRIM-{runId}-037` pada field SKU
14. Unggah `foto-a.jpg` pada field Photo
15. Ketik `  H300  ` (dua spasi di awal dan akhir) pada field Model/Type
16. Klik `[Submit]`
17. Verifikasi toast sukses "Success, device SKU has been registered." tampil
18. Ketik Search `NEW-MT-TRIM-{runId}-037`, tekan Enter
19. Verifikasi badge Model/Type baris `NEW-MT-TRIM-{runId}-037` menampilkan `H300` tanpa spasi tepi
20. Klik `(←)` pada kotak Search

### TC-AC-DS-128: Model/Type membedakan huruf besar-kecil sehingga iPhone dan iphone dapat tersimpan terpisah

21. Klik tombol `[+ SKU]` pada toolbar
22. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
23. Klik field Device Name lalu pilih `Asset TAG`
24. Klik field Brand lalu pilih `Arcturus`
25. Ketik `iPhone` pada field Model/Type
26. Ketik `NEW-CS-01-{runId}-037` pada field SKU
27. Unggah `foto-a.jpg` pada field Photo
28. Klik `[Submit]`
29. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran pertama
30. Tunggu toast sukses pertama hilang otomatis
31. Klik `[+ SKU]` lalu isi Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `iphone`, SKU `NEW-CS-02-{runId}-037`, dan Photo `foto-a.jpg`
32. Klik `[Submit]`
33. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran kedua
34. Ketik Search `{runId}-037`, tekan Enter
35. Verifikasi baris `NEW-CS-01-{runId}-037` menampilkan badge Model/Type `iPhone`
36. Verifikasi baris `NEW-CS-02-{runId}-037` menampilkan badge Model/Type `iphone`
37. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 5 mengosongkan Model/Type sebelum paste; langkah 9 (`[Clear Field]`) agar TC-AC-DS-126 mulai dari popup kosong (S-09); langkah 18, 20, 34, dan 37 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 30 menunggu toast pertama hilang agar toast kedua tidak tertukar (R-12).
- Urutan TC diubah: TC-AC-DS-127 (tanpa Submit) dijalankan lebih dulu daripada TC-AC-DS-126 dan TC-AC-DS-128 yang membuat data (S-10).
- Ukuran spec (sekitar 35 langkah): TC-AC-DS-128 memerlukan dua pendaftaran berurutan sehingga langkah isi form diulang sesuai TC; ketiga blok adalah kelas fungsional yang sama (validasi dan penyimpanan Model/Type) dan berdiri sendiri.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-037` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Teks pencarian `{runId}-037` pada langkah 34 mengandalkan Search mencocokkan substring kode SKU; cara pencocokan Search tidak dijelaskan di TC.
