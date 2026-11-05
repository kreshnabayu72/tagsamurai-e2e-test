---
id: TC-FA-RP-E2E-368-role-matrix-picker-role-transaksi-kandidat-gm-disaring-bagi-group-manager-dan-total-control
title: "Role Matrix: picker Assign Role Transaksi menyaring kandidat Group Manager pada subtree penugasannya bagi Group Manager dan tidak bagi Total Control"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-1196
coverage:
  web: automated
---

# Role Matrix: picker Assign Role Transaksi menyaring kandidat Group Manager pada subtree penugasannya bagi Group Manager dan tidak bagi Total Control

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (berkas belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| Urutan | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| 1 (hook `before`) | Group Manager (`IT Infrastructure`) | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| 2 (ganti akun, langkah 15) | Total Control | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup yang dibaca: #5 (Fajar Nugroho, aktor; Group Manager `IT Infrastructure`), #13 (Kevin Susanto, kandidat; Active, Activated; Group Manager hanya di `Data Center`, tanpa penugasan Monitoring & Report di `Data Center` dan `Helpdesk`), #18 (pohon group Company Alpha; `Data Center` descendant `IT Infrastructure`, `Helpdesk` di luar subtree penugasan Group Manager Kevin Susanto), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`; `Data Center` dan `Helpdesk` tanpa penugasan manual). Seed Group Manager Kevin Susanto beserta baris pola disediakan tim FE/BE (kemampuan seeding API, tanpa endpoint karangan).
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada. Spec tidak membuat, mengubah, atau menghapus data (tanpa data Dinamis); popup `[+ Assign]` ditutup tanpa memilih kandidat. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_GM_PASSWORD` dan `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md`, bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1196: kandidat Group Manager pada node subtree penugasannya disaring dari picker (aktor Group Manager Fajar Nugroho)

1. Klik Tab Transaction Role
2. Klik node `Data Center` di Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Klik `[+ Assign]` pada section Monitoring & Report
5. Verifikasi sedikitnya satu kandidat tampil di daftar picker
6. Ketik Search `Kevin Susanto`, tekan Enter pada popup
7. Verifikasi Kevin Susanto tidak ada di daftar picker
8. Tutup popup tanpa memilih kandidat
9. Klik node `Helpdesk` di Sidebar Group Tree
10. Klik sub-tab `Disposal`
11. Klik `[+ Assign]` pada section Monitoring & Report
12. Ketik Search `Kevin Susanto`, tekan Enter pada popup
13. Verifikasi Kevin Susanto ada di daftar picker
14. Tutup popup tanpa memilih kandidat

### TC-FA-RP-1196: aktor Total Control tidak dibatasi

15. Ganti akun: logout, lalu login sebagai Total Control Siti Rahmawati (Pre-setup #2)
16. Buka Fixed Asset > Settings > Role & Permission > Transaction Role
17. Klik node `Data Center` di Sidebar Group Tree
18. Klik sub-tab `Disposal`
19. Klik `[+ Assign]` pada section Monitoring & Report
20. Ketik Search `Kevin Susanto`, tekan Enter pada popup
21. Verifikasi Kevin Susanto ada di daftar picker
22. Tutup popup tanpa memilih kandidat

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 22 langkah.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (S-07; akun pertama login di hook `before`). Spec memuat matriks visibilitas (kandidat tidak ada bagi Group Manager, ada bagi Total Control dan pada node di luar subtree), maka title tanpa kata "Positif" atau "Negatif"; `caseType` Negative mengikuti jenis alur utama (penyaringan kandidat).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab (langkah 1 sampai 3, 9, 10, 16 sampai 18); menutup popup tanpa memilih kandidat (langkah 8, 14, 22); ganti akun (langkah 15); membuka layar Transaction Role sesudah login (langkah 16, S-07 dan S-14).
- Search (R-16, R-22): langkah 6, 12, dan 20 adalah langkah penghubung untuk menemukan kandidat Kevin Susanto di popup, karena daftar picker berpaginasi. Langkah 5 adalah anchor positif tambahan di luar TC (bagian 8b butir 2): membuktikan daftar picker sudah termuat sebelum asersi absence langkah 7.
- Pembagian TC lintas spec: TC-FA-RP-1196 hanya ada di spec ini.
- Temuan untuk QA:
  - TC-FA-RP-1196 langkah 3 menyebut "Login sbg Role: Total Control" tanpa Pre-setup; spec memakai Total Control default suite (Siti Rahmawati, Pre-setup #2, `FA_TC_PASSWORD`).
  - TC-FA-RP-1196 tidak menyebut cara menutup popup; spec menulis "Tutup popup tanpa memilih kandidat" sebagai langkah penghubung.
  - TC-FA-RP-1196 Precondition d menyebut Kevin Susanto Group Manager hanya di `Data Center` (Pre-setup #13 dan #43), sedangkan Pre-setup #38 menyebut Group Manager di `Data Center` dan `Helpdesk`. Spec memakai #13 dan #43; bila #38 yang berlaku, `Helpdesk` berada di subtree penugasan dan Expected b tidak terpenuhi.
  - TC-FA-RP-1196 tidak menyebut nilai Search di popup; spec memakai nama Kevin Susanto.
