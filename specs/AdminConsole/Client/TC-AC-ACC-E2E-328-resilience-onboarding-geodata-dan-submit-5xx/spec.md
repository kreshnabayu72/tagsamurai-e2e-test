---
id: TC-AC-ACC-E2E-328-resilience-onboarding-geodata-dan-submit-5xx
title: "Resilience One-step Onboarding: Geodata API Tidak Terjangkau dan Kegagalan 5xx Saat Submit Tidak Meninggalkan Client Parsial"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-518
  - TC-AC-ACC-442
coverage:
  web: automated
---

# Resilience One-step Onboarding: Geodata API Tidak Terjangkau dan Kegagalan 5xx Saat Submit Tidak Meninggalkan Client Parsial

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Blok kedua memakai Active-Full lewat ganti akun eksplisit.
  - Active-Full A-15 (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng) untuk TC-AC-ACC-442: `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script)
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Data Uji: Nilai tetap tiap baris Data Uji: PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia/DKI Jakarta/Jakarta Selatan`; Postal Code `12190`; Division `Finance`; Product `FAMS`; Plan `Professional`; Duration `1 year`. TC-AC-ACC-518: Company Name `PT Onboarding Geodata {runId}-328`; Default User `Dewi Anggraini`, Email `dewi.anggraini+{runId}-328@qwertysystem.net`; Group `Cabang Menteng`; Start Date hari ini. TC-AC-ACC-442: Company Name `PT Onboarding Gagal {runId}-328`; Country/State/City sesuai tabel; Default User `Hadi Wijaya`, Email `hadi.wijaya+{runId}-328@qwertysystem.net`; Group `Cabang Menteng`.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 5xx pada permintaan Geodata (TC-AC-ACC-518) dan pada permintaan submit pembuatan Client (TC-AC-ACC-442), lalu memulihkan respons normal (respons 200 untuk Geodata); endpoint tidak disebut TC (disediakan tim FE). Intercept dilepas segera setelah tiap pemicu selesai (S-09). Fixture BE untuk membaca daftar Client (state data).
- Kelas b (fault injection): satu spec resilience untuk dua kegagalan pada form onboarding.

## Test Steps

### Geodata API tidak terjangkau (TC-AC-ACC-518)

1. Paksa Geodata API gagal (intercept respons 5xx)
2. Buka Admin Console > Client Subscription
3. Klik `[+ Subscription]`
4. Pilih Subscription Type `New`
5. Buka field Client dan pilih opsi `+ New Client`
6. Lihat dropdown Country pada form inline
7. Verifikasi dropdown Country menampilkan `Unable to load this data.`
8. Verifikasi tombol `[Try Again]` tampil pada dropdown Country
9. Isi Company Name, PIC Name, PIC Email, Address, Postal Code, First Name, Last Name, Email, dan Division sesuai tabel Data Uji
10. Pilih Group `Cabang Menteng` pada tree Select Group
11. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
12. Klik `[Submit]`
13. Verifikasi form tetap terbuka
14. Verifikasi tidak ada Client `PT Onboarding Geodata {runId}-328` dan subscription baru dibuat (dibaca lewat Fixture BE; Client `PT Sejahtera Abadi` tetap terbaca sebagai anchor)
15. Verifikasi tidak ada toast sukses
16. Pulihkan Geodata API (lepas intercept, respons 200)
17. Klik `[Try Again]` pada dropdown Country
18. Verifikasi opsi Country termuat
19. Klik `✕` pada form Add Subscription
20. Verifikasi dialog `Unsaved Changes` tampil
21. Klik `[Leave]`

### Submit gagal 5xx tanpa partial (TC-AC-ACC-442)

22. Ganti akun: logout, lalu login sebagai Active-Full A-15
23. Buka Admin Console > Client Subscription
24. Klik `[+ Subscription]`
25. Pilih Subscription Type `New`
26. Buka field Client dan pilih opsi `+ New Client`
27. Isi Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, dan Division pada form inline sesuai tabel Data Uji (Company Name `PT Onboarding Gagal {runId}-328`)
28. Pilih Group `Cabang Menteng` pada tree Select Group
29. Isi Product, Plan, Duration, dan Start Date sesuai tabel Data Uji
30. Paksa submit gagal (intercept respons 5xx pada permintaan pembuatan Client)
31. Klik `[Submit]`
32. Verifikasi toast error `Error, failed to create client.`
33. Verifikasi tidak ada Client `PT Onboarding Gagal {runId}-328` tanpa subscription (dibaca lewat Fixture BE; Client `PT Sejahtera Abadi` tetap terbaca sebagai anchor)
34. Lepas intercept
35. Klik `✕` pada form Add Subscription
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik `[Leave]`
38. Logout, lalu login kembali sebagai Total Control (A-01)

## Notes

- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (fault injection pada form onboarding) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (S-03): melepas intercept dan menutup form dirty lewat `✕` + `[Leave]` (S-08); ganti akun eksplisit di blok kedua.
- Temuan untuk QA
  - TC-AC-ACC-442: Langkah dan Data Uji hanya `Paksa gagal saat submit` / `Mock 500`; nilai form dan endpoint tidak disebut; spec memakai pola Data Uji TC-AC-ACC-510. Expected `tidak ada Client tanpa subscription` memerlukan kemampuan baca state BE (disediakan tim FE/BE).
  - TC-AC-ACC-518: Expected (b) mengasumsikan [Submit] dapat diklik meski Country belum terisi; perilaku validasi form saat Country tidak termuat diasersi apa adanya (form tetap terbuka, tidak ada Client).
