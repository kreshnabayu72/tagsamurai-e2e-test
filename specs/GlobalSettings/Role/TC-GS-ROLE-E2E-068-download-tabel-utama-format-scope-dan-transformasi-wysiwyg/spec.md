---
id: TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg
title: "Download Tab Utama: Format CSV/XLSX, Cakupan Baris Filter, Kolom Tampil WYSIWYG, dan Transformasi Nilai Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-174
  - TC-GS-ROLE-175
  - TC-GS-ROLE-176
  - TC-GS-ROLE-177
  - TC-GS-ROLE-178
coverage:
  web: automated
---

# Download Tab Utama: Format CSV/XLSX, Cakupan Baris Filter, Kolom Tampil WYSIWYG, dan Transformasi Nilai Default User

## Prerequisites

- Login sebagai Total Control
- Data Uji: Export files dataset Tab Total Control & Read Only
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Pre-setup tersedia; Tab Total Control dan Tab Read Only masing-masing berisi ≥3 user dengan Position/Division berbeda
- Tab Total Control berisi >10 user

## Test Steps

### Download Tab Total Control sebagai CSV dan XLSX (TC-GS-ROLE-174)

1. Klik Download, screening overlay
2. Klik "Download as CSV"
3. Klik Download > "Download as XLSX"
4. Verifikasi Overlay: "Download as CSV" | "Download as XLSX"
5. Verifikasi File "Role-Permission-Total-Control.csv" terunduh
6. Verifikasi File "Role-Permission-Total-Control.xlsx" terunduh
7. Verifikasi Tidak ada toast sukses

### Download Tab Read Only sebagai CSV dan XLSX (TC-GS-ROLE-175)

8. Tab Read Only: Download > "Download as CSV"
9. Download > "Download as XLSX"
10. Verifikasi "Role-Permission-Read-Only.csv"
11. Verifikasi "Role-Permission-Read-Only.xlsx"
12. Verifikasi Tidak ada toast sukses

### Cakupan baris Download Tab Total Control/Read Only tanpa dan dengan filter (TC-GS-ROLE-176)

13. Download CSV tanpa filter
14. Filter Status Active → Download CSV
15. Verifikasi File tanpa filter memuat seluruh user Total Control di semua halaman (bukan hanya 10 baris halaman 1)
16. Verifikasi File dengan filter hanya memuat user Status Active di semua halaman

### Download mengikuti kolom yang tampil (TC-GS-ROLE-177)

17. Hide Division > Save > Download CSV
18. Unhide Division > Save > Download CSV
19. Verifikasi File pertama tanpa kolom Division
20. Verifikasi File kedua memuat Division

### Transformasi nilai pada file Download Tab Total Control (TC-GS-ROLE-178)

21. Download XLSX
22. Periksa baris Budi Santoso dan Dewi Lestari
23. Verifikasi Status ditulis label teks tanpa warna ("Active" untuk Budi Santoso Default User, "Inactive" untuk Dewi Lestari)
24. Verifikasi Nilai kosong Default User (Position, Division, Modified By, Last Updated) ditulis "-"; Status tidak kosong
25. Verifikasi Kolom Name tanpa avatar
26. Verifikasi Last Updated mengikuti format General Settings

## Notes

- Memvalidasi alur skenario "Download Tab Utama: Format CSV/XLSX, Cakupan Baris Filter, Kolom Tampil WYSIWYG, dan Transformasi Nilai Default User".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1 Filename Download; global-settings/role/PRD/role.md §5 Download; foundation/process/prd-process/prd-conventions.md §9.9.
- Sumber pemetaan test case granular: TC-GS-ROLE-174, TC-GS-ROLE-175, TC-GS-ROLE-176, TC-GS-ROLE-177, TC-GS-ROLE-178.
