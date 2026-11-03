---
id: TC-FA-RP-E2E-142-tab-total-control-filter-4
title: "Tab Total Control: Filter (4/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-492
  - TC-FA-RP-493
  - TC-FA-RP-494
  - TC-FA-RP-495
coverage:
  web: automated
---

# Tab Total Control: Filter (4/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Cost Center `CC-100` Ahmad Fauzi dan `CC-200` Budi Santoso, tujuh baris tanpa nilai), #37 (Tab Read Only empat baris), #22 (Custom Field `Cost Center`). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Nilai opsi Position untuk TC 495 (tidak ditulis di Data Uji TC): `Finance Officer`, dipilih spec.

## Test Steps

### Kombinasi Filter lalu Search (TC 492)

1. Klik ikon Search.
2. Verifikasi tabel menampilkan seluruh sembilan baris Pre-setup #36.
3. Klik ikon Filter, pilih opsi `Finance` pada field Division, lalu klik `[Apply]`.
4. Ketik Search `Fina`, tekan Enter.
5. Verifikasi tabel menampilkan irisan Filter Division `Finance` dan Search `Fina`: hanya baris Fitri Handayani dan Rudi Hartono.
6. Verifikasi kriteria Filter tetap aktif (badge titik pada ikon Filter masih tampil).
7. Klik `✕` pada Search, tekan Enter.
8. Pada panel Filter yang masih terbuka, klik `[Clear Field]`, lalu klik `[Apply]`.

### Menutup Filter Panel tanpa Apply (TC 493)

9. Pilih opsi `Finance Officer` pada field Position tanpa Apply.
10. Klik ikon Filter lagi untuk menutup panel.
11. Verifikasi tabel tidak berubah (seluruh sembilan baris Pre-setup #36).
12. Klik ikon Filter untuk membuka panel kembali.
13. Verifikasi panel menampilkan nilai ter-Apply terakhir (draft dibuang): field Position kosong dengan placeholder `All positions`.
14. Klik ikon Filter untuk menutup panel.

### Indikator filter aktif dan nilai kosong (TC 494)

15. Klik ikon Filter, lalu buka dropdown field Cost Center.
16. Verifikasi dropdown Cost Center memuat opsi `CC-100` dan `CC-200`.
17. Verifikasi dropdown Cost Center tidak memuat opsi untuk nilai kosong.
18. Pilih opsi `CC-100`, lalu klik `[Apply]`.
19. Verifikasi hanya baris Ahmad Fauzi yang tampil dan baris bernilai kosong pada Cost Center tersaring keluar.
20. Verifikasi badge titik (tanpa angka) muncul pada ikon Filter saat panel terbuka.
21. Klik ikon Filter untuk menutup panel.
22. Verifikasi badge titik muncul pada ikon Filter saat panel tertutup.
23. Klik ikon Filter untuk membuka panel, klik `[Clear Field]`, lalu klik `[Apply]`.
24. Verifikasi badge titik hilang setelah filter di-clear.
25. Klik ikon Filter untuk menutup panel.

### Filter independen dari visibilitas kolom (TC 495)

26. Sembunyikan kolom Position lewat Setup Column, lalu klik `[Save]`.
27. Klik ikon Filter.
28. Verifikasi field filter Position tetap tersedia walau kolom disembunyikan.
29. Tampilkan kembali kolom Position lewat Setup Column, lalu klik `[Save]`.
30. Pilih opsi `Finance Officer` pada field Position, lalu klik `[Apply]`.
31. Sembunyikan kembali kolom Position lewat Setup Column, lalu klik `[Save]`.
32. Buka panel Filter.
33. Verifikasi filter Position yang sudah ter-Apply tetap aktif: tabel menampilkan hanya Siti Rahmawati dan Fitri Handayani.
34. Klik `[Clear Field]`, lalu klik `[Apply]`.
35. Tampilkan kolom Position lewat Setup Column, lalu klik `[Save]`.

## Notes

- Langkah penghubung (S-03): langkah 1, 3, 4, 7 sampai 10, 12, 14, 15, 18, 21, 23, 25 sampai 27, 29 sampai 32, 34, dan 35. Langkah 7, 8, 23, 25, 34, dan 35 membersihkan Search, filter, atau kolom sebelum TC berikutnya (S-09). Langkah 2 dan 11 adalah pembanding positif asersi universal langkah 5, 19, dan 33 (8b butir 2).
- Temuan untuk QA:
  - TC 495 tidak menyebut nilai filter Position; spec memakai `Finance Officer`. Panel Filter diasumsikan tetap terbuka sesudah `[Save]` Setup Column (langkah 29 ke 30); TC tidak menyatakannya.
  - Panel Filter diasumsikan tetap terbuka sesudah `[Apply]` (langkah 8 dan 23); TC tidak menyatakannya.
  - TC 493 Expected b menyebut "nilai ter-Apply terakhir"; tidak ada filter ter-Apply sebelum langkah 9, sehingga nilai yang diasersi adalah field kosong.
