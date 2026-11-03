---
id: TC-AC-DS-E2E-050-register-clear-field
title: "Register SKU: Clear Field Mengosongkan Semua Field, Menghapus Pesan Error, dan Tidak Menutup Popup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-164
  - TC-AC-DS-165
coverage:
  web: automated
---

# Register SKU: Clear Field Mengosongkan Semua Field, Menghapus Pesan Error, dan Tidak Menutup Popup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`); Device Name #26 (`UHF Handheld Reader`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg` 200 KB, `foto-b.png` 300 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form yang valid sehingga tidak membuat SKU dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-164: Clear Field pada popup Register mengosongkan semua field tanpa menutup popup

1. Klik tombol `[+ SKU]` pada toolbar
2. Centang `Stay on this form after submitting`
3. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `UHF Handheld Reader`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `H-CL` pada field Model/Type
7. Ketik `NEW-CLR` pada field SKU
8. Pilih Range Type `Long Range`
9. Unggah `foto-a.jpg` pada field Photo
10. Unggah `foto-b.png` pada field Photo
11. Klik `[Clear Field]`
12. Verifikasi field Category kembali kosong
13. Verifikasi field Device Name kembali kosong
14. Verifikasi field Brand kembali kosong
15. Verifikasi field Model/Type kembali kosong
16. Verifikasi field SKU kembali kosong
17. Verifikasi kedua foto pada field Photo kembali kosong
18. Verifikasi section Range Type hilang
19. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
20. Verifikasi tidak ada dialog konfirmasi
21. Verifikasi popup Register tetap terbuka
22. Verifikasi fokus berada pada field pertama

### TC-AC-DS-165: Clear Field menghapus pesan error dan status validasi

23. Klik `[Submit]` tanpa mengisi field apa pun
24. Verifikasi pesan "Category must not be empty" tampil pada field Category
25. Verifikasi pesan "Device name must not be empty" tampil pada field Device Name
26. Verifikasi pesan "Brand must not be empty" tampil pada field Brand
27. Verifikasi pesan "Model/type must not be empty" tampil pada field Model/Type
28. Verifikasi pesan "SKU must not be empty" tampil pada field SKU
29. Verifikasi pesan "Photo must not be empty" tampil pada field Photo
30. Klik `[Clear Field]`
31. Verifikasi semua pesan error dihapus
32. Verifikasi semua border merah dihapus
33. Verifikasi popup Register tetap terbuka
34. Verifikasi semua field kosong
35. Klik ikon close `[✕]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 35 menutup popup form bersih (field kosong, Stay hanya preferensi form) tanpa dialog Unsaved Changes. Langkah 24 sampai 29 mengikuti Expected a TC-AC-DS-165 (pesan tampil sebelum `[Clear Field]`) dan menjadi anchor positif bagi asersi penghapusan pesan pada langkah 31 dan 32 (8b butir 2): tanpa langkah itu penghapusan tidak dapat dibedakan dari pesan yang tidak pernah muncul. Kode `H-CL` dan `NEW-CLR` tidak pernah tersimpan sehingga ditulis literal sesuai TC.
- Pemakaian ulang popup (bagian 3, halaman yang sama dipakai berulang): TC-AC-DS-165 melanjutkan popup TC-AC-DS-164 yang sudah kosong sesudah `[Clear Field]`, dengan Stay tercentang.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: nama literal Pre-setup (#25, #26, #27, #29) dipakai sesuai pengecualian S-12 A-11 (`suite.md`); spec tidak membuat data Dinamis.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-164 Expected c ("fokus pada field pertama") tidak menyebut field pertama yang dimaksud; spec memakai Category sebagai field pertama pada form Register.
