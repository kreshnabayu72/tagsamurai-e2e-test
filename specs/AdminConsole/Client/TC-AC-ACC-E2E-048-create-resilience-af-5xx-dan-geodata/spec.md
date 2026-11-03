---
id: TC-AC-ACC-E2E-048-create-resilience-af-5xx-dan-geodata
title: "Create Client: Resilience 5xx dan Geodata API Tidak Terjangkau (Active-Full)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-128
  - TC-AC-ACC-129
coverage:
  web: automated
---

# Create Client: Resilience 5xx dan Geodata API Tidak Terjangkau (Active-Full)

## Prerequisites

- Mode: FE+BE dengan intercept (`Spectra.intercept()` di atas backend nyata; bagian 6 konvensi).
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-048@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Company Name valid `PT Gagal Lima Xx {runId}-048`.
- Kebutuhan intercept: respons request Create Client dipaksa 500 lalu dipulihkan (TC-128); respons API Geodata untuk Country/State/City dipaksa gagal lalu dipulihkan (TC-129; endpoint Geodata tidak disebut TC, disediakan tim FE). Intercept dilepas segera setelah pemicu selesai; hook `after` melepas intercept yang tersisa.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-129: Geodata API tidak terjangkau

1. Paksa API Geodata gagal (intercept respons Country/State/City)
2. Klik `[+ New Client]`
3. Buka dropdown Country
4. Verifikasi dropdown Country menampilkan "Unable to load this data." dan tombol `[Try Again]`
5. Isi Company Name, PIC Name, PIC Email, Address, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; pilih Group "Area Jakarta"
6. Klik `[Submit]`
7. Verifikasi form tidak dapat disubmit selama data belum termuat (popup tetap terbuka dan tidak ada toast sukses "Success, client has been created.")
8. Lepas intercept Geodata
9. Klik `[Try Again]`
10. Verifikasi opsi Country termuat
11. Klik `[✕]` di header popup
12. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
13. Klik `[Leave]`

### TC-128: Create gagal 5xx

14. Klik `[+ New Client]`
15. Isi Company Name `PT Gagal Lima Xx {runId}-048`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Group "Area Jakarta"
16. Paksa respons request Create Client 500 (intercept)
17. Klik `[Submit]`
18. Verifikasi toast error "Error, failed to create client."
19. Verifikasi popup tetap terbuka
20. Verifikasi seluruh input dipertahankan
21. Verifikasi tombol `[Submit]` aktif kembali
22. Lepas intercept (pulihkan respons)
23. Klik `[Submit]`
24. Verifikasi toast sukses "Success, client has been created."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): TC-129 mengisi form agar percobaan submit bermakna dan menutup form dirty lewat `[✕]`, dialog `Unsaved Changes`, `[Leave]` (S-08).
- Spec bukan `Mode: mock` karena TC-128 mengasersi hasil retry pada backend nyata (Client terbentuk); intercept dipakai sebagai pemicu kegagalan.
- Temuan untuk QA:
  - TC-129 butir b ("Form tidak dapat disubmit selama data belum termuat") tidak menyebut perilaku tombol `[Submit]` (disabled atau toast); spec memverifikasi popup tetap terbuka dan tidak ada toast sukses.
