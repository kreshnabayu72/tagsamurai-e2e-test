---
id: TC-AC-DS-E2E-033-register-sku-format-karakter-paste-dan-batas-120
title: "Register SKU: Field SKU Huruf Besar Otomatis, Blokir Karakter Invalid, Paste, dan Batas 120 Karakter"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-109
  - TC-AC-DS-110
  - TC-AC-DS-111
  - TC-AC-DS-112
  - TC-AC-DS-113
coverage:
  web: automated
---

# Register SKU: Field SKU Huruf Besar Otomatis, Blokir Karakter Invalid, Paste, dan Batas 120 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): SKU inti #29, pohon Category #25, Device Name #26, Brand #27 dan file foto uji #37 dipakai sebagai precondition TC, tidak diasersi. Spec hanya mengetik dan mem-paste pada field SKU.
- Data Dinamis: tidak ada. Spec tidak membuat SKU dan tidak ada cleanup.
- Kemampuan teknis: clipboard browser (salin dan tempel/paste teks) untuk TC-AC-DS-111 dan TC-AC-DS-112, disediakan tim FE. Jeda nyata 1 detik pada langkah 24 memenuhi debounce pemeriksaan keunikan SKU (sekitar 500 ms) dan disebut eksplisit.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-109: Field SKU mengubah huruf kecil menjadi huruf besar secara otomatis

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field SKU lalu ketik `hhr-new-01`
3. Verifikasi teks pada field SKU tampil `HHR-NEW-01`

### TC-AC-DS-110: Karakter di luar huruf, angka, tanda hubung, dan titik diblok saat mengetik tanpa pesan

4. Kosongkan isi field SKU
5. Ketik `A_B C#D` karakter demi karakter pada field SKU
6. Verifikasi teks pada field SKU tampil `ABCD`: karakter `_`, spasi, dan `#` tidak pernah masuk
7. Verifikasi helper text "Letters, numbers, hyphens, and dots only (e.g. SKU-RFID-V2)" tetap tampil
8. Verifikasi tidak ada pesan error yang muncul

### TC-AC-DS-111: Paste teks ber-karakter invalid membuang karakter invalid dan memasukkan sisanya

9. Kosongkan isi field SKU
10. Salin teks `ab_c d.e-f` ke clipboard
11. Tempel (paste) ke field SKU
12. Verifikasi teks pada field SKU tampil `ABCD.E-F` (karakter `_` dan spasi dibuang, sisanya dimasukkan lalu di-uppercase)
13. Verifikasi tidak ada pesan error

### TC-AC-DS-112: Paste teks lebih dari 120 karakter pada field SKU tidak dipotong dan menampilkan pesan Max. 120 characters

14. Kosongkan isi field SKU
15. Salin teks berisi 130 karakter huruf `A` ke clipboard
16. Tempel (paste) ke field SKU
17. Verifikasi field SKU menampung seluruh 130 karakter `A` hasil paste tanpa pemotongan
18. Verifikasi pesan inline "Max. 120 characters" tampil pada field SKU
19. Klik `[Submit]`
20. Verifikasi `[Submit]` ditolak: popup Register tetap terbuka selama teks masih melebihi 120 karakter

### TC-AC-DS-113: SKU tepat 120 karakter diterima tanpa pesan error

21. Kosongkan isi field SKU
22. Ketik 120 karakter `A` pada field SKU
23. Verifikasi field SKU berisi 120 karakter
24. Tunggu 1 detik
25. Verifikasi tidak ada pesan error pada field SKU
26. Verifikasi helper text "Letters, numbers, hyphens, and dots only (e.g. SKU-RFID-V2)" tetap tampil
27. Verifikasi tidak ada pesan duplikat setelah debounce
28. Klik ikon close `[✕]`
29. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
30. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 4, 9, 14, dan 21 mengosongkan field SKU agar TC berikutnya mengetik pada field kosong (S-09); langkah 19 menambahkan klik `[Submit]` karena Expected c TC-AC-DS-112 (Submit ditolak) tidak punya langkah Submit di TC; langkah 28 sampai 30 menutup form dirty secara deterministik (S-08).
- Anchor absence (bagian 8b butir 2): asersi tanpa pesan error pada TC-AC-DS-110, 111, dan 113 didahului Verifikasi nilai field SKU yang tampil.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-033` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-112 Expected c (`[Submit]` ditolak selama teks lebih dari 120 karakter): Submit pada form yang field lainnya kosong juga ditolak oleh pesan wajib diisi, sehingga penolakan karena batas 120 karakter tidak dapat dibedakan dari penolakan karena field lain; TC tidak memberi langkah Submit maupun field lain yang terisi.
