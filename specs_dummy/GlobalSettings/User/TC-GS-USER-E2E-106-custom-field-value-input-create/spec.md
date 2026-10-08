---
id: TC-GS-USER-E2E-106-custom-field-value-input-create
title: 'Input Custom Field di modal Create: batas, pilihan, dan format per tipe'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-505
  - TC-GS-USER-506
  - TC-GS-USER-507
  - TC-GS-USER-508
  - TC-GS-USER-509
  - TC-GS-USER-510
  - TC-GS-USER-511
  - TC-GS-USER-512
  - TC-GS-USER-513
coverage:
  web: automated
---

# Input Custom Field di modal Create: batas, pilihan, dan format per tipe

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Custom Field aktif untuk User: `Nomor Pajak` (Text, maks 120), `Catatan` (Text Area, maks 360), `Status Kerja` (Dropdown: Permanent, Contract), `Tanggal Lahir` (Date), `Bonus Multiplier` (Numeric, 2 desimal), `Telepon Darurat` (Phone, Required)
- Spec ini tidak mengubah data: modal Create ditutup tanpa Submit

## Test Steps

1. Klik `[+ User]`
2. Isi `Nomor Pajak` dengan 121 karakter
3. Verifikasi error real-time "Max. 120 characters"
4. Isi `Catatan` dengan 361 karakter
5. Verifikasi error real-time "Max. 360 characters"
6. Buka `Status Kerja`
7. Verifikasi berupa native select dengan tepat opsi terdaftar (`Permanent`, `Contract`) tanpa input teks bebas
8. Buka `Tanggal Lahir`
9. Verifikasi date picker standar terbuka, tidak ada pengetikan teks bebas, dan hasil pilihan selalu tanggal valid
10. Ketik huruf di `Bonus Multiplier`
11. Verifikasi huruf tidak bisa masuk (keystroke filter)
12. Ketik `1.234` di `Bonus Multiplier`
13. Verifikasi error real-time "Bonus Multiplier must have at most 2 decimal place(s)"
14. Amati `Telepon Darurat`
15. Verifikasi satu kontrol gabungan dengan Country Code (dropdown searchable) di kiri dan Number di kanan, dan Number tidak Disabled menunggu Country Code dipilih
16. Ketik huruf di Number
17. Verifikasi huruf tidak bisa masuk
18. Pilih `+62` lalu isi Number dengan 15 digit
19. Verifikasi valid (Country Code tidak dihitung ke batas 15 digit)
20. Ganti Number menjadi 16 digit
21. Verifikasi error "Max. 15 characters"
22. Ganti Number menjadi 3 digit
23. Verifikasi error real-time "Min. 4 characters"
24. Kosongkan Number dengan Country Code masih terisi lalu klik `[Submit]`, kemudian ulangi dengan Country Code kosong dan Number terisi
25. Verifikasi kedua percobaan menampilkan "Telepon Darurat must not be empty" (kedua bagian harus terisi)
26. Tutup modal dengan `✕`

## Notes

- Sumber `user.md` bagian 4.4 dan 6, serta `custom-field-user/PRD/custom-field-user.md` bagian 4.2 dan 6. Aturan widget dan validasi mengikuti definisi Custom Field yang sama dengan modal Edit.
- Pasangan Edit: `TC-GS-USER-E2E-107-custom-field-value-input-edit`. Placeholder dicakup `TC-GS-USER-E2E-108-custom-field-placeholder`.
