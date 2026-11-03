---
id: TC-FA-RP-E2E-034-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-1
title: "Role Matrix: Changelog dan Download terfilter ke cakupan group per peran (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-120
  - TC-FA-RP-121
coverage:
  web: automated
---

# Role Matrix: Changelog dan Download terfilter ke cakupan group per peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager pada `Company Changelog` (akun disediakan tim FE); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC; akun pada `Company Changelog` tidak tertulis di Pre-setup TC dan disediakan tim FE):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-120 | Group Manager (cakupan `IT Infrastructure`) | Group Manager | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | disediakan tim FE | `Spectra.env.FA_CHANGELOG_GM_PASSWORD` (env baru, belum terdaftar di `suite.md`; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`) |
| TC-FA-RP-121 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | disediakan tim FE | `Spectra.env.FA_CHANGELOG_MUR_GROUP_PASSWORD` (env baru, belum terdaftar di `suite.md`; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`) |

- Data Pre-setup yang dibaca: `Company Changelog` (#24) dengan log yang memuat entri Global Role, entri Tab Total Control/Read Only, entri group dalam cakupan `IT Infrastructure` beserta descendant, dan entri group di luar cakupan; pohon group #18 (Precondition d). Spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: pembaca berkas unduhan CSV (baris dan kolom), disediakan tim FE/BE.
- State global yang diubah: tidak ada. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).

## Test Steps

### TC-FA-RP-120: Group Manager

1. Klik Tab System
2. Klik ikon Changelog pada toolbar Tab System
3. Verifikasi Modal hanya memuat entri yang merujuk group dalam cakupan `IT Infrastructure` beserta descendant
4. Verifikasi Entri Global Role, entri Tab Total Control/Read Only, dan entri group di luar cakupan tidak ditampilkan
5. Klik ikon Download pada Modal Changelog
6. Klik `Download as CSV`
7. Verifikasi File Download hanya memuat baris yang sama dengan modal
8. Tutup modal Changelog

### TC-FA-RP-121: Manage user & role (Group, Update)

9. Ganti akun: logout, lalu login sebagai Manage user & role (Group, Update) pada Company Changelog (akun disediakan tim FE)
10. Klik Tab System
11. Klik ikon Changelog pada toolbar Tab System
12. Verifikasi Modal hanya memuat entri yang merujuk group dalam cakupan `IT Infrastructure` beserta descendant
13. Verifikasi Entri Global Role, entri Tab Total Control/Read Only, dan entri group di luar cakupan tidak ditampilkan
14. Klik ikon Download pada Modal Changelog
15. Klik `Download as CSV`
16. Verifikasi File Download hanya memuat baris yang sama dengan modal
17. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1 dan 10); mengunduh Changelog dari ikon Download di dalam modal (langkah 5, 14) dan menutup modal (langkah 8, 17).
- Ganti akun eksplisit (logout lalu login) pada langkah 9.
- Asersi absence pada langkah 4, 13 memakai entri dalam cakupan yang tampil pada `Verifikasi` sebelumnya sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-119 ada di spec 297; TC-FA-RP-1110, TC-FA-RP-1113, dan TC-FA-RP-1114 ada di spec 035 dan 298.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-120 dan TC-FA-RP-121 mencantumkan Pre-setup #24 (`Company Changelog`) bersama #18, tetapi #24 tidak menyebut Group Manager, Manage user & role, maupun pohon group; tenant dan akun aktor tidak jelas. Spec mengasumsikan tenant `Company Changelog` dengan akun Group Manager dan Manage user & role yang disediakan tim FE; bila #24 hanya data log pada Company Alpha, aktor menjadi Fajar Nugroho (Pre-setup #5, `FA_GM_PASSWORD`) dan Gita Maharani (Pre-setup #7, `FA_MUR_GROUP_PASSWORD`).
  - Langkah Uji TC menulis "Tutup modal lalu unduh Changelog sebagai CSV", padahal unduhan Changelog tersedia dari ikon Download di dalam Modal Changelog; spec mengunduh dari dalam modal sebelum menutupnya (nama berkas unduhan Changelog mengikuti TC-FA-RP-763).
  - Expected a menyebut "hanya memuat entri yang merujuk group dalam cakupan" tanpa jumlah entri; spec mengasersi isi modal tanpa menghitung total entri (S-12).
