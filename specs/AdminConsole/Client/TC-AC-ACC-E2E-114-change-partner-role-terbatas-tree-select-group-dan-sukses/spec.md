---
id: TC-AC-ACC-E2E-114-change-partner-role-terbatas-tree-select-group-dan-sukses
title: "Change Partner oleh Pemegang Update Manage Active Client dan Group Manager: Tree Select Group dan Add Partner Sukses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-590
  - TC-AC-ACC-594
  - TC-AC-ACC-591
coverage:
  web: automated
---

# Change Partner oleh Pemegang Update Manage Active Client dan Group Manager: Tree Select Group dan Add Partner Sukses

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (urutan blok = urutan akun):

| Blok | Role | Akun | Env password | Assignment |
|---|---|---|---|---|
| 1 | Active-Update-Only A-06 (Manage active client: Update + Read, exact-match Area Jakarta) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` | Hanya node Area Jakarta |
| 2 | Group Manager A-03 (scope Area Jakarta + seluruh descendant) | `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_GM_PASSWORD` | Area Jakarta dan Cabang Menteng |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Ganti ke akun blok 2 lewat langkah eksplisit di tengah spec; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (Tabel A3, kelas Dikonsumsi bila TC mengubah relasi): C-ROL-8 `PT Ubah Mitra 03` (hanya dibaca), `PT Ubah Mitra 01` (dikonfirmasi lalu dipulihkan), `PT Ubah Mitra 04` (hanya dibaca); semuanya satu-satunya Partner CV Mitra Sejati. Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-ROL-8 `PT Ubah Mitra 01` di hook `before` dan `after`. Pemulihan lewat UI (Remove "CV Mitra Lestari" + [Confirm]) menjadikan relasi "CV Mitra Lestari" berstatus `transferred`; efeknya: baris Changelog `Change Partner` bertambah dan Last Updated `PT Ubah Mitra 01` berubah.
- Partner pembanding: `CV Mitra Lestari` (Active).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Update-Only

#### TC-AC-ACC-590: Remove Partner terakhir: tree Select Group untuk Group Role exact-match

1. Ketik Search `PT Ubah Mitra 03`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ubah Mitra 03` → klik `Change Partner`
3. Klik `[Remove]` pada "CV Mitra Sejati"
4. Verifikasi field `[Group]` diganti `Select Group*`
5. Verifikasi callout "This client has no partner and requires a group to be selected manually."
6. Buka tree `Select Group*`
7. Verifikasi "Area Jakarta" dapat dipilih di tree
8. Verifikasi "Regional Barat" greyed out
9. Verifikasi "Cabang Menteng" tidak muncul di tree
10. Klik node "Regional Barat"
11. Verifikasi `[Confirm]` disabled
12. Klik node "Area Jakarta"
13. Verifikasi `[Confirm]` aktif
14. Klik `[✕]` pada header dialog
15. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
16. Klik `[Leave]` pada dialog Unsaved Changes

#### TC-AC-ACC-594: Change Partner oleh pemegang Update sampai sukses

17. Ketik Search `PT Ubah Mitra 01`, tekan Enter
18. Klik `[⋯]` pada baris `PT Ubah Mitra 01` → klik `Change Partner`
19. Klik `[+ Add Partner]` lalu pilih "CV Mitra Lestari"
20. Verifikasi "CV Mitra Lestari" masuk list dengan badge `New`
21. Klik `[Confirm]`
22. Verifikasi toast sukses "Success, partner has been updated."
23. Verifikasi Managed By baris `PT Ubah Mitra 01` adalah "CV Mitra Sejati" diikuti `+1 more`
24. Klik `[⋯]` pada baris `PT Ubah Mitra 01` → klik `Change Partner`
25. Klik `[Remove]` pada "CV Mitra Lestari"
26. Klik `[Confirm]`
27. Tunggu aksi selesai (dialog Change Partner tertutup)

### Blok 2: Ganti akun ke Group Manager

28. Logout lalu login sebagai Group Manager A-03 `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` dengan `AC_CLIENT_GM_PASSWORD`

#### TC-AC-ACC-591: Remove Partner terakhir: tree Select Group untuk Group Manager

29. Ketik Search `PT Ubah Mitra 04`, tekan Enter
30. Klik `[⋯]` pada baris `PT Ubah Mitra 04` → klik `Change Partner`
31. Klik `[Remove]` pada "CV Mitra Sejati"
32. Verifikasi field `[Group]` diganti `Select Group*`
33. Verifikasi callout "This client has no partner and requires a group to be selected manually."
34. Buka tree `Select Group*`
35. Verifikasi "Area Jakarta" dan "Cabang Menteng" dapat dipilih di tree
36. Verifikasi "Regional Barat" greyed out
37. Verifikasi "Regional Timur", "Area Surabaya", dan "Cabang Bekasi" tidak muncul di tree
38. Klik node "Regional Barat"
39. Verifikasi `[Confirm]` disabled
40. Klik node "Cabang Menteng"
41. Verifikasi `[Confirm]` aktif
42. Klik `[✕]` pada header dialog
43. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil dengan tombol `[Leave]` dan `[Cancel]`
44. Klik `[Leave]` pada dialog Unsaved Changes

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas tiga TC satu topik (Change Partner oleh role terbatas); ganti akun lewat Step eksplisit sah karena bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal keras (bagian 3, pemisah beda akun butir b); tiap blok membuka dialog sendiri dari data berbeda.
- Langkah penghubung (tanpa awalan Verifikasi): `[✕]` dan `[Leave]` penutup dialog dirty (TC-AC-ACC-591 menyebutnya di Post Condition; TC-AC-ACC-590 tidak menyebutnya, lihat Temuan); pemulihan `PT Ubah Mitra 01` (Remove "CV Mitra Lestari" lalu `[Confirm]`, Post Condition TC-AC-ACC-594) "Tunggu aksi selesai" sesudah pemulihan itu (langkah 27; butir 8 bagian 8b), dan ganti akun pada Blok 2. Verifikasi dialog Unsaved Changes yang diwajibkan S-08 tidak diulang di Notes.
- Post Condition TC-AC-ACC-594 butir b (Changelog `Change Partner`, Field `Partner` tercatat satu baris) tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-590 tidak menyebut penutupan dialog yang dirty; spec menutupnya lewat `[✕]` dan `[Leave]` (S-08, S-09).
  - TC-AC-ACC-591 dan 594 menyebut "(C-ROL-8)" untuk beberapa nama berbeda; spec memakai nama bersuffix angka yang tertulis di TC (`PT Ubah Mitra 01`, `03`, `04`).
  - Pemulihan Post Condition TC-AC-ACC-594 hanya mengembalikan daftar Partner aktif; relasi "CV Mitra Lestari" tetap tercatat `transferred`, sehingga fixture butuh seed ulang bila dipakai TC lain (Kelas Dikonsumsi).
