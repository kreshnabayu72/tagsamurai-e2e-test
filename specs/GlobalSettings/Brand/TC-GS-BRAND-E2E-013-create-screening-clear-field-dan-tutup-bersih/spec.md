---
id: TC-GS-BRAND-E2E-013-create-screening-clear-field-dan-tutup-bersih
title: "Screening Popup Create Brand, Clear Field, dan Tutup Bersih"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-40
  - TC-GS-BRAND-41
  - TC-GS-BRAND-57
  - TC-GS-BRAND-58
coverage:
  web: automated
---

# Screening Popup Create Brand, Clear Field, dan Tutup Bersih

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Create di browser.
- Kebutuhan mock:
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap (Read, Create, Update, Delete). Login dilakukan sekali di hook `before` (environment variable `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons `POST /v2/enterprise-management/brands/list`: 12 brand Pre-setup Client A (Acme Corp sampai Zenith Corp) berurutan A-Z, supaya halaman Brand dan tombol [+ Brand] tampil.
  - Respons `POST /v2/enterprise-management/brands/check-availability` (cek keunikan Brand Name saat mengetik, debounce sekitar 500 ms): nama tersedia (`available` true) untuk nilai yang diketik pada field Brand Name (termasuk 121 karakter huruf biasa), sehingga tidak ada error duplikat yang muncul.
  - Endpoint `POST` Create Brand tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup. Nilai uji TC-GS-BRAND-57 adalah 121 karakter huruf biasa yang hanya diketik dan tidak pernah tersimpan.
- Kemampuan teknis: navigasi keyboard (Tab, Esc) dan pembacaan fokus elemen; pengecekan ukuran modal.
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control Client A), sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-BRAND-40: Screening Popup Create Brand

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand]
3. Verifikasi Header: Title `New Brand` dan icon close `[✕]`
4. Verifikasi Body: field `Brand Name *` dengan placeholder `Enter brand name`, kosong
5. Verifikasi Body tidak memuat checkbox `Stay on this form after submitting` (Must NOT)
6. Verifikasi Footer Row 1: checkbox `Stay on this form after submitting` unchecked, rata kanan, tepat di atas tombol
7. Verifikasi Footer Row 2 (rata kanan): `[Clear Field]` (text, primary) dan `[Submit]` (filled, success)
8. Verifikasi tidak ada tombol `[Cancel]` (Must NOT)
9. Verifikasi modal berukuran md

### TC-GS-BRAND-41: Accessibility Popup Create Brand: focus trap dan Esc pada form kosong

10. Tekan Tab berulang melewati elemen fokus terakhir di modal
11. Verifikasi fokus keyboard berputar di dalam modal (tidak keluar ke halaman di belakang)
12. Tekan Esc
13. Verifikasi modal tertutup tanpa dialog Unsaved Changes

### TC-GS-BRAND-57: Clear Field pada Create mengosongkan field tanpa dialog dan tanpa mengubah checkbox Stay

14. Klik [+ Brand]
15. Centang checkbox `Stay on this form after submitting`
16. Ketik 121 karakter huruf biasa pada field Brand Name sampai error inline `Max. 120 characters` tampil
17. Klik [Clear Field]
18. Verifikasi field Brand Name kosong
19. Verifikasi border dan pesan error hilang
20. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
21. Verifikasi tidak ada dialog Unsaved Changes
22. Verifikasi modal tetap terbuka

### TC-GS-BRAND-58: Tutup Popup Create bersih lewat [✕] tanpa dialog

23. Klik `[✕]` untuk menutup form dari TC-GS-BRAND-57 (form kosong tidak dirty, FI-02, sehingga tidak ada dialog)
24. Klik [+ Brand] (form baru yang bersih)
25. Centang checkbox `Stay on this form after submitting`
26. Lepas centang checkbox `Stay on this form after submitting`
27. Klik `[✕]`
28. Verifikasi modal tertutup langsung
29. Verifikasi dialog Unsaved Changes tidak muncul (checkbox tidak membuat form dirty)

## Notes

- Mode: mock. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembukaan form ada tiga: pembukaan pertama untuk TC-GS-BRAND-40 dan TC-GS-BRAND-41 (screening, navigasi keyboard, lalu ditutup dengan Esc), pembukaan kedua untuk TC-GS-BRAND-57 (Clear Field, ditutup lewat `[✕]`; form pasca-[Clear Field] kosong sehingga tidak dirty menurut FI-02 dan tidak ada dialog; form itu tetap tidak dipakai ulang untuk kasus tutup bersih TC-GS-BRAND-58, prinsip 6 konvensi), dan pembukaan ketiga (form baru) untuk TC-GS-BRAND-58 supaya penutupan bersih tidak bercampur dengan sisa state Clear Field.
- Langkah penghubung: langkah 23 (menutup form TC-GS-BRAND-57 lewat `[✕]`, tanpa awalan `Verifikasi`) serta langkah 24 (membuka form baru untuk TC-GS-BRAND-58).
- Pemicu error TC-GS-BRAND-57 memakai 121 karakter huruf biasa (error `Max. 120 characters`) karena emoji difilter di level input dan tidak menghasilkan error (TC-GS-BRAND-48).
- TC-GS-BRAND-40 dan TC-GS-BRAND-41 memakai Total Control yang sama dengan TC-GS-BRAND-57 dan TC-GS-BRAND-58, sehingga tidak ada ganti akun.
