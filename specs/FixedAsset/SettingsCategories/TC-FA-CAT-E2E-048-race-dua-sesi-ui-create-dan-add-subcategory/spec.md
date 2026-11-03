---
id: TC-FA-CAT-E2E-048-race-dua-sesi-ui-create-dan-add-subcategory
title: "Race Dua Sesi UI pada Create dan Add Subcategory: Slot Terakhir, Batas Platform, Name Sama, dan Code Sama"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-135
  - TC-FA-CAT-136
  - TC-FA-CAT-137
  - TC-FA-CAT-138
  - TC-FA-CAT-165
  - TC-FA-CAT-630
coverage:
  web: automated
---

# Race Dua Sesi UI pada Create dan Add Subcategory: Slot Terakhir, Batas Platform, Name Sama, dan Code Sama

## Prerequisites

- Mode: FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Sesi A login di hook `before` spec ini pada client CatMain (Pre-setup #20); halaman dibuka hook `beforeEach` suite. Sesi B adalah konteks browser kedua dengan akun yang sama, objek asersi (hasil penolakan terlihat di sesi B), sehingga tergolong konteks kedua kelas c. Perpindahan client memakai langkah Ganti akun eksplisit untuk kedua sesi. Hook `after` mengembalikan kedua sesi ke akun default suite dan menutup sesi B.
- Kemampuan teknis: hook `beforeEach` suite mengonfirmasi dialog `beforeunload`, sehingga muat ulang halaman sesi B yang berisi popup dirty ditangani (S-08); disediakan tim FE.
- Data Pre-setup: client CatMain (#20) untuk TC-FA-CAT-136, 137, 165, 630 (`Vehicle` dan `Accessory` menjadi parent TC-FA-CAT-630); client CatStarter (#27, Starter, 4 kategori L1 `Starter A` sampai `Starter D`, cap 5) untuk TC-FA-CAT-135; client CatCountLimit (#29, varian 999 kategori dengan Master Data Count Limit 1.000, satu slot tersisa) untuk TC-FA-CAT-138. Kuota Master Data Count Limit dan cap plan menjadi pemicu state, bukan objek uji.
- Data Dinamis (dihapus hook `before` dan `after` lewat API): `Race Name {runId}-048` (Code `RN1`, `RN2`), `Race Code A {runId}-048` dan `Race Code B {runId}-048` (Code `RCODE`), `Zeta One` dan `Zeta Opt` (Code kosong, nama literal agar kandidat Code sama), `Race Sub A {runId}-048` dan `Race Sub B {runId}-048` (Code `RCODE2`), `Race A {runId}-048`, `Race B {runId}-048`, `Plat A {runId}-048`, `Plat B {runId}-048`. Code literal `RN1`, `RN2`, `RCODE`, `RCODE2` dibersihkan di hook `before` (R-13). Efek pada parent `Vehicle` dan `Accessory` (Last Updated) dicatat di sini (S-06).
- Kemampuan teknis tambahan (disediakan tim FE/BE, tanpa endpoint karangan): menghapus kategori milik spec dan memulihkan hitungan awal (4 pada CatStarter, 999 pada CatCountLimit) lewat API; membaca state BE kategori.
- Suite berjalan serial (`parallel: false`) karena spec memakai satu slot terakhir plan dan satu slot terakhir Master Data Count Limit.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-136: Dua Create dengan Name sama bersamaan

1. Sesi A dan sesi B masing-masing klik `[+] Category` pada sidebar
2. Sesi A: isi Category Name `Race Name {runId}-048` dan Code `RN1`
3. Sesi B: isi Category Name `Race Name {runId}-048` dan Code `RN2`
4. Klik `[Submit]` di sesi A lalu segera di sesi B
5. Verifikasi sesi A berhasil: toast `Success, category has been created.` tampil
6. Verifikasi sesi B ditolak (422) dengan error inline `Category name already exists`
7. Verifikasi popup New Category di sesi B tetap terbuka
8. Muat ulang halaman di sesi B (dialog `beforeunload` dikonfirmasi)

### TC-FA-CAT-137: Dua Create dengan Code manual sama bersamaan

9. Sesi A dan sesi B masing-masing klik `[+] Category` pada sidebar
10. Sesi A: isi Category Name `Race Code A {runId}-048` dan Code `RCODE`
11. Sesi B: isi Category Name `Race Code B {runId}-048` dan Code `RCODE`
12. Klik `[Submit]` di sesi A lalu segera di sesi B
13. Verifikasi sesi A berhasil: toast `Success, category has been created.` tampil
14. Verifikasi sesi B ditolak (422) dengan error inline `Code already exists`
15. Muat ulang halaman di sesi B (dialog `beforeunload` dikonfirmasi)

### TC-FA-CAT-165: Dua Create dengan kandidat Code sama bersamaan

16. Sesi A dan sesi B masing-masing klik `[+] Category` pada sidebar
17. Sesi A: isi Category Name `Zeta One` dengan Code dikosongkan
18. Sesi B: isi Category Name `Zeta Opt` dengan Code dikosongkan
19. Klik `[Submit]` di kedua sesi hampir bersamaan
20. Di sesi A ketik Search `Zeta`, tekan Enter
21. Verifikasi baris `Zeta One` tampil di tabel
22. Verifikasi baris `Zeta Opt` tampil di tabel
23. Verifikasi Code yang dihasilkan untuk `Zeta One` dan `Zeta Opt` berbeda
24. Verifikasi tidak ada error ke user di sesi A
25. Verifikasi tidak ada error ke user di sesi B
26. Klik `(←)` pada kotak Search di sesi A

### TC-FA-CAT-630: Dua Add Subcategory dengan Code manual sama bersamaan

27. Sesi A: klik elipsis (⋯) pada baris `Vehicle` > `+ Add Subcategory`
28. Sesi B: klik elipsis (⋯) pada baris `Accessory` > `+ Add Subcategory`
29. Sesi A: isi Category Name `Race Sub A {runId}-048` dan Code `RCODE2`
30. Sesi B: isi Category Name `Race Sub B {runId}-048` dan Code `RCODE2`
31. Klik `[Submit]` di sesi A lalu segera di sesi B
32. Verifikasi sesi A berhasil: toast `Success, category has been created.` tampil
33. Verifikasi sesi B ditolak (422) dengan error inline `Code already exists`
34. Verifikasi popup New Subcategory di sesi B tetap terbuka
35. Verifikasi input di sesi B dipertahankan
36. Muat ulang halaman di sesi B (dialog `beforeunload` dikonfirmasi)

### TC-FA-CAT-135: Dua Create bersamaan pada slot terakhir plan

37. Ganti akun: sesi A dan sesi B logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatStarter dengan `Spectra.env.FA_TC_PASSWORD`
38. Sesi A dan sesi B masing-masing klik `[+] Category` pada sidebar
39. Sesi A: isi Category Name `Race A {runId}-048`
40. Sesi B: isi Category Name `Race B {runId}-048`
41. Klik `[Submit]` di sesi A lalu segera di sesi B
42. Verifikasi sesi A berhasil: toast `Success, category has been created.` tampil
43. Verifikasi sesi B menampilkan dialog kontekstual `Cannot Add Category` · `You've reached the category limit for your plan. Upgrade to add more.` · `[OK]` (server menolak dengan 409)
44. Verifikasi toast generik tidak tampil di sesi B
45. Verifikasi kategori `Race B {runId}-048` tidak tersimpan (dibaca dari state BE)
46. Klik `[OK]` di sesi B
47. Muat ulang halaman di sesi B (dialog `beforeunload` dikonfirmasi)
48. Hapus kategori `Race A {runId}-048` lewat API untuk memulihkan hitungan 4 dari cap 5

### TC-FA-CAT-138: Race pada batas platform

49. Ganti akun: sesi A dan sesi B logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatCountLimit dengan `Spectra.env.FA_TC_PASSWORD`
50. Sesi A dan sesi B masing-masing klik `[+] Category` pada sidebar
51. Sesi A: isi Category Name `Plat A {runId}-048`
52. Sesi B: isi Category Name `Plat B {runId}-048`
53. Klik `[Submit]` di sesi A lalu segera di sesi B
54. Verifikasi sesi A berhasil: toast `Success, category has been created.` tampil
55. Verifikasi sesi B menampilkan dialog kontekstual `Cannot Add Category` · `You've reached the platform limit of 1000 records. Contact support if you need a higher limit.` · `[OK]` (server menolak dengan 409)
56. Klik `[OK]` di sesi B
57. Muat ulang halaman di sesi B (dialog `beforeunload` dikonfirmasi)
58. Hapus kategori `Plat A {runId}-048` lewat API untuk memulihkan hitungan 999

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Enam blok berdiri sendiri dan satu kelas harness (race dua sesi UI); kegagalan satu blok tidak menghilangkan makna blok lain, sehingga jumlah langkah (58) melewati sekitar 35 tanpa dipecah.
- Urutan: blok dikelompokkan menurut client (CatMain lebih dulu, lalu CatStarter dan CatCountLimit) agar perpindahan akun hanya dua kali; urutan ini berbeda dari urutan nomor TC sumber.
- Langkah penghubung (S-03, S-09): langkah 8, 15, 36, 47, 57 (membuang popup dirty di sesi B lewat muat ulang yang dikonfirmasi; kemampuan ada di Prerequisites, S-08), langkah 20 dan 26 (Search untuk menemukan baris target dan mengosongkannya, R-16), langkah 46 dan 56 (menutup dialog), langkah 48 dan 58 (memulihkan hitungan slot), langkah 37 dan 49 (ganti akun eksplisit kedua sesi, S-07).
- Rujukan: TC-FA-CAT-138 memakai Master Data Count Limit sebagai pemicu state pada spec multi-konteks (bagian 3 P-2, 2026-10-21), tidak dipindah ke kelas e.
- Temuan untuk QA:
  - TC-FA-CAT-165 memakai nama `Zeta One` dan `Zeta Opt` agar kandidat Code (`ZO`/`Z`) sama; suffix run akan mengubah kandidat, sehingga nama ditulis literal dan dibersihkan di hook `before`/`after` (S-12 tidak mengizinkan nama literal kecuali satu karakter).
  - TC-FA-CAT-136 sampai 138, 630 tidak menyatakan keadaan popup sesi A sesudah sukses; spec tidak mengasersinya.
  - TC-FA-CAT-135 dan 138 tidak menyatakan keadaan popup sesi B sesudah `[OK]`; spec membuangnya dengan muat ulang yang dikonfirmasi.
  - Dua sesi web dengan akun yang sama pada satu client dapat terkena batas satu sesi web; TC tidak menyatakan perilakunya, spec mengikuti TC ("dua sesi").
- Spec melewati 35 langkah (58 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
