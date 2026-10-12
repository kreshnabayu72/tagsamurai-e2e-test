---
id: TC-GS-BRAND-E2E-020-edit-validasi-diblokir-dan-nama-sendiri
title: "Validasi Edit Brand yang Diblokir dan Nama Milik Sendiri"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-71
  - TC-GS-BRAND-72
  - TC-GS-BRAND-74
  - TC-GS-BRAND-76
  - TC-GS-BRAND-77
coverage:
  web: automated
---

# Validasi Edit Brand yang Diblokir dan Nama Milik Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data pre-setup (data environment tetap, tidak dibuat atau diubah spec ini): brand Client A `Orion Tech` (bebas relasi) dan `Acme Corp` (dipakai FAMS Asset Name Forklift). Fixture belum ada; tim FE menyiapkan `fixtures/brand.json` untuk identitas data ini.
- Data dinamis: tidak ada. Seluruh kasus berakhir pada Save yang diblokir dan form ditutup lewat `Leave`, sehingga tidak ada data tercipta atau berubah dan tidak ada cleanup. Nilai input uji (string 121 karakter, `acme corp`, `🚀`) dibangun atau diketik langsung oleh langkah; kunci fixture `fixtures/brand.json` (nilai disediakan tim FE): `orionTech`, `acmeCorp`. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > Master Reference > Brand.
- Kemampuan teknis: input keystroke emoji (`🚀`) ke field; mengetik string 121 karakter; membaca status respons dan request jaringan untuk memastikan Save yang diblokir tidak mengirim request Edit.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-BRAND-77: Form Edit dengan nama milik sendiri tidak menampilkan error duplikat

1. Buka Global Settings > Master Reference > Brand, lalu cari baris Orion Tech (lewat pagination atau Search)
2. Catat nilai Last Updated baris Orion Tech
3. Klik `⋯` baris Orion Tech > Edit → modal Edit Brand terbuka
4. Tunggu ±1 detik tanpa mengubah nilai field Brand Name
5. Verifikasi error `Brand Name already exists` tidak muncul
6. Hapus isi field Brand Name, lalu ketik ulang `Orion Tech`
7. Tunggu ±500 ms (debounce pengecekan keunikan)
8. Verifikasi error `Brand Name already exists` tidak muncul

### TC-GS-BRAND-74: Emoji diblok di level input pada field Brand Name (Edit)

9. Ketik `🚀` di akhir nilai `Orion Tech` pada field Brand Name
10. Verifikasi karakter emoji tidak masuk ke field (keystroke difilter)
11. Verifikasi tidak ada pesan error
12. Verifikasi nilai field tetap `Orion Tech`

### TC-GS-BRAND-72: Edit Brand Name 121 karakter

13. Ganti isi field Brand Name dengan string 121 karakter
14. Verifikasi error inline `Max. 120 characters` tampil saat mengetik
15. Klik [Save]
16. Verifikasi Save diblokir: modal tetap terbuka, tidak ada request Edit terkirim, dan tidak ada toast sukses

### TC-GS-BRAND-71: Save Edit dengan Brand Name kosong

17. Hapus seluruh isi field Brand Name
18. Klik [Save]
19. Verifikasi error inline `Brand Name must not be empty`
20. Verifikasi data tidak berubah: modal tetap terbuka, tidak ada request Edit terkirim, dan tidak ada toast sukses

### TC-GS-BRAND-76: Edit dengan nama brand lain menampilkan error duplikat

21. Ubah isi field Brand Name menjadi `acme corp`
22. Tunggu ±500 ms
23. Klik [Save]
24. Verifikasi error inline `Brand Name already exists`
25. Verifikasi data Orion Tech tidak berubah: modal tetap terbuka, tidak ada request Edit sukses, dan tidak ada toast sukses
26. Klik `✕` di header modal Edit Brand
27. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
28. Klik [Leave]
29. Verifikasi baris Orion Tech di tabel tidak berubah: nama tetap `Orion Tech`, Last Updated sama dengan nilai yang dicatat pada langkah 2, dan tidak ada baris `acme corp` baru

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan nomor TC sumber, mengikuti prinsip bagian 3 konvensi: kasus tanpa error (TC-77) dan filter keystroke (TC-74) dulu, lalu validasi diblokir (TC-72, TC-71), dan TC-76 terakhir karena form berakhir dalam keadaan dirty lalu ditutup (prinsip 6). Satu modal Edit Orion Tech dipakai berulang untuk kelima TC, jadi hanya ada satu kali buka form.
- Langkah 15 dan 18 (klik [Save] pada TC-72 dan TC-71) adalah penerapan prinsip 7 (tiap validasi diakhiri submit yang diblokir); langkah Uji TC-72 sumber hanya berhenti pada mengetik 121 karakter.
- Langkah penghubung: langkah 26 sampai 28 menutup form dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]` (teks dan tombol dialog dari TC-GS-BRAND-83 dan TC-GS-BRAND-85); langkah ini bukan asersi TC-76. Langkah 6 dan 7 mengikuti Langkah Uji TC-77 (hapus isi field, ketik ulang `Orion Tech`, tunggu ±500 ms).
- Semua TC di spec ini memakai brand pre-setup `Orion Tech` yang tidak diubah, sehingga tidak ada nama brand dinamis dan tidak memakai suffix `{runId}`.
