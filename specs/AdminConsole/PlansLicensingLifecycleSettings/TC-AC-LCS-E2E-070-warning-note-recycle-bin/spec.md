---
id: TC-AC-LCS-E2E-070-warning-note-recycle-bin
title: "Warning Note Recycle Bin: Muncul, Bertahan Saat Save Gagal, dan Hilang Setelah Save atau Reset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-328
  - TC-AC-LCS-329
  - TC-AC-LCS-330
coverage:
  web: automated
---

# Warning Note Recycle Bin: Muncul, Bertahan Saat Save Gagal, dan Hilang Setelah Save atau Reset

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Save tab Recycle Bin (permintaan pertama saja) gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Data uji: Permanently Delete Recycle Bin `30` lalu `45`.
- State global yang diubah: nilai tersimpan Permanently Delete Recycle Bin menjadi `45` pada TC-AC-LCS-329, lalu kembali ke default `30` oleh Reset to Default pada TC-AC-LCS-330; pemulihan cadangan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab Recycle Bin

### TC-AC-LCS-328: Mengubah Permanently Delete Recycle Bin memunculkan warning note dan mengembalikan nilai menyembunyikannya

2. Verifikasi warning note tidak tampil di bawah field Permanently Delete Recycle Bin
3. Ubah Permanently Delete Recycle Bin dari `30` menjadi `45`, lalu klik area kosong di luar field (blur)
4. Verifikasi warning note (severity warning) tampil di bawah field: "Changing this value will recalculate the deletion countdown for all items currently in the Recycle Bin."
5. Kembalikan Permanently Delete Recycle Bin menjadi `30`, lalu klik area kosong di luar field (blur)
6. Verifikasi warning note hilang
7. Verifikasi `[Save]` disabled

### TC-AC-LCS-329: Warning note Recycle Bin tetap tampil saat Save gagal 500 dan hilang setelah Save berhasil

8. Pasang intercept: permintaan Save tab Recycle Bin yang pertama dipaksa gagal HTTP 500, permintaan berikutnya diteruskan ke backend
9. Ubah Permanently Delete Recycle Bin dari `30` menjadi `45`
10. Klik `[Save]`
11. Verifikasi toast error "Error, failed to save recycle bin settings."
12. Verifikasi warning note tetap tampil
13. Klik `[Save]` lagi
14. Verifikasi toast sukses "Success, recycle bin settings have been saved."
15. Verifikasi warning note hilang setelah tab refresh

### TC-AC-LCS-330: Warning note Recycle Bin tidak tampil saat tab dimuat dan setelah Reset to Default

16. Muat ulang halaman dengan F5, lalu buka tab Recycle Bin
17. Verifikasi warning note tidak tampil
18. Klik `[Reset to Default]`
19. Verifikasi toast sukses "Success, recycle bin settings have been reset to default."
20. Verifikasi warning note tidak tampil

## Notes

- P-2: intercept HTTP 500 pada Save pertama (langkah 8) hanya berfungsi sebagai pemicu state UI yang diuji (warning note tetap tampil saat Save gagal); toast error adalah bagian Expected TC-AC-LCS-329, bukan objek uji resilience.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab), langkah 8 (memasang intercept), dan langkah 16 (membuka tab dalam keadaan termuat baru).
- Precondition TC-AC-LCS-330 (Permanently Delete Recycle Bin tersimpan `45`) dipenuhi oleh state akhir TC-AC-LCS-329 pada spec yang sama.
- Asersi warning note tidak tampil memakai tab Recycle Bin yang sudah termuat (field Permanently Delete Recycle Bin tampil) sebagai anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Precondition TC-AC-LCS-329 (Save pertama gagal, berikutnya sukses) membutuhkan intercept bersyarat per permintaan yang tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE.
