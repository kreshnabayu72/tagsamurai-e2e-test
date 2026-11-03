---
id: TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas
title: "Create Client oleh Active-Full: Partner Dipilih dan Email Default User Sama dengan User Distributor, Partner, Principal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-66
  - TC-AC-ACC-119
  - TC-AC-ACC-501
  - TC-AC-ACC-502
coverage:
  web: automated
---

# Create Client oleh Active-Full: Partner Dipilih dan Email Default User Sama dengan User Distributor, Partner, Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Partner `CV Mitra Sejati` (P1, Distributor induk PT Distribusi Nusantara, Group Distributor Area Jakarta) tersedia di opsi Partner. Email akun A-13 (`totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`), A-14 (`totalControlPartner_automated_cvMitraSejati@qwertysystem.net`), dan A-01 (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`) dipakai sebagai nilai Email Default User (NC-03).
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-045@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis (nama bersuffix): `PT Nusa Teknologi {runId}-045` (Partner CV Mitra Sejati), `PT Email Distributor Uji {runId}-045`, `PT Email Partner Uji {runId}-045`, `PT Email Principal Uji {runId}-045`.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-66: Create dengan 1 Partner, Group di-inherit

1. Klik `[+ New Client]`
2. Isi Company Name `PT Nusa Teknologi {runId}-045`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Budi Santoso, Division Finance, Position kosong
3. Pilih Partner "CV Mitra Sejati"
4. Verifikasi field Select Group tersembunyi saat Partner dipilih
5. Klik `[Submit]`
6. Verifikasi popup tertutup
7. Verifikasi toast sukses "Success, client has been created."
8. Ketik Search `PT Nusa Teknologi {runId}-045`, tekan Enter
9. Verifikasi Client "PT Nusa Teknologi {runId}-045" muncul di sub-tab Active
10. Verifikasi Client Code berformat `CLT-XXXXXXXX` (8 karakter acak tanpa 0, O, 1, I, L)
11. Verifikasi kolom Managed By "CV Mitra Sejati"
12. Verifikasi kolom Group mengikuti Group Distributor induk ("Area Jakarta")
13. Verifikasi kolom FAMS, SAMS, dan SIEM menampilkan "No Subscription"

### TC-119: Email Default User sama dengan user Distributor diterima

14. Klik `[+ New Client]`
15. Isi Company Name `PT Email Distributor Uji {runId}-045`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Maya Puspita dengan Email `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`
16. Pilih Group "Area Jakarta" pada tree Select Group
17. Verifikasi tidak ada pesan "Email already exists" di bawah Email
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, client has been created."

### TC-501: Email Default User sama dengan user Partner diterima

20. Klik `[+ New Client]`
21. Isi Company Name `PT Email Partner Uji {runId}-045`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Nina Rahma dengan Email `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`
22. Pilih Group "Area Jakarta" pada tree Select Group
23. Verifikasi tidak ada pesan "Email already exists" di bawah Email
24. Klik `[Submit]`
25. Verifikasi toast sukses "Success, client has been created."

### TC-502: Email Default User sama dengan user Principal diterima

26. Klik `[+ New Client]`
27. Isi Company Name `PT Email Principal Uji {runId}-045`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Oki Firmansyah dengan Email `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`
28. Pilih Group "Area Jakarta" pada tree Select Group
29. Verifikasi tidak ada pesan "Email already exists" di bawah Email
30. Klik `[Submit]`
31. Verifikasi toast sukses "Success, client has been created."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Search `PT Nusa Teknologi {runId}-045` menemukan baris target sebelum verifikasi kolom.
- Email akun A-13, A-14, dan A-01 dipakai sebagai nilai Email Default User untuk Client baru; Default User baru tidak mengubah akun aktor tersebut (NC-03: email milik user Distributor, Partner, atau Principal diterima).
- Temuan untuk QA:
  - Post Condition TC-66 butir a sampai d (relasi Client-Partner aktif, Default User tanpa App Access dan tanpa Activation Email, Division "Finance" menjadi master data Division pertama tenant tanpa Position ter-seed, Changelog Create tercatat) tidak punya langkah observasi di TC-66; tidak diasersi di spec ini. Sebagian terobservasi di spec efek lanjutan Default User (TC-131 sampai TC-134, TC-492).
  - TC-119, TC-501, TC-502 memakai nilai Email Default User yang sama dengan email akun aktor pada Tabel A1; mekanisme Global Settings tenant Client untuk Default User baru tidak dijelaskan TC.
