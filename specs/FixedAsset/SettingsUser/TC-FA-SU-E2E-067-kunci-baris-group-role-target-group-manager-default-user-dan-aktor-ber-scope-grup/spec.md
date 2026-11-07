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
- Pengguna target: Oscar Pranata (Group Manager IT Infrastructure dan Accounts Payable dengan Group Role `Manage group` penuh; Pre-setup #9; baris pola Group Manager Group Role katalog dan Transaction Role Asset Admin dan Approver termaterialisasi pada kedua grup dan turunannya, FARP-LOGIC-04i/04j) untuk TC-FA-SU-218 dan 219; Budi Santoso untuk TC-FA-SU-220: Group Role `Manage group` pada Finance & Accounting (dalam scope Sinta Dewi) dan Branch Surabaya (di luar scope), disetel lewat seed API karena Pre-setup #23 hanya memuat Finance & Accounting untuk Budi Santoso (lihat Temuan untuk QA).
- Kemampuan teknis: seed API untuk menyetel dan memulihkan penugasan `Manage group` Budi Santoso (disediakan tim FE/BE).
- State global yang diubah: penugasan `Manage group` Budi Santoso (TC-FA-SU-220 menyimpan perubahan dalam scope); dipulihkan lewat seed API pada langkah penghubung dan di hook `after`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### Total Control Lina Marlina (TC-FA-SU-219 dan TC-FA-SU-221 butir b)

1. Ketik Search `Oscar Pranata`, tekan Enter, lalu buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
2. Verifikasi checkbox CRUD dan ikon hapus pada baris IT Infrastructure Enabled bagi Total Control
3. Klik `[+ Assign Group]` untuk membuka popup Select Group
4. Verifikasi node IT Infrastructure Enabled (Disabled hanya bila sudah ter-assign) bagi Total Control
5. Verifikasi Total Control melihat seluruh pohon entitas
6. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
7. Klik Sub-tab Transaction Role
8. Verifikasi row action `Remove` dan checkbox baris pola Transaction Role Oscar di Sub-tab Transaction Role Enabled bagi Total Control

### Default User Ahmad Dahlan (TC-FA-SU-219 dan TC-FA-SU-221 butir b)

9. Ganti akun: logout lalu login sebagai Default User Ahmad Dahlan
10. Buka Settings > User lewat sidebar, ketik Search `Oscar Pranata`, tekan Enter, lalu buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
11. Verifikasi checkbox CRUD dan ikon hapus pada baris IT Infrastructure Enabled bagi Default User
12. Klik `[+ Assign Group]` untuk membuka popup Select Group
13. Verifikasi node IT Infrastructure Enabled (Disabled hanya bila sudah ter-assign) bagi Default User
14. Verifikasi Default User melihat seluruh pohon entitas
15. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
16. Klik Sub-tab Transaction Role
17. Verifikasi row action `Remove` dan checkbox baris pola Transaction Role Oscar di Sub-tab Transaction Role Enabled bagi Default User

### Manage global user & role (Update) Qori Akbar (TC-FA-SU-218)

18. Ganti akun: logout lalu login sebagai Manage global user & role (Update) Qori Akbar
19. Buka Settings > User lewat sidebar, ketik Search `Oscar Pranata`, tekan Enter, lalu buka Detail Oscar Pranata > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
20. Hover checkbox CRUD pada baris IT Infrastructure
21. Verifikasi checkbox CRUD baris IT Infrastructure Disabled dengan tooltip "You don't have permission to edit."
22. Hover ikon hapus pada baris IT Infrastructure
23. Verifikasi ikon hapus baris IT Infrastructure Disabled dengan tooltip "You don't have permission to edit."
24. Klik `[+ Assign Group]` untuk membuka popup Select Group lalu hover node IT Infrastructure
25. Verifikasi node IT Infrastructure di popup Select Group role Manage group (baris pola terkunci) Disabled dengan tooltip "You don't have permission to edit."
26. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
27. Buka popup Assign Group Role Manage user & role Oscar
28. Klik `[+ Assign Group]` untuk membuka popup Select Group
29. Verifikasi node IT Infrastructure di popup Select Group role Manage user & role (baris non-pola) dapat dipilih
30. Klik `[Cancel]` pada popup Select Group lalu klik `[✕]` pada popup Assign Group Role
31. Klik Sub-tab Transaction Role
32. Hover row action `Remove` dan checkbox baris pola Approver
33. Verifikasi row action `Remove` baris pola Approver Disabled dengan tooltip "You don't have permission to edit."
34. Verifikasi checkbox baris pola Asset Admin dan Approver (IT Infrastructure dan Accounts Payable) Disabled dengan tooltip "You don't have permission to edit."
35. Verifikasi Global Role, penugasan di luar subtree penugasan Group Manager, `[Assign Group]`, `[Detail]`, dan sakelar Active Oscar tidak terkunci

### Manage user & role Group (Update, Finance & Accounting) Sinta Dewi (TC-FA-SU-220 dan TC-FA-SU-221 butir a)

36. Setel penugasan Manage group Budi Santoso pada Finance & Accounting dan Branch Surabaya lewat seed API
37. Ganti akun: logout lalu login sebagai Manage user & role Group (Update, Finance & Accounting) Sinta Dewi
38. Buka Settings > User lewat sidebar, ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Role > Sub-tab Group Role lalu buka popup Assign Group Role Manage group
39. Verifikasi baris grup di luar scope (Branch Surabaya) tetap tampil dengan checkbox C/R/U/D dan ikon hapus Disabled dengan tooltip "You don't have permission to edit."
40. Klik `[+ Assign Group]` untuk membuka popup Select Group
41. Verifikasi Select Group memuat Finance & Accounting dan Accounts Payable saja
42. Klik `[Cancel]` pada popup Select Group
43. Klik `[Clear Field]`
44. Verifikasi `[Clear Field]` hanya mengosongkan baris dalam scope (Finance & Accounting)
45. Verifikasi baris terkunci Branch Surabaya dipertahankan
46. Klik `[Save]`
47. Verifikasi kolom Group baris Manage group Budi Santoso hanya memuat Branch Surabaya (hanya perubahan baris dalam scope yang tersimpan)
48. Pulihkan penugasan Manage group Budi Santoso ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan blok ke id TC granular untuk report per langkah. Blok disusun per akun (bukan per TC) supaya tiap akun login satu kali: asersi TC-FA-SU-221 butir b (Total Control dan Default User melihat seluruh pohon) dijalankan pada popup Select Group yang sama dengan TC-FA-SU-219, dan asersi TC-FA-SU-221 butir a pada popup Sinta Dewi sebelum Clear Field TC-FA-SU-220.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a, `[KEPUTUSAN 2026-10-30]`); judulnya tanpa kata Positif atau Negatif.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 6, 15, 26, 36, 42 dan 48. Penutupan popup tanpa perubahan tidak memunculkan dialog; popup Select Group ditutup dengan `[Cancel]`.
- Jumlah langkah 48, di atas smell 35 langkah karena ganti akun eksplisit untuk empat role (bagian 3a) dan penutupan popup antar blok; seluruh blok satu topik (kunci baris Group Role per aktor) dan satu kelas harness, dan kegagalan satu blok role tidak membuat blok role lain kehilangan makna.
- Langkah penghubung Search (S-03): Search nama pengguna target pada langkah 1, 10, 19 dan 38 digabung ke langkah pembuka Detail atau pembacaan baris, untuk menemukan baris target di User List yang memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah berikutnya mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9). Langkah 10, 19 dan 38 juga membuka Settings > User lewat sidebar karena langkah sebelumnya adalah Ganti akun (S-14).
- Temuan untuk QA:
  - Langkah penghubung tambahan: 7, 16, 27, 28, 30, 31, dan 32 (membuka sub-tab, popup, dan hover; S-09).
  - TC-FA-SU-218 langkah 5 meminta popup Assign Group Role `Manage user & role` Oscar sebagai contoh baris non-pola; Pre-setup #23 tidak merinci apakah Oscar Pranata memegang role itu (perlu dijamin seed).
  - TC-FA-SU-218 Expected e (penugasan di luar subtree) tidak punya data uji pada Pre-setup #23 untuk Oscar Pranata; spec mengasersi Global Role, `[Assign Group]`, `[Detail]`, dan sakelar Active saja.
  - TC-FA-SU-219 dan 221 menyebut "Default User" pada Expected tetapi langkah TC hanya login sebagai Total Control; spec menambahkan blok Default User berdasar Expected.
  - TC-FA-SU-219 butir b ("node IT Infrastructure Enabled dan Disabled hanya bila sudah ter-assign") tidak menyebut apakah IT Infrastructure sudah ter-assign pada role yang dibuka (Oscar memegangnya pada `Manage group`, sehingga node berpotensi Disabled); spec mengasersi sesuai teks TC.
  - TC-FA-SU-220 menyebut "grup di dalam dan di luar scope" untuk Budi Santoso, tetapi Pre-setup #23 hanya memuat Group Role `Manage group` pada Finance & Accounting; spec menyetel Branch Surabaya sebagai grup di luar scope lewat seed API.
  - TC-FA-SU-220 butir c ("hanya menyimpan perubahan baris dalam scope") tidak menyebut toast; spec mengasersi kolom Group setelah Save.
  - TC-FA-SU-218 butir e tidak menyebut lokasi pengamatan elemen yang tidak terkunci; spec mengasersinya pada halaman Detail sesudah popup ditutup.
