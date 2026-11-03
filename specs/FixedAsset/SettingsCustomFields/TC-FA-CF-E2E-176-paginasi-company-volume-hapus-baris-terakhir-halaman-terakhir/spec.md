---
id: TC-FA-CF-E2E-176-paginasi-company-volume-hapus-baris-terakhir-halaman-terakhir
title: "Paginasi Company Volume: Hapus Baris Terakhir di Halaman Terakhir (Varian 101 Field)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-439
coverage:
  web: automated
---

# Paginasi Company Volume: Hapus Baris Terakhir di Halaman Terakhir (Varian 101 Field)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`). Kelas harness: volume data (varian 101 field).
- Akun aktor: Total Control Company Volume (Pre-setup #20) dengan email mengikuti pola Pre-setup #1 `totalControl_automated_{namaCompany}@qwertysystem.net` dan `{namaCompany}` = Company Volume (email akun ini tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_VOLUME_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_VOLUME_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup: Company Volume varian 101 field Inactive pada tab General (Scope General; 11 halaman pada page size 10, halaman 11 berisi satu baris), dirujuk lewat fixture baru `Fixture.faCustomFields.volume101` (fixture belum ada, disediakan tim FE). Hook `before` spec ini memulihkan seed Company Volume ke varian 101 field (seed reset Company, disediakan tim FE/BE).
- Data yang diubah spec: satu field dari seed varian 101 dihapus pada langkah 4 (baris tunggal halaman 11). Data seed Company Volume tidak dapat dimiliki spec (jumlah tepat 101 field adalah objek uji), sehingga hook `before` spec ini dan spec lain yang memakai Company Volume memulihkan seed; hook `after` memulihkan seed Company Volume ke baseline 120 field.
- Data Dinamis: tidak ada.
- Hook suite yang berlaku (lihat `suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan jumlah baris tabel dan nomor halaman aktif.
- State global: tidak ada selain seed Company Volume yang dipulihkan.

## Test Steps

### TC-FA-CF-439: Menghapus baris terakhir di halaman terakhir memindahkan ke halaman terakhir yang masih ada

1. Pindah ke halaman terakhir (halaman 11)
2. Verifikasi halaman 11 aktif dan tabel menampilkan satu baris
3. Klik row action `⋯` > `Delete` pada baris tersebut
4. Klik `[Delete]` pada dialog konfirmasi `Delete Custom Field`
5. Verifikasi tabel pindah ke halaman terakhir yang masih ada (halaman 10)

## Notes

- Spec memuat 5 langkah. Spec ini memakai varian seed berbeda (101 field) dan satu-satunya aksi yang menghapus data pada kelompok paginasi Company Volume; TC-FA-CF-434 sampai 438 dan 440 ada di spec 114.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (sesuai langkah uji TC), langkah 4 (mengonfirmasi dialog Delete; teks dialog dan tombol `[Delete]` mengikuti TC-FA-CF-317 karena TC-FA-CF-439 tidak menyebut dialog). Hasil Delete tidak diasersi lewat toast; asersi langkah 5 memakai perpindahan halaman.
- Temuan untuk QA:
  - Email akun Total Control Company Volume tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup #1, dan akunnya disediakan tim FE.
  - TC-FA-CF-439 Precondition ("Company dengan 101 field") tidak menyebut nama Company; Pre-setup #20 hanya menyebut "varian 101 field". Spec memakai Company Volume varian 101 field.
  - TC-FA-CF-439 menghapus baris Pre-setup (S-06 butir pengecualian 2026-10-30): seed 101 field tidak dapat dimiliki spec karena jumlah tepat 101 adalah objek uji; pemulihan dijamin seed reset Company yang disediakan tim FE/BE.
  - TC-FA-CF-439 tidak menyebut dialog konfirmasi Delete; spec memakai dialog dari TC-FA-CF-317.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
