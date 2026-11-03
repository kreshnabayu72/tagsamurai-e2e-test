---
id: TC-AC-DS-E2E-014-mobile-selection-mode-dan-floating-bulk-bar
title: "Tampilan Mobile: Long-press Masuk Selection Mode, Floating Bulk Bar, dan Batal Seleksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-49
  - TC-AC-DS-50
  - TC-AC-DS-51
coverage:
  mobile: automated
---

# Tampilan Mobile: Long-press Masuk Selection Mode, Floating Bulk Bar, dan Batal Seleksi

## Prerequisites

- Mode: FE+BE. Platform: aplikasi mobile Android (Card List).
- Perangkat atau emulator Android dengan aplikasi mobile TAG Samurai Admin Console terpasang, serta kemampuan tap, long-press, dan membaca elemen UI; perangkat atau emulator belum ditetapkan di sumber dan disediakan tim FE. Perangkat fisik bersama sehingga suite berjalan serial (`parallel: false`).
- Akun aktor: Delete-Only Principal PT Arunika Prima `manageSkuD_automated_{namaCompany}@qwertysystem.net` (Pre-setup #6, Manage device master data: Delete + Read), password `Spectra.env.AC_DS_D_PASSWORD`. Login di aplikasi mobile di hook `before` spec ini; halaman Device SKU dibuka pada langkah 1. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Data milik spec (hook `before`, lewat sesi API aktor dan fixture BE yang disediakan tim BE/FE): dua SKU berstok 0 `MOB-A-{runId}-014` (Device Name `UHF Handheld Reader`, Category `UHF Handheld`, Brand `Arcturus`, Model/Type `MA-{runId}`, Range Type `Short Range`, 1 foto) dan `MOB-B-{runId}-014` (Device Name `Asset TAG`, Category `Asset TAG`, Brand `Arcturus`, Model/Type `MB-{runId}`, 1 foto), menggantikan `HHR-ARC-200` dan `TAG-ARC-OBJ` (S-06: target Delete memakai data milik spec). Hook `after` menghapus kedua SKU bila masih ada.
- Env var `AC_DS_D_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.

## Test Steps

### TC-AC-DS-49: Long-press masuk selection mode

1. Buka halaman Device SKU pada aplikasi mobile
2. Tap card `MOB-A-{runId}-014` sekali
3. Verifikasi Detail SKU tampil sebagai popup
4. Tutup Popup Detail
5. Long-press card `MOB-A-{runId}-014`
6. Verifikasi checkbox muncul di kiri tiap card
7. Verifikasi card `MOB-A-{runId}-014` terpilih
8. Tap card `MOB-B-{runId}-014`
9. Verifikasi checkbox card `MOB-B-{runId}-014` ikut tercentang
10. Verifikasi Detail tidak terbuka
11. Verifikasi Floating Bulk Bar menampilkan `[✕]`, counter `2 Selected`, `[Select All]`, dan aksi Delete
12. Tap `[✕]` pada Floating Bulk Bar

### TC-AC-DS-51: Membatalkan seleksi lewat tombol close

13. Long-press card `MOB-A-{runId}-014`
14. Tap card `MOB-B-{runId}-014`
15. Tap `[✕]` pada Floating Bulk Bar
16. Verifikasi seluruh seleksi dibatalkan
17. Verifikasi Floating Bulk Bar hilang
18. Verifikasi checkbox card hilang
19. Verifikasi Card List kembali ke mode normal tanpa perubahan data, card `MOB-A-{runId}-014` dan `MOB-B-{runId}-014` masih tampil

### TC-AC-DS-50: Floating Bulk Bar menjalankan Delete

20. Long-press card `MOB-A-{runId}-014`
21. Tap card `MOB-B-{runId}-014`
22. Tap aksi Delete pada Floating Bulk Bar
23. Verifikasi dialog berjudul "Delete SKUs" memuat bullet `MOB-A-{runId}-014` dan `MOB-B-{runId}-014` serta teks "Are you sure you want to delete them? This action cannot be undone."
24. Tap `[Delete]`
25. Verifikasi toast sukses: "Success, device SKU has been deleted."
26. Verifikasi checkbox card hilang
27. Verifikasi Floating Bulk Bar hilang
28. Verifikasi card `MOB-A-{runId}-014` dan `MOB-B-{runId}-014` tidak ada lagi di Card List

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-49, TC-51, TC-50. TC-50 diletakkan terakhir karena menghapus kedua SKU milik spec (S-10); TC-49 dan TC-51 membutuhkan kedua card masih ada.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 2, 4, 5, 8 (membuka halaman, tap, dan long-press yang hasilnya diasersi pada langkah berikutnya), 12 (keluar dari selection mode sebelum TC-51, S-09), 13 sampai 15 dan 20 sampai 22, 24 (aksi TC-51 dan TC-50 yang hasilnya diasersi pada langkah berikutnya). Langkah 15 mengulang aksi `[✕]` pada langkah 12 karena TC-51 menguji aksi itu sebagai objek uji.
- Card `MOB-A-{runId}-014` dan `MOB-B-{runId}-014` dicari pada Card List dengan menggulir; TC tidak menyebut Search pada tampilan mobile.
- Temuan untuk QA:
  - S-12: TC memakai `HHR-ARC-200` dan `TAG-ARC-OBJ` (Pre-setup #29); spec memakai SKU milik spec bersuffix dengan atribut yang sama (stok 0) karena TC-50 menghapusnya (S-06).
  - Fixture rancangan: ketersediaan Pre-setup #6 (Delete-Only Principal), #29, dan #30 di environment belum diverifikasi.
  - Perangkat atau emulator Android belum ditetapkan di TC; spec mensyaratkannya di Prerequisites (disediakan tim FE).
  - TC-49 langkah 1 dan TC-50 tidak menyebut cara menemukan card di Card List (129 SKU); spec memakai gulir Card List.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
