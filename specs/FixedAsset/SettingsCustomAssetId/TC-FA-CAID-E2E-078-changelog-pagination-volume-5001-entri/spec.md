---
id: TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri
title: "Modal Changelog: Pagination 5.001 Entri, Input Halaman, Ganti Page Size, Sort, dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-214
  - TC-FA-CAID-215
  - TC-FA-CAID-216
  - TC-FA-CAID-217
  - TC-FA-CAID-218
  - TC-FA-CAID-219
coverage:
  web: automated
---

# Modal Changelog: Pagination 5.001 Entri, Input Halaman, Ganti Page Size, Sort, dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Log Volume (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Log Volume, Pre-setup No 18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini (kredensial `Spectra.env.FA_LOGVOL_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_LOGVOL_TC_PASSWORD` (Total Control Company Log Volume) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 18 Company Log Volume dengan 5.001 entri Changelog Custom Asset ID; No 27 General Settings Company Log Volume (Date Format `dd/MM/yy`, Time Format 24 jam). Data Dinamis: tidak ada. Fixture modul Custom Asset ID untuk nilai ini belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Seeding (volume, kelas e): hook `before` men-seed 5.001 entri Changelog lewat API sesi aktor, dengan campuran Action `Create` dan `Edit` (sedikitnya satu entri `Edit` dibutuhkan TC-FA-CAID-219 dan lebih dari 10 entri `Edit` dibutuhkan agar Filter menghasilkan lebih dari satu halaman). Cara membuat entri Changelog dalam volume itu tidak disebut TC, PRD, atau LLD: disediakan tim BE/FE. Company dikembalikan tim FE/BE ke keadaan awal sebelum tiap run; spec hanya membaca sehingga tidak ada entri baru selama run.
- Kemampuan teknis: membuka dropdown page size dan memilih opsi; mengetik pada input nomor halaman; berpindah halaman; klik header `Date` untuk sort; membaca daftar entri Changelog Company Log Volume terurut Date terbaru di atas lewat API sesi aktor sebagai pembanding baris ke-41 sampai ke-50 (TC-FA-CAID-215; disediakan tim FE/BE, TC tidak menyebut caranya).
- Precondition TC-FA-CAID-214 sampai 219: login sebagai Total Control Company Log Volume; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Suite serial (`parallel: false`) karena Company Log Volume dipakai bersama spec volume Changelog lain.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: tidak ada (spec hanya membaca).

## Test Steps

### TC-FA-CAID-214: Pagination Changelog: default 10 data dan pilihan page size

1. Klik tombol `[Changelog]` pada header kartu
2. Verifikasi halaman 1 menampilkan 10 baris
3. Buka pilihan page size
4. Verifikasi pilihan page size `10`, `25`, `50`, `100`
5. Verifikasi tidak ada opsi `All`
6. Pilih page size `10`

### TC-FA-CAID-215: Input nomor halaman langsung pada Changelog

7. Ketik `5` pada input nomor halaman, tekan Enter
8. Verifikasi halaman 5 aktif
9. Verifikasi halaman 5 menampilkan baris ke-41 sampai ke-50 menurut urutan default Date terbaru di atas

### TC-FA-CAID-216: Nomor halaman tidak valid pada Changelog diabaikan

10. Klik `[✕]` pada Modal Changelog
11. Klik tombol `[Changelog]` pada header kartu
12. Ketik `0` pada input nomor halaman, tekan Enter
13. Verifikasi tabel tetap di halaman 1 tanpa pesan error
14. Ketik `9999` pada input nomor halaman, tekan Enter
15. Verifikasi tabel tetap di halaman 1 tanpa pesan error
16. Ketik `abc` pada input nomor halaman, tekan Enter
17. Verifikasi tabel tetap di halaman 1 tanpa pesan error

### TC-FA-CAID-217: Mengganti page size Changelog kembali ke halaman 1

18. Pindah ke halaman 2
19. Pilih page size `50`
20. Verifikasi halaman 1 aktif menampilkan 50 baris

### TC-FA-CAID-218: Mengganti sort Changelog tetap di nomor halaman sekarang

21. Pilih page size `10`
22. Pindah ke halaman 2
23. Klik header `Date` satu kali
24. Verifikasi halaman 2 tetap aktif
25. Verifikasi urutan Oldest First: indikator sort Date Oldest First aktif

### TC-FA-CAID-219: Apply Filter pada halaman lebih dari 1 mereset ke halaman 1

26. Klik header `Date` dua kali hingga indikator sort kembali ke default Newest First
27. Pindah ke halaman 3
28. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
29. Verifikasi halaman 1 aktif
30. Verifikasi tabel memuat sedikitnya satu baris Action `Edit`
31. Verifikasi tabel hanya memuat baris Action `Edit`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (214 sampai 219). Modal Changelog dibuka di langkah 1 dan dibuka kembali di langkah 11 supaya TC-FA-CAID-216 mulai dari halaman 1.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 6 dan 21 (mengembalikan page size ke 10), langkah 10 dan 11 (menutup dan membuka kembali Modal Changelog agar halaman kembali ke 1), dan langkah 26 (mengembalikan sort `Date` ke default). Pada TC-FA-CAID-219 `Verifikasi` tabel memuat sedikitnya satu baris `Edit` mendahului `Verifikasi` "hanya baris `Edit`" sebagai anchor positif (bagian 8b butir 2); Expected TC hanya menyebut "hasil tersaring".
- Kelas harness: volume data (kelas e, 5.001 entri). Asersi baris ke-41 sampai ke-50 mengacu pada daftar entri Changelog Company Log Volume terurut Date terbaru di atas yang dibaca tim FE/BE; total 5.001 entri tidak diasersi sebagai angka absolut (S-12).
- Pembagian TC lintas spec: download di atas 5.000 baris pada Changelog (TC-FA-CAID-227) ada di spec 080; Search, Filter, Sort pada tujuh entri seed ada di spec 067 sampai 073; Pagination Modal View Code List ada di spec 054 dan 055.
- Temuan untuk QA: (1) TC-FA-CAID-217 dan 218 tidak menyebut cara berpindah ke halaman 2 (klik nomor halaman, panah, atau input); spec memakai langkah "Pindah ke halaman 2". (2) TC-FA-CAID-218 Expected "urutan Oldest First" diamati lewat indikator sort Date, bukan isi baris. (3) Kolom ACC TC-FA-CAID-214 sampai 219 memuat akun #1 dan Company Log Volume (Pre-setup No 18) tanpa menyebut email akunnya; spec memakai Total Control Company Log Volume. (4) Page size TC-FA-CAID-217 diubah ke 50 lalu dikembalikan ke 10 oleh langkah penghubung; TC tidak menyebut pemulihan itu.
