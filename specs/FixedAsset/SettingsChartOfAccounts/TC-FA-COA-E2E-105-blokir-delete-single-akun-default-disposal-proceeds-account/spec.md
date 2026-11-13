---
id: TC-FA-COA-E2E-105-blokir-delete-single-akun-default-disposal-proceeds-account
title: "Blokir Delete Single: Akun Default Disposal Proceeds Account"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-369
coverage:
  web: automated
---

# Blokir Delete Single: Akun Default Disposal Proceeds Account

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, hanya dibaca dan tidak berubah karena Delete diblokir guard (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P118 | `CLR-9200 – Disposal Proceeds Clearing – Default` | Function Disposal Proceeds, Active, Used By 0, belum pernah diekspor; Default Disposal Proceeds Account (`SET-13`) | TC-369 |

- State global di Settings > Accounting > Preferences: hook `before` men-set `SET-13` = P118 lewat fixture BE; hook `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE (satu setting hanya menyimpan satu akun; butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-369: Delete akun yang menjadi Default Disposal Proceeds Account ditolak dengan D-06 (cabang b)

1. Ketik Search `CLR-9200`, tekan Enter
2. Klik row action `Delete` pada akun P118 (`CLR-9200`)
3. Verifikasi dialog "Cannot Delete Account" (D-06) dengan bullet `• CLR-9200 – Disposal Proceeds Clearing – Default`
4. Verifikasi body memuat kalimat cabang (b) "This account is the default company account for Default Disposal Proceeds Account in Settings > Accounting > Preferences. Change the default there before deleting it."
5. Verifikasi dialog hanya memuat tombol `[OK]`
6. Klik `[OK]`
7. Verifikasi dialog tertutup
8. Verifikasi tidak ada toast
9. Verifikasi akun P118 tetap tampil di tabel
10. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search Account Code untuk membuka baris target) dan langkah 10 (kosongkan Search, S-09).
- Asersi tidak ada toast ditaruh segera setelah dialog tertutup (8b.11); urutan Expected TC berubah untuk itu. Pola sama dengan spec 033.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-FA-COA-369 butir b (tidak ada entri log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Copy cabang (b) D-06 untuk Default Disposal Proceeds Account diasersi verbatim sesuai TC sumber; nama setting pada kalimat adalah usulan yang menunggu persetujuan PM (Changelog TC 2026-11-12).
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode `CLR-9200` sudah 8 dari 15 karakter Account Code.
