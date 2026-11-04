---
id: TC-FA-LBL-E2E-003-create-label-validasi-kode-hex-color-picker
title: "Create Label: validasi kode hex di Color Picker Overlay"
priority: High
caseType: Negative
status: draft
sourceRules:
  - E-FALB-28
  - F-FALB-06.k1
  - F-FALB-06.k3
  - FALB-LOGIC-03c
  - FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber
coverage:
  web: automated
---

# Create Label: validasi kode hex di Color Picker Overlay

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-10` (kode valid huruf kecil, langkah 35), `DU-11` (nama label uji, bersuffix `{runId}-003`), `DU-12` (kode hex tidak valid, satu nilai per kategori).
- Kategori kode di kolom Hex yang dipakai langkah (nilai persis ada di `DU-12`):

| Kategori | Dipakai di langkah |
|---|---|
| kurang dari 6 digit | 4 |
| lebih dari 6 digit | 17 |
| berisi karakter non-heksadesimal | 26 |
| 6 digit tanpa awalan `#` | 41 |

- Spec ini tidak pernah menekan `[Submit]` (tombol Disabled selama kode tidak valid) dan menutup form tanpa menyimpan (langkah 47 sampai 49), sehingga tidak membuat data dan tidak butuh cleanup.

## Test Steps

1. Klik `[+ Label]`
2. Ketik Label Name `DU-11`
3. Klik Swatch Trigger pada field Color, catat warna Swatch Trigger dan Live Preview saat ini sebagai warna valid terakhir

### FALB-LOGIC-03c: Input hex manual diizinkan dan divalidasi real-time di UI

4. Ketik di kolom Hex kode kurang dari 6 digit (`DU-12`)
5. Verifikasi kolom Hex menampilkan kode yang diketik
6. Verifikasi inline error `Invalid color format` tampil langsung saat kode diketik

### E-FALB-28: Kode hex tidak valid di kolom Hex

7. Verifikasi inline error `Invalid color format` tampil di dalam Color Picker Overlay
8. Verifikasi Swatch Trigger dan Live Preview tetap memakai warna valid terakhir
9. Verifikasi tombol `[Submit]` Disabled
10. Tekan Esc
11. Verifikasi Modal Create Label masih tampil
12. Verifikasi tombol `[Submit]` Enabled
13. Verifikasi Swatch Trigger dan Live Preview memakai warna valid terakhir
14. Klik Swatch Trigger pada field Color
15. Verifikasi kolom Hex kembali berisi warna valid terakhir
16. Verifikasi inline error `Invalid color format` tidak tampil
17. Ketik di kolom Hex kode lebih dari 6 digit (`DU-12`)
18. Verifikasi inline error `Invalid color format` tampil di dalam Color Picker Overlay
19. Klik Swatch Trigger pada field Color
20. Verifikasi Modal Create Label masih tampil
21. Verifikasi tombol `[Submit]` Enabled
22. Verifikasi Swatch Trigger dan Live Preview memakai warna valid terakhir
23. Klik Swatch Trigger pada field Color
24. Verifikasi kolom Hex kembali berisi warna valid terakhir
25. Verifikasi inline error `Invalid color format` tidak tampil
26. Ketik di kolom Hex kode berisi karakter non-heksadesimal (`DU-12`)
27. Verifikasi inline error `Invalid color format` tampil di dalam Color Picker Overlay
28. Klik pada area Modal Create Label di luar Color Picker Overlay
29. Verifikasi Modal Create Label masih tampil
30. Verifikasi tombol `[Submit]` Enabled
31. Verifikasi Swatch Trigger dan Live Preview memakai warna valid terakhir
32. Klik Swatch Trigger pada field Color
33. Verifikasi kolom Hex kembali berisi warna valid terakhir
34. Verifikasi inline error `Invalid color format` tidak tampil
35. Ketik di kolom Hex kode valid huruf kecil (`DU-10`)
36. Verifikasi kolom Hex menampilkan kode yang diketik (huruf besar atau kecil tidak dibedakan)
37. Verifikasi inline error `Invalid color format` tidak tampil
38. Verifikasi Swatch Trigger memakai warna `DU-10` (instan)
39. Verifikasi Live Preview memakai warna `DU-10` dan tetap menampilkan teks `DU-11`
40. Verifikasi tombol `[Submit]` Enabled

