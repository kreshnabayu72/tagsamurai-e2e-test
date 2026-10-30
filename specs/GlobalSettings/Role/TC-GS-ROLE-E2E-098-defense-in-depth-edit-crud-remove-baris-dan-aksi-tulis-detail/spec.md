---
id: TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail
title: "Defense-in-Depth: Edit CRUD, Remove Baris Role, dan Aksi Tulis Detail Lewat Permintaan Langsung Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-247
  - TC-GS-ROLE-248
  - TC-GS-ROLE-249
  - TC-GS-ROLE-250
  - TC-GS-ROLE-251
  - TC-GS-ROLE-252
  - TC-GS-ROLE-257
coverage:
  web: automated
---

# Defense-in-Depth: Edit CRUD, Remove Baris Role, dan Aksi Tulis Detail Lewat Permintaan Langsung Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (request langsung ke server, bypass UI), kelas a. Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi hanya respons server (status dan pesan) dan state data; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per capability pada Detail dan daftar user per access level, sesuai `roles/capabilities/users/list` dan `roles/access-level/list` di `global-settings/role/API/openapi.yaml`. Kata "tidak berubah" membandingkan dengan baseline yang dibaca di hook `before`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog Detail "Manage TAG".
- Akun (tabel Pre-setup):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-247, TC-248, TC-250 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-249, TC-251, TC-252 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Role yang diuji pada TC-257 (langkah identik, hanya akun berbeda):

| Role | Nama user | Email | Env var password |
|---|---|---|---|
| Read Only | Siti Nurhaliza (sebelum upgrade) | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` |
| Manage user and role Read saja | Fajar Nugroho | `manageUserAndRoleRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_READ_PASSWORD` (env baru) |

- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` dan `GS_ROLE_MANAGE_READ_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE).
- Data Pre-setup sebagai target permintaan (TC-247 sampai TC-252): Ahmad Fauzi, Budi Santoso (Default User, Total Control), Hendra Wijaya (punya baris Manage user and role), dan Rina Putri (Read Only, punya baris Manage TAG). Identitas ini adalah objek guard (diri sendiri, Default User, target Total Control atau Read Only) sehingga tidak dapat diganti data seed. Permintaan ditolak server dan data hanya dibaca; hook `after` memulihkan nilai Pre-setup ke baseline sebagai cadangan bila permintaan keliru diterima.
- Data seed milik spec untuk TC-257 (Dinamis, dibuat lewat API di hook `before`, dihapus di hook `after`): `Target Edit {runId}-098` (Active, Access Global Settings dicentang, baris Manage TAG: Read checked, Update unchecked, tanpa access level) dan `Kandidat Assign {runId}-098` (Active, Access Global Settings dicentang, tanpa access level dan tanpa baris role). Nilai field wajib lain user seed disediakan tim FE.
- Baseline (dicatat di hook `before` sesudah seeding, sebelum permintaan pertama): jumlah entri Changelog Detail "Manage TAG", access level dan nilai Update baris Ahmad Fauzi dan Budi Santoso pada Manage TAG, baris Budi Santoso, baris Manage user and role milik Hendra Wijaya, baris Manage TAG milik Rina Putri beserta access level Rina Putri, dan baris `Target Edit {runId}-098` serta `Kandidat Assign {runId}-098`.
- Hook `after`: hapus kedua user seed, pulihkan sesi ke akun default suite, tutup modal Changelog.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada (seluruh permintaan ditolak).

## Test Steps

### TC-GS-ROLE-247: Edit CRUD diri sendiri lewat permintaan langsung ditolak

1. Kirim permintaan langsung Edit CRUD Manage TAG Update untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
2. Verifikasi respons berstatus 403 Forbidden
3. Verifikasi pesan respons `You can't manage your own account from here.`
4. Verifikasi (lewat fixture BE) nilai Update baris `Ahmad Fauzi` pada Detail "Manage TAG" sama dengan baseline
5. Buka Detail "Manage TAG"
6. Klik `Changelog`
7. Verifikasi jumlah entri Changelog Detail "Manage TAG" sama dengan baseline (tidak ada entri log baru)
8. Tutup modal Changelog

### TC-GS-ROLE-248: Edit CRUD Default User lewat permintaan langsung ditolak

9. Kirim permintaan langsung Edit CRUD Manage TAG Update untuk `Budi Santoso` dengan sesi Ahmad Fauzi
10. Verifikasi respons berstatus 403 Forbidden
11. Verifikasi pesan respons `Default User cannot be modified.`
12. Verifikasi (lewat fixture BE) `Budi Santoso` tetap berada di daftar Total Control
13. Verifikasi (lewat fixture BE) nilai Update baris `Budi Santoso` pada Detail "Manage TAG" sama dengan baseline (tidak ada auto-revert)

### TC-GS-ROLE-250: Remove baris role Default User lewat permintaan langsung ditolak

14. Kirim permintaan langsung Remove baris Manage TAG milik `Budi Santoso` dengan sesi Ahmad Fauzi
15. Verifikasi respons berstatus 403 Forbidden
16. Verifikasi pesan respons `Default User cannot be modified.`
17. Verifikasi (lewat fixture BE) baris `Budi Santoso` tetap ada di Detail "Manage TAG"

### TC-GS-ROLE-249: Edit CRUD target Total Control oleh Manage user and role lewat permintaan langsung ditolak

18. Ganti sesi klien HTTP ke Hendra Wijaya (login `Hendra Wijaya`)
19. Kirim permintaan langsung Edit CRUD Manage TAG Update untuk `Ahmad Fauzi` (Total Control) dengan sesi Hendra Wijaya
20. Verifikasi respons berstatus 403 Forbidden
21. Verifikasi pesan respons `You don't have permission to edit.`
22. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tetap berada di daftar Total Control

