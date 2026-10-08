---
id: TC-GS-USER-E2E-107-custom-field-value-input-edit
title: 'Input Custom Field di modal Edit: batas, pilihan, dan format per tipe'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-527
  - TC-GS-USER-528
  - TC-GS-USER-529
  - TC-GS-USER-530
  - TC-GS-USER-531
  - TC-GS-USER-532
  - TC-GS-USER-533
  - TC-GS-USER-534
  - TC-GS-USER-535
coverage:
  web: automated
---

# Input Custom Field di modal Edit: batas, pilihan, dan format per tipe

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Custom Field aktif untuk User: `Nomor Pajak` (Text, maks 120), `Catatan` (Text Area, maks 360), `Status Kerja` (Dropdown: Permanent, Contract), `Tanggal Lahir` (Date), `Bonus Multiplier` (Numeric, 2 desimal), `Telepon Darurat` (Phone, Required)
- User "Budi Santoso" punya value terisi untuk semua Custom Field di atas (`Status Kerja` = `Permanent`, `Tanggal Lahir` terisi)
- Spec ini tidak mengubah data: modal Edit ditutup tanpa Save

## Test Steps

1. Klik row action `Edit` pada baris "Budi Santoso"
2. Isi `Nomor Pajak` dengan 121 karakter
3. Verifikasi error real-time "Max. 120 characters"
4. Isi `Catatan` dengan 361 karakter
5. Verifikasi error real-time "Max. 360 characters"
6. Buka `Status Kerja`
7. Verifikasi native select berisi tepat opsi terdaftar dan `Permanent` sudah terpilih, tanpa input teks bebas
8. Buka `Tanggal Lahir`
9. Verifikasi date picker standar terbuka dengan tanggal existing terpilih dan tanpa pengetikan teks bebas
10. Ketik huruf lalu `1.234` di `Bonus Multiplier`
11. Verifikasi huruf tidak bisa masuk dan muncul error "Bonus Multiplier must have at most 2 decimal place(s)"
12. Amati `Telepon Darurat` yang sudah terisi
13. Verifikasi satu kontrol gabungan yang terisi, Country Code di kiri dan Number di kanan, dan Number tidak Disabled
14. Ketik huruf di Number
15. Verifikasi huruf tidak bisa masuk
16. Ganti Number menjadi 15, lalu 16, lalu 3 digit
17. Verifikasi 15 digit valid, 16 digit menampilkan "Max. 15 characters", dan 3 digit menampilkan "Min. 4 characters"
18. Kosongkan salah satu bagian (Country Code atau Number) lalu klik `[Save]`
19. Verifikasi "Telepon Darurat must not be empty" muncul
20. Tutup modal dengan `✕`

## Notes

- Sumber `user.md` bagian 4.4 dan 6. Pasangan Edit dari `TC-GS-USER-E2E-106-custom-field-value-input-create` (Prinsip Simetri Create/Edit). Round-trip Phone dicakup `TC-GS-USER-E2E-043-phone-custom-field-roundtrip`.
