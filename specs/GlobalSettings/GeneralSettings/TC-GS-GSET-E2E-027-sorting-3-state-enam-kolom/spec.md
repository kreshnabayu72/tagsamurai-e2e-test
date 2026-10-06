---
id: TC-GS-GSET-E2E-027-sorting-3-state-enam-kolom
title: Sorting 3-state pada keenam kolom changelog
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-75
  - TC-GS-GSET-76
  - TC-GS-GSET-77
  - TC-GS-GSET-78
  - TC-GS-GSET-79
  - TC-GS-GSET-80
coverage:
  web: automated
---

# Sorting 3-state pada enam kolom tabel changelog

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Dataset changelog 20+ baris dengan nilai campuran per kolom (huruf kecil/besar, angka, tanggal,
  nama panjang).
- Kolom pada tabel: `Action`, `Field`, `Old Value`, `New Value`, `Modified By`, `Date Modified`.

## Test Steps

### Pola klik 3-state

1. Buka Modal Changelog
2. Verifikasi indikator sortir tampil pada kolom aktif (ikon panah/urutan)
3. Klik kolom `Field` satu kali
4. Verifikasi sortir ascending (`Field` A-Z)
5. Klik kolom `Field` dua kali
6. Verifikasi sortir descending (`Field` Z-A)
7. Klik kolom `Field` tiga kali
8. Verifikasi kembali ke urutan netral (tanpa indikator sortir)
9. Verifikasi jika ada lebih dari satu kolom sortir, kolom lain kembali ke default saat kolom baru
   di-sort

### Sortir tiap kolom

10. Untuk masing-masing keenam kolom: klik sekali asc dan sekali desc, serta verifikasi hasil urutannya
    sesuai tipe data:
    - `Action` (teks A-Z)
    - `Field` (teks A-Z, case-insensitive)
    - `Old Value` & `New Value` (teks numerik/currency diperlakukan sebagai teks kecuali ditetapkan alias)
    - `Modified By` (nama lengkap, case-insensitive)
    - `Date Modified` (kronologis tanggal-waktu)

### Sorting field saat kolom hidden

11. Sembunyikan kolom `Field` via Setup Column
12. Sort kolom lain (misal `Date Modified` desc); verifikasi berjalan normal
13. Verifikasi kolom `Field` yang hidden tidak dapat di-sort (tidak tampil kolom sort-nya)
14. Kembalikan kolom `Field`

## Notes

- Sorting `Modified By` pada kolom nama diperlakukan case-insensitive sebagaimana PRD §3.4.i.
- Sorting 3-state dipakai bersama di spec 025 sebagai kombinasi.