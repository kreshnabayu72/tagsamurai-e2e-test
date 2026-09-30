---
id: TC-GS-USER-E2E-043-phone-custom-field-roundtrip
title: Custom Field Phone tersimpan gabungan dan terbaca kembali di Modal Edit
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-514
coverage:
  web: automated
---

# Custom Field Phone tersimpan gabungan dan terbaca kembali di Modal Edit

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Custom Field User bertipe Phone bernama "Nomor Telepon", tidak wajib, ada di form User
- User "Budi Santoso" ada tanpa value pada Custom Field "Nomor Telepon"
- Spec ini mengisi Phone "Budi Santoso", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Buka Modal Edit "Budi Santoso"
2. Pada Custom Field "Nomor Telepon", pilih Country Code "+62" dan isi Number "812345678901234"
3. Klik `[Save]`
4. Verifikasi toast "Success, user has been updated." muncul
5. Buka Modal Edit "Budi Santoso" lagi
6. Verifikasi Country Code "+62" dan Number "812345678901234" tampil terpisah di kedua sub-kontrol
7. Verifikasi nilai yang tersimpan memakai panjang kode dari katalog kode negara dan bukan posisi karakter tetap (nilai gabungan "+62812345678901234" terbaca kembali dengan benar)

## Notes

- Nilai Phone disimpan sebagai satu string gabungan tanpa separator. Yang diuji di sini adalah penyimpanan dan pembacaan kembali di backend, sedangkan perilaku input (keystroke, boundary 4 sampai 15 digit, placeholder) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Langkah 7 mengikuti `TC-GS-USER-514`: parsing memakai panjang kode dari katalog. Variasi kode negara dengan panjang berbeda (misalnya "+1" dan "+62") bisa ditambahkan bila QA menginginkan cakupan lebih luas.
