---
id: TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih
title: "Modal Edit Allocation: Clear Field, Menutup Bersih, dan Dialog Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-138
  - TC-FA-LIC-139
  - TC-FA-LIC-140
  - TC-FA-LIC-141
coverage:
  web: automated
---

# Modal Edit Allocation: Clear Field, Menutup Bersih, dan Dialog Unsaved Changes

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
- Data: Pre-setup #12: Divisi Logistik beralokasi 500 (Minimum Quota 450). Semua blok menutup tanpa Save; tidak ada perubahan Pre-setup #12.
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 7, 25, 27, dan 29).

## Test Steps

### TC-FA-LIC-139: Menutup modal bersih lewat X dan Esc

1. Klik tab `Allocation Quota`
2. Klik node `Kantor Pusat` di Sidebar
3. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
4. Klik icon `[×]`
5. Verifikasi modal langsung tertutup tanpa dialog `Unsaved Changes`
6. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
7. Tekan Esc
8. Verifikasi modal langsung tertutup tanpa dialog `Unsaved Changes`

### TC-FA-LIC-138: Clear Field mengosongkan field tanpa menutup modal

9. Klik tombol ikon `[Edit]` pada baris `Divisi Logistik`
10. Isi New Allocated Quota `440`
11. Pindahkan fokus keluar dari field (blur)
12. Verifikasi pesan error V-FALIC-01 tampil
13. Klik `[Clear Field]`
14. Verifikasi field New Allocated Quota kosong dengan placeholder `Enter allocated quota`
15. Verifikasi error V-FALIC-01 hilang
16. Verifikasi border danger hilang
17. Verifikasi modal tetap terbuka
18. Verifikasi fokus kembali ke field
19. Verifikasi tidak ada dialog konfirmasi

### TC-FA-LIC-140: Menutup modal setelah field diubah memunculkan Unsaved Changes

20. Ubah nilai menjadi `600`
21. Klik icon `[×]`
22. Verifikasi dialog dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]` (warning)

### TC-FA-LIC-141: Cancel, Leave, dan Esc pada dialog Unsaved Changes

23. Klik `[Cancel]` pada dialog
24. Verifikasi dialog tertutup dan modal tetap terbuka dengan nilai `600`
25. Tekan Esc pada modal
26. Verifikasi dialog tampil
27. Tekan Esc pada dialog
28. Verifikasi Esc pada dialog setara `[Cancel]`: dialog tertutup dan modal tetap terbuka dengan nilai `600`
29. Tekan Esc pada modal
30. Klik `[Leave]`
31. Verifikasi modal tertutup
32. Verifikasi Allocated Quota baris `Divisi Logistik` tetap `500`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): klik node Sidebar memilih node blok; modal dibuka kembali tanpa Save di antara blok.
- Urutan TC: TC-FA-LIC-139 (penutupan bersih) lebih dulu, lalu TC-FA-LIC-138, TC-FA-LIC-140, dan TC-FA-LIC-141 (bergantung pada TC-FA-LIC-140; dialog Unsaved Changes muncul sesudah nilai `600` diisi pada modal yang sama) (S-10).
- TC-FA-LIC-141: dialog tampil setelah Esc pada modal; `[Cancel]`, Esc pada dialog, dan `[Leave]` dijalankan berurutan pada modal yang sama (S-04).
