---
id: TC-GS-USER-E2E-019-isolasi-entitas-visibilitas-data-staff-distributor-dan-opsi-access-principal
title: "Isolasi Entitas: User Client Lain Tidak Tampil, User List Distributor Tanpa Staff Partner, dan Opsi Access Create User Principal Hanya Admin Console dan Global Settings"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-85
  - TC-GS-USER-86
  - TC-GS-USER-87
coverage:
  web: automated
---

# Isolasi Entitas: User Client Lain Tidak Tampil, User List Distributor Tanpa Staff Partner, dan Opsi Access Create User Principal Hanya Admin Console dan Global Settings

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`). Flag ini disetel untuk akun aktor suite; untuk akun entitas lain di tabel di bawah, flag `gs-user` = seen disediakan tim FE/BE agar walkthrough tidak menutupi layar.
- Kelas harness: multi-konteks (beberapa entitas/tenant dalam satu spec dengan langkah ganti akun eksplisit).
- Akun yang diuji (tiap akun memakai kredensialnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps). Akun entitas lain tidak ada di Tabel Data Uji Pre-setup TC (hanya Client PT Maju Bersama, Client PT Sinar Abadi, dan Principal yang disebut di No. 26), sehingga disediakan tim FE termasuk alamat emailnya:

| Entitas | Role | Akun | Env var password | TC |
|---|---|---|---|---|
| Client B `PT Sinar Abadi` | Total Control | disediakan tim FE | `Spectra.env.GS_CLIENTB_TC_PASSWORD` | TC-GS-USER-85 (anchor data) |
| Client A `PT Maju Bersama` | Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 2) | akun default suite | `Spectra.env.GS_TC_PASSWORD` | TC-GS-USER-85 |
| Distributor | Total Control | disediakan tim FE | `Spectra.env.GS_DISTRIBUTOR_TC_PASSWORD` | TC-GS-USER-86 |
| Principal | Total Control | disediakan tim FE | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` | TC-GS-USER-87 |

- Login akun Client B (aktor pertama spec) dilakukan di hook `before`; akun lain memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Principal, hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_CLIENTB_TC_PASSWORD`, `GS_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data (hanya dibaca; spec tidak membuat, mengubah, atau menghapus data), disediakan tim FE karena tidak ada di Tabel Pre-setup selain yang tertulis: user `Teguh Santoso` milik Client B `PT Sinar Abadi` (email unik global; TC-GS-USER-85 precondition c); Dewi Lestari (Pre-setup No. 12) milik Client A sebagai data pembanding; entitas Distributor dengan daftar staff Distributor sendiri (sedikitnya satu staff Distributor seed; nama disediakan tim FE, dipakai sebagai pembanding langkah 10) dan Partner di bawah Distributor yang punya staff `Hari Susanto` (TC-GS-USER-86 precondition b); entitas Principal.
- Kemampuan teknis: login akun dari beberapa entitas dalam satu spec (logout dan login ulang).
- State global yang diubah: tidak ada. Cleanup: tidak ada data dibuat; hook `after` hanya memulihkan sesi.

## Test Steps

### TC-GS-USER-85: Data visibility, user milik entitas lain tidak tampil walau email unik global

1. Klik icon Search, ketik `Teguh`, tekan Enter
2. Verifikasi baris `Teguh Santoso` tampil di User List Client B `PT Sinar Abadi`
3. Logout, login sebagai Total Control Client A `PT Maju Bersama`, lalu buka Global Settings > User > User List (sub-tab Login User)
4. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
5. Verifikasi baris `Dewi Lestari` tampil di User List Client A
6. Ganti isi kotak search dengan `Teguh`, tekan Enter
7. Verifikasi tabel menampilkan no result state
8. Verifikasi user milik `PT Sinar Abadi` (`Teguh Santoso`) tidak tampil

### TC-GS-USER-86: Distributor hanya melihat staff Distributor sendiri, tanpa staff Partner jaringannya

9. Logout, login sebagai Total Control entitas Distributor, lalu buka Global Settings > User > User List (sub-tab Login User)
10. Verifikasi baris staff Distributor seed tampil di User List
11. Verifikasi User List hanya berisi staff Distributor
12. Klik icon Search, ketik `Hari`, tekan Enter
13. Verifikasi tabel menampilkan no result state

### TC-GS-USER-87: Opsi Access Create User untuk entitas Principal hanya Admin Console dan Global Settings

14. Logout, login sebagai Total Control entitas Principal, lalu buka Global Settings > User > User List (sub-tab Login User)
15. Klik `[+ User]`
16. Klik dropdown Access
17. Verifikasi dropdown Access (multi dropdown) hanya memuat opsi `Admin Console` dan `Global Settings`
18. Klik `✕` pada header modal Create User

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec kelas c (multi-konteks: beberapa tenant); tidak ada pengecualian P-1 sampai P-5 yang dipakai.
- Urutan TC sumber dipertahankan. Akun pertama (hook `before`) adalah Client B, bukan Client A, supaya keberadaan `Teguh Santoso` terbukti lebih dulu sebagai anchor absence TC-GS-USER-85 (bagian 8b butir 2); langkah 1 dan 2 tidak ada di TC dan ditambahkan hanya sebagai anchor, bersama langkah 4 dan 5 (data pembanding Client A pada surface yang sama dengan hasil kosong), dan langkah 10 (baris staff Distributor seed sebagai pembanding asersi universal langkah 11, bagian 8b butir 2). Langkah 2, 5, dan 10 bukan klaim Expected TC.
- Langkah buka layar User List untuk akun awal tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 4 (Search untuk anchor), 3, 9, dan 14 (ganti akun beserta pembukaan User List, karena `beforeEach` tidak dijalankan ulang), 16 (membuka dropdown Access, langkah 2 TC-GS-USER-87), 18 (menutup modal Create User yang masih kosong; form kosong tidak dirty sehingga tidak ada dialog `Unsaved Changes`).
- Temuan untuk QA:
  - TC-GS-USER-85 menyebut Client `PT Sinar Abadi` dan user `Teguh Santoso` di precondition, tetapi Tabel Data Uji Pre-setup (No. 26) hanya menyebut Client PT Sinar Abadi tanpa user itu, dan akun aktor Client B tidak ada di Tabel Pre-setup; disediakan tim FE.
  - TC-GS-USER-85 Expected b ("tidak pernah tampil") tidak menyebut cara mengamati selain Search; spec mengasersi lewat Search `Teguh` pada User List Client A.
  - TC-GS-USER-86 Expected a ("User List hanya berisi staff Distributor") tidak menyebut daftar staff Distributor yang dijadikan acuan; spec membandingkan dengan staff Distributor seed yang disediakan tim FE. Precondition b menyebut staff Partner `Hari Susanto` tanpa akun atau cara membuktikan keberadaannya di spec ini.
  - TC-GS-USER-86 dan TC-GS-USER-87 menyebut "Total Control (entitas Distributor/Principal)" tanpa akun; disediakan tim FE.
  - TC-GS-USER-87 Expected menyebut "Opsi Access" tanpa menyebut placeholder atau jenis kontrol; spec memakai multi dropdown Access sesuai langkah 2 TC (buka dropdown Access) dan tidak mengasersi placeholder.
  - TC-GS-USER-87 tidak memiliki Post Condition; modal Create User ditutup lewat `✕` sebagai langkah penghubung.
