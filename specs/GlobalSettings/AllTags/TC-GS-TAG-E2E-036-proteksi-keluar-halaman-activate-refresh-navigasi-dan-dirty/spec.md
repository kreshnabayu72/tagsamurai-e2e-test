---
id: TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty
title: "Proteksi Keluar Halaman Activate: Konfirmasi Bawaan Browser, Dialog 9 pada Navigasi In-App, dan Definisi Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-111
  - TC-GS-TAG-112
  - TC-GS-TAG-113
  - TC-GS-TAG-183
  - TC-GS-TAG-184
  - TC-GS-TAG-185
coverage:
  web: automated
---

# Proteksi Keluar Halaman Activate: Konfirmasi Bawaan Browser, Dialog 9 pada Navigasi In-App, dan Definisi Dirty

## Prerequisites

- Mode: FE+BE (backend nyata; pemicu Failed memakai sesi API, P-2).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Akun aktor:
  - Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` (TC-GS-TAG-111, 112, 113, 184, 185).
  - Total Control Client NoByo Eka Pratama `totalControl_automated_qaNoByo@qwertysystem.net`, `Spectra.env.GS_TC_NOBYO_PASSWORD` (TC-GS-TAG-183): login lewat langkah ganti akun eksplisit pada blok terakhir. Hook `after` mengembalikan sesi ke akun default suite.
  - Pelaku kedua (TC-GS-TAG-185, sesi API, hanya memicu perubahan state): Total Control kedua Client A Dewi Lestari `totalControl2_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`, mengaktivasi `356938035643001` hingga Activated (kesamaan akun dengan `.env.example` perlu dikonfirmasi tim FE saat tahap script, Q-2, kategori B).
- Data Pre-setup (dipulihkan lewat fixture BE sebelum spec dan antar blok, S-12): stok resmi Admin Console Client A: GPS `356938035643001` (DD-S1) dan `356938035643003` (DD-S3) Available, `356938035643002` (DD-S2) Damaged/Missing, Device Name `Teltonika FMB920`. Katalog Client A memuat `Queclink GV300` (Brand `Queclink`). Client NoByo: opsi mandiri nonaktif, tidak ada stok resmi untuk `356938035643101` (DD-N1). Data uji `35693803564` (DD-N6, 11 digit) hanya muncul di daftar Preview.
- Kemampuan teknis (disediakan tim FE/BE): penanganan dialog `beforeunload` di runner (mendeteksi kemunculan konfirmasi bawaan browser, membatalkannya agar tetap di halaman, atau menyetujuinya; S-08); tombol Back dan Forward browser; seed/reset stok dan registri; sesi API Total Control kedua; label dan placeholder input entri manual GPS serta tombol `Add` menunggu desain (NC-11), selektor disediakan tim FE.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan stok dan registri Client A dan Client NoByo, buang staging yang tersisa, kembalikan sesi ke akun default suite.
- Suite serial (`parallel: false`). Spec tidak mengubah state global. Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.

## Test Steps

### TC-GS-TAG-112: Tidak ada konfirmasi keluar untuk baris Activated

1. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
2. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`, klik [Submit], lalu klik [Submit] pada dialog (konfirmasi)
3. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
4. Muat ulang halaman (F5)
5. Verifikasi halaman termuat ulang (sidebar Global Settings tampil)
6. Verifikasi konfirmasi bawaan browser (`beforeunload`) tidak muncul (baris Activated tidak dihitung dirty)

### TC-GS-TAG-184: Hanya entri Preview GPS atau Template terisi, refresh tanpa konfirmasi

7. Pulihkan stok dan registri Client A ke kondisi awal lewat fixture BE, buka Global Settings > TAG > Tab All, lalu klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
8. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `35693803564` (11 digit) sehingga hanya muncul di daftar Preview
9. Muat ulang halaman (F5)
10. Verifikasi halaman termuat ulang (sidebar Global Settings tampil)
11. Verifikasi konfirmasi bawaan browser tidak muncul (entri Preview tidak dihitung dirty)
12. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
13. Isi Template Device Name `Queclink GV300`, Brand `Queclink` tanpa menambah baris
14. Muat ulang halaman (F5)
15. Verifikasi halaman termuat ulang (sidebar Global Settings tampil)
16. Verifikasi konfirmasi bawaan browser tidak muncul (Template tidak dihitung dirty)

