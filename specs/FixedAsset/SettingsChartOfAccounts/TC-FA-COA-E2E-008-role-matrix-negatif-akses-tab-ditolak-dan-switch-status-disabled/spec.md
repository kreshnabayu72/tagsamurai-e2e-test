---
id: TC-FA-COA-E2E-008-role-matrix-negatif-akses-tab-ditolak-dan-switch-status-disabled
title: "Role Matrix Negatif: Akses Tab Ditolak dan Switch Status Disabled"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-12
  - TC-FA-COA-163
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Tab Ditolak dan Switch Status Disabled

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (bagian 3a; spec ditulis per blok role, urutan blok = urutan tabel):

| Role | Akun | Env password | TC |
|---|---|---|---|
| Group Manager tanpa Manage accounting (akun pertama, login di hook `before`) | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GMNOACC_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; perlu didaftarkan tim FE. `FA_GM_PASSWORD` sudah terdaftar untuk akun Group Manager lain sehingga tidak dipakai) | TC-FA-COA-12 |
| Read Only | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` (terdaftar) | TC-FA-COA-163 |

- Login akun pertama (Group Manager) di hook `before` spec ini. Pengecualian atas hook `beforeEach` suite: akun Group Manager tidak punya akses ke tab Chart of Accounts, sehingga spec membuka Fixed Asset > Settings sendiri (langkah 1) dan membuka layar Chart of Accounts untuk blok Read Only lewat langkah spec (langkah 9). Hook `after` spec mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca, tidak diubah): akun P1 `5-6001 – Depreciation Expense – Admin` (Active).
- Kemampuan teknis: keyboard (Tab); membuka URL langsung tab Chart of Accounts di browser.
- Seed dan pemulihan akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-chart-of-accounts.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-12: Akses tab dan halaman ditolak untuk role tanpa Manage accounting

1. Buka Fixed Asset > Settings
2. Klik entri sidebar `Accounting`
3. Verifikasi sedikitnya satu tab lain tampil pada tab bar halaman Settings > Accounting
4. Verifikasi tab `Chart of Accounts` tidak tampil (Hidden) pada tab bar
5. Buka URL langsung tab Chart of Accounts
6. Verifikasi akses URL langsung ditolak dengan 403

### TC-FA-COA-163: Accessibility tooltip: Switch Status Disabled bagi aktor tanpa Update menampilkan tooltip saat menerima fokus keyboard

7. Logout dari akun Group Manager
8. Login sebagai Read Only
9. Buka Fixed Asset > Settings > Accounting > Chart of Accounts
10. Ketik Search `5-6001`, tekan Enter
11. Tekan Tab sampai fokus berada di Switch Status baris P1
12. Verifikasi Switch Status baris P1 Disabled
13. Verifikasi tooltip `You don't have permission to edit.` tampil saat elemen menerima fokus keyboard
14. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Role Matrix negatif (bagian 3a): TC-FA-COA-12 (tab dan URL ditolak) dan TC-FA-COA-163 (aksi ditolak, Switch Status Disabled) polaritas negatif seragam. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit dan langkah per role berbeda.
- Langkah penghubung (S-03): langkah 2 (membuka tab bar Settings > Accounting dari sidebar); langkah 7 sampai 9 (ganti akun eksplisit, S-07); langkah 10 (Search untuk menampilkan baris P1; R-16); langkah 14 (menutup Search dan mereset tabel, S-09).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 menjadi anchor positif untuk absence tab pada langkah 4 (bagian 8b butir 2). Tooltip diasersi tepat setelah fokus diterima (langkah 13) sebelum langkah berikutnya mengubah state (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-FA-COA-12 tidak menyatakan apakah entri sidebar `Accounting` tampil bagi Group Manager tanpa Manage accounting; spec mengasumsikan tampil dan sedikitnya satu tab lain pada tab bar.
  - TC-FA-COA-12 butir b ("403") tidak menyebut bentuk penolakan di browser; spec mengasersi 403 pada akses URL langsung.
  - TC-FA-COA-163 menyebut Switch Status Disabled menerima fokus keyboard; elemen berstatus disabled lazimnya tidak dapat difokus, sehingga cara fokus (atribut `aria-disabled` atau lainnya) perlu dikonfirmasi tim FE.
  - Akun Group Manager tanpa Manage accounting adalah asumsi tabel Pre-setup TC; nama env password usulan `FA_GMNOACC_PASSWORD`.
