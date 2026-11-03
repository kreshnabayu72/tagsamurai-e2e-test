---
id: TC-AC-ACAL-E2E-006-guided-tooltip-isi-dan-navigasi
title: "Guided Tooltip: Isi dan Navigasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-18
  - TC-AC-ACAL-20
  - TC-AC-ACAL-24
coverage:
  web: automated
---

# Guided Tooltip: Isi dan Navigasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md); spec ini mengatur flag sendiri sesudah hook suite, yaitu menyetel flag `guided_tooltip_seen_ac-activity-log` (`page_key` `ac-activity-log`, PRD §4.7) ke belum ada untuk akun aktor pada langkah penghubung sebelum tiap TC. Hook suite `after` memulihkan nilai awal.
- Kemampuan teknis (disediakan tim FE/BE): menyetel ulang flag `guided_tooltip_seen_ac-activity-log` ke belum ada untuk akun aktor dan membacanya; tidak ada endpoint yang dikarang di spec ini. Navigasi keyboard (`Enter`, `→`, `←`, `Esc`) dan membaca fokus keyboard.
- Data: tidak ada data log yang dibuat atau dibaca.
- State global yang diubah: flag Guided Tooltip akun aktor (dipulihkan hook suite `after`).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-18: Guided Tooltip muncul otomatis saat kunjungan pertama, konten 3 step

1. Setel flag `guided_tooltip_seen_ac-activity-log` ke belum ada untuk akun aktor
2. Klik menu Activity Log di sidebar Admin Console
3. Verifikasi Step 1 menyorot Tabs "Session" / "User Action"
4. Verifikasi Step 1: Title `Activity Log`
5. Verifikasi Step 1: Description `This page is a read-only record of activity across the Admin Console. Switch tabs to review staff sessions or data changes.`
6. Verifikasi Step 1: tombol `[Back]` Hidden
7. Klik `[Next]`
8. Verifikasi Step 2 menyorot icon Filter
9. Verifikasi Step 2: Title `Narrow Down the Log`
10. Verifikasi Step 2: Description `Narrow down the log to find specific entries. Available filters depend on the tab you are on.`
11. Klik `[Next]`
12. Verifikasi Step 3 menyorot icon Download
13. Verifikasi Step 3: Title `Download Log`
14. Verifikasi Step 3: Description `Export the log you are viewing. The export respects your current filters and search.`
15. Verifikasi Step 3: tombol `[Next]` berganti `[Done]`
16. Klik `[Skip]` untuk menutup walkthrough

### TC-AC-ACAL-20: Guided Tooltip, [Back] kembali ke step sebelumnya

17. Setel flag `guided_tooltip_seen_ac-activity-log` ke belum ada untuk akun aktor
18. Klik menu Activity Log di sidebar Admin Console
19. Klik `[Next]` ke Step 2
20. Verifikasi Step 2 tampil dengan tombol `[Back]`
21. Klik `[Back]`
22. Verifikasi kembali ke Step 1
23. Verifikasi tombol `[Back]` Hidden pada Step 1
24. Klik `[Skip]` untuk menutup walkthrough

### TC-AC-ACAL-24: Accessibility Guided Tooltip, navigasi keyboard

25. Setel flag `guided_tooltip_seen_ac-activity-log` ke belum ada untuk akun aktor
26. Klik menu Activity Log di sidebar Admin Console
27. Tekan `Enter`
28. Verifikasi pindah ke Step 2
29. Verifikasi kotak tooltip menerima fokus keyboard
30. Tekan `→`
31. Verifikasi pindah ke Step 3
32. Tekan `←`
33. Verifikasi kembali ke Step 2
34. Tekan `Esc`
35. Verifikasi walkthrough tertutup (setara `[Skip]`)

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-18, 20, 24). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-ACAL-19, 21, 22, dan 23 ada di spec `TC-AC-ACAL-E2E-007-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 17, dan 25 (menyetel flag ke belum ada karena precondition tiap TC mensyaratkan flag `seen` belum ada, sedangkan hook suite menyetelnya true; TC-20 dan TC-24 tidak bergantung pada hasil TC sebelumnya).
- Langkah penghubung penutup walkthrough (langkah 16 dan 24, `[Skip]`, tanpa Verifikasi): walkthrough TC-18 (Step 3) dan TC-20 (Step 1) ditutup sebelum klik menu pada langkah 18 dan 26 agar overlay tidak menghalangi klik (S-09, S-03). Walkthrough TC-24 ditutup oleh langkah 34 (`Esc`).
- Step 1 sampai 3 tiap diasersi sebelum `[Next]` berikutnya (state sementara; bagian 8b butir 5); sorotan elemen target, Title, dan Description dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-18 dan TC-20 tidak menyebut apakah klik menu Activity Log saat halaman sudah terbuka membuka ulang walkthrough; spec mengasumsikan klik menu memicu walkthrough otomatis selama flag belum ada.
  - TC-18 Expected a menyorot "Tabs Session/User Action"; PRD §4.7 menyebut target `Tabs — "Session" / "User Action"`; spec mengikuti PRD untuk kata target.
  - Apakah klik menu sidebar saat walkthrough terbuka memilih `[Skip]` atau berpindah menu belum ditetapkan di TC/PRD; spec menutup walkthrough dengan `[Skip]` dan menunggu konfirmasi QA/FE.
  - TC-24 tidak menyebut elemen mana yang menerima fokus selain "kotak tooltip"; spec mengasersi kotak tooltip.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
