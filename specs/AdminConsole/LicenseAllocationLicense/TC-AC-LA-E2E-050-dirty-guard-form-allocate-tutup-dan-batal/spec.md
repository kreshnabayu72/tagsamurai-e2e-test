---
id: TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal
title: "Dirty-Guard Form Allocate: Tutup Bersih, Tutup Dirty, Cancel Dialog, dan Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-176
  - TC-AC-LA-531
  - TC-AC-LA-177
  - TC-AC-LA-178
  - TC-AC-LA-179
coverage:
  web: automated
---

# Dirty-Guard Form Allocate: Tutup Bersih, Tutup Dirty, Cancel Dialog, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun dan nama Client.
- Data Pre-setup: Client PT Sejahtera (#19).
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-176: Menutup form bersih lewat tombol silang atau Esc tidak memunculkan dialog

1. Klik `[+ Allocation]`
2. Klik `[✕]` pada header
3. Verifikasi form tertutup langsung tanpa dialog D-02
4. Klik `[+ Allocation]`
5. Pilih Client `PT Sejahtera`, lalu kosongkan kembali pilihan itu (kembali ke nilai awal) dan tekan `Esc`
6. Verifikasi form tertutup langsung tanpa dialog D-02 karena form yang dikembalikan ke nilai awal dianggap pristine

### TC-AC-LA-531: Mencentang Stay on this form saja tidak membuat form dirty

7. Klik `[+ Allocation]`
8. Centang `Stay on this form after submitting` tanpa mengisi field apa pun
9. Klik `[✕]` pada header
10. Verifikasi form tertutup langsung tanpa dialog D-02 karena checkbox Stay bukan field data

### TC-AC-LA-177: Menutup form dirty lewat tombol silang memunculkan D-02 dan Leave membuang input

11. Klik `[+ Allocation]`
12. Pilih Client `PT Sejahtera`
13. Klik `[✕]` pada header
14. Verifikasi dialog D-02: Title `Unsaved Changes`, Body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Leave]` (severity warning) dan `[Cancel]`, tanpa bullet nama item
15. Klik `[Leave]`
16. Verifikasi `[Leave]` menutup form
17. Klik `[+ Allocation]`
18. Verifikasi field Client kosong dengan placeholder `Select client` sehingga input sebelumnya dibuang

### TC-AC-LA-178: Cancel pada D-02 kembali ke form dengan input utuh

19. Pilih Client `PT Sejahtera`
20. Tekan `Esc`
21. Klik `[Cancel]` pada dialog D-02
22. Verifikasi dialog D-02 menutup dan form tetap terbuka dengan Client `PT Sejahtera` utuh

### TC-AC-LA-179: Klik backdrop pada form dirty diabaikan tanpa dialog

23. Klik area backdrop di luar modal
24. Verifikasi modal tetap terbuka dengan input utuh
25. Verifikasi dialog D-02 tidak muncul
26. Verifikasi form tidak punya tombol `[Cancel]` di footer
27. Klik `[✕]` pada header
28. Verifikasi dialog D-02 dengan Title `Unsaved Changes` dan tombol `[Leave]` serta `[Cancel]`
29. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 5 kali, kejadian menutup 5 (langkah 2, 5 sampai 6, 9, 13 sampai 15, dan 27 sampai 29).
- Penyimpangan urutan (S-10): TC-AC-LA-178 dan TC-AC-LA-179 melanjutkan form yang dibuka pada langkah 17 (Client `PT Sejahtera` dipilih ulang pada langkah 19), sehingga jumlah buka form tidak melebihi jumlah kejadian menutup (prinsip 6).
- Langkah penghubung (S-03): langkah 5 (mengembalikan pilihan ke nilai awal sesuai TC-AC-LA-176 Langkah 2), langkah 17 sampai 18 (membuka ulang form untuk membuktikan input dibuang; Expected b TC-AC-LA-177), dan langkah 27 sampai 29 (menutup form dirty secara deterministik, S-08). `Verifikasi` dialog `Unsaved Changes` pada langkah 28 dimuat sesuai S-08.
- Asersi tidak adanya dialog (langkah 3, 6, 10, 25) memakai halaman List yang termuat setelah form tertutup atau modal yang tetap tampil sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-176 Langkah 2 ("kosongkan kembali pilihan itu") tidak menyebut cara mengosongkan pilihan pada Select Client (tombol clear atau cara lain); spec menuliskannya sebagai aksi tanpa merinci kontrol.
  - TC-AC-LA-177 Expected b ("Leave menutup form dan membuang input") membuktikan "membuang input" hanya bila form dibuka ulang; spec menambah pembukaan ulang (langkah 17 sampai 18).
  - TC-AC-LA-178 Langkah 2 menekan `Esc` pada form dirty yang membuka dialog D-02; dialog tidak punya `Verifikasi` sendiri di Expected sebelum `[Cancel]`.
  - TC-AC-LA-179 Expected c ("Form tidak punya tombol `[Cancel]` di footer") adalah klausa statis yang tidak berkaitan dengan klik backdrop; diasersi di langkah 26.
