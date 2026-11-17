---
id: TC-FA-PREF-E2E-093-resilience-save-timeout-input-dipertahankan-tombol-enabled-toast-connection-problem
title: "Resilience Save Timeout: Input Dipertahankan, Tombol Enabled, Toast Connection Problem"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-280
  - TC-FA-PREF-281
  - TC-FA-PREF-574
sourceRules: ["F-FAPREF-01.k17c", "ST-26", "RG-04", "F-FAPREF-01.k17a", "F-FAPREF-01.k17b", "ST-01", "F-FAPREF-01.k22b"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-01.k17c": [5, 10, 19, 24, 34, 38]
  "ST-26": [5, 19, 34]
  "RG-04": [5, 19, 34]
  "F-FAPREF-01.k17a": [6, 20, 35]
  "F-FAPREF-01.k17b": [7, 21, 36]
  "ST-01": 8
  "F-FAPREF-01.k22b": [9, 23, 37]
anchor: [22]
coverage:
  web: automated
---

# Resilience Save Timeout: Input Dipertahankan, Tombol Enabled, Toast Connection Problem

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Kelas harness: b (fault injection, timeout permintaan Save).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-280 dan 281 dan PC-1 untuk TC-FA-PREF-574 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; belum ada posting penyusutan, semua periode Open); akun Chart of Accounts PB-2; Asset Class IT Equipment, Vehicles, Furniture (PB-3) untuk dialog D-01 pada TC-FA-PREF-281. Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal PC-1 dilakukan lewat langkah penghubung (langkah 29).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata agar permintaan Save Preferences tidak pernah dibalas (timeout); intercept dilepas segera setelah pemicu selesai (langkah 11, 25, dan 39). Batas waktu permintaan klien tidak disebut TC; nilainya ditetapkan tim FE dan, bila di atas ±30 detik, dicapai dengan memajukan jam browser (bagian 6) dan dipulihkan sebelum langkah berikutnya.
- State yang diubah spec: form yang dirty dan jam browser bila dimajukan; dipulihkan pada langkah 12, 26, 27, 40, dan di hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-280: Save tanpa D-01 timeout

1. Pasang intercept agar permintaan Save Preferences tidak pernah dibalas (timeout)
2. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
3. Klik [Save changes]
4. Tunggu sampai batas waktu permintaan terlewati
5. Verifikasi toast error "Connection problem. Please try again." tampil di kanan bawah layar tanpa tombol aksi
6. Verifikasi form tetap terbuka tanpa pengalihan halaman
7. Verifikasi Select In-service Date Source masih menampilkan "Manual by Accounting"
8. Verifikasi [Save changes] berstatus Enabled kembali
9. Verifikasi tidak ada toast sukses
10. Verifikasi tidak ada toast "Error, failed to save accounting preferences."
11. Lepas intercept
12. Kembalikan Select In-service Date Source ke "Activation date"
13. Muat ulang halaman dengan F5

### TC-FA-PREF-281: Save dengan D-01 timeout

14. Pasang intercept agar permintaan Save Preferences tidak pernah dibalas (timeout)
15. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
16. Klik [Save changes]
17. Klik [Save] pada dialog D-01
18. Tunggu sampai batas waktu permintaan terlewati
19. Verifikasi toast error "Connection problem. Please try again." tampil di kanan bawah layar tanpa tombol aksi
20. Verifikasi dialog D-01 tetap terbuka
21. Verifikasi CurrencyInput Default Capitalization Threshold masih menampilkan "Rp 10.000.000,00"
22. Verifikasi tombol [Save] pada D-01 berstatus Enabled kembali
23. Verifikasi tidak ada toast sukses
24. Verifikasi tidak ada toast "Error, failed to save accounting preferences."
25. Lepas intercept
26. Klik [Cancel] pada dialog D-01
27. Klik [Cancel] pada form Preferences
28. Muat ulang halaman dengan F5

### TC-FA-PREF-574: Save tanpa dialog yang timeout mempertahankan form dan input

29. Seed ulang Preferences ke nilai awal PC-1 hingga tersimpan
30. Pasang intercept agar permintaan Save Preferences tidak pernah dibalas (timeout)
31. Pilih "Manual by Accounting" pada Select In-service Date Source
32. Klik [Save changes]
33. Tunggu sampai batas waktu permintaan terlewati
34. Verifikasi toast error "Connection problem. Please try again." tampil di kanan bawah layar tanpa tombol aksi
35. Verifikasi form tetap terbuka
36. Verifikasi Select In-service Date Source tetap "Manual by Accounting"
37. Verifikasi tidak ada toast sukses
38. Verifikasi tidak ada toast "Error, failed to save accounting preferences."
39. Lepas intercept
40. Kembalikan Select In-service Date Source ke "Activation date"
41. Muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03, S-09): langkah 11, 25, dan 39 (melepas intercept), langkah 12, 26, 27, dan 40 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi), langkah 13, 28, dan 41 (muat ulang agar toast dan state form bersih sebelum blok berikutnya), langkah 29 (seed ulang seri PC-1). Layar Preferences dibuka hook `beforeEach` suite.
- Langkah 9 dan 10, 23 dan 24, 37 dan 38 (absence toast) diletakkan segera setelah pemicu dan memakai toast "Connection problem. Please try again." pada langkah 5, 19, dan 34 sebagai anchor positif (bagian 8b butir 2 dan 11).
- Spec ini melewati sekitar 35 langkah (41 langkah nominal) karena tiga blok berdiri sendiri, semuanya kelas b (timeout Save) dengan pola seragam, tiap blok memulihkan form dan intercept sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-PREF-280, 281, dan 574 tidak menyebut batas waktu permintaan; spec memakai "Tunggu sampai batas waktu permintaan terlewati" dan nilai batasnya ditetapkan tim FE.
  - TC-FA-PREF-280 dan 281 Post Condition ("Preferences company belum berubah ... setelah muat ulang") dan TC-FA-PREF-574 Post Condition ("In-service Date Source tersimpan tetap Activation date") tidak punya langkah observasi di TC; tidak diasersi (S-01). Muat ulang pada langkah 13, 28, dan 41 hanya langkah penghubung.
  - TC-FA-PREF-574 memakai seri fixture PC sedangkan TC-FA-PREF-280 dan 281 memakai seri PB; spec mengasumsikan nilai awal keduanya setara.
