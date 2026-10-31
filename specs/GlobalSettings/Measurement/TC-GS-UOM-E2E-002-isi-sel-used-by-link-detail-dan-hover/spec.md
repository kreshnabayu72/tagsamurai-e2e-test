---
id: TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover
title: "Isi Sel Tabel: Used By (Items) sebagai Link, Hover/Fokus Link Unit Name dan Angka, Pembukaan Unit Detail"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-367
  - TC-GS-UOM-282
  - TC-GS-UOM-396
  - TC-GS-UOM-371
  - TC-GS-UOM-8
  - TC-GS-UOM-372
coverage:
  web: automated
---

# Isi Sel Tabel: Used By (Items) sebagai Link, Hover/Fokus Link Unit Name dan Angka, Pembukaan Unit Detail

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data): Pre-setup Client A (8 unit) dan Population D-01 (12 unit), total N = 20 unit (diturunkan dari seeding; hook `before` men-seed Population secara idempotent sesuai "Data bersama" di `suite.md`). Unit yang dipakai dengan angka Used By (Items): Box `4`, Kilogram `1`, Liter `0`, Pieces `3`. Pada urutan default A-Z, Box, Kilogram, dan Liter berada di halaman 1; Pieces berada di halaman 2 sehingga dicari lewat Search.
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite.
- State global: tidak ada yang diubah.
- Kemampuan teknis: hover dan navigasi keyboard (Tab) dengan pembacaan warna teks, text-decoration, dan focus ring.

## Test Steps

### TC-GS-UOM-367: Screening kolom Used By (Items) pada tabel Measurement

1. Perhatikan header dan sel kolom Used By (Items); cari baris Box, Kilogram, dan Liter pada halaman 1
2. Verifikasi kolom `Used By (Items)` tampil di antara `Symbol` dan `Last Updated`
3. Verifikasi kolom `Used By (Items)` sortable
4. Verifikasi sel kolom `Used By (Items)` berisi angka bulat tanpa pemisah ribuan
5. Verifikasi Box `4`, Kilogram `1`, Liter `0`
6. Verifikasi tidak ada sel `Used By (Items)` kosong pada baris halaman 1
7. Verifikasi tidak ada sel `Used By (Items)` bernilai `—` pada baris halaman 1
8. Verifikasi angka `Used By (Items)` tampil sebagai teks link (bukan teks biasa)
9. Verifikasi tidak ada kolom `Item Type` pada tabel

### TC-GS-UOM-282: Hover teks link Unit Name mengubah warna ke primary Global Settings tanpa underline

10. Perhatikan teks `Kilogram` pada kolom Unit Name tanpa hover
11. Verifikasi tanpa hover teks Unit Name berwarna netral sama dengan teks body tabel
12. Hover teks `Kilogram` dan catat warna teks serta dekorasi teksnya
13. Verifikasi saat hover warna teks berubah mengikuti warna primary Global Settings (hitam)
14. Verifikasi saat hover tidak ada garis bawah
15. Pindahkan kursor keluar dari teks `Kilogram`
16. Verifikasi warna teks kembali netral

### TC-GS-UOM-396: Hover dan fokus link angka Used By (Items) sama dengan pola link Unit Name

17. Perhatikan angka `4` pada baris Box tanpa hover
18. Verifikasi tanpa hover angka `4` berupa teks link netral
19. Hover angka `4` dan catat warna teks serta dekorasi teksnya
20. Verifikasi saat hover warna teks berubah mengikuti warna primary Global Settings (hitam)
21. Verifikasi saat hover tidak ada garis bawah
22. Verifikasi hover angka `4` memiliki warna dan dekorasi teks yang sama dengan hover teks Unit Name yang dicatat pada langkah 12 (TC-GS-UOM-282)
23. Pindahkan kursor keluar dari angka `4`
24. Verifikasi warna angka `4` kembali netral
25. Tekan Tab hingga fokus keyboard berada di angka `4`
26. Verifikasi fokus keyboard menampilkan focus ring

### TC-GS-UOM-371: Nilai 0 tampil `0` (bukan `—`) dan tetap link yang membuka Detail dengan empty state

27. Perhatikan Used By (Items) baris Liter
28. Verifikasi sel Used By (Items) Liter menampilkan `0`
29. Verifikasi sel Used By (Items) Liter bukan `—`
30. Verifikasi sel Used By (Items) Liter bukan sel kosong
31. Hover angka `0` pada baris Liter
32. Verifikasi hover angka `0` menampilkan state hover link yang sama seperti angka lain (warna dan dekorasi teks sama dengan hover angka `4` yang dicatat pada langkah 19)
33. Klik angka `0` pada baris Liter
34. Verifikasi Modal Unit Detail Liter terbuka
35. Verifikasi Total Item `0`
36. Verifikasi Accordion Item Type List menampilkan empty state `No item types linked`
37. Tutup Modal Unit Detail lewat `[✕]`

