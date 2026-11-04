---
id: TC-FA-PREF-E2E-094-resilience-pembangunan-ulang-periode-gagal-penulisan-log-gagal-dan-save-d-01-5xx-membatalkan-save
title: "Resilience: Pembangunan Ulang Periode Gagal, Penulisan Log Gagal, dan Save Dialog Save Changes 5xx Membatalkan Save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-288
  - TC-FA-PREF-392
  - TC-FA-PREF-573
coverage:
  web: automated
---

# Resilience: Pembangunan Ulang Periode Gagal, Penulisan Log Gagal, dan Save Dialog Save Changes 5xx Membatalkan Save

## Prerequisites

- Mode: FE+BE (intercept parsial dan fault-injection sisi server di atas backend nyata; asersi memuat state backend).
- Kelas harness: b (fault injection: kegagalan sisi server dan 5xx).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PB-1 untuk TC-FA-PREF-288 dan PC-1 untuk TC-FA-PREF-392 dan 573 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date; periode Mar 2026 sampai Dec 2026 berstatus Open); akun Chart of Accounts PB-2; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6; dialog D-01 menampilkan "2 asset classes use the default threshold."). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal PC-1 dilakukan lewat langkah penghubung (langkah 14).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE fault-injection untuk memaksa pembangunan ulang periode di Accounting Period gagal (langkah 1) dan untuk memaksa penulisan log pada penyimpanan Preferences gagal pada sesi ini (langkah 16), keduanya dilepas pada langkah 12 dan 28 dan di hook `after`; `Spectra.intercept()` di atas backend nyata untuk membalas permintaan Save Preferences dengan 500 (langkah 32), dilepas pada langkah 38; kemampuan baca BE jumlah baris Changelog Preferences (baseline sebelum aksi, bagian 8b butir 10 dan S-12); penanganan dialog `beforeunload` pada langkah 8 dan 22 (konfirmasi muat ulang saat form dirty) oleh hook suite, disediakan tim FE.
- State yang diubah spec: fault-injection sisi server, intercept, dan form yang dirty; dipulihkan pada langkah 12, 28, 38, 39, 40, dan di hook `after` (tetap jalan bila spec gagal di tengah). Preferences company tidak berubah karena setiap Save gagal.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-288: Save yang mengubah Fiscal Year Start batal seluruhnya saat pembangunan ulang periode gagal

1. Paksa pembangunan ulang periode di Accounting Period gagal pada sisi server lewat fixture BE fault-injection
2. Ubah Select Fiscal Year Start dari "January" menjadi "July"
3. Klik [Save changes]
4. Klik [Save] pada dialog D-01
5. Verifikasi toast gagal T-01 "Error, failed to save accounting preferences." tampil di kanan bawah layar
6. Verifikasi dialog D-01 tetap terbuka
7. Verifikasi Select Fiscal Year Start masih menampilkan "July"
8. Muat ulang halaman dengan F5
9. Verifikasi Select Fiscal Year Start menampilkan "January"
10. Buka daftar periode di modul Accounting Period
11. Verifikasi daftar periode akuntansi tetap Mar 2026 sampai Dec 2026 berstatus Open
12. Lepas fault-injection pembangunan ulang periode
13. Buka kembali Settings > Accounting > Preferences

### TC-FA-PREF-392: Kegagalan penulisan log membatalkan Save sehingga nilai tidak berubah

14. Seed ulang Preferences ke nilai awal PC-1 hingga tersimpan
15. Catat jumlah baris Changelog Preferences (baseline)
16. Paksa penulisan log pada penyimpanan Preferences gagal pada sisi server lewat fixture BE fault-injection untuk sesi ini
17. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
18. Klik [Save changes]
19. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
20. Klik [Save] pada dialog Save Changes
21. Tunggu aksi selesai
22. Muat ulang halaman dengan F5
23. Verifikasi Default Capitalization Threshold tetap "Rp 5.000.000,00"
24. Verifikasi Tab "Preferences" aktif
25. Klik ikon View history
26. Verifikasi modal Changelog: Preferences tidak memuat baris baru: jumlah baris sama dengan baseline langkah 15
27. Klik ikon [✕] di header modal Changelog
28. Lepas fault-injection penulisan log

### TC-FA-PREF-573: Save berdampak yang gagal 5xx mempertahankan dialog Save Changes dan input

29. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
30. Klik [Save changes]
31. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default threshold." lalu pertanyaan "Are you sure you want to save these changes?", tombol [Cancel] dan [Save]
32. Atur respons Save menjadi 500 pada alat intercept jaringan
33. Klik [Save] pada dialog Save Changes
34. Verifikasi toast "Error, failed to save accounting preferences." tampil tanpa tombol
35. Verifikasi dialog Save Changes tetap terbuka
36. Verifikasi form tetap terbuka
37. Verifikasi CurrencyInput Default Capitalization Threshold tetap "Rp 10.000.000,00"
38. Lepas intercept
39. Klik [Cancel] pada dialog Save Changes
40. Klik [Cancel] pada form Preferences
41. Muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03, S-09, S-14): langkah 12, 28, dan 38 (melepas fault-injection dan intercept segera setelah pemicu), langkah 13 (kembali ke modul asal setelah berpindah ke Accounting Period), langkah 14 (seed ulang seri PC-1), langkah 21 (Tunggu aksi selesai sebelum muat ulang), langkah 27 (menutup modal), langkah 39 dan 40 (mengembalikan form dirty ke nilai tersimpan, tanpa Verifikasi), dan langkah 41 (muat ulang agar toast bersih). Langkah 24 adalah anchor positif sebelum asersi absence pada popup yang dibuka sesudah F5 (R-21, bagian 8b butir 2) dan merupakan asersi tambahan di luar Expected TC; baseline langkah 15 menjadi anchor tambahan.
- Langkah 8 dan 22 memuat ulang halaman saat form dirty dengan dialog D-01 terbuka (langkah TC); `beforeunload` ditangani sesuai kemampuan di Prerequisites (S-08).
- Spec ini melewati sekitar 35 langkah (41 langkah nominal) karena tiga blok berdiri sendiri, semuanya kelas b dengan pemicu kegagalan berbeda, masing-masing memulihkan fault-injection, form, dan seed sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-PREF-288 Post Condition butir a, b, dan c ("Preferences company belum berubah", "Periode akuntansi tidak berubah", "Tidak ada entri log baru pada Changelog Preferences") dicakup sebagian oleh Expected c dan d; butir c tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-288 Expected d menyebut daftar periode "Mar 2026 sampai Dec 2026 berstatus Open" tanpa merinci sepuluh baris; spec mengasersinya sebagai satu daftar utuh.
  - TC-FA-PREF-392 tidak menyebut toast gagal pada Expected walau kegagalan penulisan log diperlakukan sebagai 5xx; spec tidak mengasersi toast. Kolom Dependensi dan Post Condition ("Nilai tersimpan dan log tidak berubah") dicakup oleh Expected b dan c.
  - TC-FA-PREF-392 langkah 5 ("amati baris teratas") hanya mensyaratkan tidak ada baris baru; spec mengasersi jumlah baris sama dengan baseline.
  - TC-FA-PREF-573 Post Condition ("threshold tersimpan tetap 5.000.000") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-FA-PREF-288 memakai seri fixture PB sedangkan TC-FA-PREF-392 dan 573 memakai seri PC; spec mengasumsikan nilai awal keduanya setara.
