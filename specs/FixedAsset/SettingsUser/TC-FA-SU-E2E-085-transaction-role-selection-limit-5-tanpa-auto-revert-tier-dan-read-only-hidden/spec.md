---
id: TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden
title: "Transaction Role: Selection Limit 5, Tanpa Auto-Revert Tier, dan Read Only Hidden"
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

# Transaction Role: Selection Limit 5, Tanpa Auto-Revert Tier, dan Read Only Hidden

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
- Data uji: Selection Limit 5 (TC-FA-SU-270); Transfer × Asset Admin pada Finance & Accounting untuk Lina Marlina (TC-FA-SU-274).
- Kemampuan teknis: Principal Automation (Pre-setup #12) mengubah Selection Limit tenant `FaUserMain` menjadi 5 sebelum TC-FA-SU-270 dan memulihkannya sesudahnya (akun atau kemampuan "disediakan tim FE", S-13); seed API untuk memulihkan Transaction Role Lina Marlina ke Pre-setup #39 (disediakan tim FE/BE).
- State global yang diubah: Selection Limit tenant `FaUserMain` (dipulihkan pada langkah penghubung sesudah TC-FA-SU-270 dan di hook `after`) dan Transaction Role Lina Marlina (dipulihkan lewat seed API di hook `after`). Suite berjalan serial.
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

### TC-FA-SU-274: Transaction Role tidak memicu Auto-Revert tier pada target Total Control

10. Ganti akun: logout lalu login sebagai Default User Ahmad Dahlan
11. Buka Detail Lina Marlina > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting, Transaction Transfer, dan Role Asset Admin
12. Klik `[Submit]`
13. Verifikasi tidak ada dialog Auto-Revert
14. Verifikasi banner Total Control tidak tampil di Sub-tab Transaction Role
15. Verifikasi tier Total Control Lina Marlina tidak terlepas

### TC-FA-SU-275: Read Only: kontrol tulis Sub-tab Transaction Role Hidden dan kolom checkbox tidak dirender

16. Ganti akun: logout lalu login sebagai Read Only Citra Lestari
17. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
18. Verifikasi Search, Filter, dan tabel tetap tampil
19. Verifikasi tombol `[+ Assign]`, aksi `[Assign Group]`, `Remove`, dan `[Bulk Remove]` Hidden
20. Verifikasi kolom checkbox baris dan header tidak dirender

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 8 dan 9. Selection Limit dipulihkan segera setelah TC-FA-SU-270 karena TC berikutnya tidak membutuhkannya (S-09).
- Temuan untuk QA:
  - TC-FA-SU-270 langkah 1 menyebut "tenant `FaUserMain` dengan Selection Limit 5" sedangkan Pre-setup #36 mendefinisikan `FaUserSel` (limit 100) dan varian `FaUserMain` (limit 5) tanpa menyebut cara menurunkan limit; spec menulisnya sebagai kemampuan "disediakan tim FE" lewat Principal Automation.
  - TC-FA-SU-274 menyebut Ahmad Dahlan "Default User, Total Control selain Lina Marlina" tanpa Expected untuk toast dan log; spec tidak mengasersi toast. Post Condition TC-FA-SU-274 (Lina tetap Total Control, entri `Assign`) tidak punya langkah observasi tambahan di TC selain yang diasersi dan tidak diasersi lagi.
  - TC-FA-SU-275 butir a mengasersi elemen `Hidden`; anchor positifnya adalah Search, Filter, dan tabel yang tampil (bagian 8b butir 2).
