---
id: TC-FA-TDC-E2E-209-role-matrix-request-langsung-delete-ditolak
title: "Role Matrix Negatif: Request Langsung Delete Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-799
  - TC-FA-TDC-800
  - TC-FA-TDC-801
  - TC-FA-TDC-802
coverage:
  web: automated
---

# Role Matrix Negatif: Request Langsung Delete Ditolak

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | TC |
|---|---|---|---|
| Read Only | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_RO_PASSWORD` | TC-FA-TDC-799 |
| Manage accounting (Read saja) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | TC-FA-TDC-800 |
| Manage accounting (Create saja) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_CREATEONLY_PASSWORD` | TC-FA-TDC-801 |
| Manage accounting (Update saja) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-TDC-802 |

- Login di hook `before` spec ini sebagai Total Control (akun default suite; password `Spectra.env.FA_TC_PASSWORD`) untuk seeding; halaman dibuka hook `beforeEach` suite. Langkah spec tidak memakai UI: request yang diuji memakai sesi API role iterasi, sedangkan setiap langkah baca (baseline dan "Baca ulang ... lewat request baca") memakai sesi API aktor Total Control (sesi seeding) karena role iterasi tidak tentu punya akses Read. Nama env pada tabel didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh penulis script.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): sesi API aktor (login API per role) dan seed serta pemulihan lewat API. Klien HTTP untuk request langsung dan request baca disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE). Kondisi awal: Class `NB-4` dengan Used By 0 tanpa Last Posted Tax Year.

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Used By 0, tanpa Last Posted Tax Year |

- Request yang diuji ditolak sehingga spec tidak mengubah data; state global tidak diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Untuk setiap role pada tabel "Role yang diuji", lakukan langkah 2 sampai 7
2. Buka sesi API aktor dengan akun role iterasi (login API memakai password pada tabel)
3. Baca jumlah versi class `NB-4` lewat request baca dengan sesi API aktor Total Control (sesi seeding) dan catat sebagai baseline
4. Kirim request langsung untuk menghapus class `NB-4` tanpa melalui UI dengan sesi API role iterasi
5. Verifikasi server menolak request dengan 403 Forbidden
6. Baca ulang daftar class lewat request baca dengan sesi API aktor Total Control (sesi seeding)
7. Verifikasi class `NB-4` tetap ada dengan jumlah versi sama dengan baseline langkah 3

## Notes

- Role Matrix negatif untuk satu aksi (Delete); polaritas seragam (bagian 3a). Perulangan atas empat role pada langkah 2 sampai 7: langkah tiap role identik dan hanya sesi API aktor yang berbeda.
- K-1: TC kelas a dengan Expected respons API tetap masuk spec FE+BE; spec hanya mengasersi status respons dan state data lewat request baca (8b.1). Tidak ada tampilan UI yang diasersi.
- Klausa Expected c TC-FA-TDC-799, TC-FA-TDC-800, TC-FA-TDC-801, dan TC-FA-TDC-802 (tidak ada entri log baru) tidak diasersi di spec ini; asersinya ada di spec absence 265 dengan aksi nyata dan baseline sendiri (S-05, P-5 butir a). Spec ini mengasersi status respons dan state data (8b.1).
- Langkah penghubung (S-03): langkah 2 (membuka sesi API aktor role iterasi) dan langkah 3 (mencatat baseline jumlah versi untuk asersi "jumlah versi yang sama").
- Sesi pembaca state: langkah baca memakai sesi API aktor Total Control (sesi seeding), bukan sesi role iterasi, supaya hasil baca tidak bergantung pada akses Read role yang diuji (8b.1).
- Temuan untuk QA:
  - Akun, email, dan company tiap role tidak tertulis di TC (tanpa nomor Pre-setup); nama env password adalah usulan.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal Example Data tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
  - Expected b "jumlah versi yang sama" tidak menyebut jumlah awal; spec mencatat baseline jumlah versi sebelum request.
