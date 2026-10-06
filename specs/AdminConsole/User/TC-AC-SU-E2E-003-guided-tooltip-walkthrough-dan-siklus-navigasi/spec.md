---
id: TC-AC-SU-E2E-003-guided-tooltip-walkthrough-dan-siklus-navigasi
title: "Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-228
  - TC-AC-SU-229
  - TC-AC-SU-267
  - TC-AC-SU-268
coverage:
  web: automated
---

# Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation

## Prerequisites

- Login sebagai Role: Principal Total Control
- Flag `guided_tooltip_seen_ac-settings-user` belum pernah di-set (`false`) untuk sesi kunjungan pertama

## Test Steps

### Auto-Trigger Kunjungan Pertama dan Verifikasi 5 Step

1. Buka halaman `Admin Console > Settings > User` pada sesi dengan flag kunjungan pertama
2. Verifikasi Guided Tooltip walkthrough otomatis muncul menunjuk target elemen Step 1: target Group Sidebar dengan title `"Group Sidebar"`
3. Verifikasi tombol `[Back]` berstatus Hidden pada Step 1 dan tombol `[Next]` tampil
4. Klik `[Next]`, verifikasi berpindah ke Step 2: target Toolbar Search & Filter Bar dengan title `"Search & Filters"` dan tombol `[Back]` kini tampil
5. Klik `[Next]`, verifikasi berpindah ke Step 3: target Switch Active kolom tabel dengan title `"Portal Access Switch"`
6. Klik `[Next]`, verifikasi berpindah ke Step 4: target kolom Role dengan title `"Role Summary"`
7. Klik `[Next]`, verifikasi berpindah ke Step 5: target kolom Row Action `[⋯]` dengan title `"User Actions"` dan tombol `[Next]` berubah menjadi `[Done]`
8. Klik tombol `[Done]`, verifikasi walkthrough tertutup dan flag `guided_tooltip_seen_ac-settings-user` tersimpan `true`

### Kunjungan Kedua dan Manual Replay

1. Muat ulang halaman User List
2. Verifikasi walkthrough TIDAK muncul secara otomatis pada kunjungan kedua
3. Klik tombol icon bantuan `[?]` di header halaman
4. Verifikasi walkthrough mulai ulang dari Step 1
5. Klik tombol `[Skip]` (atau klik pada area overlay gelap), verifikasi walkthrough langsung tertutup

### Navigasi Keyboard dan Exit Tanpa Selesai

1. Buka kembali walkthrough via tombol `[?]` dan fokuskan tooltip box via keyboard (Tab)
2. Tekan tombol `Enter` pada keyboard, verifikasi walkthrough maju ke step berikutnya (setara `[Next]`)
3. Tekan tombol `←` (Left Arrow) pada keyboard, verifikasi walkthrough mundur ke step sebelumnya (setara `[Back]`)
4. Tekan tombol `Esc` pada keyboard, verifikasi walkthrough tertutup (setara `[Skip]`)

## Notes

- Walkthrough Guided Tooltip membantu admin baru memahami layout 3 zona di halaman User List.
- Resize viewport atau navigasi keluar secara mendadak tidak menandai flag seen sebagai true.
