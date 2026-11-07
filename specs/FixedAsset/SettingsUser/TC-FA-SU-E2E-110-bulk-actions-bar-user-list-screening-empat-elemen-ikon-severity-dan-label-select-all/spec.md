---
id: TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all
title: "Bulk Actions Bar User List: Screening Empat Elemen, Ikon Severity, dan Label Select All"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1041
  - TC-FA-SU-1042
  - TC-FA-SU-1043
coverage:
  web: automated
---

# Bulk Actions Bar User List: Screening Empat Elemen, Ikon Severity, dan Label Select All

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Pengguna Pre-setup yang dicentang atau diamati (tanpa aksi tulis): Hana Kusuma (Pending Activation, Active), Kartika Sari (Pending Activation, Inactive), dan Indra Wijaya (Pending Email Confirmation). Ketiganya berada di halaman 1 pada default sort Name ascending.
- N pada `Select All ([N] records)` = 23 (25 pengguna dikurangi Default User dan akun sendiri, sesuai TC-FA-SU-1043).

## Test Steps

### TC-FA-SU-1041: Screening Bulk Actions Bar

1. Ketik Search `Hana Kusuma`, tekan Enter
2. Centang baris Hana Kusuma
3. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter
4. Centang baris Kartika Sari
5. Klik `(←)` pada kotak Search
6. Verifikasi Bulk Actions Bar muncul dengan empat elemen berurutan dari kiri ke kanan: dropdown `Bulk Action`, counter `2 Users selected`, `Select All (23 records)`, dan ikon `(×)`
7. Klik `Bulk Action`
8. Verifikasi overlay `Bulk Action` memuat empat aksi: `Activate`, `Deactivate`, `Edit Home Group`, `Resend Activation Email`
9. Tutup overlay `Bulk Action` dengan Esc
10. Klik ikon `(×)` pada Bulk Actions Bar
11. Verifikasi Bulk Actions Bar tertutup
12. Verifikasi seleksi baris Hana Kusuma dan Kartika Sari dikosongkan

### TC-FA-SU-1042: Ikon dan severity row action serta aksi Bulk Actions Bar

13. Ketik Search `Hana Kusuma`, tekan Enter
14. Klik ⋯ pada baris Hana Kusuma
15. Verifikasi row action `Detail` berikon `FileInfoLine`, `Edit Home Group` berikon `Edit2Line`, dan `Resend Activation Email` berikon `MailSendLine`, seluruhnya severity dark
16. Tutup menu row action dengan Esc
17. Ganti isi kotak search dengan `Indra Wijaya`, tekan Enter
18. Klik ⋯ pada baris Indra Wijaya
19. Verifikasi row action `Resend Confirmation Email` berikon `MailSendLine` dengan severity dark
20. Tutup menu row action dengan Esc
21. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
22. Centang baris Hana Kusuma
23. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter
24. Centang baris Kartika Sari
25. Klik `Bulk Action`
26. Verifikasi aksi overlay: `Activate` berikon `CheckLine`, `Deactivate` berikon `CloseLine`, `Edit Home Group` berikon `Edit2Line`, `Resend Activation Email` berikon `MailSendLine`, seluruhnya severity dark
27. Tutup overlay dengan Esc, lalu klik ikon `(×)` pada Bulk Actions Bar
28. Klik `(←)` pada kotak Search

### TC-FA-SU-1043: Label Select All singular dan plural

29. Klik icon Search, ketik `Hana`, tekan Enter
30. Centang satu-satunya baris hasil
31. Verifikasi tombol `Select All (1 record)` tampil
32. Klik ikon `(×)` pada Bulk Actions Bar
33. Klik `(←)` pada kotak Search
34. Centang baris pertama pada tabel
35. Verifikasi tombol `Select All (23 records)` tampil
36. Verifikasi counter `1 User selected` tampil
37. Klik ikon `(×)` pada Bulk Actions Bar

## Notes

- Jumlah langkah 37, di atas smell 35 langkah; semua blok satu kelas harness (Bulk Actions Bar User List) dan berdiri sendiri; kelebihan berasal dari Search per baris yang dicentang (R-16, S-09) dan satu Verifikasi per klausa Expected (S-01).
- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 9, 16, 20, dan 27 (menutup overlay dan menu), 22 sampai 24 (mencentang kembali baris untuk langkah 3 TC-FA-SU-1042), 32 dan 37 (membersihkan seleksi, S-09), serta 5, 28, dan 33 (menutup Search dan mereset tabel; langkah 5 memulihkan tabel penuh supaya `Select All (23 records)` menghitung seluruh pengguna, bukan hasil Search terakhir, S-09). Langkah 1, 3, 13, 17, 21, 23, dan 29 adalah Search untuk menemukan baris target (R-16 dan butir 8b.13, memakai "ganti isi kotak search" bila kotak sudah berisi).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1043 langkah 4 ("Hapus Search lalu centang satu baris") tidak menyebut nasib seleksi Hana Kusuma; Expected b menyebut counter `1 User selected`, sehingga spec membersihkan seleksi sebelum mencentang baris berikutnya (langkah 32). (2) TC-FA-SU-1041 memakai `Select All ([N] records)` tanpa nilai N; N = 23 diambil dari Expected TC-FA-SU-1043. (3) TC-FA-SU-1041 dan TC-FA-SU-1042 mencentang dua pengguna sekaligus tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti serta saat Search ditutup lewat `(←)`; mohon konfirmasi.
