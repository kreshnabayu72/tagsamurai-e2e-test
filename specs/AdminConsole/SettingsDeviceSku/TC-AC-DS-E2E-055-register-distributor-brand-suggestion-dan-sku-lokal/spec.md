---
id: TC-AC-DS-E2E-055-register-distributor-brand-suggestion-dan-sku-lokal
title: "Register SKU Distributor: Dropdown Brand, Suggestion Model/Type, dan Register SKU Lokal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-100
  - TC-AC-DS-102
  - TC-AC-DS-159
coverage:
  web: automated
---

# Register SKU Distributor: Dropdown Brand, Suggestion Model/Type, dan Register SKU Lokal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Data Pre-setup #10) `totalControlDist_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_DS_DIST_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, `Spectra.env.AC_DS_TC_PASSWORD`).
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Distributor PT Cakra Distribusi #28 (`Nordik`, `Orbitron`), sedangkan Brand Principal #27 (`Arcturus`, `Veltrix`, `Kinetia`) tidak boleh tampil; SKU Principal inti #29 (`H100`); SKU lokal Distributor #31 (`LOC-NOR-01` Model/Type `R-01`, `LOC-NOR-02` Model/Type `GW-N2`, `LOC-NOR-03`); file foto uji #37 (`foto-a.jpg`, 200 KB).
- Data Dinamis: SKU `DIS-NEW-01-{runId}-055` (Distributor PT Cakra Distribusi, Brand `Nordik`, Model/Type `T-DN1`), dibuat oleh TC-AC-DS-159. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-055`.
- Ganti akun: langkah 26 login sebagai Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD`; hook `after` mengembalikan sesi ke akun default suite yang sama.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-100: Dropdown Brand Distributor hanya memuat Brand milik Distributor

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Brand
3. Verifikasi opsi Brand hanya `Nordik` dan `Orbitron`
4. Verifikasi Brand Principal (`Arcturus`, `Veltrix`, `Kinetia`) tidak tampil sebagai opsi
5. Tekan Esc untuk menutup daftar opsi

### TC-AC-DS-102: Suggestion Model/Type Distributor memuat Model/Type SKU Principal dan SKU miliknya tanpa SKU Distributor lain

6. Klik field Model/Type lalu ketik `R`
7. Verifikasi daftar suggestion memuat `R-01` (SKU milik Distributor)
8. Kosongkan isi field Model/Type lalu ketik `H1`
9. Verifikasi daftar suggestion memuat `H100` (SKU Principal)
10. Verifikasi Model/Type SKU Distributor lain tidak tampil sebagai suggestion

### TC-AC-DS-159: Register SKU oleh Distributor menjadikan SKU milik Distributor dan tidak tampil pada Principal

11. Klik `[Clear Field]`
12. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
13. Klik field Device Name lalu pilih `Asset TAG`
14. Klik field Brand lalu pilih `Nordik`
15. Ketik `T-DN1` pada field Model/Type
16. Ketik `DIS-NEW-01-{runId}-055` pada field SKU
17. Unggah `foto-a.jpg` pada field Photo
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, device SKU has been registered." tampil
20. Ketik Search `DIS-NEW-01-{runId}-055`, tekan Enter
21. Verifikasi baris `DIS-NEW-01-{runId}-055` tampil pada List Distributor
22. Klik ⋯ pada baris `DIS-NEW-01-{runId}-055`
23. Verifikasi menu ⋯ memuat `Detail`, `Edit`, dan `Delete`
24. Tekan Esc untuk menutup menu ⋯
25. Klik `(←)` pada kotak Search
26. Ganti akun: logout lalu login sebagai Total Control Principal PT Arunika Prima
27. Buka Settings > Device > Device SKU
28. Ketik Search `DIS-NEW-01-{runId}-055`, tekan Enter
29. Verifikasi pencarian `DIS-NEW-01-{runId}-055` pada List Principal menampilkan "No results found"
30. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 20, 25, 28, dan 30 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 24 menutup menu ⋯; langkah 26 dan langkah sesudahnya mengganti akun ke Principal secara eksplisit (S-07). Langkah mengosongkan popup (`[Clear Field]`) mengikuti S-09.
- Anchor absence (bagian 8b butir 2): empty state "No results found" hasil Search adalah anchor positif bagi asersi `DIS-NEW-01-{runId}-055` tidak ada pada List Principal; List Principal berisi SKU inti #29 yang tidak ditampilkan saat Search aktif.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-055` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-102 Expected c (Model/Type SKU Distributor lain tidak tampil): nilai uji `R` dan `H1` tidak berawalan sama dengan Model/Type Distributor lain (`NM-01`, `MN-01`), sehingga asersi ini lulus tanpa membuktikan isolasi; spec mengikuti TC.
