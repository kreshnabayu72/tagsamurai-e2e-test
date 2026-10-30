---
id: TC-GS-GSET-E2E-017-save-currency-konfirmasi-multi-field-dan-tanpa-perubahan-currency
title: "Save dengan Konfirmasi Change Currency, Multi Field, dan Save Tanpa Perubahan Currency"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-38
  - TC-GS-GSET-43
  - TC-GS-GSET-41
coverage:
  web: automated
---

# Save dengan Konfirmasi Change Currency, Multi Field, dan Save Tanpa Perubahan Currency

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`).
- Kemampuan teknis:
  - Klien HTTP dengan sesi API Total Control Client A (`Spectra.env.GS_TC_PASSWORD`) untuk PUT `/v2/enterprise-management/general-settings` dengan payload baseline `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`, untuk memulihkan baseline di antara blok (langkah 13 dan 22); hook `after` suite memulihkan baseline ulang walau spec gagal di tengah.
  - `Spectra.intercept()` sebagai penghitung request PUT `/v2/enterprise-management/general-settings` yang tetap meneruskan request ke server; dipasang di langkah 1, disetel ulang ke 0 di langkah 13 dan 22, dan dilepas di langkah 29.
  - Membaca teks label opsi Currency Code `USD` dari dropdown saat memilihnya (label dan simbol opsi selain `IDR` ditentukan programmer, NC-10), dicatat sebagai `{simbolUSD}`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Data Uji: Currency Code `USD`; kombinasi lima field TC-GS-GSET-43 (`USD`, Date Format `dd MMM yy`, Time Format `hh:mm a`, Time Zone `UTC` menggantikan "Time Zone Lain", Session Idle Timeout `2 hours`); Date Format `M/d/yy` dan Session Idle Timeout `1 hour` untuk TC-GS-GSET-41. Tidak ada Data Dinamis yang dibuat; baris Changelog dihasilkan oleh Save spec ini dan tidak dihapus (audit trail permanen).
- Spec mengubah record Client A sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`).
- TC-GS-GSET-38, 43, 41: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-38: Klik Change Currency melanjutkan Save

1. Pasang penghitung request PUT general settings (intercept, request diteruskan ke server)
2. Pilih Currency Code `USD` dan catat simbol pada label opsi `USD` sebagai `{simbolUSD}`
3. Klik `[Save]`
4. Klik `[Change Currency]`
5. Verifikasi dialog tertutup
6. Verifikasi penghitung request PUT bernilai tepat 1 (request simpan terkirim)
7. Verifikasi toast sukses: `Success, general settings has been saved.`
8. Verifikasi Button "Save" disabled
9. Verifikasi Preview Currency `{simbolUSD} 5.000,00`
10. Muat ulang halaman (F5)
11. Verifikasi Currency Code `USD`
12. Verifikasi field lain tidak berubah: Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
13. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), muat ulang halaman (F5), lalu setel ulang penghitung request PUT ke 0

### TC-GS-GSET-43: Save beberapa field sekaligus termasuk Currency Code

14. Pilih Currency Code `USD`, Date Format `dd MMM yy`, Time Format `hh:mm a`, Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`, dan Session Idle Timeout `2 hours`
15. Klik `[Save]`
16. Verifikasi Dialog Change Currency muncul
17. Klik `[Change Currency]`
18. Verifikasi Dialog Change Currency tidak muncul lagi (dialog hanya muncul sekali, yaitu setelah klik `[Save]`)
19. Verifikasi toast sukses: `Success, general settings has been saved.`
20. Muat ulang halaman (F5)
21. Verifikasi kelima field sesuai nilai baru: Currency Code `USD`, Date Format `dd MMM yy`, Time Format `hh:mm a`, Time Zone `(UTC+00:00) UTC, Reykjavik, Accra`, Session Idle Timeout `2 hours`
22. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), muat ulang halaman (F5), lalu setel ulang penghitung request PUT ke 0

### TC-GS-GSET-41: Save tanpa perubahan Currency Code tidak memunculkan Dialog Change Currency

23. Pilih Date Format `M/d/yy` dan Session Idle Timeout `1 hour`
24. Klik `[Save]`
25. Verifikasi Dialog Change Currency tidak muncul
26. Verifikasi penghitung request PUT bernilai tepat 1 (request simpan langsung terkirim)
27. Verifikasi toast sukses: `Success, general settings has been saved.`
28. Verifikasi Button "Save" disabled
29. Lepas penghitung request PUT

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional (Save yang melibatkan Dialog Change Currency).
- "Time Zone Lain" pada TC-GS-GSET-43 dipetakan ke `UTC` (label `(UTC+00:00) UTC, Reykjavik, Accra`, dikunci PRD §4.3a).
- Pemetaan Expected: TC-GS-GSET-38 a ke langkah 5 dan 6, b ke 7, c ke 8, d ke 9, e ke 11 dan 12; TC-GS-GSET-43 a ke langkah 16 dan 18 (dialog muncul sekali) serta 19 (toast), b ke 21; TC-GS-GSET-41 a ke langkah 25 dan 26, b ke 27, c ke 28.
- Dialog Change Currency pada langkah 16 menjadi anchor positif sebelum asersi absence pada langkah 18; screening isi dialog ada di spec 016 sehingga langkah 4 tidak didahului `Verifikasi` dialog muncul.
- Langkah penghubung: langkah 13 dan 22 (memulihkan baseline lewat API, memuat ulang halaman, dan menyetel ulang penghitung); langkah 29 (melepas intercept).
- Temuan untuk QA:
  - TC-GS-GSET-38 dan TC-GS-GSET-43: Post Condition (Changelog dan Activity Log mencatat perubahan Currency Code, 5 baris Changelog/Activity Log pada TC-GS-GSET-43, konsumen format menampilkan simbol baru, File Download/Export memakai simbol baru) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-GS-GSET-38 dan TC-GS-GSET-43: label dan simbol opsi Currency Code `USD` serta label opsi Time Zone selain dua opsi PRD §4.3a tidak dikunci di PRD (NC-09, NC-10); spec membaca simbol `USD` dari dropdown saat memilih.
  - TC-GS-GSET-43: Expected a menyebut dialog muncul "sekali"; spec mengasersinya dengan memverifikasi dialog tidak muncul lagi sesudah `[Change Currency]`.
