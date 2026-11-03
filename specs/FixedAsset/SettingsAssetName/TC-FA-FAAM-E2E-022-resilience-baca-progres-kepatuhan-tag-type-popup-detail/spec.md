---
id: TC-FA-FAAM-E2E-022-resilience-baca-progres-kepatuhan-tag-type-popup-detail
title: "Resilience Baca: Baris Progres Kepatuhan TAG Type Tidak Tampil Sebagian Saat Popup Detail Loading atau Gagal Dimuat"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-837
coverage:
  web: automated
---

# Resilience Baca: Baris Progres Kepatuhan TAG Type Tidak Tampil Sebagian Saat Popup Detail Loading atau Gagal Dimuat

## Prerequisites

- Mode: FE+BE (backend nyata). Respons data Detail ditahan dan dipaksa gagal lewat `Spectra.intercept()` di atas backend nyata (intercept parsial, bukan mock seluruh API); asersi akhir (baris progres `33 / 40`) bergantung pada data server.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.excavator`): `Excavator 20 Ton` (#38) TAG Type `RFID`, 40 aset `Active` dalam scope client (Group `Plant A` 20 aset dan Group `Plant B` 20 aset): 33 aset ber-Tag `Paired` sesuai TAG Type, 2 `Not Paired Yet`, 5 aset Non-standard ber-Tag `QR`.
- Kemampuan teknis: `Spectra.intercept()` untuk menahan dan memaksa gagal respons data Detail (langkah 2 dan 8). Intercept dilepas segera sesudah pemicu (langkah 6 dan 13, S-09); hook `after` melepas intercept yang tersisa.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-837: Baris progres kepatuhan TAG Type tidak tampil sebagian saat Popup Detail Loading atau gagal dimuat

1. Ketik Search `Excavator 20 Ton`, tekan Enter
2. Tunda respons data Detail lewat intercept
3. Klik nama `Excavator 20 Ton`
4. Verifikasi skeleton loader tampil selama menunggu
5. Verifikasi tidak ada teks progres sementara (tanpa `0 / 0` maupun `0 / 40`)
6. Lepas intercept tunda dan tunggu respons Detail diterima
7. Klik `[✕]` pada Popup Detail
8. Paksa respons data Detail gagal lewat intercept
9. Klik nama `Excavator 20 Ton`
10. Verifikasi Alert `Unable to load this data.` dengan `[Try Again]` tampil inline
11. Verifikasi header `Asset Name Detail` dan icon `[✕]` tetap
12. Verifikasi tidak ada baris progres
13. Lepas intercept respons data Detail
14. Klik `[Try Again]`
15. Verifikasi Identitas Utama tampil
16. Verifikasi baris progres `33 / 40 assets match the TAG type` tampil
17. Klik `[✕]` pada Popup Detail

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. TC-FA-FAAM-837 berada di spec ini dan spec 017 memuat resilience baca lainnya (list, tab Total Assets, Changelog, baca setelah tulis).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 6 (melepas intercept tunda segera, S-09) dan 13 (melepas intercept gagal), langkah 7 (menutup popup sebelum fase kedua), langkah 14 (klik `[Try Again]` sesuai Langkah uji), langkah 17 (menutup popup).
- Langkah 5 (absence teks progres sementara) ditulis segera setelah pemicu dan memakai skeleton loader (langkah 4) sebagai anchor positif; langkah 12 (absence baris progres) memakai Alert pada langkah 10 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Langkah 6 dan 7 memisahkan fase Loading dari fase gagal sehingga dua fase dapat diamati pada satu spec; tanpa pemisahan, popup fase Loading masih terbuka saat fase gagal dimulai.
- Temuan untuk QA:
  - TC-837 Langkah 1 menunda respons tanpa menyebut durasi atau kapan dilepas; spec melepas intercept tunda segera sesudah asersi Loading (langkah 6) dan menutup popup (langkah 7).
  - TC-837 Langkah 2 dan 3 tidak menyebut endpoint yang di-intercept; spec tidak menulis endpoint karangan.
  - TC-837 Expected a menyebut teks progres sementara `0 / 0` dan `0 / 40`, sedangkan teks progres final memakai format `33 / 40 assets match the TAG type`; spec mengasersi keduanya sesuai tulisan TC.
