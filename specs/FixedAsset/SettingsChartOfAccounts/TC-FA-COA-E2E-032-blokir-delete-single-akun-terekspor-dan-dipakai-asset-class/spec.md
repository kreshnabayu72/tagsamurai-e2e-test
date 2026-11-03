---
id: TC-FA-COA-E2E-032-blokir-delete-single-akun-terekspor-dan-dipakai-asset-class
title: "Blokir Delete Single: Akun Terekspor dan Dipakai Asset Class"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-59
  - TC-FA-COA-60
  - TC-FA-COA-129
  - TC-FA-COA-130
  - TC-FA-COA-136
coverage:
  web: automated
---

# Blokir Delete Single: Akun Terekspor dan Dipakai Asset Class

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup, seluruhnya hanya dibaca dan tidak berubah karena Delete selalu diblokir guard (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Active, Used By 0, Last Used in Journal Aug 2026 | TC-59 |
  | P4 | `1-1002 – Equipment – Legacy Code` | Inactive, Used By 0, Last Used in Journal Mar 2025 | TC-60 |
  | P6 | `5-6002 – Depreciation Expense – Warehouse` | Active, Used By 1, belum pernah diekspor | TC-129 |
  | P7 | `4-7002 – Gain and Loss on Disposal` | Active, Used By 2, belum pernah diekspor | TC-130 |
  | P8 | `1-2001 – Accumulated Depreciation – Equipment` | Active, Used By 2, Last Used in Journal Sep 2026 | TC-136 |

- Asset Class pemakai P6, P7, dan P8 serta riwayat ekspor P2, P4, dan P8 disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-59: Delete akun yang pernah diekspor ditolak Guard 1 dengan dialog D-05 dan saran Deactivate

1. Ketik Search `6-2001`, tekan Enter
2. Klik row action `Delete` pada akun P2 (`6-2001`)
3. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 6-2001 – Repairs & Maintenance Expense`
4. Verifikasi teks "This account was last used in a journal in Aug 2026. Deleting it may break historical records."
5. Verifikasi teks "Deactivate it instead."
6. Verifikasi tombol `[OK]`
7. Klik `[OK]`

### TC-FA-COA-60: Akun Inactive yang pernah diekspor ditolak Guard 1 tanpa baris saran

8. Ganti isi kotak search dengan `1-1002`, tekan Enter
9. Klik row action `Delete` pada akun P4 (`1-1002`)
10. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 1-1002 – Equipment – Legacy Code`
11. Verifikasi teks "This account was last used in a journal in Mar 2025. Deleting it may break historical records."
12. Verifikasi tidak ada baris ketiga pada dialog
13. Verifikasi tombol `[OK]`
14. Klik `[OK]`

### TC-FA-COA-129: Delete akun yang dipakai satu Asset Class ditolak Guard 2 dengan dialog D-06

15. Ganti isi kotak search dengan `5-6002`, tekan Enter
16. Klik row action `Delete` pada akun P6 (`5-6002`)
17. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 5-6002 – Depreciation Expense – Warehouse`
18. Verifikasi teks "This account is used by 1 Asset Class and cannot be deleted."
19. Verifikasi tombol `[OK]`
20. Klik `[OK]`

### TC-FA-COA-130: Delete akun yang dipakai dua Asset Class menampilkan bentuk jamak D-06

21. Ganti isi kotak search dengan `4-7002`, tekan Enter
22. Klik row action `Delete` pada akun P7 (`4-7002`)
23. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 4-7002 – Gain and Loss on Disposal`
24. Verifikasi teks "This account is used by 2 Asset Classes and cannot be deleted."
25. Verifikasi tombol `[OK]`
26. Klik `[OK]`

### TC-FA-COA-136: Delete akun yang pernah diekspor dan dipakai dua Asset Class menampilkan dialog D-05 (Guard 1)

27. Ganti isi kotak search dengan `1-2001`, tekan Enter
28. Klik row action `Delete` pada akun P8 (`1-2001`)
29. Verifikasi dialog "Cannot Delete Account" dengan bullet `• 1-2001 – Accumulated Depreciation – Equipment`
30. Verifikasi teks "This account was last used in a journal in Sep 2026. Deleting it may break historical records."
31. Verifikasi kalimat pemakaian D-05 cabang (b) "This account is used by 2 Asset Classes and cannot be deleted."
32. Verifikasi tidak ada kalimat "Deactivate it instead."
33. Verifikasi tombol `[OK]`
34. Klik `[OK]`

## Notes

- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka tiap baris target; `[OK]` sesudah tiap TC menutup dialog blok sebelum Search berikutnya.
- Nilai `[Month Year]` pada TC-59 adalah `Aug 2026` (Data Uji TC), ditulis langsung pada teks dialog.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-129 dan TC-136 (akun tetap ada tanpa log) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-136 mengikuti teks PRD yang memakai kalimat D-06 cabang (b) pada D-05; catatan ini sudah ada di TC sumber dan perlu dikonfirmasi.
  - Akun Pre-setup bernama literal tanpa suffix `{runId}`; kode seperti `1-2001` adalah data Pre-setup di-seed tim FE/BE dan Account Code dibatasi 15 karakter.
