---
id: TC-FA-PREF-E2E-159-gating-plan-growth-professional-enterprise-tab-preferences-tersedia
title: "Gating Plan: Growth, Professional, dan Enterprise Memiliki Tab Preferences dengan Akses Penuh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-115
  - TC-FA-PREF-116
  - TC-FA-PREF-117
coverage:
  web: automated
---

# Gating Plan: Growth, Professional, dan Enterprise Memiliki Tab Preferences dengan Akses Penuh

## Prerequisites

- Mode: FE+BE.
- Kelas harness: h (state tenant, plan). Spec membaca state plan; tidak mengubah plan.
- Akun aktor: Total Control tiap company. Akun pertama: company plan Growth. Login di hook `before` spec ini. Pengecualian layar awal: spec menguji ketersediaan tab Preferences dari Settings > Accounting, sehingga hook `beforeEach` suite hanya menutup dialog dan spec dimulai dari halaman beranda aplikasi. Ganti akun memakai langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Company dan akun (PA-15, tiga company dengan Preferences sesuai PA-2):

  | Company | Plan | Total Control | TC |
  |---|---|---|---|
  | PA-15 (Growth) | Growth | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-115 |
  | PA-15 (Professional) | Professional | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-116 |
  | PA-15 (Enterprise) | Enterprise | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | TC-FA-PREF-117 |

  `{namaCompany}` ketiga company belum tertulis di TC; disediakan tim FE (lihat Temuan untuk QA). Password: `Spectra.env.FA_TC_PASSWORD`.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: Preferences ketiga company bernilai awal PA-2 (In-service Date Source Activation date, tidak terkunci, semua setting wajib terisi), hasil seed (butir "Seed dan pemulihan lewat API" di `suite.md`, disediakan tim FE/BE).
- State yang diubah spec: tidak ada yang disimpan. Spec mengubah In-service Date Source di form tanpa Save dan mengembalikannya ke "Activation date" (langkah 7, 16, 25).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-115: Company plan Growth memiliki tab Preferences dengan akses penuh

1. Buka Settings > Accounting
2. Klik Tab "Preferences"
3. Verifikasi Tab "Preferences" tersedia dan terbuka
4. Ubah In-service Date Source menjadi "Manual by Accounting"
5. Verifikasi field dapat diedit
6. Verifikasi `[Save changes]` Enabled
7. Kembalikan In-service Date Source ke "Activation date"

### TC-FA-PREF-116: Company plan Professional memiliki tab Preferences dengan akses penuh

8. Logout dari akun Total Control company plan Growth
9. Login sebagai Total Control company plan Professional (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`)
10. Buka Settings > Accounting
11. Klik Tab "Preferences"
12. Verifikasi Tab "Preferences" tersedia dan terbuka
13. Ubah In-service Date Source menjadi "Manual by Accounting"
14. Verifikasi field dapat diedit
15. Verifikasi `[Save changes]` Enabled
16. Kembalikan In-service Date Source ke "Activation date"

### TC-FA-PREF-117: Company plan Enterprise memiliki tab Preferences dengan akses penuh

17. Logout dari akun Total Control company plan Professional
18. Login sebagai Total Control company plan Enterprise (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`)
19. Buka Settings > Accounting
20. Klik Tab "Preferences"
21. Verifikasi Tab "Preferences" tersedia dan terbuka
22. Ubah In-service Date Source menjadi "Manual by Accounting"
23. Verifikasi field dapat diedit
24. Verifikasi `[Save changes]` Enabled
25. Kembalikan In-service Date Source ke "Activation date"

## Notes

- Kelas h (bagian 3 prinsip 13h): verifikasi baca state plan tiga company; ganti akun memakai langkah eksplisit karena tiap plan adalah company berbeda.
- Langkah penghubung (S-03): langkah 7, 8, 9, 16, 17, 18, 25 (pemulihan nilai form dan ganti akun). Pemulihan nilai form ditulis tanpa `Verifikasi` agar form tidak berakhir dirty (S-09).
- Langkah bersifat berulang per company (langkah 1 sampai 7, 10 sampai 16, 19 sampai 25) dengan parameter tabel company di Prerequisites; Verifikasi tetap satu per klausa (S-01).
- Temuan untuk QA:
  - Klausa "Field dapat diedit" (Expected b) tidak menyebut field yang dicek; spec mengasersi In-service Date Source yang diubah pada step 3 TC.
  - Nama company dan email Total Control untuk plan Growth, Professional, dan Enterprise tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}`); perlu dikonfirmasi tim FE.
