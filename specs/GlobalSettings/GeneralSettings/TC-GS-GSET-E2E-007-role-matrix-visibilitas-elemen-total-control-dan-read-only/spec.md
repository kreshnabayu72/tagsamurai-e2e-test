---
id: TC-GS-GSET-E2E-007-role-matrix-visibilitas-elemen-total-control-dan-read-only
title: "Role Matrix visibilitas (TC lalu RO)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-22
  - TC-GS-GSET-23
  - TC-GS-GSET-61
coverage:
  web: automated
---

# Role Matrix visibilitas (TC lalu RO)

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor pertama, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen untuk kedua akun spec ini, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Role yang diuji (Tabel Data Uji Pre-setup; langkah berbeda per role, ditulis per blok):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-GSET-22 | Total Control | Budi Santoso | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-GSET-23, TC-GS-GSET-61 | Read Only | tidak tertulis di Pre-setup TC (disediakan tim FE) | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_GSET_RO_PASSWORD` |

- Login Total Control di hook `before`; ganti akun ke Read Only lewat langkah eksplisit (langkah 7 sampai 9); hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tabel "Select form" (parameter langkah berulang):

| Select | Nilai tersimpan (Pre-setup No 10) |
|---|---|
| Currency Code | `IDR` |
| Date Format | `dd/MM/yy` |
| Time Format | `HH:mm` |
| Time Zone | `Asia/Jakarta` |
| Session Idle Timeout | `30 minutes` |

- Data Pre-setup No 10 (record Client A). Seeding Changelog (Data Uji Dinamis No 1 sampai 3, dipakai sebagai precondition TC-GS-GSET-61 dan hanya diasersi sebagai keberadaan sedikitnya satu baris (langkah 22)): hook `before` men-seed lewat PUT API di `API/openapi.yaml` (sesi Total Control) satu perubahan Session Idle Timeout `30 minutes` ke `1 hour` lalu kembali ke `30 minutes`, sehingga Modal Changelog berisi sedikitnya satu baris. Record dipulihkan ke baseline oleh hook suite.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Spec tidak menekan `[Save]` lewat UI dan tidak mengubah state global.

## Test Steps

### TC-GS-GSET-22: Total Control

1. Verifikasi menu General Settings tampil (Show) di sidebar Global Settings
2. Untuk setiap baris tabel "Select form" (langkah 2 saja): Verifikasi Select pada baris tersebut tampil dan enabled
3. Verifikasi Button "Save" tampil
4. Verifikasi Button "Save" disabled sampai ada perubahan
5. Verifikasi icon Changelog tampil
6. Verifikasi ikon info label (Currency Code, Time Zone, Session Idle Timeout) tampil

### Ganti akun ke Read Only

7. Klik menu profil lalu Logout dari akun Total Control
8. Tunggu aksi selesai (halaman Login tampil)
9. Login sebagai Read Only (`Spectra.env.GS_GSET_RO_PASSWORD`)

### TC-GS-GSET-23 dan TC-GS-GSET-61: Read Only

10. Verifikasi menu General Settings tampil (Show) di sidebar Global Settings
11. Buka General Settings
12. Untuk setiap baris tabel "Select form" (langkah 12 sampai 15): Hover Select pada baris tersebut
13. Verifikasi tooltip "You don't have permission to edit"
14. Verifikasi Select pada baris tersebut tampil dan disabled
15. Verifikasi Select pada baris tersebut menampilkan nilai tersimpan terbaca penuh sesuai tabel
16. Verifikasi Button "Save" Hidden (tidak dirender)
17. Klik icon Changelog
18. Verifikasi Modal Changelog: General Settings terbuka
19. Verifikasi Toolbar Search, Filter, dan Download tampil
20. Verifikasi Search, Filter, dan Download masing-masing enabled
21. Verifikasi tabel menampilkan enam kolom data: Date, Action, Field, Old Value, New Value, Modified By
22. Verifikasi tabel menampilkan sedikitnya satu baris riwayat
23. Verifikasi Pagination tampil
24. Tutup Modal Changelog dengan `✕`
25. Hover ikon info label Currency Code
26. Verifikasi tooltip ikon info label tampil

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Spec Role Matrix visibilitas (bagian 3a konvensi; `caseType` mengikuti alur utama positif). Nominal 26 langkah; dengan ekspansi langkah berulang (langkah 2 dikali 5 Select; langkah 12 sampai 15 dikali 5 Select) sekitar 46 langkah. Alasan melewati sekitar 35 langkah: satu kelas (Role Matrix visibilitas satu halaman), langkah berulang berasal dari tabel "Select form" tanpa langkah bersyarat, dan blok Read Only setelah Step ganti akun tetap bermakna walau blok Total Control gagal (prinsip 13 batas ukuran butir b).
- Langkah berulang: "Untuk setiap baris tabel" di langkah 2 (satu langkah, lima iterasi) dan langkah 12 sampai 15 (empat langkah, lima iterasi); tiap `Verifikasi` yang diulang tetap satu per klausa (S-01).
- Langkah penghubung (tanpa `Verifikasi`): langkah 7, 8, 9 (ganti akun), langkah 24 (menutup modal), langkah 25 (hover pemicu tooltip; tooltip diasersi segera di langkah 26).
- TC-GS-GSET-23 langkah 4 (Klik icon Changelog) dan TC-GS-GSET-61 langkah 1 (Klik icon Changelog) adalah aksi yang sama pada role yang sama sehingga dipenuhi satu pembukaan modal (langkah 17). Expected e TC-GS-GSET-23 menjadi langkah 18, 21, dan 22; Expected TC-GS-GSET-61 menjadi langkah 18 sampai 23. TC-GS-GSET-23 langkah 5 dijalankan di langkah 25 setelah modal ditutup.
- Langkah 11 (Buka General Settings) adalah langkah TC-GS-GSET-23 karena sesi Read Only baru login dan belum membuka halaman.
- Asersi absence langkah 16 (Save Hidden) didahului asersi tampil atas elemen halaman lain (langkah 12 sampai 15).
- Temuan untuk QA:
  - Nama user Read Only tidak tertulis di Pre-setup TC No 3; email disediakan tim FE.
  - TC-GS-GSET-23 Expected f ("Tooltip ikon info label tetap tampil") tidak menyebut teks tooltip; spec mengasersi tooltip tampil tanpa teks (teks Currency Code ada di TC-GS-GSET-06).
  - TC-GS-GSET-61 tidak menyebut jumlah baris atau nilai yang diharapkan; spec mengasersi "sedikitnya satu baris" dari seeding precondition.
