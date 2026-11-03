---
id: TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom
title: "List Sort: Default dan Siklus Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-349
  - TC-AC-CS-350
  - TC-AC-CS-351
  - TC-AC-CS-352
  - TC-AC-CS-353
coverage:
  web: automated
---

# List Sort: Default dan Siklus Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Tabel "Kolom uji sort teks" (TC-AC-CS-351): Product dengan nilai `FAMS`, `SAMS`, `SIEM`; Plan Owner dengan nilai `CV Karya Mandiri (Partner)` dan `PT Maju Bersama (Distributor)` (dua Plan Owner dataset #82; ascending `CV Karya Mandiri (Partner)` lebih dulu, descending sebaliknya); Client dan Plan tanpa nilai sampel karena TC dan dataset #82 tidak menyebutnya (lihat Temuan untuk QA). Tiap kolom diuji dengan siklus tiga klik header (ascending, descending, default).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-349: Default sort tab Current: Client A-Z lalu ID terbaru di atas dalam Client yang sama

1. Ketik Search `PT Sejahtera`, tekan Enter
2. Verifikasi tabel menampilkan sedikitnya satu baris
3. Verifikasi baris terurut Client A-Z (case-insensitive)
4. Verifikasi baris Client sama terurut ID terbaru di atas: `SUBS-20260810-00001` sebelum `SUBS-20260101-00001`
5. Verifikasi ikon sort kolom Client menunjukkan ascending
6. Klik `(←)` pada kotak Search tab "Current" untuk membersihkan Search `PT Sejahtera`

### TC-AC-CS-350: Default sort tab History: ID terbaru di atas

7. Klik tab "History"
8. Verifikasi tabel menampilkan sedikitnya satu baris
9. Verifikasi baris terurut Created At descending teramati lewat Subscription ID: ID terbaru di atas
10. Verifikasi tidak ada kolom sort aktif yang ditandai pada header kolom data
11. Klik tab "Current"

### TC-AC-CS-351: Siklus sort tiga state kolom teks: Client, Product, Plan, Plan Owner

12. Klik header `Product` (state 1)
13. Verifikasi urutan ascending A-Z tanpa membedakan huruf besar kecil (`FAMS`, `SAMS`, `SIEM`)
14. Klik header `Product` lagi (state 2)
15. Verifikasi urutan descending Z-A (`SIEM`, `SAMS`, `FAMS`)
16. Klik header `Product` lagi (state 3)
17. Verifikasi urutan kembali ke default tab
18. Untuk setiap kolom pada tabel "Kolom uji sort teks" selain Product (Client, Plan, Plan Owner), ulangi langkah 12 sampai 17 dengan nilai sampel kolom itu
19. Verifikasi badge pada kolom Plan tidak memengaruhi urutan

### TC-AC-CS-352: Siklus sort tiga state kolom Subscription ID berbasis string

20. Klik header `Subscription ID`
21. Verifikasi ascending berbasis string: `SUBS-20250801-00001` sebelum `SUBS-20260101-00001` (baris tab "Current", Pre-setup #51 dan #61)
22. Klik header `Subscription ID` lagi
23. Verifikasi urutan descending
24. Klik header `Subscription ID` lagi
25. Verifikasi urutan kembali ke default sort tab

### TC-AC-CS-353: Siklus sort tiga state kolom Status berdasarkan label badge

26. Klik header `Status`
27. Verifikasi ascending berdasarkan label badge A-Z (`Active`, `Expired`, `Grace`, `Pending`, `Waiting for Approval`)
28. Klik header `Status` lagi
29. Verifikasi descending (`Waiting for Approval` lebih dulu)
30. Klik header `Status` lagi
31. Verifikasi urutan kembali ke default

## Notes

- Langkah penghubung: Search (R-16: untuk menemukan baris target) dan pembersihan Search `(←)` di tab "Current" sebelum pindah tab (tab menyimpan keadaan Search sehingga sort Product dan urutan ID di blok berikutnya tidak boleh terfilter `PT Sejahtera`), serta pindah tab. Langkah 12 sampai 17 diulang per kolom pada tabel "Kolom uji sort teks" di Prerequisites (bagian 8b butir 7).
- Alasan spec lebih dari sekitar 35 langkah: seluruh blok berbagi satu layar, satu dataset (#82), dan satu jenis harness (volume data), dan langkah yang diulang per kolom atau per keyword memakai parameter yang tertulis di Prerequisites; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: (1) TC-AC-CS-351 butir d menyebut perilaku sama pada Client, Plan, dan Plan Owner tanpa nilai contoh; nilai sampel Client dan Plan (dua nilai pertama ascending) tidak disebut TC maupun dataset #82 dan perlu diisi QA; spec mengasersi urutan A-Z, Z-A, dan default tanpa membedakan huruf besar kecil. (2) TC-AC-CS-350 tidak menyebut kondisi Search; spec membersihkan Search di tab "Current" sebelum pindah ke tab "History" (TC-AC-CS-34 dan TC-AC-CS-349/350 berbeda soal Search tab disimpan atau tidak). (3) TC-AC-CS-349 tidak menyebut cara menampilkan dua baris `PT Sejahtera` pada halaman pertama; spec memakai Search `PT Sejahtera` yang tidak mengubah sort default.
