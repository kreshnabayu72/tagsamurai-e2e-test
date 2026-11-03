---
id: TC-AC-DS-E2E-043-register-port-batas-minimum-maksimum-dan-digit
title: "Register SKU: Port Batas 1 dan 65535, 65536 Diblokir, dan Hanya Digit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-149
  - TC-AC-DS-150
  - TC-AC-DS-151
coverage:
  web: automated
---

# Register SKU: Port Batas 1 dan 65535, 65536 Diblokir, dan Hanya Digit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Smart Fixed Reader > Portal Reader`); Device Name #26 (`4-Port Fixed Reader`); Brand Principal #27 (`Veltrix`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- Data Dinamis: SKU `NEW-PORT-1-{runId}-043` (Port `1`) dan `NEW-PORT-MX-{runId}-043` (Port `65535`), dibuat oleh TC-AC-DS-149. Kode `NEW-PORT-OVER` (Port `65536`) tidak pernah tersimpan. Jumlah total SKU pada footer pagination List dicatat di langkah 1 sebagai baseline N (dibaca dari UI, bukan angka absolut). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-043` milik Principal.
- Kemampuan teknis: clipboard browser (salin dan tempel/paste teks) untuk TC-AC-DS-151, disediakan tim FE.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Catat jumlah total SKU pada footer pagination List sebagai baseline N

### TC-AC-DS-151: Port hanya menerima digit: karakter non-digit diblok saat mengetik dan saat paste

2. Klik tombol `[+ SKU]` pada toolbar
3. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
4. Ketik `8a-0.,1 ` pada field Port karakter demi karakter
5. Verifikasi field Port berisi `801`: huruf, `-`, `.`, `,`, dan spasi tidak pernah masuk
6. Verifikasi tidak ada pesan error pada Port
7. Kosongkan isi field Port
8. Salin teks `9x9` ke clipboard
9. Tempel (paste) ke field Port
10. Verifikasi field Port berisi `99`

### TC-AC-DS-150: Port 65536 menampilkan pesan maksimum dan Submit diblok

11. Klik field Device Name lalu pilih `4-Port Fixed Reader`
12. Klik field Brand lalu pilih `Veltrix`
13. Ketik `SF-PO` pada field Model/Type
14. Ketik `NEW-PORT-OVER` pada field SKU
15. Ganti isi field Port dengan `65536`
16. Unggah `foto-a.jpg` pada field Photo
17. Klik `[Submit]`
18. Verifikasi pesan inline pada Port: "Port must be at most 65535"
19. Verifikasi popup Register tetap terbuka

### TC-AC-DS-149: Port 1 dan 65535 diterima sebagai batas minimum dan maksimum

20. Ganti isi field Model/Type dengan `SF-P1`
21. Ganti isi field SKU dengan `NEW-PORT-1-{runId}-043`
22. Ganti isi field Port dengan `1`
23. Verifikasi tidak ada pesan error pada Port untuk nilai `1`
24. Klik `[Submit]`
25. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran pertama
26. Tunggu toast sukses pertama hilang otomatis
27. Klik `[+ SKU]` lalu isi Category `Portal Reader`, Device Name `4-Port Fixed Reader`, Brand `Veltrix`, Model/Type `SF-PMX`, SKU `NEW-PORT-MX-{runId}-043`, Port `65535`, dan Photo `foto-a.jpg`
28. Verifikasi tidak ada pesan error pada Port untuk nilai `65535`
29. Klik `[Submit]`
30. Verifikasi toast sukses "Success, device SKU has been registered." tampil untuk pendaftaran kedua
31. Verifikasi jumlah total SKU pada footer pagination bernilai N + 2: hanya kedua SKU Port `1` dan `65535` yang tersimpan dan tidak ada SKU baru dari TC-AC-DS-150

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 1 mencatat baseline N; langkah 7 mengosongkan Port sebelum paste (S-09); langkah 26 menunggu toast pertama hilang agar toast kedua tidak tertukar (R-12). Popup tertutup sendiri sesudah Submit sukses sehingga tidak ada langkah penutupan.
- Urutan TC diubah: TC-AC-DS-151 dan TC-AC-DS-150 (tanpa pendaftaran berhasil) dijalankan sebelum TC-AC-DS-149 (validasi yang diblokir sebelum aksi sukses, S-10) dan memakai ulang popup berkategori `Portal Reader` (bagian 3, halaman yang sama dipakai berulang); Model/Type, SKU, dan Port TC-AC-DS-149 mengganti isian TC-AC-DS-150 karena kode TC-AC-DS-149 harus disimpan dan unik. Model/Type `SF-PMX` pada pendaftaran kedua dipakai karena TC hanya menyebut "field lain valid".
- Asersi tanpa pesan error Port (TC-AC-DS-149 Expected b) diletakkan sebelum klik `[Submit]` karena popup tertutup sesudah Submit sukses; asersi "tidak ada SKU baru" TC-AC-DS-150 diasersi sebagai N + 2 di langkah akhir (S-12).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-043` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
