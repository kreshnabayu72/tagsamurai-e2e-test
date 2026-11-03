---
id: TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal
title: "Form Renew: Validasi dan Preview Renewal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-125
  - TC-AC-CS-126
  - TC-AC-CS-127
  - TC-AC-CS-128
  - TC-AC-CS-129
  - TC-AC-CS-130
  - TC-AC-CS-137
  - TC-AC-CS-138
coverage:
  web: automated
---

# Form Renew: Validasi dan Preview Renewal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Warung Kopi Senja+{runId}-033` dengan satu term Active FAMS plan Professional (Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama (Distributor)), tanpa successor, berjalan di plan versi 3 sementara plan `Professional` sudah punya versi terbaru 4 (padanan Pre-setup #69). Tidak ada Submit sukses pada spec ini, sehingga term seed tidak berubah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan; sesi API aktor Principal): mengarsipkan plan `Enterprise` dan `Professional` hingga tersimpan lalu memulihkannya (Un-archive) di hook `after`; membaca jumlah term Client seed lewat fixture BE.

## Test Steps

### TC-AC-CS-125: Validasi Plan wajib pada Renew Change plan

1. Ketik Search `Warung Kopi Senja+{runId}-033`, tekan Enter
2. Klik ikon `⋯` pada baris Client `Warung Kopi Senja+{runId}-033`, lalu pilih `Renew`
3. Pilih Renewal Option `Change plan`
4. Isi Duration `1` tanpa memilih Plan, lalu klik `[Submit]`
5. Verifikasi error inline "Plan must not be empty"
6. Verifikasi modal tetap terbuka

### TC-AC-CS-137: Preview Renewal menampilkan kalimat saat plan baru berlaku di masa depan

7. Pilih Plan `Enterprise`
8. Verifikasi baris tambahan "Your current plan stays active until 31/08/26. The selected plan will take effect starting 01/09/26." tampil
9. Verifikasi Renewal term menampilkan mulai `01/09/26` dan akhir `31/08/27`

### TC-AC-CS-130: Duration batas bawah 1 tahun diterima pada Renew

10. Pilih Renewal Option `Keep current plan`, isi Duration `1`
11. Verifikasi tidak ada error Duration
12. Verifikasi Preview menampilkan tanggal mulai `01/09/26` dan tanggal akhir `31/08/27`

### TC-AC-CS-138: Preview Renewal menampilkan Current plan dan badge Updated to v[N]

13. Amati Preview Current plan pada Renewal Option `Keep current plan` dengan Duration `1`
14. Verifikasi Current plan menampilkan `Professional` dengan versi 3
15. Verifikasi badge "Updated to v4" tampil karena versi terbaru berbeda

### TC-AC-CS-129: Validasi Duration kurang dari 1 tahun pada Renew

16. Isi Duration `0`, lalu klik `[Submit]`
17. Verifikasi error inline "Duration must be at least 1 year"
18. Verifikasi jumlah term Client `Warung Kopi Senja+{runId}-033` tetap 1 (dibaca lewat fixture BE)

### TC-AC-CS-128: Validasi Duration kosong pada Renew

19. Kosongkan Duration, lalu klik `[Submit]`
20. Verifikasi error inline "Duration must not be empty"
21. Verifikasi modal tetap terbuka

### TC-AC-CS-126: Plan Change plan di-Archive sesi lain sebelum Submit pada Renew

22. Pilih Renewal Option `Change plan`, pilih Plan `Enterprise`, isi Duration `1`
23. Arsipkan plan `Enterprise` lewat sesi API aktor hingga status Archive tersimpan
24. Klik `[Submit]`
25. Verifikasi error inline "This plan no longer exists. Please select another."
26. Buka dropdown Plan
27. Verifikasi dropdown Plan memuat sedikitnya satu opsi plan
28. Verifikasi field Plan dikosongkan dan opsi dimuat ulang tanpa `Enterprise`
29. Tekan `Esc` untuk menutup dropdown Plan
30. Verifikasi Duration `1` dipertahankan
31. Pulihkan plan `Enterprise` (Un-archive) lewat sesi API aktor

### TC-AC-CS-127: Plan yang sedang berjalan di-Archive sesi lain pada Renew Keep current plan

32. Pilih Renewal Option `Keep current plan`, isi Duration `1`
33. Arsipkan plan `Professional` lewat sesi API aktor hingga status Archive tersimpan
34. Klik `[Submit]`
35. Verifikasi error "This plan no longer exists. Please select another."
36. Verifikasi field Plan tetap tersembunyi
37. Pilih Renewal Option `Change plan` untuk memilih plan lain
38. Verifikasi Duration `1` dipertahankan
39. Pulihkan plan `Professional` (Un-archive) lewat sesi API aktor, lalu klik `[✕]` pada header modal
40. Verifikasi dialog Unsaved Changes tampil
41. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Satu pembukaan form Renew untuk seluruh TC; urutan mengikuti S-10 dan S-14 (validasi tanpa efek server lebih dulu, dua TC yang mengarsipkan plan di akhir); urutan nomor TC tidak berurutan di spec.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 1), memilih Renewal Option dan mengisi Duration antar kasus (langkah 10, 22, 32), membuka dropdown Plan sebagai anchor absence (butir 8b.2; langkah 26 dan 27, positif sebelum absence pada langkah 28) dengan `Esc` pada langkah 29, dan Un-archive plan (langkah 31, 39; juga di hook `after`).
- Arsip plan lewat sesi API ditulis "... hingga ... tersimpan" (R-20).
- Penutupan form dirty pada langkah 39 sampai 41 mengikuti S-08.
- Ekspansi: 41 langkah nominal karena delapan TC dalam satu form Renew; kegagalan satu blok validasi tidak menghalangi blok lain, tetapi pemecahan menambah login dan seed tanpa menambah isolasi karena seed term tidak berubah (tidak ada Submit sukses). Alasan pertahanan di atas ~35 langkah: semua blok satu kelas (fungsional validasi Renew), satu dataset, dan satu form.
- Temuan untuk QA:
  - TC-AC-CS-125 dan TC-AC-CS-126 menyebut Plan `Enterprise` dan Plan `Growth` pada Change plan tanpa menyatakan versinya; spec mengikuti nama plan.
  - TC-AC-CS-127 Expected b tidak menyatakan state Renewal Option sesudah error ("requester beralih ke `Change plan`" adalah tindakan requester); spec memilih `Change plan` di langkah 37.
  - TC-AC-CS-138 Precondition menyatakan plan `Professional` berjalan di versi 3 dengan versi terbaru 4; kemampuan membuat versi baru plan tidak ada di TC, PRD, atau LLD sehingga ditulis sebagai fixture "disediakan tim FE/BE".
  - TC-AC-CS-126 dan TC-AC-CS-127 tidak menyebut cara sesi lain mengarsipkan plan; ditulis sebagai kemampuan "disediakan tim FE/BE".
