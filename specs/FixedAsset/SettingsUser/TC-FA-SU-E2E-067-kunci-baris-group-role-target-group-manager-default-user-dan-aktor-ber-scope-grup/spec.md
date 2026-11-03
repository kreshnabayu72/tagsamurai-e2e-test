---
id: TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup
title: "Kunci Baris Group Role: Target Group Manager, Default User, dan Aktor Ber-scope Grup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-218
  - TC-FA-SU-219
  - TC-FA-SU-220
  - TC-FA-SU-221
coverage:
  web: automated
---

# Kunci Baris Group Role: Target Group Manager, Default User, dan Aktor Ber-scope Grup

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun yang diganti secara eksplisit di langkah (tabel "Role yang diuji"):

| Role | Akun | Email | Kredensial |
|---|---|---|---|
| Manage global user & role (Update) | Qori Akbar (Pre-setup #4) | disediakan tim FE (tidak tertulis di Pre-setup TC) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Total Control | Lina Marlina (Pre-setup #1) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Default User | Ahmad Dahlan (Pre-setup #2) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| Manage user & role Group (Update, Finance & Accounting) | Sinta Dewi (Pre-setup #6) | disediakan tim FE (tidak tertulis di Pre-setup TC) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |

- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable dengan Group Role `Manage group` penuh; Pre-setup #9) untuk TC-FA-SU-218 dan 219; Budi Santoso untuk TC-FA-SU-220: Group Role `Manage group` pada Finance & Accounting (dalam scope Sinta Dewi) dan Branch Surabaya (di luar scope), disetel lewat seed API karena Pre-setup #23 hanya memuat Finance & Accounting untuk Budi Santoso (lihat Temuan untuk QA).
- Kemampuan teknis: seed API untuk menyetel dan memulihkan penugasan `Manage group` Budi Santoso (disediakan tim FE/BE).
- State global yang diubah: penugasan `Manage group` Budi Santoso (TC-FA-SU-220 menyimpan perubahan dalam scope); dipulihkan lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### Total Control Lina Marlina (TC-FA-SU-219 dan TC-FA-SU-221 butir b)

1. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
2. Verifikasi checkbox CRUD dan ikon hapus pada baris IT Infrastructure Enabled bagi Total Control
3. Klik `[+ Assign Group]` untuk membuka popup Select Group
4. Verifikasi node IT Infrastructure Enabled (Disabled hanya bila sudah ter-assign) bagi Total Control
5. Verifikasi Total Control melihat seluruh pohon entitas
6. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role

### Default User Ahmad Dahlan (TC-FA-SU-219 dan TC-FA-SU-221 butir b)

7. Ganti akun: logout lalu login sebagai Default User Ahmad Dahlan
8. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
9. Verifikasi checkbox CRUD dan ikon hapus pada baris IT Infrastructure Enabled bagi Default User
10. Klik `[+ Assign Group]` untuk membuka popup Select Group
11. Verifikasi node IT Infrastructure Enabled (Disabled hanya bila sudah ter-assign) bagi Default User
12. Verifikasi Default User melihat seluruh pohon entitas
13. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role

### Manage global user & role (Update) Qori Akbar (TC-FA-SU-218)

14. Ganti akun: logout lalu login sebagai Manage global user & role (Update) Qori Akbar
15. Buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
16. Hover checkbox CRUD pada baris IT Infrastructure
17. Verifikasi checkbox CRUD baris IT Infrastructure Disabled dengan tooltip "You don't have permission to edit."
18. Hover ikon hapus pada baris IT Infrastructure
19. Verifikasi ikon hapus baris IT Infrastructure Disabled dengan tooltip "You don't have permission to edit."
20. Klik `[+ Assign Group]` untuk membuka popup Select Group lalu hover node IT Infrastructure
21. Verifikasi node IT Infrastructure Disabled dengan tooltip "You don't have permission to edit."
22. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
23. Verifikasi Global Role, Transaction Role, grup lain, `[Assign Group]`, dan `[Detail]` tidak terkunci

### Manage user & role Group (Update, Finance & Accounting) Sinta Dewi (TC-FA-SU-220 dan TC-FA-SU-221 butir a)

24. Setel penugasan Manage group Budi Santoso pada Finance & Accounting dan Branch Surabaya lewat seed API
25. Ganti akun: logout lalu login sebagai Manage user & role Group (Update, Finance & Accounting) Sinta Dewi
26. Buka Detail Budi Santoso > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
27. Verifikasi baris grup di luar scope (Branch Surabaya) tetap tampil dengan checkbox C/R/U/D dan ikon hapus Disabled dengan tooltip "You don't have permission to edit."
28. Klik `[+ Assign Group]` untuk membuka popup Select Group
29. Verifikasi Select Group memuat Finance & Accounting dan Accounts Payable saja
30. Klik `[Cancel]` pada popup Select Group
31. Klik `[Clear Field]`
32. Verifikasi `[Clear Field]` hanya mengosongkan baris dalam scope (Finance & Accounting)
33. Verifikasi baris terkunci Branch Surabaya dipertahankan
34. Klik `[Save]`
35. Verifikasi kolom Group baris Manage group Budi Santoso hanya memuat Branch Surabaya (hanya perubahan baris dalam scope yang tersimpan)
36. Pulihkan penugasan Manage group Budi Santoso ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan blok ke id TC granular untuk report per langkah. Blok disusun per akun (bukan per TC) supaya tiap akun login satu kali: asersi TC-FA-SU-221 butir b (Total Control dan Default User melihat seluruh pohon) dijalankan pada popup Select Group yang sama dengan TC-FA-SU-219, dan asersi TC-FA-SU-221 butir a pada popup Sinta Dewi sebelum Clear Field TC-FA-SU-220.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 6, 13, 22, 24, 30 dan 36. Penutupan popup tanpa perubahan tidak memunculkan dialog; popup Select Group ditutup dengan `[Cancel]`.
- Jumlah langkah 36, di atas smell 35 langkah karena ganti akun eksplisit untuk empat role (bagian 3a) dan penutupan popup antar blok; seluruh blok satu topik (kunci baris Group Role per aktor) dan satu kelas harness, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-219 dan 221 menyebut "Default User" pada Expected tetapi langkah TC hanya login sebagai Total Control; spec menambahkan blok Default User berdasar Expected.
  - TC-FA-SU-219 butir b ("node IT Infrastructure Enabled dan Disabled hanya bila sudah ter-assign") tidak menyebut apakah IT Infrastructure sudah ter-assign pada role yang dibuka (Oscar memegangnya pada `Manage group`, sehingga node berpotensi Disabled); spec mengasersi sesuai teks TC.
  - TC-FA-SU-220 menyebut "grup di dalam dan di luar scope" untuk Budi Santoso, tetapi Pre-setup #23 hanya memuat Group Role `Manage group` pada Finance & Accounting; spec menyetel Branch Surabaya sebagai grup di luar scope lewat seed API.
  - TC-FA-SU-220 butir c ("hanya menyimpan perubahan baris dalam scope") tidak menyebut toast; spec mengasersi kolom Group setelah Save.
  - TC-FA-SU-218 butir c tidak menyebut lokasi pengamatan elemen yang tidak terkunci; spec mengasersinya pada halaman Detail sesudah popup ditutup.
