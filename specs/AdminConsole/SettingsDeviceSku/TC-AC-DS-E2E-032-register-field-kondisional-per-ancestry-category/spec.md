---
id: TC-AC-DS-E2E-032-register-field-kondisional-per-ancestry-category
title: "Register SKU: Field Kondisional per Ancestry Category (Range Type, Port, User TAG, BLE Gateway)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-104
  - TC-AC-DS-105
  - TC-AC-DS-106
  - TC-AC-DS-107
  - TC-AC-DS-108
coverage:
  web: automated
---

# Register SKU: Field Kondisional per Ancestry Category (Range Type, Port, User TAG, BLE Gateway)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`, `Hardware > Smart Fixed Reader > Portal Reader`, `Hardware > Smart Fixed Reader`, `TAG > NFC > Asset TAG`, `Hardware > BLE Gateway`). SKU inti #29, Device Name #26, Brand #27 dan file foto uji #37: dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form sehingga tidak membuat SKU dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-104: Category ancestry Handheld Reader menampilkan field Range Type dengan opsi Long Range dan Short Range

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
3. Verifikasi field Range Type tampil dengan placeholder "Select range type"
4. Verifikasi field Range Type wajib diisi
5. Klik field Range Type
6. Verifikasi opsi Range Type hanya `Long Range` dan `Short Range`
7. Verifikasi field Port dan checkbox This is User TAG tidak tampil
8. Tekan Esc untuk menutup daftar opsi

### TC-AC-DS-105: Category ancestry Smart Fixed Reader menampilkan field Port

9. Klik `[Clear Field]`
10. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
11. Verifikasi field Port tampil dengan placeholder "Enter port number"
12. Verifikasi field Port wajib diisi
13. Verifikasi field Range Type dan checkbox This is User TAG tidak tampil

### TC-AC-DS-106: Category ancestry TAG menampilkan checkbox This is User TAG tidak tercentang secara default

14. Klik `[Clear Field]`
15. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
16. Verifikasi checkbox `This is User TAG` tampil dalam keadaan tidak tercentang (artinya Object TAG)
17. Verifikasi checkbox `This is User TAG` tampil tanpa placeholder
18. Verifikasi field Range Type dan Port tidak tampil

### TC-AC-DS-107: Category ancestry BLE Gateway tidak menambah field kondisional

19. Klik `[Clear Field]`
20. Klik field Category, expand `Hardware`, pilih node `BLE Gateway`, lalu klik `[Select]`
21. Verifikasi field Category, Device Name, Brand, Model/Type, SKU, dan Photo tetap tampil
22. Verifikasi tidak ada field Range Type, Port, maupun checkbox This is User TAG

### TC-AC-DS-108: Category node induk Smart Fixed Reader tetap membawa ancestry Smart Fixed Reader

23. Klik `[Clear Field]`
24. Klik field Category, expand `Hardware`, pilih node `Smart Fixed Reader`, lalu klik `[Select]`
25. Verifikasi field Port tampil karena node `Smart Fixed Reader` sendiri berancestry Smart Fixed Reader
26. Klik ikon close `[✕]`
27. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
28. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 8 menutup daftar opsi Range Type; langkah 9, 14, 19, dan 23 (`[Clear Field]`) mengosongkan popup agar tiap TC mulai dari popup kosong seperti precondition TC (S-09); langkah 26 sampai 28 menutup form dirty secara deterministik (S-08).
- Urutan Verifikasi pada TC-AC-DS-104 (butir c), TC-AC-DS-105 (butir b), TC-AC-DS-106 (butir b), dan TC-AC-DS-107 (butir a) dibalik terhadap urutan Expected TC: elemen yang tampil diasersi lebih dulu sebagai anchor positif bagi asersi elemen yang tidak tampil (bagian 8b butir 2).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-032` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
