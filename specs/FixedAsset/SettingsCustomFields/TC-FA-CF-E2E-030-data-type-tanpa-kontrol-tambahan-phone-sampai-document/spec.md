---
id: TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document
title: "Data Type Tanpa Kontrol Tambahan (Phone sampai Document)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-82
  - TC-FA-CF-83
  - TC-FA-CF-84
  - TC-FA-CF-85
coverage:
  web: automated
---

# Data Type Tanpa Kontrol Tambahan (Phone sampai Document)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup: tidak ada data yang dibuat atau diubah; spec hanya membuka modal Create, memilih Data Type, dan mengamati kontrol.
- Tabel Data Type uji (parameter langkah 2 sampai 4):

    | No | Data Type | TC |
    |---|---|---|
    | 1 | `Phone` | TC-FA-CF-82 |
    | 2 | `Email` | TC-FA-CF-83 |
    | 3 | `URL` | TC-FA-CF-84 |
    | 4 | `Document` | TC-FA-CF-85 |

- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Custom Field]`
2. Untuk setiap baris tabel Data Type uji pada Prerequisites (langkah 2 sampai 4; 4 iterasi): pilih Data Type baris tabel
3. Verifikasi kontrol Values, Decimal Places, dan Formula Builder tidak tampil
4. Verifikasi Placeholder, Scope, Value Type, dan Required tampil
5. Klik `[✕]`
6. Verifikasi dialog `Unsaved Changes` tampil
7. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Langkah 2 sampai 4 diulang 4 kali (satu per baris tabel Data Type uji; blok berparameter, 8b butir 7); tiap iterasi memuat `Verifikasi` per klausa Expected (S-01) tanpa langkah bersyarat; dihitung dengan ekspansi spec ini 16 langkah. Id TC per iterasi ada di kolom TC tabel Prerequisites.
- Modal Create dibuka sekali dan Data Type diganti berurutan (halaman yang sama dipakai berulang); satu-satunya kejadian menutup modal adalah langkah 5 (S-08).
- Temuan untuk QA: asersi 'Kontrol ... tidak tampil' memakai modal Create yang sudah termuat sebagai anchor permukaan; TC tidak menyebut anchor lain (8b butir 2).