### TC-GS-TAG-185: Baris Failed tetap dihitung dirty

17. Buka Global Settings > TAG > Tab All, lalu klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
18. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
19. Dari sesi lain (Total Control kedua Client A, sesi API), aktivasi `356938035643001` hingga Activated tersimpan
20. Klik [Submit], lalu klik [Submit] pada dialog (konfirmasi) sehingga baris `356938035643001` berstatus Failed
21. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
22. Muat ulang halaman (F5)
23. Verifikasi konfirmasi bawaan browser muncul (baris Failed masih di staging)
24. Batalkan konfirmasi bawaan browser (tetap di halaman)
25. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

### TC-GS-TAG-111 dan TC-GS-TAG-113: Refresh dan navigasi in-app dengan staging dirty

26. Pulihkan stok dan registri Client A ke kondisi awal lewat fixture BE, lalu klik Tab All, klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
27. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
28. Muat ulang halaman (F5)
29. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
30. Verifikasi tidak ada dialog aplikasi yang tampil
31. Batalkan konfirmasi bawaan browser (tetap di halaman)
32. Klik item sidebar `Global Settings > User`
33. Verifikasi dialog Unsaved Changes (Dialog 9) dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
34. Verifikasi navigasi tertahan (halaman Activate TAG tetap tampil)
35. Klik [Cancel]
36. Verifikasi halaman Activate TAG tetap tampil dengan staging utuh (baris `356938035643001`)
37. Klik icon Profile di navbar, lalu pilih `My Profile`
38. Verifikasi dialog Unsaved Changes yang sama muncul
39. Klik [Cancel]
40. Klik tiap segmen breadcrumb (dua segmen)
41. Verifikasi breadcrumb dua segmen tidak dapat diklik (tidak ada navigasi dan tidak ada dialog)
42. Klik tombol Back browser
43. Verifikasi dialog Unsaved Changes yang sama muncul
44. Klik [Leave]
45. Verifikasi navigasi dilanjutkan (halaman Activate TAG tidak lagi tampil)
46. Klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, lalu klik [Continue] pada popup `Ready to Activate a TAG`
47. Verifikasi tabel staging kosong (staging sebelumnya dibuang)
48. Klik item sidebar `Global Settings > User`
49. Verifikasi halaman `Global Settings > User` tampil
50. Klik tombol Back browser
51. Verifikasi halaman Activate TAG tampil
52. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643001`
53. Klik tombol Forward browser
54. Verifikasi dialog Unsaved Changes yang sama muncul
55. Klik [Leave]
56. Tunggu aksi selesai (dialog tertutup)

### TC-GS-TAG-183: Hanya baris Error di staging (Client NoByo)

57. Ganti akun: logout, lalu login sebagai Total Control Client NoByo dengan `Spectra.env.GS_TC_NOBYO_PASSWORD`
58. Buka Global Settings > TAG > Tab All, lalu klik `+ Activate TAG`, pilih `GPS` pada overlay `Select TAG Type`, dan klik [Continue] pada popup `Ready to Activate a TAG`
59. Tambahkan lewat entri manual (ketik di input lalu klik [Add]) `356938035643101`
60. Muat ulang halaman (F5)
61. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul (baris Error dihitung sebagai staging belum tersubmit)
62. Batalkan konfirmasi bawaan browser (tetap di halaman)
63. Klik item sidebar `TAG`, lalu klik [Leave] pada dialog Unsaved Changes (membuang staging)

## Notes

- Mode: FE+BE. P-2: sesi API Total Control kedua (langkah 19) hanya memicu state Failed (ditulis "hingga ... tersimpan"). Konfirmasi bawaan browser ditangani runner (S-08, kemampuan tertulis di Prerequisites).
- Spec melewati sekitar 35 langkah (63 langkah). Alasan: seluruh blok satu topik (proteksi keluar halaman Activate: `beforeunload` dan Dialog 9) dengan harness yang sama (penanganan dialog `beforeunload`) dan berdiri sendiri; staging dibuang dan data dipulihkan antar blok (langkah 7, 25, 26, 56, 63) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-GS-TAG-111 dan TC-GS-TAG-113 berbagi satu sesi karena precondition dan staging awalnya identik (satu baris `356938035643001`); refresh TC-GS-TAG-111 dibatalkan agar staging utuh untuk TC-GS-TAG-113.
- Urutan: kasus tanpa konfirmasi (TC-GS-TAG-112, 184) di awal; blok Client NoByo (TC-GS-TAG-183) paling akhir karena ganti akun hanya sekali (langkah 57) dan sesudahnya tidak ada blok Client A. TC-GS-TAG-112 dan 184 dijalankan sebelum TC-GS-TAG-111 karena keduanya tidak meninggalkan staging dirty; TC-GS-TAG-185 dan blok TC-GS-TAG-111/113 memakai akun Client A yang sama tanpa ganti akun.
- Langkah penghubung (tanpa `Verifikasi`, S-03): 1, 3, 7, 12, 17, 21, 24, 25, 26, 31, 46, 56, 57, 58, 62, 63 (membuka sesi, ganti akun, menunggu aksi selesai, membatalkan konfirmasi bawaan, membuang staging, pemulihan); langkah 3, 21, 56 adalah "Tunggu aksi selesai" sebelum berpindah surface (F5 atau ganti akun, butir 8 bagian 8b); langkah 5, 10, 15 adalah anchor positif halaman termuat untuk asersi absence konfirmasi sesudah F5 (8b butir 2).
- Langkah tambahan demi Expected TC-GS-TAG-113 butir c dan d (S-03): langkah 37 sampai 41 (navbar dan breadcrumb), langkah 46 sampai 47 (mengamati staging dibuang), dan langkah 48 sampai 56 (urutan Forward: sidebar ke `Global Settings > User`, Back kembali ke halaman Activate, tambah baris, Forward, dialog, `Leave`; langkah 49 dan 51 adalah anchor positif), karena Langkah Uji TC hanya memuat sidebar dan Back.
- Pembagian TC lintas spec: TC-GS-TAG-102 (sumber baris Failed pada blok Failed) berada di spec 033; TC-GS-TAG-182 (refresh saat sesi scan aktif) berada di spec sesi scan (038).
- Temuan untuk QA:
  - TC-GS-TAG-113 Expected c menyebut pemicu navbar dan tombol Forward browser, tetapi Langkah Uji hanya memuat sidebar dan Back. Spec menambah pemicu navbar (icon Profile di navbar, lalu `My Profile`; item navbar tidak disebut TC, selektor disediakan tim FE), klik breadcrumb, dan urutan Forward (langkah 48 sampai 56). Keadaan halaman Activate setelah Back dari halaman lain (tipe terkunci atau sesi baru) tidak ditulis di TC maupun PRD; langkah 51 dan 52 mengasumsikan halaman Activate dengan input entri manual tersedia, dan bila tidak, bukti dicatat (S-15) serta TC-GS-TAG-113 diperbaiki.
  - TC-GS-TAG-111/112/183/184/185: TC tidak menyatakan pilihan pada konfirmasi bawaan browser (tetap atau muat ulang); spec membatalkannya (tetap di halaman).
  - TC-GS-TAG-112: Skenario menyebut staging kosong dan baris Waiting for Approval, tetapi Langkah Uji hanya memuat baris Activated; spec mengikuti Langkah Uji.
  - TC-GS-TAG-185 bergantung pada TC-GS-TAG-102 (baris Failed); spec membangun baris Failed sendiri (langkah 18 sampai 20) tanpa menumpang TC lain.
  - TC-GS-TAG-113 Expected d ("staging dibuang") tidak punya langkah observasi di TC; spec mengamati dengan membuka sesi baru (langkah 46 sampai 47).
  - Post Condition semua TC bernilai `-`.
