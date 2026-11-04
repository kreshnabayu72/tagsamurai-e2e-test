---
id: TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade
title: "Gating Plan Starter: Field User TAG Tidak Dirender di Popup Create, Popup Edit, dan Detail, serta Downgrade Mencabut Pairing TAG Tanpa Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-152
  - TC-GS-USER-212
  - TC-GS-USER-323
  - TC-GS-USER-324
coverage:
  web: automated
---

# Gating Plan Starter: Field User TAG Tidak Dirender di Popup Create, Popup Edit, dan Detail, serta Downgrade Mencabut Pairing TAG Tanpa Log

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`); untuk kedua akun client di bawah penyetelan flag disediakan tim FE/BE dengan mekanisme yang sama.
- Akun aktor (tidak ada di Tabel Data Uji Pre-setup; email dan client disediakan tim FE):
  - Total Control Client plan Starter: `Spectra.env.GS_PLANSTARTER_TC_PASSWORD`. Akun aktor pertama: login di hook `before`.
  - Total Control Client plan Growth khusus spec ini (terpisah dari PT Maju Bersama agar plan PT Maju Bersama tidak berubah): `Spectra.env.GS_PLANGROWTH_TC_PASSWORD`. Login lewat langkah ganti akun eksplisit.
  - Hook `after` mengembalikan sesi ke akun default suite Total Control (Siti Nurhaliza, `Spectra.env.GS_TC_PASSWORD`).
- Env var: `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`; `GS_PLANGROWTH_TC_PASSWORD` nama baru di luar daftar seragam karena TC tidak menyebut client Growth yang diturunkan).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`):
  - Client plan Starter: user `Dewi Lestari {runId}-042` (email `dewilestari+{runId}-042@qwertysystem.net`, Activated, Basic, Access `Global Settings`), pengganti Dewi Lestari Pre-setup (No. 12) yang berada di PT Maju Bersama.
  - Client plan Growth: user `John Doe {runId}-042` (email `johndoe+{runId}-042@qwertysystem.net`, Activated) dengan satu TAG user aktif dan bebas yang disediakan tim FE pada client tersebut terpasang.
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut pelaku maupun mekanismenya):
  - Menurunkan plan Client Growth ke Starter pada langkah spec; pelaku dan nama endpoint ditentukan tim FE di tahap script.
  - Memulihkan plan Client tersebut ke Growth (atau membuang client) di hook `after`.
- State global: plan Client Growth khusus spec berubah ke Starter. Suite berjalan serial (`parallel: false`, lihat `suite.md`); dipulihkan di hook `after`.

## Test Steps

### Pembukaan layar (akun Client plan Starter)

1. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-152: Plan Starter, field User TAG tidak ada di Popup Create

2. Klik `[+ User]` di Table Tools
3. Verifikasi field lain Popup Create tampil normal: Name, Email, Position, Division, dan Access
4. Verifikasi field `User TAG` tidak dirender
5. Verifikasi tombol `Scan TAG` tidak dirender
6. Klik `✕` pada header Popup Create

### TC-GS-USER-212: Plan Starter, Popup Edit tidak menampilkan field User TAG

7. Klik icon Search, ketik `Dewi Lestari {runId}-042`, tekan Enter
8. Klik (⋯) baris `Dewi Lestari {runId}-042` → `Edit`
9. Verifikasi field Name berisi `Dewi Lestari {runId}-042`
10. Verifikasi field User TAG tidak dirender
11. Klik `✕` pada header Popup Edit

### TC-GS-USER-323: Plan Starter, sub-section User TAG tidak ada di Detail

12. Klik Name `Dewi Lestari {runId}-042` di User List
13. Verifikasi General Information User Detail tampil
14. Verifikasi sub-section User TAG tidak dirender di General Information

### Ganti akun ke Client plan Growth

15. Logout dari akun Client plan Starter
16. Login sebagai Total Control Client plan Growth (`Spectra.env.GS_PLANGROWTH_TC_PASSWORD`)
17. Buka Global Settings > User > User List (sub-tab Login User)

