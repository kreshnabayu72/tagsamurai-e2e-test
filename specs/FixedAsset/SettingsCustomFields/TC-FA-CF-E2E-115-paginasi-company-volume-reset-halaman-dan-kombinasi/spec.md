---
id: TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi
title: "Paginasi Company Volume: Reset ke Halaman 1 dan Kombinasi Search, Filter, Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-372
  - TC-FA-CF-391
  - TC-FA-CF-441
  - TC-FA-CF-442
coverage:
  web: automated
---

# Paginasi Company Volume: Reset ke Halaman 1 dan Kombinasi Search, Filter, Sort

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`). Kelas harness: volume data.
- Akun aktor: Total Control Company Volume (Pre-setup #20) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Volume (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_VOLUME_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_VOLUME_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Volume dengan 120 field Inactive pada tab General (`Volume Field 001` sampai `Volume Field 120`, Scope General, seluruhnya bertipe `Text` menurut asumsi spec ini, lihat Temuan untuk QA), dirujuk lewat fixture baru `Fixture.faCustomFields.volume` (fixture belum ada, disediakan tim FE). Seed volume dipulihkan hook `before` (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan jumlah baris tabel, nomor halaman aktif, dan nama baris.
- State global: tidak ada yang diubah (Search, Filter, Sort, dan page size hanya state tampilan).

## Test Steps

### TC-FA-CF-372: Menjalankan Search selagi di halaman lebih dari 1 mereset paginasi ke halaman 1

1. Klik icon Search
2. Pindah ke halaman 3
3. Ketik Search `Volume Field 01`, tekan Enter
4. Verifikasi tabel berada di halaman 1
5. Verifikasi tabel menampilkan hasil pencarian `Volume Field 01` (baris `Volume Field 010` sampai `Volume Field 019`)
6. Klik `(←)` pada kotak Search

### TC-FA-CF-391: Apply filter selagi di halaman lebih dari 1 mereset paginasi ke halaman 1

7. Pindah ke halaman 3
8. Klik icon Filter, pilih Data Type `Text`, klik `[Apply]`
9. Verifikasi tabel berada di halaman 1
10. Bersihkan Filter lewat Filter Panel (klik `[Clear Field]`, lalu klik `[Apply]`)

### TC-FA-CF-441: Kombinasi Search, Filter, Sort, dan Pagination berlaku harmonis

11. Ketik Search `Volume`, tekan Enter
12. Klik icon Filter, pilih Data Type `Text`, klik `[Apply]`
13. Urutkan Field Name menurun (klik header `Field Name` hingga menurun)
14. Ganti page size menjadi 25
15. Verifikasi Search `Volume` masih terpasang
16. Verifikasi Filter Data Type `Text` masih terpasang
17. Verifikasi Sort Field Name menurun berlaku (baris teratas `Volume Field 120`, lalu `Volume Field 119`)
18. Verifikasi page size 25 berlaku (halaman 1 menampilkan 25 baris)
19. Klik menu `Custom Fields` dari sidebar

### TC-FA-CF-442: Melepas salah satu saringan pada hasil kosong memulihkan data

20. Ketik Search `Volume`, tekan Enter
21. Klik icon Filter, pilih Data Type `Formula`, klik `[Apply]`
22. Verifikasi tabel menampilkan hasil kosong (empty state)
23. Hapus filter Data Type (klik `✕` pada chip Data Type), klik `[Apply]`
24. Verifikasi baris `Volume Field` tampil kembali pada tabel

## Notes

- Spec memuat 24 langkah, di bawah ambang sekitar 35 langkah. Satu kelas harness (volume data), satu dataset (Company Volume 120 field), tanpa mengubah data.
- Urutan TC di spec: 372, 391, 441, 442. Search dan Filter dipulihkan di antara TC (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (`(←)` menutup kotak Search dan mereset tabel), langkah 10 (membersihkan Filter), langkah 19 (klik sidebar mereset Search, Sort, Filter, dan paginasi sebelum TC-FA-CF-442). Langkah 3, 11, dan 20 adalah Search untuk menyaring baris target (R-16).
- Langkah 22 adalah anchor positif (empty state tampil) untuk langkah 24.
- Temuan untuk QA:
  - Email akun Total Control Company Volume tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - Pre-setup #20 tidak menyebut Data Type ke-120 field Volume; TC-FA-CF-391 dan 441 memfilter `Text` dan mengharapkan hasil, sehingga spec mengasumsikan seluruhnya `Text`. Bila tidak, Expected "tabel berada di halaman 1" pada langkah 9 menjadi ambigu (hasil kosong).
  - TC-FA-CF-372 Expected tidak menyebut baris hasil; Search `Volume Field 01` dibaca cocok dengan `Volume Field 010` sampai `Volume Field 019`.
  - TC-FA-CF-441 Expected ("tanpa saling menimpa") tidak menyebut hasil tiap kontrol; langkah 15 sampai 18 memeriksa tiap kontrol tetap berlaku, dengan baris teratas diturunkan dari penamaan seed `Volume Field 001` sampai `120`.
  - TC-FA-CF-442 Expected tidak menyebut teks empty state; spec memeriksa empty state tampil tanpa teks.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
