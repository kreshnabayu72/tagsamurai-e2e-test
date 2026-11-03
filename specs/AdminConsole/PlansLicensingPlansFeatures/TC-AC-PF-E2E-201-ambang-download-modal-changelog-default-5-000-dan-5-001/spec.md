---
id: TC-AC-PF-E2E-201-ambang-download-modal-changelog-default-5-000-dan-5-001
title: Ambang Download modal Changelog Default pada 5.000 dan 5.001 entri
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-601
  - TC-AC-PF-602
coverage:
  web: automated
---

# Ambang Download modal Changelog Default pada 5.000 dan 5.001 entri

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup (volume 5.000 dan 5.001 baris, kelas e): Dataset Log D5000 (modal Changelog Default Principal dengan 5.000 entri) untuk blok TC-AC-PF-601; Dataset Log D5001 (5.001 entri) untuk blok TC-AC-PF-602. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Default Principal tepat sama dengan Dataset Log D5000 di hook `before`, menggantinya dengan Dataset Log D5001 sebagai langkah penghubung antar blok, dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog volume besar; pembaca berkas CSV yang terunduh (jumlah baris data); pengamat indikator loading (spinner biasa dan loading screen); sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### 5.000 entri (TC-AC-PF-601)

1. Klik ikon Changelog pada toolbar tab Default
2. Klik ikon Download
3. Pilih `Download as CSV`
4. Verifikasi indikator selama berkas disiapkan hanya spinner biasa
5. Verifikasi tidak ada job background, toast informasional, notifikasi in-app, maupun jendela ketersediaan berkas
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas terunduh memuat 5.000 baris data

### 5.001 entri (TC-AC-PF-602)

8. Tutup modal dengan icon (X)
9. Ganti Dataset Log D5000 dengan Dataset Log D5001 lewat fixture BE, lalu tekan F5
10. Klik ikon Changelog pada toolbar tab Default
11. Klik ikon Download
12. Pilih `Download as CSV`
13. Verifikasi loading screen tampil sampai berkas siap
14. Verifikasi tidak ada job background, toast informasional, notifikasi in-app, maupun jendela ketersediaan berkas
15. Verifikasi tidak ada toast sukses
16. Verifikasi berkas terunduh memuat 5.001 baris data

## Notes

- Langkah penghubung (S-03): langkah 8 dan 9 menutup modal dan mengganti dataset sebelum blok kedua.
- Verifikasi absence pada langkah 5, 6, 14, dan 15 diletakkan segera setelah pemicu Download dan sebelum Verifikasi berkas (bagian 8b butir 11); pemicu Download menjadi anchor positif yang buktinya menyusul pada Verifikasi berkas langkah 7 dan 16.
- Kelas e: kedua blok memakai volume 5.000 dan 5.001 baris pada topik yang sama (ambang Download sinkron versus loading screen).
- Temuan untuk QA:
  - TC-AC-PF-601 dan TC-AC-PF-602 tidak menyatakan cara mengamati "spinner biasa" dibanding "loading screen"; spec mengandalkan pengamat indikator yang disediakan tim FE/BE tanpa selector karangan.
  - TC menetapkan 5.000 dan 5.001 entri sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
