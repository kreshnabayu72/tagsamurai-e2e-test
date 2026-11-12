---
id: TC-AC-LA-E2E-030-validasi-additional-quantity
title: "Validasi Additional Quantity: Kosong, Nol, Non-Digit, dan Lebih dari 15 Karakter"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-111
  - TC-AC-LA-112
  - TC-AC-LA-114
  - TC-AC-LA-116
coverage:
  web: automated
---

# Validasi Additional Quantity: Kosong, Nol, Non-Digit, dan Lebih dari 15 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`).
- Data Dinamis: tidak ada; seluruh `[Submit]` diblokir validasi sehingga tidak ada alokasi yang dibuat.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum aksi pertama (langkah 1).
- Tabel "Input non-digit" untuk langkah 8 sampai 10 (TC-AC-LA-114):

  | Input | Cara | Isi field setelah input |
  |---|---|---|
  | `abc` | ketik | kosong (tidak ada karakter yang masuk) |
  | `1.5` | ketik | `15` |
  | `-3` | ketik | `3` |
  | `5,2` | ketik | `52` |
  | `7.9` | tempel dari clipboard | `79` |

- Kemampuan teknis: mengetik dan menempel teks dari clipboard ke field Additional Quantity.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`

### TC-AC-LA-111: Additional Quantity kosong ditolak (V-13)

4. Biarkan Additional Quantity kosong lalu klik `[Submit]`
5. Verifikasi pesan inline di bawah Additional Quantity `Additional Quantity must not be empty`

### TC-AC-LA-112: Additional Quantity nol ditolak (V-14)

6. Isi Additional Quantity `0` lalu klik `[Submit]`
7. Verifikasi pesan inline `Additional Quantity must be greater than 0`

### TC-AC-LA-114: Karakter non-digit diblok saat ketik dan paste

Untuk setiap baris tabel "Input non-digit" (langkah 8 sampai 10):

8. Kosongkan field Additional Quantity
9. Ketik atau tempel nilai kolom Input sesuai kolom Cara
10. Verifikasi isi field sama dengan kolom "Isi field setelah input"
11. Verifikasi pesan V-15 `Additional Quantity must be a whole number` tidak tampil lewat UI normal

### TC-AC-LA-116: Lebih dari 15 karakter

12. Kosongkan field Additional Quantity lalu ketik 16 digit `1234567890123456`
13. Verifikasi error real-time `Max. 15 characters` tampil di bawah field
14. Klik `[Submit]`
15. Verifikasi error `Max. 15 characters` masih tampil setelah `[Submit]`
16. Klik `[×]` pada header
17. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
18. Klik `[Leave]`

### Tidak ada record

19. Verifikasi sedikitnya satu baris tampil pada tab Current
20. Verifikasi daftar Allocation ID baris di halaman pertama tab Current sama dengan baseline langkah 1 (tidak ada record dari TC-AC-LA-111, 112, dan 116)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 16 sampai 18).
- Langkah 8 sampai 10 diulang untuk 5 baris tabel (bagian 8b butir 7); ekspansi: 5 × 3 = 15 langkah, sehingga hitungan ekspansi spec ±32 langkah, di bawah ambang. Langkah 11 diasersi sekali sesudah iterasi terakhir untuk seluruh input (Expected b TC-AC-LA-114).
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 3 (mengisi field yang tidak diuji), langkah 8 (mengosongkan field sebelum iterasi, R-12), langkah 16 sampai 18 (menutup form dirty, S-08). Langkah 19 adalah anchor positif untuk asersi langkah 20 (bagian 8b butir 2). Asersi "tidak ada record" TC-AC-LA-111, 112, dan 116 dikumpulkan pada langkah 19 sampai 20 karena modal menutupi daftar selama form terbuka.
- Urutan blok mengikuti S-10 (validasi diblokir lebih dahulu, kasus menutup form di akhir).
- Temuan untuk QA:
  - TC-AC-LA-111 dan TC-AC-LA-112 Expected b ("Tidak ada record") serta Post Condition "Tidak ada record" tidak punya langkah observasi di TC; spec memakai perbandingan daftar terhadap baseline dan tidak mengasersi log.
  - TC-AC-LA-114 Expected b ("Pesan V-15 tidak tampil lewat UI normal") tidak menyebut teksnya; teks `Additional Quantity must be a whole number` diambil dari TC-AC-LA-115.
  - TC-AC-LA-116 Expected b ("Submit tidak menyimpan record selama error tampil") tidak menyebut perilaku tombol `[Submit]` (disabled atau tetap aktif tetapi ditolak); spec hanya mengasersi error tetap tampil dan tidak ada record baru.
