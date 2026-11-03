---
id: TC-FA-CF-E2E-021-info-popover-dan-dropdown-data-type
title: "Info Popover dan Dropdown Data Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-57
  - TC-FA-CF-58
coverage:
  web: automated
---

# Info Popover dan Dropdown Data Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup: tidak ada data yang dibuat atau diubah; spec hanya membuka, mengamati, dan menutup modal Create.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-57: Info Popover Data Type memuat penjelasan keempat belas tipe data

1. Klik `[+ Custom Field]`
2. Klik icon ℹ di samping label `Data Type *`
3. Verifikasi popover terbuka berisi 14 baris tipe data berurutan: `Text`, `Text Area`, `Dropdown`, `Multi-Dropdown`, `Date`, `DateTime`, `Currency`, `Numeric`, `Phone`, `Percentage`, `Email`, `URL`, `Document`, `Formula`
4. Verifikasi popover menjelaskan `Text`: `A field that is suitable for short entries, such as brief descriptions or any information filled in free-form, with a maximum limit of 120 characters.`
5. Verifikasi popover menjelaskan `Text Area`: `A larger text field that is ideal for more extensive descriptions, notes, or detailed information, with a maximum limit of 360 characters.`
6. Verifikasi popover menjelaskan `Dropdown`: `Creates a list of predefined options, allowing users to select one option from the list. Useful for fields with a limited set of choices.`
7. Verifikasi popover menjelaskan `Multi-Dropdown`: `Similar to a dropdown but allows users to select more than one option from the list. Ideal for scenarios where multiple choices apply.`
8. Verifikasi popover menjelaskan `Date`: `Allows users to select a specific date from a calendar interface. Suitable for date-related information such as purchase dates, warranty expirations, and more.`
9. Verifikasi popover menjelaskan `DateTime`: `Similar to the Date field but includes both date and time information. Useful when tracking events with precise timestamp.`
10. Verifikasi popover menjelaskan `Currency`: `A field specifically designed to store monetary values.`
11. Verifikasi popover menjelaskan `Numeric`: `A field used for storing numerical values, ideal for quantities, measurements, or any numeric data. It supports a leading '-' for negative numbers and a decimal point for precision.`
12. Verifikasi popover menjelaskan `Phone`: `Used specifically for storing phone numbers. Helps maintain consistency and ensures a standardized format for phone entries.`
13. Verifikasi popover menjelaskan `Percentage`: `Used for storing percentage values. Useful for tracking percentages across various metrics.`
14. Verifikasi popover menjelaskan `Email`: `Specifically used for storing email addresses. Helps maintain data integrity by ensuring entries adhere to proper email format standards.`
15. Verifikasi popover menjelaskan `URL`: `A field used for storing website addresses. Useful for linking to external resources or providing references to web-based information.`
16. Verifikasi popover menjelaskan `Document`: `A field used to store or upload document in specific file formats (PDF, DOCX, DOC, XLS, XLSX, PNG, JPG, JPEG, CSV) with maximum file size is 1 MB.`
17. Verifikasi popover menjelaskan `Formula`: `An automatically calculated field derived from standard numeric asset fields using arithmetic operators (+, −, ×, ÷) and predefined mathematical logic.`
18. Tutup popover Data Type

#### TC-FA-CF-58: Dropdown Data Type menampilkan keempat belas tipe data sesuai daftar PRD

19. Klik dropdown `Data Type *`
20. Verifikasi opsi dropdown berurutan: `Text`, `Text Area`, `Dropdown`, `Multi-Dropdown`, `Date`, `DateTime`, `Currency`, `Numeric`, `Phone`, `Percentage`, `Email`, `URL`, `Document`, `Formula`
21. Tutup dropdown Data Type
22. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18 dan 21 (menutup popover dan dropdown agar langkah berikutnya tidak terhalang overlay) dan langkah 22 (menutup modal; form belum diubah sehingga tidak ada dialog `Unsaved Changes`).
- Temuan untuk QA:
  - TC-FA-CF-57 dan TC-FA-CF-58 tidak menyebut cara menutup popover atau dropdown; spec menulis langkah penghubung tanpa menetapkan mekanismenya.
  - Kedua TC bertipe UI Only; spec tetap FE+BE karena modal Create dibuka pada backend nyata.
