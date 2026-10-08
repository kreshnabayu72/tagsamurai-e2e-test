---
id: TC-AC-SG-E2E-047-table-search-cycle-dan-scope-lokal
title: "Siklus lengkap Search Box toolbar (reveal, focus, submit Enter, clear, collapse) dan cakupan pencarian lokal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-89
  - TC-AC-SG-90
  - TC-AC-SG-91
  - TC-AC-SG-154
coverage:
  web: automated
---

# Siklus lengkap Search Box toolbar (reveal, focus, submit Enter, clear, collapse) dan cakupan pencarian lokal

## Prerequisites

- Login sebagai Role: Total Control
- Dataset group bervariasi; node `"Region A"` terpilih di sidebar

## Test Steps

### Siklus Interaksi Search Box Toolbar
1. Hover pada icon Search di toolbar tabel utama, verifikasi kemunculan tooltip
2. Klik icon Search, verifikasi search bar melebar, kursor otomatis fokus, dan placeholder `"Search group..."` tampil
3. Ketik keyword `"Region"`, verifikasi tombol clear `(✕)` muncul dan tabel BELUM tersaring (bukan live-as-you-type)
4. Tekan tombol `Enter` pada keyboard
5. Verifikasi tabel utama kini tersaring menampilkan group yang cocok
6. Klik tombol `(✕)`, verifikasi teks terhapus tapi tabel TIDAK LANGSUNG RESET sebelum Enter ditekan
7. Tekan `Enter` pada input kosong, verifikasi tabel kembali ter-reset
8. Klik tombol collapse `(←)`, verifikasi search bar menguncup kembali ke icon
### Cakupan Pencarian & Negatif Kolom Date
9. Buka search bar dan ketik nilai tanggal Last Updated (contoh: `"2026-09"`), lalu tekan Enter
10. Verifikasi tidak ada data yang cocok (kolom Last Updated eksklusif untuk Filter Panel, Must NOT di Search)
### Pencarian Lokal terhadap Node Terpilih
11. Klik node `"Region A"` di sidebar
12. Ketik nama group yang berada di luar subtree Region A, lalu tekan Enter
13. Verifikasi hasil pencarian kosong (pencarian beroperasi lokal di dalam scope node sidebar aktif)

## Notes

- Pencarian tabel utama beroperasi dengan mekanisme explicit submit-on-enter (prd-conventions.md §9.4).
