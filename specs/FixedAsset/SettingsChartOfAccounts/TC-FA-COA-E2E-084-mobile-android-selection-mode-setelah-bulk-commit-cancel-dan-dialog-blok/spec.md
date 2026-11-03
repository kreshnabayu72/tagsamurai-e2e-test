---
id: TC-FA-COA-E2E-084-mobile-android-selection-mode-setelah-bulk-commit-cancel-dan-dialog-blok
title: "Mobile Android: Selection Mode Setelah Bulk Commit, Cancel, dan Dialog Blok"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-367
coverage:
  mobile: automated
---

# Mobile Android: Selection Mode Setelah Bulk Commit, Cancel, dan Dialog Blok

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi Android native pada emulator atau perangkat yang disediakan tim FE. `parallel: false` karena perangkat fisik bersama.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini. Pengecualian atas hook `beforeEach` suite: layar web tidak berlaku di Android, sehingga spec membuka layar Chart of Accounts sendiri. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: P6 `5-6002 – Depreciation Expense – Warehouse` (Active, Used By 1: Asset Class `Office Equipment`) dan P7 `4-7002 – Gain and Loss on Disposal` (Active, Used By 2); keduanya hanya dibaca. P109 `5-6114 – Depreciation Expense – Mobile Selection Commit` (Function Depreciation Expense, Active, Used By 0, Last Used in Journal kosong) adalah target nonaktif sekali pakai; seed idempotent mengembalikannya ke Active sebelum run berikutnya.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-367: Mobile: selection mode berakhir otomatis setelah bulk ter-commit, dan tetap aktif saat dialog di-cancel atau Dialog Blok

1. Buka Settings > Accounting, pilih tab Chart of Accounts
2. Gulir card list sampai card P6 dan P7 tampil
3. Tekan lama card P6
4. Tap card P7
5. Tekan aksi Bulk `Deactivate`
6. Verifikasi dialog blok `Cannot Deactivate Accounts` (D-04 bentuk jamak) tampil
7. Tekan `[OK]`
8. Verifikasi selection mode tetap aktif
9. Verifikasi card P6 dan P7 tetap terpilih
10. Tekan `[✕]` pada Floating Bottom Bulk Bar
11. Gulir card list sampai card P109 tampil
12. Tekan lama card P109
13. Tekan aksi Bulk `Deactivate`
14. Tekan `[Cancel]` pada dialog `Deactivate Account`
15. Verifikasi dialog tertutup
16. Verifikasi selection mode tetap aktif
17. Verifikasi card P109 tetap terpilih
18. Tekan aksi Bulk `Deactivate` lagi
19. Tekan `[Deactivate]`
20. Verifikasi toast `Success, account has been deactivated.`
21. Verifikasi selection mode berakhir otomatis
22. Verifikasi centang dan Floating Bottom Bulk Bar hilang

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 2 dan 11 (menggulir card list sampai card target; S-14); langkah 10 (keluar dari selection mode sebelum blok P109, S-09).
- Pembagian TC lintas spec: TC-FA-COA-101 dan TC-FA-COA-366 (selection mode lain) ada di spec 012.
- Temuan untuk QA:
  - TC-FA-COA-367 Post Condition ("P109 Inactive dengan log L-03; P6 dan P7 tetap Active tanpa log") tidak punya langkah observasi; hanya toast dan state selection mode yang diasersi.
  - TC-FA-COA-367 butir a menyebut dialog blok "bentuk jamak" tanpa menyebut isi bullet dan teks selain judul; spec mengasersi judul saja.
