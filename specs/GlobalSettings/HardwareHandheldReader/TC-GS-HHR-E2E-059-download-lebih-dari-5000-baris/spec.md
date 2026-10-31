---
id: TC-GS-HHR-E2E-059-download-lebih-dari-5000-baris
title: "Download Daftar Reader Lebih dari 5.000 Baris pada Client Large: Loading Screen dan Unduhan Langsung"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-GS-HHR-316
coverage:
  web: automated
---

# Download Daftar Reader Lebih dari 5.000 Baris pada Client Large: Loading Screen dan Unduhan Langsung

## Prerequisites

- Mode: FE+BE (backend nyata, dengan intercept parsial untuk menahan respons unduh). Kelas harness volume data khusus (konvensi bagian 3, prinsip 13e): data lebih dari 5.000 baris.
- Akun aktor hook `before`: Total Control Client Large, `totalControl_automated_{namaClient}@qwertysystem.net` dengan namaClient Client Large; email persisnya tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE. Login sekali di hook `before` dengan `Spectra.env.GS_CLIENTLARGE_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` oleh pemilik suite). Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_CLIENTLARGE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader dengan Search dan Filter kosong.
- Data: Client Large memiliki lebih dari 5.000 reader (Tabel Data Uji Pre-setup TC; ukuran data disediakan tim FE). Spec hanya membaca daftar dan tidak mengubah data.
- Kemampuan teknis: menangkap berkas unduhan browser ke direktori bersih supaya nama berkas tidak tertimpa; menahan dan melepas respons permintaan unduh lewat intercept jaringan hanya untuk mengamati state loading screen (bukan kegagalan; intercept dilepas pada langkah 6 dan tidak ada respons yang dipaksa error). Jumlah notifikasi in-app dibaca dari Notification Center, toast dan indikator job latar belakang diamati pada halaman.
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun Client Large; spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan: tidak ada state yang diubah selain intercept (dilepas pada langkah 6; hook `after` melepasnya sebagai cadangan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-HHR-316: Download lebih dari 5.000 baris

1. Catat jumlah notifikasi in-app milik akun aktor sebagai baseline
2. Tahan respons permintaan unduh (intercept) supaya loading screen dapat diamati
3. Klik ikon Download
4. Klik `Download as CSV`
5. Verifikasi loading screen tampil selama respons ditahan
6. Lepas tahanan respons permintaan unduh
7. Verifikasi file `Handheld-Reader-List.csv` langsung terunduh
8. Verifikasi tidak ada toast
9. Verifikasi tidak ada toast informasional `Preparing…`
10. Verifikasi tidak ada indikator job latar belakang pada halaman
11. Buka Notification Center
12. Verifikasi jumlah notifikasi in-app sama dengan baseline (tidak ada notifikasi baru)

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`, section 4a-6. Kelas volume data khusus (prinsip 13e): Client Large (lebih dari 5.000 reader) dipisah dari Download biasa (spec 057).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec hanya memuat satu TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): mencatat baseline jumlah notifikasi (langkah 1); menahan dan melepas respons unduh (langkah 2 dan 6); membuka Notification Center (langkah 11). Menahan respons hanya untuk mengamati loading screen dan bukan fault injection (prinsip 13b).
- Respons unduh ditahan selama loading screen diamati, sehingga toast hasil belum dapat muncul. Asersi absence (toast, toast `Preparing…`, indikator job latar belakang) ditulis sesudah langkah "Lepas tahanan respons" dan sesudah `Verifikasi` berkas terunduh (langkah 7), yang menjadi anchor positif bahwa respons sudah diproses (konvensi bagian 8b butir 11, pengecualian respons ditahan).
- Pembagian TC lintas spec: Download biasa (TC-GS-HHR-306 sampai 311, 313) di spec 057; isi berkas (TC-GS-HHR-312, 314) di spec 058; kegagalan Download (TC-GS-HHR-315) di spec 028.
- Temuan untuk QA:
  - TC-GS-HHR-316: email akun Client Large tidak tertulis di Pre-setup TC (hanya pola `totalControl_automated_{namaClient}@qwertysystem.net`) dan env var passwordnya belum terdaftar; spec memakai `GS_CLIENTLARGE_TC_PASSWORD` (env baru).
  - TC-GS-HHR-316: Langkah 2 ("Aktifkan penundaan respons pada request unduhan") tidak menyebut endpoint unduh; target intercept disediakan tim FE.
  - TC-GS-HHR-316: Expected tidak menyebut isi atau jumlah baris berkas; spec tidak mengasersi isi berkas (isi berkas diuji di spec 058 pada Client A).
  - Post Condition TC-GS-HHR-316 `-`; tidak ada yang diasersi.
