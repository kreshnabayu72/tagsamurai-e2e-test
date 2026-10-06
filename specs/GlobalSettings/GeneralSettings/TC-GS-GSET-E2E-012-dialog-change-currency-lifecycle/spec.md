---
id: TC-GS-GSET-E2E-012-dialog-change-currency-lifecycle
title: "Dialog Change Currency: trigger sebelum PUT, isi, cancel, konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-26
  - TC-GS-GSET-27
  - TC-GS-GSET-28
  - TC-GS-GSET-29
  - TC-GS-GSET-30
coverage:
  web: automated
---

# Dialog Change Currency: pemicu, isi zona, cancel, konfirmasi

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Currency tersimpan saat ini `IDR`; nilai data uji mengikuti Tabel Data Uji Dinamis: Currency Code
  `IDR`→`USD` dengan `after` mengembalikan `currency_code` ke `IDR` di akhir spec.
- Dialog muncul ketika Currency Code berubah sebelum request `PUT` terkirim (gate `GSET-LOGIC-04`).

## Test Steps

### Pemicu dialog

1. Buka halaman `Global Settings > General Settings`
2. Ubah `Currency Code` menjadi `$ - US Dollar`
3. Klik `[Save]`
4. Verifikasi dialog `Change Currency` tampil SEGERA **sebelum** request `PUT` dikirim
5. Verifikasi belum ada toast sukses maupun perubahan data di server (dialog memblokir PUT)

### Screening 3 zona dialog

6. Verifikasi header dialog menampilkan title `Change Currency`
7. Verifikasi body dialog menampilkan penjelasan bahwa amount yang sudah dimasukkan di tempat lain
   (misal Purchase Price) TIDAK dikonversi — hanya ditampilkan dengan simbol mata uang baru, dan
   menanyakan konfirmasi perubahan (verifikasi verbatim dari fixture/PRD §4.2a)
8. Verifikasi footer dialog menampilkan `[Cancel]` (teks kontras/flat) dan `[Change Currency]`
   (filled primary) dan `[✕]`/close icon

### Cancel menjaga nilai baru (tetap unsaved)

9. Klik `[Cancel]`
10. Verifikasi dialog tertutup dan kembali ke form
11. Verifikasi `Currency Code` TETAP `$ - US Dollar` (baru dipilih, belum tersimpan) — **TIDAK reset**
    ke `IDR`
12. Verifikasi tombol `[Save]` tetap aktif (form masih dirty) dan belum ada data tersimpan

### Konfirmasi change → submit normal

13. Klik `[Save]` dan klik `[Change Currency]` pada dialog
14. Verifikasi dialog tertutup dan request `PUT` terkirim
15. Verifikasi toast sukses `Success, general settings has been saved.` tampil
16. Verifikasi Modal Changelog mencatat perubahan Currency Code

### Currency tidak diubah, field lain berubah → tanpa dialog

17. Ubah hanya `Time Zone` (Currency Code tidak disentuh), klik `[Save]`
18. Verifikasi submit langsung tanpa dialog tambahan apa pun

### Tutup dialog melalui ✕/Esc tanpa memilih

19. Ubah `Currency Code` ke `$ - US Dollar`, klik `[Save]`, dialog tampil
20. Tutup dialog lewat `[✕]` / `Esc`
21. Verifikasi form tetap mempertahankan nilai `$ - US Dollar` yang baru dipilih (dirty), tidak ter-reset

## Notes

- Perilaku Cancel di langkah 9-12 sengaja dibuktikan tidak mereset nilai dropdown, sesuai TC-GS-GSET-28:
  "form tetap unsaved dgn Currency Code baru". Path "revert manual" (mengembalikan dropdown ke nilai
  tersimpan setelah Cancel) dibuktikan di spec 013, termasuk kasus bypass gate `GSET-LOGIC-04`.