---
id: TC-AC-DC-E2E-088-sinkron-format-tanggal-general-settings
title: "Format Tanggal General Settings Tercermin pada Kolom Date dan Date Filter Panel Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-239
  - TC-AC-DC-240
coverage:
  web: automated
---

# Format Tanggal General Settings Tercermin pada Kolom Date dan Date Filter Panel Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control #1 (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Budi Santoso), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture backend (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: riwayat Changelog Pre-setup #17 hanya dibaca (baris `Scanner` pada langkah 5, rentang 1 Sep 2026 sampai 10 Sep 2026 pada langkah 9). Pohon Pre-setup #14 tidak diubah dan tidak dipakai.
- State global yang diubah: General Settings entitas uji (Pre-setup #19) diubah di hook `before` menjadi Date Format `M/d/yy`, Time Format 12 jam, Timezone Asia/Jakarta; hook `after` memulihkannya ke Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta. Pelaku perubahan dan kemampuan mengubah General Settings lewat sesi API disediakan tim FE/BE (akun pelaku tidak disebut TC, PRD, atau LLD). Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): tidak ada data dinamis yang dibuat spec ini; pemulihan General Settings di hook `after` tetap jalan walau spec gagal di tengah.

## Test Steps

### TC-AC-DC-239: Format tanggal General Settings tercermin pada kolom Date Changelog

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi tabel Changelog menampilkan sedikitnya satu baris
3. Verifikasi kolom Date pada seluruh baris yang tampil mengikuti Date Format `M/d/yy` dan Time Format 12 jam dengan Timezone Asia/Jakarta
4. Ketik Search `Scanner`, tekan Enter
5. Verifikasi baris Create `Scanner` menampilkan Date tanggal 9/1/26 dan jam 8:30 AM
6. Tutup modal Changelog lewat `[×]`

### TC-AC-DC-240: Format tanggal General Settings tercermin pada isian Date Filter Panel Changelog

7. Klik ikon Changelog pada header Sidebar Category
8. Klik ikon Filter
9. Pilih rentang Date 1 Sep 2026 sampai 10 Sep 2026 dengan date picker
10. Verifikasi teks nilai tanggal pada isian field Date menampilkan 9/1/26 sampai 9/10/26 (mengikuti Date Format `M/d/yy`)

## Notes

- P-5 (b): dua TC objek-uji ringan kelas h (format tanggal General Settings) pada surface Changelog yang sama; tiap TC tanpa harness eksternal dan tanpa state berat sendiri.
- Langkah penghubung (S-03): langkah 6 (menutup modal Changelog sehingga Search dan Filter direset sebelum TC berikutnya, S-09) dan Search pada langkah 4 untuk menemukan baris `Scanner` (R-16).
- Spec berakhir dengan Filter Panel terbuka dan modal Changelog terbuka tanpa perubahan data; hook `beforeEach` suite menutup dialog (bagian 4, reset state ringan).
- Temuan untuk QA:
  - TC-AC-DC-239 Expected menulis "seluruh baris" Date mengikuti format. Karena audit trail permanen yang tumbuh, spec mengasersi baris yang tampil pada halaman pertama (anchor: sedikitnya satu baris) dan baris literal Pre-setup #17 `Scanner` (Create, 01/09/26 08:30) yang ditemukan lewat Search. Asersi baris `Scanner` bergantung pada nama literal itu dan pada keberadaan riwayat Pre-setup #17 di environment.
  - Pre-setup #19 menyebut nilai awal General Settings (Date Format `dd/MM/yy`, Time Format 24 jam), sedangkan TC-AC-DC-239 dan 240 mengubahnya menjadi `M/d/yy` dan 12 jam tanpa menyebut pelaku dan cara mengubahnya; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13).
  - TC-AC-DC-240 tidak menyebut cara menutup Filter Panel; spec berakhir dengan panel terbuka tanpa mengubah data.
