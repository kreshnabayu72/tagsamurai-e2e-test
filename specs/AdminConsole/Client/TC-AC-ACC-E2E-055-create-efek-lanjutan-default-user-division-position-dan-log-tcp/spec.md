---
id: TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp
title: "Efek Lanjutan Create Client: Default User Not Yet Activated, Division, Position, dan Tiga Log (Total Control)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-131
  - TC-AC-ACC-132
  - TC-AC-ACC-133
  - TC-AC-ACC-134
  - TC-AC-ACC-492
coverage:
  web: automated
---

# Efek Lanjutan Create Client: Default User Not Yet Activated, Division, Position, dan Tiga Log (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-055@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: `PT Log Uji {runId}-055` (Default User `Budi Log`, Email `budi.log+{runId}-055@qwertysystem.net`, Division `Finance`, Position kosong), `PT Seed Divisi {runId}-055` (Default User `Rizal Fauzi`, Email `rizal.fauzi+{runId}-055@qwertysystem.net`, Division `Finance`, Position `Operations Lead`).
- Kemampuan teknis (disediakan tim FE/BE; TC tidak menjelaskan caranya): membuka dan membaca Global Settings tenant Client > Division, Position, dan User milik Client baru; mail-catcher untuk Default User (baseline jumlah email per alamat sebelum aksi); membaca Changelog, System Log (Settings > User > Detail akun aktor > Tab System Log), dan Activity Log Admin Console dengan Search nama Client unik (baseline nol).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### Persiapan

1. Catat baseline jumlah email di mail-catcher untuk `budi.log+{runId}-055@qwertysystem.net` (E0)
2. Klik `[+ New Client]`
3. Isi Company Name `PT Log Uji {runId}-055`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Budi Log dengan Email `budi.log+{runId}-055@qwertysystem.net`, Division `Finance`, Position kosong, Group "Cabang Menteng"
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, client has been created."
6. Ketik Search `PT Log Uji {runId}-055`, tekan Enter
7. Klik Company Name `PT Log Uji {runId}-055` untuk membuka Detail

### TC-131: Create tidak mengirim Activation Email

8. Verifikasi section Default User menampilkan status "Not Yet Activated"
9. Verifikasi section Default User tidak memiliki tombol `[Resend Activation Email]`
10. Verifikasi tidak ada Activation Email baru untuk `budi.log+{runId}-055@qwertysystem.net` (jumlah email tetap E0)

### TC-132: Division menjadi master data pertama tenant

11. Buka Global Settings tenant Client > Division
12. Verifikasi Division "Finance" ada sebagai satu-satunya Division dan ditandai default

### TC-133: Position kosong, tidak ada Position ter-seed

13. Buka Global Settings tenant Client > Position
14. Verifikasi tab Position menampilkan empty state

### TC-134: Create tercatat di tiga log

15. Buka Admin Console > Client lalu klik `[Changelog]` di toolbar List
16. Klik ikon Search di modal Changelog, ketik `PT Log Uji {runId}-055`, tekan Enter
17. Verifikasi Changelog: Action `Create`, Client Name "PT Log Uji {runId}-055", Field `Company Name`, Old Value `—`, New Value `PT Log Uji {runId}-055`, Modified By aktor
18. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `PT Log Uji {runId}-055`, tekan Enter
19. Verifikasi System Log memuat baris yang sama dengan Object `Client`
20. Buka Activity Log Admin Console, klik ikon Search, ketik `PT Log Uji {runId}-055`, tekan Enter
21. Verifikasi Activity Log memuat baris yang sama dengan Object `Client`

### TC-492: Division dan Position yang diketik menjadi master data tenant

22. Buka Admin Console > Client
23. Klik `[+ New Client]`
24. Isi Company Name `PT Seed Divisi {runId}-055`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Rizal Fauzi dengan Email `rizal.fauzi+{runId}-055@qwertysystem.net`, Division `Finance`, Position `Operations Lead`, Group "Cabang Menteng"
25. Klik `[Submit]`
26. Verifikasi toast sukses "Success, client has been created."
27. Ketik Search `PT Seed Divisi {runId}-055`, tekan Enter
28. Klik Company Name `PT Seed Divisi {runId}-055` untuk membuka Detail
29. Verifikasi Detail, section Default User: Name "Rizal Fauzi", Division "Finance", Position "Operations Lead"
30. Buka Global Settings tenant Client > Division
31. Verifikasi Division "Finance" sebagai satu-satunya Division dan kolom Code terisi (tidak kosong)
32. Buka Global Settings tenant Client > Position
33. Verifikasi Position "Operations Lead" sebagai satu-satunya Position

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 45 langkah): dua Client dibuat oleh satu role; TC-131 sampai TC-134 membagi satu Create (`PT Log Uji {runId}-055`) karena langkah dan datanya sama ("Buat Client baru"), TC-492 membuat Client kedua; tiap blok membaca surface berbeda dan tetap bermakna walau blok lain gagal.
- Langkah penghubung (S-03): Search nama unik, klik Company Name ke Detail, pindah surface.
- Temuan untuk QA:
  - Cara membuka "Global Settings tenant Client" dari Admin Console tidak dijelaskan di TC-132, TC-133, TC-492 (impersonasi, tautan, atau login Default User); spec menulis kemampuan itu sebagai "disediakan tim FE/BE" tanpa mengarang mekanisme.
  - TC-131 bertanda Manual Only (inbox email asli) di TC; spec memakai mail-catcher dengan baseline jumlah email (R-11) dan memerlukan kemampuan itu.
  - TC-134 menyebut "System Log dan Activity Log memuat baris yang sama" tanpa menyebut surface System Log; spec memakai Settings > User > Detail akun aktor > Tab System Log (mengikuti TC-540).
  - TC-132 "ditandai default" tidak menyebut bentuk penanda (badge, ikon, atau kolom); asersi memakai istilah TC.
