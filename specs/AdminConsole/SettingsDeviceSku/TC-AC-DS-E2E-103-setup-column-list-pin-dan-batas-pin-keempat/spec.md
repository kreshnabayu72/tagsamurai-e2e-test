---
id: TC-AC-DS-E2E-103-setup-column-list-pin-dan-batas-pin-keempat
title: "Setup Column List: Pin dan Unpin Kelas SC-A Hideable serta Pin Keempat Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-350
  - TC-AC-DS-358
coverage:
  web: automated
---

# Setup Column List: Pin dan Unpin Kelas SC-A Hideable serta Pin Keempat Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Tabel "Kolom Hideable" untuk langkah 2 sampai 7: `Photo`, `Device Name`, `SKU`, `Category`, `Brand`, `Model/Type`, `Current Stock`, `Last Modified`.
- Lebar viewport cukup sempit sehingga tabel dapat digulir horizontal pada kolom bawaan; ukuran viewport disediakan tim FE.
- Preferensi kolom List: langkah 2 sampai 7 dan 8 menyimpan status pin di cache browser; langkah 19 meng-unpin `Photo`. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-350: Pin dan unpin kelas SC-A Hideable

1. Untuk setiap baris tabel "Kolom Hideable", lakukan langkah 2 sampai 7
2. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom {Kolom}, lalu klik `[Save]`
3. Geser tabel secara horizontal
4. Verifikasi kolom {Kolom} membeku di sisi kiri ketika tabel digulir horizontal
5. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom {Kolom} untuk unpin, lalu klik `[Save]`
6. Geser tabel secara horizontal
7. Verifikasi kolom {Kolom} kembali bergerak setelah unpin
8. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom `Photo`, lalu klik `[Save]`
9. Muat ulang halaman dengan F5
10. Verifikasi status pin tersimpan dan tetap berlaku setelah muat ulang: kolom `Photo` membeku di sisi kiri

### TC-AC-DS-358: Pin keempat diblok

11. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
12. Klik ikon Pin pada kolom `Device Name` dan `SKU` (kolom `Photo` sudah di-pin dari langkah 8), sehingga tiga kolom di-pin
13. Hover ikon Pin pada kolom `Category`
14. Verifikasi ikon Pin kolom keempat disabled dan tidak dapat diklik
15. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first." tampil
16. Klik ikon Pin pada kolom `SKU` untuk unpin
17. Verifikasi ikon Pin kolom `Category` kembali aktif
18. Klik ikon close `[✕]` pada popup

### Pemulihan state akhir

19. Klik header kolom Actions (⋯), klik `Setup Column...`, klik ikon Pin pada kolom `Photo` untuk unpin, lalu klik `[Save]`

## Notes

- Langkah 2 sampai 7 diulang untuk delapan baris tabel "Kolom Hideable" (ekspansi 48 langkah; total spec 60 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat; Save menutup popup sehingga tiap pin dan unpin membuka popup kembali.
- Alasan melewati sekitar 35 langkah: kedua blok memakai popup Setup Column yang sama dan satu dataset; iterasi per kolom identik dan berdiri sendiri, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna; blok pin keempat memerlukan pin yang sama.
- Langkah penghubung (S-03): langkah 12 melengkapi tiga pin (kolom `Photo` ter-pin dari langkah 8 dan disimpan); langkah 18 menutup popup tanpa Save sehingga perubahan tidak tersimpan; tanpa asersi tambahan.
- Langkah penghubung pemulihan (tanpa `Verifikasi`, S-03, S-09): langkah 19 meng-unpin `Photo` yang di-pin dan disimpan pada langkah 8; hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Temuan untuk QA:
  - TC-AC-DS-358 langkah 4 memin `Photo`, `Device Name`, dan `SKU` dari keadaan awal; spec melanjutkan dari `Photo` yang sudah ter-pin di langkah 8 dan memin `Device Name` dan `SKU` sehingga tiga kolom ter-pin. TC menulis "kolom lain" kembali aktif tanpa menyebut kolom yang di-unpin; spec meng-unpin `SKU`.
  - TC-AC-DS-350 langkah 12 menyebut "pin satu kolom" tanpa menyebut kolomnya; spec memakai `Photo`.
  - S-12: asersi bergantung pada Pre-setup #29 dan #30. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
