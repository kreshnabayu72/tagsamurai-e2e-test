---
id: TC-AC-ACAL-E2E-007-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai
title: "Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-19
  - TC-AC-ACAL-21
  - TC-AC-ACAL-22
  - TC-AC-ACAL-23
coverage:
  web: automated
---

# Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

| Akun | Email | Env | Dipakai di |
|---|---|---|---|
| Total Control (Principal), akun aktor pertama (Pre-setup No 1) | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-ACAL-19, akun pertama TC-AC-ACAL-21, TC-AC-ACAL-22, TC-AC-ACAL-23 |
| Read Only (Principal), akun kedua (Pre-setup No 2) | `readOnlyAdminConsolePrincipal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` | akun kedua TC-AC-ACAL-21 |

- Login akun aktor pertama (Total Control) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Ganti akun ke Read Only dan kembali ke Total Control ditulis eksplisit sebagai langkah (TC-AC-ACAL-21); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture; nama env `AC_TC_PASSWORD` dan `AC_RO_PASSWORD` mengikuti bagian 5 konvensi; `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`, sedangkan `AC_RO_PASSWORD` usulan tim FE (belum terdaftar). Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen akun Total Control (lihat suite.md); spec ini mengatur flag sendiri sesudah hook suite. Hook `before` spec ini menyetel flag `guided_tooltip_seen_ac-activity-log` (`page_key` `ac-activity-log`, PRD §4.7) akun Read Only ke belum ada, dan hook `after` memulihkannya; flag akun Total Control diatur oleh langkah penghubung dan dipulihkan hook suite `after`. Flag Guided Tooltip halaman tujuan navigasi (menu lain di sidebar, lihat langkah) disetel true untuk kedua akun di hook `before` dan dipulihkan di hook `after` supaya walkthrough halaman tujuan tidak menutupi layar (nama flag halaman tujuan ditetapkan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): (1) menyetel flag `guided_tooltip_seen_ac-activity-log` per akun ke belum ada atau ke true dan membacanya; tidak ada endpoint yang dikarang di spec ini. (2) Mengubah ukuran jendela browser (resize) dan memulihkannya. (3) Logout dan login ulang di tengah spec.
- Menu tujuan navigasi pada TC-AC-ACAL-19 dan TC-AC-ACAL-23: menu Client di sidebar Admin Console (TC menyebut "menu lain" tanpa nama; lihat Temuan untuk QA).
- Data: tidak ada data log yang dibuat atau dibaca.
- State global yang diubah: flag Guided Tooltip kedua akun dan ukuran jendela browser (dipulihkan lewat langkah dan hook `after`).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-19: Walkthrough [Done] menyimpan flag, tidak muncul otomatis lagi

1. Setel flag `guided_tooltip_seen_ac-activity-log` akun Total Control ke belum ada
2. Klik menu Activity Log di sidebar Admin Console
3. Klik `[Next]`
4. Klik `[Next]`
5. Klik `[Done]`
6. Verifikasi walkthrough tertutup setelah `[Done]`
7. Klik menu Client di sidebar Admin Console
8. Klik menu Activity Log di sidebar Admin Console
9. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-AC-ACAL-21: Guided Tooltip, [Skip] via tombol dan via klik overlay gelap

10. Setel flag `guided_tooltip_seen_ac-activity-log` akun Total Control ke belum ada
11. Klik menu Activity Log di sidebar Admin Console
12. Klik `[Skip]`
13. Verifikasi walkthrough tertutup setelah `[Skip]`
14. Ganti akun: logout lalu login sebagai Read Only (Principal)
15. Klik menu Activity Log di sidebar Admin Console
16. Klik area overlay gelap
17. Verifikasi walkthrough tertutup setelah klik area overlay gelap
18. Klik menu Client di sidebar Admin Console
19. Klik menu Activity Log di sidebar Admin Console
20. Verifikasi akun Read Only: walkthrough tidak muncul otomatis
21. Ganti akun: logout lalu login sebagai Total Control (Principal)
22. Klik menu Client di sidebar Admin Console
23. Klik menu Activity Log di sidebar Admin Console
24. Verifikasi akun Total Control: walkthrough tidak muncul otomatis

### TC-AC-ACAL-22: Guided Tooltip, replay via tombol [?] dari Step 1 tanpa mereset flag