### F-FALB-06.k1: Kode di kolom Hex bukan # diikuti 6 digit heksadesimal

41. Ketik di kolom Hex kode 6 digit tanpa awalan `#` (`DU-12`)
42. Verifikasi inline error `Invalid color format` tampil di dalam Color Picker Overlay

### FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber: Kode warna bukan #RRGGBB tidak dapat disimpan dari form

43. Verifikasi tombol `[Submit]` Disabled selama kode 6 digit tanpa awalan `#` berada di kolom Hex

### F-FALB-06.k3: Overlay ditutup saat kolom Hex berisi kode tidak valid

44. Tekan Esc
45. Klik Swatch Trigger pada field Color
46. Verifikasi kolom Hex berisi warna valid terakhir, kode tidak valid dibuang
47. Klik `[✕]` pada header Modal Create Label
48. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
49. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1, 2, 3, 10, 14, 19, 23, 28, 32, 44, 45, 47, dan 49. Langkah 10, 19, 28, dan 44 menutup overlay dengan cara berbeda (Esc, klik Swatch Trigger, klik di luar overlay, Esc) sekaligus menjadi pembersih error inline antar-kategori (R-12); langkah 14, 23, 32, dan 45 membuka ulang overlay; langkah 47 sampai 49 menutup form dirty secara deterministik (S-08).
- Anchor positif (bagian 8b butir 2): langkah 15, 24, 33, dan 36 membuktikan Color Picker Overlay terbuka dengan kolom Hex terisi sebelum absence error inline di langkah 16, 25, 34, dan 37; langkah 11, 20, dan 29 membuktikan Modal Create Label masih tampil sesudah overlay ditutup.
- Tiga cara menutup overlay pada klausa `E-FALB-28` diuji berurutan: Esc (langkah 10 sampai 16), klik Swatch Trigger (langkah 19 sampai 25), dan klik di luar overlay (langkah 28 sampai 34); konsekuensi modal tetap tampil, `[Submit]` Enabled, warna tidak berubah, dan error inline hilang diasersi untuk ketiga cara.
- Klausa terakhir `E-FALB-28` ("kode valid langsung memperbarui warna") diasersi pada langkah 35 sampai 40 dengan dasar kalimat akhir `E-FALB-28` dan teks §4.3 Kolom Hex ("Kode valid memperbarui Swatch Trigger dan Live Preview secara instan"). Kolom Hex pada langkah 36 dibandingkan tanpa membedakan huruf besar dan kecil, karena normalisasi huruf kapital termasuk aturan yang ditahan (lihat butir Temuan PRD / aturan ditahan).
- Pembagian klausa lintas spec: `FALB-LOGIC-03c` diasersi di sini untuk validasi di UI; validasi server atas permintaan langsung ada di spec 005. `FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber` diasersi di sini untuk jalur form (tombol `[Submit]` Disabled); jalur permintaan API langsung ada di spec 005.
- Temuan PRD / aturan ditahan: bagian "dinormalisasi ke huruf kapital saat disimpan" dalam `E-FALB-28` adalah klausa aturan `FALB-LOGIC-03d` yang ditahan; tidak diasersi.
- Alasan spec melewati 35 langkah: semua blok satu kelas harness (fungsional) pada satu form Create dan satu Color Picker Overlay; asersi konsekuensi tutup overlay diulang per kategori kode (bagian 8b butir 7) dan memecah spec menambah login serta form baru tanpa mengurangi langkah.
- Isi dialog `Unsaved Changes` mengikuti konvensi platform, bukan PRD modul; spec hanya mengasersi judul dan tombolnya.
