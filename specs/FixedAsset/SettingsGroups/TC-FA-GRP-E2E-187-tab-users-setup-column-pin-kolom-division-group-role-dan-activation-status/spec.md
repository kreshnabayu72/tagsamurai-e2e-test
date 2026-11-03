---
id: TC-FA-GRP-E2E-187-tab-users-setup-column-pin-kolom-division-group-role-dan-activation-status
title: "Tab Users Setup Column: Pin Kolom Division, Group Role, dan Activation Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-657
  - TC-FA-GRP-658
  - TC-FA-GRP-660
coverage:
  web: automated
---

# Tab Users Setup Column: Pin Kolom Division, Group Role, dan Activation Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- State yang diubah spec: konfigurasi Setup Column tersimpan; dipulihkan lewat hook `after` (hapus preferensi kolom di browser; kemampuan disediakan tim FE).
- Lebar viewport 900px sehingga tabel dapat di-scroll horizontal; viewport disetel pada langkah 2 dan dipulihkan pada langkah 26.
- Tiap iterasi mem-pin satu kolom lalu melepasnya kembali (unpin) sehingga iterasi berikut mulai tanpa kolom terpin (batas 3 kolom terpin tidak terpicu).

  | Kolom default (sudah tampil, tidak perlu dicentang) |
  |---|
  | Division |
  | Group Role |

  | Kolom curated (perlu dicentang di Popup Setup Column) |
  |---|
  | Activation Status |

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Setel lebar viewport 900px
3. Untuk setiap baris tabel kolom default (langkah 3 sampai 13): Buka Popup Setup Column
4. Klik icon Pin kolom tersebut
5. Klik [Save]
6. Scroll tabel horizontal
7. Verifikasi kolom tersebut membeku (sticky) saat scroll horizontal
8. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
9. Scroll tabel horizontal
10. Verifikasi pin bertahan setelah F5 (kolom tersebut tetap membeku)
11. Buka Popup Setup Column, unpin kolom tersebut, lalu klik [Save]
12. Scroll tabel horizontal
13. Verifikasi setelah unpin kolom tersebut kembali ikut scroll
14. Untuk setiap baris tabel kolom curated (langkah 14 sampai 25): Buka Popup Setup Column
15. Centang kolom pada baris tabel di Popup Setup Column
16. Klik icon Pin kolom tersebut
17. Klik [Save]
18. Scroll tabel horizontal
19. Verifikasi kolom tersebut membeku (sticky) saat scroll horizontal
20. Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
21. Scroll tabel horizontal
22. Verifikasi pin bertahan setelah F5 (kolom tersebut tetap membeku)
23. Buka Popup Setup Column, unpin kolom tersebut, lalu klik [Save]
24. Scroll tabel horizontal
25. Verifikasi setelah unpin kolom tersebut kembali ikut scroll
26. Pulihkan lebar viewport

## Notes

- Langkah 3 sampai 13 berulang untuk baris tabel kolom default (Division, Group Role); langkah 14 sampai 25 berulang untuk baris tabel kolom curated (Activation Status) dan diawali langkah mencentang kolom, karena kolom default sudah tampil (8b butir 7); satu `Verifikasi` per klausa tetap dipertahankan (8b butir 7). Langkah penghubung (S-03): `Refresh F5, lalu ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A`, scroll horizontal sebelum asersi, dan unpin di akhir tiap iterasi.
- Spec memiliki 26 langkah nominal dan 37 langkah setelah ekspansi (2 + 2 x 11 + 12 + 1), di atas smell 35 langkah. Alasan: seluruh blok satu topik (pin Setup Column Tab Users pada dataset yang sama); ekspansi berasal dari perulangan kolom tanpa langkah bersyarat (8b butir 7).
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-657, 658, dan 660 menulis "Refresh F5" tanpa menyebut keadaan popup sesudahnya; spec membuka kembali Tab Users sebagai langkah penghubung. Scroll horizontal membutuhkan tabel yang lebih lebar dari viewport; spec menyetel lebar viewport 900px (langkah 2) dan memulihkannya (langkah 26), pola spec 100.
