---
id: TC-AC-ACC-E2E-057-create-peran-partner-select-group-milik-partner
title: "Create Client oleh Partner: Field Partner Tersembunyi dan Select Group Hanya Memuat Group Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-68
coverage:
  web: automated
---

# Create Client oleh Partner: Field Partner Tersembunyi dan Select Group Hanya Memuat Group Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Partner Total Control CV Mitra Sejati (A-14) `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, password `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD`. Login akun Partner Total Control CV Mitra Sejati di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-057@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: `PT Mitra Menteng Uji {runId}-057` (Default User `Winda Lestari`, Email `winda.lestari+{runId}-057@qwertysystem.net`, Group `Cabang Menteng`).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`
2. Lihat Section "Partner & Group"
3. Verifikasi field Partner tidak tampil
4. Verifikasi field Select Group tampil dengan placeholder "Select group" dan tanpa node terpilih
5. Buka tree Select Group
6. Verifikasi tree memuat "Cabang Menteng"
7. Verifikasi "Area Surabaya" dan "Regional Timur" tidak tampil di tree
8. Isi Company Name `PT Mitra Menteng Uji {runId}-057`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Winda Lestari dengan Email `winda.lestari+{runId}-057@qwertysystem.net`
9. Pilih Group "Cabang Menteng" pada tree Select Group
10. Klik `[Submit]`
11. Verifikasi toast sukses "Success, client has been created."
12. Ketik Search `PT Mitra Menteng Uji {runId}-057`, tekan Enter
13. Verifikasi baris "PT Mitra Menteng Uji {runId}-057": Managed By "CV Mitra Sejati"
14. Verifikasi baris "PT Mitra Menteng Uji {runId}-057": Group "Cabang Menteng"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Search nama unik sebelum verifikasi baris.
- Temuan untuk QA:
  - Post Condition TC-68 ("Relasi Client-Partner aktif ke CV Mitra Sejati terbentuk otomatis") tidak punya langkah observasi; tidak diasersi (Managed By "CV Mitra Sejati" pada List adalah padanan Expected butir e).
  - Verifikasi "Area Surabaya" dan "Regional Timur" tidak tampil didahului Verifikasi "Cabang Menteng" tampil pada tree yang sama sebagai anchor.
