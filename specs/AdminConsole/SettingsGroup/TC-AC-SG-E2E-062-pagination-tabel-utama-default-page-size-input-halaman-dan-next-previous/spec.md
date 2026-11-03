---
id: TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous
title: "Pagination Tabel Utama: Default, Page Size, Input Nomor Halaman, dan Next/Previous"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-223
  - TC-AC-SG-224
  - TC-AC-SG-225
  - TC-AC-SG-226
coverage:
  web: automated
---

# Pagination Tabel Utama: Default, Page Size, Input Nomor Halaman, dan Next/Previous

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16), node `All Groups` terpilih, 14 group (page size bawaan 10 baris: halaman 1 berisi 10 baris, halaman 2 berisi 4 baris), tanpa Search, Sort, dan Filter aktif.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-223: Pagination default 10 baris dan pilihan 10/25/50/100

1. Verifikasi halaman 1 menampilkan 10 baris dari 14 baris (info pagination)
2. Pindah ke halaman 2
3. Verifikasi halaman 2 menampilkan 4 baris
4. Pindah kembali ke halaman 1
5. Buka Overlay Page Size
6. Verifikasi pilihan page size `10`, `25`, `50`, dan `100`
7. Verifikasi tidak ada opsi `All` pada pilihan page size

### TC-AC-SG-224: Mengubah page size menampilkan lebih banyak baris dalam satu halaman

8. Pilih page size 25
9. Verifikasi seluruh 14 baris tampil pada halaman 1
10. Verifikasi tidak ada halaman 2

### TC-AC-SG-225: Input nomor halaman langsung lalu Enter

11. Pilih page size 10
12. Ketik 2 pada input nomor halaman, tekan Enter
13. Verifikasi tabel menampilkan halaman 2 dengan 4 baris

### TC-AC-SG-226: Navigasi Next dan Previous antar halaman

14. Pindah kembali ke halaman 1
15. Klik Next
16. Verifikasi Next membuka halaman 2
17. Klik Previous
18. Verifikasi Previous kembali ke halaman 1
19. Verifikasi sort dan filter tidak berubah (tidak ada indikator sort maupun indikator filter aktif)

## Notes

- Langkah penghubung (S-03): langkah 4 (kembali ke halaman 1 sebelum membuka Overlay Page Size), langkah 11 (mengembalikan page size ke 10 sebelum TC-225), langkah 14 (kembali ke halaman 1 sebelum TC-226, S-09).
- Pilihan page size 10, 25, 50, 100 (langkah 6) diasersi pada Overlay Page Size yang dibuka di langkah 5; langkah 7 (absence opsi `All`) didahului langkah 6 yang membuktikan opsi lain tampil (8b butir 2).
- Temuan untuk QA:
  - TC-AC-SG-226 Expected "sort dan filter tidak berubah" tidak didahului langkah yang menyetel sort atau filter; spec mengasersi keadaan netral (tanpa indikator).
