---
id: TC-FA-COA-E2E-027-deactivate-single-pernah-diekspor-akun-default-company-dan-spinner
title: "Deactivate Single: Pernah Diekspor, Akun Default Company, dan Spinner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-48
  - TC-FA-COA-49
  - TC-FA-COA-50
  - TC-FA-COA-164
  - TC-FA-COA-286
coverage:
  web: automated
---

# Deactivate Single: Pernah Diekspor, Akun Default Company, dan Spinner

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, Used By 0, Last Used in Journal Aug 2026; hanya dibaca (dialog dibatalkan) | TC-48 |
  | P46 | `6-2102 – Repairs & Maintenance Expense – Deactivate` | Active, Used By 0, pernah diekspor; sekali pakai | TC-49 |
  | P47 | `5-6101 – Depreciation Expense – Single Deactivate` | Active, Used By 0; sekali pakai | TC-50 |
  | P88 | `5-6107 – Depreciation Expense – Spinner Deactivate` | Active, Used By 0; sekali pakai | TC-286 |
  | P113 | `4-7114 – Default Gain – Deactivate Allowed` | Active, Used By 0, nilai Default Gain on Disposal (`SET-05`) di Settings > Accounting > Preferences; sekali pakai | TC-164 |

- State global: nilai `SET-05` = P113 diset lewat fixture BE sebelum spec dan dipulihkan di hook `after`; mekanisme disediakan tim FE/BE.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request Deactivate (TC-286) di atas backend nyata; endpoint ditetapkan tim FE sesuai PRD/LLD, intercept dilepas pada langkah "Lepas tahanan respons".
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-48: Deactivate akun Active yang tidak dipakai dan pernah diekspor tetap diizinkan

1. Ketik Search `6-2001`, tekan Enter
2. Klik switch Status pada akun P2 (`6-2001`)
3. Verifikasi dialog "Deactivate Account" dengan bullet `• 6-2001 – Repairs & Maintenance Expense` dan teks "Are you sure you want to deactivate it?"
4. Verifikasi tombol `[Cancel]` dan `[Deactivate]` (severity danger)
5. Klik `[Cancel]`

### TC-FA-COA-49: Konfirmasi Deactivate single akun P46 berhasil

6. Ganti isi kotak search dengan `6-2102`, tekan Enter
7. Klik switch Status pada akun P46 sehingga dialog "Deactivate Account" (D-01) terbuka
8. Klik `[Deactivate]`
9. Verifikasi toast "Success, account has been deactivated."
10. Verifikasi switch Status P46 menjadi Inactive
11. Verifikasi akun P46 tetap di tabel

### TC-FA-COA-50: Deactivate akun P47 berhasil dan akun tetap ada di tabel

12. Ganti isi kotak search dengan `5-6101`, tekan Enter
13. Tunggu toast lama hilang otomatis
14. Klik switch Status pada akun P47 (`5-6101`)
15. Klik `[Deactivate]`
16. Verifikasi toast "Success, account has been deactivated."
17. Verifikasi switch Status P47 menjadi Inactive

### TC-FA-COA-286: Switch Status menampilkan spinner dan tidak dapat diklik selama request tertunda

18. Ganti isi kotak search dengan `5-6107`, tekan Enter
19. Tunda respons Deactivate (network delay)
20. Klik switch Status pada akun P88 (`5-6107`)
21. Klik `[Deactivate]` pada dialog D-01
22. Verifikasi switch Status P88 menampilkan spinner (ST-02)
23. Klik switch Status P88 lagi selama request tertunda
24. Verifikasi switch non-interaktif: klik kedua tidak memicu dialog atau request baru
25. Lepas tahanan respons
26. Verifikasi spinner hilang
27. Verifikasi switch menampilkan status terkini, yaitu Inactive

### TC-FA-COA-164: Deactivate akun nilai default company yang tidak dipakai Asset Class tidak diblokir

28. Ganti isi kotak search dengan `4-7114`, tekan Enter
29. Klik row action `Edit` pada akun P113 (`4-7114`)
30. Verifikasi field Account Function Enabled
31. Klik `[✕]` pada modal Edit Account
32. Tunggu toast lama hilang otomatis
33. Klik switch Status pada akun P113
34. Verifikasi dialog "Deactivate Account" (D-01) dengan bullet `• 4-7114 – Default Gain – Deactivate Allowed` dan teks "Are you sure you want to deactivate it?"
35. Verifikasi dialog bukan dialog blok D-04
36. Klik `[Deactivate]`
37. Verifikasi toast "Success, account has been deactivated."
38. Verifikasi switch Status P113 menjadi Inactive

## Notes

- Spec 38 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (Deactivate single) dengan akun sekali pakai milik blok masing-masing; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka baris target (langkah 1, 6, 12, 18, 28); `[Cancel]` pada langkah 5 menutup dialog TC-48; "Tunggu toast lama hilang otomatis" (langkah 13, 32) mencegah toast sebelumnya dengan teks sama lolos sebagai asersi.
- Urutan TC-286: asersi spinner (langkah 22) ditaruh sebelum klik kedua dan sebelum respons dilepas karena state sementara (8b.5). Status terkini pada langkah 27 adalah Inactive menurut Post Condition TC-286. Toast sesudah respons dilepas tidak diasersi karena tidak ada di Expected TC.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-49 dan TC-164 (log L-03 tiga surface, Last Used tidak berubah, dampak modul lain) dan TC-50 (Status Inactive sudah tercakup Expected) tidak punya langkah observasi di TC sehingga log tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-8214` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
