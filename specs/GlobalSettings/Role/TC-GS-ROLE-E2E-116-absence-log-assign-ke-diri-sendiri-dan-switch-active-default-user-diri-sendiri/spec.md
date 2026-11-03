---
id: TC-GS-ROLE-E2E-116-absence-log-assign-ke-diri-sendiri-dan-switch-active-default-user-diri-sendiri
title: "Absence Log: Assign ke Diri Sendiri dan Switch Active Default User/Diri Sendiri Lewat Permintaan Langsung Tidak Menulis Entri Baru"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-333
  - TC-GS-ROLE-334
coverage:
  web: automated
---

# Absence Log: Assign ke Diri Sendiri dan Switch Active Default User/Diri Sendiri Lewat Permintaan Langsung Tidak Menulis Entri Baru

## Prerequisites

- Mode: FE+BE. Kelas harness: absence log (kelas g) dengan pemicu permintaan langsung ke server (kelas a, `P-5` butir a). Suite `parallel: false` karena spec berjalan di suite yang mengubah state bersama.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi Ahmad Fauzi (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada langkah permintaan hanya respons server (status dan pesan) dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): daftar user per access level dan baris role per user, sesuai `roles/access-level/list` dan `roles/capabilities/users/list` di `global-settings/role/API/openapi.yaml`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog.
- Akun aktor: Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang hanya dibaca (semua permintaan ditolak; nilai identitas mengacu fixture `Fixture.role.*` yang dibuat di tahap script, berkas belum ada): `Ahmad Fauzi` (Total Control; target diri sendiri), `Budi Santoso` (Default User, Total Control; keenam baris role Active), dan `Rina Putri` (Read Only; pembanding Tab Read Only).
- Baseline (dicatat di hook `before` sebelum permintaan pertama, S-12; kemampuan membaca total entri disediakan tim FE): total entri Changelog Tab `Total Control` sebagai `B-TC`; Changelog Tab `Read Only` sebagai `B-RO`; Changelog Detail `Manage TAG` sebagai `B-MT`; Changelog: User > Role milik `Budi Santoso` sebagai `B-BU`; access level `Ahmad Fauzi`; switch `Manage TAG` `Budi Santoso` dan `Ahmad Fauzi`; jumlah baris `Ahmad Fauzi` pada Detail `Manage TAG`.
- Pemulihan (hook `after`, cadangan bila permintaan keliru diterima): access level dan baris role `Ahmad Fauzi` serta baris `Manage TAG` `Budi Santoso` dikembalikan ke baseline; sesi dipulihkan ke akun default suite dan modal Changelog ditutup. Efek pada Pre-setup: tidak ada bila semua permintaan ditolak; entri log bersifat immutable.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada (seluruh permintaan ditolak).

## Test Steps

### TC-GS-ROLE-313: Assign Total Control ke diri sendiri lewat permintaan langsung tidak menulis entri log

1. Kirim permintaan langsung Assign Total Control untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
2. Verifikasi respons berstatus 403 Forbidden
3. Verifikasi pesan respons `You can't manage your own account from here.`
4. Buka Global Settings > Role & Permission > Tab `Total Control`, klik `Changelog`
5. Verifikasi Changelog Tab `Total Control` memuat sedikitnya satu entri
6. Verifikasi jumlah entri Changelog Tab `Total Control` sama dengan `B-TC` (tidak ada entri log baru)
7. Tutup modal Changelog

### TC-GS-ROLE-314: Assign Read Only ke diri sendiri lewat permintaan langsung tidak menulis entri log

8. Kirim permintaan langsung Assign Read Only untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
9. Verifikasi respons berstatus 403 Forbidden
10. Verifikasi pesan respons `You can't manage your own account from here.`
11. Klik `Changelog` pada Tab `Total Control`
12. Verifikasi jumlah entri Changelog Tab `Total Control` sama dengan `B-TC` (tidak ada entri log baru)
13. Tutup modal Changelog
14. Klik Tab `Read Only`, klik `Changelog`
15. Verifikasi Changelog Tab `Read Only` memuat sedikitnya satu entri
16. Verifikasi jumlah entri Changelog Tab `Read Only` sama dengan `B-RO` (tidak ada entri log baru)
17. Tutup modal Changelog

### TC-GS-ROLE-315: Assign Role ke diri sendiri lewat permintaan langsung tidak menulis entri log

