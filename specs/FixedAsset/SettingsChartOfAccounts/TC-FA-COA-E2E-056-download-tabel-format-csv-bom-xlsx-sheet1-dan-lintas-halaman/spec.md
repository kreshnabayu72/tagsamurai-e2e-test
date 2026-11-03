---
id: TC-FA-COA-E2E-056-download-tabel-format-csv-bom-xlsx-sheet1-dan-lintas-halaman
title: "Download Tabel: Format CSV BOM, XLSX Sheet1, dan Lintas Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-221
  - TC-FA-COA-222
  - TC-FA-COA-358
coverage:
  web: automated
---

# Download Tabel: Format CSV BOM, XLSX Sheet1, dan Lintas Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Satu ganti akun eksplisit di langkah 8 dan 9 (TC-358, client uji P110); hook `after` mengembalikan sesi ke akun default suite.
- Akun client uji P110 (tabel 25 akun, plan Growth, akun P1 termasuk): `totalControlFixedAsset_automated_{namaCompanyP110}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`; disediakan tim FE/BE (lihat Seed dan pemulihan di `suite.md`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Akun Pre-setup client default (hanya dibaca dan tidak diubah; kunci fixture `Fixture.settingsChartOfAccounts.<kunci>` ditetapkan tim FE): P1 (`5-6001`, Account Name tanpa koma dan tanda kutip), P42 (satu akun dengan Account Name memuat koma dan tanda kutip ganda; asumsi pre-setup, bukan data PRD), dan P2 sampai P5.
- Akun P1 di client P110 terakhir diubah user A (Pre-setup P40; asumsi pre-setup).
- General Settings client P110 untuk TC-358: Date Format `dd/MM/yy` dan Time Format 24 jam; mekanisme mengubah dan mengembalikannya disediakan tim FE/BE (langkah 10 dan 24).
- Kemampuan teknis: membaca byte awal dan isi berkas CSV dan daftar sheet berkas XLSX yang terunduh; disediakan tim FE.
- State yang diubah spec: Date Format dan Time Format General Settings client P110 (dikembalikan pada langkah 24 dan oleh hook `after` sebagai cadangan) dan konfigurasi kolom client P110 (Modified By dan Last Updated ditampilkan pada langkah 11 sampai 13, dipulihkan pada langkah 21 sampai 23). Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor client default dan client P110 (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-221: CSV UTF-8 BOM, pemisah koma, escaping

1. Klik ikon Download, lalu pilih `Download as CSV`
2. Verifikasi berkas CSV berenkode UTF-8 dengan BOM
3. Verifikasi berkas CSV memakai koma sebagai pemisah
4. Verifikasi Account Name P42 dibungkus tanda kutip ganda dan tanda kutip di dalamnya digandakan
5. Verifikasi Account Name P1 (tanpa koma dan tanda kutip) tidak dibungkus tanda kutip

### TC-FA-COA-222: XLSX satu sheet Sheet1

6. Klik ikon Download, lalu pilih `Download as XLSX`
7. Verifikasi berkas XLSX memuat tepat satu sheet bernama `Sheet1`

### TC-FA-COA-358: CSV lintas halaman pada client P110

8. Klik Logout dari akun aktor default
9. Login sebagai Total Control client uji P110, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
10. Atur Date Format `dd/MM/yy` dan Time Format 24 jam pada General Settings client P110, lalu muat ulang halaman
11. Klik header Actions ⋯ > `Setup Column...`
12. Centang kolom Modified By dan Last Updated
13. Klik `[Save]`
14. Verifikasi halaman 1 menampilkan 10 baris
15. Klik ikon Download, lalu pilih `Download as CSV`
16. Verifikasi tidak ada toast sukses
17. Verifikasi berkas memuat 25 baris data (bukan 10 baris halaman tampil)
18. Verifikasi kolom Modified By ditulis nama lengkap utuh user (baris P1 berisi nama lengkap user A), bukan format `[First Name] [Last Initial]`
19. Verifikasi kolom Last Updated mengikuti Date Format dan Time Format General Settings
20. Verifikasi kolom Used By ditulis angka (mis. `0`)
21. Klik header Actions ⋯ > `Setup Column...`
22. Hapus centang kolom Modified By dan Last Updated
23. Klik `[Save]`
24. Kembalikan Date Format dan Time Format General Settings client P110 ke nilai awal

## Notes

- P-10: TC-221, TC-222, dan TC-358 sebagian besar mengasersi isi berkas (kelas f) pada alur tombol Download; TC-358 juga mengasersi 10 baris halaman (langkah 14) dan tidak adanya toast (langkah 16) sebagai klausa UI, ditaruh sebelum klausa isi berkas. Spec ini memuat TC yang objek ujinya isi berkas bersama TC UI sejenis pada tombol dan tabel yang sama, sehingga satu spec dengan pengecualian P-10; `Verifikasi` isi berkas satu per klausa.
- Asersi absence toast pada langkah 16 diletakkan segera setelah pemicu sebelum asersi berkas; berkas terunduh yang diamati pada langkah 17 menjadi bukti positif bahwa respons sudah diproses (8b.11).
- Langkah penghubung (S-03): langkah 8 dan 9 (ganti akun ke client P110), langkah 10 (mengatur General Settings, precondition e TC-358), langkah 11 sampai 13 (menampilkan kolom, langkah TC-358), langkah 21 sampai 24 (pemulihan Setup Column eksplisit, R-24 dan 8b.13, dan General Settings).
- Pembagian kelas harness: tidak ada TC kelas lain; ganti akun pada langkah 8 dan 9 bukan konteks kedua.
- Temuan untuk QA:
  - TC-221 langkah 1 meminta "Search akun P42 dan P1 (tampilkan keduanya)" tanpa menyebut nilai Search yang menampilkan keduanya; spec mengunduh tanpa Search sehingga berkas memuat seluruh akun, termasuk P42 dan P1.
  - TC-358 menyebut client uji P110 tanpa email akun aktornya; spec memakai `totalControlFixedAsset_automated_{namaCompanyP110}@qwertysystem.net` dan `FA_TC_PASSWORD` sebagai asumsi yang perlu dikonfirmasi tim FE.
  - TC-358 tidak menyebut nilai Timezone; asersi Last Updated hanya mengikuti Date Format dan Time Format.
  - P42 adalah asumsi pre-setup, bukan data PRD.
