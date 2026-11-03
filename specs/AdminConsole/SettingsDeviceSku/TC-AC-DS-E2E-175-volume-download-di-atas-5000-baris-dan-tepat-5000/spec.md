---
id: TC-AC-DS-E2E-175-volume-download-di-atas-5000-baris-dan-tepat-5000
title: "Volume Data: Download 5.001 Baris Memakai Loading Screen dan Tepat 5.000 Baris Tanpa Loading"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-378
  - TC-AC-DS-379
coverage:
  web: automated
---

# Volume Data: Download 5.001 Baris Memakai Loading Screen dan Tepat 5.000 Baris Tanpa Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal Uji Download Besar (5.001 SKU): `totalControlBig_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_BIG_PASSWORD` (Pre-setup #22). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Akun ganti akun (langkah 8): Total Control Principal Uji Download 5000 (tepat 5.000 SKU): `totalControlBig5k_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_BIG5K_PASSWORD` (Pre-setup #23).
- Data Pre-setup: General Settings (#35); Principal `Principal Uji Download Besar` dengan 5.001 SKU hasil seed lewat API (`BIG-0001` dan seterusnya; Asset TAG; stok 0) (#38) dan Principal Uji Download 5000 dengan tepat 5.000 SKU (`FIV-0001` dan seterusnya; Pre-setup #23). Fixture rancangan #38 dan entitas #22, #23 belum terverifikasi ada di environment.
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan (`Device-SKU.csv`) untuk memeriksa jumlah baris data; mengamati loading screen dan toast sementara.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-378: Download di atas 5.000 baris memakai loading screen lalu file langsung terunduh

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi loading screen tampil sampai berkas siap
4. Verifikasi tidak ada notifikasi in-app
5. Verifikasi tidak ada toast sukses
6. Verifikasi `Device-SKU.csv` langsung terunduh berisi 5.001 baris data
7. Verifikasi tidak ada job background

### TC-AC-DS-379: Download tepat 5.000 baris tidak memakai loading screen

8. Logout lalu login sebagai Total Control Principal Uji Download 5000 (`totalControlBig5k_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_BIG5K_PASSWORD`) dan buka halaman `Settings > Device > Device SKU`
9. Klik ikon Download
10. Klik `Download as CSV`
11. Verifikasi tidak ada loading screen
12. Verifikasi tidak ada toast
13. Verifikasi `Device-SKU.csv` terunduh langsung berisi 5.000 baris data

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 8 (ganti akun eksplisit; sesi dikembalikan ke akun default suite di hook `after`).
- Absence notifikasi in-app dan toast sukses (langkah 4 dan 5), loading screen (langkah 11), dan toast (langkah 12) diasersi tepat sesudah klik `Download as CSV` dan sebelum asersi berkas, dengan berkas terunduh (langkah 6 dan 13) sebagai anchor positif yang diverifikasi menyusul (8b butir 11). Absence job background (langkah 7) diasersi sesudah berkas terunduh karena bukan state sementara.
- Temuan untuk QA:
  - Expected 378 butir b ("Tidak ada job background, tidak ada notifikasi in-app, dan tidak ada toast sukses") tidak punya langkah observasi job background di TC; spec mengasersi notifikasi in-app dan toast sukses sebagai absence tepat sesudah klik `Download as CSV` dan job background sebagai absence sesudah berkas terunduh. TC 379 Expected butir a menyebut "tanpa loading screen" yang hanya teramati sesaat; asersi ditempatkan sebelum berkas terunduh.
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
