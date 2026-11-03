---
id: TC-AC-LA-E2E-102-sort-list-siklus-dan-alfabetis
title: "Sort List: Siklus Tiga Tahap dan Sort Alfabetis dengan atau Tanpa Nilai Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-304
  - TC-AC-LA-305
  - TC-AC-LA-306
coverage:
  web: automated
---

# Sort List: Siklus Tiga Tahap dan Sort Alfabetis dengan atau Tanpa Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; sedikitnya dua nilai distinct pada tiap kolom yang diurutkan; nilai `—` pada Product, Subscription ID, Plan, Plan Owner, dan Paid From untuk Asset Control Station, Storage, dan Payment `Free`) bersifat baca-saja untuk spec ini.
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Plan` dan `Paid From`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Parameter langkah 32 sampai 40 (TC-AC-LA-306), satu baris per kolom: `Product`, `Subscription ID`, `Plan`, `Plan Owner`, `Paid From`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-304: Siklus sort tiga tahap Last Updated

1. Verifikasi urutan awal default Last Updated Newest First
2. Klik header Last Updated
3. Verifikasi ascending (`↑`, Oldest First)
4. Klik header Last Updated
5. Verifikasi descending (`↓`, Newest First)
6. Klik header Last Updated
7. Verifikasi netral (indikator sort hilang)
8. Verifikasi urutan kembali ke default tabel

### TC-AC-LA-305: Sort alfabetis tanpa nilai kosong

9. Klik header Allocation ID
10. Verifikasi ascending A-Z tanpa membedakan huruf besar dan kecil
11. Klik header Allocation ID
12. Verifikasi descending Z-A
13. Klik header License Type
14. Verifikasi ascending A-Z dengan `Addon (Asset Control App)` paling awal
15. Pindah ke halaman terakhir
16. Verifikasi `Storage` paling akhir
17. Klik header License Type
18. Verifikasi descending Z-A
19. Klik header Client
20. Verifikasi ascending A-Z
21. Klik header Client
22. Verifikasi descending Z-A
23. Klik header Status
24. Verifikasi ascending menurut label badge (`Active`, `Pending`, `Waiting for Approval` pada tab Current)
25. Klik header Status
26. Verifikasi descending Z-A
27. Verifikasi tidak ada nilai kosong pada kolom Allocation ID, License Type, Client, dan Status

### TC-AC-LA-306: Sort alfabetis dengan nilai kosong di akhir

28. Klik `⋯` pada header kolom Actions
29. Klik `Setup Column...`
30. Centang `Plan` dan `Paid From`
31. Klik `[Save]`
32. Untuk setiap baris tabel parameter (langkah 32 sampai 40): klik header Kolom
33. Verifikasi ascending A-Z pada Kolom
34. Pindah ke halaman terakhir
35. Verifikasi `—` di akhir pada Kolom
36. Klik header Kolom
37. Pindah ke halaman 1
38. Verifikasi descending pada Kolom dengan `—` di awal
39. Pindah ke halaman 2 lalu kembali ke halaman 1
40. Verifikasi urutan baris pada Kolom sama dengan langkah 38 (deterministik antar halaman)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 32 sampai 40 diulang untuk lima baris tabel parameter (sekitar 45 langkah terekspansi; total sekitar 77 langkah terekspansi). Verifikasi tetap satu per klausa per iterasi (butir a sampai f TC-AC-LA-306).
- Alasan spec melewati sekitar 35 langkah: semua blok satu kelas harness (fungsional) dan satu dataset baca-saja (#54); tiap blok berdiri sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah berulang memakai parameter di tabel Prerequisites tanpa langkah bersyarat.
- Langkah penghubung (S-03): langkah 15, 34, 37, 39 (berpindah halaman agar posisi `—` dan kata "paling akhir" dapat diamati, S-14), langkah 28 sampai 31 (menampilkan kolom Plan dan Paid From, sesuai langkah 1 TC-AC-LA-306).
- Temuan untuk QA:
  - TC-AC-LA-305 Expected b menulis `Addon (Asset Control App)` sebagai nilai License Type, sedangkan Pre-setup #54 menulis `Asset Control App`; spec mengikuti Expected b.
  - TC-AC-LA-305 Expected e ("Tidak ada nilai kosong pada keempat kolom") diasersi pada baris yang tampil pada halaman teramati.
  - TC-AC-LA-306 Expected f ("deterministik antar halaman") tidak menyebut cara pembuktian; spec membandingkan urutan sebelum dan sesudah berpindah halaman.