### TC-GS-ROLE-251: Remove baris role diri sendiri lewat permintaan langsung ditolak

23. Kirim permintaan langsung Remove baris Manage user and role milik `Hendra Wijaya` dengan sesi Hendra Wijaya
24. Verifikasi respons berstatus 403 Forbidden
25. Verifikasi pesan respons `You can't manage your own account from here.`
26. Verifikasi (lewat fixture BE) baris Manage user and role milik `Hendra Wijaya` tetap ada

### TC-GS-ROLE-252: Remove baris role target Read Only oleh Manage user and role lewat permintaan langsung ditolak

27. Kirim permintaan langsung Remove baris Manage TAG milik `Rina Putri` (Read Only) dengan sesi Hendra Wijaya
28. Verifikasi respons berstatus 403 Forbidden
29. Verifikasi pesan respons `You don't have permission to edit.`
30. Verifikasi (lewat fixture BE) baris Manage TAG milik `Rina Putri` tetap ada
31. Verifikasi (lewat fixture BE) `Rina Putri` tetap berada di daftar Read Only

### TC-GS-ROLE-257: Aksi tulis Detail oleh Read Only lewat permintaan langsung ditolak

Untuk setiap baris tabel "Role yang diuji" pada TC-257 (langkah 32 sampai 44):

32. Ganti sesi klien HTTP ke role pada tabel (login dengan akun dan env var baris tabel)
33. Kirim permintaan langsung Edit CRUD Manage TAG Update untuk `Target Edit {runId}-098`
34. Verifikasi respons berstatus 403 Forbidden
35. Verifikasi pesan respons `You don't have permission to do this.`
36. Kirim permintaan langsung Assign Role Manage TAG untuk `Kandidat Assign {runId}-098`
37. Verifikasi respons berstatus 403 Forbidden
38. Verifikasi pesan respons `You don't have permission to do this.`
39. Kirim permintaan langsung Remove baris Manage TAG milik `Target Edit {runId}-098`
40. Verifikasi respons berstatus 403 Forbidden
41. Verifikasi pesan respons `You don't have permission to do this.`
42. Verifikasi (lewat fixture BE) baris `Target Edit {runId}-098` tetap ada di Detail "Manage TAG" dengan Update unchecked
43. Verifikasi (lewat fixture BE) `Kandidat Assign {runId}-098` tidak punya baris di Detail "Manage TAG"
44. Verifikasi (lewat fixture BE) data baris lain di Detail "Manage TAG" sama dengan baseline

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: defense-in-depth (a), prinsip 13a bagian 3 konvensi; ketujuh TC memakai pola yang sama (permintaan langsung, asersi 403 dan state data). TC defense-in-depth lain ada di spec `TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri` dan `TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403`.
- Spec melewati sekitar 35 langkah (57 langkah dengan langkah 32 sampai 44 dikali dua role) karena ketujuh blok satu kelas harness dan berdiri sendiri: tiap blok punya permintaan, target, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah 32 sampai 44 diulang untuk Siti Nurhaliza dan Fajar Nugroho; parameter ada di tabel "Role yang diuji".
- Urutan TC sumber diubah dari 247, 248, 249, 250, 251, 252, 257 menjadi 247, 248, 250, 249, 251, 252, 257 supaya ganti sesi klien HTTP terjadi paling sedikit (blok Ahmad Fauzi, blok Hendra Wijaya, lalu blok Read Only dan Manage user and role Read).
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti sesi klien HTTP (langkah 18 dan 32), membuka Detail "Manage TAG" dan Changelog (langkah 5 dan 6), serta menutup modal Changelog (langkah 8). Langkah 2 TC ("Reload halaman terkait di UI") digantikan pembacaan state lewat fixture BE (bagian 8b butir 1).
- Asersi "tidak ada entri log baru" (TC-247 Expected c) dibandingkan dengan baseline jumlah entri (S-12) di Changelog Detail "Manage TAG". Spec absence yang memuat aksi nyata untuk TC ini tidak ada, sehingga asersi ditulis di spec ini sesuai S-05. P-1: pemicu (permintaan ditolak) dan surface Changelog berada di spec yang sama dan tidak butuh state berat tambahan.
- Baris `Target Edit {runId}-098` dan `Kandidat Assign {runId}-098` dipakai sebagai target TC-257 karena TC tidak menyebut target; keduanya data milik spec (S-06) dan tidak diubah karena permintaan ditolak.
- Temuan untuk QA:
  - TC-247 Expected c ("Tidak ada entry log baru") tidak menyebut surface log; spec memakai Changelog Detail "Manage TAG".
  - TC-257 tidak menyebut target Edit CRUD, Assign Role, dan Remove baris; spec memakai user seed milik spec.
  - TC-257 Precondition menulis dua aktor (Siti Nurhaliza atau Fajar Nugroho) dengan tanda "/"; spec menjalankan keduanya sebagai Role Matrix.
  - TC-247, TC-248, TC-249, TC-250, TC-251, TC-252, dan TC-257 tidak menyebut endpoint permintaan; spec menyebut operasi (Edit CRUD, Remove baris, Assign Role) sesuai TC tanpa path.
  - TC-248 Expected b dan TC-250 Expected b menyebut "tidak ada auto-revert" dan "baris tetap ada" tanpa metode pembacaan; spec memakai fixture BE.
  - Pre-setup #5 menyebut Hendra Wijaya punya baris Manage TAG tetapi TC-251 memakai baris Manage user and role; keduanya diasumsikan ada.
