---
id: TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi
title: "Paginasi Company Volume: Ukuran Halaman dan Navigasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-434
  - TC-FA-CF-435
  - TC-FA-CF-436
  - TC-FA-CF-437
  - TC-FA-CF-438
  - TC-FA-CF-440
coverage:
  web: automated
---

# Paginasi Company Volume: Ukuran Halaman dan Navigasi

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`). Kelas harness: volume data.
- Akun aktor: Total Control Company Volume (Pre-setup #20) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Volume (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_VOLUME_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_VOLUME_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup (tetap di environment, tidak diubah spec ini): Company Volume dengan 120 field Inactive pada tab General (`Volume Field 001` sampai `Volume Field 120`, Scope General), 12 halaman pada page size 10, dirujuk lewat fixture baru `Fixture.faCustomFields.volume` (fixture belum ada, disediakan tim FE). Seed volume dipulihkan hook `before` (disediakan tim FE/BE).
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan jumlah baris tabel, nomor halaman aktif, dan nama baris pertama halaman.
- State global: tidak ada yang diubah (page size dan halaman hanya state tampilan).
- Parameter iterasi langkah 13 dan 14 (tabel Nomor Halaman Tidak Valid, TC-FA-CF-436):

| No | Nilai input |
|---|---|
| 1 | `0` |
| 2 | `-1` |
| 3 | `99` |
| 4 | `abc` |

## Test Steps

### TC-FA-CF-434: Paginasi default 10 baris per halaman dengan pilihan 10, 25, 50, 100

1. Perhatikan footer paginasi
2. Verifikasi halaman pertama menampilkan 10 baris
3. Buka pilihan page size
4. Verifikasi pilihan page size: `10`, `25`, `50`, `100`
5. Verifikasi pilihan page size tidak memuat opsi `All`
6. Tutup pilihan page size

### TC-FA-CF-435: Navigasi next, previous, dan input nomor halaman langsung

7. Klik next ke halaman 2
8. Verifikasi halaman 2 aktif dan tabel menampilkan 10 baris yang sesuai untuk halaman tersebut
9. Ketik `5` pada input nomor halaman, tekan Enter
10. Verifikasi halaman 5 aktif dan tabel menampilkan 10 baris yang sesuai untuk halaman tersebut
11. Klik previous
12. Verifikasi halaman 4 aktif dan tabel menampilkan 10 baris yang sesuai untuk halaman tersebut

### TC-FA-CF-436: Nomor halaman tidak valid diabaikan

Untuk setiap baris tabel Nomor Halaman Tidak Valid pada `## Prerequisites` (langkah 13 dan 14):

13. Ketik nilai pada input nomor halaman, tekan Enter
14. Verifikasi input tidak valid diabaikan dan tabel tetap di halaman 4

### TC-FA-CF-437: Mengganti page size kembali ke halaman 1

15. Pindah ke halaman 3
16. Ganti page size menjadi 25
17. Verifikasi tabel kembali ke halaman 1
18. Verifikasi tabel menampilkan 25 baris

### TC-FA-CF-438: Mengganti sort tetap di nomor halaman sekarang

19. Ganti page size kembali ke 10
20. Pindah ke halaman 3
21. Catat Field Name pada baris pertama halaman 3
22. Klik header `Field Name`
23. Verifikasi tabel tetap di halaman 3
24. Verifikasi Field Name pada baris pertama halaman 3 berbeda dari yang dicatat (urutan dataset berubah)

### TC-FA-CF-440: Paginasi tiap tab terpisah dan tersimpan saat pindah tab

25. Pindah ke halaman 3 pada tab General
26. Klik tab `Purchasing`
27. Klik tab `General`
28. Verifikasi paginasi tab General masih di halaman 3

## Notes

- Spec memuat 28 langkah nominal (langkah 13 dan 14 diulang empat kali, 34 langkah setelah ekspansi), di bawah ambang sekitar 35 langkah. Satu kelas harness (volume data), satu dataset (Company Volume 120 field), tanpa mengubah data. TC-FA-CF-439 (menghapus baris terakhir) memakai varian 101 field dan ada di spec 176.
- Langkah yang diulang: langkah 13 dan 14 untuk tiap baris tabel Nomor Halaman Tidak Valid.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (menutup pilihan page size), langkah 19 (mengembalikan page size ke 10 setelah TC-FA-CF-437), langkah 21 (mencatat baris pertama sebagai pembanding asersi langkah 24).
- Urutan TC di spec: 434, 435, 436, 437, 438, 440. TC-FA-CF-436 dijalankan pada halaman 4 hasil langkah 11; TC-FA-CF-438 dan 440 memakai halaman 3 yang sama (langkah 20 dan 25).
- Temuan untuk QA:
  - Email akun Total Control Company Volume tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-435 Expected ("dengan baris yang sesuai") tidak menyebut baris; spec memeriksa nomor halaman aktif dan 10 baris yang tampil.
  - TC-FA-CF-438 Expected ("urutan dataset berubah") tidak menyebut urutan awal; spec membandingkan Field Name baris pertama sebelum dan sesudah klik header, dan asersi itu gagal bila urutan default sudah sama dengan Sort `Field Name` menaik.
  - TC-FA-CF-440 mencantumkan "120 field pada General" tanpa menyebut Company Volume memiliki field tab Purchasing; spec hanya mengasersi paginasi tab General.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
