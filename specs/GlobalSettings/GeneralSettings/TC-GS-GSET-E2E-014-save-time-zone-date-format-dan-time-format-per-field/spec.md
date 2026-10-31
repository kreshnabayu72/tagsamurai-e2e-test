---
id: TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field
title: "Save per Field Date & Time: Time Zone (UTC), Date Format, dan Time Format"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-33
  - TC-GS-GSET-183
  - TC-GS-GSET-34
  - TC-GS-GSET-35
coverage:
  web: automated
---

# Save per Field Date & Time: Time Zone (UTC), Date Format, dan Time Format

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`).
- Kemampuan teknis: klien HTTP dengan sesi API Total Control Client A (`Spectra.env.GS_TC_PASSWORD`) untuk PUT `/v2/enterprise-management/general-settings` dengan payload baseline `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`. Dipakai untuk memulihkan baseline di antara blok TC (langkah 20 dan 30); hook `after` suite memulihkan baseline ulang walau spec gagal di tengah.
- Data Uji: Time Zone `UTC` (label `(UTC+00:00) UTC, Reykjavik, Accra`, dikunci PRD §4.3a) menggantikan alias "Time Zone Lain" pada TC-GS-GSET-33; Date Format `M/d/yy`; Time Format `hh:mm a`. Tidak ada Data Dinamis yang dibuat; baris Changelog dihasilkan oleh Save spec ini dan tidak dihapus (audit trail permanen).
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Baseline Changelog: jumlah baris Modal Changelog hasil Search `Time Zone` dicatat sebelum aksi pertama (langkah 1 sampai 3) dan dipakai pada asersi langkah 17 (S-12).
- Tidak ada state global lain yang diubah. Spec mengubah record Client A sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`).
- TC-GS-GSET-33, 183, 34, 35: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-33 dan TC-GS-GSET-183: Save Time Zone `UTC` (satu alur)

1. Buka Modal Changelog lewat ikon Changelog di header halaman, ketik Search `Time Zone`, tekan Enter
2. Catat jumlah total baris hasil Search sebagai `{nTimeZone}` (0 bila hasil kosong)
3. Tutup Modal Changelog lewat `✕`
4. Klik Select "Time Zone" dan catat label opsi yang terpilih (`(UTC+07:00) Bangkok, Hanoi, Jakarta`)
5. Ketik `UTC` di kotak pencarian Select Time Zone
6. Verifikasi opsi `(UTC+00:00) UTC, Reykjavik, Accra` ada di daftar dan muncul saat mengetik `UTC`
7. Pilih opsi `(UTC+00:00) UTC, Reykjavik, Accra`
8. Verifikasi opsi dapat dipilih: Select Time Zone menampilkan `(UTC+00:00) UTC, Reykjavik, Accra`
9. Klik `[Save]`
10. Verifikasi tidak ada dialog tambahan sebelum request simpan (Dialog Change Currency dan Dialog Unsaved Changes tidak tampil)
11. Verifikasi toast sukses: `Success, general settings has been saved.`
12. Verifikasi Button "Save" kembali disabled (form di-rebase ke nilai tersimpan)
13. Muat ulang halaman (F5)
14. Verifikasi Select Time Zone menampilkan `(UTC+00:00) UTC, Reykjavik, Accra` (nilai tersimpan `UTC`)
15. Verifikasi field lain tidak berubah: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Session Idle Timeout `30 minutes`
16. Buka Modal Changelog, ketik Search `Time Zone`, tekan Enter
17. Verifikasi jumlah total baris hasil Search sama dengan `{nTimeZone}` + 1 (tepat 1 baris baru)
18. Verifikasi baris teratas: Action `Edit`, Field `Time Zone`, Old Value `(UTC+07:00) Bangkok, Hanoi, Jakarta`, New Value `(UTC+00:00) UTC, Reykjavik, Accra`
19. Tutup Modal Changelog lewat `✕`
20. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), lalu muat ulang halaman (F5)

