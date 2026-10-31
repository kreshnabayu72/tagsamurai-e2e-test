---
id: TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses
title: "Dialog Submit Activation dan Commit Sukses Official/Self-Purchased: Toast T-16, Kartu GPS, dan Last Scanned"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-98
  - TC-GS-TAG-99
  - TC-GS-TAG-101
  - TC-GS-TAG-169
coverage:
  web: automated
---

# Dialog Submit Activation dan Commit Sukses Official/Self-Purchased: Toast T-16, Kartu GPS, dan Last Scanned

## Prerequisites

- Mode: FE+BE (backend nyata; tidak ada intercept).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada ganti akun.
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): stok resmi Admin Console Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available, `356938035643002` (DD-S2) Damaged/Missing, Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`. Katalog Client A memuat Device Name `Queclink GV300` (Brand `Queclink`, Model/Type `GV300`, aktif). Opsi mandiri aktif; Client A GPS terpakai 1 dari 30 (Seed Registri A).
- Data uji: IMEI `356938035643101` (DD-N1; tidak ada di stok, Self-Purchased) dan `356938035643201` (DD-N4; In Use di Client B, dibuat lewat fixture BE sebagai precondition TC-GS-TAG-169). Kolom `Last Scanned` ditampilkan di registri (precondition TC-GS-TAG-169); kolom `Last Scanned In` default Hidden (TC-GS-TAG-11) dan ditampilkan lewat Setup Column pada blok TC-GS-TAG-169. Format tanggal Client A `dd/MM/yy`, 24-hour, Asia/Jakarta.
- Kemampuan teknis (disediakan tim FE/BE): seed/reset stok resmi, registri Client A, dan unit Client B; jam server dan jam browser diatur bersama (Q-6, S-12: waktu entri dicatat sesudah aksi, toleransi satu menit; jam dimajukan 5 menit agar selisih dengan waktu Submit melebihi toleransi dan dipulihkan sesudah Submit, sebelum asersi); label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan jam server dan jam browser, preferensi Setup Column (hapus preferensi kolom di browser; kemampuan disediakan tim FE), stok resmi, registri Client A dan unit Client B ke kondisi awal, buang staging yang tersisa.
- Suite serial (`parallel: false`). Spec mengubah jam server dan jam browser serta preferensi Setup Column akun Total Control (`Last Scanned In` ditampilkan); keduanya dipulihkan seperti di atas. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-98: Dialog Submit Activation dan Cancel mempertahankan staging

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
3. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001` (Official) dan `356938035643101` (Self-Purchased)
4. Klik [Submit]
5. Verifikasi dialog `Submit Activation` dengan body "2 TAGs will be activated and will consume 2 license slots:" diikuti bullet `356938035643001` dan `356938035643101`, lalu "Are you sure you want to submit? This action cannot be undone after commit."
6. Verifikasi tombol [Cancel] dan [Submit] tampil pada dialog
7. Klik [Cancel]
8. Verifikasi staging tetap dua baris (`356938035643001` dan `356938035643101`)
9. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

### TC-GS-TAG-99: Commit sukses Official dan Self-Purchased

10. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
11. Isi Template Device Name `Queclink GV300`, Brand `Queclink`, Model/Type `GV300`
12. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001` (Official) dan `356938035643101` (Self-Purchased)
13. Klik [Submit], lalu klik [Submit] pada dialog
14. Verifikasi toast sukses: "Success, TAG has been activated." tanpa jumlah
15. Verifikasi dialog "Your activation is pending review." tidak tampil
16. Verifikasi halaman Activate TAG tetap terbuka
17. Verifikasi tipe GPS tetap terkunci
18. Verifikasi tabel staging kosong
19. Klik item sidebar `TAG`, lalu klik Tab All
20. Verifikasi registri memuat `356938035643001` (Source Official, Device Name `Teltonika FMB920`) berstatus Available
21. Verifikasi registri memuat `356938035643101` (Source Self-Purchased, Brand `Queclink`) berstatus Available
22. Verifikasi kartu GPS `3 of 30`
23. Verifikasi kartu GPS `27 remaining`
24. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE

### TC-GS-TAG-101: Official yang cocok stok Available atau Damaged/Missing aktif langsung

25. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
26. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001` (Available) dan `356938035643002` (Damaged/Missing)
27. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
28. Verifikasi toast sukses: "Success, TAG has been activated."
29. Verifikasi dialog "Your activation is pending review." tidak tampil
30. Klik item sidebar `TAG`, lalu klik Tab All
31. Verifikasi `356938035643001` berstatus `Available` di registri
32. Verifikasi `356938035643002` berstatus `Available` di registri
33. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE

