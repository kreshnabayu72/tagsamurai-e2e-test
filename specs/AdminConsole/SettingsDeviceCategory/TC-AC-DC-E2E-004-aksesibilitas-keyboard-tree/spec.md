---
id: TC-AC-DC-E2E-004-aksesibilitas-keyboard-tree
title: "Aksesibilitas Tree Category: Navigasi Keyboard, Pengumuman Error Inline Polite, Fokus Dialog Terjebak, dan Tooltip Aksi saat Fokus Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-9
  - TC-AC-DC-10
  - TC-AC-DC-279
coverage:
  web: automated
---

# Aksesibilitas Tree Category: Navigasi Keyboard, Pengumuman Error Inline Polite, Fokus Dialog Terjebak, dan Tooltip Aksi saat Fokus Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Data Pre-setup #14 (Pohon Uji Kategori) dan #15 (Device Name `HR-100` yang merujuk `Dipakai Leaf`) hanya dibaca. Aksi Delete pada `Dipakai Leaf` selalu diblokir guard referensi dan tidak mengubah data (S-06); `[Submit]` dengan input kosong ditolak validasi dan tidak membuat node.
- Pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis (kelas d, teknologi bantu sebagai objek uji): input keyboard (Tab, Enter, Arrow), pembacaan atribut pengumuman screen reader (`aria-live`) pada elemen error inline, dan pembacaan elemen yang sedang fokus.
- Kondisi awal tiap spec: halaman baru dibuka hook `beforeEach`, sehingga `Hardware` dan `TAG` collapsed, tidak ada pilihan filter Category, dan kotak pencarian tree kosong.
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DC-9: Tree dapat dioperasikan dengan keyboard Tab, Arrow, dan Enter

1. Tekan Tab hingga fokus berada di node `Hardware`
2. Verifikasi fokus keyboard berada di node `Hardware` tanpa memakai mouse
3. Tekan Enter
4. Verifikasi Enter meng-expand node `Hardware` yang terfokus
5. Tekan Arrow Down
6. Verifikasi fokus berpindah ke node anak pertama yang terlihat (`BLE Gateway`)

### TC-AC-DC-10: Accessibility: error inline dibacakan polite dan dialog menjebak fokus

7. Klik panah node `Handheld Reader`
8. Hover node `Rugged Scanner`
9. Klik aksi `+ Subcategory`
10. Klik `[Submit]` dengan input kosong
11. Verifikasi elemen error inline memiliki atribut pengumuman screen reader dengan nilai polite
12. Tutup input inline dengan menekan Esc
13. Hover node `Dipakai Leaf`
14. Klik aksi Delete
15. Tekan Tab berulang kali (lebih banyak dari jumlah elemen yang dapat difokuskan di dialog)
16. Verifikasi fokus keyboard tetap berada di dalam dialog dan tidak berpindah ke tree di belakangnya
17. Tutup dialog dengan menekan Esc

### TC-AC-DC-279: Tooltip aksi node tampil saat aksi menerima fokus keyboard

18. Hover node `Rugged Scanner` agar aksi tampil
19. Pindahkan fokus keyboard ke aksi `+ Subcategory`
20. Verifikasi tooltip "+ Subcategory" tampil
21. Pindahkan fokus keyboard ke aksi Edit
22. Verifikasi tooltip "Edit" tampil
23. Pindahkan fokus keyboard ke aksi Delete
24. Verifikasi tooltip "Delete" tampil

## Notes

- Kelas harness: d (ARIA live dan fokus dialog sebagai objek uji); tidak ada pengamat tambahan.
- Langkah penghubung (S-03): langkah 7 meng-expand `Handheld Reader` (`Hardware` sudah ter-expand oleh langkah 3) supaya `Rugged Scanner` dan `Dipakai Leaf` terlihat; langkah 12 menutup input inline kosong (tidak dirty, tidak memicu dialog Unsaved Changes); langkah 17 menutup dialog blok.
- Temuan untuk QA: (1) TC-AC-DC-9 Expected c menyebut Arrow key memindahkan fokus ke node "berikutnya atau sebelumnya", tetapi langkah TC hanya memakai Arrow Down; asersi ke node sebelumnya tidak ditulis. (2) TC-AC-DC-10 tidak menyebut tombol dialog blok referensi dan cara menutupnya; dialog ditutup dengan Esc. (3) TC-AC-DC-10 tidak menyebut jumlah Tab; spec memakai Tab berulang melebihi jumlah elemen fokus dialog.