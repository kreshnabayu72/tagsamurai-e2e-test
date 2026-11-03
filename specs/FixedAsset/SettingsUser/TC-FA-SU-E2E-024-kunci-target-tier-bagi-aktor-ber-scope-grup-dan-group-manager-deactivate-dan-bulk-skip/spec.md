---
id: TC-FA-SU-E2E-024-kunci-target-tier-bagi-aktor-ber-scope-grup-dan-group-manager-deactivate-dan-bulk-skip
title: "Kunci Target Tier bagi Aktor Ber-scope Grup dan Group Manager: Kontrol Disabled dan Bulk Deactivate Skip"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1063
coverage:
  web: automated
---

# Kunci Target Tier bagi Aktor Ber-scope Grup dan Group Manager: Kontrol Disabled dan Bulk Deactivate Skip

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role Group (Update) (Sinta Dewi, Pre-setup #6); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control (Lina Marlina). Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit; langkah 1 sampai 39 diulang untuk aktor kedua):

| Aktor | Pre-setup | Nama | Pengguna eligible (Bulk Deactivate) | Email | Env password |
|---|---|---|---|---|---|
| Manage user & role Group (Update) | #6 | Sinta Dewi | Gita Permata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Indra Wijaya | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |

- Nama env `FA_MURGR_UPD_PASSWORD` dan `FA_GM_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Tabel "Target tier" (langkah 15 sampai 18 dan 35 sampai 39): Lina Marlina (Total Control) lalu Citra Lestari (Read Only).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), tier dan penugasan (#23). Gita Permata (scope Sinta Dewi) dan Indra Wijaya (scope Oscar Pranata) adalah pengguna eligible yang dinonaktifkan oleh Bulk Deactivate; keduanya data Pre-setup karena keanggotaan scope aktor ditetapkan Pre-setup #20 dan #23 sehingga tidak dapat dimiliki spec. Keduanya dipulihkan menjadi Active lewat seed API pada langkah 42 dan hook `after`; efeknya (Last Updated dan entri Changelog, System Log, Activity Log) tidak dibalik.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen; seleksi baris berlanjut saat isi Search berganti (diasumsikan, lihat Temuan untuk QA); seed API untuk memulihkan status Active Gita Permata dan Indra Wijaya (kemampuan disediakan tim FE/BE); pembacaan jumlah entri Tab Changelog sebagai baseline (S-12) lewat UI.
- State global yang diubah: status aktif Gita Permata dan Indra Wijaya (dipulihkan pada langkah 42 dan hook `after`). Pengguna tier (Lina Marlina dan Citra Lestari) tidak diubah.

## Test Steps

### TC-FA-SU-1063: Target Total Control dan Read Only bagi aktor Manage user & role Group dan Group Manager

1. Ketik Search `Lina Marlina`, tekan Enter
2. Hover sakelar Active baris Lina Marlina
3. Verifikasi sakelar Active baris Lina Marlina Disabled dengan tooltip `You don't have permission to edit.`
4. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
5. Hover sakelar Active baris Citra Lestari
6. Verifikasi sakelar Active baris Citra Lestari Disabled dengan tooltip `You don't have permission to edit.`
7. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
8. Buka Detail Lina Marlina lalu Tab Role (Sub-tab Global Role)
9. Hover switch Global Role dan checkbox C/R/U/D
10. Verifikasi switch dan checkbox C/R/U/D Global Role Disabled dengan tooltip `You don't have permission to edit.`
11. Buka Sub-tab Group Role
12. Hover `[Assign Group]` pada baris Group Role
13. Verifikasi `[Assign Group]` Disabled dengan tooltip `You don't have permission to edit.`
14. Verifikasi `[Detail]` pada baris Group Role Enabled

Untuk setiap target pada tabel "Target tier" di `## Prerequisites` (Lina Marlina, lalu Citra Lestari), jalankan langkah 15 sampai 18.

15. Buka Settings > User dari sidebar
16. Ketik Search nama target, tekan Enter
17. Buka Detail target lalu Tab Changelog
18. Catat jumlah entri Tab Changelog target sebagai baseline target

19. Buka Settings > User dari sidebar
20. Ketik Search nama pengguna eligible aktor, tekan Enter
21. Centang baris pengguna eligible
22. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter
23. Centang baris Lina Marlina
24. Verifikasi checkbox baris Lina Marlina tercentang
25. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter
26. Centang baris Citra Lestari
27. Verifikasi checkbox baris Citra Lestari tercentang
28. Klik Bulk Action > `[Deactivate]`
29. Verifikasi dialog campuran mencantumkan Lina Marlina dan Citra Lestari pada kelompok `The following will be skipped (already inactive, inactive in Global Settings, or no permission):`
30. Klik `[Continue]`
31. Verifikasi toast "Success, user has been deactivated. Some items were skipped."
32. Ganti isi kotak search dengan nama pengguna eligible aktor, tekan Enter
33. Verifikasi sakelar Active baris pengguna eligible OFF (Inactive)
34. Klik `(←)` pada kotak Search

Untuk setiap target pada tabel "Target tier", jalankan langkah 35 sampai 39.

35. Ketik Search nama target, tekan Enter
36. Verifikasi sakelar Active baris target ON (tidak berubah)
37. Buka Detail target lalu Tab Changelog
38. Verifikasi jumlah entri Tab Changelog target sama dengan baseline langkah 18
39. Buka Settings > User dari sidebar

40. Ganti akun: logout lalu login sebagai Group Manager (Oscar Pranata)
41. Buka Settings > User dari sidebar

Ulangi langkah 1 sampai 39 untuk Group Manager (Oscar Pranata), dengan Indra Wijaya menggantikan Gita Permata sebagai pengguna eligible.

42. Pulihkan Gita Permata dan Indra Wijaya menjadi Active lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Spec berisi satu TC dengan dua aktor; tiap aktor ditulis sebagai blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Aksi Bulk Deactivate ada di akhir blok (S-10) dan pemulihan pada langkah 42.
- Spec melewati sekitar 35 langkah (42 langkah nominal, 99 langkah dengan ekspansi). Alasan: satu TC (satu kelas, fungsional kunci target tier) yang langkah terakhirnya di TC mengulang seluruh langkah sebelumnya untuk aktor kedua; satu TC masuk tepat satu spec. Langkah yang diulang: langkah 15 sampai 18 untuk dua target (+4 per blok), langkah 35 sampai 39 untuk dua target (+5 per blok), dan langkah 1 sampai 39 untuk aktor kedua (48 langkah dengan ekspansi); parameter ada di tabel `## Prerequisites`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris target pada langkah 1, 4, 7, 16, 20, 22, 25, 32, 35 dan menutupnya pada langkah 34 (R-16); langkah 15, 19, 39 (membuka Settings > User); langkah 18 (baseline jumlah entri Tab Changelog sebelum aksi, S-12); langkah 42 (pemulihan state, S-09).
- Asersi "tidak menulis log" Expected d dikerjakan di spec ini sebagai selisih jumlah entri terhadap baseline (langkah 18 dan 38), bukan asersi absence kelas g (bagian 3 prinsip 13g: asersi jumlah/state dengan baseline boleh di spec fungsional). Baseline langkah 18 adalah anchor positif untuk langkah 38 (bagian 8b butir 2). Surface yang diamati hanya Tab Changelog target; TC tidak menyebut surface log lain untuk klausa ini (lihat Temuan untuk QA).
- Langkah 31 (toast sukses) adalah anchor yang menandai respons server selesai sebelum langkah 33 dan 36.
- Temuan untuk QA:
  - TC-FA-SU-1063 Expected d ("tidak menulis log") tidak menyebut surface log (Tab Changelog, Tab System Log aktor, Activity Log); spec mengamati Tab Changelog target saja. Post Condition "tanpa entri log" tidak punya langkah observasi tambahan di TC. Penulisan log bersifat eventual (NC-03), sehingga selisih nol pada langkah 38 dapat lolos sebelum entri tertulis; usulan QA: tambahkan batas tunggu atau spec absence untuk TC ini.
  - TC-FA-SU-1063 langkah 3 mencentang tiga pengguna sekaligus, tetapi tidak menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti. Bila seleksi tidak bertahan, QA perlu menyebut cara lain (mis. ukuran halaman besar).
  - TC-FA-SU-1063 langkah 2 menyebut `Detail Lina Marlina > Tab Role` saja; baris Group Role yang dipakai untuk `[Assign Group]` dan `[Detail]` pada Lina Marlina tidak disebut di Pre-setup #23. Spec mengasersi kontrol pada baris Group Role yang tampil.
  - Email akun #6 dan #9 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
