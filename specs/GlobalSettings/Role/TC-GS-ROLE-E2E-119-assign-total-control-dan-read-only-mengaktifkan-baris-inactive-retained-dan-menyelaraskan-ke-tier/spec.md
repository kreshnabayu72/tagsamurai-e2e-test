---
id: TC-GS-ROLE-E2E-119-assign-total-control-dan-read-only-mengaktifkan-baris-inactive-retained-dan-menyelaraskan-ke-tier
title: "Assign Total Control dan Read Only: Baris Inactive-Retained Diaktifkan dan Diselaraskan ke Pola Tier"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-323
  - TC-GS-ROLE-324
coverage:
  web: automated
---

# Assign Total Control dan Read Only: Baris Inactive-Retained Diaktifkan dan Diselaraskan ke Pola Tier

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah access level dan baris role user Pre-setup bersama.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang, tanpa access level pada kedua user): `Farhan Maulana` (Active; `Import data` inactive-retained dengan Create dan Read tersimpan; `Manage files` Active dengan Read saja; tanpa baris role lain) untuk TC-323 dan `Gilang Ramadhan` (Active; `Manage hardware` inactive-retained dengan Create, Read, Update, Delete tersimpan; tanpa baris role lain) untuk TC-324. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan baris Active dan inactive-retained disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sebelum aksi pemicu pertama, S-12): total entri Changelog Tab Total Control hasil Search `Farhan Maulana` sebagai `B-TC` dan total entri Changelog Detail `Import data` hasil Search `Farhan Maulana` sebagai `B-ID`. Kemampuan membaca total entri disediakan tim FE.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): access level `Farhan Maulana` dan `Gilang Ramadhan` dicabut dan state Given keduanya dipulihkan (baris sesuai Pre-setup #20). Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-323: Assign Total Control mengaktifkan baris inactive-retained dan menyelaraskannya ke pola tier

1. Buka Global Settings > Role & Permission > Tab `Total Control`
2. Klik `[+ Assign]`
3. Ketik Search `Farhan Maulana`, tekan Enter
4. Centang `Farhan Maulana`, klik `[Assign]`
5. Verifikasi toast sukses `Success, Total Control has been assigned.`
6. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Farhan Maulana`, tekan Enter
7. Klik Name `Farhan Maulana`, buka Tab `Role`
8. Verifikasi keenam switch ON
9. Verifikasi `Import data` Create dan Read checked
10. Verifikasi `Manage files` Read dan Delete checked
11. Verifikasi `Manage hardware` dan `Manage master reference` Create, Read, Update, dan Delete checked
12. Verifikasi `Manage TAG` Read dan Update checked
13. Verifikasi `Manage user and role` Create, Read, Update, dan Delete checked
14. Buka Global Settings > Role & Permission > Tab System, buka Detail `Import data`, ketik Search `Farhan Maulana`, tekan Enter
15. Verifikasi `Farhan Maulana` tampil di Detail `Import data` dengan Create dan Read checked
16. Verifikasi hasil Search Detail `Import data` memuat tepat 1 baris untuk `Farhan Maulana`
17. Buka Detail `Manage files`, ketik Search `Farhan Maulana`, tekan Enter
18. Verifikasi `Farhan Maulana` tampil di Detail `Manage files` dengan Read dan Delete checked
19. Verifikasi hasil Search Detail `Manage files` memuat tepat 1 baris untuk `Farhan Maulana`
20. Buka Changelog Tab `Total Control`, ketik Search `Farhan Maulana`, tekan Enter
21. Verifikasi total entri sama dengan `B-TC` + 1
22. Verifikasi entry baru: Action `Assign`, Field `Access Level`, Old `—`, New `Total Control`
23. Tutup modal Changelog
24. Buka Detail `Import data`, klik `Changelog`, ketik Search `Farhan Maulana`, tekan Enter
25. Verifikasi total entri Changelog Detail `Import data` untuk `Farhan Maulana` sama dengan `B-ID` (tidak memuat entry baru untuk `Farhan Maulana`)
26. Tutup modal Changelog

### TC-GS-ROLE-324: Assign Read Only mengaktifkan baris inactive-retained dan menyelaraskannya ke Read saja

27. Buka Global Settings > Role & Permission > Tab `Read Only`
28. Klik `[+ Assign]`
29. Ketik Search `Gilang Ramadhan`, tekan Enter
30. Centang `Gilang Ramadhan`, klik `[Assign]`
31. Verifikasi toast sukses `Success, Read Only has been assigned.`
32. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Gilang Ramadhan`, tekan Enter
33. Klik Name `Gilang Ramadhan`, buka Tab `Role`
34. Verifikasi keenam switch ON
35. Verifikasi seluruh baris hanya Read checked dan Create, Update, Delete unchecked, termasuk `Manage hardware`
36. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage hardware`, ketik Search `Gilang Ramadhan`, tekan Enter
37. Verifikasi `Gilang Ramadhan` tampil di Detail `Manage hardware` dengan Read checked saja

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional. Subjudul `###` memetakan langkah ke id TC granular. TC terkait ada di spec `TC-GS-ROLE-E2E-108-switch-active-on-pertama-off-inactive-retained-dan-on-pemulihan` (Switch Active) dan `TC-GS-ROLE-E2E-109-popup-assign-role-eksklusi-baris-inactive-retained-dan-konflik-user-menjadi-inactive-retained` (popup Assign Role).
- Spec melewati sekitar 35 langkah (37 langkah) karena kedua blok satu topik (Assign access level atas user dengan baris inactive-retained) dan berdiri sendiri: tiap blok punya user, Given, dan asersi sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah 20 sampai 26 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi`).
- Search untuk menemukan user target atau baris di Detail dan Changelog ditulis sebagai langkah penghubung (R-16): langkah 3, 6, 14, 17, 20, 24, 29, 32, 36. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka tab, popup, Detail, Tab `Role`, dan Changelog (langkah 1, 2, 7, 27, 28, 33), serta menutup modal Changelog (langkah 23 dan 26).
- Klausa Expected d TC-323 "Changelog Detail `Import data` tidak memuat entry untuk Farhan Maulana" adalah scope exclusion dengan anchor positif dan baseline sendiri (bagian 3 prinsip 13g), bukan asersi absence kelas g: entry `Assign` pada Changelog Tab `Total Control` (langkah 22) membuktikan Assign sudah tercatat, dan total entri Detail `Import data` dibandingkan dengan `B-ID` (langkah 25).
- Nilai checkbox tiap role pada langkah 9 sampai 13 mengikuti Expected TC-323 (pola tier Total Control); checkbox yang tidak disebut tidak diasersi.
- Temuan untuk QA:
  - Mekanisme menyiapkan state Given baris Active dan inactive-retained (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-323 dan TC-GS-ROLE-324 Post Condition punya padanan di Expected b dan tidak diasersi terpisah.
  - TC-GS-ROLE-323 Expected b menyebut `Manage files` R,D checked sedangkan Given hanya Read; hasil upsert dianggap hasil penyelarasan ke pola tier (sesuai Expected), dan spec mengikuti Expected.
  - TC-GS-ROLE-323 dan TC-GS-ROLE-324 tidak menyebut baris pembanding atau cara mengenali entry baru; spec memakai total entri dengan baseline `B-TC` (S-12).
