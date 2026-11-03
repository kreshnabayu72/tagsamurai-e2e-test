---
id: TC-FA-CF-E2E-098-search-sort-literal-dan-tie-breaker-company-nama-khusus
title: "Search Literal, Sort Tie-Breaker, dan Sort Tanpa Peka Huruf (Company Nama Khusus)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-369
  - TC-FA-CF-404
  - TC-FA-CF-637
coverage:
  web: automated
---

# Search Literal, Sort Tie-Breaker, dan Sort Tanpa Peka Huruf (Company Nama Khusus)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Nama Khusus (Pre-setup #37). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Nama Khusus, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NAMAKHUSUS_PASSWORD`; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture. Nama env `FA_TC_NAMAKHUSUS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini; fixture baru belum ada, `Fixture.faCustomFields.namaKhusus`): Company Nama Khusus (Pre-setup #37) berisi baseline Pre-setup #11 dan #12 (delapan field tab General) ditambah tujuh field tab General bernama literal tanpa suffix karena asersi bergantung pada karakter nama dan urutan huruf besar-kecil: `Markup <b>Bold</b> Tag`, `Dup Name`, `dup name`, `Cap, "Pump"`, `charlie lower`, `Bravo Upper`, `Delta Upper`. Jumlah baris tab General 15 (delapan baseline ditambah tujuh), tampil dua halaman pada ukuran halaman bawaan 10; jumlah diturunkan dari seeding.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Nama Khusus di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan isi sel tabel dengan teks literal (tanpa menafsirkan HTML), urutan baris pada halaman teramati, dan kotak Search.
- State global: ukuran halaman tabel diubah ke 25 pada langkah 16 dan dikembalikan ke 10 pada langkah 21.

## Test Steps

### TC-FA-CF-369: Karakter khusus dan markup pada Search dicocokkan sebagai teks biasa

1. Ketik Search `<b>x</b>`, tekan Enter
2. Verifikasi pencarian `<b>x</b>` tidak menafsirkan HTML (kata kunci tampil sebagai teks apa adanya pada kotak Search, tanpa elemen tebal)
3. Verifikasi pencarian `<b>x</b>` tidak menjalankan skrip (tidak ada dialog atau perubahan halaman akibat kata kunci)
4. Ganti isi kotak search dengan `%`, tekan Enter
5. Ganti isi kotak search dengan `Markup`, tekan Enter
6. Verifikasi nilai sel Field Name baris `Markup <b>Bold</b> Tag` tampil sebagai teks apa adanya (`Markup <b>Bold</b> Tag`, tanpa cetak tebal)
7. Klik `(←)`

### TC-FA-CF-404: Baris dengan Field Name sama berurutan stabil dan arah mengikuti sort aktif

8. Klik header `Field Name` sekali (menaik)
9. Catat urutan dua baris `Dup Name` dan `dup name` pada urutan menaik
10. Klik header `Field Name` sekali lagi (menurun)
11. Catat urutan dua baris `Dup Name` dan `dup name` pada urutan menurun
12. Pindah ke halaman 2 lalu kembali ke halaman 1
13. Verifikasi urutan dua baris bernama sama (tanpa membedakan huruf besar-kecil) stabil antar request dan antar halaman (sama dengan yang dicatat pada langkah 11)
14. Verifikasi urutan menurun adalah kebalikan penuh dari urutan menaik untuk dua baris tersebut (langkah 11 terhadap langkah 9)

### TC-FA-CF-637: Sort Field Name tidak membedakan huruf besar dan kecil

15. Klik header `Field Name` sekali lagi hingga ikon sort netral
16. Ubah ukuran halaman tabel ke 25
17. Klik header `Field Name` sekali (menaik)
18. Verifikasi urutan relatif menaik: `Bravo Upper`, `charlie lower`, `Delta Upper`
19. Klik header `Field Name` sekali lagi (menurun)
20. Verifikasi urutan relatif menurun: `Delta Upper`, `charlie lower`, `Bravo Upper`
21. Ubah ukuran halaman tabel kembali ke 10

## Notes

- Spec memuat 21 langkah, di bawah ambang sekitar 35 langkah. Satu dataset (Company Nama Khusus), satu akun, satu topik (nilai literal dan urutan nama di tabel utama).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (Search `Markup` menemukan baris `Markup <b>Bold</b> Tag` yang nilai selnya diasersi pada langkah 6, R-16); langkah 7 (`(←)` menutup input dan mengosongkan keyword); langkah 9 dan 11 (mencatat urutan untuk perbandingan); langkah 15 (mereset sort, karena TC-FA-CF-404 berakhir pada sort menurun dan klik berikutnya mengembalikan ikon sort netral sebelum TC-FA-CF-637 memulai siklus dari klik pertama); langkah 16 dan 21 (ukuran halaman 25 agar ketiga baris `Bravo Upper`, `charlie lower`, dan `Delta Upper` berada pada satu halaman pada kedua arah, lalu dikembalikan ke 10).
- Langkah 4 (Search `%`) tidak punya Expected sendiri pada TC-FA-CF-369 dan tidak diasersi.
- Temuan untuk QA:
  - Email dan sandi akun Total Control Company Nama Khusus tidak tertulis di Pre-setup TC (Pre-setup #37 hanya mendefinisikan datanya); nama env `FA_TC_NAMAKHUSUS_PASSWORD` diusulkan.
  - Lampiran A konvensi belum memuat pengecualian S-12 untuk nama literal tanpa suffix modul Fixed Asset > Settings > Custom Fields (Pre-setup #37); spec ini memakai nama literal Pre-setup yang tidak diubah spec, seeding idempotent oleh seed reset Company.
  - TC-FA-CF-369 Expected a menyebut "tidak menafsirkan HTML dan tidak menjalankan skrip" tanpa menyebut hasil baris untuk `<b>x</b>` maupun cara memeriksanya; langkah 2 dan 3 mengasersi kata kunci tampil sebagai teks dan tidak ada dialog atau perubahan halaman. Langkah TC "Cari `%`" (langkah 4 spec) tidak punya Expected.
  - Langkah TC-FA-CF-404 "Pindah halaman dan kembali" (langkah 12 spec) memerlukan lebih dari satu halaman; Company Nama Khusus berisi 15 baris sehingga ada dua halaman pada ukuran halaman 10.
  - TC-FA-CF-404 dan TC-FA-CF-637 tidak menyebut ukuran halaman untuk memuat seluruh baris yang dibandingkan; spec memakai ukuran halaman 25 pada TC-FA-CF-637 (langkah 16).
  - TC-FA-CF-369, TC-FA-CF-404, dan TC-FA-CF-637 tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
