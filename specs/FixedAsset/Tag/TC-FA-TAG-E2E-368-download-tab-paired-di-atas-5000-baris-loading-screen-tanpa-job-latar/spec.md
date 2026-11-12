---
id: TC-FA-TAG-E2E-368-download-tab-paired-di-atas-5000-baris-loading-screen-tanpa-job-latar
title: "Volume Data: Download Tab Paired di Atas 5.000 Baris Memakai Loading Screen Tanpa Job Latar"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1438
coverage:
  web: automated
---

# Volume Data: Download Tab Paired di Atas 5.000 Baris Memakai Loading Screen Tanpa Job Latar

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): fixture volume yang menyiapkan 5.001 aset ber-Tag dalam scope Total Control (seed lewat API, idempotent, tersedia pada hook `before`); penanganan unduhan file di browser dan pembaca berkas CSV (nama berkas dan format); pengamatan toast dan notifikasi in-app selama berkas disiapkan.
- Data: tab Paired memuat 5.001 aset ber-Tag dalam scope (jumlah baris yang cocok: 5.001). Aset volume bernama bersuffix `{runId}-368`.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus 5.001 aset volume dan Tag-nya lewat fixture backend. Spec ini hanya membaca data (aksi hanya membaca).
- State global: tidak ada. Suite serial (`parallel: false`).
- Nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik ikon Download
2. Klik `Download as CSV`
3. Verifikasi loading screen tampil sampai berkas siap
4. Verifikasi tidak ada toast (termasuk toast informasional persiapan berkas) dan tidak ada notifikasi in-app
5. Verifikasi berkas `Paired-TAGs` format CSV langsung terunduh setelah siap

## Notes

- Spec volume data (kelas e): ambang 5.001 baris dipakai karena tidak lazim dihasilkan seed rutin.
- Urutan langkah 3, 4, 5 mengikuti bagian 8b butir 5 dan 11: asersi state sementara (loading screen, absence toast dan notifikasi) diletakkan segera setelah pemicu (klik `Download as CSV`) dan sebelum asersi artefak (berkas terunduh). Pemicu pada langkah 2 menjadi anchor positif absence pada langkah 4 yang buktinya menyusul pada langkah 5.
- A-15: nilai literal Pre-setup (kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1438 mencantumkan Post Condition "Tidak ada job background, jendela ketersediaan berkas, maupun halaman riwayat Export" tanpa langkah observasi; tidak diasersi.
  - TC-FA-TAG-1438 menyebut "5.001 aset, disiapkan lewat seed atau API" tanpa cara pembersihannya; spec menulisnya sebagai kemampuan fixture backend yang disediakan tim FE/BE.
