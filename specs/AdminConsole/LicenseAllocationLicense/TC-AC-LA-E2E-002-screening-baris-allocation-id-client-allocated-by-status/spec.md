---
id: TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status
title: "Screening Baris List: Allocation ID, Client, Allocated By, dan Badge Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-4
  - TC-AC-LA-5
  - TC-AC-LA-6
  - TC-AC-LA-7
coverage:
  web: automated
---

# Screening Baris List: Allocation ID, Client, Allocated By, dan Badge Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup yang dibaca (tidak diubah): #19 PT Sejahtera (FAMS Professional Paid Active `SUBS-20260101-A1B2C`), #41 alokasi `Waiting for Approval`, #46 alokasi `Pending`, #47 alokasi `Active`, #48 alokasi `Canceled`, #50 alokasi `Rejected`, #51 alokasi `Expired`, dan #54 (memuat baris `LALC-20260105-00001` serta alokasi yang dibuat `Dewi Anggraini` (Pre-setup #4)). Allocation ID tiap seed dirujuk lewat `Fixture.license-allocation-license` (kunci seed41, seed46, seed47, seed48, seed50, seed51, seedDewiAnggraini).
- Satu alokasi pada seed #54 dibuat `Dewi Angkasa` yang juga tampil `Dewi A`; baris TC-AC-LA-6 adalah baris `Dewi Anggraini`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-4: Allocation ID sebagai text link

1. Ketik Search `LALC-20260105-00001`, tekan Enter
2. Amati warna teks Allocation ID pada baris `LALC-20260105-00001`
3. Verifikasi warna teks Allocation ID default netral seperti teks body tabel, tanpa garis bawah
4. Arahkan kursor ke Allocation ID `LALC-20260105-00001`
5. Verifikasi saat hover warna teks berubah menjadi warna primary Admin Console (merah), tanpa garis bawah
6. Klik Allocation ID `LALC-20260105-00001`
7. Verifikasi modal `Allocation Log` terbuka untuk Allocation ID `LALC-20260105-00001`
8. Verifikasi tab dan List di belakang modal tidak berubah
9. Tutup modal dengan `[✕]`

### TC-AC-LA-5: Klik nama Client membuka Client Detail

10. Catat nilai kolom baris `LALC-20260105-00001` sebelum klik nama Client
11. Klik nama Client `PT Sejahtera` pada baris alokasi
12. Verifikasi halaman Client Detail `PT Sejahtera` terbuka pada tab browser yang sama (bukan tab baru)
13. Kembali ke List dengan tombol Back browser
14. Verifikasi nilai kolom baris `LALC-20260105-00001` sama dengan yang dicatat sebelum klik (List tidak mengubah data)

### TC-AC-LA-6: Format Allocated By dan tooltip nama lengkap

15. Ganti isi kotak search dengan Allocation ID seed alokasi `Dewi Anggraini` (`Fixture.license-allocation-license.seedDewiAnggraini`), tekan Enter
16. Amati kolom Allocated By pada baris itu
17. Verifikasi kolom Allocated By menampilkan teks biasa `Dewi A` (nama depan utuh, inisial nama belakang)
18. Verifikasi nilai Allocated By tidak berupa badge
19. Hover nilai Allocated By `Dewi A`
20. Verifikasi tooltip nama lengkap `Dewi Anggraini`

### TC-AC-LA-7: Badge Status pada List

21. Ganti isi kotak search dengan Allocation ID seed `Waiting for Approval` (Pre-setup #41), tekan Enter
22. Verifikasi badge Status `Waiting for Approval`: severity warning
23. Ganti isi kotak search dengan Allocation ID seed `Pending` (Pre-setup #46), tekan Enter
24. Verifikasi badge Status `Pending`: severity warning
25. Ganti isi kotak search dengan Allocation ID seed `Active` (Pre-setup #47), tekan Enter
26. Verifikasi badge Status `Active`: severity success
27. Klik `(←)` pada kotak Search
28. Klik tab `History`
29. Ketik Search Allocation ID seed `Expired` (Pre-setup #51), tekan Enter
30. Verifikasi badge Status `Expired`: severity danger
31. Ganti isi kotak search dengan Allocation ID seed `Rejected` (Pre-setup #50), tekan Enter
32. Verifikasi badge Status `Rejected`: severity danger
33. Ganti isi kotak search dengan Allocation ID seed `Canceled` (Pre-setup #48), tekan Enter
34. Verifikasi badge Status `Canceled`: severity danger
35. Klik `(←)` pada kotak Search
36. Verifikasi sedikitnya satu baris tampil pada tab History
37. Verifikasi tidak ada baris dengan label badge `Completed` pada tab History
38. Klik tab `Current`
39. Verifikasi sedikitnya satu baris tampil pada tab Current
40. Verifikasi tidak ada baris dengan label badge `Completed` pada tab Current

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah `Catat nilai kolom`, `Kembali ke List`, penutupan modal, dan `Klik (←)` pada kotak Search (mereset tabel sebelum pindah tab).
- Expected g TC-AC-LA-7 (`Completed` tidak pernah tampil sebagai label badge) diperiksa pada baris halaman pertama tiap tab sesudah Search dikosongkan, dengan Verifikasi pembanding (sedikitnya satu baris tampil) lebih dulu.
- Seed Pre-setup #41, #46, #47, #48, #50, dan #51 hanya dibaca di spec ini.
- Spec ini lebih dari 35 langkah. Alasannya: semua blok satu topik (isi sel baris List pada tab Current dan History), memakai seed baca-saja yang sama, dan berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; badge enam status memerlukan enam pencarian baris yang berbeda.
- Temuan untuk QA:
  - TC-AC-LA-4 memakai `LALC-20260105-00001` sebagai baris Allocation ID, sedangkan TC-AC-LA-18 memakai ID yang sama untuk baris Concurrent User +5 alokasi `Sari P` berstatus `Active`; tidak jelas apakah keduanya satu record.
  - TC-AC-LA-5 Expected b (`List License Allocation tidak mengubah data`) tidak punya langkah observasi; spec menambah pencatatan nilai kolom dan pembandingan sesudah Back (S-03).
  - TC-AC-LA-6: seed #54 memuat dua pengguna yang tampil `Dewi A` (`Dewi Anggraini` dan `Dewi Angkasa`); TC tidak menyebut Allocation ID baris `Dewi Anggraini`, sehingga identitas baris dibaca dari fixture seed.
  - TC-AC-LA-7 langkah 1 (`Cari satu baris untuk tiap status`) tidak menyebut cara mencari; spec memakai Search Allocation ID seed.
