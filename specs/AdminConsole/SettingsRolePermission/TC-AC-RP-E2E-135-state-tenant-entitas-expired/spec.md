---
id: TC-AC-RP-E2E-135-state-tenant-entitas-expired
title: "State Tenant: Entitas Expired (Kontrol Tulis Enabled, Aksi Tulis Ditolak dengan Toast Baku, dan Guard Diri Sendiri)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-414
coverage:
  web: automated
---

# State Tenant: Entitas Expired (Kontrol Tulis Enabled, Aksi Tulis Ditolak dengan Toast Baku, dan Guard Diri Sendiri)

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor: Total Control Distributor Expired `totalControlExpRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dimas Prakoso`, Pre-setup #20), password dari `Spectra.env.AC_RP_EXP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (`Distributor Expired` berstatus Expired; Total Control `Dimas Prakoso`) dan #26. Pre-setup #11 sampai #18 tidak dipakai karena entitas ini Distributor.
- Data kandidat: sedikitnya satu user Standard lain pada Tab Total Control atau kandidat picker (Precondition d TC); user itu disediakan tim FE (tidak tertulis di Pre-setup TC; lihat Temuan untuk QA).
- Data Dinamis: spec ini tidak membuat entitas baru; submit ditolak server sehingga tidak ada data yang berubah, dan suffix `+{runId}-135` dan pemulihan baseline tidak dibutuhkan.
- Kemampuan teknis: intercept respons pass-through (Pre-setup #23) yang hanya mengamati status respons submit tanpa mengubahnya (disediakan tim FE; langkah 9); intercept dilepas setelah pengamatan.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_EXP_TC_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`) karena status entitas (Expired) adalah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-414: Entitas expired: kontrol tulis enabled dan aksi tulis ditolak dengan toast baku

1. Verifikasi `[+ Assign]` dan `Remove` pada baris user lain tampil Enabled
2. Hover `[+ Assign]`
3. Verifikasi tidak ada tooltip khusus entitas pada `[+ Assign]`
4. Hover `Remove` pada baris user lain
5. Verifikasi tidak ada tooltip khusus entitas pada `Remove`
6. Klik `[+ Assign]`
7. Centang satu kandidat user Standard
8. Klik `[Assign]`
9. Verifikasi respons submit Assign berstatus 403 Forbidden
10. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
11. Tutup popup Assign dengan `✕`
12. Verifikasi kandidat tidak tampil sebagai baris di Tab Total Control (tidak ada perubahan tersimpan)
13. Hover `Remove` pada baris `Dimas Prakoso`
14. Verifikasi `Remove` baris `Dimas Prakoso` Disabled dengan tooltip guard "You can't manage your own account from here."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembanding absence (bagian 8b butir 2): toast baku (respons server selesai) menjadi anchor sebelum asersi kandidat tidak tampil sebagai baris.
- Langkah penghubung (S-03): langkah 11 menutup popup Assign dengan `✕`; popup picker adalah dialog seleksi sehingga penutupan tidak menampilkan dialog `Unsaved Changes` dan seleksi dibuang (PRD baris Tutup popup, TC-AC-RP-129).
- Temuan untuk QA:
  - TC-AC-RP-414 tidak menyebut keadaan popup Assign sesudah penolakan 403; spec mengasumsikan popup tetap terbuka dengan pilihan kandidat dan menutupnya dengan `✕` (langkah 11). Bila popup tertutup sendiri, langkah penutupan tidak berlaku.
  - TC-AC-RP-414 Precondition d (user Standard lain) tidak menyebut nama user; spec menyatakan user itu disediakan tim FE.
  - TC-AC-RP-414 Expected b menyebut "submit ditolak server 403" tanpa cara mengamati status respons dari UI; spec memakai intercept pass-through (kemampuan disediakan tim FE).
  - TC-AC-RP-414 Expected a "tanpa tooltip khusus entitas" tidak menyebut hover pada kontrol selain `[+ Assign]` dan `Remove`; spec mengikuti Langkah.
