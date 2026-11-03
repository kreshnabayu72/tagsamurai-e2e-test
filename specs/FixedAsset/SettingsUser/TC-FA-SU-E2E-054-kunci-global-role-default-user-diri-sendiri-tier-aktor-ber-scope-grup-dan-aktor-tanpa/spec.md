---
id: TC-FA-SU-E2E-054-kunci-global-role-default-user-diri-sendiri-tier-aktor-ber-scope-grup-dan-aktor-tanpa
title: "Kunci Global Role: Default User, Diri Sendiri, Tier, Aktor Ber-scope Grup, dan Aktor Tanpa Izin"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-182
  - TC-FA-SU-184
  - TC-FA-SU-185
coverage:
  web: automated
---

# Kunci Global Role: Default User, Diri Sendiri, Tier, Aktor Ber-scope Grup, dan Aktor Tanpa Izin

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (hook `before`): Manage global user & role (Update) Qori Akbar (Pre-setup #4). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Kredensial `Spectra.env.FA_MURG_UPD_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07): langkah 16 Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; email disediakan tim FE; `Spectra.env.FA_MURGR_UPD_PASSWORD`); langkah 24 Read Only Citra Lestari (Pre-setup #3) `readOnly_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_RO_PASSWORD`); langkah 32 Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_TC_PASSWORD`); langkah 35 Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_DU_PASSWORD`).
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; pohon grup #21; penugasan #23): target Ahmad Dahlan (Default User), Qori Akbar (akun sendiri), Lina Marlina (Total Control), Citra Lestari (Read Only), dan Gita Permata. Semua blok hanya membaca: tidak ada penugasan yang diubah, sehingga tidak ada pemulihan.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP dengan token sesi aktor (Sinta Dewi) untuk permintaan langsung (langkah 22); pencatat request jaringan halaman (langkah 31).
- State global dan pemulihan: sesi dikembalikan ke akun default suite di hook `after`; tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-182: Kunci Global Role bagi Default User, diri sendiri, dan target tier (aktor Qori Akbar)

1. Ketik Search `Ahmad`, tekan Enter di User List, klik nama Ahmad Dahlan, lalu buka Tab Role > Sub-tab Global Role
2. Hover switch pada baris Manage accounting
3. Verifikasi switch Manage accounting Disabled dengan tooltip "Default User cannot be modified."
4. Hover checkbox Update pada baris Manage accounting
5. Verifikasi checkbox Update Manage accounting Disabled dengan tooltip "Default User cannot be modified."
6. Kembali ke User List, ketik Search `Qori`, tekan Enter, klik nama Qori Akbar (akun sendiri), lalu buka Tab Role > Sub-tab Global Role
7. Hover switch pada baris Manage accounting
8. Verifikasi switch Manage accounting Disabled dengan tooltip "You can't manage your own account from here."
9. Hover checkbox Update pada baris Manage accounting
10. Verifikasi checkbox Update Manage accounting Disabled dengan tooltip "You can't manage your own account from here."
11. Kembali ke User List, ketik Search `Lina`, tekan Enter, klik nama Lina Marlina (Total Control), lalu buka Tab Role > Sub-tab Global Role
12. Hover switch pada baris Manage accounting
13. Verifikasi switch Manage accounting Disabled dengan tooltip "You don't have permission to edit."
14. Hover checkbox Update pada baris Manage accounting
15. Verifikasi checkbox Update Manage accounting Disabled dengan tooltip "You don't have permission to edit."

### TC-FA-SU-184: Aktor Manage user & role Group tidak dapat mengubah Global Role target

16. Ganti akun: logout, login sebagai Sinta Dewi (`Spectra.env.FA_MURGR_UPD_PASSWORD`), lalu buka Fixed Asset > Settings > User
17. Ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
18. Hover switch pada baris Manage accounting
19. Verifikasi switch Manage accounting Disabled dengan tooltip "You don't have permission to edit."
20. Hover checkbox Update pada baris Manage accounting
21. Verifikasi checkbox Update Manage accounting Disabled dengan tooltip "You don't have permission to edit."
22. Kirim permintaan langsung ke API ubah switch Global Role Gita Permata memakai klien HTTP dengan token sesi Sinta Dewi
23. Verifikasi server menolak permintaan langsung dengan status 403

### TC-FA-SU-185: Read Only dan Manage user & role tanpa Update

24. Ganti akun: logout, login sebagai Read Only Citra Lestari (`Spectra.env.FA_RO_PASSWORD`), lalu buka Fixed Asset > Settings > User
25. Ketik Search `Gita`, tekan Enter, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
26. Hover switch pada baris Manage accounting
27. Verifikasi switch Manage accounting Disabled dengan tooltip "You don't have permission to edit."
28. Hover checkbox Update pada baris Manage accounting
29. Verifikasi checkbox Update Manage accounting Disabled dengan tooltip "You don't have permission to edit."
30. Klik switch pada baris Manage accounting
31. Verifikasi tidak ada request ubah Global Role yang terkirim ke server

### TC-FA-SU-182 (butir d): Total Control dan Default User tetap dapat mengedit target tier

32. Ganti akun: logout, login sebagai Total Control Lina Marlina (`Spectra.env.FA_TC_PASSWORD`), lalu buka Fixed Asset > Settings > User
33. Ketik Search `Citra`, tekan Enter, klik nama Citra Lestari (Read Only), lalu buka Tab Role > Sub-tab Global Role
34. Verifikasi switch dan checkbox C/R/U/D baris Manage accounting Enabled bagi Total Control
35. Ganti akun: logout, login sebagai Default User Ahmad Dahlan (`Spectra.env.FA_DU_PASSWORD`), lalu buka Fixed Asset > Settings > User
36. Ketik Search `Citra`, tekan Enter, klik nama Citra Lestari (Read Only), lalu buka Tab Role > Sub-tab Global Role
37. Verifikasi switch dan checkbox C/R/U/D baris Manage accounting Enabled bagi Default User

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Urutan: butir d TC-FA-SU-182 (Total Control dan Default User) diasersi di akhir karena membutuhkan dua kali ganti akun; ganti akun dikelompokkan per aktor supaya login hanya berpindah satu kali per aktor.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 6, 11, 17, 25, 33, dan 36 (Search untuk menemukan baris target, R-16), langkah 16, 24, 32, dan 35 (ganti akun eksplisit, S-07).
- K-1 dan bagian 8b butir 1: langkah 22 sampai 23 adalah permintaan langsung ke server (TC-FA-SU-184 Langkah Uji 4); asersinya hanya status respons 403, bukan tampilan UI. Tidak ada state data tambahan yang disebut Expected TC-FA-SU-184.
- Asersi tambahan di luar Expected TC: langkah 34 dan 37 memakai aktor dan target yang dipilih penulis (Lina dan Ahmad terhadap Citra Lestari) karena Expected d TC-FA-SU-182 tidak menyebutnya di Langkah Uji; langkah 31 menerjemahkan "klik tidak mengirim request" pada Expected b TC-FA-SU-185.
- Spec ini 37 langkah. Alasan melewati sekitar 35 langkah: seluruh blok satu topik (kunci Global Role bagi aktor tanpa izin) yang hanya membaca dengan target yang sama; tiap blok berdiri sendiri dan tidak ada state yang diubah.
- Temuan untuk QA:
  - Email dan password Qori Akbar (#4) dan Sinta Dewi (#6) tidak tertulis di Pre-setup TC; disediakan tim FE (S-11, S-13).
  - Judul TC-FA-SU-185 menyebut "Read Only dan Manage user & role tanpa Update", tetapi Langkah Uji hanya login sebagai Read Only; kombinasi Manage global user & role (Read saja) (#5) tidak punya langkah dan tidak diasersi.
  - Expected d TC-FA-SU-182 menyebut Total Control dan Default User mengedit target tier tanpa langkah login untuk keduanya di Langkah Uji; spec menambah langkah 32 sampai 37 dan mencatatnya di sini (S-03, S-15).
  - Expected b TC-FA-SU-184 menyebut request langsung ditolak 403 tanpa menyebut state data; tidak ada asersi state data dan tidak ada entri log yang disebut.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
