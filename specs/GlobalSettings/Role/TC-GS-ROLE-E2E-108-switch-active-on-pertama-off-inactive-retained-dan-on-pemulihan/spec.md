---
id: TC-GS-ROLE-E2E-108-switch-active-on-pertama-off-inactive-retained-dan-on-pemulihan
title: "Switch Active: ON Pertama Membuat Baris, OFF Menyimpan Inactive-Retained, dan ON Memulihkan Nilai Tersimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-318
  - TC-GS-ROLE-319
  - TC-GS-ROLE-320
coverage:
  web: automated
---

# Switch Active: ON Pertama Membuat Baris, OFF Menyimpan Inactive-Retained, dan ON Memulihkan Nilai Tersimpan

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah baris role user Pre-setup bersama.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang pada semua user): `Bimo Sasongko` (Active, tanpa baris role dan tanpa access level) untuk TC-318 dan `Hanif Pradipta` (Active, baris `Manage TAG` Active dengan Read dan Update tercentang) untuk TC-319 dan TC-320. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan state baris role Active atau inactive-retained per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Baseline (dicatat di hook `before` sebelum aksi pemicu pertama, S-12): kolom Users `Manage files` pada Tab System sebagai `n-F` dan kolom Users `Manage TAG` sebagai `n-T`. Kemampuan membaca kedua nilai itu lewat UI Tab System.
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): baris `Manage files` milik `Bimo Sasongko` dihapus (kembali tanpa baris role) dan baris `Manage TAG` milik `Hanif Pradipta` dikembalikan Active dengan Read dan Update tercentang. Efek pada Pre-setup: Modified By dan Last Updated baris berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-318: Switch Active ON pertama kali meng-assign role

1. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Bimo Sasongko`, tekan Enter
2. Klik Name `Bimo Sasongko`, buka Tab `Role`
3. Verifikasi switch `Manage files` OFF
4. Verifikasi checkbox Read dan Delete baris `Manage files` Disabled
5. Nyalakan switch `Manage files`
6. Verifikasi toast sukses `Success, role has been updated.`
7. Verifikasi tidak ada popup atau dialog
8. Verifikasi switch `Manage files` ON
9. Verifikasi checkbox Read baris `Manage files` checked dan disabled
10. Verifikasi checkbox Delete baris `Manage files` unchecked dan dapat diklik
11. Buka Global Settings > Role & Permission > Tab System
12. Verifikasi kolom Users `Manage files` sama dengan `n-F` + 1
13. Buka Detail `Manage files`, ketik Search `Bimo Sasongko`, tekan Enter
14. Verifikasi `Bimo Sasongko` tampil dengan Read checked dan Delete unchecked

### TC-GS-ROLE-319: Switch Active OFF menyimpan role sebagai inactive-retained

15. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
16. Klik Name `Hanif Pradipta`, buka Tab `Role`
17. Matikan switch `Manage TAG`
18. Verifikasi toast sukses `Success, role has been updated.`
19. Verifikasi tidak ada dialog konfirmasi
20. Verifikasi switch `Manage TAG` OFF
21. Verifikasi seluruh checkbox baris `Manage TAG` Disabled
22. Buka Global Settings > Role & Permission > Tab System
23. Verifikasi kolom Users `Manage TAG` sama dengan `n-T` - 1
24. Buka Detail `Manage TAG`, ketik Search `Hanif Pradipta`, tekan Enter
25. Verifikasi empty state `No results found` tampil pada hasil Search
26. Verifikasi `Hanif Pradipta` tidak tampil di Detail `Manage TAG`

### TC-GS-ROLE-320: Switch Active ON memulihkan baris inactive-retained dengan nilai tersimpan

27. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
28. Klik Name `Hanif Pradipta`, buka Tab `Role`
29. Nyalakan switch `Manage TAG`
30. Verifikasi toast sukses `Success, role has been updated.`
31. Verifikasi tidak ada popup atau dialog
32. Verifikasi switch `Manage TAG` ON
33. Verifikasi checkbox Read baris `Manage TAG` checked dan disabled
34. Verifikasi checkbox Update baris `Manage TAG` checked
35. Buka Global Settings > Role & Permission > Tab System
36. Verifikasi kolom Users `Manage TAG` sama dengan `n-T`
37. Buka Detail `Manage TAG`, ketik Search `Hanif Pradipta`, tekan Enter
38. Verifikasi `Hanif Pradipta` tampil dengan Read dan Update checked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional (tidak ada kelas a sampai h); subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (38 langkah) karena ketiga blok satu topik (Switch Active pada Tab `Role` User) dan TC-320 bergantung pada state inactive-retained yang dibangun TC-319 (urutan 319 sebelum 320 dipertahankan seperti di TC); pemisahan akan mengulang Given dan pembukaan Tab `Role`.
- Search untuk menemukan user target atau baris di Detail ditulis sebagai langkah penghubung (R-16): langkah 1, 13, 15, 24, 27, 37. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab `Role` dan Tab System (langkah 2, 11, 16, 22, 28, 35).
- Absence `Hanif Pradipta` di Detail `Manage TAG` (langkah 26) didahului empty state `No results found` hasil Search (langkah 25) sebagai anchor positif (bagian 8b butir 2).
- Perilaku tidak muncul popup atau dialog (langkah 7, 19, 31) diasersi segera sesudah toast sebagai asersi state sementara (bagian 8b butir 5 dan 11).
- Log dan notifikasi akibat Switch Active diasersi di spec `TC-GS-ROLE-E2E-112-pencatatan-log-switch-active-remove-assign-auto-revert-dan-permintaan-sama` (TC-GS-ROLE-330 memakai alur TC-GS-ROLE-319 dan TC-GS-ROLE-320).
- Temuan untuk QA:
  - Mekanisme menyiapkan state Given baris role Active atau inactive-retained per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-318 Post Condition ("Bimo Sasongko punya baris Manage files Active (Read saja)") dan TC-GS-ROLE-319 Post Condition tidak punya langkah observasi tersendiri di luar Expected; keduanya tidak diasersi terpisah.
  - TC-GS-ROLE-318 dan TC-GS-ROLE-319 menyebut hitungan Users `n` dicatat tanpa menyebut cara membaca; spec memakai kolom Users pada Tab System yang dicatat di hook `before`.
  - TC-GS-ROLE-320 Precondition bergantung pada hasil TC-GS-ROLE-319; spec membangun state itu pada blok TC-GS-ROLE-319 dalam spec yang sama.
