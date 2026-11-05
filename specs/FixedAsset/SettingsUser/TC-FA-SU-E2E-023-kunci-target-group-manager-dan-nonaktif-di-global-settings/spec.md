---
id: TC-FA-SU-E2E-023-kunci-target-group-manager-dan-nonaktif-di-global-settings
title: "Kunci Target: Group Manager dan Nonaktif di Global Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-73
  - TC-FA-SU-74
coverage:
  web: automated
---

# Kunci Target: Group Manager dan Nonaktif di Global Settings

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Qori Akbar, Pre-setup #4); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Manage global user & role (Update) | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Nama env `FA_MURG_UPD_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), tier dan penugasan (#23: Oscar Pranata Group Manager IT Infrastructure dan Accounts Payable dengan Group Role Manage group penuh C/R/U/D pada kedua grup, beserta baris pola Group Manager: Group Role katalog dan Transaction Role Asset Admin dan Approver pada kedua grup dan turunannya), Global Settings (#38: Rudi Hartono nonaktif di Global Settings, sakelar FAMS ON). Rudi Hartono menjadi target aksi ubah state di Global Settings (TC-FA-SU-74); data itu data Pre-setup yang tidak dapat dimiliki spec karena kondisinya ditetapkan Pre-setup #38, sehingga dipulihkan ke kondisi nonaktif lewat seed API (langkah 41 dan hook `after`). Efeknya (Last Updated Rudi Hartono dan entri audit trail di Global Settings) tidak dibalik.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen; sesi API Principal Automation (Pre-setup #12) untuk mengaktifkan pengguna di Global Settings (kemampuan disediakan tim FE); seed API untuk memulihkan status nonaktif Rudi Hartono; muat ulang halaman (F5) tanpa dialog `Unsaved Changes` karena tidak ada form dirty.
- State global yang diubah: status aktif Rudi Hartono di Global Settings (diaktifkan pada langkah 36, dipulihkan pada langkah 41 dan hook `after`).

## Test Steps

### TC-FA-SU-73: Target Group Manager, hanya baris pola Group Role dan Transaction Role pada node GM dan turunannya yang terkunci

1. Ketik Search `Oscar Pranata`, tekan Enter
2. Verifikasi sakelar Active baris Oscar Pranata Enabled
3. Buka Detail Oscar Pranata lalu Tab Role (Sub-tab Group Role)
4. Verifikasi baris Group Role pada IT Infrastructure tampil
5. Hover checkbox C/R/U/D baris Group Role IT Infrastructure
6. Verifikasi checkbox C/R/U/D baris IT Infrastructure Disabled dengan tooltip `You don't have permission to edit.`
7. Verifikasi ikon hapus baris IT Infrastructure Disabled
8. Verifikasi `[Assign Group]` dan `[Detail]` Enabled
9. Klik `[Assign Group]`
10. Verifikasi node IT Infrastructure dan Accounts Payable di pemilih grup popup Assign Group Role Disabled (role dengan baris pola terkunci)
11. Tutup popup Assign Group Role dengan ✕
12. Verifikasi checkbox C/R/U/D baris pola Group Role Accounts Payable Disabled
13. Buka Sub-tab Global Role
14. Verifikasi switch dan checkbox C/R/U/D Global Role Enabled
15. Buka Sub-tab Transaction Role
16. Hover row action `Remove` dan checkbox baris pola Approver
17. Verifikasi row action `Remove` dan checkbox baris pola Asset Admin dan Approver (IT Infrastructure dan Accounts Payable) Disabled dengan tooltip `You don't have permission to edit.`
18. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
19. Buka Settings > User dari sidebar
20. Ketik Search `Oscar Pranata`, tekan Enter
21. Buka Detail Oscar Pranata lalu Tab Role (Sub-tab Group Role)
22. Verifikasi checkbox C/R/U/D baris Group Role IT Infrastructure Enabled
23. Verifikasi ikon hapus baris IT Infrastructure Enabled

### TC-FA-SU-74: Target nonaktif di Global Settings, sakelar terkunci untuk semua aktor

