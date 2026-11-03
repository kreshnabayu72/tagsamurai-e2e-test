---
id: TC-FA-CF-E2E-154-plan-gating-happy-path-semua-tier
title: "Plan Gating: Happy Path Create, Edit, Toggle, dan Delete di Semua Tier"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-661
coverage:
  web: automated
---

# Plan Gating: Happy Path Create, Edit, Toggle, dan Delete di Semua Tier

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, akun default suite). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Setiap baris tabel di bawah dimulai dengan ganti akun eksplisit (langkah 1); hook `after` mengembalikan sesi ke akun default suite.
- Tabel "Company yang diuji" (Total Control tiap Company; email akun Starter, Growth, dan Enterprise tidak tertulis di Pre-setup TC, lihat Temuan untuk QA, disediakan tim FE). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.

| No | Company | Plan | Pre-setup | Env password |
|---|---|---|---|---|
| 1 | Company Starter | Starter | #15 | `Spectra.env.FA_TC_STARTER_PASSWORD` |
| 2 | Company Growth | Growth | #39 | `Spectra.env.FA_TC_GROWTH_PASSWORD` |
| 3 | Company Alpha | Professional | #11 | `Spectra.env.FA_TC_PASSWORD` |
| 4 | Company Enterprise | Enterprise | #39 | `Spectra.env.FA_TC_ENTERPRISE_PASSWORD` |

- Data Dinamis: Field Name `Tier Field {runId}-154` (Data Type `Text`, Scope General) dan hasil Edit `Tier Field Edit {runId}-154`; dibuat dan dihapus pada tiap Company. Cleanup di hook `after`: hapus lewat API semua field tiap Company pada tabel yang namanya memuat `{runId}-154`.
- Baseline Company: hook `before` memulihkan baseline tiap Company pada tabel (seed reset Company, disediakan tim FE/BE).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor tiap Company pada tabel dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah; field Dinamis dihapus pada langkah 19 tiap iterasi. Suite berjalan serial (`parallel: false`).

## Test Steps

Untuk setiap baris tabel "Company yang diuji" di `## Prerequisites`, lakukan langkah 1 sampai 22.

1. Ganti akun: `Logout`, lalu login sebagai Total Control Company pada baris tabel dengan password dari kolom Env password
2. Buka Fixed Asset > Settings > Custom Fields tab General
3. Klik `[+ Custom Field]`
4. Isi Field Name `Tier Field {runId}-154` dan Data Type `Text`
5. Klik `[Submit]`
6. Verifikasi toast `Success, custom field has been created.` tampil
7. Ketik Search `Tier Field {runId}-154`, tekan Enter
8. Klik row action `⋯` > `Edit` pada baris `Tier Field {runId}-154`
9. Ubah Field Name menjadi `Tier Field Edit {runId}-154`
10. Klik `[Save]`
11. Verifikasi toast `Success, custom field has been updated.` tampil
12. Geser switch Active baris `Tier Field Edit {runId}-154` ke OFF
13. Klik `[Deactivate]`
14. Verifikasi toast `Success, custom field has been deactivated.` tampil
15. Geser switch Active baris `Tier Field Edit {runId}-154` ke ON
16. Klik `[Activate]`
17. Verifikasi toast `Success, custom field has been activated.` tampil
18. Klik row action `⋯` > `Delete` pada baris `Tier Field Edit {runId}-154`
19. Klik `[Delete]` pada dialog
20. Verifikasi toast `Success, custom field has been deleted.` tampil
21. Verifikasi tidak ada dialog gating atau upsell selama langkah 3 sampai 20
22. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Langkah 1 sampai 22 diulang untuk empat baris tabel (88 langkah dengan ekspansi, di atas smell 35 langkah). Alasan: satu TC (TC-FA-CF-661) dengan empat iterasi yang identik, parameter tiap iterasi ada di tabel `## Prerequisites`, tanpa langkah bersyarat (bagian 8b butir 7). Setiap `Verifikasi` diulang satu per klausa pada tiap iterasi.
- Expected a (Starter) dan Expected b sampai d (Growth, Professional, Enterprise "perilaku dan UI identik dengan Starter") dipenuhi oleh `Verifikasi` yang sama pada tiap iterasi: teks toast yang sama untuk kelima aksi dan tidak ada dialog gating atau upsell (langkah 6, 11, 14, 17, 20, 21).
- Aktor pertama spec adalah akun default suite (Company Alpha, baris 3); karena tiap iterasi dimulai dengan ganti akun eksplisit di langkah 1, baris 3 login ulang ke akun Alpha yang sama setelah Company Growth.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (membuka tab General setelah ganti akun), langkah 7 dan 22 (Search untuk menemukan baris target dan membersihkannya, R-16).
- Temuan untuk QA:
  - Pre-setup TC memuat Company Growth dan Company Enterprise sebagai satu baris (#39) tanpa email akun, dan tidak memuat email akun Total Control Company Starter (#15); akun disediakan tim FE.
  - TC-FA-CF-661 tidak menyebut teks toast Edit, Deactivate, Activate, dan Delete; spec memakai teks toast baku modul ini dari TC lain.
