---
id: TC-FA-TDC-E2E-089-seed-aktivasi-pertama-modul-akuntansi-tujuh-class-aktif
title: "Seed Aktivasi Pertama Modul Akuntansi: Tujuh Class Aktif dan Tidak Dibuat Ulang Saat Diaktifkan Kembali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-336
  - TC-FA-TDC-337
  - TC-FA-TDC-338
  - TC-FA-TDC-339
coverage:
  web: automated
---

# Seed Aktivasi Pertama Modul Akuntansi: Tujuh Class Aktif dan Tidak Dibuat Ulang Saat Diaktifkan Kembali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada company baru yang belum pernah mengaktifkan modul akuntansi (plan Growth atau lebih tinggi). Akun, email, dan company disediakan tim FE (tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TCNEWACC_PASSWORD` (nama env belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Pengecualian layar awal: halaman Tax Depreciation Class belum tersedia sebelum modul akuntansi diaktifkan, sehingga spec membuka layar itu sendiri (langkah 2 dan 35).
- Kemampuan teknis: mengaktifkan dan menonaktifkan modul akuntansi pada company baru, membuat company baru, dan mengembalikannya ke keadaan belum aktivasi (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD, S-13); seeding satu class dan perubahan Class Name lewat API (langkah 31).
- Nilai seed mengikuti PRD §4.1.5 sebagaimana tertulis di Expected TC-336.
- Data Dinamis: class `KHS-S9-{runId}-089` (dibuat lewat API pada langkah 31) dan Class Name `NB-4` diubah menjadi `Kelompok empat diubah` (langkah 31). Seluruh state company baru dipulihkan di hook `after` (company dikembalikan ke keadaan sebelum aktivasi atau dibuang oleh fixture).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-336: Seed aktivasi pertama membuat tujuh class seed Active

1. Aktifkan modul akuntansi untuk pertama kali
2. Buka Settings > Accounting > Tax Depreciation Class
3. Baca seluruh baris tabel (Class Code, Class Name, Asset Type, Useful Life (years), Straight Line Rate, Declining Balance Rate, Allowed Methods, Used By, Effective From, Active)
4. Verifikasi tabel memuat tepat tujuh baris, urut Class Code A-Z: BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-3, NB-4
5. Verifikasi NB-1: "Bukan bangunan – Kelompok 1", Non-building, 4, 25%, 50%, "Straight Line · Declining Balance"
6. Verifikasi NB-2: "Bukan bangunan – Kelompok 2", Non-building, 8, 12.5%, 25%, "Straight Line · Declining Balance"
7. Verifikasi NB-3: "Bukan bangunan – Kelompok 3", Non-building, 16, 6.25%, 12.5%, "Straight Line · Declining Balance"
8. Verifikasi NB-4: "Bukan bangunan – Kelompok 4", Non-building, 20, 5%, 10%, "Straight Line · Declining Balance"
9. Verifikasi BLD-P: "Bangunan permanen", Building, 20, 5%, "—", "Straight Line"
10. Verifikasi BLD-NP: "Bangunan tidak permanen", Building, 10, 10%, "—", "Straight Line"
11. Verifikasi LAND: "Tanah", Land, "—", "—", "—", "—"
12. Verifikasi seluruh baris: Active = On, Used By "0", Effective From "—"
13. Verifikasi Class Name tersimpan verbatim sebagai data client (tidak diterjemahkan)

### TC-FA-TDC-337: Seed memiliki Regulation Reference terisi

14. Ketik Search `UU HPP 7/2021`, tekan Enter
15. Verifikasi hasil Search memuat tujuh baris
16. Klik link Class Code `NB-1` pada tabel
17. Verifikasi Drawer Edit `NB-1`: Regulation Reference "UU HPP 7/2021; PMK 72/2023"
18. Klik `[×]` pada header Drawer
19. Klik link Class Code `LAND` pada tabel
20. Verifikasi Drawer Edit `LAND`: Regulation Reference "UU HPP 7/2021; PMK 72/2023"
21. Klik `[×]` pada header Drawer
22. Klik `(←)` pada kotak Search

