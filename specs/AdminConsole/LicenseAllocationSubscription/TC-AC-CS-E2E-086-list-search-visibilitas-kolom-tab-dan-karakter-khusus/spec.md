---
id: TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus
title: "List Search: Visibilitas Kolom, Tab, dan Karakter Khusus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-319
  - TC-AC-CS-320
  - TC-AC-CS-321
  - TC-AC-CS-322
  - TC-AC-CS-323
coverage:
  web: automated
---

# List Search: Visibilitas Kolom, Tab, dan Karakter Khusus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Cache Setup Column browser dikosongkan di hook `before` dan dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bagian 4).
- State global yang diubah: visibilitas kolom Client (TC-AC-CS-319) yang disimpan di cache browser; dipulihkan dengan menghapus preferensi kolom di hook `after` dan sebagai langkah penghubung.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-319: Search terikat visibilitas kolom: kolom disembunyikan tidak dapat dicari

1. Klik header kolom Actions `⋯`, lalu hilangkan centang kolom `Client` pada overlay Column Visibility
2. Ketik Search `Apotek`, tekan Enter
3. Verifikasi empty state "No results found" tampil sehingga keyword `Apotek` tidak mencocokkan baris saat kolom Client disembunyikan
4. Tampilkan kembali kolom `Client` lewat overlay Column Visibility, lalu ganti isi kotak search dengan `Apotek`, tekan Enter
5. Verifikasi baris `Apotek Sehat Sentosa` tampil

### TC-AC-CS-320: Search melakukan trim spasi tepi pada query

6. Ganti isi kotak search dengan ` Apotek ` (spasi di kedua tepi), tekan Enter
7. Verifikasi baris `Apotek Sehat Sentosa` tampil sama dengan hasil `Apotek`
8. Verifikasi isi kotak pencarian tetap apa adanya (` Apotek `)
9. Ganti isi kotak search dengan tiga spasi `   `, tekan Enter
10. Verifikasi tabel kembali ke state tanpa pencarian

### TC-AC-CS-321: Search hanya berlaku pada tab aktif

11. Ganti isi kotak search dengan `Optik`, tekan Enter
12. Verifikasi hanya baris `Optik Cahaya` berstatus Waiting for Approval tampil di tab "Current"
13. Klik tab "History"
14. Verifikasi tab "History" tidak membawa keyword sebelumnya
15. Verifikasi tab "History" menampilkan baris History tanpa penyaringan
16. Ketik Search `Optik`, tekan Enter
17. Verifikasi hanya baris Canceled `Optik Cahaya` tampil di tab "History"
18. Klik tab "Current"

### TC-AC-CS-322: Search mencakup baris Trial

19. Ganti isi kotak search dengan `Sejahtera`, tekan Enter
20. Verifikasi baris term paid milik `PT Sejahtera` tampil
21. Verifikasi baris Trial `SUBS-20260810-00001` milik `PT Sejahtera` tampil
22. Verifikasi baris Trial tampil dengan badge Trial pada kolom Plan

### TC-AC-CS-323: Keyword dengan karakter khusus dicocokkan sebagai teks biasa

23. Ganti isi kotak search dengan `<script>alert(1)</script>`, tekan Enter
24. Verifikasi keyword markup tidak dieksekusi dan tidak ada dialog script
25. Verifikasi empty state "No results found" tampil
26. Ganti isi kotak search dengan `%`, tekan Enter
27. Verifikasi jumlah baris hasil Search `%` lebih sedikit dari total baris tab "Current" (dataset #82, jumlah total dari seeding)
28. Verifikasi karakter `%` dicocokkan sebagai teks biasa, bukan pola pencarian, sehingga tidak menampilkan semua baris
29. Hapus preferensi kolom di browser lewat kemampuan tim FE

## Notes

- Langkah penghubung: penggantian isi kotak Search, klik tab "Current" setelah blok TC-AC-CS-321, dan penghapusan preferensi kolom di akhir.
- Temuan untuk QA: (1) TC-AC-CS-319 butir a menyebut "kolom lain tetap dapat dicari" tanpa langkah observasi di TC; spec tidak mengasersinya terpisah. (2) TC-AC-CS-320 butir a memakai hasil `Apotek` sebagai pembanding tanpa menyebut baris; spec memakai baris `Apotek Sehat Sentosa` dari TC-AC-CS-319. (3) TC-AC-CS-323 tidak menyebut cara membuktikan markup tidak dieksekusi selain tidak adanya dialog script; spec mengasersi tidak ada dialog. (4) TC-AC-CS-319 langkah 1 memakai overlay Column Visibility sebagai langkah aksi (bukan Setup Column modal). (5) TC-AC-CS-323 butir b ("tidak menampilkan semua baris") tidak menyebut apakah `%` menghasilkan empty state atau himpunan bagian baris; spec memakai pembanding jumlah baris terhadap total dataset sebagai anchor positif (8b.2) dan tidak mengasersi empty state.
