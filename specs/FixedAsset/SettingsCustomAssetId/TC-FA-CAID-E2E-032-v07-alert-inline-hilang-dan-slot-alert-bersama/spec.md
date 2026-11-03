---
id: TC-FA-CAID-E2E-032-v07-alert-inline-hilang-dan-slot-alert-bersama
title: "V-07: Alert Inline Hilang dan Slot Alert Bersama D-03 dan D-06"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-90
  - TC-FA-CAID-91
  - TC-FA-CAID-334
coverage:
  web: automated
---

# V-07: Alert Inline Hilang dan Slot Alert Bersama D-03 dan D-06

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `Company V07 65` (Pre-setup No 19). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun dan password disediakan tim FE dengan env var usulan `Spectra.env.FA_V0765_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (No 19): `Company V07 65` dengan satu aset Draft; Group Code `GRP-LONG-000001`, Category Code `CAT-LONG-000001`, Asset Name Code `AST-LONG-000001`, Separator `- (Dash)`, formula tanpa Purchase Date; Division Code `DIVISION-ABC-15` di-assign ke aset Draft itu.
- Alat uji (Pre-setup No 26): penyunting request pada sesi otomasi untuk mengubah payload request Save (daftar segmen kosong) dan menunda respons Save selama 5 detik. Penyunting dilepas segera setelah pemicu selesai.
- Kemampuan teknis: seed `Company V07 65` dan pengembalian ke keadaan awal sebelum run disediakan tim FE/BE; sesi API aktor untuk seed dan pemulihan (suite.md).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: konfigurasi `Company V07 65` tidak berubah karena semua Save ditolak. Hook `after` memulihkan Company ke seed awal. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-90: Alert V-07 hilang saat Separator, centang segmen, atau urutan segmen diubah

1. Centang `Division Code`
2. Klik `[Save]` hingga alert V-07 tampil
3. Pilih Separator `. (Dot)`
4. Verifikasi alert V-07 di atas `[Save]` hilang
5. Klik `[Save]` hingga alert V-07 tampil lagi
6. Centang `Purchase Date (MMYY)`
7. Verifikasi alert V-07 di atas `[Save]` hilang
8. Klik `[Save]` hingga alert V-07 tampil lagi
9. Seret baris `Category Code` ke atas baris `Group Code`
10. Verifikasi alert V-07 di atas `[Save]` hilang

### TC-FA-CAID-91: Alert V-07 hilang saat pengguna meninggalkan tab

11. Klik `[Save]` hingga alert V-07 tampil
12. Klik tab `Asset Name`
13. Verifikasi dialog berjudul `Unsaved Changes` (severity warning) dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning) tampil
14. Klik `[Leave]`
15. Klik tab `Custom Asset ID`
16. Verifikasi tidak ada alert di atas `[Save]`

### TC-FA-CAID-334: Slot alert bersama D-03 dan D-06

17. Centang `Division Code`, ubah payload request Save lewat penyunting sehingga daftar segmen kosong, lalu klik `[Save]`
18. Verifikasi hanya alert `Select at least one segment` tampil
19. Lepas penyunting payload, lalu klik `[Save]` dengan payload asli dari form (Division Code tercentang)
20. Verifikasi alert `Asset ID would exceed 64 characters. Remove a segment or choose a shorter separator.` menggantikan alert sebelumnya
21. Verifikasi hanya satu alert tampil
22. Tunda respons Save selama 5 detik, lalu klik `[Save]`
23. Verifikasi tidak ada alert di atas `[Save]` selama respons ditunda
24. Lepas tahanan respons dan tunggu respons tiba
25. Verifikasi alert V-07 tampil lagi
26. Hilangkan centang `Division Code` (pulihkan form ke nilai tersimpan)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: klik `[Save]` hingga alert V-07 tampil (precondition TC-FA-CAID-90 dan TC-FA-CAID-91 sesuai butir "Alert V-07 sedang tampil setelah Save ditolak", tidak diasersi), langkah 12 sampai 15 (pindah tab dengan form dirty; `Verifikasi` dialog `Unsaved Changes` dan `[Leave]` mengikuti S-08 sehingga tidak ada langkah bersyarat), dan langkah 26 (pemulihan form dirty, S-09).
- `P-2`: penyunting request pada langkah 17 hanya memicu alert D-03 sebagai pemicu; objek uji TC-FA-CAID-334 adalah slot alert bersama D-03 dan D-06. Menunda respons Save pada langkah 22 sampai 24 hanya untuk mengamati state UI selama request berjalan, bukan kelas b.
- Anchor asersi "alert hilang" (langkah 4, 7, 10, 16) adalah alert V-07 yang tampil pada langkah sebelumnya pada surface yang sama.
- Pembagian TC lintas spec: TC-FA-CAID-86 sampai 89 ada di spec 031; TC-FA-CAID-92 dan TC-FA-CAID-93 ada di spec 047.
- Temuan untuk QA:
  - Email akun `Company V07 65` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE".
  - TC-FA-CAID-91 langkah 1 memakai frasa "pilih `[Leave]` pada dialog bila muncul"; spec menulis dialog sebagai pasti muncul karena form dirty setelah Save ditolak (S-08).
  - TC-FA-CAID-334 langkah 2 "Kirim Save dengan payload asli dari form" tidak menyebut cara melepas penyunting request; spec menulisnya sebagai langkah melepas penyunting lalu klik `[Save]`.
  - Post Condition TC-FA-CAID-90, TC-FA-CAID-91, dan TC-FA-CAID-334 tidak diasersi karena TC tidak memberi langkah observasinya.
