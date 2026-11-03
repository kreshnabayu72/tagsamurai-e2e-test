---
id: TC-FA-CF-E2E-014-role-negatif-akses-halaman-tanpa-capability
title: "Role Negatif: Menu Hidden dan Akses URL Langsung Tanpa Capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-41
  - TC-FA-CF-49
coverage:
  web: automated
---

# Role Negatif: Menu Hidden dan Akses URL Langsung Tanpa Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| No-Capability (tanpa capability Manage asset master data, termasuk Group Manager tanpa capability itu) | #9 `noCapability_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha | `Spectra.env.FA_NOCAP_PASSWORD` |

- Login di hook `before` spec ini; password tidak ditulis di spec atau fixture. Nama env baru (`FA_NOCAP_PASSWORD`) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Layar awal: spec ini menguji akses halaman, sehingga hook `beforeEach` suite tidak membuka halaman Custom Fields; user berada di Fixed Asset (precondition TC-FA-CF-41 dan TC-FA-CF-49).
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data.
- Data URL: URL halaman Fixed Asset > Settings > Custom Fields dirujuk lewat fixture baru `Fixture.faCustomFields.pageUrl`; URL tidak tertulis di TC (lihat Temuan untuk QA).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-41: Item menu Settings > Custom Fields Hidden bagi role tanpa capability

1. Buka sidebar Settings
2. Verifikasi sedikitnya satu item menu Settings lain tampil pada sidebar Settings
3. Verifikasi item `Custom Fields` tidak muncul pada daftar menu Settings

### TC-FA-CF-49: Akses URL langsung menampilkan toast 403 baku tanpa redirect

4. Ketik URL halaman Settings > Custom Fields langsung pada address bar
5. Verifikasi toast error `You don't have permission to do this.` tampil
6. Verifikasi tidak ada redirect ke halaman unauthorized
7. Verifikasi tabel Custom Fields tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Spec negatif per topik akses (bagian 3a); subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka sidebar Settings) dan langkah 4 (mengetik URL).
- Langkah 2 adalah anchor absence untuk langkah 3 (bagian 8b butir 2: item menu lain pada sidebar yang sama sudah tampil). Langkah 5 (toast tampil) menjadi anchor untuk langkah 6 dan 7.
- Langkah 2 tidak ada di Expected TC-FA-CF-41; ditambahkan sebagai anchor absence yang diwajibkan konvensi (S-03).
- Temuan untuk QA:
  - TC-FA-CF-41 Expected tidak menyebut item menu Settings lain yang dipakai sebagai anchor absence; spec memverifikasi sedikitnya satu item menu Settings lain tampil tanpa menyebut namanya.
  - TC-FA-CF-49 Data Uji menulis "URL halaman Custom Fields" tanpa nilai URL; disediakan tim FE lewat fixture.
  - Email akun No-Capability mengikuti pola Pre-setup #9; nilai `{namaCompany}` untuk Company Alpha disediakan tim FE.
