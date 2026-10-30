---
id: TC-GS-IMPORT-E2E-184-absence-log-aktivitas-pre-commit-edit-remove-discard-tidak-menambah
title: "Absence log: aktivitas pre-commit (edit, remove, discard) tidak menambah entri Changelog Import (seed 30 entri)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-IMPORT-500
coverage:
  web: automated
---

# Absence log: aktivitas pre-commit (edit, remove, discard) tidak menambah entri Changelog Import (seed 30 entri)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai seed Changelog Import Client E (D-60) yang tidak boleh berbagi run dengan spec commit Client E tanpa pembersihan, dan draft Client E dibagikan ke seluruh admin; lihat `suite.md`.
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTE_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import untuk Client E dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE): skrip seed Changelog Import Client E 30 entri (D-60: entri ke-i bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang; Modified By `Yoga P` untuk i ganjil dan `Dimas A` untuk i genap; entri hasil commit TC lain dibersihkan); hook umur draft D-76 varian 1 (>=24 jam; `created_at` dimundurkan 25 jam, bukan menggeser jam server) sebagai pemicu agar `[Discard]` tampil (P-5a); skrip fixture reset Client E ke tanpa draft dan seeding draft D-50.
- Baseline log (S-12): total Pagination Changelog Import dicatat sebelum aksi pemicu pertama; asersi memakai kesamaan terhadap baseline (seed 30 entri sebagai keadaan awal yang dijamin hook), bukan posisi baris.
- Data Dinamis (milik spec ini; draft dibuang oleh reset): D-60 Changelog Import Client E 30 entri seed; D-50 draft Brand 12 baris `pending` Client E dari `brand-12.csv`: `Acme Corp`, `Lenovo`, `Zebra Technologies`, `Honeywell`, `Dell`, `HP Inc`, `Canon`, `Epson`, `Brother`, `Logitech`, `Cisco`, `Asus`. Nama hasil perubahan: `Acme Corp 2`.
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): bersihkan seed D-60 Client E, hapus draft Client E, dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-500: Aktivitas pre-commit tidak menambah entri Changelog Import

1. Seed Changelog Import Client E 30 entri (D-60), reset Client E ke tanpa draft, dan seed draft Brand D-50 (12 baris `pending`) dengan hook umur draft D-76 varian 1 lewat skrip fixture
2. Buka Global Settings > Import, pilih Sub-Tab Brand
3. Klik `[Changelog]`
4. Catat pagination Changelog sebagai baseline
5. Verifikasi pagination Changelog "Showing 1 - 10 of 30 items"
6. Tutup modal Changelog lewat `✕`
7. Klik row action `⋯` pada Row # 1 lalu Edit
8. Ubah Brand Name menjadi `Acme Corp 2`
9. Klik `[Save]`
10. Verifikasi toast sukses "Success, row has been updated."
11. Klik row action `⋯` pada Row # 2 lalu Remove
12. Klik `[Delete]` pada Dialog Delete Row
13. Verifikasi toast sukses "Success, row has been deleted."
14. Klik `[Discard]` pada Unsaved Banner
15. Klik `[Discard Draft]` pada Dialog Discard Draft
16. Verifikasi toast sukses "Success, draft has been discarded."
17. Verifikasi halaman kembali ke Dropzone
18. Klik `[Changelog]`
19. Verifikasi pagination Changelog tetap "Showing 1 - 10 of 30 items" sama dengan baseline langkah 4
20. Verifikasi baris pertama tetap Date `30 Sep 26` (tidak ada entri baru)

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: asersi absence (g); spec memuat aksi nyata (Edit, Remove, Discard Draft) dengan baseline sendiri, sehingga memenuhi S-05. Hook umur draft D-76 hanya pemicu (P-5a).
- Spec singkat (20 langkah) sehingga tidak melewati sekitar 35 langkah.
- Langkah penghubung (tanpa `Verifikasi`): seeding (langkah 1), pembukaan halaman dan Sub-Tab, pencatatan baseline (langkah 4), dan menutup modal Changelog (langkah 6). Asersi absence (langkah 19 dan 20) didahului toast sukses atas tiap aksi (langkah 10, 13, 16) dan Dropzone (langkah 17) sebagai anchor positif yang terhubung ke pemicu (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-IMPORT-500 Expected a dan e mengasersi pagination "of 30 items" dan baris pertama Date `30 Sep 26` sebagai angka tetap dari seed D-60; spec menambahkan baseline (langkah 4) dan mengasersi kesamaan terhadapnya, serta mempertahankan "of 30 items" sebagai keadaan awal yang dijamin seed (S-12: total Changelog tidak diasersi sebagai angka absolut kecuali keadaan seed yang disiapkan hook).
  - Post Condition TC-GS-IMPORT-500 ("draft Brand sudah di-Discard; Changelog Import tetap 30 entri") dikonfirmasi oleh Expected d dan e; tidak ada asersi tambahan.
