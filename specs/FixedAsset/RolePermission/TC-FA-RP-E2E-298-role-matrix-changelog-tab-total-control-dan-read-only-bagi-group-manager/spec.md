---
id: TC-FA-RP-E2E-298-role-matrix-changelog-tab-total-control-dan-read-only-bagi-group-manager
title: "Role Matrix: Changelog Tab Total Control dan Read Only bagi Group Manager tanpa entri tingkat akses dan Global Role"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1113
coverage:
  web: automated
---

# Role Matrix: Changelog Tab Total Control dan Read Only bagi Group Manager tanpa entri tingkat akses dan Global Role

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-1113 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup yang dibaca: Changelog Tab Total Control #42 (enam entri, Field `Access Level`), pohon group #18, dan log #24. Spec tidak membuat, mengubah, atau menghapus data.
- Kemampuan teknis: pembaca berkas unduhan CSV (baris dan kolom), disediakan tim FE/BE.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-1113: Group Manager

1. Klik ikon Changelog di toolbar Tab Total Control
2. Verifikasi Modal `Changelog: Role & Permission > Total Control` terbuka
3. Verifikasi Modal tidak memuat baris entri tingkat akses (Field `Access Level`: Assign atau Remove Total Control/Read Only)
4. Verifikasi Modal tidak memuat entri Global Role
5. Klik ikon Download pada Modal Changelog
6. Klik `Download as CSV`
7. Verifikasi File Download dari modal Tab Total Control memuat baris yang sama dengan modalnya
8. Tutup modal Changelog
9. Klik Tab Read Only
10. Klik ikon Changelog di toolbar Tab Read Only
11. Verifikasi Modal `Changelog: Role & Permission > Read Only` terbuka
12. Verifikasi Modal tidak memuat baris entri tingkat akses (Field `Access Level`: Assign atau Remove Total Control/Read Only)
13. Verifikasi Modal tidak memuat entri Global Role
14. Klik ikon Download pada Modal Changelog
15. Klik `Download as CSV`
16. Verifikasi File Download dari modal Tab Read Only memuat baris yang sama dengan modalnya
17. Tutup modal Changelog

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 9); mengunduh CSV dari ikon Download di dalam modal (langkah 5, 14) dan menutup modal (langkah 8, 17).
- Anchor absence pada kedua modal: judul modal yang terbuka (`Verifikasi` sebelum asersi absence).
- Pembagian TC lintas spec: TC-FA-RP-1110 dan TC-FA-RP-1114 ada di spec 035.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Pre-setup #42 menyebut enam entri `Access Level` pada Tab Total Control; Group Manager diharapkan tidak melihat satu pun, sehingga modal bisa kosong. Spec memakai judul modal yang terbuka sebagai anchor positif (bagian 8b butir 2); judul `Changelog: Role & Permission > Read Only` mengikuti pola judul pada TC-FA-RP-119 dan tidak disebut eksplisit untuk Tab Read Only.
  - TC mencantumkan Pre-setup #24 (`Company Changelog`) bersama #42 dan #18; spec berjalan di tenant yang sama dengan akun Group Manager Pre-setup #5 dan tidak memakai akun tenant lain (lihat Temuan untuk QA spec 034).
  - Langkah Uji TC menulis "Tutup modal lalu unduh Changelog sebagai CSV", padahal unduhan Changelog tersedia dari ikon Download di dalam Modal Changelog; spec mengunduh dari dalam modal sebelum menutupnya (nama berkas unduhan Changelog mengikuti TC-FA-RP-763).
  - Expected a menyebut entri Global Role dan Access Level tidak ada, tetapi tidak menyebut entri apa yang harus tampil; asersi hanya absence dengan judul modal sebagai anchor.
