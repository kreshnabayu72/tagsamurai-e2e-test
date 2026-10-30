---
id: TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal
title: "Commit Sebagian/Semua Gagal: Failed T-06/T-07, Evaluasi Ulang Submit Berikutnya, Waiting for Approval Client Lain, dan Toast T-25"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-102
  - TC-GS-TAG-103
  - TC-GS-TAG-104
  - TC-GS-TAG-105
  - TC-GS-TAG-176
coverage:
  web: automated
---

# Commit Sebagian/Semua Gagal: Failed T-06/T-07, Evaluasi Ulang Submit Berikutnya, Waiting for Approval Client Lain, dan Toast T-25

## Prerequisites

- Mode: FE+BE (backend nyata; pemicu "tepat saat commit" memakai sesi API, P-2, Q-5).
- Akun aktor: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Tidak ada sesi UI kedua.
- Pelaku kedua (sesi API, hanya memicu perubahan state):
  - Total Control kedua Client A Dewi Lestari `totalControl2_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`, mengaktivasi `356938035643001` hingga Activated (TC-GS-TAG-102 dan 176). Email di `.env.example` dan Pre-setup perlu dikonfirmasi FE (Q-2).
  - Akun Principal pada Admin Console > Client yang mematikan opsi mandiri (BYO) Client A (TC-GS-TAG-104). Akun tidak tertulis di TC; disediakan tim FE (S-13).
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): stok resmi Admin Console Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available, `356938035643002` (DD-S2) Damaged/Missing, Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`. Katalog Client A memuat Device Name `Queclink GV300` (Brand `Queclink`, Model/Type `GV300`). Opsi mandiri Client A aktif. IMEI `356938035643401` (DD-N13) berstatus Waiting for Approval di Client B (Total Control Client B `totalControl_automated_qaTeam2@qwertysystem.net`, `Spectra.env.GS_CLIENTB_TC_PASSWORD`; hanya fixture BE, tidak login). IMEI `356938035643101` (DD-N1) tidak ada di stok dan registri.
- State global yang diubah: opsi mandiri (BYO) Client A dimatikan pada blok TC-GS-TAG-104 (blok terakhir) dan dipulihkan menjadi aktif pada langkah 50 serta di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): seed/reset stok resmi, registri Client A, dan unit Client B; sesi API Total Control kedua dan Principal; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan opsi mandiri Client A, stok resmi, registri Client A dan unit Client B, buang staging yang tersisa.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-105: Kode Waiting for Approval di client lain berakhir Failed T-06

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
3. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643401`
4. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
5. Verifikasi toast error persisten: "Error, failed to activate TAG."
6. Verifikasi toast sukses sebagian tidak tampil
7. Verifikasi baris `356938035643401` berstatus `Failed`
8. Hover badge Failed baris `356938035643401`
9. Verifikasi tooltip "This identifier has already been activated."
10. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

### TC-GS-TAG-102: Identifier diaktivasi sesi lain persis saat commit

11. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
12. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001` dan `356938035643003` (keduanya Official)
13. Dari sesi lain (Total Control kedua Client A, sesi API), aktivasi `356938035643001` hingga Activated tersimpan
14. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
15. Verifikasi toast sukses: "Success, TAG has been activated. Some TAGs failed to activate."
16. Verifikasi baris `356938035643001` berstatus `Failed` dengan badge danger
17. Hover badge Failed baris `356938035643001`
18. Verifikasi tooltip "This identifier has already been activated."
19. Verifikasi baris `356938035643001` tetap di staging
20. Verifikasi baris `356938035643003` Activated dan keluar dari staging

### TC-GS-TAG-103: Baris Failed dievaluasi ulang pada Submit berikutnya (lanjutan sesi TC-GS-TAG-102)

21. Klik [Submit] pada halaman Activate TAG
22. Verifikasi dialog `Submit Activation` menghitung baris Failed `356938035643001` (body diawali "1 TAG will be activated")
23. Klik [Submit] pada dialog dan amati baris serta toast
24. Verifikasi toast error persisten: "Error, failed to activate TAG."
25. Hover badge Failed baris `356938035643001`
26. Verifikasi baris `356938035643001` tetap `Failed`
27. Verifikasi tooltip "This identifier has already been activated." pada baris `356938035643001`
28. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)
29. Klik Tab All, ketik Search `356938035643001`, tekan Enter
30. Verifikasi registri memuat tepat satu baris `356938035643001` (hasil aktivasi sesi lain)
31. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE

### TC-GS-TAG-176: Activate dengan seluruh baris Failed

32. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
33. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
34. Dari sesi lain (Total Control kedua Client A, sesi API), aktivasi `356938035643001` hingga Activated tersimpan
35. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
36. Verifikasi toast error persisten: "Error, failed to activate TAG."
37. Verifikasi toast sukses tidak tampil
38. Verifikasi baris `356938035643001` berstatus `Failed`
39. Verifikasi baris `356938035643001` tetap di staging
40. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

### TC-GS-TAG-104: Opsi mandiri dimatikan admin di tengah sesi

41. Pulihkan stok resmi dan registri Client A ke kondisi awal lewat fixture BE, lalu klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
42. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
43. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101`
44. Lewat Admin Console > Client (Principal, sesi API), matikan opsi BYO Client A hingga tersimpan
45. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
46. Verifikasi baris `356938035643101` berstatus `Failed`
47. Hover badge Failed baris `356938035643101`
48. Verifikasi tooltip "Self-purchased device activation is not enabled for your account."
49. Verifikasi baris `356938035643101` tetap di staging
50. Pulihkan opsi mandiri Client A menjadi aktif (sesi API Principal)
51. Kembali ke List: klik item sidebar `TAG`, klik `Leave` pada dialog konfirmasi keluar halaman (staging berisi baris `356938035643101`)

## Notes

- Mode: FE+BE. P-2: pelaku kedua (Total Control kedua dan Principal) hanya memicu perubahan state lewat sesi API ("hingga ... tersimpan"); hasil diasersi di sesi Client A. Client B hanya fixture (unit Waiting for Approval).
- Spec melewati sekitar 35 langkah (51 langkah). Alasan: seluruh blok satu kelas (kegagalan baris saat commit Activate, tanpa harness lain) atas satu halaman dan dataset stok yang sama; tiap blok berdiri sendiri karena staging dibuang (langkah 10, 28, 40) dan stok dipulihkan (langkah 31, 41); kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok yang mengubah state global (TC-GS-TAG-104, mematikan opsi mandiri) ditaruh paling akhir.
- Urutan: TC-GS-TAG-105 (tanpa pemicu sesi lain) lebih dulu; TC-GS-TAG-103 melanjutkan sesi TC-GS-TAG-102 sesuai kolom Dependensi (langkah TC-GS-TAG-102 disalin utuh, S-04).
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 10, 11, 28, 29, 31, 32, 40, 41, 50, 51 (membuka sesi, membuang staging, Search di registri, pemulihan, kembali ke List).
- Pembagian TC lintas spec: TC-GS-TAG-185 (baris Failed tetap dihitung dirty) berada di spec proteksi keluar halaman (036) dengan baris Failed yang dibangun spec itu sendiri; TC-GS-TAG-94 berada di spec lain.
- Temuan untuk QA:
  - Q-5: pemicu "persis saat commit" (TC-GS-TAG-102) tidak deterministik; spec mengaktivasi `356938035643001` dari sesi lain sebelum Submit (langkah 13 dan 34) dan mekanismenya disediakan tim FE/BE.
  - TC-GS-TAG-102 Expected c ("Baris Failed tidak ditulis ke registry pada percobaan itu") tidak punya cara observasi di TC; spec menafsirkannya sebagai registri hanya memuat satu baris `356938035643001` (hasil sesi lain, langkah 30). Post Condition TC-GS-TAG-102 tidak punya langkah observasi, tidak diasersi.
  - TC-GS-TAG-103 Expected a memotong body dialog dengan "..." (`1 TAG will be activated ...`); spec hanya mengasersi awal kalimat.
  - TC-GS-TAG-104 dan 102/176 (Q-2): akun Principal dan Total Control kedua; kesamaan dengan `GS_PRINCIPAL_TC_PASSWORD` dan `GS_TC2_PASSWORD` perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - TC-GS-TAG-105: "Template kosong sebelum langkah pertama" ditulis sebagai kondisi awal; langkah 2 tetap mengisi Template sesuai Langkah Uji.
  - Opsi mandiri (BYO) Client A bukan bagian daftar state global di `suite.md`; spec ini memulihkannya sendiri (langkah 50 dan hook `after`).
