---
id: TC-FA-COA-E2E-082-download-lebih-dari-5000-baris
title: "Download Lebih dari 5.000 Baris: Loading Tampil sampai Berkas Siap"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-87
coverage:
  web: automated
---

# Download Lebih dari 5.000 Baris: Loading Tampil sampai Berkas Siap

## Prerequisites

- Mode: FE+BE.
- Kelas harness e (volume data lebih dari 5.000 baris). Suite berjalan serial (`parallel: false`).
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada client dengan lebih dari 5.000 akun, password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Kecocokan akun Total Control pada client ini perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data: client dengan lebih dari 5.000 akun, disediakan tim FE (seed atau API; kunci fixture ditetapkan tim FE). Data hanya dibaca; tidak ada yang diubah.
- Kemampuan teknis (disediakan tim FE): pengamatan berkas unduhan CSV pada browser.
- Seed client mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.

## Test Steps

### TC-FA-COA-87: Download lebih dari 5.000 baris

1. Klik icon `Download`
2. Klik `Download as CSV`
3. Verifikasi Loading screen tampil
4. Verifikasi berkas CSV terunduh langsung setelah siap
5. Verifikasi Loading screen tidak tampil lagi

## Notes

- Alasan jumlah langkah: 5 langkah, di bawah ambang.
- Langkah 1 membuka menu Download (langkah penghubung, S-03); TC hanya menyebut `Download as CSV`. Langkah 5 memastikan "tampil sampai berkas siap": Loading screen hilang setelah berkas terunduh yang menjadi anchor (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-COA-87 tidak menyebut identitas client dengan lebih dari 5.000 akun; fixture disediakan tim FE.
  - Expected a ("sampai berkas siap") tidak menyatakan batas waktu Loading; spec tidak menunggu durasi tertentu.
