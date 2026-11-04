---
id: TC-AC-SU-E2E-184-konkurensi-dua-aktor-last-write-wins-dan-request-lama-no-op
title: "Konkurensi Dua Aktor Memakai Last-Write-Wins dan Request Lama Menjadi No-Op pada Deactivate, Activate, Save Assign Group Role, dan Dialog Auto-Revert"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-102
  - TC-AC-SU-625
  - TC-AC-SU-626
  - TC-AC-SU-627
  - TC-AC-SU-634
coverage:
  web: automated
---

# Konkurensi Dua Aktor Memakai Last-Write-Wins dan Request Lama Menjadi No-Op pada Deactivate, Activate, Save Assign Group Role, dan Dialog Auto-Revert

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI utama (aktor A): Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun UI utama di tengah spec; hook `after` memulihkan sesi ke akun default suite.
- Aktor kedua (aktor B): pemicu perubahan state memakai sesi API (login API password; token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE): Total Control (`Spectra.env.AC_TC_PASSWORD`) pada blok TC-102 dan TC-634, Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DU_PASSWORD`) pada blok TC-625 dan TC-627. Pada blok TC-626, aktor B adalah sesi UI kedua (konteks browser kedua, objek asersi karena toast di sesi B diasersi): Default User dengan `Spectra.env.AC_DU_PASSWORD`, login pada langkah 35 dan ditutup bersama sesi loginnya pada akhir blok (S-09).
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC (Branch 1 dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `John Doe {runId}-184A` | `johndoe+{runId}-184a@qwertysystem.net` | Activated, Active (TC-102) |
| U2 | `Jane Smith {runId}-184B` | `janesmith+{runId}-184b@qwertysystem.net` | Activated, Inactive (TC-625) |
| U3 | `Mike Tan {runId}-184C` | `miketan+{runId}-184c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A (TC-626) |
| U4 | `Rina Putri {runId}-184D` | `rinaputri+{runId}-184d@qwertysystem.net` | Activated, bertier Total Control (TC-627) |
| U5 | `Jane Smith {runId}-184E` | `janesmith+{runId}-184e@qwertysystem.net` | Activated, Active (TC-634) |

