---
id: TC-FA-LBL-E2E-012-request-langsung-idempotensi-penugasan-manual-dan-penolakan-lepas-relasi-default
title: "Request langsung: idempotensi penugasan manual dan penolakan lepas relasi default"
priority: Medium
caseType: Negative
status: draft
sourceRules:
  - FALB-LOGIC-06a
  - FALB-LOGIC-06b
  - FALB-LOGIC-06d
  - E-FALB-05
  - F-FALB-11.k1
  - FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d
coverage:
  web: automated
---

# Request langsung: idempotensi penugasan manual dan penolakan lepas relasi default

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Spec ini tidak membuka UI: seluruh langkah memakai klien HTTP dan fixture BE, dengan sesi API aktor akun `DU-01`; halaman tidak dibuka.
- Data uji, semuanya bersuffix `{runId}-012`, dibuat lewat API di hook `before` dan dihapus di hook `after` (aset, Asset Name, lalu label):
  - `DU-27`: Asset Name dengan label seed `DU-50` (`Assign-{runId}-012`) sebagai Default Label; aset default `DU-27` adalah aset Active dari Asset Name itu dan memegang relasi `default`.
  - `DU-28`: himpunan aset campuran untuk label seed `DU-50` yang sama: aset default `DU-28` (sama dengan aset default `DU-27`) dan aset manual `DU-28` (aset Active dengan label seed `DU-50` ditempel manual).
  - `DU-50`: label seed milik spec (`Assign-{runId}-012`), dibuat lewat API di hook `before` dan dihapus di hook `after` sesudah aset dan Asset Name.
  - `DU-26`: aset Active milik spec (aset default dan aset manual, dua aset).
- Kemampuan teknis: klien HTTP untuk permintaan langsung ke API `asset/` (attach dan detach label), sesi API aktor, dan fixture BE untuk membaca relasi aset dan label (jumlah relasi dan `source`). Endpoint attach dan detach dimiliki API `asset/` dan disediakan tim FE/BE tanpa mekanisme karangan.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB-LOGIC-06a: Satu pasangan aset dan label hanya tersimpan satu kali

1. Kirim permintaan attach manual label seed `DU-50` ke aset manual `DU-28` (aset Active milik spec `DU-26`) lewat klien HTTP
2. Verifikasi respons permintaan attach sukses
3. Baca relasi label seed `DU-50` pada aset manual `DU-28` lewat fixture BE
4. Verifikasi aset manual `DU-28` memiliki tepat satu relasi dengan label seed `DU-50`

### FALB-LOGIC-06b: Penugasan manual berulang idempoten dan tidak mengubah relasi yang ada

5. Kirim permintaan attach manual label seed `DU-50` ke aset default `DU-28` lewat klien HTTP
6. Verifikasi respons permintaan attach sukses
7. Baca relasi label seed `DU-50` pada aset default `DU-28` lewat fixture BE
8. Verifikasi relasi aset default `DU-28` dengan label seed `DU-50` tetap satu dan `source` tetap `default`
9. Verifikasi relasi aset manual `DU-28` dengan label seed `DU-50` tetap satu dan `source` tetap `manual`

### E-FALB-05: Permintaan langsung melepas label bersumber default ditolak server

10. Kirim permintaan detach label seed `DU-50` dari aset default `DU-28` lewat klien HTTP
11. Verifikasi respons permintaan detach ditolak server
12. Baca relasi label seed `DU-50` pada aset default `DU-28` lewat fixture BE
13. Verifikasi relasi aset default `DU-28` dengan label seed `DU-50` masih ada dengan `source` `default`

### F-FALB-11.k1: Detach relasi default ditolak

14. Verifikasi respons permintaan detach pada langkah 10 menolak pelepasan relasi default

### FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d: Pelepasan label default dari level aset tidak diizinkan

15. Verifikasi aset default `DU-28` tidak kehilangan relasi label seed `DU-50` setelah permintaan detach langsung

### FALB-LOGIC-06d: Pelepasan label bersifat idempoten

16. Kirim permintaan detach label seed `DU-50` dari aset manual `DU-28` lewat klien HTTP
17. Verifikasi respons permintaan detach sukses
18. Baca relasi label seed `DU-50` pada aset manual `DU-28` lewat fixture BE
19. Verifikasi aset manual `DU-28` tidak memiliki relasi dengan label seed `DU-50`
20. Kirim permintaan detach label seed `DU-50` dari aset manual `DU-28` sekali lagi lewat klien HTTP
21. Verifikasi respons permintaan detach kedua sukses tanpa galat
22. Baca relasi label seed `DU-50` pada aset manual `DU-28` lewat fixture BE
23. Verifikasi aset manual `DU-28` tetap tidak memiliki relasi dengan label seed `DU-50` dan aset default `DU-28` tetap memiliki satu relasi `default` dengan label seed `DU-50`

## Notes

- Langkah 1 sampai 23 mengirim permintaan lewat klien HTTP atau membaca state lewat fixture BE; hanya status respons dan state data yang diasersi, tampilan UI tidak diasersi di spec ini (konvensi bagian 8b butir 1).
- Pembagian klausa lintas spec: `E-FALB-05` dikutip spec 010 dan spec ini, serta `F-FALB-11.k1` dan `FALB:must-not/mengizinkan-pelepasan-label-bersumber-default-langsung-d` dikutip spec 028 dan spec ini; spec ini mengasersi sisi permintaan langsung ke server (penolakan), spec 010 mengasersi sisi UI `E-FALB-05` (ikon `[✕]` tidak tampil), spec 028 mengasersi sisi UI Bulk Remove (relasi default dilewati).
- Temuan PRD: PRD tidak menyatakan kode status atau isi respons untuk penolakan detach relasi default maupun untuk attach ulang idempoten (§9.2 F-FALB-11 hanya menyebut "ditolak server" dan "sukses"), sehingga langkah 2, 6, 11, 17, dan 21 mengasersi sukses atau ditolak tanpa kode status tertentu.
- `DU-27` hanya keadaan yang disyaratkan (Asset Name dan aset default yang memegang relasi `default` untuk label seed `DU-50`); tidak ada langkah yang mengasersinya sendiri. Langkah 17 dan 19 adalah anchor positif untuk langkah 21 dan 23 (detach pertama sukses dan relasi hilang sebelum detach kedua diuji, `FALB-LOGIC-06d`).
