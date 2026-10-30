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
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): cabut Total Control `Target Status Berubah {runId}-104` bila ada, hapus baris role ketiga user seed dan Fikri Ramadhan bila ada, lalu hapus ketiga user seed; pulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data milik spec di atas.

## Test Steps

### TC-GS-ROLE-276: Remove baris yang sudah dihapus admin lain dianggap sukses

1. [Sesi A] Buka Detail "Manage hardware"
2. [Sesi B] Remove baris Manage hardware `Target Dihapus {runId}-104` lewat sesi API
3. [Sesi A] Klik Remove pada baris `Target Dihapus {runId}-104`
4. [Sesi A] Klik `[Remove]` pada dialog
5. [Sesi A] Verifikasi tidak ada toast error
6. [Sesi A] Verifikasi tidak ada dialog konflik
7. [Sesi A] Verifikasi baris `Pembanding {runId}-104` tampil di Detail "Manage hardware"
8. [Sesi A] Verifikasi baris `Target Dihapus {runId}-104` tidak ada di Detail "Manage hardware"
9. [Sesi A] Klik `Changelog`
10. [Sesi A] Ketik Search `Target Dihapus {runId}-104`, tekan Enter
11. [Sesi A] Verifikasi Changelog memuat tepat 1 entri Remove untuk `Target Dihapus {runId}-104`
12. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-297: Remove baris oleh Total Control saat target menjadi Total Control antara render dan submit

13. [Sesi A] Klik Remove pada baris `Fikri Ramadhan` (dialog Remove tampil)
14. [Sesi B] Tetapkan Total Control ke `Fikri Ramadhan` lewat sesi API
15. [Sesi A] Klik `[Remove]` pada dialog
16. [Sesi A] Verifikasi baris `Pembanding {runId}-104` tampil di Detail "Manage hardware"
17. [Sesi A] Verifikasi baris `Fikri Ramadhan` terhapus dari Detail "Manage hardware"
18. [Sesi A] Buka Tab `Total Control`
19. [Sesi A] Verifikasi baris `Ahmad Fauzi` tampil di Tab Total Control
20. [Sesi A] Verifikasi baris `Fikri Ramadhan` tidak ada di Tab Total Control (auto-revert terhadap status saat submit)
21. [Sesi A] Klik `Changelog`
22. [Sesi A] Ketik Search `Fikri Ramadhan`, tekan Enter
23. [Sesi A] Verifikasi Changelog Tab Total Control memuat entri Auto-Revert untuk `Fikri Ramadhan`
24. [Sesi A] Verifikasi Modified By entri Auto-Revert `Fikri Ramadhan` adalah `Ahmad F`
25. [Sesi A] Tutup modal Changelog

### TC-GS-ROLE-274: Remove baris yang target-nya menjadi Total Control sejak render

26. [Sesi A] Ganti akun: logout, lalu login sebagai Hendra Wijaya
27. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
28. [Sesi B] Tetapkan Total Control ke `Target Status Berubah {runId}-104` lewat sesi API
29. [Sesi A] Klik Remove pada baris `Target Status Berubah {runId}-104`
30. [Sesi A] Klik `[Remove]` pada dialog
31. [Sesi A] Verifikasi toast error `You don't have permission to edit.` tampil
32. [Sesi A] Verifikasi baris `Target Status Berubah {runId}-104` tidak terhapus (masih ada di Detail "Manage TAG")
33. [Sesi A] Verifikasi tidak ada dialog konflik
34. [Sesi A] Verifikasi row action Remove baris `Target Status Berubah {runId}-104` disabled
35. [Sesi A] Arahkan kursor ke row action Remove baris `Target Status Berubah {runId}-104`
36. [Sesi A] Verifikasi tooltip `You don't have permission to edit.` tampil

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus`, `TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda`, dan `TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil`.
- Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B (P-2, `[KEPUTUSAN 2026-10-21]`). Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec melewati sekitar 35 langkah (36 langkah) karena ketiga blok satu kelas harness dan berdiri sendiri: tiap blok punya user target, pemicu Sesi B, dan asersi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber diubah dari 274, 276, 297 menjadi 276, 297, 274 supaya akun Sesi A berganti dari Ahmad Fauzi ke Hendra Wijaya satu kali (langkah 26).
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail, Tab, dan Changelog (langkah 1, 9, 18, 21, 27), Search (langkah 10 dan 22), menutup modal Changelog (langkah 12 dan 25), dan ganti akun (langkah 26). Detail "Manage hardware" tetap terbuka dari langkah 1 hingga langkah 13 sehingga baris `Fikri Ramadhan` yang di-seed sebelum langkah 1 sudah ter-render saat langkah 13.
- Absence baris (langkah 8, 17) didahului baris pembanding `Pembanding {runId}-104` pada surface yang sama (bagian 8b butir 2); absence `Fikri Ramadhan` di Tab Total Control (langkah 20) didahului baris `Ahmad Fauzi` (langkah 19).
- Temuan untuk QA:
  - TC-274 dan TC-276 menyebut "sesi B" tanpa akun (TC-276 menyebut "Dua admin Total Control (sesi A, B)"); spec memakai Ahmad Fauzi atau Hendra Wijaya sebagai Sesi A dan Eko Prasetyo sebagai Sesi B.
  - TC-274 memakai Wawan Setiawan dan TC-276 memakai Agus Salim (Pre-setup #9) dengan Given baris role; spec memakai user seed milik spec supaya Pre-setup bersama tidak diubah (S-06).
  - TC-297 Post Condition tidak ada; Expected c menyebut entry Auto-Revert di Changelog Tab Total Control sehingga spec memakai surface itu.
  - TC-276 Expected tidak menyebut toast; spec tidak mengasersi toast sukses.
