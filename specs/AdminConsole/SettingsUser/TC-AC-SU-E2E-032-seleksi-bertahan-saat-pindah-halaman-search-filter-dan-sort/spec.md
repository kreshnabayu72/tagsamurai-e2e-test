---
id: TC-AC-SU-E2E-032-seleksi-bertahan-saat-pindah-halaman-search-filter-dan-sort
title: "Seleksi Checkbox Bertahan saat Pindah Halaman, Search, Filter, dan Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-134
  - TC-AC-SU-326
  - TC-AC-SU-327
coverage:
  web: automated
---

# Seleksi Checkbox Bertahan saat Pindah Halaman, Search, Filter, dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-134, 326, 327 | `Jane Smith` | `Jane Smith {runId}-032` | `janesmith+{runId}-032@qwertysystem.net` | Activated, Active |
| TC-AC-SU-134, 326, 327 | `John Doe` | `John Doe {runId}-032` | `johndoe+{runId}-032@qwertysystem.net` | Activated, Active |
| TC-AC-SU-326 | `Mike Tan` | `Mike Tan {runId}-032` | `miketan+{runId}-032@qwertysystem.net` | Activated, Active |
| TC-AC-SU-134 | (user generik, TC tidak menyebut nama) | `User Seleksi 01 {runId}-032` sampai `User Seleksi 09 {runId}-032` | `userseleksiNN+{runId}-032@qwertysystem.net` | 9 user Activated, Active; total 12 user seed, page size 10 |

- N total dari seeding: Search atas suffix spec menampilkan 12 baris (2 halaman, halaman 1 berisi 10 baris, halaman 2 berisi 2 baris: urutan A-Z `Jane Smith`, `John Doe`, `Mike Tan`, lalu `User Seleksi 01` sampai `User Seleksi 09`).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-134: Seleksi bertahan saat pindah halaman, search, dan sort

1. Ketik Search `{runId}-032`, tekan Enter
2. Centang `Jane Smith {runId}-032` dan `John Doe {runId}-032` di halaman 1
3. Verifikasi counter `2 Users selected`
4. Pindah ke halaman 2
5. Verifikasi counter `2 Users selected`
6. Ganti isi kotak search dengan `Seleksi`, tekan Enter
7. Verifikasi counter `2 Users selected`
8. Klik header Name (urutan Name berubah dari A-Z ke Z-A)
9. Verifikasi counter `2 Users selected`
10. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-327: Sort tidak mereset seleksi

11. Ganti isi kotak search dengan `John Doe {runId}-032`, tekan Enter
12. Centang `John Doe {runId}-032`
13. Klik header Email (urutan Email A-Z)
14. Verifikasi `John Doe {runId}-032` tetap tercentang
15. Klik header Email dua kali lagi sampai indikator sort netral
16. Verifikasi counter `1 User selected`
17. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-326: Seleksi checkbox bertahan saat Search/Filter berubah dan lintas halaman

18. Ganti isi kotak search dengan `{runId}-032`, tekan Enter
19. Centang `John Doe {runId}-032` dan `Jane Smith {runId}-032`
20. Ganti isi kotak search dengan `mike`, tekan Enter
21. Verifikasi counter `2 Users selected` meski baris tidak tampil
22. Klik `✕` pada Search, tekan Enter
23. Ketik Search `{runId}-032`, tekan Enter
24. Verifikasi checkbox `John Doe {runId}-032` dan `Jane Smith {runId}-032` tetap tercentang setelah Search dikosongkan
25. Pindah ke halaman 2 lalu kembali ke halaman 1
26. Verifikasi checkbox `John Doe {runId}-032` dan `Jane Smith {runId}-032` tetap tercentang setelah pindah halaman
27. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 10, 17, dan 27 (batalkan seleksi sebelum TC berikutnya, S-09), langkah 11 (Search nama `John Doe {runId}-032` sebelum mencentang, supaya baris target tampil di halaman 1 untuk arah sort Name A-Z maupun Z-A, S-14), langkah 15 (header Email diklik dua kali lagi sampai sort netral, supaya blok TC-326 tidak bergantung arah klik pertama), langkah 18 (Search atas suffix sebelum mencentang; urutan netral menaruh `Jane Smith` dan `John Doe` di halaman 1), langkah 23 (Search atas suffix supaya baris target terlihat, S-14), langkah 28 (reset Search).
- Urutan TC dalam spec: 134, 327, 326 (TC-AC-SU-326 memakai Search dan pindah halaman; TC-AC-SU-327 hanya sort), tidak ada ketergantungan data antar blok.
- Temuan untuk QA:
  - TC-AC-SU-134 langkah 3 menyebut "keyword yang tidak memuat 2 baris itu" tanpa nilai; spec memakai `Seleksi`, kata yang tidak ada pada nama, email, atau suffix `Jane Smith` dan `John Doe`.
  - TC-AC-SU-326 judul menyebut Search/Filter; langkah hanya menggunakan Search, Filter tidak diasersi.
  - TC-AC-SU-326 langkah 3 (`✕` → Enter) tidak menyebut apakah daftar menampilkan kedua baris; spec menambahkan Search atas suffix sebelum mengasersi checkbox (langkah 23, S-14).
  - Nama user TC (`Jane Smith`, `John Doe`, `Mike Tan`) dipakai sebagai nama bersuffix `{runId}-032` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
