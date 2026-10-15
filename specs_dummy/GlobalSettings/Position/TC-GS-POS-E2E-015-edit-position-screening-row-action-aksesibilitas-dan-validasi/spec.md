---
id: TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi
title: "Screening overlay Row Action, form Edit, aksesibilitas dialog, dan validasi field inline"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-74
  - TC-GS-POS-75
  - TC-GS-POS-76
  - TC-GS-POS-77
  - TC-GS-POS-78
  - TC-GS-POS-80
  - TC-GS-POS-81
  - TC-GS-POS-82
  - TC-GS-POS-83
  - TC-GS-POS-84
  - TC-GS-POS-88
  - TC-GS-POS-285
coverage:
  web: automated
---

# Screening overlay Row Action, form Edit, aksesibilitas dialog, dan validasi field inline

## Prerequisites

- Login sebagai Role: Total Control
- Record Position "IT Support Specialist" tersedia di tabel

## Test Steps

### Screening Row Action & Modal Edit

1. Buka tab Position
2. Klik ikon menu baris (⋯) pada baris "IT Support Specialist"
3. Verifikasi overlay Row Action muncul dengan opsi "Edit" dan "Delete"
4. Klik opsi "Edit"
5. Verifikasi modal Edit Position terbuka dengan:
   - Header: Judul "Edit Position" dan tombol close `[✕]`
   - Body: Field input "Position Name" terisi nilai awal "IT Support Specialist"
   - Footer: Tombol "[Clear Field]" dan tombol "[Save]" (tidak ada tombol [Cancel])
6. Verifikasi focus trap aktif di dalam modal dan atribut aria-required="true" terpasang
7. Hover tombol "[Save]" dan "[Clear Field]", verifikasi perubahan gaya visual

### Validasi Field Kosong dan Whitespace

8. Hapus seluruh teks di field Position Name lalu klik "[Save]"
9. Verifikasi simpan diblokir, border merah muncul, dan pesan error "Position Name must not be empty" tampil
10. Masukkan spasi saja lalu klik "[Save]", verifikasi error tetap muncul

### Validasi Batas Karakter & Emoji

11. Masukkan teks sepanjang 121 karakter, verifikasi error "Position Name max. 120 characters" langsung muncul saat pengetikan
12. Ketik atau paste karakter emoji ke dalam field, verifikasi emoji diblokir otomatis
13. Klik tombol "[Clear Field]"
14. Verifikasi field dikosongkan (bukan me-revert ke nilai awal), error dibersihkan, dan modal tetap terbuka

## Notes

- Menggabungkan TC-GS-POS-74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 88, dan 285.
