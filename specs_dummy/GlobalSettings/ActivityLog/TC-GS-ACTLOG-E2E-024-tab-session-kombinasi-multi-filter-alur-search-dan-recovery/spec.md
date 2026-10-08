---
id: TC-GS-ACTLOG-E2E-024-tab-session-kombinasi-multi-filter-alur-search-dan-recovery
title: "Tab Session: Alur Kombinasi Search dan Filter, [Clear Field], dan Batalkan Perubahan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-72
  - TC-GS-ACTLOG-73
  - TC-GS-ACTLOG-104
  - TC-GS-ACTLOG-105
  - TC-GS-ACTLOG-106
  - TC-GS-ACTLOG-107
  - TC-GS-ACTLOG-109
  - TC-GS-ACTLOG-110
  - TC-GS-ACTLOG-111
  - TC-GS-ACTLOG-112
coverage:
  web: automated
---

# Tab Session: Alur Kombinasi Search dan Filter, [Clear Field], dan Batalkan Perubahan

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat data log Session bervariasi

## Test Steps

### Alur Kombinasi Search & Filter
1. Buka Tab Session, ketik 'Budi' di kotak Search lalu Enter, kemudian buka Filter Panel, pilih Activity 'Login', klik [Apply].
2. Verifikasi tabel menampilkan hasil irisan (Login milik Budi) dan kata kunci 'Budi' tetap ada di search box.
3. Uji alur sebaliknya: terapkan filter Activity 'Login' terlebih dahulu, lalu masukkan Search 'Budi', verifikasi hasil irisan sama.
4. Terapkan Search, Filter, Sort User, dan page size 25 secara bersamaan, verifikasi seluruh kontrol aktif bersama.
### Independensi Clear & Ganti Sort
5. Buka Filter Panel, klik tombol [Clear Field], lalu klik [Apply].
6. Verifikasi saringan filter terlepas, namun pencarian 'Budi' dan sort User tetap aktif menyaring tabel.
7. Kosongkan search box lalu tekan Enter: verifikasi pencarian terlepas tanpa membatalkan filter aktif.
8. Ganti kolom sort saat search dan filter aktif: verifikasi sort berpindah tanpa mereset search atau filter.
### Pembatalan Filter & Keyboard Operability
9. Buka Filter Panel, ubah opsi filter tanpa klik [Apply], klik di luar panel untuk menutup: verifikasi perubahan dibuang.
10. Sembunyikan kolom Position via Setup Column: verifikasi filter Position yang sedang aktif tidak terbatalkan.
11. Operasikan Filter Panel menggunakan keyboard (Tab, Panah, Spasi, Enter, Esc), verifikasi seluruh kontrol dapat dioperasikan.

## Notes

- Interaksi antar-kontrol tabel bersifat terisolasi dan dapat dikombinasikan secara fleksibel.
