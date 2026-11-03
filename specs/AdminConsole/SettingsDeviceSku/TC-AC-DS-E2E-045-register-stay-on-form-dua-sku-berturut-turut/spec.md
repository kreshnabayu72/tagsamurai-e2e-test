---
id: TC-AC-DS-E2E-045-register-stay-on-form-dua-sku-berturut-turut
title: "Register SKU: Register Berturut-turut dengan Stay on this form Menghasilkan Dua SKU"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-161
coverage:
  web: automated
---

# Register SKU: Register Berturut-turut dengan Stay on this form Menghasilkan Dua SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); File foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-BATCH-1-{runId}-045` dan `NEW-BATCH-2-{runId}-045`, dibuat oleh TC-AC-DS-161. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-045` milik Principal.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Klik tombol `[+ SKU]` pada toolbar
2. Centang `Stay on this form after submitting`
3. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
4. Klik field Device Name lalu pilih `Asset TAG`
5. Klik field Brand lalu pilih `Arcturus`
6. Ketik `T-B1` pada field Model/Type
7. Ketik `NEW-BATCH-1-{runId}-045` pada field SKU
8. Unggah `foto-a.jpg` pada field Photo
9. Klik `[Submit]`
10. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk submit pertama
11. Tunggu toast sukses pertama hilang otomatis
12. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
13. Klik field Device Name lalu pilih `Asset TAG`
14. Klik field Brand lalu pilih `Arcturus`
15. Ketik `T-B2` pada field Model/Type
16. Ketik `NEW-BATCH-2-{runId}-045` pada field SKU
17. Unggah `foto-a.jpg` pada field Photo
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk submit kedua
20. Klik ikon close `[✕]`
21. Verifikasi popup Register tertutup
22. Verifikasi dialog Unsaved Changes tidak muncul pada penutupan popup form bersih
23. Ketik Search `{runId}-045`, tekan Enter
24. Verifikasi baris `NEW-BATCH-1-{runId}-045` ada pada List
25. Verifikasi baris `NEW-BATCH-2-{runId}-045` ada pada List
26. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 11 menunggu toast pertama hilang agar toast kedua tidak tertukar (R-12); langkah 23 dan 26 (Search untuk menemukan baris target lalu menutup Search, R-16).
- Anchor absence (bagian 8b butir 2): Verifikasi dialog Unsaved Changes tidak muncul didahului Verifikasi popup Register tertutup.
- Pembagian TC lintas spec: TC-AC-DS-160 (Stay tercentang, reset semua field) ada di spec 186.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-045` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Search `{runId}-045` pada langkah 23 mengandalkan Search mencocokkan substring kode SKU; cara pencocokan Search tidak dijelaskan di TC.
