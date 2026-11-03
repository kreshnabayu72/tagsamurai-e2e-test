---
id: TC-FA-RP-E2E-297-role-matrix-ikon-download-dan-changelog-tampil-per-peran
title: "Role Matrix: ikon Download dan Changelog tampil dan berfungsi per peran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-119
coverage:
  web: automated
---

# Role Matrix: ikon Download dan Changelog tampil dan berfungsi per peran

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Read Only (Dewi Anggraini), akun urutan 1 pada tabel Role yang diuji; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC; kolom Urutan menentukan iterasi):

| Urutan | TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| 1 | TC-FA-RP-119 | Read Only | Dewi Anggraini (Pre-setup #4) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| 2 | TC-FA-RP-119 | Total Control | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 3 | TC-FA-RP-119 | Manage global user & role (Update) | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| 4 | TC-FA-RP-119 | Manage global user & role tanpa Update | Bayu Prakoso (Pre-setup #8) | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |

- Data Pre-setup yang dibaca: pool pengguna Standard #15 (Precondition TC). Spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-119: Read Only (urutan 1)

1. Verifikasi Ikon Download dan Changelog tampil pada toolbar Tab Total Control
2. Klik ikon Changelog pada toolbar Tab Total Control
3. Verifikasi Modal `Changelog: Role & Permission > Total Control` terbuka
4. Tutup modal Changelog
5. Klik ikon Download pada toolbar Tab Total Control
6. Verifikasi Overlay Download memuat `Download as CSV` dan `Download as XLSX`
7. Tutup overlay Download dengan Esc

### TC-FA-RP-119: Total Control, Manage global user & role (Update), dan Manage global user & role tanpa Update (urutan 2 sampai 4)

8. Untuk setiap role pada tabel Role yang diuji dengan urutan 2 sampai 4 (langkah 9 sampai 17):
9. Ganti akun: logout, lalu login sebagai role pada baris tabel Role yang diuji untuk iterasi ini
10. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab Total Control
11. Verifikasi Ikon Download dan Changelog tampil pada toolbar Tab Total Control
12. Klik ikon Changelog pada toolbar Tab Total Control
13. Verifikasi Modal `Changelog: Role & Permission > Total Control` terbuka
14. Tutup modal Changelog
15. Klik ikon Download pada toolbar Tab Total Control
16. Verifikasi Overlay Download memuat `Download as CSV` dan `Download as XLSX`
17. Tutup overlay Download dengan Esc

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): membuka halaman Role & Permission setelah ganti akun (langkah 10); menutup modal Changelog (langkah 4 dan 14) dan menutup overlay Download dengan Esc (langkah 7 dan 17).
- Pembagian TC lintas spec: TC-FA-RP-120 dan TC-FA-RP-121 (Changelog dan Download terfilter cakupan group) ada di spec 034.
- Langkah berulang: langkah 9 sampai 17 dijalankan tiga kali (iterasi untuk Total Control, Manage global user & role (Update), dan Manage global user & role tanpa Update). Parameter tiap iterasi ada di tabel Role yang diuji. Dengan ekspansi spec ini sekitar 34 langkah.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Expected a menyebut ikon "tampil dan berfungsi"; spec membuktikan "berfungsi" lewat Modal Changelog yang terbuka (Expected b) dan overlay Download (Expected c), tanpa langkah tambahan.
  - Langkah Uji TC menyebut "Tutup modal lalu klik ikon Download" tanpa menyebut cara menutup overlay Download; spec menutupnya dengan Esc sebagai langkah penghubung.
  - Data Uji menyebut Read Only sebagai aktor dan tiga akun lain sebagai pengulangan; spec memakai Read Only sebagai akun login hook `before` dan mengulang tiga akun lain dengan Step ganti akun eksplisit.
