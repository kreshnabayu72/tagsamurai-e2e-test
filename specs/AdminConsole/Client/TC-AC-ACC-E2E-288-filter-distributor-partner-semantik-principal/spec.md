---
id: TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal
title: "Filter Client List oleh Principal: Semantik Distributor (Transitif) dan Partner (Langsung), Relasi Transferred, Kombinasi AND dan OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-389
  - TC-AC-ACC-390
  - TC-AC-ACC-618
  - TC-AC-ACC-619
  - TC-AC-ACC-620
  - TC-AC-ACC-708
  - TC-AC-ACC-933
  - TC-AC-ACC-934
  - TC-AC-ACC-969
coverage:
  web: automated
---

# Filter Client List oleh Principal: Semantik Distributor (Transitif) dan Partner (Langsung), Relasi Transferred, Kombinasi AND dan OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 hanya dibaca: C-ROL-14 `PT Mitra Pindah` (relasi CV Mitra Sejati Transferred, relasi CV Mitra Mandiri aktif); C-ROL-4 `PT Mandiri Jaya` (relasi CV Mitra Mandiri saja); C-W3LST-3 `PT Tiga Mitra Uji` (relasi CV Mitra Sejati, CV Mitra Mandiri, CV Mitra Lestari). Fixture Pre-setup C-10 `PT Lintas Jaringan`, C-11 `PT Sinar Distributor`, C-12 `PT Timur Perkasa`.
- TC-AC-ACC-390 mensyaratkan tidak ada Client yang berelasi dengan CV Mitra Lestari dan sekaligus dengan Distributor PT Distribusi Timur; kondisi ini bagian dari fixture residen.
- Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Distributor transitif dan jaringan lain (TC-AC-ACC-389 dan TC-AC-ACC-618)

1. Klik Filter, pilih Distributor `PT Distribusi Nusantara`, lalu klik [Apply]
2. Verifikasi `PT Sejahtera Abadi` (Managed By CV Mitra Sejati) tampil walau kolom tidak menyebut Distributor
3. Ketik Search `PT Sinar Distributor`, tekan Enter
4. Verifikasi baris `PT Sinar Distributor` tampil (relasi Distributor-Client langsung)
5. Ganti isi kotak search dengan `PT Sejahtera Abadi`, tekan Enter
6. Verifikasi baris `PT Sejahtera Abadi` tampil (relasi Partner CV Mitra Sejati di jaringan PT Distribusi Nusantara)
7. Ganti isi kotak search dengan `PT Timur Perkasa`, tekan Enter
8. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (`PT Timur Perkasa` berada di jaringan PT Distribusi Timur)
9. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply]

### Distributor dan Partner tanpa irisan (TC-AC-ACC-390)

10. Klik Filter, pilih Distributor `PT Distribusi Timur` dan Partner `CV Mitra Lestari`, lalu klik [Apply]
11. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (0 baris, bukan error)
12. Klik Filter, klik [Clear Field], lalu klik [Apply]

### Partner langsung dan relasi Transferred (TC-AC-ACC-620, 933, 619)

13. Klik Filter, pilih Partner `CV Mitra Sejati`, lalu klik [Apply]
14. Ketik Search `PT Sejahtera Abadi`, tekan Enter
15. Verifikasi baris `PT Sejahtera Abadi` tampil
16. Ganti isi kotak search dengan `PT Sinar Distributor`, tekan Enter
17. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (`PT Sinar Distributor` tidak memiliki relasi Partner)
18. Ganti isi kotak search dengan `PT Mitra Pindah`, tekan Enter
19. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (relasi CV Mitra Sejati berstatus Transferred tidak dicocokkan)
20. Ganti isi kotak search dengan `PT Sejahtera Abadi`, tekan Enter
21. Verifikasi baris `PT Sejahtera Abadi` tampil
22. Klik Filter, klik [Clear Field], pilih Distributor `PT Distribusi Nusantara`, lalu klik [Apply]
23. Ganti isi kotak search dengan `PT Mitra Pindah`, tekan Enter
24. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (relasi Partner CV Mitra Sejati di jaringan berstatus Transferred tidak dicocokkan)
25. Ganti isi kotak search dengan `PT Sejahtera Abadi`, tekan Enter
26. Verifikasi baris `PT Sejahtera Abadi` tampil
27. Klik Filter, klik [Clear Field], pilih Partner `CV Mitra Mandiri`, lalu klik [Apply]
28. Ganti isi kotak search dengan `PT Mitra Pindah`, tekan Enter
29. Verifikasi baris `PT Mitra Pindah` tampil
30. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply]

