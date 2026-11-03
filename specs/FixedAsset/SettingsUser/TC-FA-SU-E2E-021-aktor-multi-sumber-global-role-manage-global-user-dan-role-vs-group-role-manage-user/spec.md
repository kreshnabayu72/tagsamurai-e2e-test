---
id: TC-FA-SU-E2E-021-aktor-multi-sumber-global-role-manage-global-user-dan-role-vs-group-role-manage-user
title: "Aktor Multi-sumber: Global Role Manage global user & role vs Group Role Manage user & role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-66
  - TC-FA-SU-67
  - TC-FA-SU-68
coverage:
  web: automated
---

# Aktor Multi-sumber: Global Role Manage global user & role vs Group Role Manage user & role

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Nanda Pratama (Pre-setup #11: Group Role Manage user & role pada Finance & Accounting, Global Role Manage global user & role OFF); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Nanda Pratama (Group Role MUR Finance & Accounting; Global Role MUR OFF) | #11 | Nanda Pratama | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_NANDA_PASSWORD` |
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Manage global user & role (Update) dan Group Manager IT Infrastructure | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |

- Nama env `FA_NANDA_PASSWORD` dan `FA_MURG_UPD_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Client `FaUserMain` dengan 25 pengguna (#20; halaman 1: 10, halaman 2: 10, halaman 3: 5), pohon grup (#21), tier dan penugasan (#23: Nanda Pratama Global MUR OFF + Group MUR Finance & Accounting; Qori Akbar Global Role Manage global user & role aktif dan Group Manager IT Infrastructure). Scope Nanda Pratama sebelum perubahan: 12 pengguna Finance & Accounting yaitu Ahmad Dahlan, Budi Santoso, Citra Lestari, Gita Permata, Lina Marlina, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Sinta Dewi, Teguh Prakoso, Umar Faruq, dan Wawan Setiawan.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen; seed API untuk memulihkan penugasan Nanda Pratama (kemampuan disediakan tim FE/BE).
- State global yang diubah: Global Role dan Group Role Nanda Pratama (TC-FA-SU-67 menyalakan switch Global Role dan menghapus penugasan grupnya). Langkah 20 memulihkannya ke kondisi Pre-setup #23 lewat seed API dan hook `after` memulihkannya lagi sebagai cadangan; efek pada Last Updated dan entri Changelog Nanda Pratama tidak dibalik.

## Test Steps

### TC-FA-SU-66: Aktor multi-sumber, Group Role Manage user & role dengan Global Role OFF hanya memberi scope grup

1. Verifikasi halaman 1 User List berisi 10 baris yang seluruhnya termasuk 12 nama scope Finance & Accounting
2. Klik halaman 2 pada Pagination
3. Verifikasi halaman 2 berisi 2 baris sisanya sehingga halaman 1 dan 2 memuat tepat 12 nama scope Finance & Accounting
4. Ketik Search `Rudi Hartono`, tekan Enter
5. Verifikasi empty state `No results found`
6. Klik `(←)` pada kotak Search

### TC-FA-SU-67: Menyalakan Global Role Manage global user & role menghapus penugasan grup dan memberi scope entity-wide

7. Ganti akun: logout lalu login sebagai Total Control (Lina Marlina)
8. Buka Settings > User dari sidebar
9. Ketik Search `Nanda Pratama`, tekan Enter
10. Buka Detail Nanda Pratama lalu Tab Role (Sub-tab Global Role)
11. Nyalakan switch `Manage global user & role` pada Nanda Pratama
12. Buka Sub-tab Group Role
13. Verifikasi Sub-tab Group Role Nanda Pratama tampil
14. Verifikasi penugasan grup Finance & Accounting pada Group Role `Manage user & role` Nanda Pratama terhapus: baris Group Role `Manage user & role` tidak tampil lagi di Sub-tab Group Role
15. Ganti akun: logout lalu login sebagai Nanda Pratama
16. Buka Settings > User dari sidebar
17. Verifikasi halaman 1 User List berisi 10 baris
18. Klik halaman 3 pada Pagination
19. Verifikasi halaman 3 berisi 5 baris, sehingga Nanda Pratama melihat seluruh 25 pengguna organisasi
20. Pulihkan Global Role Nanda Pratama menjadi OFF dan Group Role `Manage user & role` pada Finance & Accounting lewat seed API

### TC-FA-SU-68: Global Role Manage global user & role aktif dengan Group Manager tetap diperbolehkan dan scope gabungan

21. Ganti akun: logout lalu login sebagai Manage global user & role (Update) dan Group Manager IT Infrastructure (Qori Akbar)
22. Buka Settings > User dari sidebar
23. Verifikasi halaman 1 User List berisi 10 baris
24. Klik halaman 3 pada Pagination
25. Verifikasi halaman 3 berisi 5 baris, sehingga scope baris entity-wide (25 pengguna)
26. Ketik Search `Budi Santoso`, tekan Enter
27. Buka row action menu `⋯` baris Budi Santoso
28. Verifikasi row action `Edit Home Group` Show
29. Tutup row action menu dengan menekan Esc
30. Ganti isi kotak search dengan `Qori Akbar`, tekan Enter
31. Buka Detail Qori Akbar lalu Tab Role (Sub-tab Global Role)
32. Verifikasi switch `Manage global user & role` ON
33. Buka Sub-tab Group Role
34. Verifikasi Group Manager IT Infrastructure tampil pada Sub-tab Group Role Qori Akbar
35. Verifikasi baris Group Role `Manage user & role` tidak tampil pada Sub-tab Group Role Qori Akbar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec ditulis per blok role: langkah tiap aktor berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search pada langkah 4, 9, 26, 30 dan menutupnya pada langkah 6 (R-16); langkah 29 (menutup row action menu); langkah 20 (pemulihan state Nanda Pratama, S-09).
- Langkah 13 adalah anchor positif untuk asersi absence langkah 14; langkah 34 untuk langkah 35; empty state langkah 5 adalah anchor Search untuk absence Rudi Hartono (bagian 8b butir 2).
- Langkah 14 menggabungkan Expected a ("penugasan grup terhapus") dan Expected b ("baris tidak tampil lagi di Sub-tab Group Role") karena keduanya teramati lewat satu pengamatan yang sama (S-03, kesimpulan yang tidak teramati terpisah).
- Langkah 4 sampai 6 menurunkan Expected b TC-FA-SU-66 ("Global Role berstatus inactive tidak memberi wewenang apa pun") menjadi pengamatan bahwa pengguna di luar scope grup (Rudi Hartono, hanya Global Role) tidak tampil; alasan S-03: TC tidak memberi langkah observasi untuk klausa itu.
- Temuan untuk QA:
  - TC-FA-SU-66 Expected b ("Global Role berstatus inactive tidak memberi wewenang apa pun") tidak punya langkah observasi dan tidak menyebut kontrol yang diamati; spec memakai pengamatan scope (langkah 4 sampai 6).
  - TC-FA-SU-67 tidak menyebut dialog atau toast saat switch Global Role dinyalakan, sehingga tidak ada Verifikasi untuk itu; TC-FA-SU-67 Expected a dan b mengamati hal yang sama.
  - TC-FA-SU-68 Expected a dan c adalah pernyataan invarian ("dapat dipegang bersamaan", "tidak pernah dipegang bersamaan") tanpa langkah observasi; spec mengamati Detail Qori Akbar (switch Global Role ON, Group Manager IT Infrastructure tampil, tidak ada baris Group Role `Manage user & role`). TC tidak menyebut tempat tampil Group Manager pada Detail; spec memakai Sub-tab Group Role.
  - TC-FA-SU-68 tidak menyebut baris target untuk `Edit Home Group`; spec memakai Budi Santoso.
  - Email akun #4 dan #11 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