### TC-GS-UOM-8: Klik teks Unit Name membuka Modal Unit Detail

38. Klik teks link `Kilogram` pada kolom Unit Name
39. Verifikasi Modal Unit Detail terbuka untuk Kilogram
40. Catat judul modal, Total Item, dan isi accordion Item Type List
41. Tutup Modal Unit Detail lewat `[✕]`
42. Klik `⋯` baris Kilogram > Detail
43. Verifikasi hasil row action `Detail` sama dengan hasil klik teks link Unit Name pada langkah 38 (judul modal, Total Item, dan isi accordion Item Type List sama dengan yang dicatat pada langkah 40)
44. Tutup Modal Unit Detail lewat `[✕]`

### TC-GS-UOM-372: Klik angka Used By (Items) membuka Modal Unit Detail seperti link Unit Name dan row action Detail

45. Ketik Search `Pieces`, tekan Enter
46. Klik angka Used By (Items) baris Pieces
47. Verifikasi Modal Unit Detail Pieces terbuka
48. Catat judul modal, Total Item, dan isi accordion Item Type List
49. Verifikasi klik angka tidak memicu aksi lain selain membuka Modal Unit Detail (tidak ada dialog atau modal lain yang terbuka)
50. Tutup Modal Unit Detail lewat `[✕]`
51. Verifikasi checkbox baris Pieces tidak ter-centang
52. Klik teks link `Pieces` pada kolom Unit Name
53. Verifikasi Modal Unit Detail Pieces terbuka dengan isi identik dengan yang dicatat pada langkah 48
54. Tutup Modal Unit Detail lewat `[✕]`
55. Klik `⋯` baris Pieces > Detail
56. Verifikasi Modal Unit Detail Pieces terbuka dengan isi identik dengan yang dicatat pada langkah 48
57. Tutup Modal Unit Detail lewat `[✕]`
58. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-UOM-367 (screening, tanpa aksi) dan hover/fokus TC-GS-UOM-282 dan TC-GS-UOM-396 di awal, lalu TC-GS-UOM-371, TC-GS-UOM-8, dan TC-GS-UOM-372 yang membuka Modal Unit Detail. Spec tidak membuat atau menghapus data sehingga tidak butuh seeding tambahan atau cleanup.
- Spec ini sekitar 58 langkah, di atas batas 35 langkah: seluruh blok satu kelas harness (baca UI biasa pada kolom yang sama), satu akun, tanpa membuat data, dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna). Sebagian besar langkah adalah `Verifikasi` yang dipecah per klausa (S-01) dan penutupan modal.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 37, 41, 44, 50, 54, dan 57 (menutup Modal Unit Detail), 40 dan 48 (mencatat isi modal sebagai acuan perbandingan), 45 (Search `Pieces` untuk menemukan baris di halaman 2), dan 58 (mengosongkan Search).
- Langkah 22 dan 32 mewujudkan butir "sama dengan hover teks Unit Name (TC-GS-UOM-282)" pada Expected b TC-GS-UOM-396 dan "state hover link yang sama seperti angka lain" pada Expected b TC-GS-UOM-371 sebagai perbandingan langsung dengan nilai yang dicatat. Langkah 43 dan 53 serta 56 mewujudkan "hasil sama dengan row action Detail" (TC-GS-UOM-8) dan "isi identik" (TC-GS-UOM-372).
- Langkah 49 dan 51 mewujudkan klausa "tidak memilih checkbox baris dan tidak memicu aksi lain" pada Expected b TC-GS-UOM-372; TC tidak merinci "aksi lain", sehingga spec memeriksa tidak ada dialog atau modal lain selain Modal Unit Detail dan checkbox baris tidak ter-centang.
- Temuan untuk QA:
  - TC-GS-UOM-372 Expected b: frasa "tidak memicu aksi lain" tidak merinci aksi yang dimaksud; spec memakai pemeriksaan yang disebut di atas.
  - TC-GS-UOM-396 dan TC-GS-UOM-282: TC menyebut warna primary Global Settings sebagai "hitam" tanpa nilai warna eksak; asersi warna dilakukan terhadap warna primary Global Settings dan perbandingan relatif (netral vs hover), bukan nilai heks tertentu.
