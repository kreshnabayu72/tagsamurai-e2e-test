---
id: TC-FA-SU-E2E-065-group-manager-pada-group-role-dialog-remove-konfirmasi-dan-cancel
title: "Group Manager pada Group Role: Dialog Remove, Konfirmasi, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-212
  - TC-FA-SU-213
  - TC-FA-SU-214
coverage:
  web: automated
---

# Group Manager pada Group Role: Dialog Remove, Konfirmasi, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah terakhir): Group Manager Oscar Pranata (Pre-setup #9), email disediakan tim FE (tidak tertulis di Pre-setup TC), kredensial `Spectra.env.FA_GM_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Oscar Pranata, Group Manager IT Infrastructure dan Accounts Payable dengan Group Role `Manage group` penuh (Create, Read, Update, Delete) pada kedua grup (Pre-setup #9). Popup "role penopang" pada TC adalah role `Manage group`.
- Data uji: perubahan yang diuji adalah menghapus centang Update pada IT Infrastructure di popup Assign Group Role `Manage group`.
- Kemampuan teknis: seed API untuk memulihkan status Group Manager dan penugasan Oscar Pranata (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: penugasan Group Role dan status Group Manager Oscar Pranata pada IT Infrastructure; dipulihkan ke Pre-setup #9 lewat seed API di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

1. Catat jumlah entri `Auto-Revert`, `Edit`, dan `Remove` Oscar Pranata pada Tab Changelog sebagai baseline

### TC-FA-SU-212: Group Manager: Save yang membuat penugasan grup tidak lagi CRUD penuh memunculkan dialog Remove Group Manager

2. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role
3. Buka popup Assign Group Role pada role penopang Manage group
4. Hapus centang Update pada IT Infrastructure
5. Klik `[Save]`
6. Verifikasi dialog Title `Remove Group Manager` dengan Body bullet `• Oscar Pranata`, kalimat `This edit will remove Group Manager status for this group. Their role permissions in this group will remain as edited.`, dan `Are you sure you want to remove it?`
7. Verifikasi tombol `[Cancel]` dan `[Remove]`
8. Verifikasi belum ada toast tersimpan saat dialog tampil (perubahan belum disimpan)

### TC-FA-SU-214: Cancel dialog Remove Group Manager dari popup: popup kembali dengan isi utuh dan tidak ada penyimpanan

9. Klik `[Cancel]`
10. Verifikasi dialog menutup dan popup kembali tampil dengan perubahan tetap seperti sebelum klik `[Save]` (Update IT Infrastructure tidak tercentang)
11. Klik `[✕]` pada popup
12. Verifikasi dialog `Unsaved Changes`
13. Klik `[Leave]`
14. Verifikasi banner Group Manager Oscar Pranata masih memuat IT Infrastructure (status Group Manager tetap)
15. Buka Tab Changelog, Search `Oscar Pranata`, tekan Enter, lalu muat ulang
16. Verifikasi jumlah entri Oscar Pranata pada Tab Changelog sama dengan baseline

### TC-FA-SU-213: Konfirmasi Remove Group Manager: penugasan tersimpan, status GM terlepas, toast T-06b, log Auto-Revert, dan notifikasi

17. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role pada role penopang Manage group
18. Hapus centang Update pada IT Infrastructure lalu klik `[Save]`
19. Klik `[Remove]`
20. Verifikasi popup menutup
21. Verifikasi penugasan tersimpan dengan Update tidak tercentang pada IT Infrastructure
22. Verifikasi toast "Success, permissions have been updated. Oscar Pranata is no longer Group Manager for IT Infrastructure."
23. Verifikasi banner Group Manager hilang atau ter-update tanpa IT Infrastructure
24. Buka Tab Changelog, Search `Oscar Pranata`, tekan Enter, lalu muat ulang sampai entri tampil
25. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — IT Infrastructure` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog
26. Verifikasi entri `Edit` permission bertambah dibanding baseline pada Tab Changelog
27. Logout lalu login sebagai Group Manager Oscar Pranata
28. Buka panel notifikasi
29. Verifikasi notifikasi in-app view-only diterima Oscar Pranata

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-SU-212, 214, lalu 213. TC-FA-SU-213 dan 214 sama-sama memulai dari dialog yang dibuka TC-FA-SU-212 ("Ulangi perubahan hingga dialog tampil"); `[Cancel]` TC-FA-SU-214 dijalankan pada dialog TC-FA-SU-212 sehingga status Group Manager yang belum berubah dapat diasersi sebelum TC-FA-SU-213 mengubahnya (S-04: langkah dependensi disalin utuh pada TC-FA-SU-213).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1. Baseline log mengikuti S-12; penutupan popup dirty mengikuti S-08.
- Langkah pola baca-log: langkah 15, 16 dan 24 sampai 26. Search `Oscar Pranata` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16). Langkah terakhir spec mengganti akun ke Group Manager Oscar Pranata (ganti akun eksplisit, S-07); hook `after` mengembalikan sesi ke akun default suite.
- TC-FA-SU-214: klausa "tidak ada entri log" pada aksi yang dibatalkan ditulis sebagai asersi jumlah dengan baseline (bagian 3 prinsip 13 butir g, S-12).
- Temuan untuk QA:
  - TC-FA-SU-212 menyebut "role penopang" tanpa nama role; spec memakai `Manage group` sesuai Pre-setup #9.
  - TC-FA-SU-213 butir e menyebut notifikasi in-app view-only diterima Oscar Pranata; spec hanya mengasersi penerimaan (copy Title dan Body dimiliki modul Notification, Catatan TC).
  - Post Condition TC-FA-SU-213 butir d (Settings > Role & Permission > Detail Role Group Role) tidak punya langkah observasi di TC dan tidak diasersi.