### TC-GS-TAG-169: Commit Activate memperbarui Last Scanned dan Last Scanned In, tidak untuk Waiting for Approval

34. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
35. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
36. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
37. Catat waktu entri `T169` (waktu browser tepat sesudah [Add] baris `356938035643001`)
38. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643201`
39. Majukan jam server dan jam browser bersama sebesar 5 menit
40. Klik [Submit], klik [Submit] pada dialog, lalu tutup dialog informasi "Your activation is pending review."
41. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
42. Pulihkan jam server dan jam browser ke waktu semula
43. Klik item sidebar `TAG`, lalu klik Tab All
44. Buka overlay Column Visibility, klik `Setup Column`, centang `Last Scanned In`, lalu klik [Save]
45. Ketik Search `356938035643001`, tekan Enter
46. Verifikasi Last Scanned `356938035643001` sama dengan `T169` (toleransi satu menit, format `dd/MM/yy HH:mm`), bukan waktu Submit
47. Verifikasi badge Last Scanned In `356938035643001` bernilai `Global Settings`
48. Hover badge Last Scanned In `356938035643001`
49. Verifikasi tooltip "Global Settings > TAG > Activate TAG"
50. Ganti isi kotak search dengan `356938035643201`, tekan Enter
51. Verifikasi Last Scanned `356938035643201` bernilai `—`
52. Verifikasi Last Scanned In `356938035643201` bernilai `—`
53. Hapus preferensi kolom di browser (kemampuan disediakan tim FE)
54. Pulihkan stok resmi, registri Client A, dan unit Client B ke kondisi awal lewat fixture BE

## Notes

- Mode: FE+BE. Spec melewati sekitar 35 langkah (54 langkah). Alasan: seluruh blok satu topik aksi (Submit dan commit Activate) atas dataset stok yang sama, berdiri sendiri karena stok dan registri dipulihkan antar blok (langkah 24, 33, 54) dan staging dibuang (langkah 9); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 9, 10, 19, 24, 25, 30, 33, 34, 37, 39, 41, 42, 43, 45, 50, 53, 54 (membuka sesi, membuang staging, pindah ke registri, pemulihan, pengaturan jam, Setup Column untuk menampilkan `Last Scanned In` dan memulihkannya, Search untuk menemukan baris target, mencatat nilai, menunggu aksi selesai sebelum jam dipulihkan).
- Langkah tambahan (S-03): langkah 28 (toast sukses) adalah anchor positif untuk asersi absence dialog pada langkah 29 (butir 2 dan 11 bagian 8b); Expected TC-GS-TAG-101 tidak memuat toast, teks toast diambil dari Expected TC-GS-TAG-99. Langkah 44 adalah langkah 9 TC-GS-TAG-169 (Setup Column menampilkan `Last Scanned In`, default Hidden, TC-GS-TAG-11); langkah 53 memulihkan preferensi kolom.
- Urutan: blok Cancel (TC-GS-TAG-98) di awal, lalu commit sukses (TC-GS-TAG-99, 101, 169).
- Pembagian TC lintas spec: TC-GS-TAG-100 dan 167 (kolisi dan auto-switch) berada di spec kolisi (032); TC-GS-TAG-170 dan 171 (Last Scanned pada Audit) berada di spec Audit Submit (042). TC-GS-TAG-110 (info kuota header, RFID dengan reader tersimulasi, kelas hardware d) berada di spec sesi scan (025) agar kegagalan simulator tidak menggagalkan spec Submit GPS ini. Event Log dan Activity Log Activate tidak dibaca di spec ini.
- Temuan untuk QA:
  - TC-GS-TAG-98: Skenario menyebut dialog "memuat hanya baris non-Error", tetapi Langkah Uji tidak menambah baris Error; spec mengikuti Langkah Uji.
  - TC-GS-TAG-169 (Q-6): "Tunggu minimal 1 menit" tidak menentukan menunggu nyata atau mengatur jam; spec mengatur jam server dan jam browser bersama (5 menit). Nilai "1 menit" berasal dari langkah 6 TC (Q-13).
  - Dialog informasi "Your activation is pending review." (TC-GS-TAG-169, langkah 40): judul dan tombol penutupnya tidak ditulis di TC.
  - Post Condition tanpa langkah observasi tidak diasersi: TC-GS-TAG-99 butir c (Event Log dan Activity Log satu sesi Activate GPS) dan butir d (unit stok In Use dan unit baru di Admin Console TAG Stock); TC-GS-TAG-101 butir b (unit stok In Use).
