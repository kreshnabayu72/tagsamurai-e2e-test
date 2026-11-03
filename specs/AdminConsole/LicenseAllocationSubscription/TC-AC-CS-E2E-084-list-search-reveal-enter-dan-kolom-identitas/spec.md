---
id: TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas
title: "List Search: Reveal, Enter, dan Kolom Identitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-311
  - TC-AC-CS-312
  - TC-AC-CS-313
  - TC-AC-CS-314
coverage:
  web: automated
---

# List Search: Reveal, Enter, dan Kolom Identitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Hendra Wijaya, Total Control Principal PT ABC (Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Pre-setup (kelas e, baca-saja): dataset uji #82, yaitu 120 baris term di tab Current dan 60 baris di tab History untuk Client campuran (Plan Owner PT Maju Bersama dan CV Karya Mandiri); jumlah total baris diturunkan dari seeding dataset, bukan dibaca dari satu halaman tabel (bagian 8b butir 10). Spec tidak menulis ke dataset; Search, Filter, Sort, dan Pagination dibersihkan sebagai langkah penghubung antar blok TC.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-311: Search: reveal, auto-focus, placeholder, tooltip, dan icon clear tanpa filter live

1. Arahkan kursor ke ikon Search
2. Verifikasi tooltip "Search" muncul saat hover
3. Klik ikon Search
4. Verifikasi kotak pencarian melebar
5. Verifikasi kursor otomatis fokus di input
6. Verifikasi placeholder "Search by subscription ID, client name, product, plan, plan owner, or status" tampil
7. Ketik `Apotek` tanpa menekan Enter
8. Verifikasi icon clear `(✕)` muncul di sisi kanan input
9. Verifikasi tabel menampilkan sedikitnya satu baris
10. Verifikasi tabel belum tersaring
11. Klik icon panah `(←)` di kiri toolbar untuk menutup kotak pencarian dan mereset tabel

### TC-AC-CS-312: Search: Enter menjalankan pencarian, clear `(✕)` tidak mereset tabel, Enter kosong mereset, panah collapse mereset langsung

12. Klik ikon Search di toolbar
13. Ketik Search `Apotek`, tekan Enter
14. Verifikasi sedikitnya satu baris tampil
15. Verifikasi hanya baris yang memuat `Apotek` tampil
16. Klik icon `(✕)`
17. Verifikasi teks input terhapus
18. Verifikasi kursor tetap fokus di input
19. Verifikasi tabel tetap menampilkan hasil `Apotek`
20. Tekan Enter pada input kosong
21. Verifikasi tabel kembali menampilkan semua baris tab "Current"
22. Ketik Search `Apotek`, tekan Enter, lalu klik icon panah `(←)` di kiri toolbar
23. Verifikasi kotak pencarian ditutup
24. Verifikasi keyword dikosongkan
25. Verifikasi tabel langsung reset

### TC-AC-CS-313: Search kolom Subscription ID: substring dan tanpa membedakan huruf besar kecil

26. Ketik Search `20260819-00002`, tekan Enter
27. Verifikasi baris `SUBS-20260819-00002` Percetakan Mega tampil
28. Verifikasi baris lain yang ID-nya tidak memuat keyword tidak tampil
29. Ganti isi kotak search dengan `subs-20260819-00002`, tekan Enter
30. Verifikasi baris `SUBS-20260819-00002` tampil

### TC-AC-CS-314: Search kolom Client dan Plan Owner: substring dan tanpa membedakan huruf besar kecil

31. Ganti isi kotak search dengan `sehat`, tekan Enter
32. Verifikasi baris Client `Apotek Sehat Sentosa` tampil
33. Ganti isi kotak search dengan `KARYA`, tekan Enter
34. Verifikasi baris dengan Plan Owner `CV Karya Mandiri (Partner)` tampil tanpa membedakan huruf besar kecil
35. Verifikasi baris yang tidak memuat keyword pada kolom mana pun tidak tampil

## Notes

- Langkah penghubung: penutupan kotak Search lewat `(←)` (bagian 8b butir 9). Langkah "Ketik Search ..., tekan Enter" membuka input bila tertutup.
- TC-AC-CS-311 sampai TC-AC-CS-314 berjalan pada tab "Current" dengan dataset #82 sehingga baris pembanding (sedikitnya satu baris) tersedia sebelum asersi universal; asersi "hanya baris yang memuat" pada TC-AC-CS-313 dan TC-AC-CS-314 memakai baris yang cocok sebagai pembanding.
- Temuan untuk QA: (1) TC-AC-CS-312 Expected d menyebut `(←)` menutup kotak pencarian, mengosongkan keyword, dan mereset tabel sekaligus; spec memecahnya per klausa (S-01). (2) TC-AC-CS-314 butir b menyebut kolom Plan Owner `CV Karya Mandiri (Partner)` sebagai baris yang cocok untuk `KARYA`; spec mengasersi baris dengan Plan Owner itu tanpa nama Client. (3) TC-AC-CS-312 langkah 3 dan 4 menyebut kursor tetap fokus setelah `(✕)`; spec memakai Expected b TC.