- Kemampuan teknis: Fixture BE (seeding user, tier, dan assignment; membaca jumlah entri Changelog per user untuk baseline TC-625, karena dialog Activate User terbuka); sesi API aktor B; konteks browser kedua (TC-626). Layar aktor A dimuat sebelum aktor B bertindak pada tiap blok (Search baris target di langkah awal blok). Baseline jumlah entri Popup Changelog: User dicatat per user seeding sebelum aksi aktor A. Tanpa intercept dan tanpa jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-102: Deactivate user yang sudah Inactive oleh aktor lain
1. Ketik Search `John Doe {runId}-184A`, tekan Enter sehingga baris U1 tampil Active
2. Aktor B men-deactivate U1 lewat sesi API hingga status Inactive tersimpan
3. Klik switch Active baris U1 di layar aktor A (tanpa memuat ulang)
4. Klik `[Deactivate]`
5. Verifikasi toast sukses `"Success, user has been deactivated."`
6. Verifikasi list di-refresh dan switch Active baris U1 bernilai OFF
### TC-AC-SU-634: Deactivate request lama adalah no-op
7. Ganti isi kotak Search dengan `Jane Smith {runId}-184E`, tekan Enter sehingga baris U5 tampil Active
8. Aktor B men-deactivate U5 lewat sesi API hingga status Inactive tersimpan
9. Catat jumlah entri U5 pada Popup Changelog: User sebagai N5 (Search `Jane Smith {runId}-184E`), lalu tutup popup
10. Klik switch Active baris U5 dari ON ke OFF di layar aktor A, lalu klik `[Deactivate]`
11. Verifikasi toast sukses `"Success, user has been deactivated."`
12. Verifikasi list di-refresh dan switch Active baris U5 bernilai OFF
13. Buka Popup Changelog: User, ketik Search `Jane Smith {runId}-184E`, tekan Enter
14. Verifikasi jumlah entri U5 sama dengan N5 (tidak ada entri baru)
### TC-AC-SU-625: Activate oleh dua aktor bersamaan
15. Tutup popup, ganti isi kotak Search dengan `Jane Smith {runId}-184B`, tekan Enter sehingga baris U2 tampil Inactive
16. Klik switch Active baris U2 sehingga dialog Activate User tampil (belum dikonfirmasi)
17. Aktor B meng-activate U2 lewat sesi API hingga status Active tersimpan
18. Catat jumlah entri Changelog U2 sebagai N2 lewat Fixture BE (dialog Activate User tetap terbuka)
19. Klik `[Activate]`
20. Verifikasi tidak ada dialog konflik
21. Verifikasi status U2 Active
22. Verifikasi list di-refresh
23. Buka Popup Changelog: User, ketik Search `Jane Smith {runId}-184B`, tekan Enter
24. Verifikasi jumlah entri U2 sama dengan N2 (request aktor A no-op, tanpa entri log tambahan)
### TC-AC-SU-627: Switch role target Total Control diubah aktor lain saat dialog Auto-Revert terbuka
25. Tutup popup, ganti isi kotak Search dengan `Rina Putri {runId}-184D`, tekan Enter, klik Name baris U4, klik Tab Role, lalu sub-tab Global Role
26. Uncheck Delete pada "Manage group" sehingga dialog Remove Total Control tampil
27. Aktor B mengedit role U4 hingga Auto-Revert dan konfirmasi tersimpan lewat sesi API
28. Klik `[Remove]`
29. Verifikasi tidak ada dialog konflik
30. Verifikasi perubahan aktor A diterapkan (Delete "Manage group" unchecked pada state server)
31. Verifikasi Tab Role di-refresh ke state server (banner Total Control tidak tampil)
32. Klik Tab Changelog
33. Verifikasi Tab Changelog memuat tepat 1 entri Auto-Revert untuk U4 (tidak ada entri Auto-Revert kedua)
### TC-AC-SU-626: Save Assign Group Role dua aktor memakai last-write-wins
34. Klik menu Settings > User di sidebar, ketik Search `Mike Tan {runId}-184C`, tekan Enter, klik Name baris U3, klik Tab Role, lalu sub-tab Group Role
35. Buka konteks kedua (jendela privat), login sebagai Default User
36. Buka Settings > User lewat sidebar di sesi aktor B
37. Buka Detail U3 (Search nama, klik Name, Tab Role, sub-tab Group Role), lalu klik `[Assign Group]` pada baris "Manage partner"
38. Aktor A: klik `[Assign Group]` pada baris "Manage partner", klik `[+ Assign Group]`, centang Region B, klik `[Select]`, lalu klik `[Save]`
39. Verifikasi toast sukses di sesi aktor A
40. Aktor B (popup dibuka sebelum aktor A menyimpan): hapus baris Region A, klik `[+ Assign Group]`, centang Branch 1, klik `[Select]`, lalu klik `[Save]`
41. Verifikasi toast sukses di sesi aktor B
42. Verifikasi tidak ada dialog konflik di kedua sesi
43. Tutup konteks kedua dan hapus sesi loginnya, lalu muat ulang Detail U3 di sesi aktor A dan buka sub-tab Group Role
44. Verifikasi kolom Group baris "Manage partner" bernilai hasil Save aktor B (`Branch 1`)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), pencatatan jumlah entri awal (langkah 9, 18), pembukaan konteks kedua dan login (langkah 35), pembukaan Settings > User lewat sidebar di sesi aktor B (langkah 36), menutup popup dan konteks kedua. Aktor B pada TC-102, TC-634, TC-625, dan TC-627 memakai sesi API (pelaku kedua hanya memicu perubahan state, `P-2` tidak dipakai); aktor B TC-626 memakai sesi UI karena toast di sesi B diasersi.
- Urutan: TC-102, TC-634, TC-625, TC-627, TC-626. TC-626 terakhir karena memakai konteks UI kedua. Asersi "tanpa entri log tambahan" memakai selisih jumlah entri terhadap baseline (bukan absence kelas g). TC-AC-SU-102 pasangan topik dengan TC-AC-SU-634 (sama-sama Deactivate pada user yang sudah Inactive) dan keduanya tetap di spec ini.
- Lima blok kelas c berpola sama (layar aktor A dimuat, aktor B memicu state, aktor A bertindak) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, sehingga 44 langkah (di atas smell 35 langkah) dipertahankan.
- Temuan untuk QA:
  - TC-102, TC-625, TC-627, dan TC-634 tidak menyatakan apakah aktor B memakai sesi UI atau API; spec memakai sesi API untuk pelaku yang hanya memicu dan sesi UI kedua hanya pada TC-626.
  - Post Condition TC-102 ("Hanya 1 entri log Deactivate (milik aktor B)") tidak punya langkah observasi di TC dan tidak diasersi; TC-634 butir c ("tidak ada entri log baru") diasersi lewat selisih jumlah entri.
  - TC-625 langkah 2 ("Aktor B Deactivate tidak relevan; Aktor B Activate Jane Smith sampai sukses") bernada kontradiktif; spec hanya menjalankan Activate oleh aktor B.
  - TC-626 butir b menyebut "Branch 1" tanpa menyebut apakah assignment akhir hanya Branch 1; spec mengasersi kolom Group bernilai `Branch 1` (hasil Save aktor B).
  - TC-627 butir b ("Tidak ada entri Auto-Revert kedua karena tier sudah kosong") tidak menyebut surface; spec mengasersi pada Tab Changelog U4.
  - TC memakai nama literal (`John Doe`, `Jane Smith`, `Mike Tan`, `Rina Putri`); spec memakai nama bersuffix (S-12).
