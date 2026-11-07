---
id: TC-FA-LBL-E2E-074-volume-download-seluruh-baris-dan-di-atas-5000-baris
title: "Volume: Download Seluruh Baris dan di Atas 5.000 Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-265
  - TC-FA-LBL-277
coverage:
  web: automated
---

# Volume: Download Seluruh Baris dan di Atas 5.000 Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Volume (Pre-setup #10), `Fixture.assetLabeling.totalControlVolume` (email mengikuti pola Pre-setup #1 untuk Company Volume; ditetapkan tim FE), password `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun ganti: Total Control Company Export (Pre-setup #24), `Fixture.assetLabeling.totalControlExport` (email mengikuti pola Pre-setup #1 untuk Company Export; ditetapkan tim FE), password `Spectra.env.FA_TC_EXPORT_PASSWORD`; dipakai pada langkah 5 sampai 7. Kedua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #10: Company Volume dengan 120 label `Project Tag 1` sampai `Project Tag 120` (hanya dibaca); Pre-setup #24: Company Export dengan 5.001 label (seed API, hanya dibaca). Ukuran halaman tabel default 10 baris.
- Jendela tunggu notifikasi in-app: 5 detik tanpa memuat ulang halaman (pilihan spec, bukan nilai TC atau PRD; TC tidak menyebut durasi).
- Kemampuan teknis (disediakan tim FE): direktori unduhan uji untuk menangkap berkas dan pembaca CSV/XLSX (nama berkas, header, dan jumlah baris).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-LBL-265: Download tanpa Search atau Filter mengekspor seluruh baris, bukan satu halaman

1. Klik icon Download
2. Klik `Download as CSV`
3. Verifikasi halaman aktif tabel memuat 10 baris
4. Verifikasi berkas `Labels.csv` memuat baris header dan seluruh 120 label

### TC-FA-LBL-277: Download di atas 5.000 baris memakai loading screen tanpa job background

5. Ganti akun: logout dari Total Control Company Volume
6. Login sebagai Total Control Company Export (`Fixture.assetLabeling.totalControlExport`, password `Spectra.env.FA_TC_EXPORT_PASSWORD`)
7. Buka Fixed Asset > Settings > Asset Master > tab Labels
8. Klik icon Download
9. Klik `Download as XLSX`
10. Verifikasi loading screen tampil sampai berkas siap
11. Verifikasi berkas terunduh langsung memuat seluruh 5.001 label
12. Tunggu 5 detik tanpa memuat ulang halaman
13. Buka Dropdown Panel notifikasi in-app
14. Verifikasi Dropdown Panel notifikasi in-app termuat
15. Verifikasi tidak ada notifikasi in-app
16. Verifikasi tidak ada job background (tidak ada indikator job atau antrean unduhan di UI)

## Notes

- Mode: FE+BE (backend nyata; berkas diunduh dan dibaca). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah 5 sampai 7 adalah Ganti akun eksplisit (S-07); hook `after` suite mengembalikan sesi ke akun default suite.
- Asersi absence notifikasi in-app (langkah 15) diletakkan sesudah Verifikasi loading screen (langkah 10), Verifikasi berkas terunduh (langkah 11), langkah penghubung tunggu 5 detik tanpa memuat ulang halaman (langkah 12, S-03) dan pembukaan Dropdown Panel notifikasi (langkah 13); Verifikasi Dropdown Panel termuat (langkah 14) menjadi anchor positif bahwa surface notifikasi sudah tampil, sehingga absence bukan lulus semu (bagian 8b butir 2 dan 11, bagian 6).
- Temuan untuk QA:
  - TC-FA-LBL-277 Expected "tidak ada job background" tidak punya mekanisme cek di TC; spec mengasersi tidak ada indikator job atau antrean unduhan di UI.
  - TC-FA-LBL-265 menyebut "walau halaman aktif hanya 10 baris"; spec mengasersi 10 baris pada halaman aktif sebagai bagian dari Expected itu.
