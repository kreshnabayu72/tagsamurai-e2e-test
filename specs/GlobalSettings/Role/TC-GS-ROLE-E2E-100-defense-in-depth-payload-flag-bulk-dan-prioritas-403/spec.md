---
id: TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403
title: "Defense-in-Depth: Flag Payload Diabaikan, Bulk Remove Default User, dan Prioritas Pesan 403"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-258
  - TC-GS-ROLE-259
  - TC-GS-ROLE-260
  - TC-GS-ROLE-308
coverage:
  web: automated
---

# Defense-in-Depth: Flag Payload Diabaikan, Bulk Remove Default User, dan Prioritas Pesan 403

## Prerequisites

- Mode: FE+BE. Kelas harness: defense-in-depth (request langsung ke server, bypass UI), kelas a. Suite `parallel: false`.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi hanya respons server (status dan pesan) dan state data; perilaku FE untuk respons yang sama tidak diasersi di spec ini (bagian 8b butir 1).
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per capability pada Detail dan daftar user per access level, sesuai `roles/capabilities/users/list` dan `roles/access-level/list` di `global-settings/role/API/openapi.yaml`. Kata "tidak berubah" membandingkan dengan baseline yang dibaca di hook `before`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog Detail.
- Akun (tabel Pre-setup):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-258, TC-259, TC-260 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Siti Nurhaliza (Read Only, sebelum upgrade; punya baris Manage TAG) | TC-308 sesi Read Only | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` |
| Total Control pada Client C suspended (Pre-setup #16) | TC-308 sesi Client suspended | disediakan tim FE | `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD` |

- Data Given milik hook `before` (dikembalikan di hook `after`): `Wawan Setiawan` (kandidat Pre-setup #11) di-assign baris Manage TAG lewat API dengan Read checked dan Update unchecked (TC-258 dan TC-259); `Nina Kartika` (kandidat Pre-setup #11) di-assign baris Manage hardware lewat API (TC-260). Hook `after` menghapus baris Manage TAG `Wawan Setiawan` dan baris Manage hardware `Nina Kartika` bila masih ada sehingga keduanya kembali ke state kandidat tanpa baris role dan tanpa access level.
- Data Pre-setup yang hanya dibaca: `Budi Santoso` (Default User, Total Control; punya baris Manage hardware dan Manage TAG) pada Client A, serta Default User Client C (disediakan tim FE) pada TC-308. Permintaan TC-308 ditolak sehingga data tidak berubah.
- Baseline (dicatat di hook `before` sesudah Given): jumlah entri Changelog Detail "Manage TAG" dan Changelog Detail "Manage hardware"; nilai Update baris `Budi Santoso` pada Manage TAG (Client A); baris Default User Client C pada Manage TAG; nilai Update dan Read baris `Wawan Setiawan`.
- Env baru: tidak ada (semua env var di atas terdaftar di `.env.example`).
- Hook `after`: pulihkan sesi ke akun default suite dan tutup modal Changelog.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-259: Flag kolom yang tidak berlaku diabaikan

1. Kirim permintaan langsung Edit CRUD Manage TAG milik `Wawan Setiawan` dengan Create=true dan Update=true dengan sesi Ahmad Fauzi
2. Verifikasi permintaan sukses tanpa error
3. Verifikasi (lewat fixture BE) Update baris `Wawan Setiawan` pada Detail "Manage TAG" checked
4. Buka Detail "Manage TAG"
5. Klik `Changelog`
6. Verifikasi jumlah entri Changelog Detail "Manage TAG" bertambah tepat 1 dari baseline dan entri baru berfield Update untuk `Wawan Setiawan`
7. Verifikasi tidak ada entri baru berfield Create untuk `Wawan Setiawan`
8. Tutup modal Changelog

### TC-GS-ROLE-258: Nilai Read=false pada permintaan Edit CRUD diabaikan

9. Kirim permintaan langsung Edit CRUD Manage TAG milik `Wawan Setiawan` dengan Read=false dan Update=true dengan sesi Ahmad Fauzi
10. Verifikasi permintaan sukses
11. Verifikasi (lewat fixture BE) Read baris `Wawan Setiawan` pada Detail "Manage TAG" tetap checked
12. Verifikasi (lewat fixture BE) Update baris `Wawan Setiawan` pada Detail "Manage TAG" checked

### TC-GS-ROLE-260: Bulk Remove berisi baris Default User lewat permintaan langsung

13. Kirim permintaan langsung Bulk Remove Manage hardware untuk `Budi Santoso` dan `Nina Kartika` dengan sesi Ahmad Fauzi
14. Verifikasi (lewat fixture BE) baris `Budi Santoso` tetap ada di Detail "Manage hardware"
15. Verifikasi (lewat fixture BE) baris `Nina Kartika` terhapus dari Detail "Manage hardware"
16. Buka Detail "Manage hardware"
17. Klik `Changelog`
18. Verifikasi jumlah entri Changelog Detail "Manage hardware" bertambah tepat 1 dari baseline dan entri baru adalah Remove `Nina Kartika`
19. Verifikasi tidak ada entri baru Remove untuk `Budi Santoso`
20. Tutup modal Changelog

### TC-GS-ROLE-308: Prioritas pesan 403 saat beberapa kondisi penolakan berlaku sekaligus

21. Ganti sesi klien HTTP ke Siti Nurhaliza (Read Only)
22. Kirim permintaan langsung Edit CRUD (Update=true) baris `Budi Santoso` pada Manage TAG dengan sesi Siti Nurhaliza
23. Verifikasi respons berstatus 403 Forbidden
24. Verifikasi pesan respons `You don't have permission to do this.`
25. Verifikasi pesan respons bukan `Default User cannot be modified.`
26. Verifikasi pesan respons bukan `Read Only access cannot modify data.`
27. Ganti sesi klien HTTP ke Total Control Client C suspended
28. Kirim permintaan langsung Edit CRUD baris Default User Client C pada Manage TAG dengan sesi Total Control Client C
29. Verifikasi respons berstatus 403 Forbidden
30. Verifikasi pesan respons `Changes can't be saved while this workspace is suspended or expired.`
31. Verifikasi pesan respons bukan `Default User cannot be modified.`
32. Verifikasi (lewat fixture BE) nilai Update baris `Budi Santoso` pada Detail "Manage TAG" Client A sama dengan baseline
33. Verifikasi (lewat fixture BE) baris Default User Client C pada Detail "Manage TAG" sama dengan baseline

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: defense-in-depth (a), prinsip 13a bagian 3 konvensi. TC defense-in-depth lain ada di spec `TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail` dan `TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri`. TC-GS-ROLE-261 (partial success lewat intercept) ada di spec `TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial`.
- Urutan TC sumber diubah dari 258, 259, 260, 308 menjadi 259, 258, 260, 308. Update `Wawan Setiawan` harus unchecked saat TC-259 supaya Changelog mencatat tepat satu entri Field Update; TC-258 sesudahnya mengirim Update=true pada nilai yang sudah checked dan tetap menguji Read=false diabaikan. Baseline Changelog dari hook `before` dipakai langsung oleh TC-259. Blok TC-308 terakhir karena memakai dua ganti sesi klien HTTP.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail dan Changelog (langkah 4, 5, 16, 17), menutup modal Changelog (langkah 8 dan 20), dan ganti sesi klien HTTP (langkah 21 dan 27).
- Absence entri baru berfield Create (langkah 7) dan entri Remove `Budi Santoso` (langkah 19) didahului `Verifikasi` entri baru yang seharusnya ada pada Changelog yang sama (langkah 6 dan 18; bagian 8b butir 2).
- TC-259 Expected b klausa kedua ("tidak ada kolom Create di Detail Manage TAG") adalah tampilan FE dan tidak diasersi di spec request langsung (bagian 8b butir 1). Kolom Detail yang tampil mengikuti capability role dibahas di spec `TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role`; klausa ini dicatat di "Temuan untuk QA".
- TC-308 Expected b menyebut "toast"; yang diasersi adalah pesan respons server yang sama (bagian 8b butir 1).
- Temuan untuk QA:
  - TC-259 Expected b klausa kedua ("tidak ada kolom Create di Detail Manage TAG") adalah tampilan FE pada request langsung dan tidak diasersi di spec ini.
  - TC-258 dan TC-259 memakai `Wawan Setiawan` dengan baris Manage TAG tanpa Given; spec menyiapkannya di hook `before` (Pre-setup #11 menyatakan Wawan tanpa baris role).
  - TC-260 memakai `Nina Kartika` dengan baris Manage hardware tanpa Given; spec menyiapkannya di hook `before`.
  - TC-260 Expected b menyebut "dihitung gagal" tanpa Expected respons; spec tidak mengasersi respons bulk (status atau ringkasan).
  - TC-308 tidak menyebut baris Default User Client C dan akun Client C; disediakan tim FE.
  - TC-308 Expected a dan b menyebut tiga pesan penolakan berbeda dalam satu butir; spec memecahnya per klausa.
