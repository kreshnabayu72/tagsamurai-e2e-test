---
id: TC-AC-ACTS-E2E-033-role-matrix-negatif-tanpa-akses-tag-stock-dan-sidebar
title: "Role Matrix Negatif: Tanpa Akses TAG > Stock (Distributor Tanpa Role, Partner, Client, Role Lain), Direct URL Detail SKU, dan Menu Approvals > TAG Stock Hidden untuk Distributor"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-124
  - TC-AC-ACTS-125
  - TC-AC-ACTS-126
  - TC-AC-ACTS-127
  - TC-AC-ACTS-136
  - TC-AC-ACTS-137
coverage:
  web: automated
---

# Role Matrix Negatif: Tanpa Akses TAG > Stock (Distributor Tanpa Role, Partner, Client, Role Lain), Direct URL Detail SKU, dan Menu Approvals > TAG Stock Hidden untuk Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor (tabel «Role yang diuji»; Role Matrix bagian 3a). Akun pertama (`Distributor tanpa role Manage TAG stock`) login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun berikutnya login lewat langkah eksplisit «Ganti akun» di tengah spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control).

| Urutan | Role yang diuji | Email (Pre-setup) | Env var password |
|---|---|---|---|
| 1 | Distributor tanpa role Manage TAG stock (#19) | `distributorNoRole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_NOROLE_PASSWORD` |
| 2 | Partner (#17) | `partner_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_PARTNER_PASSWORD` |
| 3 | Client (#18) | `client_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_CLIENT_PASSWORD` |
| 4 | Role Lain tanpa capability (#11) | `roleLain_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_ROLELAIN_PASSWORD` |
| 5 | Distributor Toggle ON (#9) | `distributorOn_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_ON_PASSWORD` |

Nama env baru yang harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e: `AC_DIST_NOROLE_PASSWORD`, `AC_PARTNER_PASSWORD`, `AC_CLIENT_PASSWORD`, `AC_ROLELAIN_PASSWORD`, `AC_DIST_ON_PASSWORD`.

- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data Pre-setup: Tabel Data Uji Pre-setup sesuai akun pada tabel «Role yang diuji»; URL Detail SKU `Fixture.tagStock.skuRfid` (#12) diketahui.
- Data seed milik spec (Subject bersuffix `{runId}-033`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): untuk TC-AC-ACTS-136 satu Subject Register Duplicate pending dari requester lain. Selain itu spec tidak membuat, mengubah, atau menghapus data lewat UI.
- Kemampuan teknis: pembacaan Subject pending dan keanggotaan approver pool lewat fixture BE, disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Kemampuan teknis: login ke aplikasi Client untuk akun Client (aplikasi dan URL login Client disediakan tim FE karena TC hanya menyebut "aplikasi Client").
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-124: Distributor tanpa role Manage TAG stock

1. Verifikasi Dashboard Admin Console termuat
2. Perhatikan sidebar
3. Verifikasi Item sidebar TAG > Stock Hidden
4. Buka URL TAG > Stock langsung
5. Verifikasi Toast error `You don't have permission to do this.`
6. Verifikasi UI di-refresh tanpa redirect

### TC-AC-ACTS-125: Partner

7. Ganti akun: Logout, lalu login sebagai Partner (email dan password dari tabel «Role yang diuji»), lalu buka dashboard Admin Console
8. Verifikasi Dashboard Admin Console termuat
9. Perhatikan sidebar
10. Verifikasi Menu TAG > Stock tidak muncul di sidebar
11. Buka URL TAG > Stock langsung
12. Verifikasi Akses langsung ditolak dengan toast error `You don't have permission to do this.`

### TC-AC-ACTS-126: Client

13. Ganti akun: Logout, lalu login sebagai Client (email dan password dari tabel «Role yang diuji»), lalu buka aplikasi Client
14. Verifikasi Aplikasi Client termuat
15. Perhatikan menu yang tersedia
16. Verifikasi Tidak ada menu TAG > Stock
17. Buka URL Admin Console TAG > Stock langsung
18. Verifikasi Akses langsung ditolak

### TC-AC-ACTS-127 dan TC-AC-ACTS-137: Role Lain tanpa capability Manage TAG stock

19. Ganti akun: Logout, lalu login sebagai Role Lain tanpa capability (email dan password dari tabel «Role yang diuji»), lalu buka dashboard Admin Console
20. Verifikasi Dashboard Admin Console termuat
21. Perhatikan sidebar
22. Verifikasi Item sidebar TAG > Stock Hidden
23. Buka URL TAG > Stock langsung
24. Verifikasi Akses langsung ditolak dengan toast `You don't have permission to do this.`
25. Ketik URL Detail SKU langsung di address bar
26. Verifikasi Toast error `You don't have permission to do this.`
27. Verifikasi UI di-refresh agar elemen tersembunyi, tanpa redirect ke halaman unauthorized

### TC-AC-ACTS-136: Menu Approvals > TAG Stock Hidden untuk Distributor

28. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (email dan password dari tabel «Role yang diuji»), lalu buka dashboard Admin Console
29. Verifikasi Subject pending ada di Approvals untuk Principal (dibaca lewat fixture BE)
30. Perhatikan sidebar
31. Verifikasi Menu Approvals > TAG Stock tidak tampil
32. Buka URL Approvals > TAG Stock langsung
33. Verifikasi Akses langsung ditolak dengan toast `You don't have permission to do this.`
34. Verifikasi Distributor tidak pernah menjadi anggota approver pool (dibaca lewat fixture BE)

## Notes

- Spec ditulis per blok role: ganti akun menuntut Step eksplisit karena akun pertama login di hook `before` (bagian 3a, keputusan 2026-10-30).
- Urutan: TC-AC-ACTS-127 dan TC-AC-ACTS-137 memakai akun Role Lain yang sama sehingga digabung dalam satu blok; TC-AC-ACTS-136 (akun Distributor Toggle ON, menu Approvals Hidden) di akhir spec. TC-AC-ACTS-128 (item sidebar tampil untuk aktor Read, positif) ada di spec 034 (polaritas §3a).
- Langkah penghubung (S-03): Ganti akun lewat Logout dan login; membuka dashboard Admin Console untuk blok berikutnya.
- Temuan untuk QA (S-15): TC-AC-ACTS-126 menulis "Akses langsung ditolak" tanpa teks atau perilaku (toast, 403, redirect); spec mengasersi penolakan tanpa teks. TC-AC-ACTS-124 menyebut "UI di-refresh tanpa redirect" tanpa menyebut cara pengamatan; spec mengasersi URL tetap. Akun Client berada di aplikasi Client; kemampuan login ke sana disediakan tim FE. Pre-setup #18 menyebut Role Client tanpa akses Admin Console. TC-AC-ACTS-136 butir c ("Distributor tidak pernah menjadi anggota approver pool") tidak memberi langkah observasi UI; spec mengasersinya lewat pembacaan fixture BE (disediakan tim FE/BE).
