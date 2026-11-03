---
id: TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail
title: "List: Tanggal Kosong, Navigasi Baris, dan Masuk dari Client Detail"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-27
  - TC-AC-CS-28
  - TC-AC-CS-29
  - TC-AC-CS-31
  - TC-AC-CS-32
coverage:
  web: automated
---

# List: Tanggal Kosong, Navigasi Baris, dan Masuk dari Client Detail

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #49 `SUBS-20260819-00001` (Apotek Sehat Sentosa, Waiting for Approval), #52 `SUBS-20260812-00001` (Klinik Gigi Ceria, Rejected), #56 `SUBS-20260805-00001` (Optik Cahaya, Canceled), #61 `SUBS-20260101-00001` (PT Sejahtera, Active), Client `PT Sejahtera` (#38).
- Kemampuan teknis: cache Setup Column browser dikosongkan di hook `before` dan dipulihkan di hook `after` (bagian 4; disediakan tim FE).

## Test Steps

### TC-AC-CS-28: Kolom Grace End Hidden secara default sebagai kolom Curated

1. Klik header kolom `⋯`
2. Verifikasi kolom Grace End tidak tampil pada header tabel
3. Verifikasi overlay Column Visibility memuat Grace End dengan checkbox tidak tercentang dan enabled
4. Verifikasi delapan kolom lain tercentang dan enabled
5. Tutup overlay Column Visibility lewat `✕`

### TC-AC-CS-27: Tanggal kosong ditampilkan — untuk term tanpa otorisasi yang berlaku

6. Ketik Search `SUBS-20260819-00001`, tekan Enter
7. Verifikasi Start Date dan End Date menampilkan "—" pada baris Waiting for Approval
8. Klik tab `History`
9. Ganti isi kotak search dengan `SUBS-20260812-00001`, tekan Enter
10. Verifikasi Start Date dan End Date menampilkan "—" pada baris Rejected
11. Ganti isi kotak search dengan `SUBS-20260805-00001`, tekan Enter
12. Verifikasi Start Date dan End Date menampilkan "—" pada baris Canceled
13. Klik `(←)` pada kotak Search
14. Klik tab `Current`

### TC-AC-CS-29: Klik baris List membuka Subscription Detail

15. Ketik Search `SUBS-20260101-00001`, tekan Enter
16. Klik area baris `SUBS-20260101-00001` di luar kolom Client dan ikon `⋯`
17. Verifikasi halaman Subscription Detail untuk `SUBS-20260101-00001` terbuka
18. Verifikasi Breadcrumb `Allocation > Client Subscription > Detail`
19. Klik segmen `Client Subscription` pada Breadcrumb

### TC-AC-CS-31: Klik nama Client membuka Client Detail dan bukan Subscription Detail

20. Ganti isi kotak search dengan `SUBS-20260101-00001`, tekan Enter
21. Verifikasi warna teks nama Client `PT Sejahtera` netral saat idle
22. Arahkan kursor ke nama Client `PT Sejahtera`
23. Verifikasi warna teks nama Client berubah ke warna primary Admin Console tanpa underline saat hover
24. Klik nama `PT Sejahtera` pada baris `SUBS-20260101-00001`
25. Verifikasi halaman Client Detail `PT Sejahtera` terbuka
26. Verifikasi halaman Subscription Detail tidak terbuka

### TC-AC-CS-32: Masuk dari Client Detail membuka tab Current dengan filter Client ter-set

27. Klik `[Manage in Client Subscription →]` pada Client Detail `PT Sejahtera`
28. Verifikasi List terbuka di tab `Current`
29. Verifikasi Filter Client ter-set ke `PT Sejahtera`
30. Verifikasi sedikitnya satu baris tampil dan semua baris adalah baris PT Sejahtera
31. Klik tab `History`
32. Verifikasi term Renewed Client itu tersedia di tab `History`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search, klik tab `Current` dan `History`, tutup overlay Column Visibility, dan klik segmen `Client Subscription` pada Breadcrumb yang mengembalikan List sebelum TC-AC-CS-31.
- Urutan TC: 28, 27, 29, 31, 32. TC-AC-CS-31 berakhir di Client Detail `PT Sejahtera` dan TC-AC-CS-32 melanjutkan dari halaman itu; spec tidak membuka Client Detail lewat menu Client sebagai langkah terpisah.
- Klik ganda cepat, Back browser, Ctrl+klik, dan drag-select nama Client (TC-AC-CS-565, 566, 567) ada di spec 007; row action baris Waiting for Approval dan Canceled (TC-AC-CS-541) ada di spec 145.
- Temuan untuk QA:
  - TC-AC-CS-27 Precondition menyebut tab `Current` tetapi Expected b menyebut baris Rejected dan Canceled yang menurut TC-AC-CS-2 berada di tab `History`; spec mencari kedua baris itu di tab `History`.
  - TC-AC-CS-27 Expected b meminta "ketiga baris sekaligus" tidak ada sel kosong tanpa strip, padahal Search saling menggantikan sehingga tiga baris tidak pernah tampil bersamaan; spec mengasersi per baris pada langkah 7, 10, dan 12 dan tidak menulis asersi ketiga baris sekaligus.
  - TC-AC-CS-31 Expected c (warna netral saat idle dan berubah saat hover) tidak menyebut nilai warna; spec mengasersi teks Expected tanpa menambah nilai.
  - TC-AC-CS-32 Expected b menyebut "hanya baris PT Sejahtera tampil"; spec menuliskan pembanding sedikitnya satu baris sebelum asersi universal (bagian 8b butir 2).
