---
id: TC-FA-CAT-E2E-203-tab-baru-mulai-dari-default-tanpa-state-tab-pertama
title: "Tab Browser Baru Memulai dari Default: All Categories Tanpa Search dan Filter"
priority: Low
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-379
coverage:
  web: automated
---

# Tab Browser Baru Memulai dari Default: All Categories Tanpa Search dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` menutup tab kedua bila masih terbuka dan mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), hanya dibaca dan tidak diubah: L1 `Electronics` (berisi L2 `Laptop`). Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`).
- Konteks kedua: tab browser baru pada jendela browser yang sama dengan sesi aktor; state yang tampil di tab baru itu adalah objek asersi spec ini (konteks kedua kelas c).
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-379: Tab baru memulai dari default

1. Klik node `Electronics` di Sidebar Category Tree
2. Ketik Search `Lap`, tekan Enter
3. Buka tab browser baru ke Fixed Asset > Settings > Categories
4. Verifikasi tab baru menampilkan `All Categories`
5. Verifikasi tab baru tanpa Search dan tanpa Filter
6. Tutup tab baru dan kembali ke tab pertama

## Notes

- Langkah penghubung (S-03): langkah 6 (menutup tab baru).
- Konteks tab kedua adalah objek asersi (perilaku tab baru terhadap state tab pertama), sehingga spec ini tergolong kelas c (prinsip 13 bagian 3) dan berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-CAT-379 hanya mengharapkan keadaan tab baru; state tab pertama sesudah tab baru dibuka tidak diasersi.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
