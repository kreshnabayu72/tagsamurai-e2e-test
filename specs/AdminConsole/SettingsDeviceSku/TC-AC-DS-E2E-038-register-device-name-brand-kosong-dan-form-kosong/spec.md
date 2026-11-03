---
id: TC-AC-DS-E2E-038-register-device-name-brand-kosong-dan-form-kosong
title: "Register SKU: Device Name Kosong, Brand Kosong, dan Submit Form Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-130
  - TC-AC-DS-131
  - TC-AC-DS-132
coverage:
  web: automated
---

# Register SKU: Device Name Kosong, Brand Kosong, dan Submit Form Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: tidak ada. Seluruh Submit pada spec ini ditolak sehingga tidak ada SKU dibuat dan tidak ada cleanup. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut).
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-130: Submit dengan Device Name kosong menampilkan pesan wajib diisi

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-REQ` pada field Model/Type
6. Ketik `NEW-REQ` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Klik `[Submit]` dengan Device Name dibiarkan kosong
9. Verifikasi pesan inline di bawah field Device Name: "Device name must not be empty"
10. Verifikasi popup Register tetap terbuka

### TC-AC-DS-131: Submit dengan Brand kosong menampilkan pesan wajib diisi

11. Klik `[Clear Field]`
12. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
13. Klik field Device Name lalu pilih `Asset TAG`
14. Ketik `T-REQ` pada field Model/Type
15. Ketik `NEW-REQ` pada field SKU
16. Unggah `foto-a.jpg` pada field Photo
17. Klik `[Submit]` dengan Brand dibiarkan kosong
18. Verifikasi pesan inline di bawah field Brand: "Brand must not be empty"
19. Verifikasi popup Register tetap terbuka

### TC-AC-DS-132: Submit form kosong menampilkan semua pesan wajib diisi sekaligus

20. Klik `[Clear Field]`
21. Klik `[Submit]` tanpa mengisi field apa pun
22. Verifikasi pesan "Category must not be empty" tampil pada field Category
23. Verifikasi pesan "Device name must not be empty" tampil pada field Device Name
24. Verifikasi pesan "Brand must not be empty" tampil pada field Brand
25. Verifikasi pesan "Model/type must not be empty" tampil pada field Model/Type
26. Verifikasi pesan "SKU must not be empty" tampil pada field SKU
27. Verifikasi pesan "Photo must not be empty" tampil pada field Photo
28. Verifikasi popup Register tetap terbuka
29. Klik ikon close `[✕]`
30. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]`
32. Verifikasi jumlah total SKU pada footer pagination sama dengan baseline N: tidak ada SKU baru dari ketiga percobaan Submit

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 11 dan 20 (`[Clear Field]`) mengosongkan popup agar tiap TC mulai dari popup kosong (S-09); langkah 29 sampai 31 menutup form dirty secara deterministik (S-08) karena `[Clear Field]` tidak dianggap sebagai penutupan form.
- Butir "tidak ada SKU baru" pada Expected b ketiga TC diasersi sekali di langkah akhir dengan selisih terhadap baseline N (S-12) karena seluruh Submit ditolak dan tidak ada baris yang bisa dicari; kode `NEW-REQ` dan `T-REQ` tidak pernah tersimpan sehingga ditulis literal sesuai TC.
- TC-AC-DS-132 Expected a diasersi satu Verifikasi per pesan karena tiap pesan adalah klausa tersendiri pada field masing-masing (S-01).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-038` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
