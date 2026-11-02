---
id: TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci
title: "Edit: Screening dan Field Terkunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-212
  - TC-AC-CS-213
  - TC-AC-CS-214
  - TC-AC-CS-215
  - TC-AC-CS-236
coverage:
  web: automated
---

# Edit: Screening dan Field Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup (milik aktor, dibaca; satu-satunya perubahan di spec ini hanya pada TC-AC-CS-236, yang tidak menyimpan): `SUBS-20260819-00001` Client Apotek Sehat Sentosa FAMS Growth Waiting for Approval, Duration 1 year(s) (#49); `SUBS-20260819-00003` Client Toko Serba Ada FAMS Enterprise Renewal Waiting for Approval (#67); `SUBS-20260817-00001` hasil Convert mode New Client Toko Lancar Jaya FAMS Professional Waiting for Approval, Start Date terkunci `19/08/26` (#111, #112); `SUBS-20260819-00004` Trial Client PT Bintang Timur FAMS Growth Waiting for Approval (#59); tanggal acuan uji `19/08/26`.
- Data Dinamis: tidak ada; spec tidak menyimpan perubahan. Form Edit yang dirty ditutup dengan `[Leave]` sehingga record tidak berubah.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`).

## Test Steps

### TC-AC-CS-212: Screening modal Edit term paid mode New

1. Ketik Search `Apotek Sehat Sentosa`, tekan Enter
2. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
3. Verifikasi Header: Judul "Edit Subscription"
4. Verifikasi Body: Client, Product, Plan, dan Pay From Disabled dengan nilai record
5. Verifikasi Body: Renewal Option tidak dirender
6. Verifikasi Body: Duration Enabled bernilai `1`
7. Verifikasi Body: Start Date Enabled dengan nilai record
8. Verifikasi Body: blok Payment menampilkan Estimated Cost yang dihitung dari snapshot harga term
9. Verifikasi Footer: `[Clear Field]` dan `[Save]` rata kanan tanpa checkbox Stay on this form
10. Klik `[✕]`

### TC-AC-CS-213: Screening modal Edit term mode Renewal

11. Ganti isi kotak search dengan `Toko Serba Ada`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260819-00003` lalu pilih `Edit`
12. Verifikasi Renewal Option Disabled dengan nilai record
13. Verifikasi Duration Enabled
14. Verifikasi Start Date Hidden karena mulai otomatis
15. Verifikasi Client, Product, dan Plan Disabled
16. Verifikasi Payment dihitung ulang dari snapshot harga term
17. Klik `[✕]`

### TC-AC-CS-214: Screening modal Edit term hasil Convert mode New mengunci Start Date

18. Ganti isi kotak search dengan `Toko Lancar Jaya`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260817-00001` lalu pilih `Edit`
19. Verifikasi Start Date Disabled bernilai hari ini `19/08/26` dengan helper "Fixed to today when converting a trial"
20. Verifikasi Duration Enabled
21. Klik `[✕]`

### TC-AC-CS-215: Screening modal Edit baris Trial FAMS

22. Ganti isi kotak search dengan `PT Bintang Timur`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260819-00004` lalu pilih `Edit`
23. Verifikasi Client, Product, dan Plan Disabled
24. Verifikasi Trial Duration, Trial Asset Quota, dan Trial Concurrent User Quota Enabled dengan nilai record
25. Verifikasi Trial Log Source Quota tidak tampil untuk FAMS
26. Klik `[✕]`

### TC-AC-CS-236: Clear Field pada Edit hanya mengosongkan field yang dapat diubah

27. Ganti isi kotak search dengan `Apotek Sehat Sentosa`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Edit`
28. Klik `[Clear Field]`
29. Verifikasi Duration dan Start Date dikosongkan (bukan dikembalikan ke nilai tersimpan)
30. Verifikasi Client, Product, Plan, dan Pay From tetap terisi dan Disabled
31. Verifikasi modal tetap terbuka tanpa dialog konfirmasi
32. Klik `[✕]`
33. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil
34. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; Search pada kotak terisi ditulis "ganti isi kotak search dengan", 8b.9); `✕` menutup modal Edit yang bersih tanpa dialog (TC-AC-CS-212 sampai TC-AC-CS-215); form dirty TC-AC-CS-236 ditutup deterministik dengan dialog `Unsaved Changes` dan `[Leave]` (S-08, S-09).
- Temuan untuk QA: (1) TC-AC-CS-212 Expected b.ii dan TC-AC-CS-213 menyebut "nilai record" tanpa nilai Start Date atau Renewal Option baris Pre-setup #49 dan #67; spec mengasersi terisi nilai tersimpan record. (2) TC-AC-CS-214 menyebut Pre-setup #111 pada term `SUBS-20260817-00001` sedangkan Dinamis TC-AC-CS-214 memuat Client `Toko Lancar Jaya` yang sama dengan Pre-setup #112 (trial SAMS); kedua nomor dirujuk. (3) Estimated Cost TC-AC-CS-212 b.iii tidak menyebut nilainya sehingga diasersi hanya tampil.
