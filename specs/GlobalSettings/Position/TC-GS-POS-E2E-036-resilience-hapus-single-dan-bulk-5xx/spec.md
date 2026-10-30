---
id: TC-GS-POS-E2E-036-resilience-hapus-single-dan-bulk-5xx
title: "Resilience Hapus: Delete Single dan Bulk Delete saat Kegagalan Server 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-121
  - TC-GS-POS-149
coverage:
  web: automated
---

# Resilience Hapus: Delete Single dan Bulk Delete saat Kegagalan Server 5xx

## Prerequisites

- Mode: mock. Seluruh API di-mock (dijalankan tim FE sebagai integration test, tanpa backend nyata). Respons yang dipaksa:
  - Daftar Position (`POST /v2/iam/positions/list`, LLD:9, openapi:11): memuat 3 baris `IT Manager {runId}-036`, `System Administrator {runId}-036`, dan `Technical Writer {runId}-036`, ketiganya bebas relasi: `userCount` 0 pada baris respons list (LLD:19, LLD:257), yang menentukan Dialog Delete Position (single, D-01) dan dialog Bulk Delete homogen (D-04) tampil. List selalu memuat ketiga baris karena tidak ada penghapusan yang berhasil.
  - Request hapus Position single (`DELETE /v2/iam/positions` dengan satu `ids`, LLD:248, openapi:355): respons 500 (langkah 1).
  - Request Bulk Delete Position (`DELETE /v2/iam/positions` dengan beberapa `ids`, LLD:248, openapi:355): respons 500 (langkah 11).
  - SSE `position.created`, `position.updated`, dan `position.deleted` (LLD:182, :337, :260): halaman berlangganan; stream disediakan tim FE dan tidak ada event yang dikirim selama spec ini.
  - API pendukung di luar sumber modul (identitas pengguna, menu, payload sesi dan izin Total Control agar row action Delete dan Bulk Action Bar tampil) disediakan tim FE.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1) sebagai identitas sesi; sesi disediakan harness mock, tanpa login nyata dan tanpa password.
- Data Dinamis (hanya sebagai isi respons mock, tidak ada data yang dibuat di backend): `IT Manager {runId}-036`, `System Administrator {runId}-036`, `Technical Writer {runId}-036`. Fixture baru `Fixture.position.resilienceDelete036`. Data Pre-setup tidak dipakai.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): lepas semua intercept dan mock yang dipasang spec ini; tutup dialog atau dismiss toast yang masih ada.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 dan mengganti hasil mock; memuat ulang halaman (F5) tanpa dialog `beforeunload` (tidak ada form terbuka); membaca ketahanan toast (toast error tidak hilang otomatis; toast sukses hilang otomatis setelah 4 detik, `foundation/functions/toast-copy.md`) dan men-dismiss toast.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`; pada mode mock flag ini termasuk API pendukung yang disediakan tim FE.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; `## Test Steps` tidak mengulang langkah buka karena spec ini tidak menguji navigasi.

## Test Steps

### TC-GS-POS-121: Delete single, kegagalan server 5xx

1. Pasang intercept pada request hapus Position (single): respons 500
2. Klik `⋯` pada baris `IT Manager {runId}-036`, pilih `Delete`
3. Klik `[Delete]` pada dialog Delete Position
4. Verifikasi toast error "Error, failed to delete position." tampil
5. Verifikasi dialog Delete Position tetap terbuka
6. Verifikasi `[Delete]` enabled untuk retry
7. Dismiss toast error, lalu klik `[Cancel]` pada dialog Delete Position
8. Muat ulang halaman (F5) dengan respons mock list yang masih memuat `IT Manager {runId}-036`
9. Verifikasi baris `IT Manager {runId}-036` tetap ada
10. Lepas intercept pada request hapus Position (single)

### TC-GS-POS-149: Bulk Delete, kegagalan server 5xx

11. Pasang intercept pada request Bulk Delete Position: respons 500
12. Centang baris `System Administrator {runId}-036` dan `Technical Writer {runId}-036`
13. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
14. Klik `[Delete]` pada dialog Delete Position
15. Verifikasi toast error "Error, failed to delete position." tampil
16. Verifikasi toast error tetap tampil setelah jeda melebihi 4 detik (durasi hilang otomatis toast sukses), tidak hilang otomatis
17. Verifikasi dialog Delete Position tetap terbuka
18. Verifikasi `[Delete]` enabled untuk retry
19. Dismiss toast error, lalu klik `[Cancel]` pada dialog Delete Position
20. Muat ulang halaman (F5) dengan respons mock list yang masih memuat kedua baris
21. Verifikasi baris `System Administrator {runId}-036` tetap ada
22. Verifikasi baris `Technical Writer {runId}-036` tetap ada
23. Lepas intercept pada request Bulk Delete Position

## Notes

- Mode: mock. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Expected "baris tetap ada" (TC-GS-POS-121 c dan TC-GS-POS-149 c) diasersi dari tampilan tabel setelah muat ulang respons mock list (langkah 9, 21, dan 22).
- Urutan TC dipertahankan (121, lalu 149); Delete single tidak menghapus data, sehingga tidak ada aksi yang menghabisi data di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 19 (dismiss toast dan `[Cancel]` agar halaman dapat dimuat ulang tanpa dialog terbuka), langkah 8 dan 20 (muat ulang untuk mengamati list dari respons mock), langkah 10 dan 23 (melepas intercept). Muat ulang pada langkah 20 sekaligus mengosongkan seleksi baris dari TC-GS-POS-149.
- TC-GS-POS-149 menyebut baris `System Administrator` dan `Technical Writer` dari Data Dinamis No. 20 sampai 34 (TC-GS-POS-123); pada mode mock cukup diberikan oleh respons mock list dengan suffix `{runId}-036`.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi, dan state backend nyata tidak teruji pada mode mock: TC-GS-POS-121 ("Record tidak terhapus") dan TC-GS-POS-149 ("Tidak ada entri Delete di Changelog dan Activity Log").
  - TC-GS-POS-121 dan 149 tidak menyebut label tombol penutup dialog setelah kegagalan; spec memakai `[Cancel]` dari Dialog 1 dan Dialog 4 PRD §4.2d (D-01, D-04).
  - Expected TC-GS-POS-121 tidak menyebut perilaku ketahanan toast error; spec hanya mengasersinya pada TC-GS-POS-149 (Expected a, 4 detik).
  - Dependensi TC-GS-POS-149 pada TC-GS-POS-123 (membuat 15 nama bulk) tidak relevan pada mode mock.
