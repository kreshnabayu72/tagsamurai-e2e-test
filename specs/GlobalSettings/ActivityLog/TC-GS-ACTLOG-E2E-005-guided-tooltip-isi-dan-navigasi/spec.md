---
id: TC-GS-ACTLOG-E2E-005-guided-tooltip-isi-dan-navigasi
title: "Guided Tooltip: Isi dan Navigasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-18
  - TC-GS-ACTLOG-21
  - TC-GS-ACTLOG-23
coverage:
  web: automated
---

# Guided Tooltip: Isi dan Navigasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup: tidak ada selain akun aktor. Spec tidak membuat data dan tidak membutuhkan baris log tertentu.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md); spec ini mengatur flag sendiri sesudah hook suite, yaitu menyetel `guided_tooltip_seen_gs-activity-log` ke belum `true` untuk akun penguji sebelum langkah 1. Hook suite `after` memulihkan nilai awal.
- Kemampuan teknis (disediakan tim FE/BE): (1) menyetel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true` untuk akun penguji dan membacanya, tanpa memuat ulang halaman; spec memakainya sebelum langkah 1, sebagai langkah penghubung antar-TC, dan untuk mengasersi flag `seen`; tidak ada endpoint yang dikarang di spec ini. (2) Membaca keyboard focus elemen dan menekan tombol keyboard (`Enter`, `←`, `→`, `Esc`).
- State global yang diubah: flag Guided Tooltip akun penguji (dipulihkan hook suite `after`). Spec tidak mengubah format tanggal atau jam.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-18: Isi 2 step Guided Tooltip sesuai PRD

1. Buka Global Settings > Activity Log untuk pertama kali (flag belum `true`)
2. Verifikasi walkthrough tampil dengan Step 1
3. Verifikasi Step 1: sorotan pada Tabs "Session" / "User Action"
4. Verifikasi Step 1: indikator `Step 1 of 2`
5. Verifikasi Step 1: Title `Two Kinds of Activity`
6. Verifikasi Step 1: Description `Switch tabs to review sign-in activity or data changes.`
7. Klik `[Next]`
8. Verifikasi Step 2: sorotan pada icon Filter di toolbar
9. Verifikasi Step 2: indikator `Step 2 of 2`
10. Verifikasi Step 2: Title `Narrow Down the Log`
11. Verifikasi Step 2: Description `Narrow down the log to find specific entries. Available filters depend on the tab you are on.`
12. Verifikasi Step 2: tombol `[Next]` berubah menjadi `[Done]`
13. Klik `[Done]`

### TC-GS-ACTLOG-21: Navigasi Next, Back, Skip lewat tombol dan lewat klik overlay, serta Done

14. Setel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true` tanpa memuat ulang halaman
15. Klik `[?]`
16. Verifikasi Step 1: tombol `[Back]` tidak tampil (hidden)
17. Klik `[Next]`
18. Verifikasi `[Next]` memajukan ke Step 2
19. Klik `[Back]`
20. Verifikasi `[Back]` kembali ke Step 1
21. Klik `[Next]` ke Step 2
22. Verifikasi Step 2 (terakhir): tombol utama berlabel `[Done]`
23. Klik `[Done]`
24. Verifikasi `[Done]` menutup walkthrough
25. Verifikasi `[Done]` mengatur flag `seen`
26. Setel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true`
27. Klik `[?]`
28. Klik `[Skip]`
29. Verifikasi `[Skip]` menutup walkthrough
30. Verifikasi `[Skip]` mengatur flag `seen`
31. Setel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true`
32. Klik `[?]`
33. Klik area overlay gelap di luar sorotan
34. Verifikasi klik overlay gelap menutup walkthrough
35. Verifikasi klik overlay gelap mengatur flag `seen`

### TC-GS-ACTLOG-23: Operasi keyboard

36. Setel ulang flag `guided_tooltip_seen_gs-activity-log` ke belum `true`
37. Klik `[?]`
38. Verifikasi tooltip box menerima keyboard focus saat aktif
39. Tekan `Enter`
40. Verifikasi `Enter` memajukan ke step berikutnya (Step 2)
41. Tekan `←`
42. Verifikasi `←` kembali ke step sebelumnya (Step 1)
43. Tekan `→`
44. Verifikasi `→` memajukan ke step berikutnya (Step 2)
45. Tekan `Esc`
46. Verifikasi `Esc` menutup walkthrough (Skip)
47. Verifikasi `Esc` mengatur flag `seen`

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-18, 21, 23). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-GS-ACTLOG-19, 20, dan 22 (walkthrough otomatis kunjungan pertama, replay, keluar tanpa selesai) ada di spec `TC-GS-ACTLOG-E2E-006-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai`; TC-GS-ACTLOG-24 (Step 2 mobile) ada di spec `TC-GS-ACTLOG-E2E-007-mobile-card-session-card-user-action-guided-step-2-dan-download`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 13 (`[Done]` menutup walkthrough otomatis TC-18 supaya flag `seen` ter-set dan layar bersih), 14, 26, 31, dan 36 (menyetel ulang flag ke belum `true` sebelum bagian TC berikutnya; lihat Temuan untuk QA).
- Langkah 14 disetel ulang tanpa memuat ulang halaman karena TC-21 dan TC-23 menyebut pengguna sudah berada di Activity Log dan memulai walkthrough lewat `[?]`.
- Spec di atas smell 35 langkah (47 langkah). Alasan: seluruh blok satu topik (Guided Tooltip pada halaman yang sama) dan satu mode, tanpa data yang dibuat; Expected TC-21 dan TC-23 bermajemuk (lima dan lima klausa) dan dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-21 dan TC-23 mensyaratkan flag belum `true` sambil menyatakan pengguna sudah di Activity Log dan memulai lewat `[?]`; dengan flag belum `true`, walkthrough seharusnya muncul otomatis saat halaman dibuka (TC-18, TC-19). Spec menyetel flag setelah halaman terbuka tanpa muat ulang.
  - TC-21 langkah 3 sampai 5 mengasersi `[Done]`, `[Skip]`, dan klik overlay "mengatur flag `seen`" berurutan pada akun yang sama; setelah `[Done]` flag sudah `true` sehingga `[Skip]` dan overlay tidak terbedakan. Spec menyetel ulang flag sebelum tiap penutupan (langkah 26 dan 31) supaya tiap asersi bermakna; tidak ada instruksi ini di TC.
  - TC-21 langkah 4 dan 5 memulai walkthrough lewat `[?]` ketika flag sudah `true`; TC tidak menyatakan efek `[?]` pada flag (lihat TC-20 di spec 006).
  - Cara membaca flag `guided_tooltip_seen_gs-activity-log` tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
