---
id: TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker
title: "List Sort: Tanggal, Nilai Kosong, dan Tie-breaker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-354
  - TC-AC-CS-355
  - TC-AC-CS-356
  - TC-AC-CS-357
coverage:
  web: automated
---

# List Sort: Tanggal, Nilai Kosong, dan Tie-breaker

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Cache Setup Column browser dikosongkan di hook `before` dan dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bagian 4).
- Tabel "Kolom uji sort tanggal" (TC-AC-CS-354): Start Date, End Date, Grace End. Kolom Grace End ditampilkan lewat modal Setup Column (precondition TC, dipakai sebagai precondition dan tidak diasersi), lalu cache Setup Column dihapus di hook `after`.
- Pengamatan baris Start Date "—" (Waiting for Approval) memakai pindah ke halaman terakhir atau pertama sebelum asersi posisi (S-14).
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-354: Siklus sort tiga state kolom tanggal: Start Date, End Date, Grace End

1. Klik header kolom Actions `⋯`, klik `[Setup Column]`, centang `Grace End`, lalu klik `[Save]`
2. Tunggu aksi selesai (modal Setup Column tertutup)
3. Klik header `Start Date` (state 1)
4. Verifikasi tabel menampilkan sedikitnya satu baris
5. Verifikasi urutan ascending Oldest First
6. Klik header `Start Date` lagi (state 2)
7. Verifikasi urutan descending Newest First
8. Klik header `Start Date` lagi (state 3)
9. Verifikasi urutan kembali ke default
10. Untuk setiap kolom pada tabel "Kolom uji sort tanggal" selain Start Date (End Date, Grace End), ulangi langkah 3 sampai 9

### TC-AC-CS-355: Nilai tanggal kosong berada di akhir saat ascending dan di awal saat descending

11. Klik header `Start Date` sekali (ascending), lalu pindah ke halaman terakhir
12. Verifikasi baris dengan Start Date "—" tampil di akhir
13. Klik header `Start Date` sekali lagi (descending), lalu pindah ke halaman pertama
14. Verifikasi baris dengan Start Date "—" tampil di awal
15. Klik header `Start Date` lagi untuk kembali ke default

### TC-AC-CS-356: Tie-breaker sort deterministik antar halaman

16. Klik header `Product` sekali, lalu telusuri halaman 1 sampai halaman terakhir
17. Verifikasi baris bernilai Product sama diurutkan menurut default sort tab sehingga urutan stabil
18. Verifikasi tidak ada baris ganda atau terlewat antar halaman
19. Klik header `Product` dua kali lagi untuk kembali ke default, lalu pindah ke halaman pertama

### TC-AC-CS-357: Kolom Actions bukan kolom data dan tidak dapat di-sort

20. Klik header kolom Actions `⋯`
21. Verifikasi klik header Actions membuka overlay Column Visibility dan tidak mengurutkan tabel
22. Verifikasi header Actions tidak menampilkan ikon sort

## Notes

- Langkah penghubung: Setup Column untuk menampilkan Grace End, pindah halaman, dan pengembalian sort ke default antar blok. Langkah 3 sampai 9 diulang per kolom pada tabel "Kolom uji sort tanggal" di Prerequisites (bagian 8b butir 7).
- Langkah penghubung (S-03, bagian 8b butir 8): langkah `Tunggu aksi selesai` (langkah 2) menunggu modal Setup Column tertutup sesudah `[Save]` sebelum langkah berikutnya mengubah permukaan.
- Temuan untuk QA: (1) TC-AC-CS-354 tidak menyebut kolom tertentu yang diamati selain urutan; spec mengasersi urutan oldest first, newest first, dan default. (2) TC-AC-CS-355 tidak menyebut jumlah halaman; spec memakai pindah ke halaman terakhir atau pertama (S-14). (3) TC-AC-CS-356 "telusuri halaman 1 sampai halaman terakhir" tidak menyebut cara mengamati ketiadaan baris ganda; spec memakai pengamatan Subscription ID antar halaman. (4) TC-AC-CS-354 baris Grace End pada nilai kosong tidak diasersi (hanya urutan).
