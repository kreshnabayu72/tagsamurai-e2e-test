---
id: TC-GS-ROLE-E2E-110-cascade-remove-access-global-settings-baris-active-dan-inactive-retained
title: "Cascade Remove Access Global Settings: Baris Active dan Inactive-Retained Terhapus Tanpa Pemulihan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-325
coverage:
  web: automated
---

# Cascade Remove Access Global Settings: Baris Active dan Inactive-Retained Terhapus Tanpa Pemulihan

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah Access Global Settings dan baris role user Pre-setup bersama.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC): `Tiara Anggun` (Active; `Manage TAG` Active dengan Read saja; `Manage hardware` inactive-retained dengan Create, Read, Update tersimpan; tanpa access level; Access Global Settings dicentang). Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): `Tiara Anggun` dipastikan berada di state di atas. Mekanisme menyiapkan baris Active dan inactive-retained disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sesudah Given, S-12): kolom Users `Manage TAG` sebagai `n-T` dan kolom Users `Manage hardware` sebagai `n-H` pada Tab System.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): Access Global Settings `Tiara Anggun` dicentang kembali dan state Given dipulihkan (`Manage TAG` Active Read saja; `Manage hardware` inactive-retained Create, Read, Update). Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-325: Cascade Remove Access Global Settings menghapus baris Active dan inactive-retained tanpa pemulihan

1. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Tiara Anggun`, tekan Enter
2. Klik row action `Edit` pada baris `Tiara Anggun`
3. Hapus centang Global Settings
4. Klik `[Save]`
5. Verifikasi dialog Remove Access tampil
6. Klik `[Remove]` pada dialog Remove Access
7. Buka Global Settings > Role & Permission > Tab System, buka Detail `Manage TAG`, ketik Search `Tiara Anggun`, tekan Enter
8. Verifikasi empty state `No results found` tampil pada hasil Search
9. Verifikasi `Tiara Anggun` tidak tampil di Detail `Manage TAG`
10. Buka Detail `Manage hardware`, ketik Search `Tiara Anggun`, tekan Enter
11. Verifikasi empty state `No results found` tampil pada hasil Search
12. Verifikasi `Tiara Anggun` tidak tampil di Detail `Manage hardware`
13. Buka Tab System
14. Verifikasi kolom Users `Manage TAG` sama dengan `n-T` - 1
15. Verifikasi kolom Users `Manage hardware` sama dengan `n-H` (tidak berubah)
16. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Tiara Anggun`, tekan Enter
17. Klik row action `Edit` pada baris `Tiara Anggun`
18. Centang Global Settings
19. Klik `[Save]`
20. Klik Name `Tiara Anggun`, buka Tab `Role`
21. Verifikasi keenam switch OFF
22. Verifikasi seluruh checkbox Disabled
23. Nyalakan switch `Manage hardware`
24. Verifikasi baris `Manage hardware` dibuat baru dengan Read checked dan disabled
25. Verifikasi Create dan Update baris `Manage hardware` unchecked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional. Satu TC sumber; subjudul `###` memetakan langkah ke id TC granular.
- Dialog Remove Access pada langkah 5 hanya diasersi tampil, sesuai Expected a TC-325 (teks dialog tidak disebut TC). Kalimat dalam kurung pada Expected a ("Tiara Anggun masih punya 1 role Active, yaitu Manage TAG") menjelaskan alasan dialog tampil dan tidak diasersi sebagai klausa terpisah.
- Search untuk menemukan user atau baris target ditulis sebagai langkah penghubung (R-16): langkah 1, 7, 10, 16. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka row action `Edit`, mengubah centang Global Settings, `[Save]`, membuka Detail, Tab System, dan Tab `Role` (langkah 2 sampai 4, 6, 13, 17 sampai 20).
- Absence `Tiara Anggun` di Detail (langkah 9 dan 12) didahului empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- Langkah 23 menyalakan switch `Manage hardware` untuk mengamati bahwa baris dibuat baru tanpa pemulihan nilai tersimpan; TC tidak menyebut toast untuk langkah ini sehingga toast tidak diasersi.
- Temuan untuk QA:
  - Mekanisme menyiapkan state Given baris Active dan inactive-retained (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-325 Post Condition ("punya baris Manage hardware Active (Read saja); tidak ada baris role lain") tidak punya langkah observasi di luar Expected e; tidak diasersi terpisah.
  - TC-GS-ROLE-325 tidak menyebut teks dialog Remove Access; spec hanya mengasersi dialog tampil.
