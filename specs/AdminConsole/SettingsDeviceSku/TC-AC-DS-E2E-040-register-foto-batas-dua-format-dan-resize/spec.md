---
id: TC-AC-DS-E2E-040-register-foto-batas-dua-format-dan-resize
title: "Register SKU: Foto Batas Maksimum 2, Format File Picker, dan Resize di Atas 1 MB"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-136
  - TC-AC-DS-137
  - TC-AC-DS-138
coverage:
  web: automated
---

# Register SKU: Foto Batas Maksimum 2, Format File Picker, dan Resize di Atas 1 MB

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); File foto uji #37 (`foto-a.jpg` 200 KB, `foto-b.png` 300 KB, `foto-c.jpeg` 150 KB, `dokumen.gif` format tidak didukung, `foto-besar.jpg` 3 MB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-PH-BIG-{runId}-040` (foto `foto-besar.jpg` 3 MB), dibuat oleh TC-AC-DS-138. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-040` milik Principal.
- Kemampuan teknis (disediakan tim FE): pemeriksaan filter tipe file pada file picker (TC-AC-DS-137) tanpa membuka dialog sistem operasi.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`

### TC-AC-DS-136: Memilih file ketiga diblok dengan pesan Maximum 2 photos

3. Unggah `foto-a.jpg` dan `foto-b.png` pada field Photo
4. Coba pilih `foto-c.jpeg` sebagai foto ketiga
5. Verifikasi pesan "Maximum 2 photos" tampil saat file dipilih
6. Verifikasi file ketiga `foto-c.jpeg` tidak ditambahkan
7. Verifikasi dua foto sebelumnya tetap ada
8. Verifikasi popup Register tetap terbuka

### TC-AC-DS-137: File picker hanya menerima JPG, PNG, dan JPEG tanpa pesan error format

9. Klik `[Clear Field]`
10. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
11. Klik field Photo
12. Periksa filter tipe file pada file picker
13. Verifikasi file picker hanya menampilkan file berformat JPG, PNG, dan JPEG
14. Coba memilih `dokumen.gif`
15. Verifikasi `dokumen.gif` tidak dapat dipilih
16. Verifikasi tidak ada pesan error format yang muncul

### TC-AC-DS-138: File lebih dari 1 MB di-resize otomatis tanpa pesan error

17. Klik field Device Name lalu pilih `Asset TAG`
18. Klik field Brand lalu pilih `Arcturus`
19. Ketik `T-BIG` pada field Model/Type
20. Ketik `NEW-PH-BIG-{runId}-040` pada field SKU
21. Unggah `foto-besar.jpg` (3 MB) pada field Photo
22. Verifikasi foto `foto-besar.jpg` (3 MB) diterima tanpa pesan error ukuran
23. Klik `[Submit]`
24. Verifikasi toast sukses "Success, device SKU has been registered." tampil
25. Ketik Search `NEW-PH-BIG-{runId}-040`, tekan Enter
26. Verifikasi thumbnail pada baris `NEW-PH-BIG-{runId}-040` tampil
27. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 9 (`[Clear Field]`) dan pemilihan ulang Category sesudahnya menyiapkan popup tanpa foto untuk TC-AC-DS-137 (S-09); langkah 25 dan 27 (Search untuk menemukan baris target lalu menutup Search, R-16). TC-AC-DS-138 melanjutkan popup TC-AC-DS-137 dengan Category `Asset TAG` yang sudah terpilih (langkah 3 TC-AC-DS-138).
- Asersi foto `foto-besar.jpg` diterima tanpa pesan error ukuran (TC-AC-DS-138 Expected a) diletakkan sebelum klik `[Submit]` karena pesan error ukuran akan muncul saat unggah; resize otomatis tidak dapat diamati terpisah dari thumbnail yang tampil sesudah Submit.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-040` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-137 tidak menyebut cara mengamati filter tipe file picker secara otomatis; kemampuan itu dicatat di Prerequisites sebagai disediakan tim FE.
  - Post Condition TC-AC-DS-138 (entri log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
