---
id: TC-GS-GSET-E2E-012-mobile-screening-bottom-sheet-tooltip-ketuk-dan-read-only
title: "Mobile screening, bottom sheet, tooltip ketuk, Read Only"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-19
  - TC-GS-GSET-20
  - TC-GS-GSET-21
coverage:
  mobile: automated
---

# Mobile screening, bottom sheet, tooltip ketuk, Read Only

## Prerequisites

- Mode: FE+BE (aplikasi Android terhadap backend nyata).
- Platform: aplikasi Android TAG Samurai Mobile (`coverage.mobile`); spec tidak berjalan di web. Perangkat atau emulator Android uji bersama, sehingga suite berjalan serial (`parallel: false`, S-09).
- Guided Tooltip: spec ini mengecualikan hook suite untuk flag `guided_tooltip_seen_gs-general-settings` (spec mobile tidak memakai hook web suite). Hook `before` spec mencatat nilai awal flag untuk kedua akun aktor lalu menyetelnya true lewat API (disediakan tim FE/BE; nama endpoint tidak disebut di TC, PRD, atau LLD); hook `after` memulihkan nilai awal.
- Role yang diuji (Tabel Data Uji Pre-setup; langkah berbeda per role, ditulis per blok):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-GSET-19, TC-GS-GSET-21 | Total Control | Budi Santoso | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-GSET-20 | Read Only | tidak tertulis di Pre-setup TC (disediakan tim FE) | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_GSET_RO_PASSWORD` |

- Login Total Control di aplikasi Android di hook `before`; halaman Global Settings > General Settings dibuka di hook `beforeEach`. Ganti akun ke Read Only lewat langkah eksplisit (langkah 23 sampai 25); hook `after` mengembalikan sesi ke akun default suite (Total Control) dan memulihkan record Client A ke baseline.
- Tabel "Select bottom sheet" (parameter langkah berulang): `Time Zone`, `Session Idle Timeout`, `Date Format`, `Time Format`.
- Data Pre-setup No 10 (record Client A): Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`. Currency Code `USD` (label dan simbol ditentukan programmer, NC-10): `[simbol opsi USD]` adalah simbol pada label opsi `USD` yang dibaca dari bottom sheet saat memilih (langkah 6), bukan literal.
- Seeding Changelog (Data Uji Dinamis No 1 sampai 3, dipakai sebagai precondition TC-GS-GSET-21, tidak diasersi barisnya): hook `before` men-seed lewat PUT API di `global-settings/general-settings/API/openapi.yaml` (sesi Total Control) satu perubahan Session Idle Timeout `30 minutes` ke `1 hour` lalu kembali ke `30 minutes`.
- Kemampuan teknis: gesture ketuk, pembukaan dan penutupan bottom sheet, dan Back perangkat di Android; hover diganti ketuk (tooltip berbasis ketuk).
- Spec tidak menekan `[Save]`; pilihan `USD` hanya ada di form dan dikembalikan ke `IDR` di langkah 22.

## Test Steps

### TC-GS-GSET-19: Layout satu kolom, bottom sheet, sticky footer (Total Control)

1. Verifikasi field tersusun satu kolom penuh lebar
2. Verifikasi tiap kelompok field berada dalam SectionCard terpisah
3. Verifikasi urutan field dari atas ke bawah: Currency Code, Preview Currency, Date Format, Time Format, Time Zone, Preview Date & Time, Session Idle Timeout
4. Ketuk Select "Currency Code"
5. Verifikasi Select "Currency Code" membuka bottom sheet selector
6. Pilih `USD` pada bottom sheet dan catat simbol pada label opsinya sebagai `[simbol opsi USD]`
7. Verifikasi Preview Currency tampil tepat di bawah field Currency Code
8. Verifikasi Preview Currency "[simbol opsi USD] 5.000,00"
9. Untuk setiap baris tabel "Select bottom sheet" (langkah 9 sampai 11): Ketuk Select pada baris tersebut
10. Verifikasi Select pada baris tersebut membuka bottom sheet selector
11. Tutup bottom sheet tanpa memilih opsi
12. Verifikasi Button "Save" berada di sticky footer
13. Verifikasi icon Changelog tetap terlihat di header
14. Verifikasi tidak ada tombol Cancel

