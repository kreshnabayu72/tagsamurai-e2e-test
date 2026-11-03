---
id: TC-AC-DS-E2E-036-register-model-type-kosong-dan-batas-120
title: "Register SKU: Model/Type Kosong, Tepat 120 Karakter, dan 121 Karakter"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-123
  - TC-AC-DS-124
  - TC-AC-DS-125
coverage:
  web: automated
---

# Register SKU: Model/Type Kosong, Tepat 120 Karakter, dan 121 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-MT-120-{runId}-036` (Model/Type berisi 120 karakter `M`), dibuat oleh TC-AC-DS-124. Kode `NEW-REQ-MT` dan Model/Type 121 karakter tidak pernah tersimpan. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-036`.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-123: Submit dengan Model/Type kosong menampilkan pesan wajib diisi

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `Asset TAG`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `NEW-REQ-MT` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Klik `[Submit]` dengan Model/Type dibiarkan kosong
9. Verifikasi pesan inline di bawah field Model/Type: "Model/type must not be empty"
10. Verifikasi popup Register tetap terbuka

### TC-AC-DS-125: Model/Type 121 karakter menampilkan pesan Max. 120 characters

11. Ketik 121 karakter `M` pada field Model/Type
12. Verifikasi pesan inline "Max. 120 characters" tampil langsung saat karakter ke-121 diketik
13. Klik `[Submit]`
14. Verifikasi Submit diblok: popup Register tetap terbuka

### TC-AC-DS-124: Model/Type tepat 120 karakter diterima

15. Kosongkan isi field Model/Type lalu ketik 120 karakter `M`
16. Ganti isi field SKU dengan `NEW-MT-120-{runId}-036`
17. Verifikasi tidak ada pesan error pada Model/Type
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, device SKU has been registered." tampil
20. Verifikasi jumlah total SKU pada footer pagination bernilai N + 1: hanya SKU `NEW-MT-120-{runId}-036` yang tersimpan dan tidak ada SKU baru dari TC-AC-DS-123 dan TC-AC-DS-125

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 15 dan 16 menyiapkan form TC-AC-DS-124 dari form TC-AC-DS-125 (S-09), dengan SKU `NEW-REQ-MT` diganti `NEW-MT-120-{runId}-036` karena kode TC-AC-DS-124 harus disimpan dan unik.
- Urutan TC diubah: TC-AC-DS-125 dijalankan sebelum TC-AC-DS-124 (validasi yang diblokir sebelum aksi sukses, S-10) dan memakai ulang form TC-AC-DS-123 (bagian 3, halaman yang sama dipakai berulang); kode SKU `NEW-MT-121` pada TC-AC-DS-125 diganti kode form TC-AC-DS-123 dan tidak diasersi. Asersi "tidak ada SKU baru" TC-AC-DS-123 dan TC-AC-DS-125 diasersi sekali di langkah akhir dengan selisih N + 1 (S-12).
- Asersi tanpa pesan error Model/Type (TC-AC-DS-124 Expected a) diletakkan sebelum klik `[Submit]` karena popup tertutup sesudah Submit sukses; hanya Verifikasi toast sukses yang menjadi anchor sesudahnya.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-036` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
