---
id: TC-AC-DS-E2E-101-setup-column-list-screening-dan-sc-a-ceklis
title: "Setup Column List: Screening Overlay dan Popup serta Ceklis Kelas SC-A Hideable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-346
  - TC-AC-DS-347
  - TC-AC-DS-348
coverage:
  web: automated
---

# Setup Column List: Screening Overlay dan Popup serta Ceklis Kelas SC-A Hideable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Tabel "Kolom Hideable" untuk langkah 17 sampai 20: `Photo`, `Device Name`, `SKU`, `Category`, `Brand`, `Model/Type`, `Current Stock`, `Last Modified`.
- Preferensi kolom List: langkah 21 menyimpan konfigurasi kolom di cache browser. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-346: Screening Overlay Column Visibility

1. Klik header kolom Actions (⋯)
2. Verifikasi tombol `Setup Column...` di bagian bawah Overlay Column Visibility
3. Verifikasi daftar kolom berurutan `Photo | Device Name | SKU | Category | Brand | Model/Type | Current Stock | Last Modified | Hardware Type | Range Type | TAG Type`
4. Verifikasi Photo, Device Name, SKU, Category, Brand, Model/Type, Current Stock, dan Last Modified tercentang dan enabled (Hideable)
5. Verifikasi Hardware Type, Range Type, dan TAG Type tidak tercentang dan enabled (Curated)
6. Verifikasi kolom Checkbox dan Actions tidak tampil sebagai baris pada daftar
7. Verifikasi setiap kolom memiliki drag handle

### TC-AC-DS-347: Screening Popup Setup Column dan Preview Table

8. Klik `Setup Column...` pada overlay
9. Verifikasi Header: judul "Setup Column"
10. Verifikasi Header: deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
11. Verifikasi Header: ikon close `[✕]` di kanan atas
12. Verifikasi Body: daftar kolom dengan checkbox (Hideable checked untuk delapan kolom bawaan, Curated unchecked untuk Hardware Type, Range Type, dan TAG Type), drag handle, dan ikon Pin per baris
13. Verifikasi Body: section Live Preview menampilkan urutan header kolom dan data sel yang sama dengan tabel asli
14. Verifikasi Footer: tombol `[Reset to Default]` dan `[Save]` rata kanan
15. Verifikasi Footer: tidak ada tombol `[Cancel]`

### TC-AC-DS-348: Ceklis dan unceklis kelas SC-A Hideable

16. Untuk setiap baris tabel "Kolom Hideable", lakukan langkah 17 sampai 20
17. Hilangkan centang kolom {Kolom} pada popup
18. Verifikasi kolom {Kolom} hilang dari preview
19. Centang kembali kolom {Kolom} pada popup
20. Verifikasi kolom {Kolom} tampil kembali di preview
21. Klik `[Save]`
22. Muat ulang halaman dengan F5
23. Verifikasi konfigurasi tersimpan dan tetap berlaku setelah muat ulang: delapan kolom Hideable tampil di tabel

## Notes

- Langkah 17 sampai 20 diulang untuk delapan baris tabel "Kolom Hideable" (ekspansi 32 langkah; total spec 50 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Alasan melewati sekitar 35 langkah: seluruh spec memakai satu popup Setup Column dan satu dataset; blok per kolom pada TC-AC-DS-348 identik, berdiri sendiri, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna; screening TC-AC-DS-346 dan TC-AC-DS-347 hanya membaca.
- Langkah penghubung (S-03): langkah 1 dan 8 membuka overlay dan popup; tanpa asersi tambahan.
- Temuan untuk QA:
  - TC-AC-DS-348 Expected a sampai h menyebut kolom hilang "setelah Save pada tabel", tetapi langkah TC mencentang kembali setiap kolom sebelum `[Save]`; keadaan itu tidak teramati. Spec mengasersi hilang dan tampil kembali di preview per kolom serta tabel setelah Save dan F5 pada keadaan akhir. Expected j ("anggota yang menjadi satu-satunya kolom tampil tidak berlaku") tidak punya langkah dan tidak diasersi.
  - S-12: asersi bergantung pada Pre-setup #29 dan #30. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