### TC-FA-TDC-338: Versi pertama tanpa Effective From dan berstatus Current

23. Klik link Class Code `NB-1` pada tabel
24. Verifikasi Drawer Edit: Effective From "—"; Last Posted Tax Year "—"
25. Verifikasi Alert versi Scheduled tidak tampil
26. Klik tautan View versions
27. Verifikasi modal Versions memuat tepat satu baris
28. Verifikasi baris itu: Effective From "—", Status "Current", Useful Life 4, Straight Line Rate 25%, Declining Balance Rate 50%, Regulation Reference "UU HPP 7/2021; PMK 72/2023"
29. Tutup modal Versions
30. Klik `[×]` pada header Drawer

### TC-FA-TDC-339: Seed tidak dibuat ulang saat modul akuntansi diaktifkan kembali

31. Buat class `KHS-S9-{runId}-089` lewat seeding API dan ubah Class Name `NB-4` menjadi `Kelompok empat diubah`
32. Nonaktifkan modul akuntansi
33. Aktifkan kembali modul akuntansi
34. Tunggu aksi selesai
35. Buka Settings > Accounting > Tax Depreciation Class
36. Verifikasi tabel memuat delapan class: tujuh seed (NB-4 dengan Class Name "Kelompok empat diubah") dan `KHS-S9-{runId}-089`, tanpa baris seed ganda
37. Verifikasi Empty State tidak tampil

## Notes

- Alasan spec di atas sekitar 35 langkah: keempat TC satu topik (seed aktivasi modul akuntansi) pada satu company baru yang hanya dapat diaktifkan pertama kali sekali per run; tiap blok TC-336 sampai 338 adalah pembacaan keadaan yang sama (tujuh seed) dan TC-339 memakai keadaan itu sebagai awal, sehingga memecahnya menuntut aktivasi company baru ulang. Sekitar sepertiga langkah adalah `Verifikasi` nilai tujuh baris seed (satu per baris).
- Langkah 1 dan 32 sampai 34 memakai kemampuan aktivasi modul akuntansi yang disediakan tim FE/BE; TC tidak menyebut lokasi atau cara mengaktifkannya.
- Langkah penghubung (S-03): langkah 3 ("Baca" tanpa asersi), langkah 18, 21, dan 30 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`), langkah 22 (mengosongkan Search sebelum TC-338 membutuhkan tabel penuh, S-09, 8b.9), langkah 29 (menutup modal Versions), langkah 31 (menyiapkan precondition c TC-339 sebagai pembentuk state, dipakai sebagai precondition TC dan tidak diasersi), dan langkah 34 ("Tunggu aksi selesai", 8b.8).
- Search pada langkah 14 adalah langkah TC-337 (bukan pencarian baris target); baris `NB-1` dan `LAND` dibuka dari hasil Search. Pada TC-338 `NB-1` dibuka dari tabel penuh (tujuh baris pada satu halaman) tanpa Search.
- Langkah 36 dan 37 menjalankan Expected a dan b TC-339; "tanpa baris seed ganda" ditegakkan oleh jumlah delapan baris.
- Post Condition TC-336 b ("tujuh entri L-01 dengan aktor System") dan TC-339 ("tidak ada entri L-01 baru dari aktivasi ulang") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-01 ada di spec pencatatan log.
- Temuan untuk QA:
  - Mekanisme mengaktifkan dan menonaktifkan modul akuntansi serta company baru tidak disebut TC; akun, email, dan company tidak tertulis.
  - TC-339 precondition c menyebut `NB-4` diubah Class Name menjadi `Kelompok empat diubah` tanpa menyebut cara; spec memakai seeding API.
  - Post Condition TC-336 b dan TC-339 tanpa langkah observasi di TC.
  - TC-339 memakai `KHS-S9` tanpa suffix; spec memakai `-{runId}-089` (S-12).
