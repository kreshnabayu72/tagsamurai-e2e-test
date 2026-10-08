---
id: TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field
title: "Screening form Create, aksesibilitas dialog, dan validasi inline input Position Name"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-37
  - TC-GS-POS-38
  - TC-GS-POS-39
  - TC-GS-POS-40
  - TC-GS-POS-42
  - TC-GS-POS-43
  - TC-GS-POS-44
  - TC-GS-POS-45
  - TC-GS-POS-46
  - TC-GS-POS-50
  - TC-GS-POS-284
coverage:
  web: automated
---

# Screening form Create, aksesibilitas dialog, dan validasi inline input Position Name

## Prerequisites

- Login sebagai Role: Total Control
- Buka tab Position

## Test Steps

### Screening dan Aksesibilitas Form Create

1. Klik tombol primary "[+ Position]" di area Table Tools
2. Verifikasi modal Create Position terbuka menampilkan:
   - Header: Judul "Create Position" dan tombol close `[✕]`
   - Body: Field input "Position Name" dengan tanda bintang (*) wajib diisi
   - Footer: Checkbox "Stay on this form after submitting", tombol "[Clear Field]", dan tombol "[Submit]"
   - Tidak ada tombol "[Cancel]" di footer modal
3. Verifikasi input Position Name memiliki atribut aria-required="true" dan fokus berada di dalam modal (focus trap aktif)
4. Hover tombol "[Submit]" dan "[Clear Field]", verifikasi perubahan gaya visual hover

### Validasi Field Kosong dan Spasi

5. Klik tombol "[Submit]" saat input Position Name masih kosong
6. Verifikasi submit diblokir, input memiliki border error merah, dan pesan inline error "Position Name must not be empty" muncul
7. Ketik beberapa spasi (whitespace saja) ke dalam input lalu klik "[Submit]"
8. Verifikasi submit tetap diblokir dengan pesan error yang sama

### Validasi Batas Panjang Karakter

9. Masukkan teks sepanjang 121 karakter ke input Position Name
10. Verifikasi pesan inline error "Position Name max. 120 characters" langsung muncul saat pengetikan tanpa menunggu klik Submit
11. Ketik 120 karakter teks diikuti spasi (total 121 karakter), verifikasi error max 120 characters tetap muncul (dihitung sebelum trim)

### Validasi Emoji dan Clear Field

12. Coba ketik atau paste karakter emoji (misal: "Developer 🚀") ke dalam field Position Name
13. Verifikasi karakter emoji otomatis terfilter/diblokir dari field tanpa memunculkan pesan error
14. Klik tombol "[Clear Field]"
15. Verifikasi field Position Name kembali kosong, seluruh tanda error dibersihkan, dan modal tetap terbuka

## Notes

- Menggabungkan validasi input form Create dari TC-GS-POS-37, 38, 39, 40, 42, 43, 44, 45, 46, 50, dan 284.
