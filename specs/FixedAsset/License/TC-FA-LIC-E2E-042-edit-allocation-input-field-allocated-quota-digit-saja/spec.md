---
id: TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja
title: "Edit Allocation: Field Allocated Quota Hanya Menerima Digit dan Batas 15 Karakter"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-154
  - TC-FA-LIC-155
  - TC-FA-LIC-156
  - TC-FA-LIC-157
coverage:
  web: automated
---

# Edit Allocation: Field Allocated Quota Hanya Menerima Digit dan Batas 15 Karakter

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12: Divisi IT beralokasi 100 (Maximum Quota 300 = alokasi 100 + Remaining Kantor Pusat 200).
- Data: Semua blok memblokir Save (validasi) dan tidak mengubah data; tidak ada perubahan Pre-setup #12.
- Kemampuan teknis: Intercept jaringan mencatat jumlah request ke endpoint Edit Allocation (asersi nol request pada Save yang diblokir).

## Test Steps

### TC-FA-LIC-154: Hanya digit yang masuk saat diketik

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
4. Kosongkan field New Allocated Quota
5. Ketik `a`, `.`, `,`, `-`, dan `e` satu per satu
6. Verifikasi field tetap kosong (karakter terlarang tidak pernah masuk)
7. Verifikasi tidak ada pesan error
8. Ketik `12`
9. Verifikasi field berisi `12`

### TC-FA-LIC-155: Tempel teks bercampur hanya menyisakan digit

10. Kosongkan field New Allocated Quota
11. Tempel `12a3.-4`
12. Verifikasi field berisi `1234`

### TC-FA-LIC-156: Input lebih dari 15 karakter menampilkan Max. 15 characters

13. Kosongkan field New Allocated Quota
14. Pasang intercept jaringan yang mencatat request ke endpoint Edit Allocation
15. Ketik `1234567890123456` (16 digit)
16. Verifikasi pesan inline `Max. 15 characters` (V-FALIC-07) tampil real-time
17. Verifikasi field mempertahankan seluruh 16 digit `1234567890123456` (tidak dipotong)
18. Klik `[Save]`
19. Verifikasi `[Save]` diblokir: nol request ke endpoint Edit Allocation pada intercept jaringan
20. Verifikasi modal tetap terbuka
21. Hapus satu digit terakhir sehingga 15 digit
22. Verifikasi pesan `Max. 15 characters` hilang
23. Verifikasi `[Save]` tidak lagi diblokir
24. Lepas intercept jaringan

### TC-FA-LIC-157: Tepat 15 digit dievaluasi terhadap Maximum Quota

25. Kosongkan field New Allocated Quota
26. Ketik `123456789012345` (15 digit)
27. Klik `[Save]`
28. Verifikasi alert V-FALIC-02 tampil: `Allocated quota exceeds the maximum allowed for this group (300).`
29. Verifikasi tidak ada pesan `Max. 15 characters`
30. Klik icon `[×]`
31. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08); mengosongkan field dan melepas intercept menyiapkan blok berikutnya.
- Urutan TC: TC-FA-LIC-154, TC-FA-LIC-155 (bergantung pada TC-FA-LIC-154), TC-FA-LIC-156, lalu TC-FA-LIC-157; semua blok memakai modal Divisi IT yang sama dan tetap terbuka (S-10).
- TC-FA-LIC-157: asersi `tidak ada pesan Max. 15 characters` diletakkan sesudah alert V-FALIC-02 tampil sebagai anchor positif (bagian 8b butir 2).
- TC-FA-LIC-156: Save pada 16 digit diblokir tanpa request, sehingga tidak ada toast yang diasersi.
