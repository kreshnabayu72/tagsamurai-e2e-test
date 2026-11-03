---
id: TC-GS-ROLE-E2E-111-auto-revert-lewat-switch-active-total-control-dan-read-only
title: "Auto-Revert lewat Switch Active: Dialog Remove, Access Level Lepas pada User Total Control dan Read Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-326
  - TC-GS-ROLE-327
coverage:
  web: automated
---

# Auto-Revert lewat Switch Active: Dialog Remove, Access Level Lepas pada User Total Control dan Read Only

## Prerequisites

- Mode: FE+BE. Suite `parallel: false` karena spec mengubah access level dan baris role user Pre-setup bersama.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Data Pre-setup #20 (fixture switch Active, bernama literal sesuai TC; Access Global Settings dicentang pada kedua user): `Cakra Mahendra` (Active; Total Control dengan keenam baris Active CRUD penuh) untuk TC-326 dan `Mira Septiani` (Active; Read Only dengan keenam baris Active Read saja) untuk TC-327. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): kedua user dipastikan berada di state di atas. Mekanisme menyiapkan access level dan baris role per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): `Cakra Mahendra` di-assign Total Control ulang dan `Mira Septiani` di-assign Read Only ulang, lalu keenam baris role dikembalikan ke state Given masing-masing (Total Control CRUD penuh dan Read Only Read saja). Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log dan notifikasi bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-326: Switch Active OFF pada user Total Control memicu dialog auto-revert dan access level lepas

1. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Cakra Mahendra`, tekan Enter
2. Klik Name `Cakra Mahendra`, buka Tab `Role`
3. Verifikasi banner Total Control tampil
4. Matikan switch `Manage TAG`
5. Verifikasi dialog Title `Remove Total Control`, body `• Cakra Mahendra` lalu `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`, tombol `[Cancel]` dan `[Remove]`
6. Klik `[Remove]`
7. Verifikasi toast sukses `Success, permissions have been updated. Cakra Mahendra is no longer Total Control.`
8. Verifikasi banner Total Control hilang
9. Verifikasi switch `Manage TAG` OFF dengan checkbox Disabled
10. Verifikasi kelima switch lain tetap ON dengan CRUD penuh
11. Buka Global Settings > Role & Permission > Tab `Total Control`, ketik Search `Cakra Mahendra`, tekan Enter
12. Verifikasi empty state `No results found` tampil pada hasil Search
13. Verifikasi `Cakra Mahendra` hilang dari Tab `Total Control`
14. Buka Tab System, buka Detail `Manage TAG`, ketik Search `Cakra Mahendra`, tekan Enter
15. Verifikasi empty state `No results found` tampil pada hasil Search
16. Verifikasi `Cakra Mahendra` tidak tampil di Detail `Manage TAG`
17. Buka Detail `Manage files`, ketik Search `Cakra Mahendra`, tekan Enter
18. Verifikasi `Cakra Mahendra` tampil di Detail `Manage files` dengan Read dan Delete checked

### TC-GS-ROLE-327: Switch Active OFF pada user Read Only memicu dialog auto-revert dan access level lepas

19. Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Mira Septiani`, tekan Enter
20. Klik Name `Mira Septiani`, buka Tab `Role`
21. Verifikasi banner Read Only tampil
22. Matikan switch `Import data`
23. Verifikasi dialog Title `Remove Read Only`, body `• Mira Septiani` lalu `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`, tombol `[Cancel]` dan `[Remove]`
24. Klik `[Remove]`
25. Verifikasi toast sukses `Success, permissions have been updated. Mira Septiani is no longer Read Only.`
26. Verifikasi banner Read Only hilang
27. Verifikasi switch `Import data` OFF
28. Verifikasi kelima switch lain tetap ON dengan Read checked
29. Buka Global Settings > Role & Permission > Tab `Read Only`, ketik Search `Mira Septiani`, tekan Enter
30. Verifikasi empty state `No results found` tampil pada hasil Search
31. Verifikasi `Mira Septiani` hilang dari Tab `Read Only`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: fungsional. Teks dialog dan toast disalin persis dari baris TC-326 dan TC-327. Subjudul `###` memetakan langkah ke id TC granular.
- Log (Changelog Detail `Manage TAG`, Changelog Tab `Total Control`, System Log, Activity Log, Changelog: User > Role) dan notifikasi Auto-Revert untuk alur TC-326 (Post Condition c TC-326 menunjuk TC-GS-ROLE-329) diasersi di spec `TC-GS-ROLE-E2E-112-pencatatan-log-switch-active-remove-assign-auto-revert-dan-permintaan-sama`; spec ini tidak mengulangnya.
- Search untuk menemukan user target atau baris ditulis sebagai langkah penghubung (R-16): langkah 1, 11, 14, 17, 19, 29. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab `Role`, tab Role & Permission, dan Detail (langkah 2, 14, 17, 20).
- Langkah 3 dan 21 (banner tampil) adalah precondition TC-326 dan TC-327 ("banner Total Control/Read Only tampil" pada langkah 1) dan menjadi anchor positif bagi absence banner pada langkah 8 dan 26.
- Absence `Cakra Mahendra` dan `Mira Septiani` di tab dan Detail (langkah 13, 16, 31) didahului empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Mekanisme menyiapkan access level dan baris role per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-326 Given menyebut keenam baris Active CRUD penuh sedangkan Expected e menyebut `Manage files` R,D checked; spec mengikuti Expected (langkah 18) dan Expected c (langkah 10).
  - TC-GS-ROLE-326 dan TC-GS-ROLE-327 Post Condition ("Access level kosong"; "Baris Manage TAG/Import data inactive-retained") punya padanan di Expected c sampai e; tidak diasersi terpisah.