24. Buka Settings > User dari sidebar
25. Ketik Search `Rudi Hartono`, tekan Enter
26. Hover sakelar Active baris Rudi Hartono
27. Verifikasi sakelar Active ON Disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
28. Buka Detail Rudi Hartono
29. Hover sakelar Active pada header Detail Rudi Hartono
30. Verifikasi sakelar Active pada header Detail ON Disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
31. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
32. Buka Settings > User dari sidebar
33. Ketik Search `Rudi Hartono`, tekan Enter
34. Hover sakelar Active baris Rudi Hartono
35. Verifikasi sakelar Active ON Disabled dengan tooltip `This user is inactive in Global Settings. Contact a Global Settings admin to reactivate.`
36. Aktifkan Rudi Hartono di Global Settings lewat sesi API Principal Automation hingga pengaktifan tersimpan
37. Muat ulang halaman dengan F5
38. Ganti isi kotak search dengan `Rudi Hartono`, tekan Enter
39. Verifikasi sakelar Active baris Rudi Hartono Enabled
40. Verifikasi sakelar Active baris Rudi Hartono ON
41. Pulihkan Rudi Hartono menjadi nonaktif di Global Settings lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec ditulis per blok role: langkah tiap aktor berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Spec melewati sekitar 35 langkah (41 langkah). Alasan: seluruh blok satu kelas (fungsional kunci target), kedua TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap TC memakai dua aktor dengan ganti akun eksplisit.
- Urutan: TC-FA-SU-74 di akhir karena mengubah state Global Settings (S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 1, 20, 25, 33, 38 (R-16); langkah 11 (menutup popup Assign Group Role), langkah 16 (hover untuk membaca tooltip, S-09); langkah 19, 24, 32 (membuka Settings > User); langkah 37 (muat ulang halaman, langkah TC); langkah 41 (pemulihan state, S-09).
- Langkah 4 adalah anchor positif untuk asersi Disabled pada baris IT Infrastructure (langkah 6 dan 7); Hidden tidak dipakai di spec ini sehingga tidak ada asersi absence.
- Langkah 36 memicu pelaku kedua (Principal Automation) lewat sesi API sehingga bukan konteks kedua kelas c dan tidak memakai `P-2`. Langkah 37 memuat ulang halaman sesudah toggle di Global Settings supaya User List membaca status terbaru.
- Temuan untuk QA:
  - TC-FA-SU-73 Expected e menyebut Total Control dan Default User tetap dapat mengedit baris tersebut; langkah TC hanya memuat Total Control dan Manage global user & role. Spec mengasersi Total Control saja (langkah 22 dan 23); Default User tidak diasersi karena tidak ada langkah login Default User.
  - TC-FA-SU-73 Expected a menyebut ikon hapus baris Disabled tanpa tooltip; hanya state Disabled yang diasersi. Baris pola Accounts Payable hanya diasersi Disabled pada checkbox (tanpa hover tooltip); node IT Infrastructure dan Accounts Payable di pemilih grup (Expected b) diasersi dalam satu Verifikasi. Expected d (baris non-pola, mis. Group Role Manage user & role, dan penugasan di luar subtree penugasan GM) tidak diasersi karena Pre-setup #23 tidak memuat penugasan itu untuk Oscar Pranata. `[+ Assign]` di Sub-tab Transaction Role tidak lagi diasersi Enabled karena Expected terbaru tidak menyebutnya. TC tidak menyebut pengganti `[Detail]` yang diklik; `[Detail]` hanya diasersi Enabled.
  - TC-FA-SU-74 langkah 3 ("Aktifkan Rudi di Global Settings lalu muat ulang") tidak menyebut pelaku; spec memakai Principal Automation (S-13). TC-FA-SU-74 Expected b menyebut "Total Control dan Manage user & role" sedangkan Data Uji aktor adalah Total Control dan Manage global user & role (Pre-setup #4); spec memakai Qori Akbar. TC-FA-SU-74 Expected c ("posisi ON yang sama") dibaca sebagai sakelar Active ON sesudah diaktifkan (langkah 40).
  - Email akun #4 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
