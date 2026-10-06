---
id: TC-GS-GSET-E2E-039-currency-data-existing-presisi-dan-tanpa-konversi
title: Data existing presisi >2 desimal dan tanpa konversi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-135
  - TC-GS-GSET-136
coverage:
  web: automated
---

# Data existing: presisi dan ketiadaan konversi pada ganti currency

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Hook menyiapkan nilai tersimpan `Currency = IDR` dan entitas child yang menyimpan nilai bertipe angka
  (misal harga) dengan presisi di atas 2 desimal pada environment bersih.
- `after` Mengembalikan nilai & currency ke kondisi awal.

## Test Steps

### Membaca data presisi penuh

1. Buka `Global Settings > General Settings`
2. Verifikasi field/nilai pada aplikasi yang menampilkan angka presisi penuh (contoh `1.2345678`)
    dirender tanpa pembulatan yang mengubah nilai (round setengah ke atas di mana PRD mensyaratkan)
3. Verifikasi nilai yang tersimpan dengan desimal >2 ditampilkan lengkap (tidak dipotong jadi 2 desimal
    kecuali PRD menyatakan pembulatan tampilan)

### Ganti currency tanpa konversi

4. Ubah `Currency` via dialog ke `$ - US Dollar`
5. Klik `[Save]`
6. Verifikasi besaran nilai (contoh `1.2345678`) TIDAK berubah; hanya representasi simbol yang
    menyesuaikan (Rp → $)
7. Verifikasi tidak ada nilai child/entitas lain yang ternyata diubah oleh perubahan currency (tidak
    terjadi konversi nilai di backend)
8. Kembalikan `Currency` ke `IDR` dan simpan untuk menutup kondisi

## Notes

- PMC `CURRENCY-SYMBOL` terpenuhi: ganti currency hanya mengganti simbol format tampilan, tidak
  mengubah besaran numerik tersimpan. Pembulatan (round-half-up ke 2 desimal) hanya perilaku tampilan
  bila PRD menyatakannya — tidak mengubah data persisten.