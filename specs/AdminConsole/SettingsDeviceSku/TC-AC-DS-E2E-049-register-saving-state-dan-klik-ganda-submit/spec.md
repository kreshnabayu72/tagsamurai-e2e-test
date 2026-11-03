---
id: TC-AC-DS-E2E-049-register-saving-state-dan-klik-ganda-submit
title: "Register SKU: Saving State selama Request dan Klik Ganda Cepat pada Submit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-162
  - TC-AC-DS-163
coverage:
  web: automated
---

# Register SKU: Saving State selama Request dan Klik Ganda Cepat pada Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-SAVING-{runId}-049` (TC-AC-DS-162) dan `NEW-DBL-{runId}-049` (TC-AC-DS-163). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-049` milik Principal.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk menahan respons request create SKU lalu melepaskannya dengan hasil sukses (menahan respons hanya untuk mengamati state loading, bukan kegagalan yang dipaksakan); intercept dilepas segera sesudah dipakai.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-162: Tombol Submit masuk Saving state selama request Register berlangsung

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `Asset TAG`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-SV` pada field Model/Type
6. Ketik `NEW-SAVING-{runId}-049` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Tunda respons API create dengan intercept lalu klik `[Submit]`
9. Verifikasi tombol `[Submit]` menampilkan loading selama request berlangsung
10. Verifikasi tombol `[Submit]` disabled selama request berlangsung
11. Verifikasi kontrol input, `[Clear Field]`, dan ikon `[✕]` disabled sementara
12. Lepaskan respons create yang ditunda dengan hasil sukses
13. Verifikasi toast sukses "Success, device SKU has been registered." tampil
14. Verifikasi Popup Register tertutup karena checkbox Stay tidak tercentang

### TC-AC-DS-163: Klik ganda cepat pada Submit hanya membuat satu SKU

15. Tunggu toast lama hilang otomatis
16. Klik tombol `[+ SKU]` pada toolbar
17. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
18. Klik field Device Name lalu pilih `Asset TAG`
19. Klik field Brand lalu pilih `Arcturus`
20. Ketik `T-DB` pada field Model/Type
21. Ketik `NEW-DBL-{runId}-049` pada field SKU
22. Unggah `foto-a.jpg` pada field Photo
23. Tunda respons API create dengan intercept lalu klik `[Submit]` dua kali dengan cepat
24. Verifikasi tombol `[Submit]` disabled segera setelah klik pertama
25. Lepaskan respons create yang ditunda dengan hasil sukses
26. Verifikasi hanya satu toast sukses "Success, device SKU has been registered." yang tampil
27. Ketik Search `NEW-DBL-{runId}-049`, tekan Enter
28. Verifikasi hanya satu baris `NEW-DBL-{runId}-049` pada List
29. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 12 dan 25 melepaskan respons yang ditahan; langkah 15 menunggu toast TC-AC-DS-162 hilang agar hitungan toast TC-AC-DS-163 tidak tertukar (R-12); langkah 27 dan 29 (Search untuk menemukan baris target lalu menutup Search, R-16).
- TC-AC-DS-163 tidak menahan respons; spec menahan respons lewat intercept seperti TC-AC-DS-162 supaya Expected b (Submit disabled segera setelah klik pertama) teramati sebelum popup tertutup (bagian 8b butir 5). Asersi toast sesudah respons dilepas mengikuti bagian 8b butir 11.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-049` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-163 Expected b dan Post Condition (satu entri Create pada tiap surface log) tidak punya cara pengamatan di TC untuk state sementara dan log; Post Condition entri log tidak diasersi di spec ini (S-01), sedangkan satu record SKU diamati lewat satu baris pada List.
