---
id: TC-FA-CF-E2E-143-sinkron-limit-system-dan-capability-role
title: "Sinkron Limit Plans dan Lifecycle Settings serta Capability Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-551
  - TC-FA-CF-552
  - TC-FA-CF-553
coverage:
  web: automated
---

# Sinkron Limit Plans dan Lifecycle Settings serta Capability Role

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Cap, pengguna Sarah Johnson (Pre-setup #1 dan #16) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Cap (Pre-setup #1 dan #16). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_CAP_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC; disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 4): Total Control Company Plafon (Pre-setup #17) dengan `Spectra.env.FA_TC_PLAFON_PASSWORD`. Akun ketiga (langkah 11): `Master-Crud` Company Alpha (Pre-setup #8) `masterCrud_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MCRUD_PASSWORD`; pencabutan capability dilakukan lewat sesi API Total Control Company Alpha dengan `Spectra.env.FA_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Cap (Pre-setup #16; Max custom fields per asset name 2; Asset Name `Pump` memiliki dua field Active), Company Plafon (Pre-setup #17; Master Data Count Limit 1000 dengan 1000 field), dan Company Alpha (Pre-setup #11) dengan role `Master-Crud` memegang capability Manage asset master data.
- Kemampuan teknis (disediakan tim FE): perubahan Max custom fields per asset name (Admin Console > Plans & Features > tab Global Settings), Master Data Count Limit (Admin Console > Plans & Licensing > Lifecycle Settings > System Limits), dan pencabutan capability; akun pelaku perubahan state global tidak tertulis di TC, PRD, atau LLD (S-13).
- State global: Max custom fields per asset name Company Cap diubah dari 2 ke 3, Master Data Count Limit Company Plafon dari 1000 ke 1001, dan capability Manage asset master data pengguna `Master-Crud` dicabut; hook `after` memulihkan ketiganya ke nilai baseline (2, 1000, dan capability dikembalikan) (R-08). Suite berjalan serial.
- Data Dinamis: field `Cap Pump Free {runId}-143` dan `Plafon Extra {runId}-143`, dibersihkan di hook `after`.
- Pemulihan: hook `before` memulihkan baseline Company lewat seed reset Company; hook `after` membersihkan field Dinamis milik spec dan memulihkan baseline (Last Updated dan Modified By field baseline berubah oleh aksi spec; dipulihkan seed reset).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-551: Perubahan Max custom fields per asset name di Plans and Features langsung dipakai tanpa reload

1. Ubah Max custom fields per asset name menjadi 3 di Admin Console > Plans & Features > tab Global Settings hingga tersimpan
2. Kembali ke Settings > Custom Fields, klik `[+ Custom Field]`, isi Field Name `Cap Pump Free {runId}-143`, pilih Data Type `Text` dan Scope `Specific Asset Name` dengan `Pump`, lalu klik `[Submit]`
3. Verifikasi toast `Success, custom field has been created.` tampil

### TC-FA-CF-552: Perubahan Master Data Count Limit di Lifecycle Settings langsung dipakai

4. Ganti akun: logout, lalu login sebagai Total Control Company Plafon (Pre-setup #17)
5. Naikkan Master Data Count Limit menjadi 1001 di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits hingga tersimpan
6. Kembali ke Settings > Custom Fields dan klik `[+ Custom Field]`
7. Verifikasi modal Create terbuka
8. Isi Field Name `Plafon Extra {runId}-143`, pilih Data Type `Text`, lalu klik `[Submit]`
9. Verifikasi toast `Success, custom field has been created.` tampil

### TC-FA-CF-553: Capability Manage asset master data di Settings > Role & Permission mengatur akses halaman

10. Cabut capability Manage asset master data dari pengguna `Master-Crud` lewat Settings > Role & Permission (sesi API Total Control Company Alpha) hingga tersimpan
11. Ganti akun: logout, lalu login ulang sebagai `Master-Crud` Company Alpha (Pre-setup #8)
12. Buka sidebar Settings
13. Verifikasi sidebar Settings menampilkan sedikitnya satu item lain
14. Verifikasi item `Custom Fields` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 551 (Company Cap), 552 (Company Plafon, ganti akun eksplisit pada langkah 4), 553 (Company Alpha, ganti akun pada langkah 11). TC-FA-CF-553 berakhir dengan ganti akun ke akun yang capability-nya dicabut; hook `after` memulihkan capability dan sesi.
- Pelaku perubahan state global memakai sesi API (bukan konteks kedua kelas c); langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Absence item `Custom Fields` didahului `Verifikasi` item lain pada sidebar Settings (anchor, 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 dan 11 (ganti akun eksplisit), pembukaan sidebar Settings.
- Temuan untuk QA:
  - TC-FA-CF-551 Expected "tanpa angka di-hardcode" tidak dapat diamati dari UI; spec mengasersi Create sukses saja.
  - TC-FA-CF-553 tidak menyebut item sidebar Settings lain yang dijadikan anchor dan tidak menyebut aktor yang mencabut capability; spec memakai anchor generik dan sesi API Total Control Company Alpha.
  - Indeks TC memetakan spec ini ke Pre-setup #8 (`Master-Crud`) hanya karena TC-FA-CF-553; TC-FA-CF-551 dan TC-FA-CF-552 berprecondition Total Control (login default Company Cap dan Company Plafon).
  - Email akun Total Control Company Cap dan Company Plafon tidak tertulis di Pre-setup TC; env var `FA_TC_CAP_PASSWORD` dan `FA_TC_PLAFON_PASSWORD` disediakan tim FE.