25. Setel flag `guided_tooltip_seen_ac-activity-log` akun Total Control ke true
26. Klik menu Activity Log di sidebar Admin Console
27. Klik tombol `[?]` di header
28. Verifikasi walkthrough mulai dari Step 1
29. Klik `[Skip]`
30. Verifikasi walkthrough tertutup
31. Klik menu Client di sidebar Admin Console
32. Klik menu Activity Log di sidebar Admin Console
33. Verifikasi walkthrough tidak muncul otomatis

### TC-AC-ACAL-23: Guided Tooltip, keluar tanpa selesai (resize / navigasi) tidak menyimpan flag

34. Setel flag `guided_tooltip_seen_ac-activity-log` akun Total Control ke belum ada
35. Klik menu Activity Log di sidebar Admin Console
36. Verifikasi walkthrough tampil dari Step 1
37. Klik `[Next]` ke Step 2
38. Ubah ukuran viewport jendela browser
39. Verifikasi walkthrough tertutup setelah resize
40. Pulihkan ukuran viewport jendela browser ke ukuran awal
41. Buka ulang halaman Admin Console > Activity Log (muat ulang halaman, F5)
42. Verifikasi walkthrough muncul lagi dari Step 1
43. Klik menu Client di sidebar Admin Console pada saat Step 1
44. Verifikasi walkthrough tertutup saat navigasi
45. Klik menu Activity Log di sidebar Admin Console
46. Verifikasi walkthrough muncul otomatis lagi dari Step 1
47. Klik `[Skip]`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-19, 21, 22, 23). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-ACAL-18, 20, dan 24 ada di spec `TC-AC-ACAL-E2E-006-guided-tooltip-isi-dan-navigasi`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 10, 25, dan 34 (menyetel flag sesuai precondition tiap TC; TC-22 mensyaratkan flag sudah ada sehingga flag disetel true eksplisit, tidak bergantung pada TC sebelumnya), langkah 7, 18, 22, dan 31 (berpindah ke menu lain sebelum membuka ulang Activity Log; langkah TC "klik menu lain lalu klik kembali Activity Log"), langkah 14 dan 21 (ganti akun eksplisit), langkah 40 (memulihkan ukuran jendela), dan langkah 47 (menutup walkthrough yang masih terbuka dengan `[Skip]` supaya spec tidak berakhir dengan walkthrough terbuka; S-03).
- Pada TC-21 langkah TC nomor 3 "kedua akun membuka ulang halaman" dikerjakan per akun: akun Read Only membuka ulang sebelum ganti akun, lalu akun Total Control membuka ulang sesudah ganti akun kembali. Spec berakhir pada akun Total Control, akun default suite (S-07).
- Menu Client dipilih spec sebagai "menu lain di sidebar"; TC tidak menyebut nama menu. Flag halaman tujuan disetel true agar walkthrough halaman tujuan tidak muncul.
- Langkah "Verifikasi walkthrough tampil dari Step 1" pada TC-23 adalah anchor sebelum asersi tertutup; Expected TC-23 tidak memuatnya.
- Spec di atas smell 35 langkah (47 langkah). Alasan: seluruh blok satu kelas (Guided Tooltip dan flag seen), empat TC berdiri sendiri karena tiap TC menyetel flag sendiri sebelum dijalankan, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ganti akun TC-21 eksplisit dan berakhir di akun default suite (bagian 3, pemisah beda akun).
- Temuan untuk QA:
  - TC-19, TC-22, dan TC-23 menyebut "menu lain" tanpa nama menu; spec memakai menu Client (pilihan spec, bukan nilai TC). QA perlu menetapkan menu tujuan.
  - TC-21 menyebut "akun kedua `readOnlyAdminConsole`" tanpa email penuh; spec memakai Pre-setup No 2 `readOnlyAdminConsolePrincipal_automated_{namaCompany}@qwertysystem.net` dan env `AC_RO_PASSWORD` (nama usulan, perlu didaftarkan tim FE).
  - TC-23 langkah 1 tidak menyebut ukuran viewport baru; spec mengubah ukuran jendela ke ukuran yang ditetapkan tim FE dan memulihkannya.
  - TC-23 Expected b berbunyi "muncul lagi dari Step 1 lalu tertutup saat navigasi"; spec mengasersi kedua klausa berurutan.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, terdaftar di `.env.example` dan `spectra.config.ts`) serta `AC_RO_PASSWORD` (nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`).
