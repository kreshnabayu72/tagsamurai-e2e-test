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
2. Ketik Search `Yuda Pratama`, tekan Enter, lalu buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role lalu klik Select All
3. Verifikasi Select All hanya menghitung baris yang dapat dihapus aktor dan tombol berganti `[Unselect All]`
4. Verifikasi 5 baris pertama terpilih (dipotong ke Selection Limit)
5. Verifikasi toast "Error, only the first 5 of 7 rows were selected. Narrow your filter to include the rest."
6. Hover checkbox baris ke-6
7. Verifikasi checkbox baris ke-6 Disabled dengan tooltip "You've reached the maximum selection of 5 rows."
8. Klik `[Unselect All]`
9. Pulihkan Selection Limit tenant FaUserMain ke nilai awal lewat Principal Automation

### TC-FA-SU-274: Remove baris pola Transaction Role target Total Control menyimpang dari pola: dialog Auto-Revert D-05a, tier lepas

10. Ganti akun: logout lalu login sebagai Default User Ahmad Dahlan
11. Buka Settings > User dari sidebar
12. Ketik Search `Lina Marlina`, tekan Enter, lalu buka Detail Lina Marlina > Tab Role > Sub-tab Transaction Role
13. Klik ⋯ pada baris Transfer × Approver pada Finance & Accounting lalu klik `Remove`
14. Verifikasi dialog Auto-Revert D-05a (bukan dialog Remove Transaction Role) dengan Title `Remove Total Control`
15. Verifikasi Body bullet `• Lina Marlina`
16. Verifikasi kalimat `This change will remove this user's Total Control access level. Their other role assignments will remain as they are.`
17. Verifikasi penutup `Are you sure you want to remove it?`
18. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil
19. Klik `[Remove]`
20. Verifikasi toast sukses auto-revert (T-06a) tampil
21. Verifikasi baris Transfer × Approver pada Finance & Accounting terhapus
22. Verifikasi tingkat akses Total Control Lina Marlina terlepas
23. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Transaction Role
24. Klik Sub-tab Global Role
25. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Global Role
26. Klik Sub-tab Group Role
27. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Group Role
28. Verifikasi baris Transaction Role lain milik Lina Marlina tidak direset
29. Pulihkan Transaction Role dan tier Total Control Lina Marlina ke Pre-setup #23 dan #39 lewat seed API

### TC-FA-SU-275: Read Only: kontrol tulis Sub-tab Transaction Role Hidden dan kolom checkbox tidak dirender

30. Ganti akun: logout lalu login sebagai Read Only Citra Lestari
31. Buka Settings > User dari sidebar
32. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
33. Verifikasi Search, Filter, dan tabel tetap tampil
34. Verifikasi tombol `[+ Assign]`, aksi `[Assign Group]`, `Remove`, dan `[Bulk Remove]` Hidden
35. Verifikasi kolom checkbox baris dan header tidak dirender

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 8, 9, 11, 24, 26, 29 dan 31 (langkah 11 dan 31 membuka Settings > User dari sidebar sesudah ganti akun, S-14). Selection Limit dipulihkan segera setelah TC-FA-SU-270 karena TC berikutnya tidak membutuhkannya (S-09).
- Search nama pengguna target pada User List digabung dalam langkah buka Detail (langkah 2, 12 dan 32): langkah penghubung untuk menemukan baris target karena User List memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13).
- Temuan untuk QA:
  - TC-FA-SU-270 langkah 1 menyebut "tenant `FaUserMain` dengan Selection Limit 5" sedangkan Pre-setup #36 mendefinisikan `FaUserSel` (limit 100) dan varian `FaUserMain` (limit 5) tanpa menyebut cara menurunkan limit; spec menulisnya sebagai kemampuan "disediakan tim FE" lewat Principal Automation.
  - TC-FA-SU-274 langkah 1 menyebut Ahmad Dahlan "Default User, Total Control selain Lina Marlina" sedangkan Pre-setup #2 menyebut Default User; spec memakai Default User. Copy Body dialog D-05a varian Role Transaksi bertanda "copy usulan, perlu persetujuan PM" (PRD 12 #1 `settings-role-permission`); spec mengasersi teks apa adanya.
  - TC-FA-SU-274 Expected d menyebut toast T-06a tanpa teksnya; spec hanya mengasersi toast sukses auto-revert tampil. Post Condition (entri `Remove` dan `Auto-Revert` pada tiga surface log, notifikasi in-app) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-FA-SU-275 butir a mengasersi elemen `Hidden`; anchor positifnya adalah Search, Filter, dan tabel yang tampil (bagian 8b butir 2).
