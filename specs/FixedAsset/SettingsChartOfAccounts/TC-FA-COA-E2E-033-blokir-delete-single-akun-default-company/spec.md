---
id: TC-FA-COA-E2E-033-blokir-delete-single-akun-default-company
title: "Blokir Delete Single: Akun Default Company"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-165
  - TC-FA-COA-166
  - TC-FA-COA-167
coverage:
  web: automated
---

# Blokir Delete Single: Akun Default Company

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca dan tidak berubah karena Delete selalu diblokir guard (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P29 | `4-7020 – Default Gain and Loss – Shared` | Active, Used By 0, belum pernah diekspor; Default Gain on Disposal (`SET-05`) dan Default Loss on Disposal (`SET-06`) | TC-165 |
  | P30 | `CAP-7010 – Default Capitalization Offset – Main` | Active, Used By 0, belum pernah diekspor; Default Capitalization Offset (`SET-08`) | TC-166 |
  | P31 | `3-9010 – Found Asset Credit – Other Income` | Active, Used By 0, belum pernah diekspor; Found Asset Credit Account (`SET-09`) pada TC-166 | TC-166 |
  | P32 | `5-6970 – Depreciation Expense – Used Default` | Active, Used By 1 (Asset Class `Vehicles Fleet`), belum pernah diekspor; Found Asset Credit Account (`SET-09`) pada TC-167 | TC-167 |

- State global di Settings > Accounting > Preferences: hook `before` men-set `SET-05` dan `SET-06` = P29, `SET-08` = P30, `SET-09` = P31 lewat fixture BE; langkah 26 mengganti `SET-09` ke P32; hook `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE (satu setting hanya menyimpan satu akun).
- Asset Class pemakai P32 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-165: Delete akun default company ditolak dengan D-06 (cabang b), daftar nama setting mengikuti urutan tab Preferences

1. Ketik Search `4-7020`, tekan Enter
2. Klik row action `Delete` pada akun P29 (`4-7020`)
3. Verifikasi dialog "Cannot Delete Account" (D-06) dengan bullet `• 4-7020 – Default Gain and Loss – Shared`
4. Verifikasi body memuat kalimat cabang (b) "This account is the default company account for Default Gain on Disposal, Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it."
5. Verifikasi dialog hanya memuat tombol `[OK]`
6. Klik `[OK]`
7. Verifikasi dialog tertutup
8. Verifikasi tidak ada toast
9. Verifikasi akun P29 tetap tampil di tabel

### TC-FA-COA-166: Delete akun Default Capitalization Offset atau Found Asset Credit Account ditolak dengan D-06 (cabang b)

10. Ganti isi kotak search dengan `CAP-7010`, tekan Enter
11. Klik row action `Delete` pada akun P30 (`CAP-7010`)
12. Verifikasi dialog "Cannot Delete Account" dengan bullet `• CAP-7010 – Default Capitalization Offset – Main`
13. Verifikasi body memuat kalimat cabang (b) "This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it."
14. Verifikasi dialog hanya memuat tombol `[OK]`
15. Klik `[OK]`
16. Verifikasi dialog tertutup
17. Verifikasi tidak ada toast
18. Ganti isi kotak search dengan `3-9010`, tekan Enter
19. Klik row action `Delete` pada akun P31 (`3-9010`)
20. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 3-9010 – Found Asset Credit – Other Income`
21. Verifikasi body memuat kalimat cabang (b) "This account is the default company account for Found Asset Credit Account in Settings > Accounting > Preferences. Change the default there before deleting it."
22. Verifikasi dialog hanya memuat tombol `[OK]`
23. Klik `[OK]`
24. Verifikasi dialog tertutup
25. Verifikasi tidak ada toast

### TC-FA-COA-167: Akun yang dipakai Asset Class sekaligus default company menampilkan cabang (a) lebih dahulu lalu cabang (b) dalam satu dialog D-06

26. Atur Found Asset Credit Account (`SET-09`) ke akun P32 lewat fixture BE hingga tersimpan
27. Ganti isi kotak search dengan `5-6970`, tekan Enter
28. Klik row action `Delete` pada akun P32 (`5-6970`)
29. Verifikasi satu dialog "Cannot Delete Account" dengan bullet `• 5-6970 – Depreciation Expense – Used Default`
30. Verifikasi kalimat cabang (a) "This account is used by 1 Asset Class and cannot be deleted." tampil lebih dahulu
31. Verifikasi setelah cabang (a) tampil kalimat cabang (b) "This account is the default company account for Found Asset Credit Account in Settings > Accounting > Preferences. Change the default there before deleting it."
32. Verifikasi dialog hanya memuat tombol `[OK]`
33. Klik `[OK]`
34. Verifikasi dialog tertutup
35. Verifikasi tidak ada toast

## Notes

- Spec 35 langkah. Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; langkah 26 mengganti nilai `SET-09` dari P31 ke P32 lewat fixture BE (P31 dan P32 bergantian sebagai `SET-09` menurut catatan nilai default company di TC).
- Asersi tidak ada toast ditaruh segera setelah dialog tertutup (8b.11); urutan Expected TC berubah untuk itu.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-165, TC-166, TC-167 (akun tetap ada dan Active, tidak ada entri log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Copy cabang (b) D-06 diasersi verbatim sesuai resolusi NC-09 di TC sumber.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-7010` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
