---
id: TC-FA-COA-E2E-002-tabel-kosong-client-tanpa-akun
title: "Tabel Kosong Client Tanpa Akun"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-2
coverage:
  web: automated
---

# Tabel Kosong Client Tanpa Akun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client yang belum memiliki akun Chart of Accounts sama sekali. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password dibaca lewat `Spectra.env.FA_TC_PASSWORD` bila akun memakai password Total Control yang sama (perlu dikonfirmasi tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite setelah login. Hook `after` spec mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Data: client tanpa akun (tidak ada identitas Pre-setup di TC); disediakan tim FE, kunci fixture ditetapkan tim FE. Spec hanya membaca; tidak membuat atau mengubah data.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` untuk akun aktor yang dipakai, termasuk akun client kosong (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client uji lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas client kosong dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-2: Tabel kosong saat belum ada akun sama sekali

1. Verifikasi ilustrasi dengan judul `No account yet` dan deskripsi `Get started by creating your first account.`
2. Verifikasi tombol `+ Account` tampil di toolbar
3. Verifikasi tidak ada tombol `+ Account` kedua di area empty state

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`.
- Mode: FE+BE.
- Layar awal: langkah "Buka tab Chart of Accounts" TC-FA-COA-2 dikerjakan hook `beforeEach` suite setelah login akun client kosong di hook `before` spec ini.
- Asersi tambahan di luar Expected TC (S-03): langkah 2 menjadi anchor positif untuk langkah 3 (bagian 8b butir 2); Expected butir b ("tombol `+ Account` tetap satu") ditulis sebagai dua `Verifikasi` (tombol di toolbar tampil, tidak diduplikasi di empty state).
- Temuan untuk QA:
  - TC-FA-COA-2 Precondition "Belum ada akun di company" tidak menyebut client atau email akun aktor; spec memakai client kosong "disediakan tim FE" tanpa email karangan (S-13).
  - Tidak ada Pre-setup untuk client tanpa akun di tabel Data Uji Pre-setup TC (hanya P23 sampai P26, P89, dan P110 untuk client uji lain).
