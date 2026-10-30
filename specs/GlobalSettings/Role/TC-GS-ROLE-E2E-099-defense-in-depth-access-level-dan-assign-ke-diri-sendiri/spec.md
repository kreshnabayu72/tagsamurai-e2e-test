---
id: TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri
title: "Defense-in-Depth: Remove Access Level dan Assign ke Diri Sendiri Lewat Permintaan Langsung Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-253
  - TC-GS-ROLE-254
  - TC-GS-ROLE-255
  - TC-GS-ROLE-256
  - TC-GS-ROLE-313
  - TC-GS-ROLE-314
  - TC-GS-ROLE-315
coverage:
  web: automated
---

# Defense-in-Depth: Remove Access Level dan Assign ke Diri Sendiri Lewat Permintaan Langsung Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (request langsung ke server, bypass UI), kelas a. Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi hanya respons server (status dan pesan) dan state data; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per access level dan daftar user per capability pada Detail, sesuai `roles/access-level/list` dan `roles/capabilities/users/list` di `global-settings/role/API/openapi.yaml`. Kata "tidak berubah" membandingkan dengan baseline yang dibaca di hook `before`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog (Tab Total Control, Tab Read Only, dan Detail "Manage TAG").
- Akun (tabel Pre-setup):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-253, TC-254, TC-313, TC-314, TC-315 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-255, TC-256 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE).
- Data Pre-setup sebagai target permintaan: Ahmad Fauzi (Total Control), Budi Santoso (Default User, Total Control), Hendra Wijaya (punya baris Manage TAG), Wawan Setiawan (kandidat Pre-setup #11, tanpa access level), dan Rina Putri (Read Only). Identitas ini adalah objek guard (diri sendiri, Default User) atau kandidat yang hanya diminta di-assign; semua permintaan ditolak dan data hanya dibaca. Hook `after` memulihkan nilai Pre-setup ke baseline sebagai cadangan bila permintaan keliru diterima.
- Baseline (dicatat di hook `before` sebelum permintaan pertama): jumlah entri Changelog Tab Total Control, Changelog Tab Read Only, dan Changelog Detail "Manage TAG"; access level Ahmad Fauzi, Budi Santoso, Wawan Setiawan, dan Rina Putri; jumlah baris Ahmad Fauzi dan jumlah baris Hendra Wijaya di Detail "Manage TAG".
- Hook `after`: pulihkan sesi ke akun default suite dan tutup modal Changelog.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada (seluruh permintaan ditolak).

## Test Steps

### TC-GS-ROLE-253: Remove access level Default User lewat permintaan langsung ditolak

1. Kirim permintaan langsung Remove Total Control `Budi Santoso` dengan sesi Ahmad Fauzi
2. Verifikasi respons berstatus 403 Forbidden
3. Verifikasi pesan respons `Default User cannot be modified.`
4. Verifikasi (lewat fixture BE) `Budi Santoso` tetap berada di daftar Total Control

### TC-GS-ROLE-254: Remove access level diri sendiri lewat permintaan langsung ditolak

5. Kirim permintaan langsung Remove Total Control `Ahmad Fauzi` dengan sesi Ahmad Fauzi
6. Verifikasi respons berstatus 403 Forbidden
7. Verifikasi pesan respons `You can't manage your own account from here.`
8. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tetap berada di daftar Total Control

### TC-GS-ROLE-313: Assign Total Control ke diri sendiri lewat permintaan langsung ditolak

9. Kirim permintaan langsung Assign Total Control untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
10. Verifikasi respons berstatus 403 Forbidden
11. Verifikasi pesan respons `You can't manage your own account from here.`
12. Verifikasi (lewat fixture BE) access level `Ahmad Fauzi` tidak berubah (tetap Total Control)
13. Klik Tab `Total Control`
14. Klik `Changelog`
15. Verifikasi jumlah entri Changelog Tab Total Control sama dengan baseline (tidak ada entri log baru)
16. Tutup modal Changelog

### TC-GS-ROLE-314: Assign Read Only ke diri sendiri lewat permintaan langsung ditolak

17. Kirim permintaan langsung Assign Read Only untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
18. Verifikasi respons berstatus 403 Forbidden
19. Verifikasi pesan respons `You can't manage your own account from here.`
20. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tetap berada di daftar Total Control
21. Verifikasi (lewat fixture BE) daftar Read Only memuat `Rina Putri`
22. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tidak ada di daftar Read Only
23. Klik `Changelog` pada Tab Total Control
24. Verifikasi jumlah entri Changelog Tab Total Control sama dengan baseline (tidak ada entri log baru)
25. Tutup modal Changelog
26. Klik Tab `Read Only`
27. Klik `Changelog`
28. Verifikasi jumlah entri Changelog Tab Read Only sama dengan baseline (tidak ada entri log baru)
29. Tutup modal Changelog

### TC-GS-ROLE-315: Assign Role ke diri sendiri lewat permintaan langsung ditolak

30. Kirim permintaan langsung Assign Role Manage TAG untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
31. Verifikasi respons berstatus 403 Forbidden
32. Verifikasi pesan respons `You can't manage your own account from here.`
33. Verifikasi (lewat fixture BE) jumlah baris `Ahmad Fauzi` di Detail "Manage TAG" sama dengan baseline (tidak ada baris baru)
34. Buka Detail "Manage TAG"
35. Klik `Changelog`
36. Verifikasi jumlah entri Changelog Detail "Manage TAG" sama dengan baseline (tidak ada entri log baru)
37. Tutup modal Changelog

### TC-GS-ROLE-255: Assign Role ke diri sendiri lewat permintaan langsung ditolak (Manage user and role)

38. Ganti sesi klien HTTP ke Hendra Wijaya (login `Hendra Wijaya`)
39. Kirim permintaan langsung Assign Role Manage TAG dengan user `Hendra Wijaya` dengan sesi Hendra Wijaya
40. Verifikasi respons berstatus 403 Forbidden
41. Verifikasi pesan respons `You can't manage your own account from here.`
42. Verifikasi (lewat fixture BE) jumlah baris `Hendra Wijaya` di Detail "Manage TAG" sama dengan baseline (tidak ada baris baru)

### TC-GS-ROLE-256: Assign/Remove access level oleh Manage user and role lewat permintaan langsung ditolak

43. Kirim permintaan langsung Assign Total Control untuk `Wawan Setiawan` dengan sesi Hendra Wijaya
44. Verifikasi respons berstatus 403 Forbidden
45. Verifikasi pesan respons `You don't have permission to do this.`
46. Kirim permintaan langsung Remove Read Only `Rina Putri` dengan sesi Hendra Wijaya
47. Verifikasi respons berstatus 403 Forbidden
48. Verifikasi pesan respons `You don't have permission to do this.`
49. Verifikasi (lewat fixture BE) daftar Total Control memuat `Ahmad Fauzi`
50. Verifikasi (lewat fixture BE) `Wawan Setiawan` tidak ada di daftar Total Control
51. Verifikasi (lewat fixture BE) `Rina Putri` tetap berada di daftar Read Only

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: defense-in-depth (a), prinsip 13a bagian 3 konvensi; ketujuh TC memakai pola yang sama (permintaan langsung, asersi 403 dan state data). TC-313 sampai TC-315 berada di spec ini karena sekelas dengan TC-253 sampai TC-256. TC defense-in-depth lain ada di spec `TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail` dan `TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403`.
- Spec melewati sekitar 35 langkah (51 langkah) karena ketujuh blok satu kelas harness dan berdiri sendiri: tiap blok punya permintaan, target, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah dari 253, 254, 255, 256, 313, 314, 315 menjadi 253, 254, 313, 314, 315, 255, 256 supaya ganti sesi klien HTTP ke Hendra Wijaya terjadi sekali (blok Ahmad Fauzi lalu blok Hendra Wijaya).
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti sesi klien HTTP (langkah 38), membuka Tab, Detail, dan Changelog (langkah 13, 14, 23, 26, 27, 34, 35), serta menutup modal Changelog (langkah 16, 25, 29, 37). Langkah 2 TC (reload halaman di UI) digantikan pembacaan state lewat fixture BE (bagian 8b butir 1).
- Asersi "tidak ada entri log" (TC-313 Expected b, TC-314 Expected b, TC-315 Expected b) dibandingkan dengan baseline jumlah entri (S-12). Spec absence yang memuat aksi nyata untuk TC ini tidak ada, sehingga asersi ditulis di spec ini sesuai S-05. P-1: pemicu (permintaan ditolak) dan surface Changelog berada di spec yang sama dan tidak butuh state berat tambahan. Absence `Ahmad Fauzi` di daftar Read Only pada TC-314 memakai baris pembanding `Rina Putri` (langkah 21) dan baseline jumlah entri.
- Temuan untuk QA:
  - TC-313 sampai TC-315 Expected b menyebut "tidak ada entri log" tanpa menyebut surface; spec memakai Changelog (Tab Total Control untuk TC-313 dan TC-314, Tab Read Only untuk TC-314, Detail "Manage TAG" untuk TC-315).
  - TC-313 sampai TC-315 bertanda PIC FE `-` (hanya PIC BE) tetapi berkelas defense-in-depth lewat UI dan sesi aktor; spec memuatnya.
  - TC-315 dan TC-255 menyebut "tidak ada baris baru" tetapi Ahmad Fauzi (Total Control) dan Hendra Wijaya (Pre-setup #5 punya baris Manage TAG) bisa sudah punya baris; spec membandingkan jumlah baris dengan baseline.
  - TC-253 sampai TC-256 dan TC-313 sampai TC-315 tidak menyebut endpoint permintaan; spec menyebut operasi sesuai TC tanpa path.
