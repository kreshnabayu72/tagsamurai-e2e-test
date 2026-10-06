---
id: TC-GS-GSET-E2E-013-revert-currency-pasca-cancel-dialog
title: "Revert manual Currency Code pasca Cancel dan bypass gate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-149
  - TC-GS-GSET-150
coverage:
  web: automated
---

# Revert manual Currency Code pasca Cancel dan bypass gate submit

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Currency tersimpan saat ini `IDR`. Resolver `after` memastikan `currency_code` tetap `IDR` setelah
  spec.
- Menjalankan alur di spec 012 TC-GS-GSET-28 dulu (Cancel pada dialog → form dirty dgn USD).

## Test Steps

### Revert manual pasca Cancel — tombol Save non-aktif & navigasi bebas

1. Buka halaman `Global Settings > General Settings`
2. Ubah `Currency Code` ke `$ - US Dollar`, klik `[Save]`, dialog `Change Currency` muncul
3. Klik `[Cancel]` (dialog tutup, form dirty dgn USD sesuai TC-GS-GSET-28)
4. Buka dropdown `Currency Code`, pilih kembali `IDR` (nilai tersimpan)
5. Verifikasi dropdown kembali `IDR`
6. Verifikasi tombol `[Save]` otomatis kembali Disabled (tidak ada perubahan lagi)
7. Navigasikan keluar halaman (klik Back/menu lain)
8. Verifikasi langsung keluar tanpa Dialog Unsaved Changes (form sudah bersih)

### Bypass dialog saat Currency sudah dikembalikan tapi field lain berubah

9. Ubah kembali `Currency Code` ke `$ - US Dollar`, klik `[Save]`, dialog muncul, klik `[Cancel]`
10. Kembalikan `Currency Code` ke `IDR` (dengan cara langkah 4-5)
11. Ubah `Time Zone` ke zona lain (misal `(UTC+08:00) Perth`)
12. Verifikasi tombol `[Save]` kembali enabled (karena Time Zone berubah)
13. Klik `[Save]`
14. Verifikasi request `PUT` langsung terkirim **tanpa** memunculkan Dialog `Change Currency`
15. Verifikasi toast sukses `Success, general settings has been saved.`
16. Verifikasi nilai `Time Zone` tersimpan; `Currency Code` tetap `IDR`

## Notes

- Gate `GSET-LOGIC-04` menghitung perubahan dari nilai tersimpan saat ini, bukan dari riwayat
  dirty-session sebelumnya. Soal langkah 14 membuktikan: selama Currency yang DIKIRIM = `IDR`, tidak ada
  dialog walaupun sesi sempat memegang USD.
- Perilaku Cancel yang belum mereset (langkah 3) dijembatani ke spec 012 TC-GS-GSET-28.