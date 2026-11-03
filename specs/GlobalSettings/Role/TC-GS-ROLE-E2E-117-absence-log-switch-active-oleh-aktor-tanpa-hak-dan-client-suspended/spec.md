---
id: TC-GS-ROLE-E2E-117-absence-log-switch-active-oleh-aktor-tanpa-hak-dan-client-suspended
title: "Absence Log: Switch Active Target Total Control oleh Manage user and role, oleh Read Only, dan pada Client Suspended Tidak Menulis Entri Baru"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-335
  - TC-GS-ROLE-336
  - TC-GS-ROLE-337
coverage:
  web: automated
---

# Absence Log: Switch Active Target Total Control oleh Manage user and role, oleh Read Only, dan pada Client Suspended Tidak Menulis Entri Baru

## Prerequisites

- Mode: FE+BE. Kelas harness: absence log (kelas g) dengan pemicu permintaan langsung ke server (kelas a, dan kelas h pada TC-337 sebagai pemicu; `P-5` butir a). Suite `parallel: false` karena spec berganti akun dan memakai user Pre-setup bersama.
- Klien HTTP: klien HTTP yang mengirim permintaan langsung ke server dengan sesi aktor tiap blok (token sesi aktor; cara memperolehnya disediakan tim FE). Asersi pada langkah permintaan hanya respons server (status dan pesan) dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Kemampuan membaca state data lewat fixture BE (disediakan tim FE): baris role dan access level per user, sesuai `roles/capabilities/users/list` dan `roles/access-level/list` di `global-settings/role/API/openapi.yaml`. Changelog tidak punya endpoint di openapi sehingga dibaca lewat UI modal Changelog.
- Akun (tabel Pre-setup):

| Aktor | Blok | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, pembaca log, akun hook `before`) | TC-335, TC-336 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` (terdaftar) |
| Hendra Wijaya (Manage user and role C/R/U/D, sesi klien HTTP) | TC-335 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |
| Siti Nurhaliza (Read Only, sesi klien HTTP) | TC-336 | disediakan tim FE | `Spectra.env.GS_RO_PASSWORD` (terdaftar) |
| Total Control pada Client C suspended (Pre-setup #16, sesi klien HTTP dan pembaca log) | TC-337 | disediakan tim FE | `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD` (terdaftar) |

- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Login Ahmad Fauzi di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; nilai identitas mengacu fixture `Fixture.role.*` yang dibuat di tahap script, berkas belum ada): `Cakra Mahendra` (Active; Total Control dengan keenam baris Active, Given: di-assign Total Control ulang di hook `before`) untuk TC-335 dan `Hanif Pradipta` (Active; baris `Manage TAG` Active dengan Read dan Update tercentang) untuk TC-336. TC-337 memakai salah satu user Client C suspended yang tidak disebut TC (disediakan tim FE; lihat Temuan untuk QA) dan switch `Manage files` pada user itu.
- Given (hook `before`): `Cakra Mahendra` dan `Hanif Pradipta` dipastikan berada di state di atas. Mekanisme menyiapkan access level dan baris role per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sesudah Given dan sebelum permintaan pertama, S-12; kemampuan membaca total entri disediakan tim FE): total entri Changelog Tab `Total Control` hasil Search `Cakra Mahendra` sebagai `B-TCC`; Changelog Detail `Manage TAG` hasil Search `Cakra Mahendra` sebagai `B-DMC` dan hasil Search `Hanif Pradipta` sebagai `B-DMH`; Changelog: User > Role `Hanif Pradipta` sebagai `B-URH`; Changelog Detail `Manage files` Client C suspended sebagai `B-CS` (dibaca dengan akun Total Control Client C suspended; kemampuan baca bagi akun suspended disediakan tim FE).
- Pemulihan (hook `after`, cadangan bila permintaan keliru diterima): `Cakra Mahendra` dan `Hanif Pradipta` dikembalikan ke state Given dan data user Client C suspended ke baseline; sesi dipulihkan ke akun default suite dan modal Changelog ditutup. Efek pada Pre-setup: tidak ada bila semua permintaan ditolak; entri log bersifat immutable.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada (seluruh permintaan ditolak).

## Test Steps

### TC-GS-ROLE-335: Switch Active target Total Control oleh Manage user and role lewat permintaan langsung ditolak

1. Ganti sesi klien HTTP ke Hendra Wijaya (login `Hendra Wijaya`)
2. Kirim permintaan langsung matikan switch Active `Manage TAG` untuk `Cakra Mahendra` dengan sesi Hendra Wijaya
3. Verifikasi respons berstatus 403 Forbidden
4. Verifikasi pesan respons `You don't have permission to edit.`
5. Verifikasi (lewat fixture BE) `Cakra Mahendra` tetap Total Control
6. Verifikasi (lewat fixture BE) keenam switch `Cakra Mahendra` ON
7. Buka Global Settings > Role & Permission > Tab `Total Control`, klik `Changelog`
8. Verifikasi Changelog Tab `Total Control` memuat sedikitnya satu entri
9. Ketik Search `Cakra Mahendra`, tekan Enter
10. Verifikasi total entri sama dengan `B-TCC` (tidak ada entry log baru)
11. Tutup modal Changelog
12. Buka Tab System, buka Detail `Manage TAG`, klik `Changelog`
13. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
14. Ketik Search `Cakra Mahendra`, tekan Enter
15. Verifikasi total entri sama dengan `B-DMC` (tidak ada entry log baru)
16. Tutup modal Changelog

### TC-GS-ROLE-336: Switch Active oleh Read Only lewat permintaan langsung ditolak

