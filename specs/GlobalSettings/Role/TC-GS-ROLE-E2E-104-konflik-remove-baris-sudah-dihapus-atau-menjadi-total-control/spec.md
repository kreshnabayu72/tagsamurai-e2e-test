---
id: TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control
title: "Konflik Antar Admin pada Remove Baris Role: Sudah Dihapus Admin Lain atau Target Menjadi Total Control"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-274
  - TC-GS-ROLE-276
  - TC-GS-ROLE-297
coverage:
  web: automated
---

# Konflik Antar Admin pada Remove Baris Role: Sudah Dihapus Admin Lain atau Target Menjadi Total Control

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin), kelas c. Suite `parallel: false`.
- Akun Sesi A (UI):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-276, TC-297 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-274 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Akun Sesi B (pemicu): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Sesi B memakai sesi API (klien HTTP dengan kredensial Eko Prasetyo; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B.
- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser untuk Sesi A (ganti akun Ahmad Fauzi ke Hendra Wijaya lewat logout dan login); klien HTTP untuk Sesi B; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Data milik spec (dibuat lewat sesi API Eko Prasetyo di hook `before`; kemampuan seeding user dan Assign Role disediakan tim FE; nilai field wajib lain user seed disediakan tim FE). Setara user TC: Wawan Setiawan (TC-274) dan Agus Salim (TC-276). Semua user Active, Access Global Settings dicentang, tanpa access level:
  - `Target Status Berubah {runId}-104`: baris Manage TAG (TC-274).
  - `Target Dihapus {runId}-104`: baris Manage hardware (TC-276).
  - `Pembanding {runId}-104`: baris Manage hardware, dipakai sebagai baris pembanding absence pada TC-276 dan TC-297.
- Data Pre-setup #18: `Fikri Ramadhan` (Active, Access Global Settings dicentang, tanpa access level) dengan Given baris Manage hardware di-assign lewat sesi API di hook `before` (TC-297). Hook `after` memastikan Fikri Ramadhan kembali tanpa access level dan tanpa baris role.
- Efek pemulihan Pre-setup yang tidak terpulihkan (S-06): Fikri Ramadhan di-assign baris role, di-assign Total Control oleh Sesi B, lalu dibersihkan di hook `after`; Modified By dan Last Updated user itu berubah dan tidak dapat dipulihkan ke nilai awal, serta entri Changelog (Assign, Remove, Auto-Revert), Activity Log, dan System Log bersifat immutable dan tidak dihapus. Karena itu asersi log atas Fikri Ramadhan tidak memakai nilai absolut: jumlah entri Auto-Revert memakai selisih terhadap baseline `B-FR-AR` (S-12) dan Modified By hanya dibaca dari entri baru (langkah 34 dan 35).
- Baseline (dicatat di hook `before` sesudah Given `Fikri Ramadhan` dan sebelum permintaan pertama Sesi B, S-12; jumlah entri dibaca dari UI Changelog lewat Search nama user): jumlah entri Auto-Revert untuk `Fikri Ramadhan` di Changelog Tab Total Control sebagai `B-FR-AR`. Asersi memakai selisih terhadap baseline karena audit trail permanen dan nama Pre-setup literal dipakai ulang antar run; entri target milik spec (bersuffix `{runId}-104`) tidak memerlukan baseline.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): cabut Total Control `Target Status Berubah {runId}-104` bila ada, hapus baris role ketiga user seed dan Fikri Ramadhan bila ada, lalu hapus ketiga user seed; pulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data milik spec di atas.

## Test Steps

### TC-GS-ROLE-276: Remove baris yang sudah dihapus admin lain dianggap sukses