18. Kirim permintaan langsung Assign Role `Manage TAG` untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
19. Verifikasi respons berstatus 403 Forbidden
20. Verifikasi pesan respons `You can't manage your own account from here.`
21. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`, klik `Changelog`
22. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
23. Verifikasi jumlah entri Changelog Detail `Manage TAG` sama dengan `B-MT` (tidak ada entri log baru)
24. Tutup modal Changelog

### TC-GS-ROLE-333: Switch Active baris role Default User lewat permintaan langsung ditolak

25. Kirim permintaan langsung matikan switch Active `Manage TAG` untuk `Budi Santoso` dengan sesi Ahmad Fauzi
26. Verifikasi respons berstatus 403 Forbidden
27. Verifikasi pesan respons `Default User cannot be modified.`
28. Verifikasi (lewat fixture BE) switch `Manage TAG` `Budi Santoso` tetap ON
29. Verifikasi (lewat fixture BE) keenam baris role `Budi Santoso` tetap Active
30. Buka Detail `Manage TAG`, klik `Changelog`
31. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
32. Verifikasi jumlah entri Changelog Detail `Manage TAG` sama dengan `B-MT` (tidak ada entri log baru)
33. Tutup modal Changelog
34. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Budi Santoso`, tekan Enter
35. Klik Name `Budi Santoso`, buka tab Changelog: User > Role
36. Verifikasi tab Changelog: User > Role tampil
37. Verifikasi jumlah entri Changelog: User > Role `Budi Santoso` sama dengan `B-BU` (tidak ada entri log baru)

### TC-GS-ROLE-334: Switch Active baris role diri sendiri lewat permintaan langsung ditolak

38. Kirim permintaan langsung matikan switch Active `Manage TAG` untuk `Ahmad Fauzi` dengan sesi Ahmad Fauzi
39. Verifikasi respons berstatus 403 Forbidden
40. Verifikasi pesan respons `You can't manage your own account from here.`
41. Verifikasi (lewat fixture BE) switch `Manage TAG` `Ahmad Fauzi` tidak berubah
42. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`, klik `Changelog`
43. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
44. Verifikasi jumlah entri Changelog Detail `Manage TAG` sama dengan `B-MT` (tidak ada entri log baru)
45. Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Spec absence (kelas g, bagian 3 prinsip 13g) dengan pemicu permintaan langsung yang ditolak sebagai kelas a (`P-5` butir a, S-05): tiap blok punya pemicu, target, dan baseline sendiri. TC milik spec ini: TC-GS-ROLE-333 dan TC-GS-ROLE-334 (seluruh Expected: penolakan, state data, lalu absence). Blok TC-GS-ROLE-313, TC-GS-ROLE-314, dan TC-GS-ROLE-315 memuat aksi nyata untuk asersi absence entri log TC itu; id ketiga TC tetap di `sourceTc` spec asalnya `TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri`, dan rujukan dicatat di `## Notes` kedua spec (S-05). Status respons dan state data ketiga TC itu diasersi di spec asal.
- K-1 (bagian 2 konvensi): TC-GS-ROLE-333 dan TC-GS-ROLE-334 adalah TC kelas a defense-in-depth dengan Expected respons API (status dan pesan respons, state data lewat fixture BE) yang tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-role-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Spec melewati sekitar 35 langkah (45 langkah) karena kelima blok satu kelas (absence entri log atas permintaan langsung yang ditolak) dan berdiri sendiri: tiap blok punya pemicu, target, dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sebagian besar langkah adalah blok baca-log berpola (buka surface, `Verifikasi` jumlah entri).
- Anchor positif absence (bagian 8b butir 2): respons 403 beserta pesan penolakan (langkah 2, 3, 9, 10, 19, 20, 26, 27, 39, 40) dan Changelog yang memuat sedikitnya satu entri (langkah 5, 15, 22, 31, 43) atau tab Changelog: User > Role yang tampil (langkah 36) membuktikan surface sudah termuat sebelum asersi jumlah. Asersi jumlah dengan baseline mengikuti S-12.
- Langkah 2 TC-313 sampai TC-315, TC-333, dan TC-334 ("Reload ... di UI") digantikan pembacaan state lewat fixture BE (bagian 8b butir 1).
- Search untuk menemukan user target ditulis sebagai langkah penghubung (R-16): langkah 34. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab, Detail, Changelog, dan tab Changelog: User > Role (langkah 4, 11, 14, 21, 30, 35, 42), serta menutup modal Changelog (langkah 7, 13, 17, 24, 33, 45).
- Temuan untuk QA:
  - TC-GS-ROLE-333 sampai TC-GS-ROLE-334 dan TC-GS-ROLE-313 sampai TC-GS-ROLE-315 (Expected "tidak ada entry log baru") tidak menyebut surface log; spec memakai Changelog Tab `Total Control` dan Tab `Read Only` (TC-313, TC-314), Changelog Detail `Manage TAG` (TC-315, TC-333, TC-334), dan Changelog: User > Role target Default User (TC-333).
  - TC-GS-ROLE-333 Expected b menyebut keenam switch Default User ON dan Disabled; "Disabled" adalah perilaku FE, bukan efek permintaan yang ditolak, sehingga tidak diasersi di spec ini (bagian 8b butir 1); spec mengasersi switch tetap ON lewat fixture BE.
  - TC-GS-ROLE-333 dan TC-GS-ROLE-334 tidak menyebut endpoint permintaan; spec menyebut operasi (matikan switch Active) sesuai TC tanpa path.
  - TC-GS-ROLE-313 sampai TC-GS-ROLE-315 bertanda PIC FE `-` (hanya PIC BE) tetapi berkelas defense-in-depth lewat UI dan sesi aktor; spec memuat blok absence-nya.
