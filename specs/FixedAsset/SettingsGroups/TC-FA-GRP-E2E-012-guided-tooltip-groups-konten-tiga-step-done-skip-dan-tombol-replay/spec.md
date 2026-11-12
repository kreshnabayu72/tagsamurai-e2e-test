---
id: TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay
title: "Guided Tooltip Groups: Kunjungan Pertama Tiga Step, [Done], [Skip], Replay [?] Tidak Mereset Flag, dan Posisi Tombol Replay"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-34
  - TC-FA-GRP-35
  - TC-FA-GRP-36
  - TC-FA-GRP-37
  - TC-FA-GRP-1095
coverage:
  web: automated
---

# Guided Tooltip Groups: Kunjungan Pertama Tiga Step, [Done], [Skip], Replay [?] Tidak Mereset Flag, dan Posisi Tombol Replay

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Spec ini mengatur flag Guided Tooltip `fa-settings-groups` sendiri sesudah hook suite menyetelnya `seen`: kemampuan menyetel flag menjadi belum diset atau `seen` untuk akun aktor disediakan tim FE/BE; flag dipulihkan ke `seen` di hook `after`.
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9). Seluruh kolom tabel (Function dan Total Asset) dalam keadaan visible.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini mengubah flag Guided Tooltip akun aktor dan memulihkannya di hook `after`.

## Test Steps

### TC-FA-GRP-34: Kunjungan pertama, konten tiga step

1. Setel flag `fa-settings-groups` menjadi belum diset
2. Muat ulang halaman dengan F5
3. Verifikasi walkthrough muncul otomatis pada Step 1
4. Verifikasi Step 1 menyorot Sidebar Group Tree dengan judul `Group Tree` dan isi `Browse your group hierarchy. Click any group to see its assets and users.`
5. Verifikasi penomor `Step 1 of 3`
6. Verifikasi [Back] hidden di Step 1
7. Klik [Next]
8. Verifikasi Step 2 menyorot kolom Function dengan judul `Assignable Groups` dan isi `Groups can be marked as Assignable to hold active assets.`
9. Verifikasi penomor `Step 2 of 3`
10. Klik [Next]
11. Verifikasi Step 3 menyorot kolom Total Asset dengan judul `Asset Count` dan isi `See how many assets each group holds. Click a number for details.`
12. Verifikasi penomor `Step 3 of 3`
13. Verifikasi [Next] berubah menjadi [Done] di step terakhir
14. Verifikasi tombol [+] Group bukan target dari ketiga step

### TC-FA-GRP-35: [Done] menyetel flag seen

15. Setel flag `fa-settings-groups` menjadi belum diset
16. Muat ulang halaman dengan F5
17. Verifikasi walkthrough muncul otomatis pada Step 1
18. Klik [Next]
19. Klik [Next]
20. Klik [Done]
21. Verifikasi walkthrough tertutup
22. Muat ulang halaman dengan F5
23. Verifikasi Breadcrumb `Settings > Groups` tampil
24. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-GRP-36: [Skip] lewat klik overlay menyetel flag seen

25. Setel flag `fa-settings-groups` menjadi belum diset
26. Muat ulang halaman dengan F5
27. Verifikasi walkthrough muncul otomatis pada Step 1
28. Klik area overlay gelap
29. Verifikasi walkthrough tertutup
30. Muat ulang halaman dengan F5
31. Verifikasi Breadcrumb `Settings > Groups` tampil
32. Verifikasi walkthrough tidak muncul lagi secara otomatis

### TC-FA-GRP-37: Replay lewat [?] tidak mereset flag seen

33. Klik tombol [?] di header
34. Verifikasi replay dimulai dari Step 1
35. Klik [Next]
36. Klik [Next]
37. Klik [Done]
38. Muat ulang halaman dengan F5
39. Verifikasi Breadcrumb `Settings > Groups` tampil
40. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-GRP-1095: Posisi tombol replay [?]

41. Verifikasi tombol [?] (ikon tanda tanya) berada tepat di sebelah kanan Breadcrumb `Settings > Groups`
42. Hover tombol [?]
43. Verifikasi tooltip `Show guide` tampil
44. Klik tombol [?]
45. Verifikasi walkthrough dimulai dari Step 1
46. Klik [Skip]

## Notes

- Spec melewati sekitar 35 langkah (46 langkah): seluruh blok adalah satu kelas (Guided Tooltip halaman Groups) pada layar yang sama, tiap blok berdiri sendiri dengan flag diatur ulang di awal blok (langkah 1, 15, 25), dan perulangan [Next]-[Next]-[Done] tidak dapat diringkas karena tiap klik adalah aksi sendiri.
- Langkah penghubung (S-03): langkah 1, 15, 25 (menyetel flag), langkah 2, 16, 26 (muat ulang agar flag dievaluasi, menggantikan "Buka Fixed Asset > Settings > Groups" karena halaman sudah dibuka hook `beforeEach`), langkah 46 (menutup walkthrough).
- Urutan TC dalam spec: 34, 35, 36, 37, 1095. TC-FA-GRP-37 dan 1095 memerlukan flag sudah diset; flag itu diset oleh TC-FA-GRP-36 (langkah 28).
- Temuan untuk QA:
  - TC-FA-GRP-34 menyebut "Klik [Next] sampai step terakhir" dan penomor `Step [Current Step] of 3`; format `Step N of 3` dipakai sebagai teks asersi.
  - TC-FA-GRP-36 menyebut "[Skip] (tombol atau klik overlay)" sedangkan langkah TC hanya klik overlay; spec mengikuti langkah TC (klik overlay).
  - Mekanisme menyetel dan membaca flag tidak disebut TC; disediakan tim FE/BE tanpa endpoint karangan (S-13).
