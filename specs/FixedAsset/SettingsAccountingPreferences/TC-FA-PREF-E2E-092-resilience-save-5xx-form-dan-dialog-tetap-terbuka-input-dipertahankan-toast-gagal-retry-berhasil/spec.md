---
id: TC-FA-PREF-E2E-092-resilience-save-5xx-form-dan-dialog-tetap-terbuka-input-dipertahankan-toast-gagal-retry-berhasil
title: "Resilience Save 5xx: Form dan Dialog D-01 Tetap Terbuka, Input Dipertahankan, Toast Gagal Tampil, Retry Berhasil"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-278
  - TC-FA-PREF-279
  - TC-FA-PREF-282
coverage:
  web: automated
---

# Resilience Save 5xx: Form dan Dialog D-01 Tetap Terbuka, Input Dipertahankan, Toast Gagal Tampil, Retry Berhasil

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; asersi memuat state backend pada retry TC-FA-PREF-282).
- Kelas harness: b (fault injection, HTTP 5xx).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); akun Chart of Accounts PB-2; Asset Class IT Equipment, Vehicles, Furniture (PB-3) untuk dialog D-01 pada TC-FA-PREF-279. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal dilakukan lewat langkah penghubung (langkah 34).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk membalas permintaan Save Preferences dengan 500 (TC-FA-PREF-278 dan 279) atau membalas 500 pada permintaan pertama lalu meneruskan permintaan berikutnya ke server (TC-FA-PREF-282); intercept dilepas segera setelah pemicu selesai (langkah 9, 21, dan 33).
- State yang diubah spec: Preferences company (In-service Date Source pada TC-FA-PREF-282) dan form yang dirty; dipulihkan pada langkah 10, 22, 23, dan 34 dan di hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-278: Save tanpa D-01 gagal dengan 5xx

1. Pasang intercept agar permintaan Save Preferences dibalas 500
2. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
3. Klik [Save changes]
4. Verifikasi toast "Error, failed to save accounting preferences." tampil di kanan bawah layar tanpa tombol aksi dan tidak hilang otomatis
5. Verifikasi form tetap terbuka tanpa pengalihan halaman
6. Verifikasi Select In-service Date Source masih menampilkan "Manual by Accounting"
7. Verifikasi [Save changes] berstatus Enabled kembali
8. Verifikasi tidak ada toast sukses
9. Lepas intercept
10. Kembalikan Select In-service Date Source ke "Activation date"
11. Muat ulang halaman dengan F5

### TC-FA-PREF-279: Save dengan D-01 gagal dengan 5xx

12. Pasang intercept agar permintaan Save Preferences dibalas 500
13. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
14. Klik [Save changes]
15. Klik [Save] pada dialog D-01
16. Verifikasi toast "Error, failed to save accounting preferences." tampil di kanan bawah layar tanpa tombol aksi
17. Verifikasi dialog D-01 tetap terbuka
18. Verifikasi CurrencyInput Default Capitalization Threshold masih menampilkan "Rp 10.000.000,00"
19. Verifikasi tombol [Save] pada D-01 berstatus Enabled kembali
20. Verifikasi tidak ada toast sukses
21. Lepas intercept
22. Klik [Cancel] pada dialog D-01
23. Klik [Cancel] pada form Preferences
24. Muat ulang halaman dengan F5

### TC-FA-PREF-282: Retry manual dengan Save ulang berhasil setelah Save gagal 5xx

25. Pasang intercept agar permintaan Save Preferences pertama dibalas 500 dan permintaan berikutnya diteruskan ke server
26. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
27. Klik [Save changes]
28. Verifikasi toast "Error, failed to save accounting preferences." tampil di kanan bawah layar
29. Klik [Save changes] sekali lagi
30. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
31. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
32. Verifikasi [Save changes] dan [Cancel] berstatus Disabled karena form pristine
33. Lepas intercept
34. Pulihkan Preferences ke nilai awal PB-1 lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03, S-09): langkah 9, 21, dan 33 (melepas intercept segera setelah pemicu), langkah 10, 22, dan 23 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi), langkah 11 dan 24 (muat ulang agar toast persisten dan state form bersih sebelum blok berikutnya), langkah 34 (memulihkan Preferences). Layar Preferences dibuka hook `beforeEach` suite.
- Langkah 8 dan 20 (absence toast sukses) diletakkan segera setelah pemicu dan memakai toast error pada langkah 4 dan 16 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Pemicu 5xx dipasang lewat intercept di atas backend nyata (bagian 6); karena Expected TC-FA-PREF-282 memuat hasil Save sukses pada server nyata, spec ini `FE+BE`, bukan `mock`.
- Temuan untuk QA:
  - TC-FA-PREF-278 dan 279 Post Condition butir a ("Preferences company belum berubah ... setelah muat ulang") dan butir b ("Tidak ada entri log baru pada Changelog Preferences") tidak punya langkah observasi di TC; keduanya tidak diasersi (S-01). Muat ulang pada langkah 11 dan 24 hanya langkah penghubung.
  - TC-FA-PREF-278 Expected a menyebut toast "tidak hilang otomatis" tanpa jeda amat; spec mengasersinya sebagai sifat toast persisten pada langkah 4 tanpa menunggu waktu nyata.
  - TC-FA-PREF-279 tidak menyebut apakah dialog D-01 menampilkan ErrorState pratinjau; spec tidak mengasersinya.
  - TC-FA-PREF-282 Expected a tidak menyebut apakah toast gagal hilang sebelum toast sukses tampil; spec mengasersi teks tiap toast pada langkah 28 dan 30.
