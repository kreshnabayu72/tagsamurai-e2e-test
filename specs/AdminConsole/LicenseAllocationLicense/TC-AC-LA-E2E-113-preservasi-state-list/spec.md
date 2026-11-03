---
id: TC-AC-LA-E2E-113-preservasi-state-list
title: "Preservasi State List: Refresh F5, Kembali dari Client Detail, Klik Menu, dan Allocation Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-349
  - TC-AC-LA-350
  - TC-AC-LA-351
  - TC-AC-LA-353
coverage:
  web: automated
---

# Preservasi State List: Refresh F5, Kembali dari Client Detail, Klik Menu, dan Allocation Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab; Client `PT Sejahtera`; License Type `Concurrent User`; dibaca saja untuk spec ini). Hasil Search `Sejahtera` dengan Filter License Type `Concurrent User` pada tab History dan hasil Search `Sejahtera` pada tab Current yang memuat lebih dari 10 baris agar halaman 2 tersedia pada langkah 5 dan 34 disediakan tim FE; seed #54 tidak menjamin jumlah itu (lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-349: Refresh F5

1. Klik tab `History`
2. Ketik Search `Sejahtera`, tekan Enter
3. Terapkan filter License Type `Concurrent User`
4. Klik header Quantity
5. Pindah ke halaman 2
6. Catat Search, Filter, Sort, halaman aktif, dan jumlah baris per halaman
7. Muat ulang halaman (F5)
8. Verifikasi List terbuka di tab `History`
9. Verifikasi Search `Sejahtera` sama seperti sebelum F5
10. Verifikasi Filter License Type `Concurrent User` sama seperti sebelum F5
11. Verifikasi Sort Quantity sama seperti sebelum F5
12. Verifikasi halaman aktif 2 sama seperti sebelum F5
13. Verifikasi jumlah baris per halaman sama seperti sebelum F5

### TC-AC-LA-350: Kembali dari Client Detail

14. Klik menu `License Allocation` di sidebar
15. Klik tab `History`
16. Ketik Search `Sejahtera`, tekan Enter
17. Klik nama Client `PT Sejahtera` pada baris untuk membuka Client Detail
18. Verifikasi Client Detail terbuka
19. Klik tombol Back browser
20. Verifikasi List kembali pada tab `History`
21. Verifikasi Search `Sejahtera` sama seperti sebelum ditinggalkan
22. Verifikasi Filter, Sort, dan paginasi sama seperti sebelum ditinggalkan

### TC-AC-LA-351: Klik ulang menu sidebar

23. Klik menu `License Allocation` di sidebar
24. Klik tab `History`
25. Ketik Search `Sejahtera`, tekan Enter
26. Klik menu `License Allocation` di sidebar
27. Verifikasi List terbuka pada tab `Current`
28. Verifikasi Search kosong
29. Verifikasi Filter default
30. Verifikasi Sort default Last Updated Newest First
31. Verifikasi halaman 1

### TC-AC-LA-353: Allocation Log tidak mereset state

32. Ketik Search `Sejahtera`, tekan Enter
33. Klik header Quantity
34. Pindah ke halaman 2
35. Buka Allocation Log salah satu baris dengan klik Allocation ID-nya
36. Tutup Allocation Log
37. Verifikasi Search `Sejahtera` tidak berubah
38. Verifikasi Sort Quantity tidak berubah
39. Verifikasi halaman 2 tidak berubah

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-AC-LA-352 (tab browser baru dan logout-login, kelas multi-konteks) ada di spec 139.
- Langkah `Terapkan filter <Field> <opsi>` berarti: klik ikon Filter, buka dropdown Field, centang opsi, klik `[Apply]`.
- Langkah penghubung (S-03): langkah 6 (mencatat state), langkah 14, 23, dan 26 (klik menu sidebar).
- Alasan spec melewati sekitar 35 langkah: semua blok satu topik (preservasi state List) pada satu dataset baca-saja; tiap blok memulai dari state default sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-LA-349 menyebut "halaman 2" pada hasil Search `Sejahtera` dengan Filter License Type tab History; kombinasi itu hampir pasti kurang dari 10 baris pada seed #54, sehingga halaman 2 tidak tersedia. Butuh data seed khusus atau penyesuaian TC.
  - TC-AC-LA-353 tidak menyebut cara membuka Allocation Log dan baris targetnya; spec memakai klik Allocation ID (TC-AC-LA-4) pada salah satu baris.
  - TC-AC-LA-350 tidak menyebut Filter dan Sort yang diterapkan sebelum meninggalkan List selain Search; spec mengasersi Filter, Sort, dan paginasi sama dengan keadaan sebelum ditinggalkan.
