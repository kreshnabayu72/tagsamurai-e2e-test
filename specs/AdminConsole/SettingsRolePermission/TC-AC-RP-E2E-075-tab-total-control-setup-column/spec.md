---
id: TC-AC-RP-E2E-075-tab-total-control-setup-column
title: "Setup Column Tab Total Control dan Tab Read Only, kolom curated, Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-251
  - TC-AC-RP-252
  - TC-AC-RP-253
  - TC-AC-RP-254
  - TC-AC-RP-255
coverage:
  web: automated
---

# Setup Column Tab Total Control dan Tab Read Only, kolom curated, Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Data Pre-setup Tab Total Control (Pre-setup #1 dan #13), enam baris urutan Name A-Z: `Bambang Hartono` (CEO, Board; Modified By dan Last Updated "—"), `Budi Santoso` (Supervisor, Warehouse, Pending Activation; "Siti N" 08 Jun 2026, 09:30), `John Doe` (Manager, Finance; "Siti N" 15 Jun 2026, 10:05), `Rina Wijaya` (Staff, Finance; "Bambang H" 05 Jun 2026, 15:20), `Sarah Kim` (Staff, Operations, Inactive; "John D" 10 Jun 2026, 14:50), `Siti Nurhaliza` (Admin Lead, IT; "Bambang H" 01 Jun 2026, 08:00).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Custom field User aktif (Pre-setup #12): `Employee Grade` (Dropdown) dan `Nickname` (Text); `John Doe` memiliki Nickname `JD`.
- State yang diubah: konfigurasi kolom disimpan di browser (per perangkat per tabel, `localStorage`). Antar blok TC preferensi kolom dihapus (langkah penghubung) dan hook `after` menghapusnya lagi.
- Kemampuan teknis: menghapus preferensi kolom tabel di browser (disediakan tim FE); drag kolom dan pin kolom lewat Setup Column.

## Test Steps

### TC-AC-RP-254: Daftar kolom curated di Column Visibility

1. Buka Column Visibility lewat header Actions `⋯`
2. Verifikasi daftar memuat Name, Position, Division, Status, Modified By, dan Last Updated dengan keadaan checked
3. Verifikasi daftar memuat Email, Activation Status, Temporary User, Temporary Until, TAG, `Employee Grade`, dan `Nickname` dengan keadaan unchecked
4. Verifikasi daftar tidak memuat User Type maupun Authenticator (MFA)

### TC-AC-RP-255: Filter dan Search kolom Custom Field aktif

5. Tampilkan kolom `Employee Grade` dan `Nickname` lewat Column Visibility
6. Buka Filter Panel
7. Verifikasi Filter Panel memuat field `Employee Grade` (Dropdown)
8. Verifikasi Filter Panel tidak memuat field `Nickname` (Text)
9. Ketik Search `JD`, tekan Enter
10. Verifikasi baris `John Doe` tampil
11. Klik `(←)` pada kotak Search
12. Hapus preferensi kolom tabel di browser, lalu muat ulang halaman (F5)

### TC-AC-RP-251: Setup Column Tab Total Control: hide, unhide, reorder, pin

13. Buka Column Visibility lewat header Actions `⋯`
14. Sembunyikan kolom Division
15. Drag kolom Status ke posisi kedua
16. Pin kolom Name
17. Verifikasi kolom Division hilang dari tabel
18. Verifikasi kolom Status pindah ke posisi kedua
19. Verifikasi kolom Name ter-pin
20. Refresh halaman (F5)
21. Verifikasi susunan kolom tetap setelah F5: Division tidak tampil, Status di posisi kedua, Name ter-pin
22. Hapus preferensi kolom tabel di browser, lalu muat ulang halaman (F5)

### TC-AC-RP-252: Setup Column mencegah menyembunyikan kolom terakhir yang visible

23. Buka Column Visibility lewat header Actions `⋯`
24. Sembunyikan kolom Position, Division, Status, Modified By, dan Last Updated (seluruh kolom kecuali Name)
25. Coba sembunyikan kolom Name
26. Verifikasi kolom Name tidak dapat disembunyikan (minimal 1 kolom visible)
27. Hapus preferensi kolom tabel di browser, lalu muat ulang halaman (F5)

### TC-AC-RP-253: Setup Column Tab Total Control dan Tab Read Only tersimpan terpisah per tabel

28. Sembunyikan kolom Position di Tab Total Control lewat Column Visibility
29. Klik tab `Read Only`
30. Verifikasi kolom Position tetap tampil di Tab Read Only

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Penyimpangan urutan: TC-AC-RP-254 dan TC-AC-RP-255 dijalankan lebih dulu karena TC-AC-RP-254 membaca daftar kolom dalam keadaan bawaan; TC-AC-RP-253 terakhir karena berakhir di Tab Read Only. TC-AC-RP-251 dan TC-AC-RP-252 mengubah konfigurasi kolom, sehingga urutan antar blok ditentukan oleh kebutuhan keadaan bawaan.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 11 mengosongkan Search; langkah 12, 22, dan 27 memulihkan konfigurasi kolom ke bawaan sebelum TC berikutnya mengandalkannya (S-09), memakai kemampuan hapus preferensi kolom (bukan `[Reset to Default]`).
- Langkah "Sembunyikan kolom Position, Division, Status, Modified By, dan Last Updated" pada TC-AC-RP-252 menyebut kolom visible bawaan selain Name; dijalankan dari keadaan bawaan (sesudah langkah 22) sehingga tidak ada kolom yang menyala kembali.
- Temuan untuk QA:
  - TC-AC-RP-251, 252, 253, 254, dan 255 menyebut Column Visibility tanpa `[Save]`; konvensi mencatat modal Setup Column punya `[Reset to Default]` dan `[Save]`. Spec mengikuti TC; QA perlu memastikan apakah perubahan berlaku langsung atau memerlukan `[Save]`.
  - TC-AC-RP-251 menyebut penyimpanan "web: `localStorage`" sebagai bagian Expected; spec hanya mengasersi susunan kolom setelah F5, tidak membaca `localStorage` (tidak ada kemampuan baca yang disebut TC).
