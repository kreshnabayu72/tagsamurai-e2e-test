---
id: TC-AC-DS-E2E-027-register-screening-popup-dan-picker-category
title: "Register SKU: Screening Popup, Screening Picker Category, dan Klik Root Non-selectable"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-87
  - TC-AC-DS-88
  - TC-AC-DS-89
coverage:
  web: automated
---

# Register SKU: Screening Popup, Screening Picker Category, dan Klik Root Non-selectable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25 (root `Hardware` dan `TAG` tidak dapat dipilih), Device Name #26, Brand #27, file foto #37, SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada). Spec ini membuka popup Register SKU tanpa mengisi field dan tidak menyimpan data.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-87: Screening popup Register SKU

1. Klik tombol `[+ SKU]` pada toolbar
2. Verifikasi judul popup `Register SKU` dan ikon close `[✕]` di sudut kanan atas
3. Verifikasi Section `Device Info` dan `SKU Info` tampil
4. Verifikasi field Category berupa tombol dengan placeholder "Select category"
5. Verifikasi field Device Name dengan placeholder "Select device name"
6. Verifikasi field Brand dengan placeholder "Select brand"
7. Verifikasi field Model/Type dengan placeholder "Enter model/type"
8. Verifikasi field SKU dengan placeholder "Enter SKU"
9. Verifikasi field Photo dengan teks "Upload photo (JPG, PNG, JPEG)"
10. Verifikasi urutan field Category, Device Name, Brand, Model/Type, SKU, Photo
11. Verifikasi helper text di bawah field SKU: "Letters, numbers, hyphens, and dots only (e.g. SKU-RFID-V2)" tampil sejak awal
12. Verifikasi field Range Type, Port, dan checkbox `This is User TAG` tidak dirender
13. Verifikasi tidak ada field Measurement
14. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang dan rata kanan pada Row 1 footer
15. Verifikasi `[Clear Field]` dan `[Submit]` rata kanan pada Row 2 footer
16. Verifikasi tidak ada tombol `[Cancel]` pada popup

### TC-AC-DS-88: Screening picker Category

17. Klik field Category
18. Verifikasi picker tampil sebagai popup pohon dengan kotak pencarian, `[Cancel]`, dan `[Select]`
19. Expand berurutan node `Hardware`, `Handheld Reader`, `Smart Fixed Reader`, `TAG`, lalu `NFC`
20. Verifikasi pohon memuat `Hardware` > (`Handheld Reader` > `UHF Handheld`, `Barcode Handheld`, `Perangkat Pemindai Kode Batang Industri`; `Smart Fixed Reader` > `Portal Reader`, `Tunnel Reader`; `BLE Gateway`) dan `TAG` > `NFC` > (`Wearable TAG`, `Asset TAG`)
21. Verifikasi `Hardware` dan `TAG` tampil sebagai root yang tidak dapat dipilih
22. Verifikasi `Handheld Reader`, `Smart Fixed Reader`, dan `NFC` (node yang punya anak) tampil sebagai node yang dapat dipilih

### TC-AC-DS-89: Klik root tidak memilih node

23. Klik node `Hardware`
24. Klik node `TAG`
25. Verifikasi `Hardware` dan `TAG` tidak berstatus terpilih, tidak ada highlight
26. Klik `[Select]`
27. Verifikasi field Category tetap menampilkan placeholder "Select category"
28. Tutup popup Register SKU dengan ikon close `[✕]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-87, TC-88, TC-89. Ketiganya memakai satu pembukaan popup Register SKU dan satu pembukaan picker (prinsip halaman yang sama dipakai berulang, bagian 3 prinsip 13); popup ditutup satu kali di langkah 28.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 17, 19, 23, 24, 26 (aksi yang hasilnya diasersi pada langkah berikutnya) dan langkah 28 (menutup popup yang tidak dirty lewat `[✕]`).
- Langkah 3 sampai 10 memecah Expected b.i TC-87 per field (S-01); langkah 12 dan 13 (absence) didahului langkah 3 sampai 10 (field lain tampil sebagai anchor); langkah 16 didahului langkah 15.
- Langkah 19 mengekspansi node berurutan sebagai satu langkah teks biasa; ekspansi sesuai langkah 4 TC-88.
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #25/#26/#27/#37 di environment belum diverifikasi.
  - TC-89 langkah 6 menulis "picker dicoba ditutup" dan Expected b mengasersi placeholder Category; TC tidak menyebut apakah picker tetap terbuka setelah `[Select]` tanpa pilihan. Spec mengikuti TC dan tidak mengasersi status picker.
  - TC-87 Expected b.i menyebut urutan field tanpa merinci cara membaca urutan; langkah 10 mengasersi urutan sesuai TC.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
