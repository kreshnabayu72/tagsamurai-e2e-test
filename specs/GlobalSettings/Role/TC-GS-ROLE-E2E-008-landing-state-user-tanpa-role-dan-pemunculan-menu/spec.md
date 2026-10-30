---
id: TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-pemunculan-menu
title: "Landing State User tanpa Access Level dan tanpa Role, serta Pemunculan Menu Setelah Mendapat Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-21
  - TC-GS-ROLE-22
coverage:
  web: automated
---

# Landing State User tanpa Access Level dan tanpa Role, serta Pemunculan Menu Setelah Mendapat Role

## Prerequisites

- Mode: FE+BE.
- Aktor pertama (hook `before`, sesi B): Agus Salim (Pre-setup #9, Access Global Settings dicentang, tanpa access level, tanpa baris role), email disediakan tim FE, password `Spectra.env.GS_ROLE_TARGET_PASSWORD`. Aktor sesi A (langkah 10): Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser aktif bersamaan (sesi B Agus Salim tetap terbuka pada landing state selama sesi A Ahmad Fauzi bertindak); sesi UI sesi A dipakai karena langkah TC menetapkan aksi lewat UI.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`), termasuk akun Agus Salim.
- Data: Agus Salim dikembalikan ke Pre-setup #9 di hook `before` (tanpa baris role dan tanpa access level) lewat API (kemampuan disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Hook `after` memulihkan Agus Salim ke Pre-setup #9 dengan menghapus baris role Manage TAG hasil Assign pada TC-GS-ROLE-22, lalu menutup konteks sesi A dan mengembalikan sesi ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`).
- Detail "Manage TAG" tidak memuat baris Agus Salim pada awal spec; popup Assign Role menampilkan Agus Salim sebagai kandidat (Access Global Settings dicentang, tanpa baris role).

## Test Steps

### TC-GS-ROLE-21: Landing page Global Settings untuk user tanpa access level dan tanpa role

1. Verifikasi Portal tampil (login Agus Salim berhasil)
2. Klik card Global Settings di Portal
3. Verifikasi app Global Settings terbuka
4. Verifikasi pengguna tidak dialihkan kembali ke Portal
5. Verifikasi area konten menampilkan illustration
6. Verifikasi area konten menampilkan "You don't have access to any menu yet."
7. Verifikasi area konten menampilkan subtext "Contact your administrator to get access."
8. Verifikasi sidebar tidak menampilkan menu User, Role & Permission, Import, TAG, Hardware, Brand, Measurement, File Manager, General Settings, dan Activity Log
9. Verifikasi tidak tampil "Unable to load this data." dan tidak tampil `[Try Again]`

### TC-GS-ROLE-22: Landing state hilang setelah user tanpa role mendapat role

10. Sesi A: login sebagai Total Control (Ahmad Fauzi) di konteks browser kedua
11. Sesi A: buka Global Settings > Role & Permission > System
12. Sesi A: klik Role Name `Manage TAG`
13. Sesi A: klik `[+ Assign]`
14. Sesi A: ketik Search `Agus Salim`, tekan Enter
15. Sesi A: centang baris `Agus Salim`
16. Sesi A: klik `[Assign]`
17. Tunggu aksi selesai
18. Sesi B: reload halaman
19. Verifikasi sidebar sesi B menampilkan menu TAG
20. Verifikasi pesan "You don't have access to any menu yet." tidak tampil lagi
21. Verifikasi menu Role & Permission tetap tidak tampil di sidebar

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini kelas multi-konteks (kelas c): sesi B (Agus Salim) adalah objek asersi dan sesi A (Ahmad Fauzi) memicu perubahan state lewat UI sesuai langkah TC-GS-ROLE-22; karena kelas c adalah kelas spec ini, pengecualian P-2 tidak dipakai.
- TC-GS-ROLE-22 bertanda Automation `Manual Only — (d) dua sesi paralel` di TC dan tetap masuk spec; kebutuhan dua konteks browser dicatat di Prerequisites (Kemampuan teknis).
- Langkah 1 menjadi anchor bahwa login Agus Salim (hook `before`) berhasil; "Login sukses" pada Expected a TC-GS-ROLE-21 teramati sebagai Portal tampil. Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): menunggu aksi `[Assign]` selesai sebelum berpindah ke sesi B (langkah 17).
- Langkah 8 (absence sidebar) didahului langkah 5 sampai 7 yang membuktikan halaman Global Settings sudah termuat; langkah 20 dan 21 (absence pesan dan menu) didahului langkah 19 (menu TAG tampil di sidebar yang sama).
- Pengecekan state TC-GS-ROLE-22 butir c (menu Role & Permission tetap tidak tampil) diasersi pada langkah 21.
- Temuan untuk QA:
  - TC-GS-ROLE-22 Post Condition "Agus Salim punya baris role Manage TAG (Read)" tidak punya langkah observasi di TC; tidak diasersi di spec.
  - TC-GS-ROLE-21 langkah 1 ("Login") adalah login akun Agus Salim; spec memakai hook `before` untuk login dan mengasersi Portal tampil.
  - TC-GS-ROLE-22 tidak menyebut cara Agus Salim dicari di popup Assign (halaman atau Search); spec memakai Search.
