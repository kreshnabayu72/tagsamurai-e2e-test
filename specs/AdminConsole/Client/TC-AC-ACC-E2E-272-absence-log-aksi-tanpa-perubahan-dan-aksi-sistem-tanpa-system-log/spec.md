---
id: TC-AC-ACC-E2E-272-absence-log-aksi-tanpa-perubahan-dan-aksi-sistem-tanpa-system-log
title: "Absence Log: Edit No-Op, Bulk Suspend Baris yang Sudah Suspended, dan Aksi Sistem Send Activation Email Tidak Menulis Baris Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-431
  - TC-AC-ACC-999
coverage:
  web: automated
---

# Absence Log: Edit No-Op, Bulk Suspend Baris yang Sudah Suspended, dan Aksi Sistem Send Activation Email Tidak Menulis Baris Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Pelaku kedua (Sesi B pada TC-AC-ACC-431; hanya memicu perubahan state dan hasilnya di sesi itu tidak diasersi, sehingga memakai sesi API, bukan konteks UI kedua dan tidak memakai `P-2`): A-01 yang sama (`AC_TC_PASSWORD`) lewat Sesi API aktor; sesi API tidak dihitung sebagai sesi web (tidak mengusir sesi UI); kemampuan ini disediakan tim FE/BE dan dinyatakan di `suite.md`. Sesi UI pada TC-AC-ACC-431 adalah Sesi A.
- Data Pre-setup (Tabel A) yang diubah lalu dipulihkan lewat UI (S-06): C-11 `PT Sinar Distributor` (Active, FAMS Active; Distributor langsung `PT Distribusi Nusantara`) untuk TC-AC-ACC-431; di-Suspend oleh Sesi B lalu di-Unsuspend sebagai Post Condition TC. Efek: baris Changelog `Suspend` dan `Unsuspend` serta Last Updated bertambah.
- Data Dinamis milik spec (dibuat lewat API seeding di hook `before`, dihapus di `after`; nama bersuffix `{runId}-272`): Client "PT Kirim Awal Absence {runId}-272" (Active, belum pernah memiliki subscription, Default User Not Yet Activated dengan email `kirimawal-272+{runId}@qwertysystem.net`) untuk bagian TC-AC-ACC-999.
- Kemampuan teknis: pemicu aksi di Admin Console > Client Subscription (aktifkan term pertama FAMS mode New, terotorisasi langsung, Plan Professional, Duration 1 year(s), Start Date hari ini) lewat UI modul itu atau sesi API aktor (disediakan tim FE); pembacaan Changelog: Client dan System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log).
- Baseline (S-12): jumlah baris Action `Suspend` pada Changelog: Client untuk "PT Sinar Distributor" dicatat sebelum aksi Sesi B (N1) dan sesudahnya (N2), ukuran halaman 100; untuk TC-AC-ACC-999 jumlah baris Action `Send Activation Email` dicatat di Changelog: Client (N1, N2) dan System Log akun aktor (S1) dengan Search nama Client bersuffix unik. Asersi memakai selisih terhadap baseline, bukan angka absolut.
- State global: Changelog "PT Sinar Distributor" mendapat satu baris `Suspend` (Sesi B) dan satu baris `Unsuspend` (pemulihan) pada audit trail permanen; Changelog "PT Kirim Awal Absence {runId}-272" mendapat baris `Send Activation Email` (TC-AC-ACC-999); suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-431: Aksi tanpa perubahan atau di-skip tidak menulis log

