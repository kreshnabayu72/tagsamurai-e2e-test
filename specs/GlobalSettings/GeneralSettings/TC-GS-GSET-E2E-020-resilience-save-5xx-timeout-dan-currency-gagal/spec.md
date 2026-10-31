---
id: TC-GS-GSET-E2E-020-resilience-save-5xx-timeout-dan-currency-gagal
title: "Resilience Save: Gagal 5xx, Timeout, dan Gagal Setelah Konfirmasi Change Currency"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-46
  - TC-GS-GSET-47
  - TC-GS-GSET-48
coverage:
  web: automated
---

# Resilience Save: Gagal 5xx, Timeout, dan Gagal Setelah Konfirmasi Change Currency

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`).
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada PUT `/v2/enterprise-management/general-settings` dan dilepas segera setelah pemicu selesai (S-09):
  - respons dipaksa HTTP 500 tanpa meneruskan request ke server (TC-GS-GSET-46, dilepas di langkah 10; TC-GS-GSET-48, dilepas di langkah 34);
  - request dipaksa tidak mendapat respons sampai timeout klien (TC-GS-GSET-47, dilepas di langkah 22).
- Kemampuan teknis:
  - Klien HTTP dengan sesi API Total Control Client A (`Spectra.env.GS_TC_PASSWORD`) untuk GET `/v2/enterprise-management/general-settings` (membaca nilai tersimpan di server, langkah 8) dan PUT dengan payload baseline `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30` (memulihkan baseline, langkah 13).
  - Memuat ulang halaman dengan konfirmasi bawaan browser `beforeunload` dikonfirmasi otomatis oleh harness (langkah 32: form masih berisi perubahan belum tersimpan), tanpa langkah bersyarat.
- Data Uji: Session Idle Timeout `1 hour`, Time Format `hh:mm a`, Currency Code `USD`. Tidak ada Data Dinamis yang dibuat; Save berhasil di langkah 11 menghasilkan baris Changelog yang tidak dihapus (audit trail permanen).
- Spec mengubah record Client A sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`); hook `after` suite memulihkan baseline dan melepas semua intercept.
- TC-GS-GSET-46, 47, 48: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-46: Save gagal 5xx, form tetap unsaved, dan dapat dicoba lagi

1. Paksa respons PUT general settings HTTP 500 (intercept)
2. Pilih Session Idle Timeout `1 hour`
3. Klik `[Save]`
4. Verifikasi toast error: `Error, failed to save general settings.`
5. Verifikasi form tetap terbuka
6. Verifikasi Session Idle Timeout tetap `1 hour` (input dipertahankan)
7. Verifikasi Button "Save" kembali enabled
8. Baca nilai tersimpan di server lewat GET API (sesi API Total Control Client A)
9. Verifikasi Session Idle Timeout tersimpan di server tetap `30 minutes` (`sessionIdleTimeout` 30)
10. Lepas intercept HTTP 500
11. Klik `[Save]`
12. Verifikasi toast sukses: `Success, general settings has been saved.`
13. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), lalu muat ulang halaman (F5)

### TC-GS-GSET-47: Save gagal karena timeout

14. Buat PUT general settings tidak mendapat respons (intercept timeout)
15. Pilih Time Format `hh:mm a`
16. Klik `[Save]`
17. Tunggu hingga timeout klien
18. Verifikasi toast error: `Error, failed to save general settings.`
19. Verifikasi form tetap terbuka
20. Verifikasi Time Format tetap `hh:mm a`
21. Verifikasi Button "Save" enabled kembali
22. Lepas intercept timeout
23. Pilih kembali Time Format `HH:mm` (nilai tersimpan)

### TC-GS-GSET-48: Save gagal 5xx setelah konfirmasi Change Currency

24. Paksa respons PUT general settings HTTP 500 (intercept)
25. Pilih Currency Code `USD`
26. Klik `[Save]`
27. Klik `[Change Currency]`
28. Verifikasi dialog tertutup
29. Verifikasi toast error: `Error, failed to save general settings.`
30. Verifikasi Currency Code tetap `USD` (form unsaved)
31. Verifikasi Button "Save" enabled
32. Muat ulang halaman (F5), konfirmasi bawaan browser `beforeunload` dikonfirmasi
33. Verifikasi Currency Code `IDR`
34. Lepas intercept HTTP 500

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE dengan intercept parsial. Kelas fault injection (prinsip 13b): kegagalan Save yang dipaksakan (500 dan timeout).
- Pemetaan Expected: TC-GS-GSET-46 a ke langkah 4, b ke 5 sampai 7, c ke 8 dan 9, d ke 12; TC-GS-GSET-47 a ke langkah 18, b ke 19, 20, dan 21; TC-GS-GSET-48 a ke langkah 28 dan 29, b ke 30 dan 31, c ke 33.
- Langkah penghubung: langkah 10, 22, 34 (melepas intercept segera setelah pemicu; langkah 10 dilakukan sebelum Save kedua sesuai langkah 6 TC-GS-GSET-46); langkah 13 (memulihkan baseline dan memuat ulang halaman); langkah 23 (mengembalikan Time Format ke nilai tersimpan supaya form bersih sebelum blok berikutnya).
- Temuan untuk QA:
  - TC-GS-GSET-48: langkah 5 TC memuat ulang halaman saat form masih berisi perubahan belum tersimpan (`USD`), sehingga browser menampilkan konfirmasi bawaan `beforeunload` (PC §24.1d). TC tidak menyebut konfirmasi itu; spec mengonfirmasinya otomatis (Prerequisites).
  - TC-GS-GSET-47: durasi timeout klien tidak disebut TC; spec menunggu sampai toast error tampil.
