---
id: TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas
title: "List Filter: Opsi Status dan Perilaku per Kelas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-331
  - TC-AC-CS-332
  - TC-AC-CS-333
  - TC-AC-CS-334
  - TC-AC-CS-335
coverage:
  web: automated
---

# List Filter: Opsi Status dan Perilaku per Kelas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-331: Opsi Status pada tab Current hanya status milik tab Current

1. Klik ikon Filter, lalu buka dropdown Status
2. Verifikasi sedikitnya satu opsi Status tampil di dropdown Status
3. Verifikasi opsi hanya dari Waiting for Approval, Pending, Active, Expired, Grace yang ada pada baris tab "Current"
4. Verifikasi Renewed, Rejected, Canceled, Archive, Purge, Deleted, dan Converted tidak tampil
5. Tutup dropdown Status dan panel Filter

### TC-AC-CS-332: Opsi Status pada tab History termasuk Converted tanpa bergantung filter Type

6. Klik tab "History", klik ikon Filter, lalu buka dropdown Status tanpa memilih filter Type
7. Verifikasi sedikitnya satu opsi Status tampil di dropdown Status
8. Verifikasi opsi hanya status yang ada pada baris tab "History": Renewed, Rejected, Canceled, Archive, Purge, Deleted, dan Converted
9. Verifikasi `Converted` tampil tanpa perlu memilih Type `Trial`
10. Verifikasi Waiting for Approval, Pending, Active, Expired, dan Grace tidak tampil
11. Tutup dropdown Status dan panel Filter, lalu klik tab "Current"

### TC-AC-CS-333: Filter dropdown kelas entitas: Client, Plan, Plan Owner

12. Klik ikon Filter, pilih Client `PT Sejahtera`, klik `[Apply]`
13. Verifikasi tabel menampilkan sedikitnya satu baris
14. Verifikasi hanya baris PT Sejahtera tampil
15. Klik `[Clear Field]`, pilih Plan `Professional`, klik `[Apply]`
16. Verifikasi tabel menampilkan sedikitnya satu baris
17. Verifikasi hanya baris Plan Professional tampil
18. Klik `[Clear Field]`, pilih Plan Owner `CV Karya Mandiri (Partner)`, klik `[Apply]`
19. Verifikasi tabel menampilkan sedikitnya satu baris
20. Verifikasi hanya baris dengan Plan Owner `CV Karya Mandiri (Partner)` tampil

### TC-AC-CS-334: Filter dropdown kelas enum: Product dan Type

21. Klik `[Clear Field]`, pilih Product `SIEM`, klik `[Apply]`
22. Verifikasi tabel menampilkan sedikitnya satu baris
23. Verifikasi hanya baris Product SIEM tampil
24. Klik `[Clear Field]`, pilih Type `Trial`, klik `[Apply]`
25. Verifikasi tabel menampilkan sedikitnya satu baris
26. Verifikasi hanya baris bertipe Trial tampil
27. Klik `[Clear Field]`, pilih Type `Paid`, klik `[Apply]`
28. Verifikasi sedikitnya satu baris bertipe Paid tampil
29. Verifikasi baris bertipe Trial tidak tampil

### TC-AC-CS-335: Filter Status pada tab Current

30. Klik `[Clear Field]`, pilih Status `Active`, klik `[Apply]`
31. Verifikasi tabel menampilkan sedikitnya satu baris
32. Verifikasi hanya baris Active (paid dan Trial) tampil
33. Klik `[Clear Field]`, pilih Status `Expired`, klik `[Apply]`
34. Verifikasi tabel menampilkan sedikitnya satu baris
35. Verifikasi hanya baris Expired (paid dan Trial) tampil
36. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Alasan spec lebih dari sekitar 35 langkah: seluruh blok memakai satu Filter Panel, satu layar, dan satu dataset baca-saja (#82); langkah per variasi filter memuat anchor sedikitnya satu baris, dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung: penutupan dropdown dan panel, pindah tab, serta `[Clear Field]` dan `[Apply]` antar variasi filter.
- Panel Filter tetap terbuka setelah `[Apply]` sehingga variasi filter berikutnya dimulai dari `[Clear Field]` pada panel yang sama.
- Temuan untuk QA: (1) TC-AC-CS-333 sampai TC-AC-CS-335 menulis "Ganti ke ..." tanpa menyebut pembersihan nilai sebelumnya; spec memakai `[Clear Field]` sebagai langkah penghubung. (2) TC-AC-CS-334 butir c ("Type `Paid` tidak menampilkan baris Trial") memakai Verifikasi absence dengan baris Paid tampil sebagai pembanding hasil filter.
