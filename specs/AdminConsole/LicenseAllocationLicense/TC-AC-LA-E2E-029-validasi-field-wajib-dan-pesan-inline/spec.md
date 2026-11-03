---
id: TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline
title: "Validasi Field Wajib Form Allocate: Type, Client, Target, Pesan Inline, dan Aksesibilitas"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-108
  - TC-AC-LA-109
  - TC-AC-LA-110
  - TC-AC-LA-118
  - TC-AC-LA-119
coverage:
  web: automated
---

# Validasi Field Wajib Form Allocate: Type, Client, Target, Pesan Inline, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup: Client PT Sejahtera (#19, term `SUBS-20260101-A1B2C`).
- Data Dinamis: tidak ada; seluruh `[Submit]` diblokir validasi sehingga tidak ada alokasi yang dibuat.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum aksi pertama (langkah 1) sebagai pembanding "tidak ada record".
- Kemampuan teknis: membaca atribut `aria-required` dan `aria-describedby` field form.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat baseline Allocation ID baris di halaman pertama tab Current
2. Klik `[+ Allocation]`

### TC-AC-LA-119 (bagian fokus): aksesibilitas form Allocate

3. Tekan `Tab` berurutan sampai melewati elemen terakhir modal
4. Verifikasi fokus terjebak di dalam modal saat `Tab`

### TC-AC-LA-109 dan TC-AC-LA-118: Client kosong ditolak, pesan hilang setelah diisi

5. Biarkan semua field kosong lalu klik `[Submit]`
6. Verifikasi pesan inline di bawah Client `Client must not be empty`
7. Verifikasi form tetap terbuka
8. Pilih Client `PT Sejahtera`
9. Verifikasi pesan Client `Client must not be empty` hilang

### TC-AC-LA-110: Target kosong ditolak

10. Biarkan Target kosong lalu klik `[Submit]`
11. Verifikasi pesan inline di bawah Target `Target must not be empty`
12. Verifikasi form tetap terbuka

### TC-AC-LA-108: Type kosong ditolak

13. Pilih Target `SUBS-20260101-A1B2C`, biarkan Type kosong, lalu klik `[Submit]`
14. Verifikasi pesan inline di bawah Type `Type must not be empty`
15. Verifikasi form tetap terbuka

### TC-AC-LA-119 (bagian atribut): aria-required dan aria-describedby

16. Pilih Type `Concurrent User` agar Additional Quantity tampil
17. Verifikasi Client, Target, Type, dan Additional Quantity memiliki `aria-required`
18. Biarkan Additional Quantity kosong lalu klik `[Submit]`
19. Verifikasi field yang menampilkan pesan error memiliki `aria-describedby` ke pesan itu
20. Klik `[Clear Field]`
21. Tekan `Esc`
22. Verifikasi modal tertutup

### Tidak ada record

23. Verifikasi sedikitnya satu baris tampil pada tab Current
24. Verifikasi daftar Allocation ID baris di halaman pertama tab Current sama dengan baseline langkah 1 (tidak ada record baru dari TC-AC-LA-108, 109, dan 110)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 21 sampai 22).
- Penyimpangan urutan (S-05, S-10): TC-AC-LA-119 dijalankan dalam dua bagian. Bagian fokus (langkah 3 sampai 4) dijalankan pada form pristine di awal, bagian `aria-required` dan `aria-describedby` (langkah 16 sampai 19) setelah Additional Quantity tampil (field itu baru dirender setelah Type dipilih), dan `Esc` (langkah 21) sesudah `[Clear Field]` agar form pristine dan modal tertutup tanpa dialog. TC-AC-LA-118 Expected a dan TC-AC-LA-109 Expected a memiliki kondisi yang sama (Submit dengan form kosong, langkah 5 sampai 6) sehingga satu `Verifikasi` memenuhi keduanya; TC-AC-LA-118 Expected b diasersi di langkah 9. TC-AC-LA-108, 109, dan 110 membagi satu `Verifikasi` "tidak ada record" pada langkah 23 sampai 24 karena modal menutupi daftar selama form terbuka.
- Langkah penghubung (S-03): langkah 1 (baseline), langkah 8, 13, dan 16 (mengisi field agar pesan berikutnya dapat dimunculkan), langkah 20 sampai 21 (membuat form pristine sebelum `Esc`). Langkah 23 adalah anchor positif untuk asersi langkah 24 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-118 berjudul "semua pesan wajib sekaligus" tetapi Expected hanya menyebut pesan Client; TC-AC-LA-184 menyatakan Submit kosong memunculkan pesan V-01, V-02, V-04 sekaligus. Spec hanya mengasersi pesan Client sesuai Expected TC-AC-LA-109 dan TC-AC-LA-118.
  - TC-AC-LA-108 Expected b ("tidak ada record maupun log") berisi asersi absence log; asersi itu hanya sah di spec absence (S-05) dan tidak diasersi di sini. Perlu spec absence dengan aksi nyata untuk TC-AC-LA-108 atau keputusan QA.
  - TC-AC-LA-119 Langkah 1 memeriksa `aria-required` Additional Quantity pada form yang baru dibuka, padahal field itu belum dirender sebelum Type dipilih.
  - TC-AC-LA-119 Expected b tidak menyebut field mana yang menampilkan error pada langkah 2 ("Submit kosong"); spec memeriksa field yang berpesan error (Additional Quantity pada langkah 18).