### TC-GS-GSET-21: Modal Changelog dan Setup Column sebagai bottom sheet (Total Control)

15. Ketuk icon Changelog di header
16. Verifikasi Modal Changelog: General Settings tampil sebagai full-height bottom sheet
17. Ketuk header kolom Actions (⋯)
18. Ketuk item `Setup Column...`
19. Verifikasi Modal Setup Column tampil sebagai full-height bottom sheet
20. Tutup Modal Setup Column
21. Tutup Modal Changelog
22. Pilih Currency Code `IDR` kembali pada bottom sheet agar form identik dengan record tersimpan

### Ganti akun ke Read Only

23. Ketuk menu profil lalu Logout dari akun Total Control
24. Tunggu aksi selesai (halaman Login tampil)
25. Login sebagai Read Only di aplikasi Android (`Spectra.env.GS_GSET_RO_PASSWORD`)
26. Buka Global Settings > General Settings

### TC-GS-GSET-20: Tooltip berbasis ketuk, Read Only

27. Ketuk ikon info label "Currency Code"
28. Verifikasi tooltip label tampil saat diketuk: "Currency used to display amounts across all products. Changing it does not convert existing amounts."
29. Ketuk Select "Session Idle Timeout" yang disabled
30. Verifikasi tooltip "You don't have permission to edit" tampil saat diketuk
31. Verifikasi Button "Save" Hidden

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Spec mobile Android (`coverage.mobile: automated`, tanpa `web`), mengikuti spec mobile suite Division. Nominal 31 langkah; dengan ekspansi langkah 9 sampai 11 (empat Select, tiga langkah) sekitar 40 langkah. Alasan melewati sekitar 35 langkah: satu platform dan satu kelas (tampilan mobile), langkah berulang berasal dari tabel "Select bottom sheet" tanpa langkah bersyarat, dan blok Read Only setelah Step ganti akun tetap bermakna walau blok Total Control gagal.
- Urutan TC: TC-GS-GSET-19, TC-GS-GSET-21, lalu TC-GS-GSET-20 (satu akun Total Control berurutan, kemudian Read Only setelah ganti akun, prinsip 3 butir b).
- Langkah berulang: "Untuk setiap baris tabel" di langkah 9 sampai 11; `Verifikasi` yang diulang (langkah 10) tetap satu per klausa (Expected b TC-GS-GSET-19: kelima Select membuka bottom sheet; Currency Code diasersi di langkah 5).
- Langkah penghubung (tanpa `Verifikasi`): langkah 11, 20, 21 (menutup bottom sheet atau modal), langkah 22 (mengembalikan nilai form agar tidak ada perubahan belum tersimpan saat Logout, tanpa dialog Unsaved Changes), dan langkah 23, 24, 25, 26 (ganti akun; langkah 24 mengikuti butir 8 bagian 8b).
- TC-GS-GSET-21 berdependensi TC-GS-GSET-36 (baris Changelog); baris disiapkan lewat seeding API di hook `before`, bukan dengan menjalankan TC-GS-GSET-36.
- Pecahan Expected: TC-GS-GSET-19 a menjadi langkah 1 sampai 3, b menjadi langkah 5 dan 10, c menjadi langkah 7 dan 8, d menjadi langkah 12 sampai 14; TC-GS-GSET-20 a menjadi langkah 28, b menjadi langkah 30 dan 31.
- Temuan untuk QA:
  - TC-GS-GSET-19 langkah 4 tidak menyebut cara menutup bottom sheet selector tanpa memilih opsi; spec menutupnya sebagai langkah penghubung (langkah 11) dengan gesture yang disediakan tim FE.
  - TC-GS-GSET-21 langkah 2 ("ketuk header kolom Actions lalu item `Setup Column...`") tidak menyebut Panel Column Visibility yang disebut PRD §4.1 baris #4; spec mengikuti langkah TC.
  - Label opsi `USD` tidak dikunci di PRD (NC-10); spec membaca simbol dari bottom sheet saat memilih.
  - Nama user Read Only tidak tertulis di Pre-setup TC No 3; email disediakan tim FE.