17. Ganti sesi klien HTTP ke Siti Nurhaliza (login `Siti Nurhaliza`)
18. Kirim permintaan langsung matikan switch Active `Manage TAG` untuk `Hanif Pradipta` dengan sesi Siti Nurhaliza
19. Verifikasi respons berstatus 403 Forbidden
20. Verifikasi pesan respons `You don't have permission to do this.`
21. Verifikasi (lewat fixture BE) switch `Manage TAG` `Hanif Pradipta` tidak berubah
22. Buka Detail `Manage TAG`, klik `Changelog`
23. Verifikasi Changelog Detail `Manage TAG` memuat sedikitnya satu entri
24. Ketik Search `Hanif Pradipta`, tekan Enter
25. Verifikasi total entri sama dengan `B-DMH` (tidak ada entry log baru)
26. Tutup modal Changelog
27. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
28. Klik Name `Hanif Pradipta`, buka tab Changelog: User > Role
29. Verifikasi tab Changelog: User > Role tampil
30. Verifikasi jumlah entri Changelog: User > Role `Hanif Pradipta` sama dengan `B-URH` (tidak ada entry log baru)

### TC-GS-ROLE-337: Switch Active saat client suspended ditolak

31. Ganti akun: Logout dari akun Ahmad Fauzi, login sebagai Total Control Client C suspended (Pre-setup #16)
32. Kirim permintaan langsung nyalakan switch Active `Manage files` untuk salah satu user Client C suspended dengan sesi Total Control Client C suspended
33. Verifikasi respons berstatus 403 Forbidden
34. Verifikasi respons membedakan alasan suspended dari 403 permission
35. Verifikasi (lewat fixture BE) data switch `Manage files` user itu tidak berubah
36. Buka Detail `Manage files`, klik `Changelog`
37. Verifikasi Changelog Detail `Manage files` Client C suspended memuat sedikitnya satu entri
38. Verifikasi jumlah entri Changelog Detail `Manage files` sama dengan `B-CS` (tidak ada entry log baru)
39. Tutup modal Changelog

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Spec absence (kelas g, bagian 3 prinsip 13g) dengan pemicu permintaan langsung yang ditolak sebagai kelas a, dan kondisi client suspended sebagai pemicu kelas h pada TC-GS-ROLE-337 (`P-5` butir a, S-05): tiap blok punya pemicu, user, dan baseline sendiri. Seluruh Expected ketiga TC (penolakan, state data, lalu absence) berada di spec ini karena tiap TC tepat satu spec.
- K-1 (bagian 2 konvensi): TC-GS-ROLE-335, TC-GS-ROLE-336, dan TC-GS-ROLE-337 adalah TC kelas a defense-in-depth dengan Expected respons API (status dan pesan respons, state data lewat fixture BE) yang tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-role-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Spec melewati sekitar 35 langkah (39 langkah) karena ketiga blok satu kelas harness (absence log atas permintaan langsung yang ditolak) dan berdiri sendiri: tiap blok punya aktor, user, dan baseline sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`).
- Anchor positif absence (bagian 8b butir 2): respons 403 beserta pesan penolakan (langkah 3, 4, 19, 20, 33, 34) dan Changelog yang memuat sedikitnya satu entri (langkah 8, 13, 23, 37) atau tab Changelog: User > Role yang tampil (langkah 29) membuktikan surface sudah termuat sebelum asersi jumlah. Asersi jumlah dengan baseline mengikuti S-12.
- Langkah 2 TC-335 dan TC-336 ("Reload User > ... Tab Role sbg Ahmad Fauzi") digantikan pembacaan state lewat fixture BE (bagian 8b butir 1).
- Search untuk menemukan user atau entri target ditulis sebagai langkah penghubung (R-16): langkah 9, 14, 24, 27. Langkah penghubung lain (aksi tanpa `Verifikasi`): ganti sesi klien HTTP dan ganti akun (langkah 1, 17, 31), membuka Tab, Detail, dan Changelog (langkah 7, 12, 22, 28, 36), serta menutup modal Changelog (langkah 11, 16, 26, 39).
- Temuan untuk QA:
  - TC-GS-ROLE-335 sampai TC-GS-ROLE-337 (Expected "tidak ada entry log baru") tidak menyebut surface log; spec memakai Changelog Tab `Total Control` dan Detail `Manage TAG` (TC-335), Changelog Detail `Manage TAG` dan Changelog: User > Role target (TC-336), dan Changelog Detail `Manage files` (TC-337).
  - TC-GS-ROLE-337 tidak menyebut user target, surface log, maupun cara akun client suspended membaca log; spec memakai salah satu user Client C suspended dan akun Total Control Client C suspended sebagai pembaca log (kemampuan baca bagi akun suspended disediakan tim FE).
  - TC-GS-ROLE-337 Expected a menyebut respons yang membedakan alasan suspended dari 403 permission (`entity-isolation.md` §18.8) tanpa menyebut pesan atau kode; spec mengasersinya apa adanya tanpa mengarang nilai.
  - Email dan kredensial akun Total Control Client C suspended dan Siti Nurhaliza tidak ada di Tabel Pre-setup TC; ditulis "disediakan tim FE".
  - TC-GS-ROLE-335 Given menyebut Cakra Mahendra di-assign Total Control ulang "bila TC-GS-ROLE-326 sudah dijalankan"; spec menulis Given sendiri di hook `before` dan tidak bergantung urutan spec.
  - TC-GS-ROLE-335 dan TC-GS-ROLE-336 memakai pesan berbeda ("You don't have permission to edit." dan "You don't have permission to do this.") untuk penolakan serupa; spec mengikuti TC.
  - Mekanisme menyiapkan access level dan baris role per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
