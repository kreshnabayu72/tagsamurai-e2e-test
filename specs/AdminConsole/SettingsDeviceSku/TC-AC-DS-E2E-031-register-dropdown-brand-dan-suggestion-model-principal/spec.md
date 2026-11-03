---
id: TC-AC-DS-E2E-031-register-dropdown-brand-dan-suggestion-model-principal
title: "Register SKU Principal: Dropdown Brand, Suggestion Model/Type, dan Model/Type Bebas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-99
  - TC-AC-DS-101
  - TC-AC-DS-103
coverage:
  web: automated
---

# Register SKU Principal: Dropdown Brand, Suggestion Model/Type, dan Model/Type Bebas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`, `International Scanner Solutions`, `Kinetia`, `Veltrix`, `Zephyr` yang belum dipakai SKU mana pun); SKU inti #29 sebagai sumber suggestion Model/Type (`T-OBJ`, `T-USR`, `H100`, `H200`); SKU lokal Distributor #31 (`R-01`, `GW-N2`) dipakai untuk asersi suggestion tidak tampil; file foto uji #37 (`foto-a.jpg`, 200 KB).
- Data Dinamis: SKU `NEW-TAG-FREE-{runId}-031` (Model/Type `Model Baru X1`), dibuat oleh TC-AC-DS-103. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-031` milik Principal.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-99: Dropdown Brand Principal memuat Brand milik entitas login secara flat dan alfabetis

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Brand
3. Verifikasi opsi Brand berurutan alfabetis dan datar tanpa hierarki: `Arcturus`, `International Scanner Solutions`, `Kinetia`, `Veltrix`, `Zephyr`
4. Verifikasi Brand `Zephyr` yang belum dipakai SKU mana pun tetap tampil sebagai opsi karena sumbernya master Brand, bukan isi tabel
5. Tekan Esc untuk menutup daftar opsi

### TC-AC-DS-101: Suggestion Model/Type berupa prefix case-insensitive dari SKU yang dapat dilihat Principal

6. Klik field Model/Type lalu ketik `t-`
7. Verifikasi daftar suggestion memuat `T-OBJ` dan `T-USR` (prefix tidak membedakan huruf besar-kecil)
8. Kosongkan isi field Model/Type lalu ketik `H`
9. Verifikasi daftar suggestion memuat `H100` dan `H200`
10. Verifikasi suggestion Model/Type SKU Distributor (`R-01`, `GW-N2`) tidak tampil bagi Principal

### TC-AC-DS-103: Model/Type bebas diisi dengan nilai di luar daftar suggestion dan tersimpan persis

11. Klik `[Clear Field]`
12. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
13. Klik field Device Name lalu pilih `Asset TAG`
14. Klik field Brand lalu pilih `Arcturus`
15. Ketik `Model Baru X1` pada field Model/Type
16. Ketik `NEW-TAG-FREE-{runId}-031` pada field SKU
17. Unggah `foto-a.jpg` pada field Photo
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, device SKU has been registered." tampil
20. Ketik Search `NEW-TAG-FREE-{runId}-031`, tekan Enter
21. Verifikasi baris `NEW-TAG-FREE-{runId}-031` menampilkan badge Model/Type `Model Baru X1` apa adanya
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 5 (Esc menutup daftar opsi Brand), langkah 8 (mengosongkan Model/Type agar `H` diketik pada field kosong sesuai langkah 4 TC-AC-DS-101), langkah 11 (`[Clear Field]` agar TC-AC-DS-103 mulai dari popup kosong, S-09), langkah 20 dan 22 (Search untuk menemukan baris target lalu menutup Search, R-16).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-031` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-101 Expected c (suggestion Model/Type SKU Distributor `R-01`, `GW-N2` tidak tampil bagi Principal): nilai uji `t-` dan `H` tidak berawalan sama dengan `R-01` atau `GW-N2`, sehingga asersi ini lulus tanpa membuktikan isolasi scope; spec mengikuti TC.
  - Post Condition TC-AC-DS-103 (entri log Changelog, System Log, Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
