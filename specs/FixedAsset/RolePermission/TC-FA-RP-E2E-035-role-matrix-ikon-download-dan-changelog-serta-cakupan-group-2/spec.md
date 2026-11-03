---
id: TC-FA-RP-E2E-035-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-2
title: "Role Matrix: Download Tab Total Control dan Read Only terfilter ke cakupan Home Group (2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1110
  - TC-FA-RP-1114
coverage:
  web: automated
---

# Role Matrix: Download Tab Total Control dan Read Only terfilter ke cakupan Home Group (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-1110 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| TC-FA-RP-1114 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18 dan pool Home Group #17. Tiga user Total Control yang di-seed hook `before` dari pool Pre-setup #17: Gunawan Halim (Home Group `Data Center`), Hesti Rahma (Home Group `Logistics Warehouse`), dan Indra Kusuma (tanpa Home Group), ditetapkan Total Control lewat seed API; hook `after` mengembalikan ketiganya ke kondisi Pre-setup #17 (tanpa tingkat akses).
- Data milik spec: dua user Read Only yang di-seed hook `before` lewat seed API dengan nama bersuffix (S-12): `Uji Helpdesk {runId}-035` (Home Group `Helpdesk`) dan `Uji Head Office {runId}-035` (Home Group `Head Office`); hook `after` menghapus keduanya. TC tidak menyebut nama kedua user Read Only (lihat Temuan untuk QA).
- Kemampuan teknis: pembaca berkas unduhan CSV (baris dan kolom), disediakan tim FE/BE.
- State global yang diubah: tingkat akses tiga user #17 dan dua user Read Only milik spec (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-1110: Group Manager

1. Klik ikon Download pada toolbar Tab Total Control
2. Klik `Download as CSV`
3. Verifikasi File `Role-Permission-Total-Control` hanya memuat user Total Control ber-Home Group `Data Center` (Gunawan Halim)
4. Verifikasi Baris pada file sama dengan baris Tab Total Control di layar
5. Verifikasi User ber-Home Group `Logistics Warehouse` (Hesti Rahma) dan user tanpa Home Group (Indra Kusuma) tidak ada di file
6. Klik Tab Read Only
7. Klik ikon Download pada toolbar Tab Read Only
8. Klik `Download as CSV`
9. Verifikasi File `Role-Permission-Read-Only` hanya memuat user Read Only ber-Home Group `Helpdesk` (Uji Helpdesk {runId}-035)
10. Verifikasi Baris pada file sama dengan baris Tab Read Only di layar
11. Verifikasi User Read Only ber-Home Group `Head Office` (Uji Head Office {runId}-035, ancestor di luar cakupan) tidak ada di file

### TC-FA-RP-1114: Manage user & role (Group, Update)

12. Ganti akun: logout, lalu login sebagai Manage user & role (Group, Update, `IT Infrastructure`) (Gita Maharani)
13. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab Total Control
14. Klik ikon Download pada toolbar Tab Total Control
15. Klik `Download as CSV`
16. Verifikasi File `Role-Permission-Total-Control` tetap dihasilkan
17. Verifikasi File `Role-Permission-Total-Control` hanya memuat user Total Control ber-Home Group `Data Center` (Gunawan Halim)
18. Verifikasi Baris pada file sama dengan baris Tab Total Control di layar
19. Verifikasi User ber-Home Group `Logistics Warehouse` (Hesti Rahma) dan user tanpa Home Group (Indra Kusuma) tidak ada di file
20. Klik Tab Read Only
21. Klik ikon Download pada toolbar Tab Read Only
22. Klik `Download as CSV`
23. Verifikasi File `Role-Permission-Read-Only` tetap dihasilkan
24. Verifikasi File `Role-Permission-Read-Only` hanya memuat user Read Only ber-Home Group `Helpdesk` (Uji Helpdesk {runId}-035)
25. Verifikasi Baris pada file sama dengan baris Tab Read Only di layar
26. Verifikasi User Read Only ber-Home Group `Head Office` (Uji Head Office {runId}-035, ancestor di luar cakupan) tidak ada di file

## Notes

- Asersi isi berkas Download (baris yang dibandingkan dengan layar atau modal) tetap berada di spec fungsional ini dan tidak dipecah ke spec kelas f (konvensi bagian 3 butir 13f, [KEPUTUSAN 2026-11-02]).
- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 6 dan 20); membuka halaman Role & Permission setelah ganti akun (langkah 13); mengunduh CSV tab Read Only setelah pindah tab (langkah 6, 20).
- Ganti akun eksplisit (logout lalu login) pada langkah 12.
- Asersi absence pada file memakai baris user dalam cakupan yang ada di file sebagai anchor positif (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-1113 ada di spec 298; TC-FA-RP-119 sampai TC-FA-RP-121 ada di spec 297 dan 034.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Expected a TC-FA-RP-1110 dan TC-FA-RP-1114 menyebut "hanya memuat user Total Control ber-Home Group `Data Center`", tetapi Pre-setup #36 memuat sembilan user Total Control lain; spec mengasersi baris Gunawan Halim ada dan Hesti Rahma serta Indra Kusuma tidak ada, serta baris file sama dengan layar, tanpa menjamin tidak ada user #36 ber-Home Group dalam cakupan.
  - Precondition d tidak menamai tiga user Total Control maupun dua user Read Only; spec memakai Gunawan Halim, Hesti Rahma, dan Indra Kusuma (Pre-setup #17) untuk Total Control dan dua user Read Only bersuffix milik spec.
  - TC-FA-RP-1110 dan TC-FA-RP-1114 bertanda "menunggu konfirmasi BE, PRD 12 #3" pada kolom Sumber PRD; hasil asersi bergantung pada konfirmasi itu.
  - Langkah Uji TC meminta "bandingkan barisnya dengan layar" tanpa menyebut cara; spec membandingkan baris file dengan baris tab yang tampil.
