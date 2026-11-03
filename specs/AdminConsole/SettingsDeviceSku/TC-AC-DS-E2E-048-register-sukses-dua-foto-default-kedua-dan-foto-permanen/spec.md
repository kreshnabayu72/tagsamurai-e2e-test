---
id: TC-AC-DS-E2E-048-register-sukses-dua-foto-default-kedua-dan-foto-permanen
title: "Register SKU Berhasil: Dua Foto dengan Foto Kedua sebagai Default dan Foto Menjadi Permanen Setelah Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-144
  - TC-AC-DS-158
coverage:
  web: automated
---

# Register SKU Berhasil: Dua Foto dengan Foto Kedua sebagai Default dan Foto Menjadi Permanen Setelah Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg` 200 KB, `foto-b.png` 300 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-PH-OK-{runId}-048` (satu foto `foto-a.jpg`) dan `NEW-2PH-01-{runId}-048` (dua foto, default `foto-b.png`), dibuat oleh TC-AC-DS-144 dan TC-AC-DS-158. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-048` milik Principal.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk membaca status penyimpanan file foto (berada di staging tanpa referensi, atau permanen dan direferensikan record SKU); mekanisme dan endpoint-nya tidak tercantum di TC sehingga tidak disebut di sini.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-144: Foto menjadi permanen dan direferensikan hanya setelah Submit sukses

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `Asset TAG`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-PHOK` pada field Model/Type
6. Ketik `NEW-PH-OK-{runId}-048` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Periksa penyimpanan file lewat Fixture BE sebelum Submit
9. Verifikasi foto `foto-a.jpg` berada di staging tanpa referensi record SKU
10. Klik `[Submit]`
11. Tunggu popup Register tertutup (aksi selesai)
12. Periksa penyimpanan file lewat Fixture BE sesudah Submit
13. Verifikasi foto `foto-a.jpg` direferensikan oleh record SKU `NEW-PH-OK-{runId}-048`
14. Ketik Search `NEW-PH-OK-{runId}-048`, tekan Enter
15. Verifikasi thumbnail baris `NEW-PH-OK-{runId}-048` pada List tampil

### TC-AC-DS-158: Register SKU dengan dua foto dan foto kedua sebagai default

16. Klik tombol `[+ SKU]` pada toolbar
17. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
18. Klik field Device Name lalu pilih `Asset TAG`
19. Klik field Brand lalu pilih `Arcturus`
20. Ketik `T-2P` pada field Model/Type
21. Ketik `NEW-2PH-01-{runId}-048` pada field SKU
22. Unggah `foto-a.jpg` pada field Photo
23. Unggah `foto-b.png` pada field Photo
24. Tandai foto kedua `foto-b.png` sebagai default
25. Klik `[Submit]`
26. Verifikasi toast sukses "Success, device SKU has been registered." tampil
27. Ganti isi kotak search dengan `NEW-2PH-01-{runId}-048`, tekan Enter
28. Verifikasi thumbnail baris `NEW-2PH-01-{runId}-048` pada List adalah `foto-b.png` (foto default)
29. Klik ⋯ pada baris `NEW-2PH-01-{runId}-048` lalu pilih `Edit`
30. Verifikasi popup Edit SKU menampilkan dua foto
31. Verifikasi popup Edit SKU menampilkan `foto-b.png` sebagai default
32. Klik ikon close `[✕]` pada popup Edit SKU
33. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 11 menunggu aksi Submit selesai sebelum pembacaan Fixture BE (bagian 8b butir 8); langkah 14, 27, dan 33 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 32 menutup popup Edit SKU yang tidak diubah (form bersih, tanpa dialog Unsaved Changes).
- Urutan Expected TC-AC-DS-144: butir b (setelah Submit) diasersi dalam dua Verifikasi, status di Fixture BE lalu thumbnail pada List, karena keduanya klausa yang dapat gagal sendiri (S-01).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-048` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Post Condition TC-AC-DS-144 dan TC-AC-DS-158 (entri log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
  - TC-AC-DS-158 tidak menyebut kontrol UI untuk menandai foto default; langkah mengikuti kata kerja TC dan perlu penjelasan QA/FE. Cara menyatakan thumbnail `foto-b.png` di List (nama berkas atau gambar) juga tidak dijelaskan di TC.
