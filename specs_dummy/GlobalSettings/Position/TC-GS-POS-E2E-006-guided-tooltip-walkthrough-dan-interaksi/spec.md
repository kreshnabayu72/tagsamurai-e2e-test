---
id: TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi
title: "Guided Tooltip walkthrough 3-step, navigasi keyboard, resize, dan dismiss/replay"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-16
  - TC-GS-POS-17
  - TC-GS-POS-18
  - TC-GS-POS-19
  - TC-GS-POS-20
  - TC-GS-POS-21
  - TC-GS-POS-22
  - TC-GS-POS-23
  - TC-GS-POS-24
coverage:
  web: automated
---

# Guided Tooltip walkthrough 3-step, navigasi keyboard, resize, dan dismiss/replay

## Prerequisites

- Akun aktor Total Control dan Read Only dengan flag guided_tooltip_seen_gs-position belum diset (kunjungan pertama)

## Test Steps

### Walkthrough Otomatis & Step Content

1. Buka Global Settings > User > Position dengan akun baru
2. Verifikasi walkthrough otomatis aktif di Step 1: spotlight mengarah ke Table Tools, judul "Table Tools", indikator "Step 1 of 3", tombol "[Skip]" dan "[Next]" muncul, tombol "[Back]" tersembunyi
3. Klik "[Next]", verifikasi berpindah ke Step 2: spotlight mengarah ke Position Table, judul "Position Table", indikator "Step 2 of 3", tombol "[Back]" dan "[Next]" muncul
4. Klik "[Next]", verifikasi berpindah ke Step 3: spotlight mengarah ke ikon Changelog, judul "Changelog Audit", indikator "Step 3 of 3", tombol "[Next]" berubah menjadi "[Done]"
5. Klik "[Back]" dan verifikasi kembali ke Step 2

### Navigasi Keyboard dan Aksesibilitas

6. Tekan tombol panah kanan (→), verifikasi berpindah ke Step 3
7. Tekan tombol panah kiri (←), verifikasi kembali ke Step 2
8. Tekan tombol Esc, verifikasi walkthrough tertutup

### Replay via Tombol [?]

9. Buka kembali tab Position, verifikasi walkthrough tidak muncul otomatis lagi
10. Klik tombol "[?]" di samping breadcrumb
11. Verifikasi walkthrough terbuka kembali mulai dari Step 1
12. Klik tombol "[Skip]", verifikasi walkthrough tertutup dan kunjungan berikutnya tetap tidak muncul otomatis

### Parity Role Read Only

13. Login sebagai Role: Read Only yang belum pernah membuka tab Position
14. Buka tab Position
15. Verifikasi walkthrough menampilkan konten 3 step yang sama persis (Step 1 Table Tools, Step 2 Table, Step 3 Changelog)

## Notes

- Menggabungkan TC-GS-POS-16 s.d. 24 untuk pengujian menyeluruh sistem bantuan Guided Tooltip.
