---
id: TC-AC-ACC-E2E-325-onboarding-screening-form-inline-dan-validasi-duplikat
title: "One-step Onboarding: Screening Form Inline Tanpa Field Position, Company Name Duplikat, dan Email Default User Milik Client Lain Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-509
  - TC-AC-ACC-516
  - TC-AC-ACC-517
coverage:
  web: automated
---

# One-step Onboarding: Screening Form Inline Tanpa Field Position, Company Name Duplikat, dan Email Default User Milik Client Lain Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Data Uji: Nilai tetap tiap baris Data Uji: PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia/DKI Jakarta/Jakarta Selatan`; Postal Code `12190`; Division `Finance`; Product `FAMS`; Plan `Professional`; Duration `1 year`. Start Date hari ini; Group `Cabang Menteng` (tree Select Group). TC-AC-ACC-516: Company Name `PT Sejahtera Abadi` (Pre-setup C-01, duplikat), Default User `Dewi Anggraini`, Email `dewi.anggraini+{runId}-325@qwertysystem.net`. TC-AC-ACC-517: Company Name `PT Onboarding Email Kembar {runId}-325`, Default User `Sari Pratiwi`, Email `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` (email A-16 milik Default User C-01, Tabel A1).
- Kemampuan teknis: Fixture BE untuk membaca daftar Client (state data: tidak ada Client baru). Tidak ada data yang berhasil dibuat; tidak butuh intercept, klien HTTP, atau jam server.

## Test Steps

### Screening form inline (TC-AC-ACC-509)

1. Buka Admin Console > Client Subscription
2. Klik `[+ Subscription]`
3. Pilih Subscription Type `New`
4. Buka field Client dan pilih opsi `+ New Client`
5. Lihat field pada form inline
6. Verifikasi form inline memuat field Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Select Group, First Name, Last Name, Email, dan Division
7. Verifikasi tidak ada field Position

### Company Name duplikat (TC-AC-ACC-516)

8. Ketik Company Name `PT Sejahtera Abadi` pada form inline
9. Tunggu 1 detik
10. Verifikasi pesan error inline di bawah Company Name `Company name already exists`
11. Isi PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division sesuai tabel Data Uji
12. Pilih Group `Cabang Menteng` pada tree Select Group
13. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
14. Klik `[Submit]`
15. Verifikasi form tetap terbuka
16. Verifikasi tidak ada Client dan subscription baru dibuat (Company Name `PT Sejahtera Abadi` tetap satu baris; dibaca lewat Fixture BE)
17. Verifikasi tidak ada toast sukses

### Email Default User milik Client lain (TC-AC-ACC-517)

18. Ganti isi Company Name dengan `PT Onboarding Email Kembar {runId}-325`
19. Ganti isi field Email dengan `clientDefaultUser_automated_ptSejahteraAbadi@qwertysystem.net` tanpa memindahkan fokus
20. Tunggu 1 detik
21. Verifikasi pesan error inline di bawah Email `Email already exists`
22. Ganti isi First Name dan Last Name dengan `Sari` dan `Pratiwi`
23. Klik `[Submit]`
24. Verifikasi form tetap terbuka
25. Verifikasi tidak ada Client `PT Onboarding Email Kembar {runId}-325` dan subscription baru dibuat (dibaca lewat Fixture BE; Client `PT Sejahtera Abadi` tetap terbaca sebagai anchor)
26. Verifikasi tidak ada toast sukses

### Tutup form dirty

27. Klik `✕` pada form Add Subscription
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

## Notes

- Urutan blok mengikuti prinsip 3: screening, lalu validasi yang diblokir; tidak ada aksi sukses sehingga tidak ada data yang dibuat. Form dibuka sekali karena ketiga TC memakai form yang sama; field diganti antar TC (S-03). Satu pembukaan form, satu kejadian menutup (S-08, prinsip 6).
- Pada TC-AC-ACC-517 nilai Company Name diganti ke nama unik bersuffix karena Company Name `PT Sejahtera Abadi` dari TC-AC-ACC-516 masih berisi; First Name/Last Name `Sari`/`Pratiwi` mengikuti Data Uji TC-AC-ACC-517.
- Temuan untuk QA
  - TC-AC-ACC-517: Langkah 4 menyebut `tanpa memindahkan fokus`; spec mengikuti dengan mengetik Email lalu menunggu 1 detik tanpa pindah field.
  - TC-AC-ACC-509: Precondition tidak menyebut apakah Position memang tidak ada di semua role; spec mengasersi hanya untuk Total Control.
  - Dialog `Unsaved Changes` saat menutup form Add Subscription dengan form dirty tidak disebut TC-AC-ACC-509/516/517; spec mengikuti S-08 (bentuk kanonis aplikasi).
