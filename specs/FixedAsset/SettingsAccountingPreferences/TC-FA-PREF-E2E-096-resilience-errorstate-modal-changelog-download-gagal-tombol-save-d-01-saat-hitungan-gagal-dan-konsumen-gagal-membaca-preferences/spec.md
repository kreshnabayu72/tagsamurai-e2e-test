---
id: TC-FA-PREF-E2E-096-resilience-errorstate-modal-changelog-download-gagal-tombol-save-d-01-saat-hitungan-gagal-dan-konsumen-gagal-membaca-preferences
title: "Resilience ErrorState: Modal Changelog Gagal, Download Gagal, Tombol Save D-01 saat Hitungan Gagal, dan Konsumen Gagal Membaca Preferences"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-296
  - TC-FA-PREF-361
  - TC-FA-PREF-598
  - TC-FA-PREF-508
coverage:
  web: automated
---

# Resilience ErrorState: Modal Changelog Gagal, Download Gagal, Tombol Save D-01 saat Hitungan Gagal, dan Konsumen Gagal Membaca Preferences

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; asersi memuat state backend pada TC-FA-PREF-598).
- Kelas harness: b (fault injection, 5xx).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-296 dan 361 dan PC-1 untuk TC-FA-PREF-598 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); Changelog Preferences berisi 9 entri contoh PB-C1 (tanggal format dd/MM/yy dan 24 jam, PB-1); Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang seri PC-1 dilakukan lewat langkah penghubung (langkah 15 dan 24).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk membalas permintaan data Changelog dengan 5xx lalu meneruskan permintaan berikutnya (langkah 1), permintaan Download dengan 500 (langkah 8), permintaan hitungan dampak dengan kegagalan (langkah 17), dan pembacaan Preferences oleh Depreciation Run dengan kegagalan (langkah 25); intercept dilepas segera setelah pemicu selesai (S-09).
- TC-FA-PREF-508 adalah TC `[DEFERRED]` (NC-09): modul konsumen Depreciation Run belum disusun, disediakan tim FE setelah modul tersedia, beserta data PC-16 dan PC-17 (Depreciation Run dengan aset penyusutan); blok ini ditaruh di akhir spec agar kegagalan modul konsumen tidak menutupi blok lain.
- State yang diubah spec: Default Capitalization Threshold tersimpan 10.000.000 pada langkah 22 (dipulihkan pada langkah 24 dan di hook `after`, tetap jalan bila spec gagal di tengah) dan intercept (dilepas pada langkah 13, 23, dan 28; intercept langkah 1 meneruskan permintaan berikutnya sehingga tidak perlu dilepas).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-296: Modal Changelog menampilkan ErrorState dan [Try Again] memuat ulang data

1. Pasang intercept agar respons data Changelog pertama gagal dengan 5xx lalu respons berikutnya diteruskan
2. Klik ikon View history di header tab Preferences
3. Verifikasi area tabel modal menampilkan ErrorState "Unable to load this data." dengan tombol [Try Again]
4. Klik [Try Again]
5. Verifikasi baris Changelog tampil pada tabel
6. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-361: Download gagal menampilkan toast error tanpa extension

7. Klik ikon View history di header tab Preferences
8. Pasang intercept agar permintaan Download dibalas 500
9. Klik ikon Download
10. Klik "Download as CSV"
11. Verifikasi toast "Error, failed to download Changelog-Preferences." tampil di kanan bawah layar
12. Verifikasi tidak ada berkas terunduh
13. Lepas intercept
14. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-598: Tombol Save pada dialog Save Changes tetap Enabled saat hitungan dampak gagal dimuat

15. Seed ulang Preferences ke nilai awal PC-1 (Asset Class PC-6) hingga tersimpan
16. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
17. Atur respons hitungan dampak menjadi gagal pada alat intercept jaringan
18. Klik [Save changes]
19. Verifikasi area pratinjau dampak menampilkan ErrorState "Unable to load this data." dengan tombol [Try Again]
20. Verifikasi tombol [Save] pada dialog Save Changes berstatus Enabled
21. Klik [Save]
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Lepas intercept hitungan dampak
24. Pulihkan Preferences ke nilai awal PC-1 lewat seed hingga tersimpan

### TC-FA-PREF-508: [DEFERRED] Konsumen menampilkan ErrorState saat pembacaan Preferences gagal

25. Pasang intercept agar pembacaan Preferences oleh Depreciation Run gagal
26. Buka Depreciation Run
27. Verifikasi ErrorState tampil pada konsumen yang bersangkutan
28. Lepas intercept pembacaan Preferences

## Notes

- Langkah penghubung (S-03, S-09): langkah 6 dan 14 (menutup modal), langkah 13, 23, dan 28 (melepas intercept), langkah 15 dan 24 (seed ulang seri PC-1), langkah 7 (membuka modal Changelog kembali sebagai precondition TC-FA-PREF-361; tidak ada Verifikasi). Layar Preferences dibuka hook `beforeEach` suite.
- Langkah 12 (absence "tidak ada berkas terunduh") diletakkan segera setelah pemicu dan memakai toast error pada langkah 11 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Langkah 17 memasang intercept sesudah form diubah dan sebelum [Save changes] mengikuti urutan langkah TC-FA-PREF-598.
- Temuan untuk QA:
  - TC-FA-PREF-598 Expected c menyebut toast sukses "setelah klik [Save]" tanpa posisi toast; Post Condition ("threshold tersimpan 10.000.000") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-508 hanya menyebut "konsumen yang bersangkutan" dan "area yang membutuhkan nilai Preferences" tanpa menamai area atau teks ErrorState; spec mengasersi ErrorState tampil pada Depreciation Run. Precondition TC tidak menyebut data Preferences yang dipakai; Post Condition ("Preferences tidak berubah") tidak punya langkah observasi dan tidak diasersi.
  - TC-FA-PREF-508 memakai seri fixture PC (PC-16, PC-17) dan modul konsumen belum ada.
  - TC-FA-PREF-296 dan 361 memakai seri PB sedangkan TC-FA-PREF-598 memakai seri PC; spec mengasumsikan nilai awal keduanya setara.
  - TC-FA-PREF-361 judul menyebut "tanpa extension" tanpa penjelasan di Expected; spec mengikuti teks toast dan tidak mengasersi nama berkas.
