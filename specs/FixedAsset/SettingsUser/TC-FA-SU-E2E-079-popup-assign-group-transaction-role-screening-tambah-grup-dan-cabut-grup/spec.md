---
id: TC-FA-SU-E2E-079-popup-assign-group-transaction-role-screening-tambah-grup-dan-cabut-grup
title: "Popup Assign Group Transaction Role: Screening, Tambah Grup, dan Cabut Grup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-257
  - TC-FA-SU-258
  - TC-FA-SU-259
coverage:
  web: automated
---

# Popup Assign Group Transaction Role: Screening, Tambah Grup, dan Cabut Grup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini; baris Disposal × Staff pada Finance & Accounting dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: grup IT Infrastructure ditambahkan lalu dicabut pada baris Disposal × Staff (TC-FA-SU-258 dan 259).
- Kemampuan teknis: seed API untuk memulihkan Transaction Role Mira Anggraini ke Pre-setup #39 (disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (disediakan tim FE/BE, bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: Transaction Role Mira Anggraini (IT Infrastructure ditambahkan lalu dicabut pada Disposal × Staff); dipulihkan ke Pre-setup #39 lewat seed API di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-257: Screening popup Assign Group Transaction Role: header, pencarian, pohon tercentang, dan footer

1. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
2. Verifikasi header `Assign Group` dengan close `[✕]`
3. Verifikasi Search `Search groups...`
4. Verifikasi pohon multi-select dengan grup ter-assign pada baris (Finance & Accounting) tercentang dan dapat dicabut centangnya (bukan Disabled)
5. Verifikasi footer `[Cancel]` (Text, Contrast) dan `[Save]` (Success)
6. Verifikasi Jenis Transaksi dan Role tidak ditampilkan di popup
7. Verifikasi `[Save]` Disabled sampai pilihan berbeda dari kondisi saat popup dibuka

### TC-FA-SU-258: Assign Group: tambah grup baru memakai Role baris, toast assigned, dan log Assign

8. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
9. Centang IT Infrastructure pada popup yang masih terbuka
10. Klik `[Save]`
11. Verifikasi popup menutup
12. Verifikasi toast "Success, Staff has been assigned."
13. Verifikasi baris Disposal × Staff menampilkan dua badge Finance & Accounting dan IT Infrastructure
14. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
15. Verifikasi entri `Assign` Field `Disposal — IT Infrastructure — Staff` bertambah satu dibanding baseline pada Tab Changelog

### TC-FA-SU-259: Assign Group: cabut grup menampilkan dialog Remove Transaction Role lalu toast removed dan log Remove

16. Catat jumlah entri `Remove` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
17. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
18. Hapus centang IT Infrastructure
19. Klik `[Save]`
20. Verifikasi dialog Title `Remove Transaction Role` dengan Body `• Mira Anggraini`, `This user will lose the selected transaction role.`, dan `Are you sure you want to remove it?`
21. Klik `[Remove]`
22. Verifikasi toast "Success, Staff has been removed."
23. Verifikasi IT Infrastructure hilang dari baris Disposal × Staff
24. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
25. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Disposal — IT Infrastructure — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 8 dan 16. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 14, 15, 24 dan 25. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Popup `Assign Group` dibuka pada TC-FA-SU-257 dan dipakai TC-FA-SU-258 tanpa dibuka ulang karena belum ada perubahan (halaman yang sama dipakai berulang, bagian 3 prinsip 13). TC-FA-SU-259 (dependensi TC-FA-SU-258) membuka popup lagi dan mencabut grup yang ditambahkan TC-FA-SU-258 (S-04).
- Temuan untuk QA:
  - TC-FA-SU-258 butir c dan TC-FA-SU-259 butir c menyebut log tanpa menyebut permukaan; spec mengasersi Tab Changelog. Post Condition TC-FA-SU-258 dan 259 (state baris, tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi tambahan di TC dan tidak diasersi.
