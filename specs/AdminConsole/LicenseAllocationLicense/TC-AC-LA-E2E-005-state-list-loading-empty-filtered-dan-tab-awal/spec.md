---
id: TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal
title: "State List: Loading, Empty, Empty Filtered, Pemulihan, dan Tab Awal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-10
  - TC-AC-LA-11
  - TC-AC-LA-12
  - TC-AC-LA-13
  - TC-AC-LA-16
  - TC-AC-LA-17
coverage:
  web: automated
---

# State List: Loading, Empty, Empty Filtered, Pemulihan, dan Tab Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kemampuan teknis: `Spectra.intercept()` atas respons list License Allocation di atas backend nyata (tunda 5 detik dan respons list kosong untuk tab Current dan tab History). Endpoint list tidak tertulis di TC; kebutuhan intercept ditulis oleh tim FE (S-13). Intercept dilepas segera setelah dipakai (S-09).
- Empty state genuinely kosong (TC-AC-LA-11 dan TC-AC-LA-12) dibentuk dengan respons list yang di-intercept kosong, karena seed Pre-setup #54 men-seed minimal 30 alokasi pada scope Principal yang sama dan Pre-setup TC tidak memuat akun atau tenant tanpa alokasi (lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-17: Tab awal List adalah Current

1. Buka dashboard Admin Console
2. Klik menu `License Allocation` di sidebar (Allocation)
3. Verifikasi List terbuka dengan tab `Current` aktif
4. Verifikasi pagination halaman 1 dengan 10 data per halaman
5. Verifikasi sort default Last Updated Newest First

### TC-AC-LA-13: Empty state hasil Search tanpa kecocokan

6. Klik ikon Search
7. Ketik Search `zzzzqqqq`, tekan Enter
8. Verifikasi Illustration tampil
9. Verifikasi Title: `No results found`
10. Verifikasi Description: `Try adjusting your search or filter.`
11. Verifikasi Title bukan Title empty state genuinely kosong `No current license allocations`
12. Verifikasi state error `Unable to load this data.` tidak tampil

### TC-AC-LA-16: Pemulihan dari empty filtered

13. Ganti isi kotak search dengan `zzzzqqqq`, tekan Enter
14. Verifikasi empty state `No results found` tampil
15. Kosongkan isi kotak search, tekan Enter
16. Verifikasi tabel kembali menampilkan baris data tab Current
17. Verifikasi empty state `No results found` tidak tampil

### TC-AC-LA-10: Loading List

18. Pasang intercept respons list License Allocation: tunda 5 detik
19. Klik menu `License Allocation` di sidebar (membuka List dengan respons list ditahan)
20. Verifikasi komponen Loading tampil di area tabel
21. Verifikasi empty state dan state error tidak tampil selama loading
22. Lepas tahanan respons list dan tunggu tabel selesai dimuat

### TC-AC-LA-11: Empty state tab Current

23. Pasang intercept respons list License Allocation: respons kosong untuk tab Current dan tab History
24. Klik menu `License Allocation` di sidebar (membuka List tab Current)
25. Verifikasi Illustration tampil
26. Verifikasi Title: `No current license allocations`
27. Verifikasi Description: `Allocations that are waiting for a decision, not started yet, or in effect will appear here. Finished ones are in History.`
28. Verifikasi tidak ada tombol di dalam empty state

### TC-AC-LA-12: Empty state tab History

29. Klik tab `History`
30. Verifikasi Illustration tampil
31. Verifikasi Title: `No license allocation history yet`
32. Verifikasi Description: `Expired, rejected, and canceled allocations will appear here.`
33. Lepas intercept respons list

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah membuka dashboard, langkah pasang dan lepas intercept, langkah `Klik ikon Search`, dan langkah menunggu tabel selesai dimuat. Urutan TC dalam spec: TC-AC-LA-17, TC-AC-LA-13, TC-AC-LA-16, TC-AC-LA-10, TC-AC-LA-11, TC-AC-LA-12, supaya state intercept dibangun terakhir dan dilepas segera (S-09, S-10).
- TC-AC-LA-11 dan TC-AC-LA-12 memakai satu intercept respons kosong yang dipasang sebelum membuka List dan dilepas sesudah TC-AC-LA-12.
- TC-AC-LA-14 dan TC-AC-LA-15 (error load List dengan Try Again) ditangani spec lain; spec ini tidak memuat state error kecuali asersi tidak tampil.
- Temuan untuk QA:
  - TC-AC-LA-11 dan TC-AC-LA-12 mensyaratkan scope tanpa alokasi sama sekali (`Principal baru tanpa data`), sedangkan Pre-setup #54 men-seed minimal 30 alokasi pada scope Total Control Principal #1 dan Pre-setup TC tidak memuat akun atau tenant kosong; spec memakai respons list yang di-intercept kosong. Butuh keputusan QA: akun atau tenant kosong atau intercept.
  - TC-AC-LA-10 Data Uji menyebut `tunda 5 detik` tetapi tidak menyebut endpoint GET list; endpoint tidak dikarang di spec (S-13).
  - TC-AC-LA-17 langkah 1 tidak menyebut cara menuju dashboard Admin Console dari List yang dibuka hook `beforeEach` suite; spec membuka dashboard lebih dulu sebagai langkah pertama.
  - TC-AC-LA-17 Expected c (`Sort default Last Updated Newest First`) hanya bermakna bila halaman pertama memuat sedikitnya dua nilai Last Updated berbeda; seed #54 diasumsikan memenuhinya.
