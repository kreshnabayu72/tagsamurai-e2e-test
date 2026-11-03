---
id: TC-AC-DS-E2E-030-register-ganti-category-membuang-nilai-kondisional
title: "Register SKU: Mengganti Category Mereset Device Name dan Membuang Nilai Kondisional (Range Type, Port, User TAG)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-98
  - TC-AC-DS-580
  - TC-AC-DS-581
coverage:
  web: automated
---

# Register SKU: Mengganti Category Mereset Device Name dan Membuang Nilai Kondisional (Range Type, Port, User TAG)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC karena menjadi teks UI yang diasersi): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`, `Hardware > Smart Fixed Reader > Portal Reader`, `TAG > NFC > Asset TAG`); Device Name #26 (`UHF Handheld Reader`, `4-Port Fixed Reader`, `Asset TAG`); Brand Principal #27 (`Arcturus`). SKU inti #29 dan file foto uji #37: dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Spec tidak men-Submit form sehingga tidak membuat SKU; tidak ada state global yang diubah dan tidak ada cleanup.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup di atas.

## Test Steps

### TC-AC-DS-98: Mengganti Category setelah Device Name dan field kondisional terisi mereset Device Name dan membuang nilai kondisional

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `UHF Handheld Reader`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `H300` pada field Model/Type
6. Pilih Range Type `Short Range`
7. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
8. Verifikasi field Device Name kembali ke placeholder "Select device name"
9. Verifikasi section Range Type hilang dan nilai `Short Range` dibuang
10. Verifikasi section Port tampil kosong
11. Verifikasi field Brand tetap `Arcturus`
12. Verifikasi field Model/Type tetap `H300`

### TC-AC-DS-580: Mengganti Category setelah Port terisi membuang nilai Port dan menampilkan section Range Type

13. Klik `[Clear Field]`
14. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
15. Klik field Device Name lalu pilih `4-Port Fixed Reader`
16. Ketik `8080` pada field Port
17. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
18. Verifikasi field Device Name kembali ke placeholder "Select device name"
19. Verifikasi section Port hilang
20. Verifikasi section Range Type tampil kosong
21. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
22. Klik field Device Name lalu pilih `4-Port Fixed Reader`
23. Verifikasi field Port tampil kosong (nilai `8080` sudah dibuang dan tidak dipulihkan)

### TC-AC-DS-581: Mengganti Category setelah This is User TAG dicentang membuang pilihan checkbox

24. Klik `[Clear Field]`
25. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
26. Klik field Device Name lalu pilih `Asset TAG`
27. Centang checkbox `This is User TAG`
28. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
29. Verifikasi section checkbox `This is User TAG` hilang
30. Verifikasi field Device Name kembali ke placeholder "Select device name"
31. Verifikasi section Port tampil kosong
32. Klik field Category, pilih node `Asset TAG` (expand `TAG` lalu `NFC`), lalu klik `[Select]`
33. Klik field Device Name lalu pilih `Asset TAG`
34. Verifikasi checkbox `This is User TAG` tampil tidak tercentang (pilihan sebelumnya sudah dibuang)
35. Klik ikon close `[✕]`
36. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
37. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi): langkah 13 dan 24 (`[Clear Field]`) mengosongkan popup agar blok TC berikutnya mulai dari form kosong seperti precondition TC (S-09); langkah 35 sampai 37 menutup form dirty secara deterministik (S-08). Langkah 21, 22, 32, dan 33 mengembalikan Category dan Device Name sesuai langkah 7 TC-AC-DS-580 dan TC-AC-DS-581.
- Ukuran spec (di atas sekitar 35 langkah, 37 langkah): tiga blok memakai satu popup Register dan satu kelas fungsional (perilaku ganti Category), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; tidak ada pemisah nyata yang lebih baik daripada satu pembukaan popup (konvensi bagian 3, halaman yang sama dipakai berulang).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_TC_PASSWORD` dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