1. [Sesi A] Buka Detail "Manage hardware"
2. [Sesi A] Ketik Search `{runId}-104`, tekan Enter
3. [Sesi B] Remove baris Manage hardware `Target Dihapus {runId}-104` lewat sesi API hingga perubahan tersimpan
4. [Sesi A] Klik `(⋯)` pada baris `Target Dihapus {runId}-104`
5. [Sesi A] Klik `Remove`
6. [Sesi A] Klik `[Remove]` pada dialog
7. [Sesi A] Verifikasi tidak ada toast error
8. [Sesi A] Verifikasi tidak ada dialog konflik
9. [Sesi A] Verifikasi baris `Pembanding {runId}-104` tampil di Detail "Manage hardware"
10. [Sesi A] Verifikasi baris `Target Dihapus {runId}-104` tidak ada di Detail "Manage hardware"
11. [Sesi A] Klik `Changelog`
12. [Sesi A] Ketik Search `Target Dihapus {runId}-104`, tekan Enter
13. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Dihapus {runId}-104`
14. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-297: Remove baris oleh Total Control saat target menjadi Total Control antara render dan submit

15. [Sesi A] Klik `(←)` pada kotak Search
16. [Sesi A] Ketik Search `Fikri Ramadhan`, tekan Enter
17. [Sesi A] Klik `(⋯)` pada baris `Fikri Ramadhan`
18. [Sesi A] Klik `Remove`
19. [Sesi A] Verifikasi dialog Remove tampil
20. [Sesi B] Tetapkan Total Control ke `Fikri Ramadhan` lewat sesi API hingga perubahan tersimpan
21. [Sesi A] Klik `[Remove]` pada dialog
22. [Sesi A] Klik `(←)` pada kotak Search
23. [Sesi A] Ketik Search `{runId}-104`, tekan Enter
24. [Sesi A] Verifikasi baris `Pembanding {runId}-104` tampil di Detail "Manage hardware"
25. [Sesi A] Ketik Search `Fikri Ramadhan`, tekan Enter
26. [Sesi A] Verifikasi baris `Fikri Ramadhan` terhapus dari Detail "Manage hardware"
27. [Sesi A] Buka Tab `Total Control`
28. [Sesi A] Ketik Search `Ahmad Fauzi`, tekan Enter
29. [Sesi A] Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control
30. [Sesi A] Ketik Search `Fikri Ramadhan`, tekan Enter
31. [Sesi A] Verifikasi baris `Fikri Ramadhan` tidak ada di Tab Total Control (auto-revert terhadap status saat submit)
32. [Sesi A] Klik `Changelog`
33. [Sesi A] Ketik Search `Fikri Ramadhan`, tekan Enter
34. [Sesi A] Verifikasi jumlah entri Auto-Revert untuk `Fikri Ramadhan` di Changelog Tab Total Control bertambah tepat 1 dari baseline `B-FR-AR` (selisih +1)
35. [Sesi A] Verifikasi Modified By entri Auto-Revert baru `Fikri Ramadhan` adalah `Ahmad F`
36. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-274: Remove baris yang target-nya menjadi Total Control sejak render

37. [Sesi A] Ganti akun: logout, lalu login sebagai Hendra Wijaya
38. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
39. [Sesi A] Ketik Search `Target Status Berubah {runId}-104`, tekan Enter
40. [Sesi B] Tetapkan Total Control ke `Target Status Berubah {runId}-104` lewat sesi API hingga perubahan tersimpan
41. [Sesi A] Klik `(⋯)` pada baris `Target Status Berubah {runId}-104`
42. [Sesi A] Klik `Remove`
43. [Sesi A] Klik `[Remove]` pada dialog
44. [Sesi A] Verifikasi toast error `You don't have permission to edit.` tampil
45. [Sesi A] Verifikasi baris `Target Status Berubah {runId}-104` tidak terhapus (masih ada di Detail "Manage TAG")
46. [Sesi A] Verifikasi tidak ada dialog konflik
47. [Sesi A] Klik `(⋯)` pada baris `Target Status Berubah {runId}-104`
48. [Sesi A] Verifikasi row action Remove baris `Target Status Berubah {runId}-104` disabled
49. [Sesi A] Arahkan kursor ke row action Remove baris `Target Status Berubah {runId}-104`
50. [Sesi A] Verifikasi tooltip `You don't have permission to edit.` tampil

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda`, dan `TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil`.
- Sesi B adalah sesi API pemicu: hanya memicu perubahan state dan tidak ada asersi di Sesi B. Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (50 langkah) karena ketiga blok satu kelas harness dan berdiri sendiri: tiap blok punya user target, pemicu Sesi B, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah dari 274, 276, 297 menjadi 276, 297, 274 supaya akun Sesi A berganti dari Ahmad Fauzi ke Hendra Wijaya satu kali (langkah 37).
- Search target sebelum aksi baris ditulis sebagai langkah penghubung (R-16) dan ditempatkan sebelum pemicu Sesi B supaya tampilan Sesi A tetap sebelum perubahan Sesi B; Search diperlukan karena daftar user bisa lebih dari satu halaman. Langkah 2, 16, dan 39; langkah 2 memakai `{runId}-104` supaya baris pembanding `Pembanding {runId}-104` tetap tampil. Langkah 15 dan 22 mengosongkan Search lewat `(←)` dan baris pembanding `Pembanding {runId}-104` ditampilkan lagi oleh Search `{runId}-104` pada langkah 23 sebelum `Verifikasi` pada langkah 24.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail, Tab, dan Changelog (langkah 1, 11, 27, 32, 38), Search (langkah 12 dan 33), menutup modal Changelog (langkah 14 dan 36), dan ganti akun (langkah 37). Detail "Manage hardware" tetap terbuka dari langkah 1 hingga langkah 17 sehingga baris `Fikri Ramadhan` yang di-seed sebelum langkah 1 sudah ter-render saat langkah 17.
- Absence baris (langkah 10, 26; langkah 26 setelah Search `Fikri Ramadhan` pada langkah 25 dengan anchor langkah 24 pada Detail yang sama) didahului baris pembanding `Pembanding {runId}-104` pada surface yang sama (bagian 8b butir 2); absence `Fikri Ramadhan` di Tab Total Control (langkah 31) didahului baris `Ahmad Fauzi` (langkah 29).
- Langkah penghubung (S-15, bukan dari TC sumber): row action `Remove` berada di overlay `(⋯)` baris, sehingga "Klik Remove pada baris X" ditulis `Klik (⋯)` pada baris lalu `Klik Remove` (langkah 4 dan 5; langkah 17 dan 18; langkah 41 dan 42). Langkah 19 adalah `Verifikasi` sendiri untuk keadaan dialog Remove tampil (sebelumnya klaim keadaan dalam kurung di langkah aksi, R-02); keadaan itu berasal dari Langkah Uji 1 TC-297, bukan dari butir Expected. Langkah 47 membuka kembali overlay `(⋯)` baris `Target Status Berubah {runId}-104` karena overlay tertutup sesudah `Remove` diklik dan row action `Remove` yang diasersi disabled berada di overlay itu.
- Langkah penghubung (R-16, bukan dari TC sumber): Search `{runId}-104` (langkah 23) sebelum `Verifikasi` baris pembanding karena daftar user bisa lebih dari satu halaman; Search `Fikri Ramadhan` (langkah 25) sebelum absence baris `Fikri Ramadhan` supaya absence tidak trivial terhadap filter `{runId}-104`.
- Asersi log atas `Fikri Ramadhan` (langkah 34 dan 35) memakai selisih terhadap baseline `B-FR-AR` yang dicatat di hook `before` (S-12), karena Changelog Tab Total Control permanen dan `Fikri Ramadhan` dipakai ulang antar run.
- Langkah penghubung (R-16, bukan dari TC sumber): Search `Ahmad Fauzi` (langkah 28) sebelum `Verifikasi` baris pembanding dan Search `Fikri Ramadhan` (langkah 30) sebelum absence di Tab Total Control karena tab berpagination; absence langkah 31 tetap bermakna karena baris pembanding `Ahmad Fauzi` sudah terverifikasi pada Tab yang sama (langkah 29) dan Search `Fikri Ramadhan` mengganti isi Search `Ahmad Fauzi`.
- Temuan untuk QA:
  - TC-274 dan TC-276 menyebut "sesi B" tanpa akun (TC-276 menyebut "Dua admin Total Control (sesi A, B)"); spec memakai Ahmad Fauzi atau Hendra Wijaya sebagai Sesi A dan Eko Prasetyo sebagai Sesi B.
  - TC-274 memakai Wawan Setiawan dan TC-276 memakai Agus Salim (Pre-setup #9) dengan Given baris role; spec memakai user seed milik spec supaya Pre-setup bersama tidak diubah (S-06).
  - TC-297 Post Condition tidak ada; Expected c menyebut entry Auto-Revert di Changelog Tab Total Control sehingga spec memakai surface itu.
  - TC-276 Expected tidak menyebut toast; spec tidak mengasersi toast sukses.
