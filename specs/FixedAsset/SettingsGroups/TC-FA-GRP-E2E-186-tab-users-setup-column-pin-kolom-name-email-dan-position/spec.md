---
id: TC-FA-GRP-E2E-186-tab-users-setup-column-pin-kolom-name-email-dan-position
title: "Tab Users Setup Column: Pin Kolom Name, Email, dan Position"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-654
  - TC-FA-GRP-655
  - TC-FA-GRP-656
coverage:
  web: automated
---

# Tab Users Setup Column: Pin Kolom Name, Email, dan Position

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Lebar viewport 900px sehingga tabel dapat di-scroll horizontal; viewport disetel pada langkah 2 dan dipulihkan pada langkah 15.
- Tiap iterasi mem-pin satu kolom lalu melepasnya kembali (unpin) sehingga iterasi berikut mulai tanpa kolom terpin (batas 3 kolom terpin tidak terpicu).

  | Kolom |
  |---|
  | Name |
  | Email |
  | Position |

## Test Steps

1. Klik angka Total User Warehouse A
2. Setel lebar viewport 900px
3. Untuk setiap baris tabel Prerequisites (langkah 3 sampai 14): Buka Popup Setup Column
4. Pastikan kolom pada baris tabel tampil (kolom curated dicentang di Popup Setup Column)
5. Klik icon Pin kolom tersebut
6. Klik [Save]
7. Scroll tabel horizontal
8. Verifikasi kolom tersebut membeku (sticky) saat scroll horizontal
9. Refresh F5, lalu klik angka Total User Warehouse A
10. Scroll tabel horizontal
11. Verifikasi pin bertahan setelah F5 (kolom tersebut tetap membeku)
12. Buka Popup Setup Column, unpin kolom tersebut, lalu klik [Save]
13. Scroll tabel horizontal
14. Verifikasi setelah unpin kolom tersebut kembali ikut scroll
15. Pulihkan lebar viewport

## Notes

- Langkah 3 sampai 14 berulang untuk setiap baris tabel Prerequisites (Name, Email, Position); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7). Langkah penghubung (S-03): `Refresh F5, lalu klik angka Total User Warehouse A`, scroll horizontal sebelum asersi, dan unpin di akhir tiap iterasi.
- Spec memiliki 15 langkah nominal dan 39 langkah setelah ekspansi, di atas smell 35 langkah. Alasan: seluruh blok satu topik (pin Setup Column Tab Users pada dataset yang sama); ekspansi berasal dari perulangan tiga kolom tanpa langkah bersyarat (8b butir 7).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-654 sampai 656 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung. Scroll horizontal membutuhkan tabel yang lebih lebar dari viewport; spec menyetel lebar viewport 900px (langkah 2) dan memulihkannya (langkah 15), pola spec 100.
