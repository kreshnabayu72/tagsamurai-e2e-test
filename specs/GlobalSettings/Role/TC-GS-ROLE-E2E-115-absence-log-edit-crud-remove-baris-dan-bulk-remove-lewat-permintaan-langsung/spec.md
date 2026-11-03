---
id: TC-GS-ROLE-E2E-115-absence-log-edit-crud-remove-baris-dan-bulk-remove-lewat-permintaan-langsung
title: "Absence Log: Edit CRUD, Remove Baris, dan Bulk Remove Lewat Permintaan Langsung Tidak Menulis Entri Baru"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-340
  - TC-GS-ROLE-341
coverage:
  web: automated
---

# Absence Log: Edit CRUD, Remove Baris, dan Bulk Remove Lewat Permintaan Langsung Tidak Menulis Entri Baru

## Prerequisites

- Mode: FE+BE. Kelas harness: absence log (kelas g) dengan pemicu permintaan langsung ke server (kelas a, `P-5` butir a). Suite `parallel: false` karena spec mengubah baris role user Pre-setup bersama.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada langkah permintaan hanya respons server (status dan pesan) dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per capability pada Detail, sesuai `roles/capabilities/users/list` di `global-settings/role/API/openapi.yaml`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog Detail.
- Akun (tabel Pre-setup):

