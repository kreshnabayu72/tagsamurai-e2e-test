---
id: TC-AC-ACC-E2E-058-create-peran-distributor-opsi-partner-dan-group-otomatis
title: "Create Client oleh Distributor: Opsi Partner Jaringan, Partner Dipilih, dan Tanpa Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-482
  - TC-AC-ACC-483
  - TC-AC-ACC-69
coverage:
  web: automated
---

# Create Client oleh Distributor: Opsi Partner Jaringan, Partner Dipilih, dan Tanpa Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Total Control PT Distribusi Nusantara (A-13) `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD`. Login akun Distributor Total Control PT Distribusi Nusantara di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Partner Suspended `CV Mitra Beku` (P-ROL-2, Tabel A3) tersedia dan tidak boleh muncul di opsi. Partner jaringan PT Distribusi Nusantara: CV Mitra Sejati, CV Mitra Lestari; CV Mitra Timur adalah jaringan PT Distribusi Timur.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-058@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: `PT Jaringan Menteng {runId}-058` (Partner `CV Mitra Sejati`, Default User `Hendra Wijaya`), `PT Distributor Langsung {runId}-058` (tanpa Partner).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-482 dan TC-483: Opsi Partner dan Create dengan Partner

1. Klik `[+ New Client]`
2. Lihat field Partner pada Section "Partner & Group"
3. Verifikasi field Partner menampilkan placeholder "Select partner(s) (optional)" dan tanpa pilihan
4. Buka dropdown Partner
5. Verifikasi opsi memuat CV Mitra Sejati dan CV Mitra Lestari
6. Verifikasi "CV Mitra Timur" tidak ada di opsi
7. Verifikasi "CV Mitra Beku" (Suspended) tidak ada di opsi
8. Isi Company Name `PT Jaringan Menteng {runId}-058`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Hendra Wijaya dengan Email `hendra.wijaya+{runId}-058@qwertysystem.net`
9. Pilih Partner "CV Mitra Sejati"
10. Verifikasi field Select Group tidak tampil setelah Partner dipilih
11. Klik `[Submit]`
12. Verifikasi toast sukses "Success, client has been created."
13. Ketik Search `PT Jaringan Menteng {runId}-058`, tekan Enter
14. Verifikasi baris "PT Jaringan Menteng {runId}-058" di sub-tab Active: Managed By "CV Mitra Sejati"
15. Verifikasi baris "PT Jaringan Menteng {runId}-058" di sub-tab Active: Group "Cabang Menteng"

### TC-69: Create tanpa Partner

16. Klik `[+ New Client]`
17. Isi Company Name `PT Distributor Langsung {runId}-058`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Partner dikosongkan
18. Verifikasi field Select Group tidak tampil
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, client has been created."
21. Ketik Search `PT Distributor Langsung {runId}-058`, tekan Enter
22. Verifikasi baris "PT Distributor Langsung {runId}-058": Managed By "Direct"
23. Verifikasi baris "PT Distributor Langsung {runId}-058": Group "Area Jakarta" (Group otomatis milik Distributor)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): Search nama unik sebelum verifikasi baris.
- Temuan untuk QA:
  - TC-69 Expected butir a ("Group otomatis milik Distributor ('Area Jakarta')") diasersi lewat kolom Group List (butir c) karena field Select Group tersembunyi tidak punya nilai tampil.
