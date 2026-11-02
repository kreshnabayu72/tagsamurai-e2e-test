---
id: TC-FA-GRP-E2E-189-tab-users-setup-column-pin-kolom-custom-field-dan-sel-tanpa-nilai-tampil-dash
title: "Tab Users Setup Column: Pin Kolom Custom Field dan Sel Tanpa Nilai Tampil Dash (Bukan Blank)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-664
  - TC-FA-GRP-1061
coverage:
  web: automated
---

# Tab Users Setup Column: Pin Kolom Custom Field dan Sel Tanpa Nilai Tampil Dash (Bukan Blank)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user, termasuk user tanpa Position, user tanpa Division, user non-Temporary (Temporary Until kosong), user tanpa TAG, dan user tanpa nilai pada Custom Field aktif Phone (Data Dinamis, dibaca saja). Data ini tidak punya tabel konkret di TC (lihat Temuan untuk QA).
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Kolom Temporary Until, TAG, dan Custom Field Phone adalah kolom curated yang ditampilkan lewat Column Visibility; pemulihan lewat hook `after`.

## Test Steps

1. Klik angka Total User Warehouse A

### TC-664: Pin kolom Custom Field Phone

2. Buka Popup Setup Column
3. Centang kolom Custom Field aktif Phone
4. Klik icon Pin Custom Field aktif Phone
5. Klik [Save]
6. Scroll tabel horizontal
7. Verifikasi kolom Custom Field aktif Phone membeku (sticky) saat scroll horizontal
8. Refresh F5, lalu klik angka Total User Warehouse A
9. Scroll tabel horizontal
10. Verifikasi pin bertahan setelah F5 (kolom tetap membeku)
11. Buka Popup Setup Column, unpin kolom Custom Field aktif Phone, lalu klik [Save]
12. Scroll tabel horizontal
13. Verifikasi setelah unpin kolom kembali ikut scroll

### TC-1061: Sel tanpa nilai tampil dash

14. Tampilkan kolom Temporary Until, TAG, dan Custom Field aktif Phone via Column Visibility
15. Amati sel user tanpa Position, tanpa Division, non-Temporary, tanpa TAG, dan tanpa nilai Custom Field
16. Verifikasi sel Position dan Division yang tidak bernilai tampil `—`
17. Verifikasi sel Temporary Until user non-Temporary tampil `—`
18. Verifikasi sel TAG dan Custom Field yang tidak bernilai tampil `—`
19. Verifikasi sel tidak blank dan tidak berisi teks null

## Notes

- Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A`, scroll horizontal sebelum asersi, dan unpin di akhir TC-664.
- Spec memiliki 19 langkah, di bawah smell 35 langkah. Scroll horizontal membutuhkan tabel yang lebih lebar dari viewport; viewport disesuaikan tim FE bila perlu.
- Temuan untuk QA:
  - TC-1061 menyebut data user tanpa nilai tanpa tabel konkret; spec memakai Warehouse A (Prerequisites).
  - TC-664 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung.
