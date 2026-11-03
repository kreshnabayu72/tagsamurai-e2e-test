---
id: TC-AC-DS-E2E-039-register-foto-unggah-ganti-default-dan-hapus
title: "Register SKU: Foto Unggah Satu dan Dua, Ganti Default, dan Hapus Foto Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-133
  - TC-AC-DS-134
  - TC-AC-DS-135
  - TC-AC-DS-140
coverage:
  web: automated
---

# Register SKU: Foto Unggah Satu dan Dua, Ganti Default, dan Hapus Foto Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); file foto uji #37 (`foto-a.jpg` 200 KB dan `foto-b.png` 300 KB). SKU inti #29, Device Name #26, dan Brand #27 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form sehingga tidak membuat SKU dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`

### TC-AC-DS-133: Unggah satu foto menampilkan foto dan otomatis menjadikannya default

3. Unggah `foto-a.jpg` pada field Photo
4. Verifikasi foto `foto-a.jpg` tampil pada slot Photo pertama
5. Verifikasi foto `foto-a.jpg` ditandai default secara otomatis
6. Verifikasi slot Photo kedua tersedia untuk diisi

### TC-AC-DS-134: Unggah dua foto menampilkan keduanya dengan foto pertama sebagai default

7. Unggah `foto-b.png` pada slot Photo kedua
8. Verifikasi kedua foto `foto-a.jpg` dan `foto-b.png` tampil
9. Verifikasi foto pertama `foto-a.jpg` ditandai default
10. Verifikasi tidak ada slot ketiga dan batas maksimum 2 foto tercapai

### TC-AC-DS-135: Mengganti foto default menjadi foto kedua mengubah tanda default

11. Tandai foto kedua `foto-b.png` sebagai default
12. Verifikasi tanda default berpindah ke `foto-b.png`
13. Verifikasi tanda default hilang dari `foto-a.jpg`
14. Verifikasi tidak ada mekanisme pengurutan manual foto

### TC-AC-DS-140: Menghapus foto default menaikkan foto yang tersisa menjadi default

15. Tandai foto pertama `foto-a.jpg` sebagai default
16. Hapus foto default `foto-a.jpg`
17. Verifikasi foto tersisa `foto-b.png` otomatis menjadi default
18. Verifikasi slot kedua kosong kembali
19. Verifikasi tidak ada pesan error
20. Klik ikon close `[✕]`
21. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
22. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 15 mengembalikan `foto-a.jpg` sebagai default agar precondition TC-AC-DS-140 (dua foto dengan `foto-a.jpg` default) terpenuhi setelah langkah 11; langkah 20 sampai 22 menutup form dirty secara deterministik (S-08). Seluruh TC memakai satu pembukaan popup dengan Category `Asset TAG` (bagian 3, halaman yang sama dipakai berulang); TC-AC-DS-134 melanjutkan foto dari TC-AC-DS-133 (unggah `foto-a.jpg` lalu `foto-b.png`).
- Anchor absence (bagian 8b butir 2): Verifikasi tidak ada slot ketiga, tanda default hilang, dan tidak ada pesan error didahului Verifikasi foto yang tampil pada slot yang sama.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-039` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-135 dan TC-AC-DS-140 tidak menyebut kontrol UI untuk menandai default atau menghapus foto (ikon, tombol, atau menu); langkah spec ditulis mengikuti kata kerja TC dan perlu penjelasan QA/FE.
  - TC-AC-DS-135 Expected b ("tidak ada mekanisme pengurutan manual foto") adalah asersi absence tanpa anchor khusus; spec memakai Verifikasi tanda default sebagai anchor.
