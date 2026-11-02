---
id: TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action
title: "Screening Breadcrumb, Klik Baris, Hover Path, Modified By, dan Overlay Row Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-05
  - TC-AC-SG-06
  - TC-AC-SG-07
  - TC-AC-SG-08
  - TC-AC-SG-09
coverage:
  web: automated
---

# Screening Breadcrumb, Klik Baris, Hover Path, Modified By, dan Overlay Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); nama pengubah `Admin A` (`Admin Alpha`) untuk `Region A` dan `Admin C` untuk `Head Office` (#20).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-002`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-05: Breadcrumb Settings > Group tidak dapat diklik dan tanpa Page Title Header

1. Verifikasi Breadcrumb "Settings > Group" terdiri dari dua segmen
2. Klik segmen "Settings" pada Breadcrumb
3. Verifikasi halaman Settings > Group tetap tampil tanpa berpindah halaman (segmen pertama bersifat label statis)
4. Klik segmen "Group" pada Breadcrumb
5. Verifikasi halaman Settings > Group tetap tampil tanpa berpindah halaman (segmen terakhir bersifat label statis)
6. Cari elemen Page Title Header "Group" atau "Groups" di bawah Breadcrumb
7. Verifikasi tidak ada Page Title Header di bawah Breadcrumb
8. Verifikasi konten langsung dimulai di dalam Card

### TC-AC-SG-06: Klik area baris tabel tidak melakukan aksi apa pun

9. Ketik Search `Region A`, tekan Enter
10. Verifikasi baris `Region A` tampil di tabel
11. Klik teks nama group pada baris `Region A`
12. Verifikasi klik nama group tidak membuka popup, tidak berpindah halaman, dan tidak memilih node di sidebar
13. Klik area kosong pada baris `Region A` di luar checkbox, angka, dan ikon ⋯
14. Verifikasi klik area baris tidak membuka popup, tidak berpindah halaman, dan tidak memilih node di sidebar
15. Verifikasi ikon `⋯` pada baris `Region A` tampil sebagai akses ke aksi data existing

### TC-AC-SG-07: Hover nama group di tabel menampilkan full path breadcrumb

16. Ganti isi kotak search dengan `Room 301`, tekan Enter
17. Hover nama group `Room 301` pada baris tabel
18. Verifikasi tooltip `Room 301` menampilkan full path "Region A > Branch 1 > Floor 1 > Room 301"
19. Ganti isi kotak search dengan `Region A`, tekan Enter
20. Hover nama group `Region A`
21. Verifikasi tooltip `Region A` menampilkan "Region A" (level 1 tanpa parent selain root)

### TC-AC-SG-08: Format kolom Modified By dan tooltip nama lengkap

22. Verifikasi kolom Modified By baris `Region A` tampil sebagai teks polos "Admin A" tanpa badge
23. Hover nilai Modified By pada baris `Region A`
24. Verifikasi tooltip nama lengkap "Admin Alpha"
25. Ganti isi kotak search dengan `Head Office`, tekan Enter
26. Verifikasi kolom Modified By baris `Head Office` tampil sebagai teks polos "Admin C" tanpa badge

### TC-AC-SG-09: Tombol ⋯ pada baris tabel membuka Overlay Row Action untuk Total Control

27. Ganti isi kotak search dengan `Region A`, tekan Enter
28. Klik ikon `⋯` pada baris group `Region A` di tabel
29. Verifikasi Overlay Row Action memuat tepat tiga aksi berurutan: "+ Add Subgroup" (ikon `AddLine`, severity dark), "Edit" (ikon `Edit2Line`, severity dark), "Delete" (ikon `DeleteBin6Line`, severity danger)
30. Verifikasi tidak ada aksi "Detail" pada Overlay Row Action
31. Tutup Overlay Row Action dengan Esc
32. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, R-16): langkah 9, 16, 19, 25, 27 (Search untuk menemukan baris target `Region A`, `Room 301`, `Head Office` karena tabel All Groups terbagi dua halaman), langkah 31 (menutup overlay), dan langkah 32 (mengosongkan Search sebelum spec berakhir). Hook `beforeEach` suite membuka halaman untuk TC pertama; Search antar-TC diganti isinya.
- Urutan TC-AC-SG-08 mengikuti state (bagian 8b butir 5): Expected a untuk `Region A` diasersi, lalu hover (Expected b), baru berpindah ke baris `Head Office`, karena kedua baris tidak tampil bersamaan setelah Search.
- Langkah 12 dan 14 menyatukan tiga negasi atas satu kejadian klik (daftar elemen yang sama-sama tidak ada, S-01); anchor positifnya adalah baris `Region A` tampil (langkah 10) dan ikon `⋯` (langkah 15).
- Temuan untuk QA:
  - TC-AC-SG-06 Expected b ("akses ke aksi data existing hanya tersedia lewat ikon ⋯") adalah klaim eksklusif yang tidak dapat diasersi selain dengan menunjukkan ikon `⋯` tampil dan klik baris tidak melakukan aksi; spec mengasersi keduanya (langkah 12, 14, 15).
  - Pengganti isi Search dengan Enter diperlukan karena urutan default baris tabel All Groups tidak disebut TC; halaman tempat `Room 301`, `Head Office`, dan `Region A` berada tidak dapat dipastikan.
