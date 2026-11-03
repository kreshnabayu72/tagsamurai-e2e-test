---
id: TC-AC-RP-E2E-034-assign-total-control-user-standard-dan-seluruh-global-role
title: "Assign Total Control: User Standard Muncul di Tab dan di Role Detail Seluruh Global Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-122
coverage:
  web: automated
---

# Assign Total Control: User Standard Muncul di Tab dan di Role Detail Seluruh Global Role

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Tabel "Global Role yang diperiksa" di akhir Prerequisites memuat 10 Global Role Principal berurut katalog A-Z (sumber: Expected TC-AC-RP-28).
- Jam server dan jam browser sinkron untuk asersi Last Updated sama dengan waktu aksi (toleransi satu menit).
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

Tabel "Global Role yang diperiksa":

| No | Global Role |
|---|---|
| 1 | `Manage device master data` |
| 2 | `Manage group` |
| 3 | `Manage hardware stock` |
| 4 | `Manage language` |
| 5 | `Manage plans & licensing` |
| 6 | `Manage preload` |
| 7 | `Manage presetup` |
| 8 | `Manage privacy policy` |
| 9 | `Manage TAG stock` |
| 10 | `Manage user and role` |

## Test Steps

### TC-AC-RP-122: Assign Total Control ke satu user Standard

1. Klik tombol "+ Assign"
2. Ketik Search `Alex Tan`, tekan Enter
3. Centang `Alex Tan`
4. Klik `[Assign]`
5. Verifikasi popup tertutup
6. Verifikasi toast "Success, Total Control has been assigned."
7. Catat waktu aksi sesaat setelah toast tampil
8. Verifikasi baris `Alex Tan` muncul di Tab Total Control
9. Verifikasi Modified By baris `Alex Tan` bernilai "Siti N"
10. Verifikasi Last Updated baris `Alex Tan` sesuai waktu aksi (toleransi satu menit)
11. Untuk setiap baris tabel "Global Role yang diperiksa" pada Prerequisites, lakukan langkah 12 sampai 15
12. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
13. Klik `⋯` pada baris Global Role tersebut lalu klik `Detail`
14. Ketik Search `Alex Tan`, tekan Enter
15. Verifikasi `Alex Tan` tampil dengan C/R/U/D penuh sesuai kolom yang berlaku untuk role tersebut
16. Pulihkan baseline: `Alex Tan` kembali Standard

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 7, 11, 12, 16 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 2, 14.
- Alasan di atas sekitar 35 langkah (bagian 8b butir 7): spec memuat satu TC; langkah 12 sampai 15 berulang tanpa percabangan untuk 10 Global Role dengan parameter tiap iterasi di tabel Prerequisites, sehingga ekspansinya sekitar 50 langkah (11 langkah awal, 4 langkah dikali 10 iterasi, 1 langkah pemulihan); tiap iterasi berdiri sendiri.
- Langkah 12 mengulang pembukaan halaman per iterasi karena klik sidebar mereset state halaman (bagian 4).
- Temuan untuk QA:
  - TC-AC-RP-122 Expected c "Role Detail tiap Global Role" tidak menyebut daftar role atau kolom yang berlaku per role; spec memakai 10 Global Role dari TC-AC-RP-28 dan asersi "C/R/U/D penuh sesuai kolom yang berlaku" tanpa merinci kolom per role (S-15).
  - TC-AC-RP-122 Expected b tidak menyebut langkah pembuka Role Detail; spec mencari baris `Alex Tan` lewat Search karena Role Detail memuat banyak baris.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
