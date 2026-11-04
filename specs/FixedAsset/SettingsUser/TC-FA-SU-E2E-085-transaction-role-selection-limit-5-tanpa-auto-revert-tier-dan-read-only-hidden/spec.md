---
id: TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden
title: "Transaction Role: Selection Limit 5, Auto-Revert Tier dari Remove Baris Pola, dan Read Only Hidden"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-270
  - TC-FA-SU-274
  - TC-FA-SU-275
coverage:
  web: automated
---

# Transaction Role: Selection Limit 5, Auto-Revert Tier dari Remove Baris Pola, dan Read Only Hidden

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang diganti secara eksplisit di langkah:

| Role | Akun | Email | Kredensial |
|---|---|---|---|
| Default User | Ahmad Dahlan (Pre-setup #2) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| Read Only | Citra Lestari (Pre-setup #3) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan penugasan (Pre-setup #23) dan Transaction Role (Pre-setup #39); varian `FaUserMain` dengan Selection Limit 5 (Pre-setup #36).
- Pengguna target: Yuda Pratama (7 baris Transaction Role) untuk TC-FA-SU-270; Lina Marlina (Total Control dengan Transaction Role) untuk TC-FA-SU-274; Mira Anggraini untuk TC-FA-SU-275.
- Data uji: Selection Limit 5 (TC-FA-SU-270); baris Transfer × Approver pada Finance & Accounting milik Lina Marlina yang di-Remove (TC-FA-SU-274).
- Kemampuan teknis: Principal Automation (Pre-setup #12) mengubah Selection Limit tenant `FaUserMain` menjadi 5 sebelum TC-FA-SU-270 dan memulihkannya sesudahnya (akun atau kemampuan "disediakan tim FE", S-13); seed API untuk memulihkan Transaction Role Lina Marlina ke Pre-setup #39 (disediakan tim FE/BE).
- State global yang diubah: Selection Limit tenant `FaUserMain` (dipulihkan pada langkah penghubung sesudah TC-FA-SU-270 dan di hook `after`) serta Transaction Role dan tier Total Control Lina Marlina (dipulihkan ke Pre-setup #23 dan #39 lewat seed API pada langkah penghubung dan di hook `after`). Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-270: Select All dan Selection Limit pada Sub-tab Transaction Role: auto-cap, toast, dan checkbox Disabled setelah limit

1. Ubah Selection Limit tenant FaUserMain menjadi 5 lewat Principal Automation
2. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role lalu klik Select All
3. Verifikasi Select All hanya menghitung baris yang dapat dihapus aktor dan tombol berganti `[Unselect All]`
4. Verifikasi 5 baris pertama terpilih (dipotong ke Selection Limit)
5. Verifikasi toast "Error, only the first 5 of 7 rows were selected. Narrow your filter to include the rest."
6. Hover checkbox baris ke-6
7. Verifikasi checkbox baris ke-6 Disabled dengan tooltip "You've reached the maximum selection of 5 rows."
8. Klik `[Unselect All]`
9. Pulihkan Selection Limit tenant FaUserMain ke nilai awal lewat Principal Automation

### TC-FA-SU-274: Remove baris pola Transaction Role target Total Control menyimpang dari pola: dialog Auto-Revert D-05a, tier lepas

10. Ganti akun: logout lalu login sebagai Default User Ahmad Dahlan
11. Buka Detail Lina Marlina > Tab Role > Sub-tab Transaction Role
12. Klik ⋯ pada baris Transfer × Approver pada Finance & Accounting lalu klik `Remove`
13. Verifikasi dialog Auto-Revert D-05a (bukan dialog Remove Transaction Role) dengan Title `Remove Total Control`
14. Verifikasi Body bullet `• Lina Marlina`
15. Verifikasi kalimat `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`
16. Verifikasi penutup `Are you sure you want to remove it?`
17. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
18. Klik `[Remove]`
19. Verifikasi toast sukses auto-revert (T-06a) tampil
20. Verifikasi baris Transfer × Approver pada Finance & Accounting terhapus
21. Verifikasi tingkat akses Total Control Lina Marlina terlepas
22. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Transaction Role
23. Klik Sub-tab Global Role
24. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Global Role
25. Klik Sub-tab Group Role
26. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Group Role
27. Verifikasi baris Transaction Role lain milik Lina Marlina tidak direset
28. Pulihkan Transaction Role dan tier Total Control Lina Marlina ke Pre-setup #23 dan #39 lewat seed API

### TC-FA-SU-275: Read Only: kontrol tulis Sub-tab Transaction Role Hidden dan kolom checkbox tidak dirender

29. Ganti akun: logout lalu login sebagai Read Only Citra Lestari
30. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
31. Verifikasi Search, Filter, dan tabel tetap tampil
32. Verifikasi tombol `[+ Assign]`, aksi `[Assign Group]`, `Remove`, dan `[Bulk Remove]` Hidden
33. Verifikasi kolom checkbox baris dan header tidak dirender

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 8, 9, 23, 25 dan 28. Selection Limit dipulihkan segera setelah TC-FA-SU-270 karena TC berikutnya tidak membutuhkannya (S-09).
- Temuan untuk QA:
  - TC-FA-SU-270 langkah 1 menyebut "tenant `FaUserMain` dengan Selection Limit 5" sedangkan Pre-setup #36 mendefinisikan `FaUserSel` (limit 100) dan varian `FaUserMain` (limit 5) tanpa menyebut cara menurunkan limit; spec menulisnya sebagai kemampuan "disediakan tim FE" lewat Principal Automation.
  - TC-FA-SU-274 langkah 1 menyebut Ahmad Dahlan "Default User, Total Control selain Lina Marlina" sedangkan Pre-setup #2 menyebut Default User; spec memakai Default User. Copy Body dialog D-05a varian Role Transaksi bertanda "copy usulan, perlu persetujuan PM" (PRD 12 #1 `settings-role-permission`); spec mengasersi teks apa adanya.
  - TC-FA-SU-274 Expected d menyebut toast T-06a tanpa teksnya; spec hanya mengasersi toast sukses auto-revert tampil. Post Condition (entri `Remove` dan `Auto-Revert` pada tiga surface log, notifikasi in-app) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-FA-SU-275 butir a mengasersi elemen `Hidden`; anchor positifnya adalah Search, Filter, dan tabel yang tampil (bagian 8b butir 2).
