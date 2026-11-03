---
id: TC-AC-LCS-E2E-090-unsaved-changes-back-backdrop-dan-refresh
title: "Proteksi Keluar Halaman: Tombol Back Browser, Backdrop Dialog, dan Konfirmasi Bawaan Browser pada Refresh F5"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-341
  - TC-AC-LCS-342
  - TC-AC-LCS-343
  - TC-AC-LCS-344
  - TC-AC-LCS-345
coverage:
  web: automated
---

# Proteksi Keluar Halaman: Tombol Back Browser, Backdrop Dialog, dan Konfirmasi Bawaan Browser pada Refresh F5

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): menangani dialog `beforeunload` bawaan browser (konfirmasi muat ulang) pada langkah F5 saat form dirty.
- Data uji: Max Trial Duration `30` lalu `45`; menu sidebar Plans & Features sebagai tujuan keluar.
- Riwayat browser memuat halaman sebelum Lifecycle Settings: hook `beforeEach` suite membuka halaman lewat menu sidebar dari halaman aplikasi sebelumnya (disediakan tim FE); langkah Back pada TC-AC-LCS-341 kembali ke halaman itu.
- State global yang diubah: Max Trial Duration tersimpan `45` pada TC-AC-LCS-345; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-341: Tombol Back browser keluar dari Lifecycle Settings dengan tab dirty memunculkan dialog Unsaved Changes

1. Ubah Max Trial Duration dari `30` menjadi `45`
2. Klik tombol Back browser hingga meninggalkan halaman Lifecycle Settings
3. Verifikasi dialog "Unsaved Changes" dengan body "You have unsaved changes. Are you sure you want to leave?" tampil
4. Klik `[Leave]`
5. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings

### TC-AC-LCS-342: Klik area backdrop di luar dialog Unsaved Changes diabaikan

6. Ubah Max Trial Duration dari `30` menjadi `45`
7. Klik menu Plans & Features di sidebar
8. Verifikasi dialog "Unsaved Changes" dengan body "You have unsaved changes. Are you sure you want to leave?" tampil
9. Klik area backdrop di luar dialog
10. Verifikasi dialog "Unsaved Changes" tetap tampil dan tidak tertutup
11. Verifikasi halaman Lifecycle Settings tetap terbuka
12. Klik `[Leave]`
13. Klik menu Plans & Licensing > Lifecycle Settings di sidebar, lalu buka tab Trial Settings

### TC-AC-LCS-343: Refresh F5 saat tab dirty memunculkan konfirmasi bawaan browser

14. Ubah Max Trial Duration dari `30` menjadi `45`
15. Tekan F5
16. Verifikasi konfirmasi bawaan browser (`beforeunload`) tampil sebelum halaman dimuat ulang
17. Konfirmasi dialog `beforeunload` agar halaman dimuat ulang

### TC-AC-LCS-344: Refresh F5 saat seluruh tab clean tidak memunculkan konfirmasi bawaan browser

18. Tekan F5
19. Verifikasi halaman Lifecycle Settings dimuat ulang
20. Verifikasi tidak ada konfirmasi bawaan browser

### TC-AC-LCS-345: Refresh F5 setelah Save berhasil tidak memunculkan konfirmasi bawaan browser

21. Ubah Max Trial Duration dari `30` menjadi `45`
22. Klik `[Save]`
23. Tunggu aksi Save selesai (toast sukses tampil dan `[Save]` kembali disabled)
24. Tekan F5
25. Verifikasi halaman Lifecycle Settings dimuat ulang
26. Verifikasi tidak ada konfirmasi bawaan browser

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 4, 12 (meninggalkan halaman dengan `[Leave]` agar form dirty ditutup, S-08 dan S-09), langkah 5, 13 (membuka kembali halaman Lifecycle Settings), langkah 17 (mengonfirmasi dialog `beforeunload` agar form dirty hilang lewat muat ulang; kemampuan tertulis di Prerequisites), dan langkah 23 (menunggu Save selesai).
- Langkah 8 adalah asersi tambahan di luar Expected TC-AC-LCS-342 (Expected hanya menyebut dialog tetap tampil sesudah klik backdrop); dicatat sebagai anchor positif bagi asersi dialog tidak tertutup.
- Asersi tidak ada konfirmasi bawaan browser memakai halaman Lifecycle Settings yang dimuat ulang sebagai anchor positif (bagian 8b butir 2).
- Teks dan tombol konfirmasi `beforeunload` ditentukan browser, sehingga spec hanya mengasersi tampil atau tidaknya konfirmasi.
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - TC-AC-LCS-343 sampai TC-AC-LCS-345 bergantung pada kemampuan menangani dialog `beforeunload`; bila tim FE belum dapat, spec ditandai `coverage.web: unsupported`, bukan dihapus.
  - Precondition TC-AC-LCS-341 butir d (riwayat browser memuat halaman sebelum Lifecycle Settings) tidak menyebut cara menyiapkannya.
