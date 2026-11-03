---
id: TC-AC-DS-E2E-034-register-sku-121-karakter-kosong-dan-category-kosong
title: "Register SKU: SKU 121 Karakter, SKU Kosong, dan Category Kosong Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-114
  - TC-AC-DS-115
  - TC-AC-DS-129
coverage:
  web: automated
---

# Register SKU: SKU 121 Karakter, SKU Kosong, dan Category Kosong Diblokir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Seluruh Submit pada spec ini ditolak sehingga tidak ada SKU dibuat dan tidak ada cleanup. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut).
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-114: SKU 121 karakter menampilkan pesan Max. 120 characters dan Submit diblok

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `Asset TAG`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `T-LEN` pada field Model/Type
7. Unggah `foto-a.jpg` pada field Photo
8. Ketik 121 karakter `A` pada field SKU
9. Verifikasi pesan inline "Max. 120 characters" tampil langsung saat karakter ke-121 diketik
10. Klik `[Submit]`
11. Verifikasi Submit diblok: popup Register tetap terbuka

### TC-AC-DS-115: Submit dengan SKU kosong menampilkan pesan wajib diisi

12. Kosongkan isi field SKU
13. Klik `[Submit]`
14. Verifikasi pesan inline di bawah field SKU: "SKU must not be empty"
15. Verifikasi popup Register tetap terbuka

### TC-AC-DS-129: Submit dengan Category kosong menampilkan pesan wajib diisi

16. Klik `[Clear Field]`
17. Klik field Brand lalu pilih `Arcturus`
18. Ketik `T-REQ` pada field Model/Type
19. Ketik `NEW-REQ` pada field SKU
20. Unggah `foto-a.jpg` pada field Photo
21. Klik `[Submit]`
22. Verifikasi pesan inline di bawah field Category: "Category must not be empty"
23. Verifikasi popup Register tetap terbuka
24. Klik ikon close `[✕]`
25. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
26. Klik `[Leave]`
27. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga percobaan Submit

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 12 (kosongkan SKU) dan 16 (`[Clear Field]`) menyiapkan form untuk TC berikutnya (S-09); langkah 24 sampai 26 menutup form dirty secara deterministik (S-08).
- Pemakaian ulang form (bagian 3, halaman yang sama dipakai berulang): TC-AC-DS-115 melanjutkan form TC-AC-DS-114 dengan Model/Type `T-LEN` (TC-AC-DS-115 menyebut `T-REQ`); nilai itu bukan objek asersi TC-AC-DS-115.
- Butir "tidak ada SKU baru" pada Expected b ketiga TC diasersi sekali di langkah akhir dengan selisih terhadap baseline N (S-12) karena seluruh Submit ditolak dan tidak ada baris yang bisa dicari; kode `NEW-REQ` dan `T-REQ` tidak pernah tersimpan sehingga ditulis literal sesuai TC.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-034` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
