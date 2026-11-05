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
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node IT Infrastructure (langkah 10) tidak Disabled oleh gate Home Group constraint; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
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
8. Verifikasi preview scope tidak memuat grup yang sudah tercentang sejak popup dibuka (Finance & Accounting)

### TC-FA-SU-258: Assign Group: tambah grup baru memakai Role baris, toast assigned, dan log Assign

9. Catat jumlah entri `Assign` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
10. Centang IT Infrastructure pada popup yang masih terbuka
11. Verifikasi preview scope hanya untuk grup yang baru dicentang (IT Infrastructure beserta cakupannya) dan tidak memuat Finance & Accounting
12. Klik `[Save]`
13. Verifikasi popup menutup
14. Verifikasi toast "Success, Staff has been assigned."
15. Verifikasi baris Disposal × Staff menampilkan dua badge Finance & Accounting dan IT Infrastructure
16. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
17. Verifikasi entri `Assign` Field `Disposal — IT Infrastructure — Staff` bertambah satu dibanding baseline pada Tab Changelog

### TC-FA-SU-259: Assign Group: cabut grup menampilkan dialog Remove Transaction Role lalu toast removed dan log Remove

18. Catat jumlah entri `Remove` Object `Transaction Role` Mira Anggraini pada Tab Changelog sebagai baseline
19. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[Assign Group]` pada baris Disposal × Staff
20. Hapus centang IT Infrastructure
21. Klik `[Save]`
22. Verifikasi dialog Title `Remove Transaction Role` dengan Body `• Mira Anggraini`, `This user will lose the selected transaction role.`, dan `Are you sure you want to remove it?`
23. Klik `[Remove]`
24. Verifikasi toast "Success, Staff has been removed."
25. Verifikasi IT Infrastructure hilang dari baris Disposal × Staff
26. Buka Tab Changelog, Search `Mira Anggraini`, tekan Enter, lalu muat ulang sampai entri tampil
27. Verifikasi entri `Remove` / Object `Transaction Role` / Field `Disposal — IT Infrastructure — Staff` / Old Value `Assigned` / New Value `—` bertambah satu dibanding baseline pada Tab Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 9 dan 18. Baseline log mengikuti S-12.
- Langkah pola baca-log: langkah 16, 17, 26 dan 27. Search `Mira Anggraini` pada langkah itu adalah langkah penghubung untuk menemukan baris target (R-16).
- Popup `Assign Group` dibuka pada TC-FA-SU-257 dan dipakai TC-FA-SU-258 tanpa dibuka ulang karena belum ada perubahan (halaman yang sama dipakai berulang, bagian 3 prinsip 13). TC-FA-SU-259 (dependensi TC-FA-SU-258) membuka popup lagi dan mencabut grup yang ditambahkan TC-FA-SU-258 (S-04).
- Pre-setup #50 diterapkan hanya pada Mira Anggraini (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih IT Infrastructure (langkah 10); Home Group Mira Anggraini dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - TC-FA-SU-257 butir e diperbarui: preview scope hanya untuk grup yang baru dicentang. Asersi ditulis pada langkah 8 (sebelum ada centang baru) dan langkah 11 (sesudah IT Infrastructure dicentang pada blok TC-FA-SU-258, karena aksi centang berada di sana); TC dan PRD tidak menetapkan copy, format, atau selektor preview scope sehingga asersi longgar sebagai daftar node, dan format perlu dikonfirmasi tim FE (lihat TC-FA-SU-1103, E2E-410).
  - TC-FA-SU-258 butir c dan TC-FA-SU-259 butir c menyebut log tanpa menyebut permukaan; spec mengasersi Tab Changelog. Post Condition TC-FA-SU-258 dan 259 (state baris, tiga permukaan log, Settings > Role & Permission) tidak punya langkah observasi tambahan di TC dan tidak diasersi.
