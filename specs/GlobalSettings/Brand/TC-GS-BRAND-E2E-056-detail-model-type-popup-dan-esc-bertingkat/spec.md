---
id: TC-GS-BRAND-E2E-056-detail-model-type-popup-dan-esc-bertingkat
title: "Brand Detail: Popup Model/Type dan Esc Bertingkat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-201
  - TC-GS-BRAND-202
coverage:
  web: automated
---

# Brand Detail: Popup Model/Type dan Esc Bertingkat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, hanya dibaca, tanpa suffix `{runId}`): brand `Vertex Labs` dengan Item Type Laptop bermodel `Nova 5 Pro`, `Nova Slim 3`, `Vertex Pro 14`, `Vertex Pro 16`, `Vertex Pro 20` (5 model; tabel menampilkan 2 chip dan `+3 more`).
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup. Population D-01 tidak dibutuhkan; baris Vertex Labs dicari lewat Search `Vertex Labs`.
- Kemampuan teknis: simulasi keyboard Esc (dua kali berurutan).
- Precondition TC-GS-BRAND-201, 202: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.
- State global yang dipulihkan: tidak ada.

## Test Steps

### TC-GS-BRAND-201: Popup Model/Type bertingkat dari +N more

1. Search `Vertex Labs` pada tabel Brand
2. Klik `⋯` pada baris Vertex Labs
3. Klik Detail → modal Brand Detail tampil
4. Klik `+3 more` pada baris Laptop di accordion Item Type List → modal `Model / Type` tampil
5. Verifikasi modal `Model / Type` tampil di atas modal Brand Detail
6. Verifikasi subtitle modal `Laptop (5)`
7. Verifikasi chip `Nova 5 Pro`, `Nova Slim 3`, `Vertex Pro 14`, `Vertex Pro 16`, `Vertex Pro 20` (urut A-Z)
8. Verifikasi modal `Model / Type` tidak memiliki kolom Product

### TC-GS-BRAND-202: Esc pada modal Model/Type menutup modal kecil dulu

9. Tekan Esc
10. Verifikasi modal `Model / Type` tertutup
11. Verifikasi modal Brand Detail tetap tampil
12. Tekan Esc
13. Verifikasi modal Brand Detail tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah 1-4 TC-GS-BRAND-202 (buka Detail Vertex Labs, klik `+3 more` baris Laptop) identik dengan langkah 1-4 TC-GS-BRAND-201 dan tidak diulang: keduanya berbagi kondisi modal `Model / Type` terbuka di atas Brand Detail. Tidak ada kasus lain di spec yang butuh Brand Detail terbuka sesudah Esc kedua, sehingga TC-GS-BRAND-202 yang menutup modal ditaruh terakhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search `Vertex Labs` untuk menemukan baris brand).
