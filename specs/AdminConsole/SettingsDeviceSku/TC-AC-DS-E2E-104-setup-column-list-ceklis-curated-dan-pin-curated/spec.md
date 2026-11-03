---
id: TC-AC-DS-E2E-104-setup-column-list-ceklis-curated-dan-pin-curated
title: "Setup Column List: Ceklis Kelas SC-B Curated dan Pin atau Unpin Kelas SC-B Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-351
  - TC-AC-DS-353
coverage:
  web: automated
---

# Setup Column List: Ceklis Kelas SC-B Curated dan Pin atau Unpin Kelas SC-B Curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Tabel "Kolom Curated" untuk langkah 4 sampai 7 dan langkah 15 sampai 20: `Hardware Type`, `Range Type`, `TAG Type` (ketiganya Hidden secara default).
- Lebar viewport cukup sempit sehingga tabel dapat digulir horizontal; ukuran viewport disediakan tim FE.
- Preferensi kolom List: langkah 8, 13, 15 sampai 21 menyimpan konfigurasi kolom di cache browser. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-351: Ceklis dan unceklis kelas SC-B Curated

1. Klik header kolom Actions (⋯)
2. Klik `Setup Column...` pada overlay
3. Untuk setiap baris tabel "Kolom Curated", lakukan langkah 4 sampai 7
4. Centang kolom {Kolom} pada popup
5. Verifikasi kolom {Kolom} tampil di preview
6. Hilangkan centang kolom {Kolom} pada popup
7. Verifikasi kolom {Kolom} hilang dari preview
8. Klik `[Save]`
9. Verifikasi kolom bawaan `Brand` tampil di tabel
10. Verifikasi kolom `Hardware Type`, `Range Type`, dan `TAG Type` tidak tampil di tabel
11. Muat ulang halaman dengan F5
12. Verifikasi konfigurasi tersimpan dan tetap berlaku setelah muat ulang: kolom `Hardware Type`, `Range Type`, dan `TAG Type` tidak tampil di tabel

### TC-AC-DS-353: Pin dan unpin kelas SC-B Curated

13. Klik header kolom Actions (⋯), klik `Setup Column...`, centang kolom `Hardware Type`, `Range Type`, dan `TAG Type`, lalu klik `[Save]`
14. Untuk setiap baris tabel "Kolom Curated", lakukan langkah 15 sampai 20
15. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom {Kolom}, lalu klik `[Save]`
16. Geser tabel secara horizontal
17. Verifikasi kolom {Kolom} membeku di sisi kiri ketika tabel digulir horizontal
18. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom {Kolom} untuk unpin, lalu klik `[Save]`
19. Geser tabel secara horizontal
20. Verifikasi kolom {Kolom} kembali bergerak setelah unpin
21. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom `Hardware Type`, lalu klik `[Save]`
22. Muat ulang halaman dengan F5
23. Verifikasi status pin tersimpan dan tetap berlaku setelah muat ulang: kolom `Hardware Type` membeku di sisi kiri

## Notes

- Langkah 4 sampai 7 diulang untuk tiga baris tabel "Kolom Curated" dan langkah 15 sampai 20 untuk tiga baris yang sama (ekspansi 12 dan 18 langkah; total spec 41 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat; Save menutup popup sehingga tiap pin dan unpin membuka popup kembali.
- Alasan melewati sekitar 35 langkah: kedua blok memakai popup Setup Column yang sama dan satu dataset; iterasi per kolom identik dan berdiri sendiri, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah penghubung (S-03, S-14): langkah 1 sampai 2 membuka overlay dan popup; langkah 13 membuat kolom curated tampil di tabel sebelum di-pin; tanpa asersi tambahan. Langkah 9 adalah anchor positif tambahan (bukan Expected TC) untuk asersi absence di langkah 10.
- Temuan untuk QA:
  - TC-AC-DS-351 menyuruh "hilangkan centang" kolom curated lebih dulu, padahal ketiganya tidak tercentang secara default (TC-AC-DS-346); spec mencentang lebih dulu lalu menghilangkan centang. Expected "ceklis menampilkannya kembali" ditulis sebagai kolom tampil di preview sesudah dicentang. Expected e ("anggota yang menjadi satu-satunya kolom tampil tidak berlaku") tidak punya langkah dan tidak diasersi.
  - TC-AC-DS-353 langkah 7 menyebut "pin satu kolom" tanpa menyebut kolomnya; spec memakai `Hardware Type`.
  - S-12: asersi bergantung pada Pre-setup #29 dan #30. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
