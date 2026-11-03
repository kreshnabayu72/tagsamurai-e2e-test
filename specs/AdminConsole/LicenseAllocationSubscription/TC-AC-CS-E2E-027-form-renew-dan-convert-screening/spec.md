---
id: TC-AC-CS-E2E-027-form-renew-dan-convert-screening
title: "Form Renew dan Convert: Screening"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-103
  - TC-AC-CS-104
  - TC-AC-CS-105
  - TC-AC-CS-131
  - TC-AC-CS-106
coverage:
  web: automated
---

# Form Renew dan Convert: Screening

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; form hanya dibuka lalu ditutup tanpa Submit):
  - Client `Warung Kopi Senja+{runId}-027` dengan satu term Active FAMS plan Professional, Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama (Distributor), tanpa successor dan tanpa trial aktif (padanan Pre-setup #69), plan Professional berjalan di versi 3.
  - Client `Klinik Harapan Bunda A+{runId}-027`: trial SAMS Growth Active (Start 10/08/26, End 08/09/26), Plan Owner CV Karya Mandiri, tanpa term paid SAMS (padanan Pre-setup #71).
  - Client `Klinik Harapan Bunda B+{runId}-027`: term paid SAMS Growth Active (End Date 14/09/26, Plan Owner PT Maju Bersama) dan trial SAMS Professional Active (Plan Owner CV Karya Mandiri) (padanan Pre-setup #73).
  - Keadaan #71 dan #73 tidak berlaku bersamaan pada satu Client sehingga spec memakai dua Client seed.

## Test Steps

### TC-AC-CS-103: Screening modal Renew Subscription dengan Keep current plan

1. Ketik Search `Warung Kopi Senja+{runId}-027`, tekan Enter
2. Klik ikon `⋯` pada baris Client `Warung Kopi Senja+{runId}-027`, lalu pilih `Renew`
3. Pilih Renewal Option `Keep current plan`
4. Verifikasi header modal berjudul "Renew Subscription"
5. Verifikasi Client dan Product Disabled dan terisi `Warung Kopi Senja+{runId}-027` dan `FAMS`
6. Verifikasi Renewal Option * (radio horizontal) memuat `Keep current plan` (default) dan `Change plan`
7. Verifikasi field Plan Hidden dan Start Date tidak ada (mulai otomatis)
8. Verifikasi Preview Current plan menampilkan nama dan versi, dan Duration * memiliki helper "Whole years, minimum 1"
9. Verifikasi footer hanya memuat `[Clear Field]` dan `[Submit]` rata kanan tanpa checkbox "Stay on this form after submitting" (varian Renew)

### TC-AC-CS-104: Screening modal Renew Subscription dengan Change plan

10. Pilih Renewal Option `Change plan`
11. Verifikasi field Plan * tampil dengan placeholder "Select plan"
12. Buka dropdown Plan
13. Verifikasi dropdown Plan memuat sedikitnya satu opsi plan lain (daftar opsi termuat)
14. Verifikasi plan `Professional` yang sedang berjalan tidak ada di opsi Plan
15. Tekan `Esc` untuk menutup dropdown
16. Verifikasi Client dan Product tetap Disabled dan Start Date tetap tidak ada
17. Klik `[✕]` pada header modal
18. Klik `(←)` pada kotak Search

### TC-AC-CS-105: Screening modal Convert Trial mode New dengan Start Date terkunci hari ini

19. Ketik Search `Klinik Harapan Bunda A+{runId}-027`, tekan Enter
20. Klik ikon `⋯` pada baris trial Client `Klinik Harapan Bunda A+{runId}-027`, lalu pilih `Convert`
21. Verifikasi header modal berjudul "Convert Trial"
22. Verifikasi ringkasan trial sumber di atas Preview menampilkan plan dan End Date trial serta sisa hari trial yang hangus
23. Verifikasi Client dan Product Disabled dan terisi, dan Renewal Option tidak dirender
24. Verifikasi Start Date Disabled bernilai `19/08/26` dengan helper "Fixed to today when converting a trial"
25. Verifikasi tombol `[+ New Client]` tidak ada pada dropdown Client
26. Verifikasi footer hanya memuat `[Clear Field]` dan `[Submit]` rata kanan tanpa checkbox "Stay on this form after submitting" (varian Convert)

### TC-AC-CS-131: Start Date varian Convert terkunci dan tidak dapat diubah

27. Klik field Start Date
28. Verifikasi Start Date Disabled bernilai `19/08/26`
29. Verifikasi date picker tidak terbuka
30. Verifikasi helper "Fixed to today when converting a trial" tampil
31. Klik `[✕]` pada header modal
32. Klik `(←)` pada kotak Search

### TC-AC-CS-106: Screening modal Convert Trial mode Renewal dengan Renewal Option Disabled

33. Ketik Search `Klinik Harapan Bunda B+{runId}-027`, tekan Enter
34. Klik ikon `⋯` pada baris trial SAMS Professional Client `Klinik Harapan Bunda B+{runId}-027`, lalu pilih `Convert`
35. Verifikasi header modal berjudul "Convert Trial"
36. Verifikasi Renewal Option Disabled dengan `Change plan` terpilih
37. Verifikasi field Plan tampil
38. Buka dropdown Plan
39. Verifikasi dropdown Plan memuat sedikitnya satu opsi plan
40. Verifikasi opsi Plan mengecualikan plan term paid yang berjalan
41. Tekan `Esc` untuk menutup dropdown Plan
42. Verifikasi Start Date Hidden karena mulai otomatis mengikuti predecessor
43. Klik `[✕]` pada header modal

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-104 melanjutkan modal TC-AC-CS-103 (dependensi TC) dan TC-AC-CS-131 melanjutkan modal TC-AC-CS-105 (dependensi TC); langkah dependensi tidak diulang karena modal yang sama masih terbuka.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 1, 19, 33), `(←)` pada kotak Search (langkah 18, 32), `Esc` menutup dropdown Plan (langkah 15, 41), membuka dropdown Plan (langkah 38), dan `[✕]` pada form bersih (langkah 17, 31, 43; tanpa dialog Unsaved Changes). Langkah 3 memilih Renewal Option `Keep current plan` yang menjadi langkah TC-AC-CS-103 Langkah 2.
- Anchor absence (butir 8b.2): dropdown Plan dibuka pada langkah 12 dan Verifikasi opsi plan lain tampil pada langkah 13 mendahului langkah 14 (Plan `Professional` tidak ada); dropdown Plan dibuka pada langkah 38 dan opsi plan tampil pada langkah 39 mendahului langkah 40 (plan term paid yang berjalan tidak ada).
- Ukuran: 43 langkah, di atas 35 langkah. Alasan: semua blok satu kelas (screening form Renew dan Convert), dua modal dibuka sekali untuk lima TC, dan jumlah langkah berasal dari Verifikasi per klausa Expected (S-01); pemecahan menambah login dan seeding tanpa menambah isolasi.
- Temuan untuk QA:
  - TC-AC-CS-105 dan TC-AC-CS-106 tidak menyebut Allocation ID baris trial; spec mencari lewat nama Client seed.
  - Teks ringkasan trial sumber pada form Convert tidak dinyatakan persis oleh TC (GAP-600); spec hanya mengasersi isi ringkasan (plan, End Date trial, sisa hari trial yang hangus) sesuai Expected.