### Distributor dan Partner bersamaan, logika AND (TC-AC-ACC-934)

31. Klik Filter, pilih Distributor `PT Distribusi Nusantara` dan Partner `CV Mitra Sejati`, lalu klik [Apply]
32. Ketik Search `PT Sejahtera Abadi`, tekan Enter
33. Verifikasi baris `PT Sejahtera Abadi` tampil
34. Klik Filter, klik [Clear Field], pilih Distributor `PT Distribusi Nusantara` dan Partner `CV Mitra Mandiri`, lalu klik [Apply]
35. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.` (Search `PT Sejahtera Abadi` masih aktif)
36. Ganti isi kotak search dengan `PT Mandiri Jaya`, tekan Enter
37. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`
38. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply]

### Distributor dan Partner bersamaan, Client berelasi ke keduanya tampil (TC-AC-ACC-969)

39. Klik Filter, pilih Distributor `PT Distribusi Timur` dan Partner `CV Mitra Sejati`, lalu klik [Apply]
40. Ketik Search `PT Lintas Jaringan`, tekan Enter
41. Verifikasi baris `PT Lintas Jaringan` tampil (relasi ke CV Mitra Sejati dan, lewat CV Mitra Timur, ke jaringan PT Distribusi Timur)
42. Klik Filter, klik [Clear Field], pilih Distributor `PT Distribusi Nusantara` dan Partner `CV Mitra Mandiri`, lalu klik [Apply]
43. Ganti isi kotak search dengan `PT Tiga Mitra Uji`, tekan Enter
44. Verifikasi baris `PT Tiga Mitra Uji` tampil (relasi ke CV Mitra Mandiri dan, lewat CV Mitra Sejati dan CV Mitra Lestari, ke jaringan PT Distribusi Nusantara)
45. Klik `(←)` pada kotak Search, lalu klik Filter, klik [Clear Field], klik [Apply]

### Partner dengan dua opsi, logika OR dalam satu field (TC-AC-ACC-708)

46. Ubah ukuran halaman menjadi 100 baris
47. Klik Filter, pilih Partner `CV Mitra Timur`, lalu klik [Apply]
48. Verifikasi `PT Timur Perkasa` dan `PT Lintas Jaringan` tampil
49. Verifikasi `PT Teknologi Maju` tidak tampil
50. Klik Filter, tambahkan Partner `CV Mitra Lestari` (dua opsi terpilih), lalu klik [Apply]
51. Verifikasi `PT Timur Perkasa`, `PT Lintas Jaringan`, dan `PT Teknologi Maju` tampil
52. Klik Filter, klik [Clear Field], lalu klik [Apply]

## Notes

- Urutan TC disusun ulang: TC-AC-ACC-620 dan TC-AC-ACC-933 dijalankan bersama TC-AC-ACC-619 karena memakai filter Partner/Distributor yang sama dan Search yang sama; TC-AC-ACC-708 dipindah ke akhir karena mengubah ukuran halaman (S-05 perubahan urutan dicatat di sini).
- Langkah penghubung (S-03): `[Clear Field]`/`[Apply]` dan `(←)` pada kotak Search di antara blok adalah pemulihan state (S-09); `Verifikasi` empty state `No results found` adalah Expected TC itu sendiri dan menjadi anchor positif absence.
- Spec melewati sekitar 35 langkah; alasan: seluruh blok satu kelas harness dan satu dataset (Filter Distributor/Partner List) dan blok berurutan tanpa state bersama.
- Temuan untuk QA
  - TC-AC-ACC-389: Data Uji kosong dan tidak menyebut apakah hanya `PT Sejahtera Abadi` yang diasersi; spec hanya mengasersi baris yang disebut TC.
  - TC-AC-ACC-390: precondition (d) menyatakan fakta data tanpa langkah cek; spec tidak mengasersinya.