### TC-GS-GSET-34: Save Date Format saja

21. Pilih Date Format `M/d/yy`
22. Klik `[Save]`
23. Verifikasi tidak ada dialog tambahan sebelum request simpan
24. Verifikasi toast sukses: `Success, general settings has been saved.`
25. Verifikasi Button "Save" kembali disabled (form di-rebase ke nilai tersimpan)
26. Verifikasi Preview Date & Time `3/17/23 14:30`
27. Muat ulang halaman (F5)
28. Verifikasi Date Format `M/d/yy`
29. Verifikasi field lain tidak berubah: Currency Code `IDR`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
30. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), lalu muat ulang halaman (F5)

### TC-GS-GSET-35: Save Time Format saja

31. Pilih Time Format `hh:mm a`
32. Klik `[Save]`
33. Verifikasi tidak ada dialog tambahan sebelum request simpan
34. Verifikasi toast sukses: `Success, general settings has been saved.`
35. Verifikasi Button "Save" kembali disabled (form di-rebase ke nilai tersimpan)
36. Verifikasi Preview Date & Time `17/03/23 02:30 PM`
37. Muat ulang halaman (F5)
38. Verifikasi Time Format `hh:mm a`
39. Verifikasi field lain tidak berubah: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional tanpa kelas harness (Save per field).
- TC-GS-GSET-33 dan TC-GS-GSET-183 dilebur menjadi satu alur (blok langkah 1 sampai 20): keduanya Save Time Zone dari `Asia/Jakarta` ke opsi selain `Asia/Jakarta`, tanpa alur baru; "Time Zone Lain" pada TC-GS-GSET-33 dipetakan ke `UTC`. Pemetaan Expected: TC-GS-GSET-33 a ke langkah 10, b ke 11, c ke 12, d ke 14 dan 15; TC-GS-GSET-183 a ke langkah 6 dan 8, b ke 11, c ke 12, d ke 14 dan 15, e ke 17 dan 18. TC-GS-GSET-183 diurutkan setelah TC-GS-GSET-33 sesuai kolom Dependensi.
- Spec melewati sekitar 35 langkah (39) karena tiga blok Save yang berpola sama (empat TC, TC-GS-GSET-33 dan TC-GS-GSET-183 dilebur) (pilih, Save, tiga asersi hasil Save, muat ulang, dua asersi nilai tersimpan); semuanya satu kelas (Save satu field) dan tiap blok berdiri sendiri dengan baseline yang dipulihkan lewat API, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung: langkah 1 sampai 3 (mencatat baseline Changelog sebelum aksi); langkah 3, 19 (menutup Modal Changelog); langkah 4 (mencatat label opsi awal, dipakai sebagai Old Value pada langkah 18); langkah 20 dan 30 (memulihkan baseline lewat API dan memuat ulang halaman); langkah 16 (Search `Time Zone` untuk membaca baris yang diasersi).
- Jumlah baris Changelog tidak diasersi sebagai angka absolut (S-12): hanya selisih terhadap `{nTimeZone}`.
- Temuan untuk QA:
  - TC-GS-GSET-33, 34, 35, 36: Post Condition a (Changelog dan Activity Log mencatat perubahan), b (event `general_settings.updated` ke Admin Console, FAMS, SAMS), dan c (File Download/Export memakai format baru, dieksekusi di TC modul lain) tidak punya langkah observasi di TC-GS-GSET-33, 34, 35, sehingga tidak diasersi di spec ini. Baris Changelog Time Zone hanya diasersi lewat Expected e TC-GS-GSET-183.
  - TC-GS-GSET-33: "Time Zone Lain" tidak punya nilai pasti karena daftar opsi Time Zone di luar dua opsi PRD §4.3a ditentukan programmer; spec memakai `UTC`.
  - TC-GS-GSET-183 langkah 1: label opsi terpilih dicatat tanpa Expected tersendiri; spec mencatatnya sebagai langkah tanpa `Verifikasi` dan memakainya pada Old Value baris Changelog.
