---
id: TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template
title: "Validasi Required Create Custom Plan: Plan Name, Product, dan Template"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-111
  - TC-AC-PF-112
  - TC-AC-PF-113
  - TC-AC-PF-127
coverage:
  web: automated
---

# Validasi Required Create Custom Plan: Plan Name, Product, dan Template

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A (default plan FAMS `Growth` aktif sebagai Template) untuk TC-AC-PF-111 sampai TC-AC-PF-113; Dataset Plan W (Product `SAMS` hanya memiliki plan Free aktif `Supply Starter`, tanpa plan Paid aktif) untuk TC-AC-PF-127. Kedua Dataset disediakan fixture backend dan dipulihkan.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`, `Supply Starter`) dipakai apa adanya, hanya dibaca; pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-048` (`Paket Tanpa Product-{runId}-048`, `Paket Tanpa Template-{runId}-048`, `Paket Tanpa Paid-{runId}-048`); tidak ada plan yang tersimpan.
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-048`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Plan Name kosong (TC-AC-PF-111)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Biarkan Plan Name kosong lalu klik `[Submit]`
5. Verifikasi pesan inline `Plan name must not be empty` muncul di bawah field Plan Name setelah Submit
6. Verifikasi form tetap terbuka dan tidak berpindah ke Plan Detail (tidak ada plan baru)

### Product kosong (TC-AC-PF-112)

7. Klik `[Clear Field]` agar form kembali ke kondisi awal dan pesan error sebelumnya hilang
8. Isi Plan Name `Paket Tanpa Product-{runId}-048`
9. Biarkan Product belum dipilih lalu klik `[Submit]`
10. Verifikasi pesan inline `Product must not be empty` muncul di bawah field Product setelah Submit
11. Verifikasi form tetap terbuka dan tidak berpindah ke Plan Detail (tidak ada plan baru)

### Template kosong (TC-AC-PF-113)

12. Klik `[Clear Field]` agar form kembali ke kondisi awal dan pesan error sebelumnya hilang
13. Pilih Product `FAMS`
14. Isi Plan Name `Paket Tanpa Template-{runId}-048`
15. Biarkan Template belum dipilih lalu klik `[Submit]`
16. Verifikasi pesan inline `Template must not be empty` muncul di bawah field Template setelah Submit
17. Verifikasi form tetap terbuka dan tidak berpindah ke Plan Detail (tidak ada plan baru)

### Product tanpa plan Paid aktif (TC-AC-PF-127)

18. Klik `[Clear Field]` agar form kembali ke kondisi awal dan pesan error sebelumnya hilang
19. Pilih Product `SAMS`
20. Klik dropdown Template
21. Verifikasi dropdown Template menampilkan `No options available` tanpa opsi
22. Tutup dropdown Template (Esc)
23. Isi Plan Name `Paket Tanpa Paid-{runId}-048` lalu klik `[Submit]`
24. Verifikasi pesan inline `Template must not be empty` muncul
25. Verifikasi form tetap terbuka dan tidak berpindah ke Plan Detail (tidak ada plan baru)

### Pemulihan

26. Klik `[Clear Field]` untuk mengembalikan form ke kondisi awal tanpa dirty

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 7, 12, 18, 22, 26.
- Pemulihan form: `[Clear Field]` di antara TC mengosongkan pesan error inline (TC-AC-PF-618) sehingga pesan identik tidak lolos secara semu (R-12) dan menjadi pemulihan akhir sehingga spec tidak berakhir dengan form dirty; Dataset W menggantikan Dataset A untuk Product `SAMS` hanya pada bagian TC-AC-PF-127.
- "Tidak ada plan baru" diamati lewat form yang tetap terbuka tanpa berpindah ke Plan Detail, karena TC tidak memberi langkah observasi daftar.
- Temuan untuk QA: (1) TC-AC-PF-112 tidak memasang Template, padahal TC-AC-PF-618 menunjukkan Submit tanpa Template juga memunculkan `Template must not be empty`; Expected TC-AC-PF-112 hanya menyebut `Product must not be empty` dan spec tidak mengasersi pesan Template pada langkah itu. (2) TC-AC-PF-127 memakai Dataset Plan W, yang membuat Product `SAMS` tanpa plan Paid, padahal TC-AC-PF-150 memakai Dataset Plan S (`Supply Pro`, SAMS Paid); kedua Dataset tidak boleh aktif bersamaan.
