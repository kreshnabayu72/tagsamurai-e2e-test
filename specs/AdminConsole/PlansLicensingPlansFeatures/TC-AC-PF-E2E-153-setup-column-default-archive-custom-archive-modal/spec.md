---
id: TC-AC-PF-E2E-153-setup-column-default-archive-custom-archive-modal
title: Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Ceklis, Geser, dan Pin
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-622
  - TC-AC-PF-623
  - TC-AC-PF-624
coverage:
  web: automated
---

# Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Ceklis, Geser, dan Pin

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; Default Archive `Growth Plus (old)`, custom archived `Enterprise Reseller`), Dataset Plan R (Pre-setup #30; Default Archive `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`), dan Dataset Log C (Pre-setup #41; Changelog Custom Principal 6 entri).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Tabel "Surface yang diuji" (langkah berulang untuk tiap baris):

| Kode | Surface | Cara membuka | Kolom disembunyikan | Kolom di-drag ke awal | Kolom di-Pin |
|---|---|---|---|---|---|
| DR | Default > Archive | klik tab Default, lalu sub-tab Archive | `Clients` | `Last Modified` | `Plan Name` |
| CR | Custom > Archive | klik tab Custom, lalu sub-tab Archive | `Clients` | `Last Modified` | `Plan Name` |
| MC | Modal Changelog Custom | klik tab Custom, lalu klik ikon Changelog | `Old Value` | `Modified By` | `Date` |

- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Mengubah lebar viewport browser (diperkecil pada langkah 12, dipulihkan pada langkah 21). Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: konfigurasi kolom yang disimpan spec (cache browser per tabel) dihapus di hook `after` (kemampuan menghapus preferensi kolom di browser disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-622 Ceklis dan unceklis kolom

Untuk setiap baris tabel "Surface yang diuji" (langkah 1 sampai 6):

1. Buka surface sesuai kolom "Cara membuka".
2. Buka Popup Setup Column, uncheck kolom pada "Kolom disembunyikan", klik `[Save]`.
3. Verifikasi kolom pada "Kolom disembunyikan" hilang dari tabel surface.
4. Tekan F5.
5. Buka kembali surface sesuai kolom "Cara membuka".
6. Verifikasi kolom pada "Kolom disembunyikan" tetap hilang setelah F5.

### TC-AC-PF-623 Geser urutan kolom

Untuk setiap baris tabel "Surface yang diuji" (langkah 7 sampai 11):

7. Buka surface sesuai kolom "Cara membuka".
8. Buka Popup Setup Column, drag kolom pada "Kolom di-drag ke awal" ke posisi awal, klik `[Save]`.
9. Tekan F5.
10. Buka kembali surface sesuai kolom "Cara membuka".
11. Verifikasi header tabel dimulai dari kolom pada "Kolom di-drag ke awal" setelah Save dan F5.

### TC-AC-PF-624 Pin dan Unpin

12. Perkecil lebar viewport sehingga tabel scroll horizontal.

Untuk setiap baris tabel "Surface yang diuji" (langkah 13 sampai 20):

13. Buka surface sesuai kolom "Cara membuka".
14. Buka Popup Setup Column, klik icon Pin pada kolom "Kolom di-Pin", klik `[Save]`, lalu scroll tabel ke kanan.
15. Verifikasi kolom "Kolom di-Pin" tetap terlihat di sisi kiri saat tabel di-scroll (freeze).
16. Tekan F5.
17. Buka kembali surface sesuai kolom "Cara membuka", lalu scroll tabel ke kanan.
18. Verifikasi kolom "Kolom di-Pin" masih beku setelah F5.
19. Buka Popup Setup Column, klik icon Pin kolom "Kolom di-Pin" lagi (Unpin), klik `[Save]`, lalu scroll tabel ke kanan.
20. Verifikasi kolom "Kolom di-Pin" ikut bergeser saat scroll.

21. Pulihkan lebar viewport ke ukuran semula.

## Notes

- Langkah berulang: "Untuk setiap baris tabel" mengulang langkah 1 sampai 6, 7 sampai 11, dan 13 sampai 20 untuk baris DR, CR, dan MC; parameter tiap iterasi ada di tabel "Surface yang diuji", tanpa langkah bersyarat, dan tiap `Verifikasi` tetap satu per klausa.
- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1, 5, 7, 10, 13, dan 17 membuka (kembali) surface karena F5 menutup modal Changelog dan dapat mengembalikan halaman ke tab awal; langkah 12 dan 21 mengubah serta memulihkan lebar viewport.
- Alasan di atas sekitar 35 langkah: TC sumber masing-masing mencakup tiga surface (Default Archive, Custom Archive, modal Changelog Custom) dalam satu TC dengan langkah identik dan parameter berbeda; hasil ekspansi iterasi sekitar 59 langkah, dan semua blok berada pada satu jenis aksi (Setup Column) dengan dataset yang sama. Estimasi langkah semula lebih rendah karena tiap TC menghitung satu surface.
- Temuan untuk QA: (1) TC-AC-PF-622 sampai 624 tidak menyatakan apakah F5 mempertahankan tab dan sub-tab aktif serta membuka kembali modal Changelog; spec menambah langkah membuka kembali surface. (2) Dataset Plan A memuat custom archived `Enterprise Reseller` sedangkan Dataset Plan C memuat `Arsip Custom Satu` dan `Arsip Custom Dua` pada tenant yang sama; TC ini hanya menyebut `Enterprise Reseller` untuk Custom Archive. (3) TC-AC-PF-624 mengasersi pin pada modal Changelog Custom dengan scroll horizontal tanpa menyatakan lebar modal yang membuat tabel scroll.
