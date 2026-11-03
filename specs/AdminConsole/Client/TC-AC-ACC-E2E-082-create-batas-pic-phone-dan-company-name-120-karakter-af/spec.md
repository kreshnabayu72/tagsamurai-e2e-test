---
id: TC-AC-ACC-E2E-082-create-batas-pic-phone-dan-company-name-120-karakter-af
title: "Create Client: PIC Phone 4 dan 15 Digit Diterima serta Company Name Tepat 120 Karakter (Active-Full)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-111
  - TC-AC-ACC-112
coverage:
  web: automated
---

# Create Client: PIC Phone 4 dan 15 Digit Diterima serta Company Name Tepat 120 Karakter (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-082@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong.
- Dataset Dinamis: Company Name tepat 120 karakter termasuk suffix (diawali `PT Batas Nama ` dan diakhiri ` {runId}-082`, dengan huruf `A` di tengah hingga tepat 120 karakter); Default User `Maya Sari`.
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`

### TC-111: PIC Phone 4 digit dan 15 digit diterima

2. Ketik `1234` ke field PIC Phone
3. Verifikasi tidak ada pesan error pada PIC Phone (batas minimum 4 digit)
4. Ganti isi PIC Phone dengan `123456789012345`
5. Verifikasi tidak ada pesan error pada PIC Phone (batas maksimum 15 digit)

### TC-112: Company Name tepat 120 karakter diterima

6. Isi Company Name tepat 120 karakter (`PT Batas Nama ` + huruf `A` pengisi + ` {runId}-082`), PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name `Maya`, Last Name `Sari`, Email `maya.sari+{runId}-082@qwertysystem.net`, dan Division sesuai Data valid Create; pilih Group "Area Jakarta"
7. Verifikasi tidak ada pesan error pada Company Name
8. Klik `[Submit]`
9. Verifikasi toast sukses "Success, client has been created."

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- TC-111 dan TC-112 memakai popup yang sama (satu kejadian menutup: submit sukses TC-112). Nilai PIC Phone `123456789012345` dari TC-111 tetap terisi saat TC-112 dan valid.
- Nilai "tepat 120 karakter" dihitung termasuk suffix (R-06).
- Temuan untuk QA:
  - TC-112 Expected hanya menyebut "Client berhasil dibuat" lewat toast; tidak ada verifikasi baris List, sehingga spec tidak menambahkannya.
