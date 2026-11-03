---
id: TC-AC-ACC-E2E-327-onboarding-form-inline-per-aktor-partner-distributor-active-full
title: "One-step Onboarding per Aktor: Field Partner dan Select Group untuk Partner dan Distributor, serta Pembuatan Atomik oleh Active-Full"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-511
  - TC-AC-ACC-512
  - TC-AC-ACC-441
coverage:
  web: automated
---

# One-step Onboarding per Aktor: Field Partner dan Select Group untuk Partner dan Distributor, serta Pembuatan Atomik oleh Active-Full

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun aktor pertama login di hook `before` spec ini; role berikutnya lewat ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`)):
  - Partner Total Control A-14 (CV Mitra Sejati): `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-511).
  - Distributor Total Control A-13 (PT Distribusi Nusantara): `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-512).
  - Active-Full A-15 (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng): `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script) (TC-AC-ACC-441).
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Data Uji TC-AC-ACC-441 (TC tidak memberi nilai; spec memakai nilai pola yang sama dengan spec 326): Company Name `PT Onboarding Full {runId}-327`; Nilai tetap tiap baris Data Uji: PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia/DKI Jakarta/Jakarta Selatan`; Postal Code `12190`; Division `Finance`; Product `FAMS`; Plan `Professional`; Duration `1 year`. Group `Cabang Menteng`; Default User `Budi Santoso`, Email `budi.santoso+{runId}-327@qwertysystem.net`; Start Date hari ini.
- Kemampuan teknis: mail-catcher untuk membaca inbox Default User dengan baseline jumlah email sebelum aksi (R-11); Fixture BE untuk membaca data dan menghapus Client yang dibuat (hook `after`). Tidak butuh intercept, klien HTTP, atau jam server.

## Test Steps

### Partner (TC-AC-ACC-511)

1. Buka Admin Console > Client Subscription
2. Klik `[+ Subscription]`
3. Pilih Subscription Type `New`
4. Buka field Client dan pilih opsi `+ New Client`
5. Lihat Partner dan Select Group pada form inline
6. Verifikasi field Partner tidak tampil
7. Verifikasi field Select Group tampil
8. Buka tree Select Group
9. Verifikasi tree memuat `Cabang Menteng`
10. Verifikasi `Area Surabaya` dan `Regional Timur` tidak tampil di tree
11. Tutup tree Select Group dan form Add Subscription tanpa mengisi apa pun

### Distributor tanpa Partner (TC-AC-ACC-512)

12. Ganti akun: logout, lalu login sebagai Distributor Total Control A-13
13. Buka Admin Console > Client Subscription
14. Klik `[+ Subscription]`
15. Pilih Subscription Type `New`
16. Buka field Client dan pilih opsi `+ New Client`
17. Lihat Partner dan Select Group pada form inline
18. Verifikasi field Partner tampil dan tanpa pilihan
19. Verifikasi field Select Group tidak tampil
20. Tutup form Add Subscription tanpa mengisi apa pun

### Pembuatan atomik oleh Active-Full (TC-AC-ACC-441)

21. Ganti akun: logout, lalu login sebagai Active-Full A-15
22. Catat jumlah email di inbox Default User `budi.santoso+{runId}-327@qwertysystem.net` lewat mail-catcher (baseline)
23. Buka Admin Console > Client Subscription, klik `[+ Subscription]`, pilih Subscription Type `New`, buka field Client, lalu pilih `+ New Client`
24. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Onboarding Full {runId}-327`)
25. Pilih Group `Cabang Menteng` pada tree Select Group
26. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
27. Klik `[Submit]`
28. Verifikasi toast sukses `Success, client has been created.`
29. Buka Admin Console > Client, ketik Search `PT Onboarding Full {runId}-327`, tekan Enter
30. Verifikasi Client `PT Onboarding Full {runId}-327` dan term FAMS dibuat (baris tampil di sub-tab Active dengan FAMS `Active`)
31. Buka Detail Client `PT Onboarding Full {runId}-327`
32. Verifikasi Default User dibuat (section Default User menampilkan `Budi Santoso`)
33. Periksa inbox email Default User lewat mail-catcher
34. Verifikasi Activation Email terkirim saat term Active (satu email baru dibandingkan baseline)
35. Logout, lalu login kembali sebagai Total Control (A-01)

## Notes

- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3a). TC pembuat data (TC-AC-ACC-441) di akhir; dua TC pertama tidak membuat data.
- Langkah penghubung (S-03): menutup tree/form tanpa mengisi (form belum dirty sehingga tidak ada dialog `Unsaved Changes`).
- Temuan untuk QA
  - TC-AC-ACC-441: Langkah `Pilih + New Client lalu isi form inline` tanpa Data Uji. Expected (b) `Activation Email terkirim saat term Active, bukan saat create` ambigu: bila term Active saat create (Start Date hari ini), email terkirim saat create; spec mengasersi satu email baru untuk Start Date hari ini.
  - TC-AC-ACC-511: Precondition tidak menyebut Group milik Partner selain `Cabang Menteng`; spec mengasersi hanya yang disebut Expected.
