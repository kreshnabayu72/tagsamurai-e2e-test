---
id: TC-GS-DIV-E2E-007-guided-tooltip-walkthrough-keyboard-resize-dan-role-gating
title: "Guided Tooltip Walkthrough: Navigasi Keyboard, Pembatalan Flag saat Resize, dan Pelompataan Step per Hak Akses"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-15
  - TC-GS-DIV-16
  - TC-GS-DIV-17
coverage:
  web: automated
---

# Guided Tooltip Walkthrough: Navigasi Keyboard, Pembatalan Flag saat Resize, dan Pelompataan Step per Hak Akses

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control dan Read Only
- Flag guided_tooltip_seen_gs-division belum ada untuk akun uji
- Akun uji: Total Control dan Read Only
- Flag `guided_tooltip_seen_gs-division` belum ada untuk akun ini

## Test Steps

### Resize viewport atau pindah halaman di tengah walkthrough tidak menyimpan flag seen (TC-GS-DIV-15)

1. Buka Tab Division untuk kunjungan pertama
2. Ubah ukuran viewport browser saat Step 1 tampil
3. Muat ulang halaman
4. Pindah ke Tab Position saat walkthrough tampil
5. Kembali ke Tab Division
6. Verifikasi Resize menutup walkthrough tanpa menyimpan flag `seen`
7. Verifikasi Pada kunjungan berikutnya walkthrough muncul lagi otomatis dari Step 1

### Keyboard pada walkthrough: Esc, Enter, panah kanan, panah kiri (TC-GS-DIV-16)

8. Buka Tab Division untuk kunjungan pertama
9. Tekan Enter
10. Tekan panah kanan
11. Tekan panah kiri
12. Tekan Esc
13. Verifikasi Tooltip mendapat keyboard focus saat aktif
14. Verifikasi Enter dan panah kanan = Next, panah kiri = Back
15. Verifikasi Esc = Skip: walkthrough tertutup dan flag `seen` tersimpan

### Step Add Division dilewati bagi aktor tanpa capability Create (TC-GS-DIV-17)

16. Buka Tab Division untuk kunjungan pertama
17. Klik `[Next]` pada tiap step sampai selesai
18. Verifikasi Tombol `[+ Division]` Hidden sehingga step `Add Division` dilewati
19. Verifikasi Walkthrough hanya memuat step `Division Table` dan `Changelog Audit`

## Notes

- Memvalidasi kontrol keyboard pada walkthrough (Esc, Enter, panah kanan, panah kiri), proteksi viewport resize/pindah halaman agar tidak menyimpan flag seen prematur, dan pelompataan Step 1 (+ Division) bagi pengguna dengan peran tanpa hak akses Create (PRD §4.7).
- Sumber pemetaan test case granular: TC-GS-DIV-15, TC-GS-DIV-16, TC-GS-DIV-17.