1. Ketik Search "PT Sinar Distributor", tekan Enter, buka ⋯ baris, klik Edit, lalu klik `[Save]` tanpa mengubah field apa pun (Edit No-Op)
2. Tunggu aksi selesai (modal Edit tertutup)
3. [Sesi A] Klik ikon Changelog di toolbar List, ketik Search "PT Sinar Distributor" di modal, tekan Enter, ubah ukuran halaman menjadi 100, catat jumlah baris Action `Suspend` (N1), lalu tutup modal
4. [Sesi A] Klik sub-tab Active, ketik Search "PT Sinar Distributor", tekan Enter, centang barisnya, klik Bulk Action lalu pilih Suspend sampai dialog "Suspend Clients" terbuka
5. [Sesi B] Suspend "PT Sinar Distributor" lewat sesi API pelaku kedua hingga status Suspended tersimpan
6. [Sesi A] Klik `[Suspend]` pada dialog
7. [Sesi A] Verifikasi dialog blok Title "Unable to Suspend Clients" dengan bullet `• PT Sinar Distributor`
8. [Sesi A] Verifikasi dialog blok memuat teks "The selected clients cannot be suspended because they are already suspended, archived, or are derived clients."
9. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]`
10. [Sesi A] Verifikasi tidak ada toast sukses
11. [Sesi A] Klik `[OK]` pada dialog blok
12. [Sesi A] Verifikasi baris "PT Sinar Distributor" tetap tercentang
13. [Sesi A] Verifikasi Bulk Action Bar tetap tampil
14. [Sesi A] Klik ikon Changelog di toolbar List, ketik Search "PT Sinar Distributor" di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action `Suspend` (N2)
15. [Sesi A] Verifikasi N2 = N1 + 1 (satu baris `Suspend` dari Sesi B; Sesi A tidak menambah baris)
16. [Sesi A] Tutup modal Changelog, klik ikon (X) pada Bulk Action Bar, lalu Unsuspend "PT Sinar Distributor" (sub-tab Suspended, centang barisnya, Bulk Action → `Unsuspend`, `[Unsuspend]`)

### TC-AC-ACC-999: Aksi sistem Send Activation Email tidak ditulis di System Log akun aktor

17. Klik menu Client di sidebar, klik [Changelog] di toolbar List, ketik Search "PT Kirim Awal Absence {runId}-272" di modal, ubah ukuran halaman menjadi 100, hitung baris Action `Send Activation Email` (N1), lalu tutup modal
18. Buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Kirim Awal Absence {runId}-272", tekan Enter, dan catat jumlah baris Action `Send Activation Email` (S1)
19. Aktifkan term pertama FAMS "PT Kirim Awal Absence {runId}-272" (mode New, terotorisasi langsung, Plan Professional, Duration 1 year(s), Start Date hari ini) dari Admin Console > Client Subscription hingga term tersimpan
20. Buka Admin Console > Client, klik [Changelog] di toolbar List, ketik Search "PT Kirim Awal Absence {runId}-272" di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan hitung baris Action `Send Activation Email` (N2)
21. Verifikasi N2 = N1 + 1 (anchor positif: aksi sistem tercatat di Changelog: Client)
22. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Kirim Awal Absence {runId}-272", tekan Enter
23. Verifikasi jumlah baris Action `Send Activation Email` pada System Log tetap S1 (aksi sistem tanpa user aktor tidak tercatat di System Log)

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec absence (kelas g, bagian 3 prinsip 13 butir g): TC-AC-ACC-431 (Expected c: Sesi A tidak menambah baris `Suspend`, dengan baris Sesi B sebagai anchor positif lewat N2 = N1 + 1) dan butir d TC-AC-ACC-999 punya aksi nyata dan baseline sendiri di spec ini (S-05). TC-AC-ACC-999 terbelah antara presence (spec 268: baris `Send Activation Email` di Changelog Client dan Activity Log) dan absence (spec ini: tidak ada baris di System Log); TC-AC-ACC-999 tercantum di `sourceTc` kedua spec.
- Langkah penghubung (S-03, R-16, S-12): langkah 2 dan 16 (langkah 2 "Tunggu aksi selesai", bagian 8b butir 8; langkah 16 pemulihan Post Condition TC-AC-ACC-431, S-06), langkah 17 dan 20 (klik menu Client di sidebar atau membuka Admin Console > Client), langkah 18 dan 22 (Search nama Client bersuffix, ukuran halaman 100, dan baseline jumlah baris log pada audit trail permanen, S-14).
- Langkah 1 memakai "PT Sinar Distributor" (C-11) karena hanya itu Client yang disebut TC-AC-ACC-431; Expected TC tidak memuat butir untuk Edit No-Op sehingga tidak diasersi (S-03).
- Temuan untuk QA:
  - TC-AC-ACC-431 langkah 1 ("Edit No-Op") tidak menyebut Client dan cara melakukannya; spec memakai C-11 dan `[Save]` tanpa mengubah field.
  - TC-AC-ACC-431 langkah 4 menulis "[Sesi B] Suspend ... lewat ⋯ > Suspend" (UI); karena hasil di Sesi B tidak diasersi, spec memakai sesi API pelaku kedua (Sesi API aktor, `suite.md`).
  - TC-AC-ACC-431 Post Condition `Unsuspend "PT Sinar Distributor"` tanpa langkah observasi di TC: dilakukan sebagai pemulihan (langkah 16), tidak diasersi.
  - TC-AC-ACC-999 Expected d tidak menyebut pembanding positif pada System Log; anchor positif spec berada di Changelog: Client (langkah 21), bukan di System Log.
  - TC-AC-ACC-999 Expected d memakai Client Pre-setup C-FX14-2 di spec 268; spec ini memakai Client milik sendiri agar baseline System Log terpisah.
