---
id: TC-FA-CF-E2E-151-request-langsung-validasi-422
title: "Request Langsung Ditolak 422 (Validasi Payload Create)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-565
  - TC-FA-CF-566
  - TC-FA-CF-567
  - TC-FA-CF-568
  - TC-FA-CF-569
  - TC-FA-CF-570
  - TC-FA-CF-571
coverage:
  web: automated
---

# Request Langsung Ditolak 422 (Validasi Payload Create)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11 dan #12), field `Asset Serial Tag` dipakai sebagai operan custom field pada TC-FA-CF-566. Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE). Berkas uji `malware.exe` dan `over-1mb.pdf` (Pre-setup #36) mengacu `Fixture.berkasUji`.
- Data Dinamis: Field Name request ditolak `Req 565 {runId}-151` sampai `Req 571 {runId}-151` (satu nama per TC; tidak pernah tersimpan). Cleanup di hook `after`: hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-151`.
- Kemampuan teknis: klien HTTP dengan token Total Control Company Alpha (sesi API aktor, lihat `suite.md`; kemampuan disediakan tim BE/FE); fixture BE untuk membaca field tersimpan.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah (semua request ditolak). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-565: Dropdown dengan nol opsi

1. Kirim request Create Dropdown tanpa opsi langsung (klien HTTP) dengan Field Name `Req 565 {runId}-151`
2. Verifikasi server menolak dengan 422
3. Verifikasi field `Req 565 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-566: Formula dengan operan custom field

4. Kirim request Create Formula langsung dengan token field merujuk custom field `Asset Serial Tag` dan Field Name `Req 566 {runId}-151`
5. Verifikasi server menolak dengan 422
6. Verifikasi pesan `Only standard numeric asset fields can be used in a formula`
7. Verifikasi field `Req 566 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-567: Required bukan boolean

8. Kirim request Create langsung dengan Required bernilai `maybe` dan Field Name `Req 567 {runId}-151`
9. Verifikasi server menolak dengan 422
10. Verifikasi pesan `Required must be a boolean value`
11. Verifikasi field `Req 567 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-568: Decimal Places selain 0, 1, atau 2

12. Kirim request Create Numeric langsung dengan Decimal Places 3 dan Field Name `Req 568 {runId}-151`
13. Verifikasi server menolak dengan 422
14. Verifikasi pesan `Decimal places must be 0, 1, or 2`
15. Verifikasi field `Req 568 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-569: request tanpa Scope

16. Kirim request Create langsung tanpa nilai Scope dengan Field Name `Req 569 {runId}-151`
17. Verifikasi server menolak dengan 422
18. Verifikasi pesan `Scope must not be empty`
19. Verifikasi field `Req 569 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-570: Value Type Global tanpa Global Value

20. Kirim request Create Value Type Global langsung tanpa nilai dengan Field Name `Req 570 {runId}-151`
21. Verifikasi server menolak dengan 422
22. Verifikasi pesan `Value must not be empty`
23. Verifikasi field `Req 570 {runId}-151` tidak tersimpan (dibaca lewat fixture BE)

### TC-FA-CF-571: Global Document berformat atau berukuran tidak valid

24. Kirim request Create Document Global langsung dengan berkas `.exe` dan Field Name `Req 571 {runId}-151`
25. Verifikasi server menolak dengan 422
26. Verifikasi pesan `Unsupported file format. Use PDF, DOCX, DOC, XLS, XLSX, PNG, JPG, JPEG, or CSV.`
27. Kirim request Create Document Global langsung dengan berkas lebih dari 1 MB dan Field Name `Req 571 {runId}-151`
28. Verifikasi server menolak dengan 422
29. Verifikasi pesan `File size must not exceed 1 MB.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a dengan Expected respons API (TC-FA-CF-565 sampai 571) tetap di spec FE+BE ini; request hanya mengasersi status respons, pesan, dan state data lewat fixture BE (bagian 8b butir 1). TC lain request langsung validasi ada di spec 181.
- Pelaku request memakai sesi API Total Control Company Alpha (bukan konteks UI kedua); `P-2` tidak dipakai.
- Temuan untuk QA:
  - TC-FA-CF-565 sampai 571 tidak menyebut payload lengkap (Data Type, nilai lain); spec memakai Field Name Dinamis bersuffix dan nilai valid lain yang disediakan tim FE.
  - TC-FA-CF-565 Expected hanya menyebut "422" tanpa pesan; spec tidak mengasersi pesan.
  - TC-FA-CF-571 tidak menyebut Field Name dan Scope request; langkah 24 dan 27 memakai Field Name Dinamis yang sama karena kedua request ditolak.
  - Kolom Pre-setup #36 menyebut `malware.exe` dan `over-1mb.pdf`; TC-FA-CF-571 hanya menyebut `.exe` dan "lebih dari 1 MB", spec memakai kedua berkas Pre-setup itu.
