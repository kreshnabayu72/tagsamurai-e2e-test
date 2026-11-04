---
id: TC-FA-TDC-E2E-052-create-rate-tampil-mengikuti-metode-read-only-dan-batas-seratus
title: "Create - Rate Tampil Mengikuti Metode, Read-only, dan Batas 100"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-165
  - TC-FA-TDC-166
  - TC-FA-TDC-167
  - TC-FA-TDC-171
coverage:
  web: automated
---

# Create - Rate Tampil Mengikuti Metode, Read-only, dan Batas 100

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: tujuh class seed bawaan (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE) dalam keadaan belum diubah. Master Data Count Limit belum tercapai.
- Data Dinamis: tidak ada data yang disimpan (tidak ada Submit). Nilai yang dipilih atau diketik: Asset Type `Non-building`; Useful Life `8`, `1`, `2`; Allowed Methods `Straight Line` dan `Declining Balance`; nilai `99` yang diketik pada rate (ditolak karena read-only).
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-165: Create - rate Straight Line dan Declining Balance tampil atau tersembunyi mengikuti metode terpilih

1. Klik `+ Class` di toolbar
2. Pilih Asset Type `Non-building` dan isi Useful Life `8`
3. Pilih Allowed Methods `Straight Line`
4. Verifikasi teks Straight Line Rate (%) tampil dengan helper "Calculated from useful life."
5. Verifikasi Declining Balance Rate (%) tidak tampil
6. Tambahkan Allowed Methods `Declining Balance`
7. Verifikasi kedua teks rate tampil
8. Lepas Allowed Methods `Straight Line`
9. Verifikasi Declining Balance Rate (%) tampil
10. Verifikasi Straight Line Rate (%) tidak tampil
11. Lepas Allowed Methods `Declining Balance`
12. Verifikasi kedua teks rate tidak tampil

### TC-FA-TDC-166: Create - rate tidak tampil selama Useful Life belum terisi lalu dihitung seketika

13. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
14. Kosongkan Useful Life
15. Verifikasi Straight Line Rate (%) dan Declining Balance Rate (%) tidak tampil, tanpa nilai angka dan tanpa placeholder "—" (kedua metode sudah dipilih)
16. Ketik Useful Life `8`
17. Verifikasi Straight Line Rate (%) "12.5" muncul seketika tanpa Submit
18. Verifikasi Declining Balance Rate (%) "25" muncul seketika tanpa Submit
19. Hapus Useful Life
20. Verifikasi kedua rate kembali tidak tampil

### TC-FA-TDC-167: Create - rate adalah teks read-only dan tidak menerima input

21. Isi Useful Life `8`
22. Klik teks Straight Line Rate (%) dan ketik `99`
23. Klik teks Declining Balance Rate (%) dan ketik `99`
24. Verifikasi Straight Line Rate (%) tetap "12.5"
25. Verifikasi Declining Balance Rate (%) tetap "25"
26. Verifikasi tidak ada kursor input atau caption error pada kedua rate

### TC-FA-TDC-171: Create - Declining Balance Rate dibatasi paling besar 100 (Useful Life 1 dan 2)

27. Isi Useful Life `1` dan amati kedua rate
28. Verifikasi Straight Line Rate (%) "100" (Useful Life `1`)
29. Verifikasi Declining Balance Rate (%) "100" (Useful Life `1`; 2 × 100 dibatasi 100)
30. Isi Useful Life `2` dan amati kedua rate
31. Verifikasi Straight Line Rate (%) "50" (Useful Life `2`)
32. Verifikasi Declining Balance Rate (%) "100" (Useful Life `2`)
33. Klik `[Clear Field]`
34. Klik ikon ✕ pada Drawer

## Notes

- Langkah penghubung (S-03): langkah 13 dan 14 (menyiapkan keadaan awal TC-FA-TDC-166: kedua metode terpilih dan Useful Life kosong; Asset Type `Non-building` sudah terpilih pada langkah 2), langkah 21 (mengisi ulang Useful Life sebagai keadaan awal TC-FA-TDC-167), langkah 33 (`[Clear Field]`; S-09), langkah 34 (menutup Drawer yang bersih).
- Langkah 27 dan 30 mengganti isi Useful Life yang sudah berisi dengan nilai baru; langkah 2 mengikuti TC-FA-TDC-165 ("Pilih Asset Type `Non-building` dan isi Useful Life `8`") dalam satu langkah.
- Asersi absence langkah 5, 10, 12, 15, dan 20 didahului anchor positif pada Drawer yang sama (rate lain tampil atau field Useful Life tampil; 8b.2). Langkah 15 didahului pemilihan kedua metode (langkah 13) sebagai pemicu.
- Pembagian TC lintas spec: perhitungan rate dan pembulatan (TC-FA-TDC-168 sampai 170, 172) ada di spec `TC-FA-TDC-E2E-053-create-rate-bulat-pembulatan-dua-desimal-half-up-dan-useful-life-maksimum`.
- Temuan untuk QA:
  - TC-FA-TDC-167 tidak menyebut cara mengasersi "tidak ada kursor input"; spec mengasersi elemen tidak menjadi input dan tidak ada caption error.
  - Rate di Drawer ditulis tanpa simbol `%` karena label field memuat `(%)` (keputusan NC-22 di TC); spec mengikuti TC.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