| Aktor | Blok | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-247, TC-260, TC-340 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` (terdaftar) |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-341 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Login Ahmad Fauzi di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (bernama literal sesuai TC; nilai identitas mengacu fixture `Fixture.role.*` yang dibuat di tahap script, berkas belum ada): `Ahmad Fauzi` (target TC-247, diri sendiri), `Budi Santoso` (Default User, Total Control; baris `Manage hardware` Active) dan `Nina Kartika` (kandidat Pre-setup #11, Given: di-assign baris `Manage hardware` di hook `before`) untuk TC-260, `Laras Wulandari` (Pre-setup #20: Active, baris `Manage hardware` inactive-retained dengan Create, Read, Update tersimpan) untuk TC-340, dan `Hendra Wijaya` (Given: baris `Manage files` inactive-retained) untuk TC-341.
- Given (hook `before`): `Nina Kartika`, `Laras Wulandari`, dan `Hendra Wijaya` dipastikan berada di state di atas. Mekanisme menyiapkan baris role inactive-retained disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum permintaan pertama, S-12; kemampuan membaca total entri disediakan tim FE): total entri Changelog Detail `Manage TAG` sebagai `B-247`; total entri Changelog Detail `Manage hardware` hasil Search `Nina Kartika` sebagai `B-NK` dan hasil Search `Budi Santoso` sebagai `B-BS`; total entri Changelog Detail `Manage hardware` hasil Search `Laras Wulandari` sebagai `B-LW`; total entri Changelog Detail `Manage files` hasil Search `Hendra Wijaya` sebagai `B-HW`; nilai Update baris `Ahmad Fauzi` pada `Manage TAG`; nilai baris `Manage files` milik `Hendra Wijaya`.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): baris `Manage hardware` `Nina Kartika` dihapus bila masih ada (kembali ke state kandidat); `Laras Wulandari` dikembalikan ke baris `Manage hardware` inactive-retained (Create, Read, Update); baris `Manage files` `Hendra Wijaya` dikembalikan inactive-retained; sesi dipulihkan ke akun default suite dan modal Changelog ditutup. Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-247: Edit CRUD diri sendiri lewat permintaan langsung tidak menulis entri log

1. Kirim permintaan langsung Edit CRUD `Manage TAG` Update untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
2. Verifikasi respons berstatus 403 Forbidden
3. Verifikasi pesan respons `You can't manage your own account from here.`
4. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`
5. Klik `Changelog`
6. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
7. Verifikasi jumlah entri Changelog Detail `Manage TAG` sama dengan `B-247` (tidak ada entri log baru)
8. Tutup modal Changelog

### TC-GS-ROLE-260: Bulk Remove berisi baris Default User lewat permintaan langsung hanya menulis entri Remove untuk baris yang berhasil

9. Kirim permintaan langsung Bulk Remove `Manage hardware` untuk `Budi Santoso` dan `Nina Kartika` dengan sesi Ahmad Fauzi
10. Tunggu aksi selesai
11. Buka Detail `Manage hardware`, klik `Changelog`
12. Ketik Search `Nina Kartika`, tekan Enter
13. Verifikasi total entri sama dengan `B-NK` + 1
14. Verifikasi entry baru Action `Remove` untuk `Nina Kartika`
15. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
16. Verifikasi tidak ada entri baru Action `Remove` untuk `Budi Santoso` (total entri sama dengan `B-BS`)
17. Tutup modal Changelog

### TC-GS-ROLE-340: Edit CRUD baris inactive-retained lewat permintaan langsung ditolak

18. Kirim permintaan langsung centang Delete baris `Manage hardware` milik `Laras Wulandari` dengan sesi Ahmad Fauzi
19. Verifikasi permintaan ditolak dengan pesan `Turn on this role first.`
20. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Laras Wulandari`, tekan Enter
21. Klik Name `Laras Wulandari`, buka Tab `Role`
22. Nyalakan switch `Manage hardware`
23. Verifikasi baris `Manage hardware` nilai tersimpan tidak berubah: Create, Read, dan Update tercentang
24. Verifikasi baris `Manage hardware` Delete tidak tercentang
25. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage hardware`, klik `Changelog`
26. Ketik Search `Laras Wulandari`, tekan Enter
27. Verifikasi total entri sama dengan `B-LW` + 1
28. Verifikasi entry baru Action `Assign` untuk `Laras Wulandari` (dari penyalaan switch pada langkah 22)
29. Verifikasi tidak ada entry Action `Edit` untuk `Laras Wulandari`
30. Tutup modal Changelog

### TC-GS-ROLE-341: Prioritas pesan penolakan Edit CRUD baris inactive-retained milik diri sendiri

31. Ganti sesi klien HTTP ke Hendra Wijaya (login `Hendra Wijaya`)
32. Kirim permintaan langsung centang Delete baris `Manage files` milik `Hendra Wijaya` dengan sesi Hendra Wijaya
33. Verifikasi permintaan ditolak dengan pesan `You can't manage your own account from here.`
34. Verifikasi (lewat fixture BE) nilai baris `Manage files` milik `Hendra Wijaya` tidak berubah
35. Buka Detail `Manage files`, klik `Changelog`
36. Verifikasi Changelog Detail `Manage files` memuat sedikitnya satu entri
37. Ketik Search `Hendra Wijaya`, tekan Enter
38. Verifikasi total entri sama dengan `B-HW` (tidak ada entry log baru)
39. Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Spec absence (kelas g, bagian 3 prinsip 13g) dengan pemicu permintaan langsung yang ditolak sebagai kelas a (`P-5` butir a, S-05): tiap blok punya pemicu, user, dan baseline sendiri. TC milik spec ini: TC-GS-ROLE-340 dan TC-GS-ROLE-341 (seluruh Expected: penolakan, state data, lalu absence). Blok TC-GS-ROLE-247 dan TC-GS-ROLE-260 memuat aksi nyata untuk asersi absence entri log TC itu; id kedua TC tetap di `sourceTc` spec asalnya, yaitu `TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail` (TC-GS-ROLE-247) dan `TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403` (TC-GS-ROLE-260). Rujukan dicatat di `## Notes` kedua spec asal (S-05).
- K-1 (bagian 2 konvensi): TC-GS-ROLE-340 dan TC-GS-ROLE-341 adalah TC kelas a defense-in-depth dengan Expected respons API (pesan penolakan dan state data) yang tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-role-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Spec melewati sekitar 35 langkah (39 langkah) karena keempat blok satu kelas (absence entri log atas permintaan langsung yang ditolak) dan berdiri sendiri: tiap blok punya pemicu, target, baseline, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah 4 sampai 8, 11 sampai 17, 25 sampai 30, dan 35 sampai 39 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`).
- Anchor positif absence (bagian 8b butir 2): TC-247 memakai respons 403 beserta pesan (langkah 2 dan 3) dan Changelog Detail `Manage TAG` yang memuat sedikitnya satu entri (langkah 6); TC-260 memakai entry Remove `Nina Kartika` pada Changelog yang sama (langkah 14); TC-340 memakai entry Assign dari penyalaan switch (langkah 28); TC-341 memakai Changelog Detail `Manage files` yang memuat sedikitnya satu entri (langkah 36). Asersi jumlah dengan baseline mengikuti S-12.
- Penyalaan switch `Manage hardware` `Laras Wulandari` (langkah 22) adalah langkah 2 TC-340 dan menulis entry Assign; entry itu dihitung dalam `B-LW` + 1 sehingga entry Edit akibat permintaan yang ditolak dapat dibedakan.
- Search untuk menemukan user atau entri target ditulis sebagai langkah penghubung (R-16): langkah 12, 15, 20, 26, 37. Langkah penghubung lain (aksi tanpa `Verifikasi`): ganti sesi klien HTTP (langkah 31), "Tunggu aksi selesai" (langkah 10), membuka Detail, Changelog, dan Tab `Role` (langkah 4, 5, 11, 21, 25, 35), serta menutup modal Changelog (langkah 8, 17, 30, 39).
- Temuan untuk QA:
  - TC-GS-ROLE-247, TC-GS-ROLE-340, dan TC-GS-ROLE-341 (Expected "tidak ada entry log baru") tidak menyebut surface log; spec memakai Changelog Detail role terkait dan, untuk user target, Changelog: User > Role bila TC kelak menyebutnya.
  - TC-GS-ROLE-340 dan TC-GS-ROLE-341 tidak menyebut endpoint permintaan; spec menyebut operasi (centang Delete baris) sesuai TC tanpa path.
  - Mekanisme menyiapkan baris role inactive-retained `Laras Wulandari` dan `Hendra Wijaya` (Given) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-341 Given menyebut `Hendra Wijaya` punya baris `Manage files` inactive-retained tanpa Pre-setup; Pre-setup #5 hanya menyebut baris `Manage TAG`.
  - TC-GS-ROLE-340 Post Condition tidak punya langkah observasi di luar Expected b; tidak diasersi terpisah.
