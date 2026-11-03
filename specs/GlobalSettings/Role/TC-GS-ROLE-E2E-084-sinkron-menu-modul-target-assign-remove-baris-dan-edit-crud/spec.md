---
id: TC-GS-ROLE-E2E-084-sinkron-menu-modul-target-assign-remove-baris-dan-edit-crud
title: "Sinkronisasi Menu Modul Target: Assign Role, Remove Baris, dan Edit CRUD"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-226
  - TC-GS-ROLE-227
  - TC-GS-ROLE-228
coverage:
  web: automated
---

# Sinkronisasi Menu Modul Target: Assign Role, Remove Baris, dan Edit CRUD

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (aktor): Total Control, Ahmad Fauzi, `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Layar awal Sesi A (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Akun Sesi B (target, objek asersi): Wawan Setiawan (TC-GS-ROLE-226) dan Doni Pratama (TC-GS-ROLE-227 dan TC-GS-ROLE-228). Email disediakan tim FE (tidak ada di Tabel Pre-setup TC), kredensial `Spectra.env.GS_ROLE_TARGET_PASSWORD`. Sesi B dibuka di konteks browser kedua dengan login pada langkah pembuka tiap TC, dan ditutup di akhir TC (konteks ditutup, sesi login terkait dihapus) sebelum TC berikutnya.
- Kelas harness: multi-konteks (kelas c). Hasil di Sesi B adalah objek asersi, bukan pemicu.
- Environment variable: `GS_TC_PASSWORD` dan `GS_ROLE_TARGET_PASSWORD`. `GS_ROLE_TARGET_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang diubah (dipulihkan di hook `after`, tanpa berasumsi langkah spec berhasil penuh):
  - Wawan Setiawan (Pre-setup #11, Active, Access Global Settings, tanpa access level dan tanpa baris role): TC-GS-ROLE-226 meng-assign baris Manage TAG. Hook `after` menghapus baris Manage TAG Wawan Setiawan lewat API bila ada.
  - Doni Pratama (Pre-setup #10: Manage TAG R; Import data C,R; Manage files R,D): hook `before` meng-uncheck Delete pada baris Manage files lewat API sehingga Manage files Read saja (precondition TC-GS-ROLE-228, tidak diasersi). TC-GS-ROLE-227 menghapus baris Manage TAG Doni Pratama; TC-GS-ROLE-228 mencentang Delete Manage files. Hook `after` memulihkan Doni Pratama ke Pre-setup #10 lewat API (baris Manage TAG Read, Manage files Read dan Delete).
  - Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log yang tercatat oleh aksi di atas (log bersifat immutable).
- Kemampuan teknis: dua konteks browser paralel; muat ulang halaman tanpa logout di Sesi B; seeding dan pemulihan baris role dan CRUD lewat API (sesi API aktor Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite), termasuk untuk akun target Sesi B; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-226: Assign Role membuka menu modul untuk target pada request berikutnya

1. [Sesi B] Buka konteks browser baru, login sebagai Wawan Setiawan
2. [Sesi A] Buka Tab System, lalu Detail "Manage TAG"
3. [Sesi A] Klik `[+ Assign]`
4. [Sesi A] Ketik Search `Wawan Setiawan`, tekan Enter
5. [Sesi A] Centang Wawan Setiawan
6. [Sesi A] Klik `[Assign]`
7. [Sesi A] Tunggu aksi selesai
8. [Sesi B] Muat ulang halaman tanpa logout
9. [Sesi B] Verifikasi menu `TAG` tampil di sidebar
10. [Sesi B] Verifikasi menu `Role & Permission` tidak tampil di sidebar
11. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-227: Remove baris role menyembunyikan menu modul target

12. [Sesi B] Buka konteks browser baru, login sebagai Doni Pratama
13. [Sesi A] Ketik Search `Doni Pratama` pada Detail "Manage TAG", tekan Enter
14. [Sesi A] Klik `(⋯)` pada baris Doni Pratama
15. [Sesi A] Klik `Remove`
16. [Sesi A] Klik `[Remove]`
17. [Sesi A] Tunggu aksi selesai
18. [Sesi B] Muat ulang halaman
19. [Sesi B] Verifikasi menu `File Manager` tampil di sidebar
20. [Sesi B] Verifikasi menu `TAG` tidak tampil di sidebar
21. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

### TC-GS-ROLE-228: Edit CRUD berlaku pada request berikutnya tanpa logout

22. [Sesi B] Buka konteks browser baru, login sebagai Doni Pratama
23. [Sesi B] Buka File Manager
24. [Sesi B] Verifikasi aksi hapus file tidak tersedia
25. [Sesi A] Buka Tab System, lalu Detail "Manage files"
26. [Sesi A] Ketik Search `Doni Pratama`, tekan Enter
27. [Sesi A] Centang Delete pada baris Doni Pratama
28. [Sesi A] Tunggu aksi selesai
29. [Sesi B] Muat ulang File Manager
30. [Sesi B] Verifikasi aksi hapus file tersedia
31. [Sesi B] Tutup konteks browser Sesi B dan hapus sesi login terkait

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Ketiga TC bertanda Automation `Manual Only — (d) dua sesi paralel`; tetap masuk spec, kebutuhan dua konteks ada di Prerequisites.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC mengikuti TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka dan menutup konteks Sesi B (langkah 1, 11, 12, 21, 22, 31); membuka Detail role dan Search baris target (langkah 2, 13, 25, 26); Search nama target di Popup Assign sebelum dicentang, karena daftar user di popup (urut Name A-Z) bisa lebih dari satu halaman (langkah 4, R-16/S-03); "Tunggu aksi selesai" sebelum Sesi B memuat ulang (langkah 7, 17, 28); membuka File Manager (langkah 23).
- Urutan Verifikasi TC-GS-ROLE-227: Expected b (menu `File Manager` tampil) ditulis lebih dulu pada langkah 19 sebagai anchor positif sidebar sebelum asersi absence menu `TAG` (Expected a) pada langkah 20 (bagian 8b butir 2).
- Urutan Verifikasi TC-GS-ROLE-226: menu `TAG` tampil (Expected a, langkah 9) mendahului absence `Role & Permission` (Expected b, langkah 10) sehingga sidebar yang sama sudah terbukti termuat.
- Aksi Sesi A pada TC-GS-ROLE-226 sampai TC-GS-ROLE-228 hanya dilakukan lewat UI karena aksi itu adalah pemicu yang diuji; hasil di Sesi B diasersi lewat sesi UI kedua (tidak memakai `P-2`).
- Langkah penghubung (S-15, bukan dari TC sumber): row action `Remove` berada di overlay `(⋯)` baris, sehingga "Klik Remove pada baris Doni Pratama" (TC-GS-ROLE-227) ditulis `Klik (⋯)` pada baris (langkah 14) lalu `Klik Remove` (langkah 15).
- Temuan untuk QA:
  - TC-GS-ROLE-228 precondition a menyatakan Doni Pratama "Manage files Read saja", sedangkan Tabel Pre-setup #10 mencatat Manage files R,D; spec menyetel Delete menjadi unchecked di hook `before`.
  - TC-GS-ROLE-226 dan TC-GS-ROLE-227 tidak menyebut cara membuktikan keadaan sidebar sebelum aksi (precondition "tanpa menu TAG" dan "menu TAG tampil"); spec tidak menambah asersi pada keadaan awal.
  - TC-GS-ROLE-226 tidak menyebut hasil Assign di Sesi A (toast); spec tidak mengasersinya.
  - Nama persis item sidebar `TAG`, `File Manager`, dan `Role & Permission` mengikuti Expected TC; labelnya belum diverifikasi ke PRD sidebar.
  - TC-GS-ROLE-227 "Klik Remove pada baris Doni Pratama" tidak menyebut overlay `(⋯)`; spec membuka overlay `(⋯)` lalu klik `Remove`.
