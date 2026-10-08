---
id: TC-GS-GSET-E2E-016-aksesibilitas-form-dan-dialog
title: Aksesibilitas form dan dialog
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-37
  - TC-GS-GSET-38
coverage:
  web: automated
---

# Aksesibilitas: ARIA wajib pada form dan dialog

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Form dalam keadaan kosong pada `Currency` untuk membuktikan `aria-required`; field lain diisi agar
  `aria-describedby` dapat dibuktikan.
- Verifikasi ARIA dilakukan dengan pemeriksaan DOM atribut, bukan hanya perilaku klik.

## Test Steps

### Form: atribut wajib dan deskripsi

1. Buka halaman `Global Settings > General Settings`
2. Verifikasi field `Currency`, `Time Zone`, `Session Idle Timeout`, `Date Format`, dan `Time Format`
   memiliki atribut `aria-required` bernilai `true` (atau pola ekspos yang setara)
3. Verifikasi tiap field memiliki kaitan `aria-describedby` ke elemen bantuan/penjelas yang sesuai
   (misal teks preview/tooltip/helper text)
4. Verifikasi atribut `aria-describedby` dan `aria-required` mengikuti perubahan state field (tidak statis)
5. Verifikasi elemen bantu yang dirujuk `aria-describedby` ada di DOM dan berisi teks yang tidak kosong

### Dialog: fokus dan pembacaan layar

6. Ubah `Currency` menjadi `$ - US Dollar` sehingga dialog `Change Currency` terbuka
7. Verifikasi dialog ditandai sebagai modal (atribut `role="dialog"`/`aria-modal`) dan diberi judul yang
   terbaca oleh assistive tech
8. Verifikasi fokus pindah ke dalam dialog saat terbuka
9. Verifikasi fokus terkunci/terperangkap di dalam dialog (Tab tetap berputar di dalam, tidak keluar ke
   background)
10. Verifikasi menekan `Esc` menutup dialog dan fokus kembali ke elemen pemicu (`Currency`)
11. Verifikasi elemen background tidak dapat difocus ketika dialog terbuka
12. Verifikasi saat form dimuat ulang tanpa dialog, elemen fokus awal berada pada field pertama yang dapat
    difokus

## Notes

- Spesifikasi nilai `aria-required` mengikuti implementasi aktual komponen; spec menuntut ekspos
  aksesibilitas yang setara, bukan literal `true` keras.