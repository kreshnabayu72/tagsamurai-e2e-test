---
id: TC-AC-DS-E2E-056-register-keunikan-kode-sku-lintas-scope
title: "Register SKU: Keunikan Kode SKU Lintas Scope Principal dan Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-119
  - TC-AC-DS-120
  - TC-AC-DS-121
coverage:
  web: automated
---

# Register SKU: Keunikan Kode SKU Lintas Scope Principal dan Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Data Pre-setup #10) `totalControlDist_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_DS_DIST_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, `Spectra.env.AC_DS_TC_PASSWORD`).
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); Brand Distributor Cakra #28 (`Nordik`); SKU Principal inti #29 (`TAG-ARC-USR`); SKU lokal Distributor Cakra #31 (`LOC-NOR-01`); SKU lokal Distributor PT Nusantara Mitra #31 (`NUS-LOC-01`, milik Distributor lain yang tidak terlihat oleh Cakra); file foto uji #37 (`foto-a.jpg`, 200 KB).
- Data Dinamis: SKU `NUS-LOC-01` milik Distributor PT Cakra Distribusi (Model/Type `T-DUP`, dibuat TC-AC-DS-120) dan SKU `LOC-NOR-01` milik Principal PT Arunika Prima (Model/Type `T-DUP2`, dibuat TC-AC-DS-121). Kedua kode ditulis literal tanpa suffix karena asersi bergantung pada kode yang sama dengan SKU Pre-setup entitas lain (S-12). Hook `before` menghapus lewat API sisa SKU `NUS-LOC-01` milik Cakra dan `LOC-NOR-01` milik Principal; hook `after` menghapus keduanya (tidak berasumsi seeding berhasil penuh).
- Ganti akun: langkah 19 login sebagai Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD`; langkah 31 login kembali sebagai Distributor Cakra. Hook `after` mengembalikan sesi ke akun default suite (Principal).
- Kemampuan teknis: jeda nyata 1 detik pada langkah 3 dan 11 memenuhi debounce pemeriksaan keunikan SKU (sekitar 500 ms) dan disebut eksplisit.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-119: Distributor tidak dapat memakai kode SKU yang sudah dimiliki SKU Principal

1. Klik tombol `[+ SKU]` pada toolbar
2. Ketik `TAG-ARC-USR` pada field SKU
3. Tunggu 1 detik
4. Verifikasi pesan error "SKU already exists" tampil karena Distributor diperiksa terhadap SKU Principal dan SKU miliknya

### TC-AC-DS-120: Dua Distributor boleh memakai kode SKU yang sama

5. Klik `[Clear Field]`
6. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
7. Klik field Device Name lalu pilih `Asset TAG`
8. Klik field Brand lalu pilih `Nordik`
9. Ketik `T-DUP` pada field Model/Type
10. Ketik `NUS-LOC-01` pada field SKU
11. Tunggu 1 detik
12. Verifikasi tidak ada pesan duplikat pada field SKU walau Distributor PT Nusantara Mitra sudah memiliki `NUS-LOC-01`
13. Unggah `foto-a.jpg` pada field Photo
14. Klik `[Submit]`
15. Verifikasi toast sukses "Success, device SKU has been registered." tampil
16. Ketik Search `NUS-LOC-01`, tekan Enter
17. Verifikasi baris `NUS-LOC-01` milik PT Cakra Distribusi tampil pada List Distributor
18. Klik `(←)` pada kotak Search
19. Ganti akun: logout lalu login sebagai Total Control Principal PT Arunika Prima

### TC-AC-DS-121: Principal boleh mendaftarkan kode SKU yang sama dengan SKU lokal Distributor dan Distributor melihat dua baris berkode sama

20. Klik tombol `[+ SKU]` pada toolbar
21. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
22. Klik field Device Name lalu pilih `Asset TAG`
23. Klik field Brand lalu pilih `Arcturus`
24. Ketik `T-DUP2` pada field Model/Type
25. Ketik `LOC-NOR-01` pada field SKU
26. Tunggu 1 detik
27. Verifikasi tidak ada pesan duplikat pada field SKU
28. Unggah `foto-a.jpg` pada field Photo
29. Klik `[Submit]`
30. Verifikasi toast sukses "Success, device SKU has been registered." tampil
31. Ganti akun: logout lalu login sebagai Total Control Distributor PT Cakra Distribusi
32. Buka Settings > Device > Device SKU
33. Klik icon Search, ketik `LOC-NOR-01`, lalu tekan Enter
34. Verifikasi Distributor melihat dua baris `LOC-NOR-01`: SKU Principal (read-only) dan SKU miliknya sendiri
35. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 16, 18, 33, dan 35 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 19 dan 31 adalah ganti akun eksplisit (S-07); langkah mengosongkan popup (`[Clear Field]`) mengikuti S-09; langkah 'Buka Settings > Device > Device SKU' membuka halaman sesudah login ulang. Popup tertutup sendiri sesudah Submit sukses.
- Verifikasi "tidak ada pesan duplikat" pada TC-AC-DS-120 dan TC-AC-DS-121 diletakkan sebelum klik `[Submit]` karena popup tertutup sesudah Submit sukses; anchor positifnya adalah pesan duplikat yang diasersi pada TC-AC-DS-119 untuk mekanisme yang sama dan toast sukses yang diasersi sesudahnya.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-056` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - S-12: kode `NUS-LOC-01` dan `LOC-NOR-01` ditulis literal tanpa suffix karena asersi bergantung pada kode yang sama dengan SKU Pre-setup entitas lain; pengecualian ini belum ada di Lampiran A dan perlu keputusan.
  - TC-AC-DS-120 Post Condition b (keberadaan SKU Distributor lain tidak terungkap) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
