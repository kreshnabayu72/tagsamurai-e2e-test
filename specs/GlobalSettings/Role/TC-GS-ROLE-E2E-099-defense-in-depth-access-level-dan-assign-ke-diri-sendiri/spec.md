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
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per access level dan daftar user per capability pada Detail, sesuai `roles/access-level/list` dan `roles/capabilities/users/list` di `global-settings/role/API/openapi.yaml`. Kata "tidak berubah" membandingkan dengan baseline yang dibaca di hook `before`.
- Akun (tabel Pre-setup):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-253, TC-254, TC-313, TC-314, TC-315 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-255, TC-256 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE).
- Data Pre-setup sebagai target permintaan: Ahmad Fauzi (Total Control), Budi Santoso (Default User, Total Control), Hendra Wijaya (punya baris Manage TAG), Wawan Setiawan (kandidat Pre-setup #11, tanpa access level), dan Rina Putri (Read Only). Identitas ini adalah objek guard (diri sendiri, Default User) atau kandidat yang hanya diminta di-assign; semua permintaan ditolak dan data hanya dibaca. Hook `after` memulihkan nilai Pre-setup ke baseline sebagai cadangan bila permintaan keliru diterima.
- Baseline (dicatat di hook `before` sebelum permintaan pertama): access level Ahmad Fauzi, Budi Santoso, Wawan Setiawan, dan Rina Putri; jumlah baris Ahmad Fauzi dan jumlah baris Hendra Wijaya di Detail "Manage TAG".
- Hook `after`: pulihkan sesi ke akun default suite.
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

### TC-GS-ROLE-314: Assign Read Only ke diri sendiri lewat permintaan langsung ditolak

13. Kirim permintaan langsung Assign Read Only untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
14. Verifikasi respons berstatus 403 Forbidden
15. Verifikasi pesan respons `You can't manage your own account from here.`
16. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tetap berada di daftar Total Control
17. Verifikasi (lewat fixture BE) daftar Read Only memuat `Rina Putri`
18. Verifikasi (lewat fixture BE) `Ahmad Fauzi` tidak ada di daftar Read Only

### TC-GS-ROLE-315: Assign Role ke diri sendiri lewat permintaan langsung ditolak

19. Kirim permintaan langsung Assign Role Manage TAG untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
20. Verifikasi respons berstatus 403 Forbidden
21. Verifikasi pesan respons `You can't manage your own account from here.`
22. Verifikasi (lewat fixture BE) jumlah baris `Ahmad Fauzi` di Detail "Manage TAG" sama dengan baseline (tidak ada baris baru)

### TC-GS-ROLE-255: Assign Role ke diri sendiri lewat permintaan langsung ditolak (Manage user and role)

23. Ganti sesi klien HTTP ke Hendra Wijaya (login `Hendra Wijaya`)
24. Kirim permintaan langsung Assign Role Manage TAG dengan user `Hendra Wijaya` dengan sesi Hendra Wijaya
25. Verifikasi respons berstatus 403 Forbidden
26. Verifikasi pesan respons `You can't manage your own account from here.`
27. Verifikasi (lewat fixture BE) jumlah baris `Hendra Wijaya` di Detail "Manage TAG" sama dengan baseline (tidak ada baris baru)

### TC-GS-ROLE-256: Assign/Remove access level oleh Manage user and role lewat permintaan langsung ditolak

28. Kirim permintaan langsung Assign Total Control untuk `Wawan Setiawan` dengan sesi Hendra Wijaya
29. Verifikasi respons berstatus 403 Forbidden
30. Verifikasi pesan respons `You don't have permission to do this.`
31. Kirim permintaan langsung Remove Read Only `Rina Putri` dengan sesi Hendra Wijaya
32. Verifikasi respons berstatus 403 Forbidden
33. Verifikasi pesan respons `You don't have permission to do this.`
34. Verifikasi (lewat fixture BE) daftar Total Control memuat `Ahmad Fauzi`
35. Verifikasi (lewat fixture BE) `Wawan Setiawan` tidak ada di daftar Total Control
36. Verifikasi (lewat fixture BE) `Rina Putri` tetap berada di daftar Read Only

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: defense-in-depth (a), prinsip 13a bagian 3 konvensi; ketujuh TC memakai pola yang sama (permintaan langsung, asersi 403 dan state data). TC-313 sampai TC-315 berada di spec ini karena sekelas dengan TC-253 sampai TC-256. TC defense-in-depth lain ada di spec `TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail` dan `TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403`.
- Spec melewati sekitar 35 langkah (36 langkah) karena ketujuh blok satu kelas harness dan berdiri sendiri: tiap blok punya permintaan, target, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah dari 253, 254, 255, 256, 313, 314, 315 menjadi 253, 254, 313, 314, 315, 255, 256 supaya ganti sesi klien HTTP ke Hendra Wijaya terjadi sekali (blok Ahmad Fauzi lalu blok Hendra Wijaya).
- Langkah penghubung (aksi tanpa `Verifikasi`): ganti sesi klien HTTP (langkah 23). Langkah 2 TC (reload halaman di UI) digantikan pembacaan state lewat fixture BE (bagian 8b butir 1).
- Asersi "tidak ada entri log" (TC-313 Expected b, TC-314 Expected b, TC-315 Expected b) ada di spec absence `TC-GS-ROLE-E2E-116-absence-log-assign-ke-diri-sendiri-dan-switch-active-default-user-diri-sendiri` (blok TC-GS-ROLE-313, TC-GS-ROLE-314, TC-GS-ROLE-315: permintaan langsung yang sama, baseline `B-TC`, `B-RO`, `B-MT`) sesuai S-05; id ketiga TC tetap di `sourceTc` spec ini dan rujukan dicatat di `## Notes` kedua spec. Spec ini hanya mengasersi status respons, pesan, dan state data. Absence `Ahmad Fauzi` di daftar Read Only pada TC-314 memakai baris pembanding `Rina Putri` (langkah 17).
- K-1 (bagian 2 konvensi): TC kelas a defense-in-depth dengan Expected respons API (status dan pesan respons, state data lewat fixture BE) tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-role-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Alasan pemisahan dari spec defense-in-depth lain: ketujuh TC di spec ini memakai permukaan yang sama (Remove access level dan Assign ke diri sendiri atau oleh Manage user and role) dengan baseline access level dan jumlah baris sendiri. TC Edit CRUD, Remove baris role, dan aksi tulis Detail (spec 098) serta TC flag payload, Bulk Remove, dan prioritas 403 (spec 100) memakai target, Given, dan baseline yang berbeda. Digabung, ketiga spec menjadi sekitar 123 langkah (53 + 36 + 34) sehingga satu kegagalan menyembunyikan blok lain.
- Temuan untuk QA:
  - TC-313 sampai TC-315 Expected b menyebut "tidak ada entri log" tanpa menyebut surface; asersinya ada di spec 116 yang memakai Changelog Tab Total Control (TC-313, TC-314), Tab Read Only (TC-314), dan Detail `Manage TAG` (TC-315).
  - TC-313 sampai TC-315 bertanda PIC FE `-` (hanya PIC BE) tetapi berkelas defense-in-depth lewat UI dan sesi aktor; spec memuatnya.
  - TC-315 dan TC-255 menyebut "tidak ada baris baru" tetapi Ahmad Fauzi (Total Control) dan Hendra Wijaya (Pre-setup #5 punya baris Manage TAG) bisa sudah punya baris; spec membandingkan jumlah baris dengan baseline.
  - TC-253 sampai TC-256 dan TC-313 sampai TC-315 tidak menyebut endpoint permintaan; spec menyebut operasi sesuai TC tanpa path.
