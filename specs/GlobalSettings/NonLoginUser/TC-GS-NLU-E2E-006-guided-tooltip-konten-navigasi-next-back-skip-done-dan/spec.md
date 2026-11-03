---
id: TC-GS-NLU-E2E-006-guided-tooltip-konten-navigasi-next-back-skip-done-dan
title: "Guided Tooltip: konten, navigasi Next Back Skip Done, dan keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-20
  - TC-GS-NLU-22
  - TC-GS-NLU-24
  - TC-GS-NLU-25
  - TC-GS-NLU-28
coverage:
  web: automated
---

# Guided Tooltip: konten, navigasi Next Back Skip Done, dan keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: akun First Visit (Total Control tanpa flag Guided Tooltip untuk halaman ini). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.GS_FIRSTVISIT_TC_PASSWORD` (nama baru, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan tim FE). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Pengecualian hook suite (Guided Tooltip): spec ini menguji flag `guided_tooltip_seen_gs-non-login-user` sendiri. Akun First Visit dikecualikan dari penyetelan flag true oleh hook suite `before`. Spec mengatur flag untuk akun First Visit: keadaan "belum ada" dicapai lewat langkah penghubung "Hapus flag"; keadaan "sudah ada" dicapai oleh aksi `[Skip]` atau `[Done]` pada spec ini. Hook `after` spec memulihkan flag akun First Visit ke nilai awal.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak tertulis di TC, PRD, atau LLD sehingga tidak dikarang, S-13): menghapus flag, memulihkan nilai awal flag, dan membaca flag untuk satu akun.
- Data Pre-setup No. 9 sampai 12 hanya dibaca. Spec tidak membuat data dan tidak mengubah state global selain flag akun First Visit.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-20: Guided Tooltip otomatis tampil Step 1 pada kunjungan pertama

1. Hapus flag `guided_tooltip_seen_gs-non-login-user` untuk akun First Visit
2. Buka sub-tab Non-Login User (muat ulang halaman)
3. Verifikasi walkthrough muncul otomatis di Step 1
4. Verifikasi target Step 1 adalah sub-tab switcher `Non-Login User`
5. Verifikasi Title `"Non-Login Users"`
6. Verifikasi Description `"Manage people who are represented in transactions but never log in — like field workers or contractors. Every non-login user is linked to a login user who acts on their behalf."`
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil
8. Verifikasi tombol `[Back]` Hidden

### TC-GS-NLU-22: Guided Tooltip Step 2 menunjuk header kolom Actions dan tombol berubah jadi Done

9. Klik `[Next]` di Step 1
10. Verifikasi target Step 2 adalah header kolom Actions `⋯`
11. Verifikasi Title `"Non-Login User Actions"`
12. Verifikasi Description `"Manage each person from the Actions column and adjust which columns are shown. Available actions depend on your permissions."`
13. Verifikasi tombol `[Next]` berubah menjadi `[Done]`
14. Verifikasi tombol `[Back]` tampil

### TC-GS-NLU-25: Guided Tooltip Back kembali ke step sebelumnya

15. Klik `[Back]` di Step 2
16. Verifikasi walkthrough kembali ke Step 1 (Title `"Non-Login Users"`)
17. Verifikasi tombol `[Back]` Hidden di Step 1

### TC-GS-NLU-24: Guided Tooltip Done di Step 2 menutup walkthrough dan menandai sudah dilihat

18. Klik `[Next]` satu kali sampai Step 2
19. Klik `[Done]`
20. Verifikasi walkthrough tertutup
21. Muat ulang halaman
22. Verifikasi walkthrough tidak muncul otomatis

### TC-GS-NLU-28: Guided Tooltip dapat dioperasikan dengan keyboard

23. Hapus flag `guided_tooltip_seen_gs-non-login-user` untuk akun First Visit
24. Buka sub-tab Non-Login User (muat ulang halaman) hingga Step 1 tampil
25. Verifikasi kotak tooltip menerima keyboard focus saat aktif
26. Tekan `Enter`
27. Verifikasi walkthrough maju ke Step 2
28. Tekan `←`
29. Verifikasi walkthrough kembali ke Step 1
30. Tekan `→`
31. Verifikasi walkthrough maju ke Step 2
32. Tekan `Esc`
33. Verifikasi walkthrough tertutup
34. Verifikasi flag `guided_tooltip_seen_gs-non-login-user` untuk akun First Visit sudah diset (dibaca lewat kemampuan baca flag)

## Notes

- Langkah penghubung (S-03): langkah 1, 23, 24 (mengembalikan akun First Visit ke keadaan flag belum ada sebelum TC yang mensyaratkannya).
- Penyimpangan urutan (S-10): TC-GS-NLU-20, 22, 25, 24 dijalankan berantai tanpa menghapus flag di antaranya karena preconditionnya ("tampil di Step 1", "tampil di Step 2") dipenuhi oleh akhir TC sebelumnya: urutan 20 (Step 1), 22 (Step 2), 25 (kembali ke Step 1), 24 (Step 1 ke Step 2 lalu `[Done]`). TC-GS-NLU-28 butuh flag belum ada lagi sehingga didahului langkah "Hapus flag".
- Temuan untuk QA:
  - Email akun First Visit tidak tertulis di Tabel Pre-setup TC; precondition TC hanya menulis "Login sbg Role: Total Control" dan "Flag belum ada untuk akun ini". Akun dan env var diusulkan penulis dan disediakan tim FE.
  - TC-GS-NLU-28 Expected c ("flag sudah dilihat diset") tidak memberi langkah observasi flag. Spec membacanya lewat kemampuan baca flag yang disediakan tim FE/BE; cara cek lain tidak disebut TC.
  - TC-GS-NLU-28 Expected d ("Kotak tooltip menerima keyboard focus saat aktif") diasersi sebelum tombol keyboard ditekan (urutan state, bukan urutan penulisan Expected).
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