### TC-GS-USER-324: Downgrade plan ke Starter mencabut pairing TAG tanpa log

18. Buka Modal Changelog User, cari `John Doe {runId}-042`
19. Catat jumlah baris `Unpair TAG` untuk `John Doe {runId}-042` sebagai baseline
20. Tutup Modal Changelog User
21. Turunkan plan Client Growth ke Starter (kemampuan disediakan tim FE/BE)
22. Refresh halaman User List
23. Buka Modal Changelog User, cari `John Doe {runId}-042`
24. Verifikasi jumlah baris `Unpair TAG` untuk `John Doe {runId}-042` sama dengan baseline (tidak ada baris `Unpair TAG` baru)
25. Tutup Modal Changelog User
26. Ketik Search `John Doe {runId}-042`, tekan Enter
27. Klik Name `John Doe {runId}-042` di User List
28. Verifikasi General Information User Detail tampil
29. Verifikasi sub-section User TAG tidak ada di General Information
30. Klik menu User di sidebar Global Settings
31. Klik header kolom Column Visibility (⋯) → `Setup Column...`
32. Verifikasi daftar kolom Setup Column memuat kolom `Name` (pembanding)
33. Verifikasi kolom curated `TAG` tidak tersedia di Setup Column
34. Tutup modal Setup Column dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness h (state tenant: plan Starter dan perubahan plan tier); semua TC di spec ini berkelas itu.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 34 langkah, di bawah batas sekitar 35.
- Dua konteks client dipakai berurutan dengan langkah ganti akun eksplisit (langkah 15 dan 16); blok TC-GS-USER-324 tetap bermakna walau blok Client plan Starter gagal.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 17 (pembukaan), 6 dan 11 (menutup popup tanpa perubahan), 7 (Search user seed), 15 sampai 16 (ganti akun), 19 dan 20 (baseline jumlah baris `Unpair TAG` lalu menutup modal), 21 dan 22 (pemicu downgrade lalu refresh), 25, 26 (Search nama baris persis `John Doe {runId}-042` sebelum Klik Name, supaya baris terlihat walau tabel lebih dari satu halaman), 30 sampai 31, dan 34.
- Urutan langkah di TC-GS-USER-152: butir b (field lain tampil normal) diasersi sebelum butir a (field `User TAG` dan `Scan TAG` tidak dirender) agar absence punya anchor positif pada surface yang sama (8b butir 2).
- TC-GS-USER-324 memakai asersi jumlah berbaseline (jumlah baris `Unpair TAG` John Doe sebelum dan sesudah downgrade), bukan asersi absence log (kelas g, S-05).
- Temuan untuk QA:
  - TC-GS-USER-152 Expected b "Field lain tampil normal" tidak merinci field; spec memeriksa Name, Email, Position, Division, dan Access.
  - TC-GS-USER-152, 212, dan 323 menyebut "Client plan Starter" tanpa menyebut client dan akunnya (tidak ada di Tabel Data Uji Pre-setup); disediakan tim FE (S-13).
  - TC-GS-USER-324 menyebut "plan Client diturunkan ke Starter" tanpa pelaku, akun, dan mekanisme; disediakan tim FE/BE (S-13).
  - TC-GS-USER-324 tidak menjamin ada baris Changelog John Doe sebagai anchor positif pada hasil pencarian; spec memakai jumlah baris `Unpair TAG` berbaseline.
  - TC-GS-USER-324 menyebut John Doe (Pre-setup No. 18, di PT Maju Bersama); spec memakai John Doe milik spec pada client Growth khusus agar plan PT Maju Bersama tidak berubah.
  - TC-GS-USER-324 Expected a hanya berlaku untuk baris `Unpair TAG`; hasil pencabutan pairing pada data (TAG tidak lagi terpasang) tidak punya Expected dan tidak diasersi.
