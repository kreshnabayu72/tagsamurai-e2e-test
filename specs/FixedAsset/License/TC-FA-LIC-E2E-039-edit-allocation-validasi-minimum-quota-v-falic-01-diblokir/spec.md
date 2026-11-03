---
id: TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir
title: "Edit Allocation: Validasi Minimum Quota V-FALIC-01 Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-124
  - TC-FA-LIC-125
  - TC-FA-LIC-126
  - TC-FA-LIC-137
coverage:
  web: automated
---

# Edit Allocation: Validasi Minimum Quota V-FALIC-01 Diblokir

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 (Minimum Quota 450, Maximum Quota 700) dan Divisi IT beralokasi 100 (Used 60, Minimum Quota 60).
- Data: Semua blok memblokir Save (validasi) dan tidak mengubah data; tidak ada perubahan Pre-setup #12.

## Test Steps

### TC-FA-LIC-124: Nilai 449 ditolak V-FALIC-01 saat blur

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Isi New Allocated Quota `449`
5. Pindahkan fokus keluar dari field (blur)
6. Verifikasi field berborder danger dengan pesan inline `Cannot set quota below used, reserved, and subgroup-allocated quota (450).`
7. Verifikasi pesan muncul saat blur, sebelum `[Save]` diklik
8. Verifikasi modal tetap terbuka dengan nilai `449` dipertahankan

### TC-FA-LIC-126: Pesan V-FALIC-01 hilang setelah nilai dikoreksi

9. Isi New Allocated Quota `440`
10. Pindahkan fokus keluar dari field (blur)
11. Verifikasi pesan error V-FALIC-01 tampil
12. Ubah nilai menjadi `460`
13. Pindahkan fokus keluar dari field (blur)
14. Verifikasi pesan error hilang
15. Verifikasi border danger kembali normal

### TC-FA-LIC-125: Klik Save dengan nilai di bawah Minimum Quota tidak mengubah data

16. Isi New Allocated Quota `440`
17. Klik `[Save]`
18. Verifikasi pesan inline V-FALIC-01 tampil: `Cannot set quota below used, reserved, and subgroup-allocated quota (450).`
19. Verifikasi modal tetap terbuka dengan input `440` dipertahankan
20. Verifikasi tidak ada toast sukses
21. Klik icon `[×]`
22. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`
24. Verifikasi Allocated Quota baris `Divisi Logistik` tetap `500`

### TC-FA-LIC-137: Nilai 0 pada grup ber-Minimum Quota di atas 0 ditolak

25. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
26. Isi New Allocated Quota `0`
27. Pindahkan fokus keluar dari field (blur)
28. Verifikasi pesan V-FALIC-01 tampil: `Cannot set quota below used, reserved, and subgroup-allocated quota (60).`
29. Verifikasi nilai `0` dievaluasi sebagai angka dan bukan Remove Allocation: modal tetap terbuka dengan `0` dipertahankan
30. Klik icon `[×]`
31. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
32. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup modal dirty lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08).
- Urutan TC: TC-FA-LIC-124, TC-FA-LIC-126 (bergantung pada TC-FA-LIC-124), TC-FA-LIC-125, lalu TC-FA-LIC-137; TC-FA-LIC-126 dan TC-FA-LIC-125 memakai modal yang masih terbuka dari blok sebelumnya (S-04: langkah dependensi disalin sebagai isi dan blur).
- Klausa `Allocated Quota baris Divisi Logistik tetap 500` TC-FA-LIC-125 diasersi sesudah modal ditutup.
- TC-FA-LIC-137 mengasersi `0` sebagai angka lewat pesan V-FALIC-01 dan modal yang tetap terbuka; TC tidak memberi langkah observasi lain untuk klausa `bukan dianggap Remove Allocation` (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-FA-LIC-137 klausa b: `0 dievaluasi sebagai angka, bukan dianggap Remove Allocation` tidak punya observasi terpisah di TC; spec memakai modal yang tetap terbuka beserta pesan V-FALIC-01 sebagai bukti.
