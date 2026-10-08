---
id: TC-GS-DIV-E2E-051-tabel-utama-search-toolbar-mekanisme-dan-enter
title: "Pencarian Tabel Utama: Perilaku Toolbar Search, Ekspansi, Auto-Focus, Icon Clear X, Panah Kembali, dan Eksekusi Enter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-141
  - TC-GS-DIV-142
  - TC-GS-DIV-143
coverage:
  web: automated
---

# Pencarian Tabel Utama: Perilaku Toolbar Search, Ekspansi, Auto-Focus, Icon Clear X, Panah Kembali, dan Eksekusi Enter

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi data divisi (TC-GS-DIV-30)
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Search Toolbar: reveal, auto-focus, tooltip, icon clear, dan submit lewat Enter (TC-GS-DIV-141)

1. Hover icon Search
2. Klik icon Search
3. Ketik `Fin` pada kotak Search
4. Perhatikan tabel sebelum Enter
5. Tekan Enter
6. Verifikasi Tooltip icon Search tampil
7. Verifikasi Search bar melebar, kursor auto-focus di input, placeholder `Search division name or code...`
8. Verifikasi Setelah mengetik, icon `(✕)` muncul di dalam input dan tabel belum tersaring
9. Verifikasi Setelah Enter tabel tersaring: hanya baris `Finance` (Name `Finance`, Code `FIN`) yang tampil

### Search Toolbar: icon clear mengosongkan input tanpa mereset tabel hingga Enter (TC-GS-DIV-142)

10. Klik icon Search, ketik `Fin`, tekan Enter
11. Klik icon `(✕)`
12. Perhatikan tabel
13. Tekan Enter pada input kosong
14. Verifikasi Klik `(✕)` mengosongkan input, search bar tetap terbuka dan kursor tetap fokus
15. Verifikasi Tabel tetap menampilkan hasil search terakhir (belum reset)
16. Verifikasi Enter pada input kosong mereset tabel ke seluruh data

### Search Toolbar: icon panah kembali menutup search dan mereset tabel langsung (TC-GS-DIV-143)

17. Klik icon Search, ketik `Fin`, tekan Enter
18. Klik icon panah `(←)` di kiri toolbar
19. Verifikasi Kotak pencarian menutup menjadi icon Search biasa dan keyword dikosongkan
20. Verifikasi Tabel langsung kembali menampilkan seluruh data tanpa menekan Enter

## Notes

- Memvalidasi mekanika interaksi Search Toolbar (FI-10): expand search bar saat diklik, kursor auto-focus, tooltip icon, tombol clear (✕) mengosongkan teks tanpa mereset tabel sebelum Enter, panah kembali (←) menutup kotak dan langsung mereset tabel, dan eksekusi penyaringan hanya saat Enter ditekan (tanpa debounce) (PRD §4.1.1, §4.4, §5).
- Sumber pemetaan test case granular: TC-GS-DIV-141, TC-GS-DIV-142, TC-GS-DIV-143.
