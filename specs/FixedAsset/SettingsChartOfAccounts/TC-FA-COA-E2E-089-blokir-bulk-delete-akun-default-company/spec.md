---
id: TC-FA-COA-E2E-089-blokir-bulk-delete-akun-default-company
title: "Blokir Bulk Delete: Seluruh Seleksi Akun Default Company"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-168
  - TC-FA-COA-355
coverage:
  web: automated
---

# Blokir Bulk Delete: Seluruh Seleksi Akun Default Company

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca dan tidak berubah karena Bulk Delete selalu diblokir guard (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P29 | `4-7020 – Default Gain and Loss – Shared` | Active, Used By 0, belum pernah diekspor; `SET-05` dan `SET-06` | TC-168 |
  | P30 | `CAP-7010 – Default Capitalization Offset – Main` | Active, Used By 0, belum pernah diekspor; `SET-08` | TC-168 |
  | P32 | `5-6970 – Depreciation Expense – Used Default` | Active, Used By 1 (Asset Class `Vehicles Fleet`), belum pernah diekspor; `SET-09` | TC-355 |
  | P28 | `4-7010 – Default Gain – Disposal` | Active, Used By 0; `SET-05` pada TC-355 | TC-355 |

- State global di Settings > Accounting > Preferences: hook `before` men-set `SET-05` dan `SET-06` = P29 dan `SET-08` = P30 lewat fixture BE; langkah 14 mengganti `SET-05` ke P28 dan `SET-09` ke P32; hook `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE (satu setting hanya menyimpan satu akun).
- Asset Class pemakai P32 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-168: Bulk Delete seluruh akun terpilih adalah akun default company menampilkan D-12 kelompok default company

1. Ketik Search `4-7020`, tekan Enter
2. Centang akun P29 (`4-7020`)
3. Ganti isi kotak search dengan `CAP-7010`, tekan Enter
4. Centang akun P30 (`CAP-7010`)
5. Klik Bulk `Delete`
6. Verifikasi dialog "Cannot Delete Accounts" (D-12)
7. Verifikasi kelompok default company diawali kalimat pengantar "The following are default company accounts and cannot be deleted:"
8. Verifikasi kelompok default company memuat `• 4-7020 – Default Gain and Loss – Shared` diikuti "This account is the default company account for Default Gain on Disposal, Default Loss on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it."
9. Verifikasi kelompok default company memuat `• CAP-7010 – Default Capitalization Offset – Main` diikuti "This account is the default company account for Default Capitalization Offset in Settings > Accounting > Preferences. Change the default there before deleting it."
10. Verifikasi bagian "The following were last used in a journal and cannot be deleted:" dan "The following are in use and cannot be deleted:" tidak tampil
11. Verifikasi dialog hanya memuat tombol `[OK]`
12. Klik `[OK]`
13. Verifikasi seleksi dipertahankan

### TC-FA-COA-355: Bulk Delete seluruh akun diblokir: akun Asset Class sekaligus default company hanya tampil di kelompok Asset Class dengan dua alasan (D-12)

14. Atur Default Gain on Disposal (`SET-05`) ke akun P28 dan Found Asset Credit Account (`SET-09`) ke akun P32 lewat fixture BE hingga tersimpan
15. Muat ulang halaman (F5)
16. Ketik Search `5-6970`, tekan Enter
17. Centang akun P32 (`5-6970`)
18. Ganti isi kotak search dengan `4-7010`, tekan Enter
19. Centang akun P28 (`4-7010`)
20. Klik Bulk `Delete`
21. Verifikasi dialog "Cannot Delete Accounts" (D-12) dengan tombol `[OK]`
22. Verifikasi "The following are in use and cannot be deleted:" memuat `• 5-6970 – Depreciation Expense – Used Default`
23. Verifikasi dua alasan berurutan di bawah bullet itu: kalimat cabang (a) "This account is used by 1 Asset Class and cannot be deleted." lalu satu kalimat cabang (b) "This account is the default company account for Found Asset Credit Account in Settings > Accounting > Preferences. Change the default there before deleting it."
24. Verifikasi kelompok default company diawali kalimat pengantar "The following are default company accounts and cannot be deleted:" lalu memuat `• 4-7010 – Default Gain – Disposal` diikuti "This account is the default company account for Default Gain on Disposal in Settings > Accounting > Preferences. Change the default there before deleting it."
25. Verifikasi akun P32 tidak diulang di kelompok default company
26. Klik `[OK]`

## Notes

- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; langkah 14 mengganti nilai Preferences untuk TC-355; "Muat ulang halaman (F5)" (langkah 15) membersihkan seleksi dan Search; `[OK]` (langkah 26) menutup dialog di akhir spec.
- Asumsi: seleksi baris bertahan saat isi Search diganti (lihat Temuan untuk QA).
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - TC tidak menyatakan apakah seleksi checkbox bertahan saat Search diganti; spec mengasumsikan bertahan.
  - Post Condition TC-168 (P29 dan P30 tetap ada, tidak ada log) dan TC-355 (P32 dan P28 tetap ada tanpa log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `CAP-7010` sudah 8 dari 15 karakter Account Code sehingga suffix tidak muat.
